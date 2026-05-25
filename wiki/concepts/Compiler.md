---
title: "Compiler (ML)"
type: concept
tags: [compiler, ml, infrastructure, optimization]
sources: [ai-engineering-ch09-inference-optimization]
last_updated: 2024-12-04
---

# Compiler (ML)

**A tool that converts ML model code into a form that can run on specific hardware.** Per [[ai-engineering-ch09-inference-optimization|*AI Engineering* Ch 9]]:

> *"A model script specifies a series of operations that need to be performed to execute that model. To run this code on a piece of hardware, such as a GPU, it has to be converted into a language compatible with that hardware. This process is called lowering. A tool that lowers code to run a specific hardware is called a compiler. Compilers bridge ML models and the hardware they run on. During the lowering process, whenever possible, these operations are converted into specialized kernels to run faster on the target hardware."*

## The ML compiler taxonomy (Ch 9)

### Standalone tools

- **[[TVM|Apache TVM]]** — cross-hardware ML compiler.
- **[[MLIR|MLIR]]** — multi-level IR compiler infrastructure (LLVM Foundation).

### Framework-integrated

- **`torch.compile`** — PyTorch's compiler (uses Triton, AOTAutograd, TorchInductor).
- **[[XLA]] / OpenXLA** — originally TensorFlow; now also JAX and (experimentally) PyTorch.
- **TensorRT compiler** — built into [[TensorRTLLM|TensorRT]]; NVIDIA-only.

### Proprietary / vendor

> *"AI companies might have their own compilers, with their proprietary kernels designed to speed up their own workloads."* — Ch 9

Including Google for TPU (XLA), AMD for ROCm, AWS for Inferentia/Trainium (Neuron), Apple for Neural Engine.

## What compilers do during lowering

Per Ch 9, compilers apply (where possible) the same four optimizations a kernel writer would do by hand:

- **[[Vectorization|Vectorization]]** — SIMD across contiguous elements.
- **Parallelization** — split arrays into independent chunks for cores/threads.
- **[[LoopTiling|Loop tiling]]** — reorder access patterns for cache hierarchy.
- **[[OperatorFusion|Operator fusion]]** — combine multiple operators into one pass to reduce memory traffic.

Operator fusion gets the most attention because it requires understanding model structure, not just generic loop transformations.

## Why kernels are still hand-written

> *"While vectorization, parallelization, and loop tiling can be applied broadly across different models, operator fusion requires a deeper understanding of a model's specific operators and architecture. As a result, operator fusion demands more attention from optimization engineers."* — Ch 9

For high-stakes kernels ([[FlashAttention]], MatMul libraries), hand-tuned kernels still beat compiler output. Compilers shrink the gap year over year.

## The trade secret angle

> *"Many companies consider their kernels their trade secrets. Having kernels that allow them to run models faster and cheaper than their competitors is a competitive advantage."* — Ch 9 footnote

This is why frontier labs' best inference stacks are proprietary even when their model weights are open.

## Connections

- [[Lowering]] — what compilers do.
- [[Kernel]] — what compilers produce.
- [[TVM]] / [[MLIR]] — standalone instances.
- [[XLA]] / [[TorchCompile]] / [[TensorRTLLM]] — framework-integrated instances.
- [[OperatorFusion]] / [[Vectorization]] / [[LoopTiling]] — the four optimization techniques.
- [[CompilerOptimization]] — adjacent broader concept.
- [[InferenceOptimization]] — broader discipline.
- [[ai-engineering-ch09-inference-optimization]] — primary source.
