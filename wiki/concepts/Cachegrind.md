---
title: "Cachegrind"
type: concept
tags: [profiling, cache, valgrind, tooling, performance, dynamic-analysis]
sources: [dis-11-5-cachegrind, dis-11-4-caching, dis-3-3-valgrind]
last_updated: 2026-05-17
---

# Cachegrind

**Cachegrind** is the **[[CacheMemory|cache]]-simulation tool** in the [[Valgrind]] dynamic-binary-translation suite. It runs an unmodified binary through a synthetic CPU + simulated cache hierarchy and counts every [[CacheHit|hit]] and [[CacheMiss|miss]] — turning the [[dis-11-3-locality|locality]] theory of [[dis-11-3-locality|DIS Ch 11.3]] and the [[dis-11-4-caching|cache mechanism]] of [[dis-11-4-caching|Ch 11.4]] into **measurable, per-source-line numbers**.

Per [[dis-11-5-cachegrind|DIS Ch 11.5]]: *"Cachegrind simulates how a program interacts with the computer's cache hierarchy."*

## What it measures

Cachegrind simulates two tiers — **L1** (split instruction + data caches) and the **last-level cache (LL)** — and reports six core counters plus derived miss rates:

| Counter | Meaning |
|---|---|
| **Ir**   | Instruction reads (total dynamic instruction count) |
| **I1mr** | L1 instruction-cache misses |
| **ILmr** | LL instruction-cache misses |
| **Dr**   | Data reads |
| **Dw**   | Data writes |
| **D1mr / D1mw** | L1 data read / write misses |
| **DLmr / DLmw** | LL data read / write misses |

Miss rates are derived ratios (`D1mr / Dr`, etc.). The default output is one row of totals per executable; `cg_annotate` decodes the `cachegrind.out.<PID>` file into per-function and per-source-line breakdowns.

**Why L1 + LL only**: [[dis-11-5-cachegrind|Ch 11.5]] notes the tool *"focuses on these tiers because L1 has low associativity and LL significantly impacts runtime"* — the intermediate L2 is abstracted away to keep the simulation tractable.

## Invocation

```bash
gcc -g matrix.c -o matrix                # -g for cg_annotate source-line mapping
valgrind --tool=cachegrind --cache-sim=yes ./matrix
cg_annotate cachegrind.out.<PID>         # decode totals + per-function breakdown
cg_annotate --auto=yes cachegrind.out.<PID>   # add per-source-line breakdown
```

- `--tool=cachegrind` selects Cachegrind (default tool is [[Memcheck]]).
- `--cache-sim=yes` enables full cache simulation (otherwise only branch prediction).
- `--I1=`, `--D1=`, `--LL=` override the auto-detected cache geometry (`size,associativity,line_size`) to simulate a different machine.
- The output file `cachegrind.out.<PID>` is binary-ish text — `cg_annotate` is the consumer.

## Headline empirical result (matrix-sum benchmark)

The chapter's pedagogical anchor — two functionally identical matrix-averaging routines:

| Version | Access pattern | Runtime | D1 misses | Miss rate |
|---|---|---|---|---|
| **1** | row-major `mat[i][j]` ([[RowMajorOrder|C-natural]]) | 1× | **62,688** | low |
| **2** | column-major `mat[j][i]` (cache-hostile) | **4.61×** | **1,062,996** | **~17× higher** |

Same algorithm, same instruction count (Ir identical to within a percent), same big-O — **only [[SpatialLocality|spatial locality]] differs**. Cachegrind surfaces the dimension that algorithmic complexity hides: the row-major version walks one [[CacheLine|cache line]] worth of consecutive `int`s before crossing a line boundary; the column-major version jumps a full row-stride (typically ≫64 bytes) per access, defeating the block-load.

## Relationship to [[Valgrind]]

Cachegrind is a **sibling of [[Memcheck]]** inside [[Valgrind]]:

| Tool | Role | Slowdown |
|---|---|---|
| **[[Memcheck]]** (default) | Heap-error detection ([[UninitializedReadError]] / [[UseAfterFree]] / [[MemoryLeak]] / [[BufferOverflow]]) | ~10–50× |
| **Cachegrind** | Cache simulation + miss profiling | ~20–100× |
| **callgrind** | Cachegrind + call-graph instrumentation | similar |
| **helgrind** / **DRD** | Race detection | ~10–50× |

