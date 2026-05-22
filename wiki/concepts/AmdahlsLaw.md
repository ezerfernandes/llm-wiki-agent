---
title: "Amdahl's Law"
type: concept
tags: [parallel-computing, performance, scaling, theory, multicore]
sources: [dis-14-4-1-performance-basics, dis-14-4-performance]
last_updated: 2026-05-18
---

# Amdahl's Law

**Amdahl's Law** (Gene Amdahl, 1967) is the **theoretical ceiling** on [[ParallelSpeedup|speedup]] imposed by the serial fraction of a program. [[DiveIntoSystems]] [[dis-14-4-1-performance-basics|Ch 14.4.1]] formalizes it; prior wiki pages ([[Speedup]] from [[dis-14-1-multicore|Ch 14.1.2]]) had named it as a forward reference but deferred coverage.

## Statement

Let $S$ be the **serial fraction** of a computation (the part that must execute sequentially) and $P = 1 - S$ the **parallelizable fraction**. With $c$ cores:

$$\text{Speedup}(c) = \frac{1}{S + P/c}$$

## Asymptotic ceiling

As $c \to \infty$, $P/c \to 0$, so:

$$\lim_{c \to \infty} \text{Speedup}(c) = \frac{1}{S}$$

**The serial fraction alone caps achievable speedup**, no matter how many cores are thrown at the problem.

## Worked example (DIS)

A program is **90% parallelizable** ($S = 0.10$, $P = 0.90$):

| Cores | Speedup | Efficiency |
|---|---|---|
| 2 | $1/(0.10 + 0.45) = 1.82$ | 0.91 |
| 4 | $1/(0.10 + 0.225) = 3.08$ | 0.77 |
| 8 | $1/(0.10 + 0.1125) = 4.71$ | 0.59 |
| 16 | $1/(0.10 + 0.05625) = 6.40$ | 0.40 |
| 64 | $1/(0.10 + 0.0141) = 8.77$ | 0.14 |
| ∞ | $1/0.10 = 10.0$ | 0.00 |

**10× is the ceiling**, regardless of how much hardware is added.

## Pessimistic framing

Amdahl's Law produces **pessimistic projections** for high-core systems:
- Even 95% parallelizable code caps at **20× speedup**.
- Even 99% parallelizable code caps at **100× speedup** (still only useful for ~100 cores).
- The serial fraction matters *more* the more cores you add.

This pessimism is the **motivation for [[GustafsonsLaw|Gustafson-Barsis Law]]**, which inverts Amdahl's fixed-problem-size assumption.

## What's "serial"

- **Initialization** — read input, allocate buffers, set up data structures.
- **Reduction** — combine per-thread results into a final answer.
- **I/O** — file reads, network calls, output.
- **Critical sections** — code inside [[Mutex|mutex]] locks.
- **Dependency chains** — any computation where step $n$ requires step $n-1$ (e.g., generating Fibonacci numbers — see [[dis-14-4-1-performance-basics|Ch 14.4.1]]).

## Assumption critique (leads into Gustafson)

Amdahl assumes **problem size is fixed**. In practice, larger machines are deployed against larger problems — Gustafson's empirical observation that core count $c$ and parallel fraction $P$ are *"virtually never independent."* [[GustafsonsLaw|Gustafson-Barsis Law]] re-derives speedup under the **scaled-problem** assumption and produces a much more optimistic result for [[WeakScaling|weak scaling]].

## Connections

- [[ParallelSpeedup]] — the metric Amdahl bounds.
- [[ParallelEfficiency]] — Amdahl's ceiling drives the efficiency-decay curve.
- [[GustafsonsLaw]] — the problem-scaling alternative that critiques Amdahl's fixed-problem assumption.
- [[StrongScaling]] — the regime Amdahl directly bounds (fixed problem size, grow cores).
- [[WeakScaling]] — the regime where Gustafson dominates and Amdahl's ceiling is less relevant.
- [[Speedup]] — the prior wiki page on the informal 1/c rule that Amdahl bounds formally.
- [[CriticalPath]] — the dependency-chain concept Amdahl's serial fraction captures.
- [[ParallelComputing]] / [[SharedMemoryParallelism]] — the paradigms Amdahl governs.
- [[dis-14-4-1-performance-basics]] — primary DIS source.
- [[parproc-ch01-intro-parallel-processing]] — earlier corpus coverage referenced from [[Speedup]].
