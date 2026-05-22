---
title: "Dive into Systems — Ch 14.5 Cache Coherence and False Sharing"
type: source
tags: [dive-into-systems, textbook, parallel-programming, cache-coherence, false-sharing, multicore]
date: 2026-05-18
source_file: https://diveintosystems.org/book/C14-SharedMemory/cache_coherence.html
---

## Summary

**Fifth leaf** of Ch 14 *Leveraging Shared Memory in the Multicore Era* of *[[DiveIntoSystems]]* — pivots from [[dis-14-4-performance|Ch 14.4]]'s performance metrics into the **hardware-level subtlety** that destroys parallel speedup even when synchronization is correct: **[[CacheCoherency|cache coherence]]** and its pathological inverse, **[[FalseSharing|false sharing]]**. Codifies the [[SnoopingProtocol|snooping]] mechanism (per-core L1 caches monitor the [[MemoryBus|memory bus]] for writes and invalidate matching lines) and the **write-invalidate** family of protocols — [[MSI|MSI]] / [[MESI|MESI]] / MESIF — where any write to a shared [[CacheLine|cache line]] invalidates **every other copy** across the chip. The chapter's **headline failure mode**: writes to *different* array elements that happen to share a [[CacheLine|cache line]] trigger the same invalidation cascade as true sharing — the cache thrashes without any data contention. Measured pathology — runtime climbs **0.34 s (1 thread) → 0.80 s (2 threads) → 0.77 s (4 threads)** on the per-thread counter array, the **opposite of [[ParallelSpeedup|speedup]]**.

## Key Claims

- **[[CacheCoherency|Cache coherence]] is a hardware invariant**: on a [[MulticoreProcessor|multicore]] chip, when one core modifies a memory location, every other core that has cached the same location must see the update — otherwise reads return stale values and shared memory parallelism breaks. The hardware (not the programmer) enforces this.
- **[[SnoopingProtocol|Snoopy caches]] are the dominant mechanism**: each core's L1 cache monitors the [[MemoryBus|memory bus]] for write signals and invalidates entire [[CacheLine|cache lines]] when another core writes to a matching address — *"every write to counts invalidates the entire line in every other L1 cache."*
- **The [[MSI|MSI]] / [[MESI|MESI]] family is **write-invalidate**: a single write to a shared line transitions every other copy to the **Invalid** state. The next read on those cores misses the L1 and re-fetches the line — correctness preserved, performance taxed.
- **[[FalseSharing|False sharing]] is the silent killer**: when multiple threads update **different array elements** that reside on the **same [[CacheLine|cache line]]**, the coherence hardware cannot distinguish independent writes from true sharing. Every write to any element invalidates every cached copy on every other core — *"repeated conflicts in the cache cause a series of misses"*. No data race, no synchronization needed, no bug visible to the programmer — yet performance collapses.
- **Empirical pathology**: DIS measures runtime on a parallel counter-increment loop where each thread updates its own array slot. Sequential baseline runs in **0.34 s**. With 2 threads, runtime jumps to **0.80 s** (the **opposite** of [[ParallelSpeedup|speedup]] — slowdown to ~0.43× of serial). With 4 threads, **0.77 s** — still slower than serial. The cache-line thrashing dominates the parallel work.
- **Two canonical mitigations**: (1) **local thread-private accumulators** — each thread updates its own private variable on its private stack, then writes the result once to a shared array at the end (eliminates the per-iteration shared-line contact entirely — same coarse-grained-update lesson as [[dis-14-3-1-mutex|14.3.1's]] mutex optimization); (2) **cache-line padding** — pad each thread's slot to a full [[CacheLine|cache line]] so no two threads ever share a line (architecturally explicit, less portable).

## Key Quotes

> "every write to counts invalidates the entire line in every other L1 cache"

> "repeated conflicts in the cache cause a series of misses"

## Connections

- [[DiveIntoSystems]] — parent textbook; this is the **fifth leaf** of Ch 14 *Leveraging Shared Memory in the Multicore Era*.
- [[dis-14-4-2-performance-advanced]] — immediate predecessor (closed Ch 14.4); 14.5 opens the **hardware-pathology** arc that subverts the performance theory just established.
- [[dis-11-6-cache-coherency]] — Part III precursor; this section is the **multicore-programming application** of the cache-coherence hardware story Ch 11.6 laid down.
- [[CacheCoherency]] — central concept; this section is its parallel-programming-perspective treatment.
- [[FalseSharing]] — central concept; this section is one of its canonical introductions.
- [[CacheLine]] — the granularity unit at which coherence operates and false sharing emerges.
- [[MESI]] / [[MSI]] — the write-invalidate protocol family.
- [[SnoopingProtocol]] — the bus-monitoring mechanism.
- [[MemoryBus]] — the substrate snoopy caches watch.
- [[CacheInvalidation]] — the action coherence triggers on remote writes.
- [[ParallelSpeedup]] — what false sharing destroys (here measured at <1× — actual slowdown).
- [[dis-14-3-1-mutex]] — sibling pattern: same *thread-private accumulators* mitigation applies to both lock contention and false sharing.
- [[MulticoreProcessor]] — the substrate on which coherence and false sharing exist.

## Contradictions

- None. Extends [[CacheCoherency]] / [[FalseSharing]] / [[MESI]] (introduced from the [[ParallelProcessorsAlgorithms|ParProc]] corpus) into the explicit-Pthreads-programmer context. The DIS pathology measurements (0.34 → 0.80 s slowdown) are the first empirical numbers in the wiki for this failure mode.

## Notes

- **136th ingested DIS chapter — opens Ch 14.5.** No new concept pages — fully reuses the existing [[CacheCoherency]] / [[FalseSharing]] / [[MESI]] / [[CacheLine]] / [[SnoopingProtocol]] vocabulary from the [[ParallelProcessorsAlgorithms|ParProc]] corpus.
