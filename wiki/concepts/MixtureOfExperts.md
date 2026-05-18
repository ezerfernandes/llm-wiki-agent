---
title: "Mixture-of-Experts"
type: concept
tags: [ml-architecture, routing, sparse-model, foundational]
sources: [2605.12966-agentic-ai-to-agi]
last_updated: 2026-05-15
---

# Mixture-of-Experts

**Mixture-of-Experts (MoE)** routes each input through a small subset of expert sub-networks via a learned gating function rather than activating an entire dense network. The "Outrageously Large Neural Networks" sparsely-gated MoE layer (Shazeer et al., 2017) and **Switch Transformer** (Fedus et al., 2022) are the canonical references; **GShard** (Lepikhin et al., 2021) and successors scaled the idea to trillion-parameter models.

## Why it works (shared insight with [[AgenticAI]])

Both MoE and [[AgenticAI]] are built on the same insight: task heterogeneity is better handled by specialized components than by a universal compromise. [[2605.12966-agentic-ai-to-agi]] (§5) explicitly reinterprets MoE as the **single-layer routing regime** of [[RoutingBasedAgenticAI]] with [[CompositionalCapacity]] $C(\mathcal{G})\approx\sum_u L_u$ — a bounded sum of per-expert Lipschitz constants. The boundedness is what makes MoE *inherently stable*.

The empirical success of sparse MoE — Switch Transformer, GShard, modern MoE-LLMs — counts in this framing as direct empirical validation of the paper's central thesis: *routing to specialized sub-networks beats a monolithic dense pass*, even when the experts share a common backbone.

## Three axes where [[AgenticAI]] generalizes MoE

Per §5 of [[2605.12966-agentic-ai-to-agi]]:

1. **Scope.** MoE uses fixed expert sub-networks within a single forward pass. Agentic AI uses autonomous agents with independent parameters capable of multi-step reasoning.
2. **Topology.** MoE is single-layer (router → expert). Agentic AI extends to arbitrary DAGs (Def. 4.1).
3. **Routing mechanism.** MoE relies on differentiable gating trained end-to-end. Agentic routing accommodates iterative refinement, external tool use, and dynamic knowledge retrieval — non-differentiable, autonomous, possibly online.

Agentic AI therefore admits richer topological structures and greater expressivity than MoE while keeping MoE's stability advantage on the routing regime.

## Connections
- [[2605.12966-agentic-ai-to-agi]]
- [[AgenticAI]]
- [[RoutingBasedAgenticAI]]
- [[CompositionalCapacity]]
- [[Transformer]]
- [[ScalingLaws]]
