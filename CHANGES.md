# Proposed Changes to soleio/luck

Draft revision prepared 2026-06-12, based on a review of `luck.md` v1.0 and the repository README. Each change maps to a specific weakness identified in the review. Nothing of the original framework's substance was removed -- content was restructured, anchored, and made testable.

## Summary

| # | Change | Files | Review finding it addresses |
|---|---|---|---|
| 1 | Split into operational core + theory companion | `luck.md`, `THEORY.md` | ~60% of the original file was for human readers; models follow short operational docs better, and the split halves per-invocation token cost |
| 2 | PASS / AT RISK / FAIL anchors per facet | `luck.md` | Check questions had no scale; two runs of the same diagnostic produced incomparable verdicts |
| 3 | Mechanical binding-constraint rule | `luck.md` | The Quick-Reference table pivoted on "the binding constraint" but no procedure existed to identify it; conflicting facets had no resolution |
| 4 | Defined diagnostic output format | `luck.md` | No output schema meant essay one run, table the next; format also enforces "one recommended action," which is the framework's actual value |
| 5 | Worked transcript (input -> output) | `luck.md`, `examples/` | All original examples illustrated the theory; none demonstrated skill behavior. Few-shot anchoring is the single highest-leverage consistency fix |
| 6 | Scoped the "For AI Systems" section | `luck.md` | As written it applied seven checks to every output; now: full diagnostic on strategic questions, silent heuristics on artifacts, nothing on tactical queries |
| 7 | Tightened frontmatter triggers | `luck.md` | "user asks about improving their luck" fired on casual well-wishes; added explicit anti-triggers |
| 8 | Softened Prediction 2's (N-1)/N functional form | `THEORY.md` | Exact form had no derivation and silently assumed equal, independent gradients; restated as the defensible monotonic claim with the open work named |
| 9 | Labeled the Weimar claim a retrodiction | `THEORY.md` | It was presented as a prediction; added a general "Note on Retrodiction" section covering all worked examples |
| 10 | Acknowledged Assembly Theory is contested; corrected citations | `THEORY.md`, `README.md` | Original cited "Cronin & Marshall 2021" as settled science; now cites Marshall et al. 2021 (Nat. Comms) and Sharma et al. 2023 (Nature) and states the framework's claims don't depend on AT winning its disputes |
| 11 | Reframed "luck is a fundamental force" as a definitional move | `luck.md`, `THEORY.md` | The metaphysical claim was the framework's most quotable weakness and nothing downstream needed it |
| 12 | Marked the failure taxonomy as non-exhaustive | `luck.md`, `THEORY.md` | Seven facets x three ratings generate far more states than seven named patterns; diagnostics may now answer "none" instead of forcing a fit |
| 13 | Added Prediction 7 (reflexive) + eval harness | `THEORY.md`, `evals/` | The framework stated its falsification condition but never ran the test; the harness implements the cheapest version (blinded pairwise judging, 12 prompts) |
| 14 | examples/ directory with outcome tracking | `examples/` | Converts the repo from retrodiction-only to a vehicle for prospective evidence; each diagnosis records an Outcome section filled in later |
| 15 | Rewrote README around the new structure | `README.md` | Points users at the operational file vs. theory file; tones down the "civic, moral, perhaps divine duty" framing, which undercut the falsifiability positioning |

## Repository hygiene

- **Version bump and changelog.** The frontmatter now says 1.1; if these changes are adopted, a CHANGELOG entry should record the 1.0 -> 1.1 restructuring, since the diagnostic anchors change what existing users' outputs look like.

## What was deliberately preserved

- All seven facets, their ordering, and the dependency hierarchy (assembly -> ecology).
- The full failure-mode table with original names and examples.
- All five original worked examples (moved to THEORY.md, with the reflexive one updated to reference the eval harness).
- The six original predictions (Prediction 2 softened, all else verbatim or lightly edited).
- The theoretical grounding section and all four adjacent-theory citations.
- The closing "geometry" passage, including "the luckiest agent is not the one standing where gradients converge but the one actively widening the flow."
