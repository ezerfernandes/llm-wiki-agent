---
title: "__syncthreads (CUDA Thread Barrier)"
type: concept
tags: [gpu, cuda, synchronization, barrier]
sources: [parproc-ch05-cuda-gpu-programming]
last_updated: 2026-05-17
---

# __syncthreads (CUDA Thread Barrier)

The [[CUDA]] device-side **intra-[[Block|block]] barrier**. A call to `__syncthreads()` blocks every thread in the calling block until **all** of that block's threads have reached the same point ([[parproc-ch05-cuda-gpu-programming]] §5.3, §5.5).

> *"There is also a thread barrier available for the threads themselves, at the block level. The call is `__syncthreads();`. This can only be invoked by threads within a block, not across blocks. In other words, this is barrier synchronization within blocks."*

## The intra-block-only rule

`__syncthreads()` operates **only within a single block**. It has no effect on threads in other blocks; threads across blocks cannot synchronize this way. The reason is structural: blocks may be assigned to different [[StreamingMultiprocessor|SMs]], and SMs have no barrier coupling between them ([[parproc-ch05-cuda-gpu-programming]] §5.4.1).

For inter-block synchronization, see [[AtomicOperation|atomic operations]] or [[CudaThreadSynchronize|`cudaThreadSynchronize()`]] (host roundtrip).

## When to call it

The standard pattern is **between a write phase and a read phase** in [[SharedMemory|shared memory]]:

```c
__shared__ int s[256];
int me = threadIdx.x;
s[me] = compute(me);           // each thread writes its slot
__syncthreads();               // make writes visible to other threads
int val = s[(me + 1) % 256];   // safe to read sibling slot now
```

Without `__syncthreads`, [[parproc-ch05-cuda-gpu-programming]] §5.4.3.1 warns that shared-memory consistency is *"relaxed among threads in a block: A write by one thread is not guaranteed to be visible to the others in a block until `__syncthreads()` is called."*

## When you can skip it

*"If each thread writes only to portions of shared memory that are not read by other threads in the block, then `__syncthreads()` need not be called."* (§5.4.3.1).

Writes are immediately visible to the **writing thread** without a barrier — only cross-thread visibility requires it.

## Relation to OpenMP's `#pragma omp barrier`

| Property | `__syncthreads()` (CUDA) | [[Barrier|`#pragma omp barrier`]] (OpenMP) |
|---|---|---|
| Scope | Single block | Whole team |
| Cost | Cheap (warp-scheduler primitive) | Synchronization overhead, see Ch4 §4.10 |
| Inter-team / inter-block | **Not supported** | Not supported (one team per `parallel`) |
| Implicit barriers? | Between kernels | After `single`/`for`/`sections`/`parallel` |

## See also

- [[Block]] — the scope unit.
- [[SharedMemory]] — the memory the barrier orders.
- [[AtomicOperation]] — alternative for inter-block needs.
- [[CudaThreadSynchronize]] — host-side counterpart.
- [[Barrier]] — the parent concept across paradigms.
- [[CUDA]] — substrate.
- [[parproc-ch05-cuda-gpu-programming]] — §5.3 / §5.4.3.1 / §5.5.
