---
title: "GCC Optimization Levels"
type: concept
tags: [compilers, gcc, optimization]
sources: [dis-12-2-compiler-optimizations, dis-12-4-summary]
last_updated: 2026-05-17
---

# GCC Optimization Levels

The **`-O<N>`** flag family controls how aggressively [[GCC|GCC]] optimizes a translation unit. The four primary levels covered by [[DiveIntoSystems]] Ch 12:

| Level | Meaning | Notes |
|---|---|---|
| **`-O0`** | No optimization (default) | Statement-by-statement debuggability; large/slow binary; the regime against which Ch 12.1's manual loop-invariant motion was measured. |
| **`-O1`** | Basic optimizations | [[ConstantFolding|Constant folding]], [[DeadCodeElimination|dead-code elimination]], simple register allocation, no aggressive inlining. |
| **`-O2`** | Standard optimization | Adds more aggressive scheduling and tuning; the typical production default. |
| **`-O3`** | Aggressive optimization | Auto-enables **`-finline-functions`** ([[FunctionInlining|function inlining]]); adds vectorization and more aggressive transformations. Increases code size. |

> Sibling flags: **`-finline-functions`** (inlining; auto-on at `-O3`), **`-funroll-loops`** ([[LoopUnrolling|loop unrolling]] for known trip counts), **`-funroll-all-loops`** (aggressive, including variable trip counts). See [[dis-12-2-compiler-optimizations|Ch 12.2]].

## Ch 12 stance

[[DiveIntoSystems]] is emphatic that **most modern programs should trust the compiler** at `-O2` or `-O3` rather than performing manual [[LoopUnrolling|unrolling]] / [[FunctionInlining|inlining]] / [[ConstantFolding|folding]] in source code: *"a programmer should let the compiler optimize whenever possible"* ([[dis-12-2-compiler-optimizations]]). The chapter's empirical work shows GCC flags matching or beating manual transformations **without** sacrificing readability.

## Caveats

- [[Profiling]] / [[Benchmarking]] should still measure each level — pathological cases exist where `-O3` inlines/vectorizes counterproductively (code-size blowup, instruction-cache pressure).
- The compiler **cannot** safely optimize across opaque function calls (e.g., `sqrt`) — manual [[HotSpot|loop-invariant code motion]] from [[dis-12-1-first-steps|Ch 12.1]] sometimes beats `-O3`.
- Memory-access-pattern optimizations ([[dis-12-3-memory-considerations|Ch 12.3]] loop interchange) are largely **outside** the `-O<N>` mandate — the programmer must do them by hand.

## Not the same as Rust `opt-level`

Rust / [[Rustc|`rustc`]]'s `-C opt-level` flag has a related but **distinct** taxonomy (`0` / `1` / `2` / `3` / `"s"` / `"z"`) — see [[OptLevel]]. Both inherit from the LLVM optimization pipeline but expose different defaults and size-vs-speed knobs.

## Connections

- [[GCC]] — the compiler.
- [[CompilerOptimization]] — parent concept.
- [[FunctionInlining]] / [[LoopUnrolling]] / [[ConstantFolding]] / [[DeadCodeElimination]] — the individual optimizations controlled by these levels.
- [[OptLevel]] — Rust/`rustc` analog with different taxonomy.
- [[Profiling]] / [[Benchmarking]] — the empirical-measurement tools that justify level selection.
- [[dis-12-2-compiler-optimizations]] / [[dis-12-4-summary]] — canonical sources.
