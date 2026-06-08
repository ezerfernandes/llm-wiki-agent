---
title: "Amdahl's Law"
type: concept
tags: [parallel-computing, performance, scaling, theory, multicore]
sources: [dis-14-4-1-performance-basics, dis-14-4-performance, mlsysbook-ch02-ml-systems, mlsysbook-ch04-data-engineering, mlsysbook-ch11-hardware-acceleration, mlsysbook-ch12-benchmarking, mlsysbook-ch16-conclusion]
last_updated: 2026-06-05
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

## In ML deployment ([[mlsysbook-ch02-ml-systems|mlsysbook Ch 2]])

Reddi applies Amdahl's Law to ML *pipelines*, where the model is one stage of many. A smartphone camera pipeline (100 ms ISP + 60 ms ML scene classification + 40 ms postprocessing = 200 ms) gains only **1.37×** from a 10× faster ML stage — and even an infinitely fast model yields just 1.43×, because the non-ML 70% is untouched. Since ML inference is typically 30–50% of production pipelines, even a 100× model speedup yields only ~1.4–2× end-to-end. This is the "model optimization translates linearly to system speedup" *fallacy*; the [[BottleneckPrinciple|bottleneck principle]] is the operational corollary.

## Connections

- [[ParallelSpeedup]] — the metric Amdahl bounds.
- [[BottleneckPrinciple]] — the ML-systems operationalization of Amdahl's Law (optimize the slowest stage).
- [[ParallelEfficiency]] — Amdahl's ceiling drives the efficiency-decay curve.
- [[GustafsonsLaw]] — the problem-scaling alternative that critiques Amdahl's fixed-problem assumption.
- [[StrongScaling]] — the regime Amdahl directly bounds (fixed problem size, grow cores).
- [[WeakScaling]] — the regime where Gustafson dominates and Amdahl's ceiling is less relevant.
- [[Speedup]] — the prior wiki page on the informal 1/c rule that Amdahl bounds formally.
- [[CriticalPath]] — the dependency-chain concept Amdahl's serial fraction captures.
- [[ParallelComputing]] / [[SharedMemoryParallelism]] — the paradigms Amdahl governs.
- [[dis-14-4-1-performance-basics]] — primary DIS source.
- [[parproc-ch01-intro-parallel-processing]] — earlier corpus coverage referenced from [[Speedup]].
- [[mlsysbook-ch02-ml-systems]] — the ML-deployment-pipeline application.
- [[mlsysbook-ch04-data-engineering]] — applies Amdahl to **distributed data processing**: embarrassingly-parallel KWS feature extraction gets ~64× on 64 cores, but coordination-heavy global normalization only ~10× due to the serial aggregation phase; the [[MapReduce]] compute-follows-data "coordination tax."
- [[mlsysbook-ch11-hardware-acceleration]] — "Amdahl's Law for AI" is the chapter's "acceleration wall": a 247× H100 matmul advantage yields only ~18× on compute-bound ResNet-50 ($p$=0.95) and ~5× on memory-bound GPT-2 ($p$=0.80, ceiling $1/(1-p)$=5×) — *why* LLM inference optimization targets the serial fraction (batching, speculative decoding) over raw silicon, and why multi-chip scaling stalls beyond 64–128 accelerators (gradient-sync serial fraction).
- [[mlsysbook-ch12-benchmarking]] — Ch 12 makes Amdahl the **benchmarking optimization ceiling**: a 3–5× model-inference speedup yields ≪3–5× end-to-end when preprocessing/queuing dominate (8 ms preprocess + 10 ms infer, 5× infer speedup → only 1.8× end-to-end; ceiling $1/f$). It explains why model-only vendor speedups mislead and why [[TailLatency|end-to-end latency breakdown]] must be reported.
- [[mlsysbook-ch16-conclusion]] — the conclusion makes Amdahl's Law invariant #8 of the [[ThirteenQuantitativeInvariants|thirteen]] ("the serial fraction caps all parallelism gains") and the "optimize a single pipeline stage without profiling" pitfall: a 10× speedup of a 10%-of-latency stage yields only ~1.1× system speedup — "engineers who optimize without profiling are guessing, and Amdahl's Law is unforgiving."
