---
title: "Low-Rank Factorization"
type: concept
tags: [linear-algebra, dimensionality-reduction, lora, model-compression, mlsysbook]
sources: [ai-engineering-ch07-finetuning, ai-engineering-ch09-inference-optimization, mlsysbook-ch10-model-compression]
last_updated: 2026-06-05
---

# Low-Rank Factorization

A long-standing **dimensionality reduction technique**: decompose a large matrix `W ∈ ℝ^{n × m}` into a product of two smaller matrices `A ∈ ℝ^{n × r}` and `B ∈ ℝ^{r × m}` where `r ≪ min(n, m)`. The product `A·B` is the **low-rank approximation** of `W`. Per [[ai-engineering-ch07-finetuning|*AI Engineering* Ch 7]]:

> "[[lora|LoRA]] (Low-Rank Adaptation) is built on the concept of low-rank factorization, a long-standing dimensionality reduction technique. The key idea is that you can factorize a large matrix into a product of two smaller matrices to reduce the number of parameters, which, in turn, reduces both the computation and memory requirements."

## Counting parameters

| Matrix | Dimensions | Parameter count |
|---|---|---|
| Full-rank `W` | n × m | n·m |
| Low-rank `A` | n × r | n·r |
| Low-rank `B` | r × m | r·m |
| **Factorized total** | | **n·r + r·m = (n+m)·r** |

If `r ≪ min(n, m)`, the factorized form has dramatically fewer parameters.

## Ch 7's worked example

> "A 9 × 9 matrix can be factorized into the product of two matrices of dimensions 9 × 1 and 1 × 9. The original matrix has 81 parameters, but the two product matrices have only 18 parameters combined." — Ch 7

**77% fewer parameters at rank 1**.

## Lossiness

Low-rank factorization is **lossy** unless the original matrix is actually low-rank. The higher the rank, the more information from the original matrix the factorization preserves. The trade-off:

| Rank | Parameter count | Approximation quality |
|---|---|---|
| 1 | (n+m) | Worst (only first principal direction) |
| min(n,m) | n·m | Lossless (full rank) |
| Anywhere between | Intermediate | Intermediate |

## Pre-LoRA neural-network applications

Per Ch 7, the 2010s saw many attempts to train low-rank neural networks:

- **Sainath et al. (2013)** — "Low-Rank Matrix Factorization for Deep Neural Network Training with High-Dimensional Output Targets."
- **Povey et al. (2018)** — "Semi-Orthogonal Low-Rank Matrix Factorization for Deep Neural Networks."
- **Jaderberg et al. (2014)** — "Speeding up Convolutional Neural Networks with Low Rank Expansions."
- **SqueezeNet** (Iandola et al. 2016) — achieves AlexNet-level accuracy on ImageNet using **50× fewer parameters** via various factorization strategies including replacing 3×3 convolutions with 1×1.

These showed factorization works **at small scales**. Scaling up was the open problem.

## [[lora|LoRA]] as the modern application

[[lora|LoRA]] applies low-rank factorization not to the *original* weight matrix but to the **update** during finetuning:

`W' = W + (α/r) · A·B`

The base weights `W` stay full-rank; the *delta* is low-rank. This sidesteps the "you can't pre-train low-rank" problem — pre-training stays full-rank (and full-cost), but finetuning becomes low-rank (and cheap).

## Connections

- [[lora|LoRA]] — the most prominent modern application.
- [[QLoRA]] — adds quantization on top.
- [[IntrinsicDimension]] — the theoretical reason low-rank works in NN context.
- [[SVD]] — the linear-algebraic ancestor.
- [[ReLoRA]] / [[GaLore]] — attempts to apply low-rank to pre-training.
- [[ai-engineering-ch07-finetuning]] — primary source.

## From [[ai-engineering-ch09-inference-optimization|AI Engineering Ch 9]]

Ch 9 reframes low-rank factorization explicitly as one of the **[[ModelCompression|model-compression]] families** for inference optimization — alongside [[Quantization|quantization]], [[knowledgedistillation|distillation]], and [[Pruning|pruning]]. The compression view (applying factorization to the *full pre-trained matrix* rather than to a finetuning delta) is mentioned but not the chapter's recommendation:

- **Quantization dominates** because it's "easy to use, works out of the box for many models, and is extremely effective."
- **Low-rank factorization** of pre-trained weights typically degrades quality more than weight-only quantization because modern LLM weight matrices are *approximately* but not exactly low-rank — error compounds across layers in ways quantization noise doesn't.
- The [[IntrinsicDimension|intrinsic-dimension hypothesis]] supports the *finetuning-delta* application (LoRA) better than the *whole-model* application — pre-training distributes information across the full rank.

The chapter's framing thus consolidates the wiki's earlier LoRA-centric view: low-rank works for the **delta**, not the **whole weight tensor**.

## The bandwidth-compute trade-off ([[mlsysbook-ch10-model-compression|mlsysbook Ch 10]])

Ch 10 frames LRMF (Low-Rank Matrix Factorization) as a structured-approximation compression technique that **trades arithmetic for bandwidth**: a 4096×4096 FP32 matrix (67 MB) factored at rank-128 → two matrices totaling ~4 MB (**16× data-movement reduction**); applying the factors directly drops per-vector compute from $\mathcal{O}(mn)$ to $\mathcal{O}(k(m+n))$. The optimal rank-$k$ approximation comes from **[[SingularValueDecomposition|SVD]]** (Eckart-Young theorem). Critical caveat: **never materialize $UV$ explicitly** — that adds $\mathcal{O}(mkn)$ and defeats the purpose. The one-time $\mathcal{O}(mn\cdot\min(m,n))$ factorization cost must be amortized by repeated inference savings. [[TensorDecomposition]] (CP/Tucker/Tensor-Train) extends this to conv filters and attention. [[mlsysbook-ch10-model-compression]]

## Connections (mlsysbook)

- [[TensorDecomposition]] — the multi-dimensional generalization.
- [[SingularValueDecomposition]] — the optimal factorization method.
- [[mlsysbook-ch10-model-compression]] — bandwidth-compute trade, Eckart-Young, never-materialize-UV caveat.
