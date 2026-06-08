---
title: "Conditional Computation"
type: concept
tags: [model-compression, inference, dynamic-computation, routing, mlsysbook]
sources: [mlsysbook-ch10-model-compression]
last_updated: 2026-06-05
---

# Conditional Computation

**Letting a network decide *which* layers, units, or paths to activate based on each input, via learned gating or routing — turning off parts of the model that are unnecessary for a given input.** Per [[mlsysbook-ch10-model-compression|mlsysbook Ch 10]], where [[EarlyExit|early exit]] makes a single exit-or-continue decision, conditional computation dynamically selects sub-networks.

## Examples

- **SkipNet** — a gating mechanism skips CNN layers for simple inputs; a lightweight per-layer classifier predicts whether a layer should execute.
- **Gate-based / Dynamic Filter Networks** — routers (gating networks) predict which path executes; DFN generates input-conditioned filters.
- **[[MixtureOfExperts|Mixture-of-Experts]] / [[SwitchTransformer|Switch Transformer]]** — a gating network routes each token to a small subset of specialist experts (Switch: 1.6T params, ~0.13% active per token, 7× faster pretraining than dense T5).

## Costs

Gating/routing add latency and memory-access overhead; discrete decisions break standard backprop (need RL or continuous approximations); load imbalance requires auxiliary losses and capacity factors.

## Connections

- [[AdaptiveInference]] / [[EarlyExit]] — sibling adaptive mechanisms.
- [[MixtureOfExperts]] / [[SwitchTransformer]] — the large-scale gating instantiation.
- [[ModelCompression]] — architectural-efficiency dimension.
- [[mlsysbook-ch10-model-compression]] — source.
