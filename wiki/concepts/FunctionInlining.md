---
title: "Function Inlining"
type: concept
tags: [compilers, optimization, gcc]
sources: [dis-12-2-compiler-optimizations, dis-12-4-summary]
last_updated: 2026-05-17
---

# Function Inlining

A [[CompilerOptimization|compiler optimization]] that **replaces a function call with the body of the callee** in place. Beyond saving the call/return overhead, inlining is a **gateway optimization** — once the body is exposed at the call site, the compiler can perform [[ConstantFolding|constant folding]], constant propagation, and [[DeadCodeElimination|dead-code elimination]] across what was previously a function boundary ([[dis-12-2-compiler-optimizations]]).

> *"Function inlining eliminates these excessive calls, and makes it easier for the compiler to identify other potential improvements, including constant propagation, constant folding, and dead code elimination."* — [[DiveIntoSystems]] Ch 12.2

## GCC controls

- **`-finline-functions`** — auto-enabled at **`-O3`** ([[GccOptLevels]]).
- **`static inline`** keyword — a programmer **hint**, not a directive; the compiler retains the inlining decision.
- The compiler may **decline** to inline very large functions, recursive calls, or functions whose addresses are taken.

## Trade-offs

[[DiveIntoSystems]] cautions against **manual inlining** by the programmer — it "*significantly reducing the readability of code, increasing the likelihood of errors, and making it harder to update and maintain functions"* ([[dis-12-2-compiler-optimizations]]). The chapter's closing advice in [[dis-12-4-summary|Ch 12.4]]: split complex operations into multiple small functions for readability — modern compilers will inline back when profitable.

**Costs**: code-size growth (instruction-cache pressure), longer compile times. **Benefits**: call overhead removed, downstream optimizations enabled, register-allocation flexibility increased.

## Connections

- [[CompilerOptimization]] — parent concept.
- [[GCC]] / [[GccOptLevels]] — the toolchain that performs inlining; `-O3` enables `-finline-functions`.
- [[ConstantFolding]] / [[DeadCodeElimination]] — the downstream optimizations inlining unlocks.
- [[LoopUnrolling]] — sister classical optimization, also covered in [[dis-12-2-compiler-optimizations|Ch 12.2]].
- [[dis-12-2-compiler-optimizations]] / [[dis-12-4-summary]] — canonical sources.
