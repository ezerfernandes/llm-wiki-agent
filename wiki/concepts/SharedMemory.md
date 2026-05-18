---
title: "Shared Memory (CUDA)"
type: concept
tags: [gpu, cuda, memory, programmer-managed-cache]
sources: [parproc-ch05-cuda-gpu-programming]
last_updated: 2026-05-17
---

# Shared Memory (CUDA)

The on-chip, small, fast, **block-scoped** tier of the [[GPUMemoryHierarchy|GPU memory hierarchy]] in [[CUDA]]. Shared memory is *"used essentially as a programmer-managed cache"* ([[parproc-ch05-cuda-gpu-programming]] §5.4.3.1) — the programmer explicitly copies data from [[GlobalMemory|global memory]] into shared memory, performs reuse-heavy computation there, then writes results back.

## Properties (Tesla baseline)

| Property | Value |
|---|---|
| Scope | Global to [[Block|block]] |
| Size | **16K bytes per [[StreamingMultiprocessor|SM]]** (divvied across blocks) |
| Location | On-chip |
| Speed | "Blinding" — comparable to register access |
| Lifetime | Kernel |
| Host access | No |
| Cached (Tesla) | N/A — *is* the on-chip storage |
| Banks | 8 (Tesla) / 32 (newer); low-order interleaved |

If 4 blocks run on one SM, each gets only **16K / 4 = 4K** of shared memory.

## Declaration patterns

**Static** — inside the kernel:

```c
__shared__ int abcsharedmem[100];
```

**Dynamic** — sized at launch via the kernel-launch third argument:

```c
extern __shared__ int sv[];                            // kernel side
kernel<<<dimGrid, dimBlock, vsize>>>(dv, n);           // host side
```

Only **one** dynamic `extern __shared__` region per kernel — multiple such declarations all alias the same buffer. Aliased sub-arrays are constructed by pointer arithmetic (`int *x = &sv[120]`).

## Consistency model

*"Shared memory consistency is sequential within a thread, but relaxed among threads in a block: A write by one thread is not guaranteed to be visible to the others in a block until `__syncthreads()` is called."* (§5.4.3.1).

Writes are immediately visible to the **writing thread itself**; only cross-thread visibility requires a barrier. Threads that only read their own per-thread sub-region need no barrier.

## Bank conflicts

Shared memory is split into 8 (Tesla) or 32 (newer) banks, with consecutive word addresses falling in consecutive banks mod the bank count. Performance rules ([[parproc-ch05-cuda-gpu-programming]] §5.4.3.3):

- **Half-warp threads should hit different banks.** Conflict-free.
- **Half-warp threads all hit the same word in the same bank.** Conflict-free **broadcast**.
- **Mixed pattern** (some same word, some different) → may or may not conflict, depends on hardware tie-breaking.

## Use-it-or-don't rule

*"Shared memory only helps if we are doing multiple accesses to the data. If for instance our code does a single read and a single write to an element of an array, then transferring it back and forth between global and shared memory isn't worthwhile."* ([[parproc-ch05-cuda-gpu-programming]] §5.12).

The Sieve of Eratosthenes (§5.10), matrix tiling (§11.3.2.2 forward reference), and cumulative-sum partial scan (§5.11) are canonical reuse-heavy patterns that justify the copy overhead.

## See also

- [[GlobalMemory]] — the slow off-chip backing store shared memory caches from.
- [[GPUMemoryHierarchy]] — the full hierarchy table.
- [[CUDA]] — the parent programming model.
- [[Block]] — the scope unit; one block sees one slice.
- [[MemoryCoalescing]] — the analog optimization for global memory.
- [[TrueCaching]] — newer GPUs split the on-chip storage between shared memory and an automatic L1.
- [[parproc-ch05-cuda-gpu-programming]] — §5.4.3.1 / §5.4.3.3 / §5.12.
