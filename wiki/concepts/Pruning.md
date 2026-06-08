---
title: "Pruning"
type: concept
tags: [model-compression, sparsity, inference, optimization]
sources: [ai-engineering-ch09-inference-optimization, mlsysbook-ch10-model-compression, mlsysbook-ch12-benchmarking, mlsysbook-ch15-responsible-engineering]
last_updated: 2026-06-05
---

# Pruning

**Removing unimportant parts of a neural network** — either *nodes* (architectural change) or *parameters* (zeroed out, producing sparsity). One of the four [[ModelCompression|model-compression]] families covered in [[ai-engineering-ch09-inference-optimization|*AI Engineering* Ch 9]].

## Two senses of "pruning"

> *"Pruning, in the context of neural networks, has two meanings. One is to remove entire nodes of a neural network, which means changing its architecture and reducing its number of parameters. Another is to find parameters least useful to predictions and set them to zero. In this case, pruning doesn't reduce the total number of parameters, only the number of non-zero parameters. This makes the model more sparse, which both reduces the model's storage space and speeds up computation."* — Ch 9

Ch 9 treats the second sense as primary because it produces **[[Sparsity|sparsity]]** that compression formats (and some hardware) can exploit.

## Why pruning is encouraging in research

- **Frankle & Carbin (2019)** — the *lottery-ticket hypothesis* paper — showed pruning can reduce non-zero parameters of certain trained networks by **> 90%** without accuracy loss.
- **Liu et al. (2018)** — pruning can discover promising small architectures, which can then be trained from scratch (Zhu et al. 2017).

## Why pruning is uncommon in production

> *"In practice, as of this writing, pruning is less common. It's harder to do, as it requires an understanding of the original model's architecture, and the performance boost it can bring is often much less than that of other approaches. Pruning also results in sparse models, and not all hardware architectures are designed to take advantage of the resulting sparsity."* — Ch 9

Three barriers:
1. **Architecture-specific** — engineers must know which sub-structures to prune.
2. **Smaller gains** than [[Quantization|quantization]] for comparable engineering effort.
3. **Hardware mismatch** — without sparsity-aware kernels / tensor cores, zeroed parameters still cost compute.

## Post-pruning finetuning

> *"Pruned models can be used as-is or be further finetuned to adjust the remaining parameters and restore any performance degradation caused by the pruning process."* — Ch 9

## Pruning vs quantization

| | Pruning | Quantization |
|---|---|---|
| Reduces | Parameter count (or non-zeros) | Bytes per parameter |
| Produces | Sparsity | Lower-precision tensor |
| Hardware support | Specialized (sparse tensor cores) | Universal (FP16/INT8 supported everywhere) |
| Engineering effort | High (architecture-aware) | Low (drop-in libraries) |
| Typical 2024 use | Rare in production | Standard practice |

## Connections

- [[Sparsity]] — what parameter-zeroing pruning produces.
- [[ModelCompression]] — the umbrella family.
- [[Quantization]] — the dominant alternative (and usually the better lever).
- [[knowledgedistillation]] — sibling compression family.
- [[LotteryTicketHypothesis]] — Frankle & Carbin 2019 (if/when a separate page exists).
- [[FineTuning]] — used to recover post-pruning accuracy.
- [[InferenceOptimization]] — broader discipline.
- [[ai-engineering-ch09-inference-optimization]] — primary source.

## From [[mlsysbook-ch10-model-compression|mlsysbook Ch 10]]

Reddi's ML-systems treatment is more taxonomic than AI Engineering's. It frames pruning as *"sparsification of the parameter space"* — $\min_{\hat W}\mathcal{L}(\hat W)$ s.t. $\|\hat W\|_0 \le k$ (NP-hard), hence magnitude heuristics. Three orthogonal axes:

- **What:** unstructured (individual weights → storage win, needs sparse kernels) vs **structured** (neurons/channels/filters/layers → dense sub-network, real latency win on commodity hardware) vs dynamic (input-conditioned at runtime).
- **Criterion:** magnitude (cheap default) → activation-based (profiles average activations) → gradient-based (uses training dynamics, most expensive).
- **Schedule:** **iterative beats one-shot** — on a 22-channel CNN removing 6 channels, iterative ends at 0.991 accuracy (−0.4%) while one-shot recovers only to 0.943 (−5%), despite identical final structure.

Historical anchor: **Optimal Brain Damage** (LeCun 1990) used Hessian info for 4× reduction at $\mathcal{O}(n^2)$ cost; magnitude pruning won at scale. Hardware-aware [[NMSparsity|N:M (2:4) structured sparsity]] is the modern way to make pruning translate to [[SparseTensorCore|Sparse Tensor Core]] speedup. See [[LotteryTicketHypothesis]] for the discovery-mechanism reframing and [[ConservationOfComplexity]] for why pruning relocates (not removes) complexity. [[mlsysbook-ch10-model-compression]]

## Benchmarking pruning ([[mlsysbook-ch12-benchmarking|mlsysbook Ch 12]])

Ch 12's [[Benchmarking|benchmarking]] view sharpens the structured/unstructured distinction into a *measurement* requirement: **structured** pruning gives 2–4× compression with consistent speedup, while **unstructured** reaches 10–100× compression but rarely improves latency on dense hardware (sparse ops lack efficient support on most GPUs) — so benchmark protocols *must specify hardware platform and software implementation*. The Lottery Ticket Hypothesis supplies [[ParetoFrontier|Pareto-frontier]] data, but the acceptable sparsity point is empirical, not universal. Pruning is the chapter's reminder that "size reduction" alone is a misleading compression metric.

## Efficiency-as-responsibility ([[mlsysbook-ch15-responsible-engineering|mlsysbook Ch 15]])

Ch 15 recasts pruning (50–90% reduction) as an instrument of responsibility — cutting inference energy/[[CarbonFootprint|carbon]] and [[TotalCostOfOwnership|TCO]] over the deployed life (where inference dominates training ~40:1) and widening accessibility — alongside [[Quantization|quantization]] and [[knowledgedistillation|distillation]]. See [[Sustainability]], [[GreenAI]], [[mlsysbook-ch15-responsible-engineering]].
