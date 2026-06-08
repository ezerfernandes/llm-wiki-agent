---
title: "Google TPU (Tensor Processing Unit)"
type: concept
tags: [hardware, google, ai-accelerator, inference, training]
sources: [ai-engineering-ch09-inference-optimization, mlsysbook-ch02-ml-systems, mlsysbook-ch06-network-architectures, mlsysbook-ch07-ml-frameworks, mlsysbook-ch11-hardware-acceleration]
last_updated: 2026-06-05
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

## In the deployment spectrum ([[mlsysbook-ch02-ml-systems|mlsysbook Ch 2]])

Reddi uses the **TPU v4 Pod** (4,096 chips, >1 EFLOP/s, 131 TB HBM2, ~MW power) as the [[CloudML|Cloud ML]] anchor of the [[DeploymentSpectrum|hardware spectrum]] — the high-compute, high-power extreme, in contrast to a $10 ESP32 microcontroller at the [[TinyML]] end. He frames the TPU as an ASIC that trades general-purpose flexibility for >10× performance-per-watt on matmul, economical only for massive sustained ML computation. The post-[[DennardScaling|Dennard]] [[PowerWall|power wall]] is presented as *why* such specialization exists.

## Connections

- [[google|Google]] — the developer / owner.
- [[AIAccelerator]] — the umbrella concept.
- [[DeploymentSpectrum]] / [[CloudML]] — the TPU v4 Pod as the cloud-tier hardware anchor.
- [[XLA]] — the dominant TPU compiler.
- [[PaLM]] — the model whose TPU v4 MFU (46.2%) Ch 9 cites.
- [[TensorCore]] — NVIDIA's tensor primitive, adopted later than TPU's design.
- [[GPU]] / [[NVIDIA]] — competing AI accelerator family.
- [[InferenceOptimization]] — broader discipline.
- [[ai-engineering-ch09-inference-optimization]] / [[mlsysbook-ch02-ml-systems]] — sources.
- [[mlsysbook-ch06-network-architectures]] — Ch 6 presents the TPU as Google's response to the prevalence of [[GEMM|matrix multiplication]] across all architectures: a large [[SystolicArray|systolic array]] doing thousands of MACs/cycle. TPU v1 ~92 TOPS (INT8) @ 40 W vs NVIDIA K80 ~8.7 TFLOP/s (FP32) @ 300 W ≈ 80× peak ops/W — illustrating "dedicating silicon to a dominant primitive can outperform general-purpose flexibility."
- [[mlsysbook-ch07-ml-frameworks]] — Ch 7 frames the TPU as the framework abstraction problem in action: the same model code reaches the TPU via [[XLA]] HLO compilation (vs [[CUBLAS|cuBLAS]] on GPU), TPUs "require static shapes," and [[BF16]] (Google Brain ~2018) was designed for TPU training stability. [[JAX]]'s functional purity enables >90% TPU utilization.
- [[mlsysbook-ch11-hardware-acceleration]] — Ch 11 tells the TPU origin in full: the 2013 "capacity cliff" (voice search would double Google's data centers), the 15-month design-to-deploy sprint, and the TPUv1-vs-K80 "efficiency shock" (15–30× inference, 30–80× perf/watt) that "ended the General Purpose era." TPUv4 = two cores/chip, each a 128×128 BF16 [[SystolicArray|systolic array]] — the canonical [[DomainSpecificArchitecture]].
