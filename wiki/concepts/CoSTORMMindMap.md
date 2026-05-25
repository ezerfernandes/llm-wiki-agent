---
title: "Co-STORM Mind Map"
type: concept
tags: [data-structure, multi-agent, information-organization]
sources: [2408.15232-co-storm]
last_updated: 2026-05-22
---

# Co-STORM Mind Map

The **dynamic mind map** $\mathcal{M} = (\mathcal{C}, \mathcal{E})$ maintained by [[CoSTORM|Co-STORM]] to track the discourse and act as **shared conceptual space** between user and system. Introduced in [[2408.15232-co-storm]] §3.2; inspired by [[Buzan1974|Buzan 1974]]'s mind-mapping technique and [[Roschelle1995|Roschelle & Teasley 1995]]'s notion of *shared knowledge* in collaborative problem solving.

## Structure

- $\mathcal{C}$ — set of concepts (nodes); each concept $c$ has associated retrieved information $I^c \subset \mathcal{I}$.
- $\mathcal{E}$ — directed parent-child edges encoding latent topic-subtopic relationships (e.g., *Drug Discovery Acceleration* is a subtopic of *Impact and Applications*).
- Each piece of retrieved info is also associated with the **question that led to its retrieval** — intent-driven organization.

## Operations

### `insert`
Place a piece of information under the most appropriate concept by:
1. **Candidate selection** via embedding similarity between the info's associated question and each existing concept name in $\mathcal{C}$.
2. **Final placement** by prompting the LM with the candidates to pick the best fit.

### `reorganize`
Triggered when a concept exceeds **$K = 10$** pieces of information:
1. Prompt the LM to generate a list of new subtopic names under $c$.
2. Apply `insert` to place each piece of $I^c$ into the new subtree rooted at $c$.

### Bottom-up cleaning
After expansion:
- Delete concepts with **no supporting info**.
- Collapse concepts that have **only one subtopic** (i.e., flatten degenerate chains).

## Roles in the system

1. **Tracking the discourse** — the live mind map gives the user an at-a-glance view of what the agents have covered. Per the human evaluation, **80 mind-map snapshots** were judged as accurately tracking the discourse **71% of the time**.
2. **Reducing user cognitive load** — users do not need to remember every utterance; the mind map curates it.
3. **Outline for the final cited report** — when the user requests a takeaway document, Co-STORM generates the long-form report section-by-section using $\mathcal{M}$ as outline and $I^c$ as the per-section retrieval context.

## Why a tree (not a flat list or graph)

A flat list saturates user attention as the discourse grows; a general graph is hard to render legibly. A bounded-depth, bounded-fanout **tree** matches the human mental-model intuition behind mind-mapping ([[Buzan1974]]). The `reorganize` operation keeps fanout from exploding.

## See also
- [[CoSTORM]] · [[CollaborativeDiscourse]] · [[InformationOrganization]]