All four share the [[Valgrind]] dynamic-binary-translation framework — the program is **recompiled into instrumented intermediate code on the fly**, then run on a synthetic CPU. This is why Cachegrind:
- **needs no recompilation** — any unmodified binary works (though `-g` is required for source-line attribution via `cg_annotate`);
- **is deterministic** — results are reproducible across machines (it simulates a *specified* cache geometry, not the host machine's actual hardware counters);
- **is slow** — the 20–100× overhead is the price of simulation; on tiny benchmarks this is fine, on production workloads it requires a representative subset.

## Cachegrind vs hardware performance counters

Cachegrind is a **simulator**, not a sampler. The alternative — `perf stat -e cache-misses ./prog` on Linux, Instruments on macOS — reads **hardware performance counters** directly from the actual CPU's cache controller.

| Dimension | Cachegrind (simulation) | `perf` / Instruments (HW counters) |
|---|---|---|
| **Accuracy** | Exact (simulated) | Sampled / approximate |
| **Overhead** | ~20–100× | Near zero |
| **Determinism** | Reproducible | Varies with CPU state, neighbors |
| **Geometry** | Configurable (`--D1=...`) | Fixed to host CPU |
| **Granularity** | Per-source-line via `cg_annotate` | Per-function (or hot-spot) |
| **Source-line attribution** | First-class (with `-g`) | Requires symbol resolution |

[[dis-11-5-cachegrind|Ch 11.5]] uses Cachegrind because the chapter teaches the **theory** — and a simulator that produces clean, deterministic, source-line-attributable miss counts is pedagogically more useful than a noisy hardware sampler.

## Workflow integration

Typical performance-debugging chain:

1. **Detect a slowdown** — wall-clock benchmark shows two semantically equivalent code paths diverging.
2. **Run Cachegrind** — `valgrind --tool=cachegrind --cache-sim=yes ./prog` on each path.
3. **Annotate** — `cg_annotate cachegrind.out.<PID>` → see which functions / lines have anomalous D1mr or DLmr counts.
4. **Cross-check** with `perf stat -e LLC-load-misses ./prog` on real hardware.
5. **Fix** — reorder loops ([[RowMajorOrder|row-major traversal]]), reshape data (struct-of-arrays vs array-of-structs), tile / block ([[LoopTiling|loop tiling]]), prefetch ([[PrefetchInstruction|`__builtin_prefetch`]]).
6. **Verify** — re-run Cachegrind; D1mr should drop.

## Scope boundary

- **What Cachegrind sees**: data and instruction memory references, cache-hit/miss outcomes per the simulated L1 + LL geometry, branch predictions (with `--branch-sim=yes`).
- **What it does NOT see**: actual wall-clock time (only miss *counts*, not penalties); TLB behavior (use `valgrind --tool=callgrind` or hardware counters); inter-core [[CacheCoherency|coherence]] traffic or [[FalseSharing|false sharing]] (single-thread / abstract cache only); [[DRAM]] / memory-bus saturation; speculative execution effects.

## Connections

- [[Valgrind]] — the parent dynamic-binary-translation framework; Cachegrind is one of several tools inside it. Same `-g` / [[DebugSymbol|debug-symbol]] prerequisite, same per-PID output convention, same recompile-on-the-fly mechanism.
- [[Memcheck]] — sibling [[Valgrind]] tool for heap-error detection — orthogonal but commonly run alongside Cachegrind on the same binary.
- [[CacheMiss]] — the primary metric Cachegrind reports; the **3C taxonomy** (compulsory / capacity / conflict) from [[dis-11-4-caching|Ch 11.4]] is what miss counts quantify (though Cachegrind doesn't classify by 3C class in default output).
- [[CacheHit]] — implicit complement; hit rate = 1 − miss rate.
- [[CacheLine]] — the granularity at which Cachegrind tracks transfers (typically 64-byte blocks).
- [[CacheLevel]] — Cachegrind simulates L1 + LL; L2 abstracted away.
- [[CacheMemory]] / [[SetAssociativeCache]] / [[CacheReplacementPolicy]] / [[LeastRecentlyUsed]] — the mechanism Cachegrind simulates.
- [[LocalityOfReference]] / [[SpatialLocality]] / [[TemporalLocality]] / [[WorkingSet]] — the program properties Cachegrind makes measurable.
- [[RowMajorOrder]] — the [[CLanguage|C]] layout invariant whose alignment / misalignment with traversal order produces the 17× miss-count gap.
- [[MemoryHierarchy]] — the structural context Cachegrind exists to instrument.
- [[AddressSanitizer]] — orthogonal compile-time-instrumented alternative for memory-error detection (not cache profiling).
- [[GccDashG]] / [[DebugSymbol]] — the build-side prerequisite for `cg_annotate` source-line mapping.
- [[DiveIntoSystems]] / [[dis-11-5-cachegrind]] / [[dis-11-4-caching]] / [[dis-3-3-valgrind]] — introducing sources.
