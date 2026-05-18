---
title: "Definite Iteration"
type: concept
tags: [control-flow, iteration, design-rule]
sources: [dis-1-3-conditionals-loops]
last_updated: 2026-05-17
---

# Definite Iteration

**Definite iteration** is the family of loops whose **iteration count is known (or knowable) before the loop starts** — counting from `0` to `n`, walking over a fixed-size array, stepping over a range of indices. It contrasts with [[IndefiniteIteration]], where the loop runs *until* a condition emerges with no a-priori bound.

## In [[CLanguage|C]]

Per [[dis-1-3-conditionals-loops|DiS Ch 1.3]]: although [[ForLoop|`for`]] and [[WhileLoop|`while`]] are *equivalent in expressive power*, [[DiveIntoSystems]] recommends the [[ForLoop|`for` loop]] for **definite iteration** because its three clauses — *init*, *condition*, *step* — surface the iteration count at the top of the loop:

```c
for (int i = 0; i < n; i++) {
    /* body */
}
```

A reader can see `i = 0`, `i < n`, `i++` at a glance and know the loop runs `n` times. The same logic in a [[WhileLoop|`while`]] form distributes the loop variable across three places (declaration above, test in the head, step inside the body), making the iteration count harder to read.

## Why the distinction matters

- **Readability** — choosing the right loop form telegraphs intent.
- **Bounded-correctness reasoning** — definite-iteration loops have a static termination argument (count goes from a known start to a known bound).
- **Compiler optimization** — definite-iteration loops with affine bounds are amenable to loop unrolling, vectorization, and parallel-for transformations.

## Connections

- [[dis-1-3-conditionals-loops]] — source.
- [[IndefiniteIteration]] — the contrasting family; pairs with [[WhileLoop]].
- [[ForLoop]] — the C construct of choice.
- [[WhileLoop]] — equivalent-in-power alternative; usually preferred for indefinite.
- [[ControlFlow]] / [[CLanguage]] / [[DiveIntoSystems]].
