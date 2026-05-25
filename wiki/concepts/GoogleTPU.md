---
title: "Google TPU (Tensor Processing Unit)"
type: concept
tags: [hardware, google, ai-accelerator, inference, training]
sources: [ai-engineering-ch09-inference-optimization]
last_updated: 2024-12-04
---

# Google TPU — Tensor Processing Unit

**[[google|Google]]'s family of custom AI accelerators** designed primarily for tensor operations. Mentioned throughout [[ai-engineering-ch09-inference-optimization|*AI Engineering* Ch 9]] as the dominant non-NVIDIA AI accelerator family — and as the chip family the [[transformer|transformer]] architecture was originally optimized for.

## Hardware lineage

| Generation | Use | MFU example (Ch 9 Table 9-1) |
|---|---|---|
| TPU v3 | Gopher 280B training (4096 chips) | 32.5% |
| TPU v4 | PaLM 540B training (6144 chips) | **46.2%** |
| TPU v5 / v5e / v5p | Gemini, Pathways | (not in Ch 9) |
| Edge TPU | On-device inference (mobile, Coral) | n/a |

## Compute primitive

> *"TPUs, on the other hand, are designed with tensor operations as their primary compute primitive."* — Ch 9

Where modern NVIDIA GPUs have *added* [[TensorCore|Tensor Cores]] to a vector-centric architecture, TPUs were designed from the ground up around 2D / 3D tensor primitives.

## TPU and the transformer's origin

> *"While a chip can be developed to run one model architecture, a model architecture can be developed to make the most out of a chip, too. For example, the transformer was originally designed by Google to run fast on TPUs and only later optimized on GPUs."* — Ch 9 footnote

This is a noteworthy co-evolution claim: the transformer's matmul-heavy design wasn't accidental — it matched TPU strengths.

## TPU software stack

The dominant compiler is **[[XLA]]** (now OpenXLA). JAX is TPU-first; TensorFlow has first-class TPU support; PyTorch reaches TPU via OpenXLA / PyTorch-XLA.

## Pricing / availability

TPUs are available via Google Cloud only; you cannot buy them. This is a structural difference from NVIDIA GPUs and one reason CUDA dominates the broader ecosystem.

## Connections

- [[google|Google]] — the developer / owner.
- [[AIAccelerator]] — the umbrella concept.
- [[XLA]] — the dominant TPU compiler.
- [[PaLM]] — the model whose TPU v4 MFU (46.2%) Ch 9 cites.
- [[TensorCore]] — NVIDIA's tensor primitive, adopted later than TPU's design.
- [[GPU]] / [[NVIDIA]] — competing AI accelerator family.
- [[InferenceOptimization]] — broader discipline.
- [[ai-engineering-ch09-inference-optimization]] — primary source.
