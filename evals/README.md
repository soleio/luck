# Eval Harness

The framework states its own falsification condition: if it does not produce measurably better outputs, it is -- by its own logic -- insolvent. This directory is the test.

## What it measures

**Prediction 7 (reflexive, from THEORY.md):** responses to strategic-decision prompts generated *with* `luck.md` loaded as a system prompt should be preferred by blinded judges over responses generated *without* it.

This is deliberately the cheapest prediction to test. It does not validate the framework's historical claims or its facet ordering -- only whether loading the skill improves the artifact a user actually receives. That is the bar a skill file must clear to justify its context-window cost.

## Protocol

1. **Prompts.** `prompts.json` contains 12 strategic-decision prompts spanning product, career, open source, organizational design, content strategy, and research direction. Each is the kind of question the skill's frontmatter claims to handle.
2. **Paired generation.** For each prompt, generate two responses from the same model: one with `luck.md` as the system prompt, one with a minimal generic system prompt ("You are a thoughtful strategic advisor."). The generic baseline matters -- comparing against *no* system prompt would confound the skill's content with the mere presence of an advisor framing.
3. **Blinded pairwise judging.** A judge model receives both responses labeled A and B, with the assignment randomized per pair (seeded, reproducible). The judge never sees which condition produced which response, scores both against `judge-rubric.md`, and returns a structured verdict.
4. **Scoring.** Report the skill's win rate with the tie count, per-criterion score deltas, and the judge's reasoning per pair. With n=12, treat the result as directional: a 9-3 split is signal, a 7-5 split is noise. Extend `prompts.json` before drawing strong conclusions.

## Known limitations

- **Judge bias.** LLM judges favor longer, more structured responses. The rubric explicitly instructs against length preference, but the bias is not fully removable. A skeptical reading should discount narrow wins.
- **Same-family judge.** Generation and judging both use Claude by default. A judge from the same model family may share stylistic preferences with the generator. For stronger evidence, re-judge with a different model family and compare.
- **Single-turn only.** The skill claims value in multi-turn strategic conversations; this harness tests single-turn responses only.
- **n=12.** Directional, not conclusive. The harness is built to make extending the prompt set trivial.

## Running it

Requires Python 3.10+, the `anthropic` package, `pydantic`, and an `ANTHROPIC_API_KEY` in the environment.

```
pip install anthropic pydantic
python run_eval.py                          # full run, default models
python run_eval.py --limit 3                # quick smoke test on 3 prompts
python run_eval.py --judge-model claude-sonnet-4-6
python run_eval.py --seed 7                 # different blinding assignment
```

Results are written to `results/results-<timestamp>.json` (full transcripts + verdicts) and a summary is printed to stdout. The skill file is sent with a prompt-cache breakpoint, so the 12 with-skill generations share one cached prefix.
