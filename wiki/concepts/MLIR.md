---
title: "MLIR (Multi-Level Intermediate Representation)"
type: concept
tags: [compiler, ml, infrastructure, llvm]
sources: [ai-engineering-ch09-inference-optimization]
last_updated: 2024-12-04
---

# MLIR — Multi-Level Intermediate Representation

**A compiler infrastructure project under the LLVM Foundation** that provides multi-level IR design and tooling for building domain-specific compilers — including ML compilers. One of two standalone ML compiler tools named in [[ai-engineering-ch09-inference-optimization|*AI Engineering* Ch 9]] (alongside [[TVM|Apache TVM]]):

> *"Compilers can be standalone tools, such as Apache TVM and MLIR (Multi-Level Intermediate Representation) or integrated into ML and inference frameworks, like torch.compile, XLA, and the compiler built into the TensorRT."*

## What "multi-level IR" means

Traditional compilers (e.g. LLVM) have a single mid-level IR. MLIR allows compiler authors to **stack multiple IRs**, each at a different abstraction level — e.g. one IR for tensor operations, one for loop nests, one for hardware-specific intrinsics. Each level can have its own type system and transformations, lowered into the next.

This is useful for ML because ML compilers want to:
1. Start at a **high level** (tensor operations from PyTorch).
2. Pass through **intermediate** levels (operator fusion, layout transformations).
3. Emit **low-level** code (CUDA, Triton, vectorized CPU).

MLIR provides the infrastructure for that lowering pipeline.

## Where MLIR appears

- **[[XLA]] / OpenXLA** — uses MLIR-based IR.
- **TensorFlow** — has migrated significant parts to MLIR.
- **Specialized AI compilers** at various chip vendors use MLIR as a foundation.

## Position in the compiler landscape

Unlike [[TVM]] (a complete compiler stack), MLIR is **infrastructure** — building blocks for compiler authors. The two are complementary; some compilers use both.

## Connections

- [[TVM]] — sibling standalone ML compiler.
- [[XLA]] — MLIR-based.
- [[TorchCompile]] / [[TensorRTLLM]] — framework-integrated counterparts.
- [[Compiler]] — broader concept.
- [[Lowering]] — the process MLIR's multi-level IR supports.
- [[InferenceOptimization]] — broader discipline.
- [[ai-engineering-ch09-inference-optimization]] — primary source.
