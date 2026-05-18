---
title: "Constant Folding"
type: concept
tags: [compilers, optimization, gcc]
sources: [dis-12-2-compiler-optimizations]
last_updated: 2026-05-17
---

# Constant Folding

A [[CompilerOptimization|compiler optimization]] that **evaluates constant expressions at compile time** rather than at runtime. The expression `3 * 4 + 7` is folded to the literal `19` during compilation, eliminating the arithmetic instructions entirely. Closely related to **constant propagation** — once a variable is known to hold a constant, every subsequent use can be replaced by the literal, exposing further folding opportunities.

[[DiveIntoSystems]] names constant folding alongside constant propagation and [[DeadCodeElimination|dead code elimination]] as the **downstream optimizations that [[FunctionInlining|function inlining]] enables**: once a callee's body is visible at a call site with constant arguments, folding can collapse entire expression chains ([[dis-12-2-compiler-optimizations]]).

## Example

```c
int x = 4;
int y = x * 3 + 1;   // after folding: int y = 13;
```

After **constant propagation** replaces `x` with `4`, **constant folding** evaluates `4 * 3 + 1` to `13` at compile time. If `y` is subsequently never used, [[DeadCodeElimination|dead-code elimination]] removes the assignment entirely.

## GCC

Enabled by default at all optimization levels (`-O1` and above) — it is one of the cheapest and safest transformations in the [[GCC|GCC]] pipeline. Composes with **constant propagation**, **algebraic simplification** (`x * 1 → x`, `x + 0 → x`), and **strength reduction** (`x * 8 → x << 3`).

## Connections

- [[CompilerOptimization]] — parent concept.
- [[FunctionInlining]] — the optimization that exposes new folding opportunities by collapsing call-site boundaries.
- [[DeadCodeElimination]] — frequently follows folding when results become unused.
- [[GCC]] / [[GccOptLevels]] — folding is on at `-O1` and above.
- [[dis-12-2-compiler-optimizations]] — canonical [[DiveIntoSystems]] source.
