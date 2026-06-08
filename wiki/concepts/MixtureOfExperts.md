---
title: "Mixture-of-Experts"
type: concept
tags: [ml-architecture, routing, sparse-model, foundational]
sources: [2605.12966-agentic-ai-to-agi, ai-engineering-ch02-foundation-models, ai-engineering-ch07-finetuning]
last_updated: 2024-12-04
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
- [[Mixtral8x7B]] — the canonical worked example from Ch 2.
- [[Jamba]] — Transformer–Mamba MoE hybrid (Ch 2).
- [[ai-engineering-ch02-foundation-models]] — primary source for the production-MoE framing.
- [[SwitchTransformer]] / [[ConditionalComputation]] / [[mlsysbook-ch10-model-compression]] — Ch 10 frames MoE as **gate-based conditional computation** (an adaptive-computation compression technique): a router activates only a small subset of experts per token. Switch Transformer = 1.6T params but ~2B active/token (0.13%), 7× faster pretraining than dense T5; load imbalance needs auxiliary losses + capacity factors.

## From [[ai-engineering-ch02-foundation-models|AI Engineering Ch 2]]

Ch 2 frames MoE as **the canonical example of how sparse models break the "parameter count = capacity = cost" identity**. A 7B-param model that is 90% sparse has only 700M non-zero parameters; sparsity allows more efficient storage and computation, so a large sparse model can require less compute than a small dense model.

### Mixtral 8x7B worked example

[[Mixtral8x7B|Mixtral 8x7B]] (Mistral) has:
- **8 experts × 7B params = 56B** *if no parameters were shared* — but only **46.7B total** thanks to shared parameters.
- **Only 2 experts active per token per layer** → **12.9B active parameters per token**.
- **Cost and speed match a 12.9B dense model** despite the 46.7B total-param count.

This makes the "how big is the model?" question genuinely ambiguous for sparse models.

### Scaling-law caveat

Ch 2 explicitly notes that the [[ChinchillaScalingLaw|Chinchilla scaling law]] was derived for **dense models on human-generated data**. Adapting it for sparse models like MoE (and for synthetic data) is an active research area.

### Jamba: MoE on top of a hybrid backbone

[[Jamba]] (Lieber et al. 2024) interleaves Transformer and [[Mamba]] layers, then layers MoE on top: 52B total / 12B active params, designed to fit one 80GB GPU. Demonstrates that MoE composes cleanly with non-Transformer architectures.

## From [[ai-engineering-ch07-finetuning|AI Engineering Ch 7]]

Ch 7 introduces a new way to *construct* MoEs that doesn't require training one from scratch: **[[SparseUpcycling|sparse upcycling]]** ([[Komatsuzaki2022SparseUpcycling|Komatsuzaki et al., 2022]]) — "Sparse Upcycling: Training Mixture-of-Experts from Dense Checkpoints."

### The recipe (Ch 7)

1. Take a **pre-trained dense model**.
2. **Replicate certain layers or modules** N times.
3. **Add a router** that sends each input to the most suitable copy.
4. **Train the merged model + router** to refine performance.

Komatsuzaki et al. showed sparse-upcycling can produce MoEs that *outperform* MoEs trained from scratch — i.e., dense pre-training is reusable as MoE pre-training. This makes MoE creation accessible to teams that have a dense checkpoint but not the compute to train an MoE from scratch.

### [[TogetherAI]]'s [[MixtureOfAgents]] (Ch 7, Wang et al. 2024)

Using layer-stacking + routing across **six weaker open-source models**, Together AI built a system with performance comparable to [[gpt54|GPT-4o]] on some benchmarks. Spiritually a multi-model MoE rather than a single-model MoE.

### Position within Ch 7

Sparse upcycling lives in the **[[ModelMerging|model-merging]] → [[LayerStacking|layer-stacking]]** branch of the chapter. The bigger framing: MoEs aren't just an architectural choice you commit to at pre-training time — they're a *merging output* you can produce from a dense lineage.
