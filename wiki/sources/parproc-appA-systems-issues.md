---
title: "ParProcBook Appendix A: Miscellaneous Systems Issues"
type: source
tags: [textbook, parallel-computing, operating-systems, memory-hierarchy, cache]
date: 2026-05-17
source_file: raw/parproc-matloff.pdf
sources: []
last_updated: 2026-05-17
---

# ParProcBook Appendix A: Miscellaneous Systems Issues

Appendix A (book pp. 305–312, PDF pp. 325–332) of *Programming on Parallel Machines: GPU, Multicore, Clusters and More* by [[NormMatloff]] of [[UCDavis]]. The appendix is a self-contained systems primer covering three topics — timesharing, memory hierarchies, and array storage — that surface repeatedly throughout the main chapters.

## Summary

§A.1 explains [[Timesharing]]: the OS gives each process a short turn (a *quantum* or *timeslice*, typically 50–60 ms) on the CPU, enforced via a hardware timer interrupt that triggers a [[ContextSwitch]]. Processes that voluntarily yield (e.g., waiting for keyboard input via `scanf`) move to Sleep state; the OS wakes them on I/O completion. On multicore machines, several processes may run truly in parallel, but the OS-managed turn-taking mechanism is otherwise identical.

§A.2 covers [[MemoryHierarchy]]: §A.2.1 introduces [[CacheMemory]] — a small, fast on-chip copy of recently accessed RAM, organized in blocks; accesses either hit (fast) or miss (triggers a full-block fetch from RAM, evicting an existing block). §A.2.2 introduces [[VirtualMemory]]: the OS maps each program's virtual addresses to physical addresses via a *page table*, allowing programs to exceed physical RAM (pages not resident in RAM generate a *page fault*, which the OS services by loading the page from disk). §A.2.3 discusses performance: cache misses are expensive but rare in practice due to [[LocalityOfReference]] (temporal and spatial); page faults are catastrophic because disk access is mechanical. A [[TranslationLookasideBuffer]] (TLB) caches page-table entries to avoid the double-memory-access overhead of virtual-to-physical translation.

§A.3 covers array issues in C/C++: §A.3.1 explains [[RowMajorOrder]] storage — 2D arrays are stored as contiguous 1D blocks, row by row, so element `z[i][j]` of a `c`-column array lies at flat index `i*c + j`; §A.3.2 shows how row-major layout enables subarray access by pointer arithmetic; §A.3.3 revisits [[MemoryAllocation]] — dynamic allocation via `malloc()`/`new` is expensive and in large parallel programs should be avoided where possible in favor of static or stack allocation; when size is known at compile time but the array is local, declare it global; on 64-bit `gcc`, use `-mcmodel=medium` to accommodate large global arrays.

## Key Claims

- **Timesharing is implemented by hardware timer interrupts.** The OS cannot stop a running process directly — it relies on a periodic timer interrupt (e.g., every 10 ms on x86 with the 8253 timer at 100 Hz, every 6th interrupt triggering a context switch, yielding 60 ms quanta) to transfer control to the OS, which then performs the context switch. (§A.1.1, p. 305–306)

- **Context switching saves and restores register state.** A context switch saves all registers of the outgoing process (including PC and EFLAGS) and restores those of the incoming process. The CPU resumes the new process from exactly where it was suspended. (§A.1.1, p. 306)

- **Cache misses bring in an entire block, and may require evicting another block.** On a miss, the CPU fetches the whole block containing the missing item; a currently resident block is evicted to make room. Write-back policy means a dirty evicted block is also written to RAM. (§A.2.1, p. 307)

- **Virtual memory has three goals: overcome memory-size limits, relieve the compiler of real-address management, and enforce security.** The page table — an OS-maintained array mapping virtual page numbers to physical page numbers — is set up at program load time and consulted by CPU hardware on every memory access. (§A.2.2.1–A.2.2.2, pp. 307–308)

- **A page fault is catastrophically expensive.** Unlike a cache miss (handled entirely in hardware, invisible to software), a page fault raises an interrupt, the OS handles it by loading a page from disk, then restarts the instruction. Disk is mechanical; the performance impact far exceeds a cache miss. (§A.2.3, p. 309)

- **Locality of reference keeps cache hit rates above 90%.** Most programs exhibit temporal locality (re-accessing the same item within a short window) and spatial locality (accessing nearby items within the same block in quick succession). The block replacement policy further improves hit rates. (§A.2.3, p. 309)

