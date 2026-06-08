---
title: "Switch Transformer"
type: entity
tags: [cs324, llm, mlsysbook, model-compression]
sources: [cs324-selective-architectures, cs324-environment, mlsysbook-ch10-model-compression]
last_updated: 2026-06-05
---

Switch Transformer is a Google Mixture-of-Experts Transformer that uses top-1 routing to send each token to a single expert, simplifying and stabilizing MoE training. It scales to 1.6 trillion parameters and achieves roughly 4x faster pretraining than the dense T5-XXL baseline.

## In [[mlsysbook-ch10-model-compression|mlsysbook Ch 10]]

Reddi presents Switch Transformer as the large-scale instance of **gate-based [[ConditionalComputation|conditional computation]]** — an [[AdaptiveInference|adaptive-computation]] compression technique: 1.6T params but only ~2B activated per token (0.13%), ~7× faster pretraining than dense T5 at equal FLOPs. Top-1 routing cuts communication vs top-$k$, but load imbalance requires auxiliary loss terms and capacity factors (1.25–2×) — defining the MoE design space of "massive capacity at low per-token compute, with complex load-balancing engineering."

## Connections
- [[MixtureOfExperts]] — Switch Transformer is a sparsely-activated MoE model
- [[ConditionalComputation]] / [[AdaptiveInference]] / [[mlsysbook-ch10-model-compression]] — MoE as architectural-efficiency compression (mlsysbook Ch 10).
- [[T5]] — built on and compared against the T5 architecture
- [[cs324-selective-architectures]] — discussed in this CS324 lecture
- [[cs324-environment]] — discussed in this CS324 lecture
