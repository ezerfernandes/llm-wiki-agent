---
title: "d-Separation"
type: concept
tags: [probabilistic-modeling, graphical-models, foundational]
sources: [mml-ch08-when-models-meet-data, mml-book]
last_updated: 2026-06-04
---

# d-Separation

The graph-topological criterion for reading **[[ConditionalIndependence|conditional independence]] directly off a [[DirectedGraphicalModel|directed graphical model]]** ([[mml-book]] §8.5.2, p. 281; d-separation due to Pearl 1988). It lets us decide, purely by inspecting the DAG, whether a statement "$\mathcal{A}$ is conditionally independent of $\mathcal{B}$ given $\mathcal{C}$" — written $\mathcal{A}\perp\!\!\!\perp\mathcal{B}\,|\,\mathcal{C}$ (Eq. 8.34) — is implied by the graph.

## The blocking rules

For disjoint node-sets $\mathcal{A},\mathcal{B},\mathcal{C}$, consider **all trails** (paths that ignore arrow direction) from any node in $\mathcal{A}$ to any node in $\mathcal{B}$. A trail is **blocked** if it contains a node such that **either**:

1. the arrows meet **head-to-tail or tail-to-tail** at the node **and** the node is **in** $\mathcal{C}$; **or**
2. the arrows meet **head-to-head** at the node **and** **neither the node nor any of its descendants** is in $\mathcal{C}$.

If **all** trails are blocked, $\mathcal{A}$ is **d-separated** from $\mathcal{B}$ by $\mathcal{C}$, and the joint distribution satisfies $\mathcal{A}\perp\!\!\!\perp\mathcal{B}\,|\,\mathcal{C}$.

## Worked example (Fig. 8.11)

For the DAG $a\to b\to c$ with $a\to d$, $b\to d$, $c\to d$, $d\to e$ ([[mml-book]] Example 8.9):

- $b\perp\!\!\!\perp d\,|\,a,c$ (Eq. 8.35)
- $a\perp\!\!\!\perp c\,|\,b$ (Eq. 8.36)
- $b\not\perp\!\!\!\perp d\,|\,c$ (Eq. 8.37)
- $a\not\perp\!\!\!\perp c\,|\,b,e$ (Eq. 8.38)

The last is the key subtlety: conditioning on the **descendant** $e$ of a head-to-head ("collider") node *un*-blocks a path — the **"explaining away"** phenomenon (independent causes of a common effect become dependent once the effect, or a descendant of it, is observed).

## Connections

- [[mml-ch08-when-models-meet-data]] — §8.5.2 canonical reference (Eqs. 8.34–8.38).
- [[mml-book]] — §8.5.2.
- [[ConditionalIndependence]] — what d-separation certifies.
- [[DirectedGraphicalModel]] / [[BayesianNetwork]] — the graphs d-separation operates on.
- [[StatisticalIndependence]] — the unconditional special case ($\mathcal{C}=\emptyset$).
