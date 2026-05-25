---
title: "Collaborative Discourse"
type: concept
tags: [pedagogy, multi-agent, framing]
sources: [2408.15232-co-storm]
last_updated: 2026-05-22
---

# Collaborative Discourse

**Collaborative discourse** — multi-party conversation in which participants take *different points of view* and engage in critical discussion. The pedagogical foundation invoked by [[2408.15232-co-storm|Co-STORM (2024)]] for why LM-agent-driven discussion can foster human learning.

## Educational-psychology grounding

- **[[Nussbaum2008|Nussbaum (2008)]]** — *Collaborative discourse, argumentation, and learning: Preface and literature review.* The keystone reference. Argues not all types of collaborative discourse are equally beneficial; emphasizes the importance of **critical discussion** where participants assume different points of view.
- **[[Osborne2010]]** — *Arguing to learn in science.* Science learning depends on argumentation between divergent views.
- **[[Kolodner2007]]** — Roles of scripts in promoting collaborative discourse in learning by design.
- **[[Chinn2000]]** — Structure of discourse in collaborative learning.
- **[[Onrubia2022]]** — *Assisting teacher collaborative discourse in professional development.* Highlights the **facilitator role**: asking questions and providing complementary information are popular strategies.
- **[[Roschelle1995|Roschelle & Teasley 1995]]** — Construction of *shared knowledge* in collaborative problem solving. Cited by Co-STORM as motivation for the [[CoSTORMMindMap|mind map]] (a shared conceptual space).

## Operationalized in Co-STORM

[[2408.15232-co-storm|Co-STORM]] instantiates the collaborative-discourse model with:

- **[[PerspectiveGuidedExpert|Perspective-guided experts]]** $p_1, ..., p_N$ — multiple agents with distinct viewpoints, fulfilling the Nussbaum requirement for *different points of view*.
- **[[ModeratorAgent|Moderator agent]]** — the *facilitator* in Onrubia's sense; asks questions and surfaces complementary information.
- **[[CoSTORMMindMap|Mind map]]** — the *shared knowledge* substrate in Roschelle & Teasley's sense.
- **Mixed-initiative [[TurnManagement|turn management]]** — user can take turns but is not required to, matching the educational scenario of a student observing then engaging with expert discourse.

## Implications for LM-system design

Where pure-QA systems treat the user as the **sole question source**, collaborative-discourse-style systems distribute question-asking across LM agents. This:

- Reduces user **cognitive load** (less mental effort to formulate questions in unfamiliar domains).
- Surfaces [[UnknownUnknowns|unknown unknowns]] via perspective diversity.
- Risks **echo chambers** if all agents share a model bias — Co-STORM's perspective-guidance and moderator-reranking are the mitigations.

## See also
- [[CoSTORM]] · [[UnknownUnknowns]] · [[ModeratorAgent]] · [[PerspectiveGuidedExpert]] · [[CoSTORMMindMap]] · [[MixedInitiativeDiscourse]]
