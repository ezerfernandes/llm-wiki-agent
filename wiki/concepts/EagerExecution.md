---
title: "Eager Execution"
type: concept
tags: [frameworks, execution-model, autograd, deep-learning]
sources: [mlsysbook-ch07-ml-frameworks]
last_updated: 2026-06-05
---

# Eager Execution

**Eager execution** ("define-by-run") evaluates each tensor operation immediately as the program calls it, building the [[ComputationalGraph|computational graph]] *dynamically at runtime*. When a programmer writes `y = x * 2`, the multiplication happens instantly and the result is available for inspection — enabling standard Python debugging (`print`, `pdb`, breakpoints) and data-dependent control flow (variable-length RNNs, beam search, adaptive computation). It is [[PyTorch]]'s default mode and [[TensorFlow]] 2.x's default.

## Systems trade-off

Flexibility comes at a cost that maps to the [[IronLawOfMLSystems|iron law]]'s overhead term $L_{\text{lat}}$:

- **Dispatch tax**: every op pays ~10 μs of Python dispatch (function lookup, arg parsing, type checking). For a 1 μs ReLU the tax is ~91% (overhead-bound); for a 100 μs matmul it drops to ~9%.
- **No cross-op fusion**: because the framework sees one op at a time, it cannot fuse [[Kernel|kernels]] — each op launches its own GPU kernel.
- **Autograd tape overhead**: each forward pass rebuilds the [[Autograd|autograd tape]] from scratch, increasing memory ~2–3× vs forward-only.

A ResNet-50 eager forward pass adds ~5–10 ms of dispatch + tape overhead vs an optimized compiled version. This is why small models benefit disproportionately from [[TorchCompile|torch.compile]] (per the [[DispatchOverhead|Dispatch Overhead Law]]).

The opposite design — capturing the whole computation before running any of it — is the [[StaticGraph|static graph]]; the hybrid middle ground is [[JITCompilation|JIT compilation]].

## Connections

- [[mlsysbook-ch07-ml-frameworks]] — the execution problem; eager as one of three execution strategies.
- [[StaticGraph]] / [[JITCompilation]] — the other two points on the execution continuum.
- [[ComputationalGraph]] / [[Autograd]] — the dynamic graph / tape that eager builds.
- [[DispatchOverhead]] / [[CompilationContinuum]] — why and when to leave eager mode.
- [[PyTorch]] — eager-first framework; [[TensorFlow]] 2.x — eager by default with `tf.function` for graph mode.
