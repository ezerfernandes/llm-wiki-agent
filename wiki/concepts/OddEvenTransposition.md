---
title: "OddEvenTransposition"
type: concept
tags: [algorithm, sorting, parallel-computing, cuda, openmp]
sources: [parproc-ch12-parallel-sorting]
last_updated: 2026-05-17
---

# OddEvenTransposition

A parallel variant of [[BubbleSort]] that alternates between two coupling phases, enabling regular and deadlock-free parallelization. Each thread is assigned one element of the array.

## Algorithm

```c
// "me" is this thread's ID
void oddevensort(int *x, int n, int me) {
    for (i = 1 to n) {
        if (i is odd) {
            if (me is even)  compare-exchange(x, me, me+1, n)
            else             compare-exchange(x, me, me-1, n)
        } else {  // i is even
            if (me is even)  compare-exchange(x, me, me-1, n)
            else             compare-exchange(x, me, me+1, n)
        }
    }
}
```

If the argument to `compare-exchange` is < 0 or ≥ n-1, the function has no action. From the perspective of an even-numbered element: it trades with its right neighbor during odd phases and its left neighbor during even phases.

## CUDA Implementation

The CUDA kernel (`oekern`) maps array positions to blocks and handles one iteration per launch:

```c
__global__ void oekern(int *da, int *daaux, int n, int iter) {
    int bix = blockIdx.x;
    if (iter % 2) {
        if (bix % 2) cas(da, daaux, bix-1, bix, n, bix);
        else         cas(da, daaux, bix, bix+1, n, bix);
    } else {
        if (bix % 2) cas(da, daaux, bix, bix+1, n, bix);
        else         cas(da, daaux, bix-1, bix, n, bix);
    }
}
```

The host function `oddeven()` loops for n iterations, calling the kernel once per iteration. A scratch array `daaux` prevents write hazards; array pointers `da` and `daaux` are swapped between iterations (except on the last, where `daaux` is copied back to host).

**Key constraint:** CUDA blocks cannot synchronize with each other across a single kernel launch. Therefore each launch handles exactly one iteration, with host-side control alternating between odd and even phases. Shared memory is not exploited in this baseline implementation; a more optimized version would use `__syncthreads()` within each block for intra-block compare-exchanges and handle boundary operations on the host.

## Connections

- [[BubbleSort]] — the sequential algorithm this extends.
- [[CompareExchange]] — the primitive operation in each phase.
- [[CUDA]] — the GPU implementation uses one kernel launch per iteration.
- [[OpenMP]] — the shared-memory pseudocode uses one thread per element.
- [[parproc-ch12-parallel-sorting]] — §12.3.2–12.3.3 source.
