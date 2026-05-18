---
title: "Cache Memory"
type: concept
tags: [hardware, systems, performance, memory, parallel-computing]
sources: [parproc-appA-systems-issues]
last_updated: 2026-05-17
---

# Cache Memory

**Cache memory** is a small, fast section of the CPU chip that holds copies of recently accessed main memory (RAM) content. Because RAM is off-chip — signals travel through thicker wires over greater distances — it is slow relative to the CPU's clock speed. The cache bridges this gap by keeping frequently needed data on-chip.

## Mechanics

The cache is organized in fixed-size units called **blocks** (also called *cache lines*, typically 64 bytes on modern x86). When the CPU requests a memory word:

- **Cache hit**: the block containing the word is already in cache. Access is fast.
- **Cache miss**: the block is not in cache. The CPU fetches the entire block from RAM and places it in cache. If the cache is full, a resident block must be **evicted** first to make room. Under a **write-back** policy, a dirty (modified) evicted block is written back to RAM before eviction.

## Hit rates and locality

Cache sizes are small relative to total RAM, so one might expect frequent misses. In practice, hit rates are typically above 90% due to [[LocalityOfReference]]:

- **Temporal locality**: programs tend to re-access the same memory item repeatedly within short time windows. The first access misses; subsequent accesses hit.
- **Spatial locality**: programs tend to access items near each other in memory in quick succession. Fetching a block on a miss pre-loads the neighbors, which are likely to be accessed soon.

The **block replacement policy** (deciding which block to evict on a miss) further improves hit rates; LRU (Least Recently Used) is a common choice.

## Multiple cache levels

Modern processors have multiple cache levels (L1, L2, L3), each larger and slower than the one above it. L1 is the fastest and smallest (32–64 KB per core); L3 may be several MB and is often shared across cores. See [[MemoryHierarchy]] for latency numbers.

## Cache misses vs page faults

A cache miss is handled **entirely in hardware** — the CPU stalls briefly while the block is fetched, and no software is involved. This makes it invisible to the program and incountable in software. A [[VirtualMemory|page fault]], by contrast, triggers an OS interrupt and a disk access, making it orders of magnitude more expensive.

## Parallel programming implications

- **[[FalseSharing]]**: two threads writing to different variables that happen to share a cache line cause the line to bounce between cores, degrading performance. Pad data structures to cache-line boundaries to avoid this.
- **[[RowMajorOrder]]**: in C/C++, accessing 2D array elements in row-major order (rightmost index varying in the inner loop) ensures sequential cache-line traversal. Column-major access strides across cache lines and can reduce the hit rate dramatically.
- **Coherence**: in multicore systems, each core has its own cache. [[CoherentCaches|Cache coherence protocols]] (e.g., MESI) keep copies consistent when multiple cores write to the same address, but at a performance cost.

## Connections

- [[parproc-appA-systems-issues]] — §A.2.1; primary source.
- [[MemoryHierarchy]] — the broader layered structure of which cache is the fastest tier.
- [[LocalityOfReference]] — the access-pattern property that makes caches effective.
- [[VirtualMemory]] — the OS mechanism extending the hierarchy to disk; page faults are the disk-tier analogue of cache misses.
- [[TranslationLookasideBuffer]] — a special cache for page-table entries.
- [[CoherentCaches]] — multicore cache-coherence protocols.
- [[RowMajorOrder]] — C/C++ array layout optimized for cache spatial locality.
- [[gpumemoryhierarchy]] — GPU on-chip shared memory is an explicitly programmer-managed cache analogue.