- **The TLB avoids double memory access for page-table lookup.** Without it, every memory access would require two RAM accesses: one to read the page table entry, one to read the actual data. The TLB is a special cache for page table entries. (§A.2.3, p. 309)

- **C/C++ 2D arrays are row-major; element (i,j) of a c-column array is at flat index i*c+j.** This fact is *"used a lot in this book, and in general in code written in the parallel processing community."* (§A.3.1, p. 310)

- **Dynamic memory allocation is expensive in parallel programs.** `malloc()`/`new` should be avoided in performance-critical parallel code. Prefer static global arrays; use `-mcmodel=medium` for large arrays on 64-bit `gcc`. (§A.3.3, pp. 310–311)

## Key Quotes

> *"Timesharing involves having several programs running in what appears to be a simultaneous manner."* — p. 305. Definition of timesharing.

> *"The OS is dead while u is running."* — p. 306. Why quanta are enforced by a hardware timer, not by the OS directly.

> *"This term refers to the fact that most programs tend to either access the same memory item repeatedly within short time periods (temporal locality), and/or access items within the same block often during short periods (spatial locality). Hit rates are typically well above 90%."* — p. 309. Locality of reference explaining cache effectiveness.

> *"A page fault is pretty catastrophic in performance terms. Remember, the disk speed is on a mechanical scale, not an electronic one."* — p. 309. Page fault cost.

> *"You'll see this fact used a lot in this book, and in general in code written in the parallel processing community."* — p. 310. On row-major storage and the i*c+j formula.

> *"In large parallel programs, this approach may be quite slow."* — p. 310. On `malloc()`/`new` in parallel code.

## Connections

- [[NormMatloff]] — author.
- [[UCDavis]] — author's institution.
- [[Timesharing]] — §A.1; new concept page; OS mechanism giving each process a time quantum on the CPU.
- [[ContextSwitch]] — §A.1.1; the OS operation of saving/restoring process register state during a quantum boundary.
- [[MemoryHierarchy]] — §A.2; new concept page; the layered RAM/cache/disk structure and its performance implications.
- [[CacheMemory]] — §A.2.1; new concept page; on-chip fast memory storing blocks of RAM; hit/miss/eviction mechanics.
- [[VirtualMemory]] — §A.2.2; new concept page; OS/hardware page-table mechanism mapping virtual to physical addresses.
- [[LocalityOfReference]] — §A.2.3; new concept page; temporal and spatial access patterns explaining >90% cache hit rates.
- [[TranslationLookasideBuffer]] — §A.2.3; special cache for page-table entries, avoiding double memory access per VM lookup.
- [[RowMajorOrder]] — §A.3.1; existing page; C/C++ 2D array storage row by row; i*c+j formula central to parallel code.
- [[MemoryAllocation]] — §A.3.3; existing page; `malloc()`/`new` expensive in parallel programs; prefer static/global arrays.
- [[CoherentCaches]] — §A.2.1; cache coherence concerns arise in multicore settings where multiple caches must stay consistent.
- [[gpumemoryhierarchy]] — §A.2; GPU memory hierarchies (shared memory, global memory, L1/L2) are specialized instances of the general hierarchy described here.
- [[parproc-ch02-recurring-performance-issues]] — Ch2 §2.7 flags memory allocation as a recurring parallel performance issue, cross-referenced by §A.3.3.

## Contradictions

- **No contradiction with [[RowMajorOrder]].** The existing page (sourced from [[dis-2-5-arrays]]) covers the same row-major indexing formula and cache-locality implications. Appendix A adds the parallel-programming-community usage note and the `-mcmodel=medium` tip for large arrays on 64-bit `gcc`.
- **No contradiction with [[MemoryAllocation]].** Ch2 §2.7 and §A.3.3 give consistent advice — dynamic allocation is expensive, prefer static/global arrays — with §A.3.3 adding the `gcc` flag for large global arrays.
- **Cache miss vs page fault severity.** §A.2.3 draws a sharp qualitative distinction: cache misses are hardware-handled and recoverable at low cost; page faults require OS intervention and disk I/O. This is consistent with [[gpumemoryhierarchy]] and [[CoherentCaches]] which treat cache misses as the primary concern at the GPU/multicore level.
