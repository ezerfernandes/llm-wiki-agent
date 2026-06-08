---
title: "Triton (Kernel Language)"
type: concept
tags: [gpu, kernel, compiler, openai, infrastructure]
sources: [ai-engineering-ch09-inference-optimization, mlsysbook-ch07-ml-frameworks, mlsysbook-ch14-ml-operations]
last_updated: 2026-06-05
---

# Triton (Kernel Language)

**A GPU kernel programming language developed by [[openai|OpenAI]]** that targets NVIDIA GPUs with Python-like syntax instead of CUDA's C++. Per [[ai-engineering-ch09-inference-optimization|*AI Engineering* Ch 9]]:

> *"Kernels are typically written in lower-level programming languages like CUDA (for NVIDIA GPUs), Triton (a language developed by OpenAI for writing custom kernels), and ROCm (for AMD GPUs). These languages allow fine-grained control over thread management and memory access but are also harder to learn than the languages that most AI engineers are familiar with, like Python."*

## Disambiguation

Triton-the-kernel-language is **not** to be confused with NVIDIA Triton Inference Server ([[NvidiaTriton]]). The names collision is unfortunate. Same Anthropic-engineer-might-have-named-it problem as `triton`/`torch.compile`/`triton_kernel`.

## Why Triton vs CUDA

- **Python-like syntax** — most AI engineers can read and write Triton with minimal learning curve.
- **Block-level abstractions** — Triton operates at the level of tiles/blocks rather than individual threads, simplifying common kernel patterns.
- **Integrated with PyTorch** — `torch.compile` can emit Triton kernels as part of its lowering process.

## Triton in the broader stack

> *"Popular frameworks such as PyTorch and TensorFlow don't yet allow fine-grained control of memory access. This has led many AI researchers and engineers to become interested in GPU programming languages such as CUDA (originally Compute Unified Device Architecture), OpenAI's Triton, and ROCm (Radeon Open Compute)."* — Ch 9

Triton is one of three GPU programming languages explicitly named in Ch 9 alongside [[CUDA]] and [[ROCm]].

## Where Triton is used

- Many `torch.compile`-lowered kernels emit Triton.
- The [[FlashAttention]] reference implementations include Triton variants alongside CUDA ones.
- The [[Mamba]]-family selective-scan kernels were originally written in Triton.

## From [[mlsysbook-ch07-ml-frameworks|mlsysbook Vol 1 Ch 7]]

Ch 7 explains *why* [[TorchInductor]] generates Triton rather than CUDA: Triton's Python-like syntax is a simpler, more stable compilation target, handling GPU details like memory coalescing automatically — a requirement for automated [[KernelFusion|kernel fusion]]. The accepted trade-off is 80–95% of hand-tuned CUDA performance in exchange for compiler-tractable autotuning and dev-time cut from weeks to hours. Triton compiles down to [[PTX]] (the stable NVIDIA IR), so the driver does the final SASS translation.

## Connections

- [[mlsysbook-ch07-ml-frameworks]] — why TorchInductor emits Triton; the 80–95%-of-CUDA trade-off.
- [[TorchInductor]] / [[PTX]] — the codegen path Triton sits in.
- [[CUDA]] — NVIDIA's lower-level alternative.
- [[ROCm]] — AMD's open-source alternative.
- [[FlashAttention]] — has Triton implementations.
- [[TorchCompile]] — the PyTorch compiler that can emit Triton.
- [[Kernel]] — what Triton produces.
- [[openai|OpenAI]] — the developer.
- [[NvidiaTriton]] — the unrelated inference server (name collision).
- [[InferenceOptimization]] — broader discipline.
- [[ai-engineering-ch09-inference-optimization]] — primary source.
- [[mlsysbook-ch14-ml-operations]] — mlsysbook Vol 1 Ch 14 lists NVIDIA Triton among production serving frameworks (best for multi-framework GPU serving) alongside TF Serving and KServe.

