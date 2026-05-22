---
title: "Atomic Operation"
type: concept
tags: [gpu, cuda, synchronization, concurrency, threads]
sources: [parproc-ch05-cuda-gpu-programming, dis-14-3-synchronization]
last_updated: 2026-05-18
---

# Atomic Operation

**An action that executes without interruption from the thread's perspective — "all or nothing" behavior** ([[dis-14-3-synchronization|DIS Ch 14.3]]). The property a [[CriticalSection|critical section]] must collectively achieve; the property a single hardware atomic instruction (compare-and-swap, fetch-and-add, load-link/store-conditional) gives natively. Page combines the **general / CPU-side** treatment from [[dis-14-3-synchronization|DIS Ch 14.3]] with the **CUDA-side** treatment from [[parproc-ch05-cuda-gpu-programming|Parallel Processing Ch 5.5]].

## General / CPU-side (DIS Ch 14.3)

[[dis-14-3-synchronization|DIS Ch 14.3]]'s headline rule: *"all operations should be assumed to be nonatomic unless mutual exclusion is explicitly enforced."* Even `int i = 0; i++;` is **three** machine instructions on most architectures (load → increment → store) and any one of them can be interrupted by a [[ContextSwitch|context switch]] or [[Interrupt|interrupt]]. The point of [[Synchronization|synchronization]] primitives is to lift a *sequence* of non-atomic machine instructions to *collective* atomicity — the [[Mutex|mutex]] lock/unlock pair around `COUNTER += 1` makes the [[ReadModifyWrite|read-modify-write]] **as if** it were a single uninterruptible instruction.

### Hardware-native atomicity

Modern CPUs provide hardware-atomic primitives that don't require locking:

- **x86-64**: `LOCK` prefix on `XADD` / `CMPXCHG` / `XCHG` instructions.
- **ARM**: load-link / store-conditional (`LDREX` / `STREX`) — read with reservation, write only if no intervening write.
- **RISC-V**: A-extension atomic instructions.

These map onto [[Atomic|`AtomicUsize::fetch_add`]] / `compare_exchange` in Rust / C11 `<stdatomic.h>` / C++11 `<atomic>`. They are the lock-free alternative to [[Mutex|mutexes]] for **single-word** state.

### Atomicity vs ordering

Atomicity (no partial state) is **necessary but not sufficient** for correctness. [[MemoryOrdering|Memory ordering]] (when other threads observe the write) is the orthogonal axis — `Ordering::Relaxed` gives atomicity without ordering, `Ordering::SeqCst` gives both. Out of scope for [[dis-14-3-synchronization|DIS Ch 14.3]] but central to [[Atomic|`std::sync::atomic`]].

## CUDA-side (Parallel Processing Ch 5.5)

In [[CUDA]], an **atomic operation** is a read-modify-write action on [[GlobalMemory|global]] or [[SharedMemory|shared]] memory that *"a thread can execute without pre-emption, i.e. without interruption"* ([[parproc-ch05-cuda-gpu-programming]] §5.5). Atomics are the primary mechanism for **inter-block** coordination — since `__syncthreads()` only works within a [[Block]] and SMs cannot barrier-sync with each other ([[parproc-ch05-cuda-gpu-programming]] §5.4.1).

## Available primitives

| Operation | Action | Use |
|---|---|---|
| [[AtomicAdd|`atomicAdd(addr, inc)`]] | Fetch-and-add | Reductions across blocks |
| `atomicExch(addr, val)` | Exchange | Lock release |
| `atomicCAS(addr, cmp, val)` | Compare-and-swap | Lock acquire, lock-free structures |
| `atomicMin` / `atomicMax` | Min / max update | Reductions |
| `atomicAnd` / `atomicOr` | Bitwise | Flag aggregation |

The return value of every atomic is the **previous value** at that address.

## Implementing a lock

```c
__device__ void lock(int *lockVar) {
    while (atomicCAS(lockVar, 0, 1) != 0) { ; }
}

__device__ void unlock(int *lockVar) {
    atomicExch(lockVar, 0);
}
```

(Compile with `nvcc -arch=sm_11` or higher to enable the atomics.)

## Why a barrier built from atomics is expensive

*"Though a barrier could in principle be constructed from the atomic operations, its overhead would be quite high. In earlier models that was near a microsecond, and though that problem has been ameliorated in more recent models, implementing a barrier in this manner would not be much faster than attaining interblock synchronization by returning to the host and calling `cudaThreadSynchronize()` there."* ([[parproc-ch05-cuda-gpu-programming]] §5.5).

So for **real inter-block synchronization** (iterative algorithms where all threads must wait at the end of each iteration), the standard pattern is to **end the kernel** between iterations:

```c
for (int it = 0; it < niter; it++) {
    kernel<<<grid, block>>>(...);
    cudaThreadSynchronize();   // implicit barrier
}
```

## Connections

- [[dis-14-3-synchronization]] — DIS Ch 14.3; the general CPU-side framing.
- [[parproc-ch05-cuda-gpu-programming]] — Parallel Processing Ch 5.5; the CUDA-side framing.
- [[CriticalSection]] — the code-region whose collective execution must be atomic.
- [[Synchronization]] — the family of primitives that achieves atomicity.
- [[Atomic]] — the Rust embedded family of hardware-atomic types.
- [[DataRace]] / [[RaceCondition]] — the failure modes non-atomicity allows.
- [[ReadModifyWrite]] — the canonical non-atomic instruction sequence.
- [[Mutex]] — the lock-based alternative for multi-word state.
- [[ContextSwitch]] — the timing event that breaks naive atomicity assumptions on a single core.
- [[Interrupt]] — the embedded-systems analog.
- [[AtomicAdd]] — the most common CUDA atomic.
- [[CudaThreadSynchronize]] — the host-side barrier alternative on GPU.
- [[ThreadBarrier]] — the intra-block alternative (`__syncthreads`).
- [[Block]] — atomics' raison d'être in CUDA (only mechanism across blocks).
- [[CUDA]] — substrate.
