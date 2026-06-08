---
title: "XLA (Accelerated Linear Algebra)"
type: concept
tags: [compiler, ml, tensorflow, jax, tpu, infrastructure]
sources: [ai-engineering-ch09-inference-optimization, mlsysbook-ch07-ml-frameworks, mlsysbook-ch11-hardware-acceleration]
last_updated: 2026-06-05
---

# XLA — Accelerated Linear Algebra

**A machine-learning compiler originally developed by [[google|Google]] for [[TensorFlow]]**, now open-sourced as **OpenXLA**. The dominant compiler for Google's TPU stack and a key backend for JAX. Per [[ai-engineering-ch09-inference-optimization|*AI Engineering* Ch 9]]:

> *"Compilers can be ... integrated into ML and inference frameworks, like torch.compile (a feature in PyTorch), XLA (Accelerated Linear Algebra, originally developed by TensorFlow, with an open source version called OpenXLA), and the compiler built into the TensorRT, which is optimized for NVIDIA GPUs."*

## What XLA does

XLA accepts ML computations expressed as graphs (TensorFlow `tf.function`, JAX `jit`, PyTorch via OpenXLA experimental support) and produces hardware-optimized code via:
- **Operator fusion** — combining many small operations into one kernel.
- **Layout transformations** — choosing tensor layouts that match hardware preferences.
- **Constant folding, dead-code elimination, common-subexpression elimination** — classical compiler optimizations applied at tensor granularity.
- **Backend code generation** — currently TPU, GPU (NVIDIA via PTX), CPU.

## XLA vs torch.compile

| | XLA | `torch.compile` |
|---|---|---|
| Origin | Google / TensorFlow | Meta / PyTorch |
| Primary targets | TPU, GPU, CPU | GPU (CUDA via Triton) |
| Frontend | TF, JAX (and PyTorch via OpenXLA) | PyTorch |
| Open source | Yes (OpenXLA) | Yes |

## XLA and TPUs

XLA is *the* TPU compilation path. TPU's tensor primitives are sufficiently different from GPU's that a dedicated compiler is required to extract performance. This is also why the [[PaLM]] paper's MFU number (46.2%) was reported on TPU v4 + XLA, not on a GPU stack.

## From [[mlsysbook-ch07-ml-frameworks|mlsysbook Vol 1 Ch 7]]

Ch 7 uses XLA as the canonical [[StaticGraph|static-graph]] / AOT compiler: fusing matmul+bias+ReLU into one kernel cuts data movement $D_{\text{vol}}$ by 2–3× vs three separate launches, for ~1.5–2× end-to-end transformer-training speedup "without any model changes." The speedup is *modest on compute-bound* transformer GEMMs (little overhead to remove) but **3–10× on memory-bound** models where fusion hides many small sequential ops. XLA is also the compile target of [[JAX]]'s composable `jit` transformation, reaching >90% TPU utilization on pure functions.

## Connections

- [[mlsysbook-ch07-ml-frameworks]] — XLA as the static-graph/AOT compiler; JAX's jit backend.
- [[StaticGraph]] / [[JITCompilation]] — the execution modes XLA serves.
- [[TVM]] / [[MLIR]] — standalone-compiler counterparts.
- [[TorchCompile]] — framework-integrated peer.
- [[TensorRTLLM]] — NVIDIA-specific compiler/runtime peer.
- [[GoogleTPU]] — primary deployment target.
- [[TensorFlow]] — origin framework.
- [[Compiler]] / [[Lowering]] — broader concepts.
- [[OperatorFusion]] — the canonical XLA optimization.
- [[InferenceOptimization]] — broader discipline.
- [[ai-engineering-ch09-inference-optimization]] — primary source.
