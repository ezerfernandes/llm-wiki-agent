---
title: "Pareto Optimization"
type: concept
tags: [optimization, methodology, multi-objective]
sources: [ai-engineering-ch04-evaluate-ai-systems]
last_updated: 2024-12-04
---

# Pareto Optimization

**Optimizing across multiple objectives simultaneously**, surfacing the Pareto frontier of solutions that aren't dominated by any other in all dimensions. Per [[ai-engineering-ch04-evaluate-ai-systems|*AI Engineering* Ch 4]], Pareto optimization is the natural framing for model-selection trade-offs:

> "A model that generates high-quality outputs but is too slow and expensive to run will not be useful. … Optimizing for multiple objectives is an active field of study called Pareto optimization."

## The practical recipe (Ch 4)

> "When optimizing for multiple objectives, it's important to be clear about what objectives you can and can't compromise on. For example, if latency is something you can't compromise on, you start with latency expectations for different models, filter out all the models that don't meet your latency requirements, and then pick the best among the rest."

This is the **lexicographic** flavor of Pareto optimization — pick one hard constraint, filter, then optimize within the survivors.

## Typical AI-engineering objectives

- **Quality** — accuracy, factual consistency, instruction-following.
- **Latency** — [[TTFT]] / [[TPOT]] / [[TimePerQuery]].
- **Cost** — per-token API cost or amortized compute.

The full chapter framing this lives at [[CostAndLatency]].

## Connections

- [[ai-engineering-ch04-evaluate-ai-systems]] — primary source.
- [[CostAndLatency]] — the chapter's named "balance these three" criterion.
- [[ModelSelectionWorkflow]] — where Pareto reasoning is applied.
- [[HardModelAttribute]] / [[SoftModelAttribute]] — Pareto filters are essentially hard attributes.
