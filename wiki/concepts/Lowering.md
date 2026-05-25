---
title: "Lowering (Compiler)"
type: concept
tags: [compiler, ml, infrastructure]
sources: [ai-engineering-ch09-inference-optimization]
last_updated: 2024-12-04
---

# Lowering

**The process of converting a model script into code that can run on a specific piece of hardware.** Per [[ai-engineering-ch09-inference-optimization|*AI Engineering* Ch 9]]:

> *"A model script specifies a series of operations that need to be performed to execute that model. To run this code on a piece of hardware, such as a GPU, it has to be converted into a language compatible with that hardware. This process is called lowering. A tool that lowers code to run a specific hardware is called a compiler."*

## What lowering produces

> *"During the lowering process, whenever possible, these operations are converted into specialized kernels to run faster on the target hardware."* — Ch 9

The output is **[[Kernel|kernels]]** — hardware-specific compute routines.

## Lowering as multi-level translation

Modern ML compilers often perform lowering in **multiple stages**:

1. **High-level IR** — close to the user's model code (tensor operations).
2. **Mid-level IR** — operator-fused tensor ops with explicit memory layout.
3. **Low-level IR** — close to hardware (PTX for NVIDIA, LLVM IR for CPU, TPU-specific MLIR dialects).
4. **Machine code** — what the chip actually executes.

[[MLIR]] is specifically designed for this multi-level lowering. [[TVM]], [[XLA]], and `torch.compile` all perform multi-step lowering internally.

## Where lowering matters

- **Performance** — well-lowered code does kernel fusion, layout transformation, and hardware-specific intrinsic selection.
- **Portability** — the same model script can run on multiple hardware backends if the compiler can lower to each.
- **New hardware support** — when a new accelerator emerges, the question is how quickly the lowering pipeline can be updated.

## Connections

- [[Compiler]] — the tool that performs lowering.
- [[Kernel]] — the hardware-specific output.
- [[TVM]] / [[MLIR]] / [[XLA]] / [[TorchCompile]] — instances of compilers doing lowering.
- [[OperatorFusion]] — the canonical lowering optimization.
- [[CompilerOptimization]] — adjacent broader concept.
- [[InferenceOptimization]] — broader discipline.
- [[ai-engineering-ch09-inference-optimization]] — primary source.
