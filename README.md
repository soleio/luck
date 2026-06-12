# luck

A skill for improving the luck of your AI stack and projects -- a diagnostic framework, grounded in Assembly Theory, for why some things persist and compound while others don't, packaged as a procedure an AI model can actually execute.

## The core idea

This framework *defines* luck as something other than randomness: the rate at which an agent increases the throughput, circulation, and integration of the systems it inhabits. Under that definition, luck has structure -- and structure can be diagnosed, built, and measured. Whether the definition earns its keep is an empirical question; this repository includes the test (see `evals/`).

## What's in the box

- **[`luck.md`](luck.md)** -- the operational skill file. Seven sequential diagnostics with explicit PASS / AT RISK / FAIL anchors, a mechanical binding-constraint rule, a defined output format, a worked transcript, named failure modes, and scoped instructions for AI systems. This is what you load.
- **[`THEORY.md`](THEORY.md)** -- the conceptual foundation. Core premise, grounding in Assembly Theory and adjacent work (including where that grounding is contested), extended worked examples, and seven falsifiable predictions with explicit falsification conditions. Read it to evaluate or attack the framework; you don't need it to use the skill.
- **[`examples/`](examples/)** -- transcripts of the skill in use: real question in, diagnostic out. Each ends with an outcome section to be filled in when the outcome is known, so the repository accumulates prospective evidence rather than only retrodiction.
- **[`evals/`](evals/)** -- a blinded pairwise eval harness testing whether loading the skill measurably improves responses to strategic-decision prompts. The framework names its own falsification condition; this is the cheapest version of the test.

## Usage

Add `luck.md` to your project as a skill file or system prompt. It uses standard Markdown with YAML frontmatter and works with any frontier model that accepts structured instructions.

The skill activates on strategic and durability questions -- should I build/keep/kill X, will X last, why did X fail, which option compounds. It produces a fixed diagnostic format: a verdict per facet with evidence, the single binding constraint, a failure-mode match, and one recommended action. For everything else it stays out of the way by design.

## Repository structure

```
luck.md              <- operational skill file (load this)
THEORY.md            <- premise, grounding, predictions
examples/            <- transcripts with pending-outcome tracking
evals/               <- blinded pairwise eval harness
README.md            <- you are here
```

## Theoretical roots

Extends Assembly Theory (Marshall et al. 2021, Nature Communications; Sharma et al. 2023, Nature) with adjacent work from dissipative adaptation, the free energy principle, niche construction theory, and the adjacent possible. Assembly Theory is contested in the literature; THEORY.md states what this framework does and does not inherit from that dispute.

## Author

[soleio](https://github.com/soleio)
