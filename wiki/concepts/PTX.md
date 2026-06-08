---
title: "PTX (Parallel Thread Execution)"
type: concept
tags: [gpu, nvidia, compilation, intermediate-representation]
sources: [mlsysbook-ch07-ml-frameworks]
last_updated: 2026-06-05
---

# PTX (Parallel Thread Execution)

**PTX** is an [[IntermediateRepresentation|intermediate representation]] from [[NVIDIA]] that serves as a stable compilation target for high-level GPU languages like [[Triton]]. It lets compilers ([[TorchInductor]]) generate *portable* code: the NVIDIA driver — not the framework — performs the final translation to hardware-specific machine code (SASS). This forward compatibility costs ~10–15% performance vs kernels hand-tuned for a specific GPU architecture.

## Connections

- [[mlsysbook-ch07-ml-frameworks]] — the target of Triton/TorchInductor codegen.
- [[Triton]] / [[TorchInductor]] — compile to PTX; [[CUDA]] / [[NVIDIA]] — the platform.
- [[IntermediateRepresentation]] — the compiler pattern.
