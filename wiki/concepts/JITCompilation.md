---
title: "JIT Compilation (ML Frameworks)"
type: concept
tags: [frameworks, execution-model, compilation, deep-learning]
sources: [mlsysbook-ch07-ml-frameworks]
last_updated: 2026-06-05
---

# JIT Compilation (ML Frameworks)

**Just-in-time (JIT) compilation** pursues both [[EagerExecution|eager]] debugging and [[StaticGraph|static-graph]] optimization at once by capturing computation *at runtime*. Developers write natural Python that runs eagerly during development; the framework automatically captures and compiles hot paths into optimized [[Kernel|kernels]] for production. The core trade-off is **fidelity vs generality**:

- **Tracing** records the exact execution path taken during a sample run — high fidelity to that input, but silently *wrong outputs* for untaken data-dependent branches.
- **Scripting** analyzes the full program structure (AST), preserving all control-flow branches, but requires a restricted language subset.

Both produce an [[IntermediateRepresentation|intermediate representation]] enabling the AOT optimizations of static graphs (fusion, [[ConstantFolding|constant folding]], [[DeadCodeElimination|DCE]], buffer reuse). JIT amortizes the dispatch overhead $L_{\text{lat}}$ across the compiled region — which is why **graph breaks** (returns to eager) are performance-critical: each break resets the amortization.

First call pays a one-time cost (~100 ms small, 5–30 s transformer, 5–10 min GPT-3 scale); subsequent same-shape calls dispatch to cached compiled code in microseconds. Shape changes trigger recompilation (shape specialization). Exemplars: [[TorchScript]] (tracing/scripting), [[TorchCompile|torch.compile]] (bytecode capture via [[TorchDynamo]]), and JAX `jit` (compiles pure functions to [[XLA]]).

## Connections

- [[mlsysbook-ch07-ml-frameworks]] — the hybrid execution strategy.
- [[EagerExecution]] / [[StaticGraph]] — the two endpoints JIT bridges.
- [[TorchCompile]] / [[TorchScript]] / [[TorchDynamo]] / [[TorchInductor]] / [[FXGraph]] — the PyTorch JIT path.
- [[XLA]] / [[JAX]] — JAX's `jit` transformation.
- [[CompilationContinuum]] / [[DispatchOverhead]] — when JIT pays off.
