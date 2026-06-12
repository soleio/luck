# Example: Internal Knowledge-Base Chatbot

## Context

**User:** Our ops team wants me to build an internal chatbot over our company wiki and SOPs. Leadership is excited, I have two weeks of slack time to build a prototype, and the wiki is... not great -- maybe 60% of it is current. Is this worth building?

Relevant facts surfaced during the conversation: the wiki has no owner and no update process; the ops team currently answers repeated questions in a shared inbox; the company has an existing M365/Copilot license that nobody has evaluated for this use case.

## Diagnostic

### Luck Diagnostic: internal knowledge-base chatbot

| # | Facet | Verdict | Evidence |
|---|-------|---------|----------|
| 1 | Solvency | FAIL | The bot's substrate (the wiki) is already decaying -- 40% stale with no owner and no update process. A bot built on it inherits the decay rate and adds its own maintenance cost. |
| 2 | Gradient coupling | PASS | Two active gradients exist today: a measurable stream of repeated questions hitting the ops inbox, and leadership attention with budget authority behind it. |
| 3 | Structural compatibility | PASS | A chat interface over existing content requires no new behavior from askers; they already ask these questions, just at the wrong endpoint. |
| 4 | Niche construction | AT RISK | A feedback loop is possible -- failed answers could flag stale pages and drive wiki repair -- but nothing in the prototype plan builds it. As scoped, usage does not improve the substrate. |
| 5 | Circulation | AT RISK | Answers flow out to askers, but nothing returns: no signal back to wiki authors about what is missing or wrong. One-directional as scoped. |
| 6 | Integration | AT RISK | The bot would couple the wiki to daily ops work (good), but the existing unevaluated Copilot license means a parallel, competing path may already exist -- building a second one fragments rather than integrates. |
| 7 | Path sensitivity | PASS | Precursors exist (wiki, license, demand), the window is open, and no incumbent occupies the niche internally. |

**Binding constraint:** Solvency -- a bot over a decaying, ownerless corpus will answer confidently from stale content, burn trust, and then require you to maintain both the bot and the wiki.

**Failure mode match:** Institutional zombie (projected) -- if shipped as scoped, it will persist on leadership enthusiasm while its gradient (accurate content) depletes underneath it.

**Recommended action:** Spend the two weeks on the constraint, not the bot. Propose: (1) a wiki ownership and review process, established first; (2) the bot scoped so that every unanswerable or wrongly-answered question automatically files a content-repair task -- making the bot the wiki's niche-construction engine rather than its parasite; (3) a one-day evaluation of the existing Copilot license before building anything custom. If leadership won't fund (1), decline (2).

## Outcome

Pending.
