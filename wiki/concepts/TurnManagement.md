---
title: "Turn Management (Co-STORM)"
type: concept
tags: [discourse, multi-agent]
sources: [2408.15232-co-storm]
last_updated: 2026-05-22
---

# Turn Management

The **turn-management protocol** in [[CoSTORM|Co-STORM]] determines *which agent speaks next* in the multi-party discourse. The protocol implements [[MixedInitiativeDiscourse|mixed-initiative]] dialogue ([[Traum2003|Traum 2003]]).

## The protocol

At each timestep $i$:

1. **If the user has taken the turn** (injected an utterance $u$): use $u$ as a query to retrieve information; prompt the LM to obtain an updated list of experts $\mathcal{P}'$; switch back to auto-steering mode.
2. **Otherwise**: pick the next expert from $\mathcal{P} = \{p_1, ..., p_N\}$ in **round-robin** order to generate the utterance.
3. **Override**: if the last $L$ consecutive turns have intents in {Potential Answer, Further Details}, *override* the round-robin pick and invoke the [[ModeratorAgent|moderator]] instead.

## Hyperparameter

- $L = 2$ in Co-STORM's default config.

## Why the override exists

Without the override, experts who have just been answering a question tend to keep elaborating (intent = Further Details), and the discourse collapses into a deep but narrow rabbit hole. The override forces a redirection turn by the moderator, which surfaces **on-topic but unexplored** material (see [[ModeratorAgent]] for the reranking formula).

## Connection to dialogue theory

Per [[Traum2003|Traum 2003]]'s framework, dialogue systems can be:

- **User-initiative only** — e.g., a [[QASystem|QA system]] where the user asks and the system answers.
- **System-initiative only** — e.g., [[STORM]], which decides everything itself.
- **Mixed-initiative** — both can take initiative; control passes back and forth.

Co-STORM is mixed-initiative: the user *can* take a turn anytime, but is not *required* to. When the user is idle, the system auto-steers via the round-robin + override protocol. The user controls who-takes-initiative.

## See also
- [[CoSTORM]] · [[UtteranceIntent]] · [[ModeratorAgent]] · [[MixedInitiativeDiscourse]]
