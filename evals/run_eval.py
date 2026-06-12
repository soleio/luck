"""Blinded pairwise eval for the luck.md skill.

For each prompt in prompts.json, generates a response with luck.md as the
system prompt and one with a minimal generic system prompt, then has a judge
model compare the pair blind (randomized A/B assignment) against
judge-rubric.md. See README.md in this directory for the protocol and its
known limitations.
"""

import argparse
import json
import random
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Literal

import anthropic
from pydantic import BaseModel

HERE = Path(__file__).parent

BASELINE_SYSTEM = "You are a thoughtful strategic advisor."

JUDGE_INSTRUCTIONS = """\
{rubric}

---

## Question the responses are answering

{question}

## Response A

{response_a}

## Response B

{response_b}
"""


class CriterionScores(BaseModel):
    diagnostic_depth: int
    actionability: int
    persistence_reasoning: int
    falsifiable_framing: int
    fit_to_asker: int


class Verdict(BaseModel):
    scores_a: CriterionScores
    scores_b: CriterionScores
    winner: Literal["A", "B", "tie"]
    reasoning: str


def text_of(message: anthropic.types.Message) -> str:
    if message.stop_reason == "refusal":
        raise RuntimeError("model refused the request")
    return "\n".join(b.text for b in message.content if b.type == "text")


def generate(client: anthropic.Anthropic, model: str, system, prompt: str) -> str:
    with client.messages.stream(
        model=model,
        max_tokens=16000,
        thinking={"type": "adaptive"},
        system=system,
        messages=[{"role": "user", "content": prompt}],
    ) as stream:
        return text_of(stream.get_final_message())


def judge(
    client: anthropic.Anthropic,
    model: str,
    rubric: str,
    question: str,
    response_a: str,
    response_b: str,
) -> Verdict:
    response = client.messages.parse(
        model=model,
        max_tokens=8000,
        thinking={"type": "adaptive"},
        messages=[
            {
                "role": "user",
                "content": JUDGE_INSTRUCTIONS.format(
                    rubric=rubric,
                    question=question,
                    response_a=response_a,
                    response_b=response_b,
                ),
            }
        ],
        output_format=Verdict,
    )
    if response.parsed_output is None:
        raise RuntimeError("judge returned no parseable verdict")
    return response.parsed_output


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--gen-model", default="claude-opus-4-8")
    parser.add_argument("--judge-model", default="claude-opus-4-8")
    parser.add_argument("--skill-path", type=Path, default=HERE.parent / "luck.md")
    parser.add_argument("--prompts", type=Path, default=HERE / "prompts.json")
    parser.add_argument("--rubric", type=Path, default=HERE / "judge-rubric.md")
    parser.add_argument("--out-dir", type=Path, default=HERE / "results")
    parser.add_argument("--limit", type=int, help="run only the first N prompts")
    parser.add_argument("--seed", type=int, default=42, help="blinding RNG seed")
    args = parser.parse_args()

    skill_text = args.skill_path.read_text(encoding="utf-8")
    rubric = args.rubric.read_text(encoding="utf-8")
    prompts = json.loads(args.prompts.read_text(encoding="utf-8"))
    if args.limit:
        prompts = prompts[: args.limit]

    # Cache breakpoint on the skill text: all with-skill generations share
    # one cached prefix instead of re-processing the skill per prompt.
    skill_system = [
        {"type": "text", "text": skill_text, "cache_control": {"type": "ephemeral"}}
    ]

    client = anthropic.Anthropic()
    rng = random.Random(args.seed)
    results = []
    wins = {"skill": 0, "baseline": 0, "tie": 0}

    for i, item in enumerate(prompts, 1):
        print(f"[{i}/{len(prompts)}] {item['id']}", flush=True)

        with_skill = generate(client, args.gen_model, skill_system, item["prompt"])
        baseline = generate(client, args.gen_model, BASELINE_SYSTEM, item["prompt"])

        # Blind: randomize which condition is shown as A.
        skill_is_a = rng.random() < 0.5
        a, b = (with_skill, baseline) if skill_is_a else (baseline, with_skill)

        verdict = judge(client, args.judge_model, rubric, item["prompt"], a, b)

        if verdict.winner == "tie":
            outcome = "tie"
        elif (verdict.winner == "A") == skill_is_a:
            outcome = "skill"
        else:
            outcome = "baseline"
        wins[outcome] += 1
        print(f"    winner: {outcome}", flush=True)

        results.append(
            {
                "prompt_id": item["id"],
                "prompt": item["prompt"],
                "response_with_skill": with_skill,
                "response_baseline": baseline,
                "skill_shown_as": "A" if skill_is_a else "B",
                "verdict": verdict.model_dump(),
                "outcome": outcome,
            }
        )

    n = len(results)
    summary = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "gen_model": args.gen_model,
        "judge_model": args.judge_model,
        "seed": args.seed,
        "n": n,
        "skill_wins": wins["skill"],
        "baseline_wins": wins["baseline"],
        "ties": wins["tie"],
        "skill_win_rate_excl_ties": (
            wins["skill"] / (wins["skill"] + wins["baseline"])
            if wins["skill"] + wins["baseline"]
            else None
        ),
    }

    args.out_dir.mkdir(parents=True, exist_ok=True)
    out_path = args.out_dir / f"results-{time.strftime('%Y%m%d-%H%M%S')}.json"
    out_path.write_text(
        json.dumps({"summary": summary, "results": results}, indent=2),
        encoding="utf-8",
    )

    print()
    print(
        f"n={n}  skill: {wins['skill']}  baseline: {wins['baseline']}  ties: {wins['tie']}"
    )
    if summary["skill_win_rate_excl_ties"] is not None:
        print(
            f"skill win rate (excluding ties): {summary['skill_win_rate_excl_ties']:.0%}"
        )
    print(f"full results: {out_path}")
    print()
    print("Reminder: with n this small, treat the result as directional, and")
    print("re-judge with a different model family before believing a narrow win.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
