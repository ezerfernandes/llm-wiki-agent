---
title: "Intermediate Representation (IR)"
type: concept
tags: [frameworks, compilation, intermediate-representation]
sources: [mlsysbook-ch07-ml-frameworks]
last_updated: 2026-06-05
---

# Intermediate Representation (IR)

An **intermediate representation (IR)** is a language-independent layer that decouples a compiler's *frontend* (high-level code capture) from its *backend* (hardware code generation) — exactly as LLVM IR decouples C/Rust/Swift frontends from x86/ARM backends. ML frameworks adopted this pattern because it reduces the $\mathcal{O}(M \times N)$ cost of supporting $M$ frontends and $N$ hardware backends to $\mathcal{O}(M + N)$: a single graph-capture mechanism ([[TorchDynamo]], `tf2xla`) can target multiple backends without rewriting capture logic.

The IR is where the AOT optimizations live: operator [[KernelFusion|fusion]], [[ConstantFolding|constant folding]], [[DeadCodeElimination|dead code elimination]], and buffer reuse. ML-framework IRs include [[FXGraph|FX Graph]] (PyTorch's LLVM-IR analog), [[TorchScript]] IR (using the `aten`/`prim` namespaces in SSA form), HLO ([[XLA]]'s IR), and [[PTX]] (the GPU IR). [[Lowering|Lowering]] is the process of translating from a high-level IR down through successively lower IRs to hardware-native code.

## Connections

- [[mlsysbook-ch07-ml-frameworks]] — the compiler pattern underlying JIT and static graphs.
- [[FXGraph]] / [[TorchScript]] / [[XLA]] / [[PTX]] — concrete ML-framework IRs.
- [[Lowering]] — high-IR → low-IR → hardware translation.
- [[KernelFusion]] / [[ConstantFolding]] / [[DeadCodeElimination]] — IR-level optimization passes.
- [[ONNX]] — a hardware-agnostic interchange IR.
