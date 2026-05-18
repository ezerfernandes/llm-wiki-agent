---
title: "Memory Coalescing (CUDA)"
type: concept
tags: [gpu, cuda, performance, memory, bandwidth]
sources: [parproc-ch05-cuda-gpu-programming]
last_updated: 2026-05-17
---

# Memory Coalescing (CUDA)

A [[CUDA]] hardware optimization that **merges multiple [[GlobalMemory|global-memory]] accesses from a half-[[Warp|warp]] into one transaction** when the accessed words are consecutive ([[parproc-ch05-cuda-gpu-programming]] §5.4.3.2).

> *"If the hardware sees that the threads in this half-warp (or at least the ones currently accessing global memory) are accessing consecutive words, the hardware can execute the memory requests in groups of up to 32 words at a time. This works because the memory is low-order interleaved."*

## Why it matters

Global memory takes **hundreds of clock cycles per access**. Without coalescing, 16 threads in a half-warp each issue independent loads → 16 separate transactions, fully serialized at the memory controller. With coalescing, a 16-word block load fetches the same data in one transaction — roughly **16× bandwidth improvement** in the ideal case.

## Tesla rules (relaxed in newer hardware)

- Operates at **half-warp granularity** (16 threads).
- Words must be **consecutive in memory** (and aligned to a 32/64/128-byte boundary, depending on word size).
- Reads and writes both coalesce.
- *"The newer GPUs go even further, coalescing much more general access patterns, not just to consecutive words."*

## Programmer techniques

- **Layout arrays so thread `i` reads element `i`.** The canonical idiom: `int me = blockIdx.x * blockDim.x + threadIdx.x; x = a[me];` — adjacent threads hit adjacent words.
- **Transpose row-major data for column scans.** Matloff's §5.8 row-sums-vs-column-sums experiment: row sums (each thread scans a full row, threads access non-adjacent words at the same step) misses coalescing; column sums on the same row-major matrix (each thread scans a column, half-warp threads access adjacent matrix elements at each step) coalesces — observable in the small but consistent timing gap between `rs 20000` (4.54 s) and `cs 20000` (4.40 s).
- **Pad arrays.** The Ch3 §3.2.2 [[BankConflict|stride/padding]] technique applies to global accesses too; insert padding so half-warp access strides hit consecutive words.

## Shared-memory analog: banks

Shared memory has an analogous structure ([[parproc-ch05-cuda-gpu-programming]] §5.4.3.3): 8 (Tesla) or 32 (newer) low-order-interleaved banks. The "consecutive words coalesce" rule maps to "half-warp threads should hit **different banks**" — same hardware idea, different name.

## See also

- [[GlobalMemory]] — what coalescing speeds up.
- [[SharedMemory]] — the bank-conflict sibling problem.
- [[Warp]] — the half-warp is the coalescing unit.
- [[MemoryInterleaving]] — the underlying low-order interleaving the hardware exploits.
- [[BankConflict]] — the dual problem on shared memory.
- [[parproc-ch05-cuda-gpu-programming]] — §5.4.3.2 / §5.8.
