---
title: "Memory Hierarchy"
type: concept
tags: [hardware, systems, performance, parallel-computing]
sources: [d2l-computational-performance, parproc-appA-systems-issues, dis-11-1-memory-hierarchy, mlsysbook-ch11-hardware-acceleration]
last_updated: 2026-06-05
---

# Memory Hierarchy

The pyramid of memory tiers — registers / L1 / L2 / L3 / DRAM / SSD / HDD / network — each progressively larger, slower, and cheaper. The fundamental shape of every modern computer; the cost model under [[gpumemoryhierarchy]], [[FlashAttention]], and essentially all systems-aware deep-learning optimization ([[d2l-computational-performance]] §`hardware`).

## The defining trade-off (from [[dis-11-1-memory-hierarchy|DIS Ch 11.1]])

[[DiveIntoSystems|DIS]] Ch 11.1 frames the entire structure as the consequence of a single hardware-physics constraint:

> *"devices with higher capacities offer lower performance... no single device does both. This trade-off between performance and capacity is known as the memory hierarchy."* — [[dis-11-1-memory-hierarchy]]

The trade-off has a **cost dimension** as well: *"faster devices are more expensive, both in terms of bytes per dollar and operational costs (e.g., energy usage)"* — narrow top, wide base, with money and energy concentrated at the top. The engineering corollary follows directly: *"Practical systems must utilize a combination of devices to meet the performance and capacity requirements of programs."* No single-tier system is viable.

## The six-tier pyramid (DIS naming)

[[dis-11-1-memory-hierarchy|DIS Ch 11.1]] names the tiers from **highest performance / lowest capacity** to **lowest performance / highest capacity**:

| # | Tier | Notes |
|---|---|---|
| 1 | [[CpuRegister\|Registers]] | Top of pyramid; compiler-managed; tens per core. |
| 2 | [[CacheMemory\|Cache]] | Multi-level — [[CacheLevel\|L1 / L2 / L3]]. 11.1 treats as a single tier. |
| 3 | [[RAM\|Main Memory]] | [[DRAM]]; the *RAM* tier. |
| 4 | [[FlashMemory\|Flash Disk]] | SSD (solid-state); non-volatile, no moving parts. |
| 5 | Traditional Disk | Rotational HDD; mechanical seek. |
| 6 | Remote Secondary Storage | Network-attached / cloud / datacenter-scale. |

The cache tier itself decomposes into three levels per [[CacheLevel|CacheLevel]]: *"L1 (very small and fast, near the [[ALU]]), L2 (larger and slower), and L3 (shared among multicore CPUs)."*

## Programmer commitment (DIS)

[[dis-11-1-memory-hierarchy|DIS Ch 11.1]] commits to a deliberate stance on locality-aware coding: *"Ideally, programmers wouldn't need to worry about data location, though performance-critical code sections may justify such optimization."* The hierarchy is an *implementation detail* most of the time; it becomes a *programmer concern* only in performance-critical code. The remainder of [[DiveIntoSystems|DIS]] Ch 11 (sections 11.2 *Storage Devices*, 11.3 *Locality*, 11.4 *Caching*, 11.5 *Cache Analysis and Cachegrind*, 11.6 *Caching on Multicore Processors*) operationalizes the *"when it does matter"* half of this stance.

## CPU side — latency numbers every programmer should know

From [[d2l-computational-performance]]'s consolidated table (after Eshelman / Jeff Dean 2010 / Colin Scott):

| Tier | Latency | Notes |
|---|---|---|
| Register | ≤1 cycle | Compiler-managed; tens per core |
| L1 cache | 1.5 ns / 4 cycles | 32–64 KB per core; split inst / data |
| L2 cache | 5 ns / 12–17 cycles | 256–512 KB per core |
| L3 cache (local) | 16 ns / 42 cycles | 4–256 MB shared |
| L3 (remote socket) | 40 ns | Cross-socket QPI hop |
| Local DRAM | 46 ns | Burst read |
| Remote-socket DRAM | 70–120 ns | NUMA penalty |
| Intel Optane | 94 / 305 ns | Write / read |
| 4 KB over 100 Gbps HPC | 1 µs | InfiniBand-class |
| 4 KB over 10 GbE | 10 µs | Datacenter Ethernet |
| 1 MB to NVMe SSD | 30 µs (write) | DC P3608 |
| **1 MB to/from NVLink GPU** | **30 µs** | ~33 GB/s |
| **1 MB to/from PCIe GPU** | **80 µs** | ~12 GB/s |
| Round trip same DC | 500 µs | One-way ping ~250 µs |
| HDD seek | 10 ms | Rotational |
| CA → Netherlands → CA | 150 ms | Speed of light |

The two design lessons:

1. **Random access is expensive.** First DRAM read is ~500× more expensive than a subsequent burst-read (100 ns address setup vs 0.2 ns / 64 bits). Aligned, sequential, forward-direction access wins.
2. **Aim for small numbers of large transfers.** Whether RAM, SSD, network, or GPU — packet/kernel/setup overhead dominates small transfers. The mantra appears verbatim in [[d2l-computational-performance]]'s chapter summary.

## GPU memory tiers

D2L's GPU latency table:

| Tier | Latency | Notes |
|---|---|---|
| GPU shared memory (SRAM) | 30 ns | 30–90 cycles; bank conflicts add latency |
| GPU global memory ([[HBM]]) | 200 ns | 200–800 cycles |
| Kernel launch | 10 µs | Host instructs GPU |

See [[gpumemoryhierarchy]] for the full A100 reference. [[FlashAttention]] explicitly designs around SRAM ↔ HBM asymmetry.

## Parallel programming implications (from [[parproc-appA-systems-issues]])

[[NormMatloff]]'s Appendix A gives the systems-oriented programmer's view of the same hierarchy:

- **Cache misses** bring in an entire block; eviction may require a write-back to RAM. Cache miss rates are kept low by [[LocalityOfReference]] (typically >90% hit rate). The block replacement policy is a key lever.
- **Page faults** are catastrophically more expensive than cache misses — disk is mechanical. On Unix systems, the `time` command reports page fault counts; cache misses cannot be counted in software because they are handled entirely in hardware.
- **TLB**: a [[TranslationLookasideBuffer]] caches page-table entries so that virtual-to-physical translation does not require a separate RAM access on every memory operation.
- **Array layout**: C/C++ stores 2D arrays in [[RowMajorOrder]]; the inner loop should walk the rightmost index for cache-sequential access.
- **[[MemoryAllocation]]**: `malloc()`/`new` is expensive in parallel programs; prefer static or global arrays. On 64-bit `gcc`, use `-mcmodel=medium` for large global arrays.

## See also
- [[gpumemoryhierarchy]] — GPU-specific drill-down.
- [[HBM]] — the GPU DRAM tier.
- [[PCIe]] / [[NVLink]] / [[Ethernet]] — the inter-device tiers.
- [[FlashAttention]] — canonical memory-hierarchy-aware algorithm.
- [[CacheMemory]] — on-chip cache tier; hit/miss/eviction mechanics.
- [[VirtualMemory]] — OS/hardware page-table extension to disk.
- [[LocalityOfReference]] — access pattern property enabling >90% cache hit rates.
- [[TranslationLookasideBuffer]] — page-table entry cache avoiding double memory access.
- [[d2l-computational-performance]] §`hardware`.
- [[parproc-appA-systems-issues]] — §A.2; systems primer for parallel programmers.
