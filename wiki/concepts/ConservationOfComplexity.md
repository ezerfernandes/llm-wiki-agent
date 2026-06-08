---
title: "Conservation of Complexity"
type: concept
tags: [model-compression, ml-systems, principle, mlsysbook]
sources: [mlsysbook-ch10-model-compression, mlsysbook-ch16-conclusion]
last_updated: 2026-06-05
---

# Conservation of Complexity

**The meta-law governing all of model compression: like energy in thermodynamics, an ML system cannot destroy complexity — it can only relocate it between data, algorithm, and machine.** Per [[mlsysbook-ch10-model-compression|mlsysbook Ch 10]], this principle "constrains all possible optimizations and explains why no compression technique achieves a free lunch."

## How techniques relocate complexity

- **[[Pruning]]** moves complexity from parameters to the hardware's burden of irregular sparse memory access (the model is simpler, but the system must now handle [[Sparsity|sparsity]]).
- **[[KnowledgeDistillation]]** moves it from inference compute to training compute (a smaller deployed model, a larger training budget).
- **[[NeuralArchitectureSearch]]** moves it from human design effort to automated search budget (22,400 GPU-days for early RL-NAS).

The engineer's task is to relocate complexity to wherever the cost is lowest given the deployment constraints.

## Connections

- [[ModelCompression]] — the discipline this law governs.
- [[IronLawOfMLSystems]] — the quantitative companion (compression attacks the iron law's terms).
- [[DAMTaxonomy]] — Data/Algorithm/Machine are the three destinations complexity can move between.
- [[ThirteenQuantitativeInvariants]] — the conclusion ([[mlsysbook-ch16-conclusion|Ch 16]]) elevates this from a compression-specific law to the **meta-principle uniting all thirteen invariants**: every invariant quantifies a consequence of *where complexity currently resides*. It also names the HCI analogue (Tesler's Law) and applies it to the Fallacies/Pitfalls (e.g., "tools abstract complexity; they do not eliminate it").
- [[mlsysbook-ch10-model-compression]] / [[mlsysbook-ch16-conclusion]] — sources.
