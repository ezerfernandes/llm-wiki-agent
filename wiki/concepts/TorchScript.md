---
title: "TorchScript"
type: concept
tags: [pytorch, compilers, deep-learning, deployment]
sources: [d2l-computational-performance]
last_updated: 2026-05-16
---

# TorchScript

[[PyTorch]]'s [[SymbolicProgramming|symbolic-compilation]] front-end. `torch.jit.script(net)` (and the more permissive `torch.jit.trace`) converts an [[ImperativeProgramming|imperatively-written]] `nn.Module` into a serializable, Python-independent [[ComputationalGraph|graph]] that runs entirely in the C++ backend ([[d2l-computational-performance]] §`hybridize`).

## Why

> "PyTorch is based on imperative programming and uses dynamic computation graphs. In an effort to leverage the portability and efficiency of symbolic programming, developers […] [created] torchscript that lets users develop and debug using pure imperative programming, while having the ability to convert most programs into symbolic programs to be run when product-level computing performance and deployment are required."  
> — [[d2l-computational-performance]]

## Benefits

- **Performance** — eliminates the Python-frontend bottleneck for fast GPUs; D2L's hybridize benchmarks show meaningful speedups on a 1000-iteration loop.
- **Serialization** — `net.save('my_mlp')` produces a binary parameter file + a graph description that **can be loaded by non-Python front-ends** (C++, R, Scala) for deployment.

## Cousins in other frameworks

- TensorFlow 2: `tf.function` decorator (with optional `jit_compile=True` enabling [[XLA]]).
- MXNet: `HybridSequential.hybridize()`.
- Successor in modern PyTorch (post-2.0): `torch.compile` (TorchDynamo + Inductor) — a more permissive whole-program tracer that has largely supplanted TorchScript for new code.

## See also
- [[ImperativeProgramming]] / [[SymbolicProgramming]] — the two paradigms TorchScript bridges.
- [[XLA]] — TensorFlow's equivalent JIT.
- [[ComputationalGraph]] — what TorchScript produces.
- [[d2l-computational-performance]] §`hybridize`.
