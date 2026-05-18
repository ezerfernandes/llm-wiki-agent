---
title: "Dead Code Elimination"
type: concept
tags: [compilers, optimization, gcc]
sources: [dis-12-2-compiler-optimizations]
last_updated: 2026-05-17
---

# Dead Code Elimination

A [[CompilerOptimization|compiler optimization]] (often abbreviated **DCE**) that **removes code whose results are never used** or **code that is unreachable**. Two flavors:

1. **Unreachable-code elimination** — statements after a `return`, branches of an `if (0) { ... }`, or code following an infinite loop.
2. **Dead-assignment elimination** — assignments to variables that are never read before being overwritten or going out of scope.

[[DiveIntoSystems]] names DCE alongside [[ConstantFolding|constant folding]] and constant propagation as the **downstream optimizations that [[FunctionInlining|function inlining]] enables** — once a function body is exposed at the call site with concrete argument values, entire branches can be proved dead and pruned ([[dis-12-2-compiler-optimizations]]).

## Example

```c
int x = compute();
if (0) {            // unreachable — entire block eliminated
    printf("%d", x);
}
x = 5;              // previous compute() result is dead — call may be eliminated
return x;
```

After DCE, the `if` body is removed; if `compute()` is **pure**, the entire call is also eliminated because its result is dead.

## GCC

Performed at `-O1` and above as part of [[GCC|GCC]]'s standard optimization pipeline. Composes tightly with **constant folding** (folded constants often render branches unreachable), **constant propagation**, and **[[FunctionInlining|inlining]]** (which exposes dead branches across function boundaries).

## Connections

- [[CompilerOptimization]] — parent concept.
- [[FunctionInlining]] — the optimization that exposes new dead-code opportunities.
- [[ConstantFolding]] — frequently produces the constants that prove branches dead.
- [[GCC]] / [[GccOptLevels]] — enabled at `-O1` and above.
- [[dis-12-2-compiler-optimizations]] — canonical [[DiveIntoSystems]] source.
