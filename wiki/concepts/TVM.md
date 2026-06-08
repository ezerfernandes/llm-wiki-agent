---
title: "Apache TVM"
type: concept
tags: [compiler, ml, infrastructure, apache, open-source]
sources: [ai-engineering-ch09-inference-optimization, mlsysbook-ch11-hardware-acceleration]
last_updated: 2026-06-05
---

# Apache TVM

**An open-source machine-learning compiler stack that lowers high-level ML models into hardware-specific code.** One of two standalone ML compilers named in [[ai-engineering-ch09-inference-optimization|*AI Engineering* Ch 9]] (alongside [[MLIR]]):

> *"Compilers can be standalone tools, such as Apache TVM and MLIR (Multi-Level Intermediate Representation) or integrated into ML and inference frameworks, like torch.compile (a feature in PyTorch), XLA (Accelerated Linear Algebra, originally developed by TensorFlow, with an open source version called OpenXLA), and the compiler built into the TensorRT, which is optimized for NVIDIA GPUs."*

## What TVM does

TVM accepts models from PyTorch / TensorFlow / ONNX / etc., lowers them to its intermediate representation, applies hardware-aware optimizations (operator fusion, layout transformation, loop tiling), and emits code for diverse backends — CPUs, GPUs (NVIDIA + AMD), FPGAs, mobile, microcontrollers.

> *"During the lowering process, whenever possible, these operations are converted into specialized kernels to run faster on the target hardware."* — Ch 9

## Position in the compiler landscape

| Compiler | Lineage | Primary use |
|---|---|---|
| **Apache TVM** | Independent / Apache | Cross-hardware deployment |
| **[[MLIR]]** | LLVM Foundation | Compiler infrastructure |
| **[[XLA]]** | TensorFlow / OpenXLA | TPU + GPU |
| **`torch.compile`** | PyTorch / Meta | PyTorch-native |
| **TensorRT** | NVIDIA | NVIDIA-only |

## Why standalone compilers matter

Framework-integrated compilers (`torch.compile`, XLA) are easy to adopt but tied to their framework. Standalone compilers (TVM, MLIR) target the **deployment** problem — getting a model trained in any framework onto any hardware.

## Connections

- [[MLIR]] — the other standalone compiler Ch 9 names.
- [[XLA]] / [[TorchCompile]] — framework-integrated counterparts.
- [[TensorRTLLM]] — NVIDIA's compiler+runtime for NVIDIA GPUs.
- [[Compiler]] — broader concept.
- [[Lowering]] — the process compilers perform.
- [[Kernel]] — what compilers produce.
- [[InferenceOptimization]] — broader discipline.
- [[ai-engineering-ch09-inference-optimization]] — primary source.
