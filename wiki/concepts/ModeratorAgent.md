---
title: "Moderator Agent (Co-STORM)"
type: concept
tags: [multi-agent, llm-role, information-seeking]
sources: [2408.15232-co-storm]
last_updated: 2026-05-22
---

# Moderator Agent

The **moderator agent** in [[CoSTORM|Co-STORM]] — a non-expert LM-played role that **steers the discourse toward unexplored regions** by reranking **uncited / unused** search results from prior expert turns and generating a new question grounded in them.

## When the moderator speaks

Triggered by the [[TurnManagement|turn-management protocol]]: after $L = 2$ consecutive expert turns with intent in {Potential Answer, Further Details}, Co-STORM asks the moderator to intervene. This prevents the discourse from collapsing into a deep but narrow chain of niche follow-ups.

The user can also explicitly *request* a moderator turn.

## How the moderator chooses what to say

Given the set of uncited sources $\mathcal{I}_{\text{uncited}}$ retrieved since the last moderator turn, each source $i$ is scored:

$$\text{score}(i) = \cos(\mathbf{i}, \mathbf{t})^\alpha \cdot (1 - \cos(\mathbf{i}, \mathbf{q}))^{1-\alpha}$$

— where $\mathbf{t}$ is the topic embedding, $\mathbf{q}$ is the embedding of the question that originally retrieved $i$, and $\alpha = 0.5$ in Co-STORM's default config. The score rewards sources that are **on-topic** ($\cos(\mathbf{i}, \mathbf{t})$ high) but **dissimilar to the original question** ($1 - \cos(\mathbf{i}, \mathbf{q})$ high) — i.e., **on-topic but unexplored**.

The top-ranked sources are concatenated with the current concept-name set $\mathcal{C}$ from the [[CoSTORMMindMap|mind map]] (to avoid repetitive concepts) and given to the LM to generate:

1. An informed **question** that opens a new direction.
2. An **updated expert list** $\mathcal{P}'$ — if the new direction calls for different perspectives, the moderator can adjust who participates.

The moderator's utterance is then run through a **polish utterance** step (also applied to expert turns) to make it chatty and engaging.

## Why it's load-bearing

The Co-STORM ablation table shows **removing the moderator** has a larger negative impact than reducing expert count:

| Setting | Relevance | Breadth | Depth | Novelty |
|---|---|---|---|---|
| Full Co-STORM | 3.78 | 3.79 | 3.77 | 3.05 |
| w/o Multi-Expert | 3.73 | 3.75 | 3.77 | 2.93 |
| **w/o Moderator** | **3.56** | **3.69** | **3.41** | **2.89** |

The paper's framing:

> *"the moderator role in Co-STORM raises questions based on unused information about the topic — such a role represents somebody with a much larger known unknowns, effectively steering the discourse to help users discover more in the space of their unknown unknowns."*

## Critique: not a sound critic

Per the [[2402.01817-llm-modulo|LLM-Modulo]] framing, the moderator is a **soft critic** — useful but not sound. The moderator's question generation inherits the base model's failure modes (hallucinated framings, biased perspective enumeration). Co-STORM does not claim the moderator *reliably* finds [[UnknownUnknowns|unknown unknowns]]; only that it does so often enough to improve user-facing Novelty / Depth / Engagement / Serendipity ratings.

## See also
- [[CoSTORM]] · [[PerspectiveGuidedExpert]] · [[TurnManagement]] · [[UnknownUnknowns]] · [[CoSTORMMindMap]]
