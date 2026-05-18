---
title: "Dive into Systems — Ch 12.2 Other Compiler Optimizations: Loop Unrolling and Function Inlining"
type: source
tags: [systems, optimization, compilers, gcc, inlining, loop-unrolling]
date: 2026-05-17
source_file: https://diveintosystems.org/book/C12-CodeOpt/loops_functions.html
---

## Summary
Chapter 12.2 of *[[DiveIntoSystems]]* is the **second leaf** of Ch 12 *Code Optimization*. It surveys two classical optimizations — **[[LoopUnrolling|loop unrolling]]** and **[[FunctionInlining|function inlining]]** — that **modern [[GCC|GCC]] performs automatically** and that programmers **should generally leave to the compiler**. Inlining replaces a function call with the callee body, enabling downstream **[[ConstantFolding|constant folding]]**, **constant propagation**, and **[[DeadCodeElimination|dead-code elimination]]**. Loop unrolling reduces iteration count by factor `n` while increasing per-iteration work by `n`, eliminating branch overhead. Both are exposed as [[GccOptLevels|GCC flags]] — `-finline-functions` (auto-enabled at `-O3`), `static inline` keyword hint, `-funroll-loops`, `-funroll-all-loops` — but the chapter's headline recommendation is *"code today is more often read than it is written... a programmer should let the compiler optimize whenever possible."*

## Key Claims
- **[[FunctionInlining|Function inlining]]** — *"eliminates these excessive calls, and makes it easier for the compiler to identify other potential improvements, including [[ConstantFolding|constant propagation, constant folding]], and [[DeadCodeElimination|dead code elimination]]"*.
- **[[GCC|GCC]] inlining controls**: `-finline-functions` is automatically on at `-O3`; `static inline` keyword tells the compiler the function is inlining-eligible; **inlining decision remains the compiler's** — the keyword is a hint, not a directive.
- **[[LoopUnrolling|Loop unrolling]]** — for `n`-factor unrolling, iteration count drops by factor `n` and per-iteration work rises by factor `n`; 2-factor unroll of `isPrime`'s divisibility loop checks both `i` and `i+1` per iteration.
- **GCC unrolling flags**: `-funroll-loops` (unrolls loops with compile-time-known trip counts); `-funroll-all-loops` (aggressively unrolls all loops including variable-trip-count ones — riskier).
- **Empirical result on 5,000,000-prime benchmark**: manual unrolling yielded only **marginal** runtime improvements; the GCC flags produced comparable speedups **without sacrificing readability**.
- **Readability trade-off**: manual inlining *"significantly reducing the readability of code, increasing the likelihood of errors, and making it harder to update and maintain functions"* — the chapter's central caution.
- **Headline recommendation**: *"Code today is more often read than it is written... a programmer should let the compiler optimize whenever possible."*

## Key Quotes
> "Function inlining eliminates these excessive calls, and makes it easier for the compiler to identify other potential improvements, including constant propagation, constant folding, and dead code elimination."

> "Code today is more often read than it is written... a programmer should let the compiler optimize whenever possible."

## Connections
- [[DiveIntoSystems]] — **115th ingested chapter — second leaf of Ch 12**.
- [[dis-12-1-first-steps|Ch 12.1]] — directly preceding leaf; established the profile-first methodology this chapter applies to compiler-side optimizations.
- [[LoopUnrolling]] — extends the existing CUDA-flavored page with DIS's GCC-flag treatment.
- [[FunctionInlining]] — new concept page.
- [[ConstantFolding]] — new concept page (downstream of inlining).
- [[DeadCodeElimination]] — new concept page (downstream of inlining).
- [[GccOptLevels]] — new concept page covering `-O0` / `-O1` / `-O2` / `-O3` and the `-finline-functions` / `-funroll-loops` flags.
- [[GCC]] — the compiler whose flags this chapter exposes.
- [[CompilerOptimization]] — umbrella concept.
- [[CCompiler]] — the agent the chapter recommends trusting.
- [[SuzanneJMatthews]] / [[TiaNewhall]] / [[KevinCWebb]] — authors.

## Contradictions
None. Aligns with the wiki's existing *"let the compiler do it"* stance from [[dis-9-3-arm64-arithmetic]].
