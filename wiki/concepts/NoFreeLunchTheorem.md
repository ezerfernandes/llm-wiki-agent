---
title: "No Free Lunch Theorem"
type: concept
tags: [learning-theory, foundational]
sources: [2605.12966-agentic-ai-to-agi]
last_updated: 2026-05-15
---

# No Free Lunch Theorem

Wolpert & Macready (1997) showed that, averaged over *all* possible problem instances, no learning or optimization algorithm outperforms any other. Concretely: for any pair of algorithms $A$, $B$ and any performance measure averaged uniformly over the space of all $f:\mathcal{X}\to\mathcal{Y}$, $A$ and $B$ achieve identical expected performance.

## Role as a baseline

The NFL theorem is the standard rebuttal to "universal AGI from one algorithm + scale alone": without *some* structural assumption on the data-generating distribution, no learner generalizes better than chance on a uniformly-random task. Every meaningful generalization result therefore prices in a prior.

## In the corpus

[[2605.12966-agentic-ai-to-agi]] (§1) cites the NFL theorem as the entry point for its central move: real-world data is *not* uniformly random, so the right question is *which prior* to commit to. The paper's answer is the [[StructuredRealWorldDistribution]] — support concentrated on a union of low-dimensional manifolds. Under that prior, the [[CurseOfDimensionality]] applies only to the *ambient* dimension $D$; the *intrinsic* per-task dimension $d_k \ll D$ is what matters, which is what powers the exponential sample-efficiency gain of [[RoutingBasedAgenticAI]] and [[AgenticAI]] over a monolithic learner.

## Connections
- [[2605.12966-agentic-ai-to-agi]]
- [[StructuredRealWorldDistribution]]
- [[CurseOfDimensionality]]
