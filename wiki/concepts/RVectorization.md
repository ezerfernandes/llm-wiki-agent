---
title: "R Vectorization"
type: concept
tags: [r-language, performance, functional-programming]
sources: [parproc-appC-r-quick-start]
last_updated: 2026-05-17
---

# R Vectorization

In [[Rlanguage|R]], *vectorization* means writing code that operates on entire vectors, matrices, or data frames in a single call to a compiled built-in function, rather than using an interpreted `for` loop in R code. Because R's built-in functions (`sum`, `mean`, `apply`, `ifelse`, `%*%`, etc.) are implemented in C or Fortran, they run many hundreds of times faster than equivalent R-level loops.

This is distinct from hardware [[Vectorization|SIMD vectorization]] (executing one instruction on multiple data lanes). R vectorization is a *language-level* technique: it shifts work from R's interpreter into pre-compiled code.

## Performance Impact

[[NormMatloff]] benchmarks the difference in [[parproc-appC-r-quick-start]] §C.4:

```r
x <- runif(1000000)
system.time(sum(x))
# elapsed: 0.006 s

system.time({ s <- 0; for (i in 1:1000000) s <- s + x[i] })
# elapsed: 2.859 s
```

A ~476× speedup from replacing a loop with a single built-in call. The gains compound in [[Snow]]-based parallel R programs, where each worker function should itself be vectorized.

## Recycling

[[Rlanguage|R]] has no scalar type: `2.5` is a one-element vector. When binary operations involve mismatched lengths, R *recycles* the shorter operand by repeating it to match the longer. Example: `2.5 * matrix` recycles `2.5` to a conforming all-2.5 matrix before element-wise multiplication. Explicit vectorized conditionals use `ifelse(bool_vec, yes_vec, no_vec)`.

## Key Vectorized Idioms

| Pattern | Idiom |
|---|---|
| Count elements satisfying predicate | `sum(x %% 2 == 1)` |
| Boolean mask extraction | `x[x > 0]` |
| Vectorized conditional | `ifelse(cond, yes, no)` |
| Apply function to matrix rows/cols | `apply(m, 1, f)` / `apply(m, 2, f)` |
| Map over list | `lapply(lst, f)` / `sapply(lst, f)` |
| Reduce list elements | `Reduce(sum, lst)` |

## Connections

- [[Rlanguage]] — the language this applies to.
- [[parproc-appC-r-quick-start]] — primary source; §C.4 and §C.7 define and benchmark vectorization.
- [[Snow]] — R parallel package; worker functions should be vectorized.
- [[Vectorization]] — hardware SIMD vectorization (distinct sense).
- [[DataFrame]] — operations on data frames also benefit from vectorized idioms.
