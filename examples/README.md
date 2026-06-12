# Examples

Transcripts of the skill in use: a real question in, the diagnostic format out. These serve two purposes.

**Few-shot anchoring.** Models loading `luck.md` produce far more consistent diagnostics when they have seen the format executed, not just specified. If you extend the skill, add your transcripts here.

**Prospective evidence.** The framework's worked examples in `THEORY.md` are retrodictions -- history read backward. The only way the framework accumulates real evidence is diagnoses recorded *before* outcomes are known. Each example file ends with an `Outcome` section, initially marked `pending`. Revisit and fill it in. A diagnosis whose recommended action was followed and whose predicted failure mode then materialized (or didn't) is worth more than any historical narrative.

## Format

One file per diagnosis:

```
example-<slug>.md
  ## Context        - the question as asked, plus relevant facts
  ## Diagnostic     - the standard output format from luck.md
  ## Outcome        - pending | what actually happened, dated
```
