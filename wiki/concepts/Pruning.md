---
title: "Pruning"
type: concept
tags: [model-compression, sparsity, inference, optimization]
sources: [ai-engineering-ch09-inference-optimization]
last_updated: 2024-12-04
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
