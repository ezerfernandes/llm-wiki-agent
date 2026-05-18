---
title: "Dive into Systems — Ch 11.5 Cache Analysis and Cachegrind"
type: source
tags: [systems, memory-hierarchy, cache, profiling, tooling, valgrind, performance]
date: 2026-05-17
source_file: https://diveintosystems.org/book/C11-MemHierarchy/cachegrind.html
---

## Summary
Chapter 11.5 of *[[DiveIntoSystems]]* introduces **[[Cachegrind]]**, the [[Valgrind]] suite's cache-simulation tool, as the empirical bridge from [[dis-11-4-caching|Ch 11.4]]'s [[CacheMemory|cache]] mechanism into measurable program behavior. Where [[dis-11-3-locality|Ch 11.3]] argued *why* [[LocalityOfReference|locality]] matters and [[dis-11-4-caching|Ch 11.4]] explained *how* hardware exploits it, **11.5 closes the loop by showing how to measure it** — running two functionally identical matrix-sum routines through Cachegrind reproduces the row-major vs column-major gap as a **17× difference in [[CacheMiss|D1 cache misses]]** (62,688 vs 1,062,996), validating the locality theory empirically. The tool simulates the **L1 instruction + data caches** and the **last-level (LL) cache**, reports instruction reads (Ir), D1 / LL read+write misses, and miss rates, and is invoked through `valgrind --tool=cachegrind`.

## Key Claims
- **Cachegrind is a [[Valgrind]] tool** — invoked via `valgrind --tool=cachegrind --cache-sim=yes ./prog`, producing a `cachegrind.out.<PID>` file that `cg_annotate` decodes into per-function / per-source-line miss counts.
- **It simulates L1 + LL, not L2** — the tool focuses on **L1 (instruction + data caches)** and the **last-level cache**, the two tiers whose behavior most directly explains runtime variation; intermediate levels are abstracted away. *"Cachegrind simulates how a program interacts with the computer's cache hierarchy."*
- **Measures Ir / D1mr / D1mw / DLmr / DLmw / ILmr** — instruction reads, plus D1 and LL **read** and **write** miss counts; miss rates are derived ratios. Reference counts cover both reads and writes.
- **Empirical validation of [[LocalityOfReference|locality]] theory** — two functionally identical matrix-averaging programs (Version 1 = row-major, Version 2 = column-major) execute **4.61× apart**; Cachegrind attributes the gap to **62,688 vs 1,062,996 D1 cache misses** — a **~17× miss-count delta** that matches the runtime ratio almost exactly, *"validating locality theory empirically"*.
- **[[RowMajorOrder|Row-major access]] preserves [[SpatialLocality|spatial locality]]** — accessing `mat[i][j]` sequentially walks one [[CacheLine|cache line]] worth of consecutive elements before crossing a line boundary; column-major `mat[j][i]` jumps full row-strides per access, defeating block-loading and inflating misses by the row-length factor.
- **`cg_annotate` for source-line attribution** — Cachegrind's raw output is reference + miss totals; `cg_annotate cachegrind.out.<PID>` decodes them per function and (with `--auto=yes`) per source line, turning the simulation into actionable diff-of-loop guidance.
- **Cache analysis ≠ algorithmic complexity** — the two versions have **identical O(N²) complexity** and identical instruction counts; only [[CacheMiss|miss rate]] differs. Cachegrind is the tool that surfaces a performance dimension invisible to big-O.

## Key Quotes
> "Cachegrind simulates how a program interacts with the computer's cache hierarchy." — opening definition; positions the tool as a **simulator** (not a hardware-counter sampler), which makes results deterministic and platform-portable.

> "Version 2 yields 1,062,996 data misses, compared to only 62,688 misses in version 1." — the headline empirical result: a ~17× miss-count delta produced by the column-major vs row-major matrix access pattern, on the same algorithm.

## Connections
- [[Cachegrind]] — **promoted from forward-reference to full concept page**; previously named-only in [[dis-11-4-caching|Ch 11.4]] and [[Valgrind]]'s tools list — now the canonical [[CacheMemory|cache]]-profiling tool page in the wiki.
- [[Valgrind]] — Cachegrind is a sibling tool to [[Memcheck]] inside the same [[Valgrind]] dynamic-binary-translation framework; the [[GccDashG|`-g`]] / [[DebugSymbol|debug-symbol]] prerequisite carries over; the ~20–100× simulation slowdown is structurally similar to Memcheck's 10–50×.
- [[CacheMiss]] — the central metric Cachegrind reports; the **3C taxonomy** (compulsory / capacity / conflict) from [[dis-11-4-caching|Ch 11.4]] is what Cachegrind quantifies, though it does not classify misses by type in its default output.
- [[CacheHit]] — implicit complement; high hit rates (>90%) correspond to the low miss counts Version 1 exhibits.
- [[CacheLine]] — the granularity at which Cachegrind tracks transfers (typically 64-byte blocks on x86-64).
- [[LocalityOfReference]] / [[SpatialLocality]] / [[TemporalLocality]] — the program properties Cachegrind measures the exploitation of; **Ch 11.5 is the empirical chapter** validating the [[dis-11-3-locality|Ch 11.3]] theory.
- [[RowMajorOrder]] — the [[CLanguage|C]] matrix layout that makes row-major traversal cache-friendly; the row-vs-column benchmark is the canonical demonstration.
- [[CacheLevel]] — Cachegrind simulates L1 + LL; the L2 abstraction is intentional simplification.
- [[CacheMemory]] / [[CacheReplacementPolicy]] / [[SetAssociativeCache]] — the structural primitives whose hit-rate impact Cachegrind measures.
- [[MemoryHierarchy]] — the structural context Cachegrind exists to instrument.
- [[dis-11-4-caching]] — *the mechanism this chapter measures*; [[dis-11-3-locality]] — *the theory this chapter validates*; [[dis-11-2-storage-devices]] — *the latency table that makes a [[CacheMiss|miss]] expensive*; [[dis-11-1-memory-hierarchy]] — *the pyramid this entire chain populates*.
- [[DiveIntoSystems]] — 110th ingested chapter; **fifth leaf of Ch 11 *The Memory Hierarchy***.
- [[SuzanneJMatthews]] / [[TiaNewhall]] / [[KevinCWebb]] — authors.

## Contradictions
None. Ch 11.5 is the empirical companion to [[dis-11-4-caching|Ch 11.4]]'s mechanism and [[dis-11-3-locality|Ch 11.3]]'s theory; the row-vs-column 5× claim from 11.3 sharpens here to a **4.61× runtime / 17× miss-count** measurement on a specific [[Cachegrind]]-instrumented matrix-sum.
