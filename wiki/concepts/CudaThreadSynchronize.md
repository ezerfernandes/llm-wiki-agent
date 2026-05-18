---
title: "cudaThreadSynchronize"
type: concept
tags: [gpu, cuda, synchronization, host-side]
sources: [parproc-ch05-cuda-gpu-programming]
last_updated: 2026-05-17
---

# cudaThreadSynchronize

A host-side [[CUDA]] runtime call that **blocks the CPU thread until all previously-launched device work is complete** ([[parproc-ch05-cuda-gpu-programming]] §5.3).

## Why it's needed

Kernel launches **do not block**:

```c
kernel<<<grid, block>>>(args);          // returns immediately
// host code here runs concurrently with kernel
cudaMemcpy(hOut, dOut, sz, cudaMemcpyDeviceToHost);   // would race with kernel
```

Without an explicit wait, the host's `cudaMemcpy` could see stale device data. `cudaThreadSynchronize()` is the explicit barrier:

```c
kernel<<<grid, block>>>(args);
cudaThreadSynchronize();                // wait for kernel
cudaMemcpy(hOut, dOut, sz, cudaMemcpyDeviceToHost);
```

## Implicit synchronization alternatives

CUDA also synchronizes implicitly in several cases:

- **`cudaMemcpy()` blocks** until prior kernel work is done — the most common case.
- **Two consecutive kernel calls** with a dependency between them have an implicit barrier — *"there would be an implied barrier between the two calls; the second would not start execution before the first finished."* (§5.3, p. 123).
- **Output of one kernel is input to another** — implicit ordering enforced by the runtime.

## Use as an inter-block barrier

Because [[Block|blocks]] cannot barrier-sync with each other inside a kernel, the standard idiom for iterative algorithms is to **end the kernel between iterations**:

```c
for (int it = 0; it < niter; it++) {
    iterationStep<<<grid, block>>>(...);
    cudaThreadSynchronize();         // implicit inter-block barrier
}
```

This trades kernel-launch overhead for synchronization correctness. *"Implementing a barrier [from atomics] would not be much faster than attaining interblock synchronization by returning to the host and calling `cudaThreadSynchronize()` there."* ([[parproc-ch05-cuda-gpu-programming]] §5.5).

## Naming note

Modern CUDA renamed this `cudaDeviceSynchronize`. Matloff's chapter (Tesla-era) uses the older `cudaThreadSynchronize` name; the semantics are unchanged.

## See also

- [[KernelLaunch]] — the async call this waits on.
- [[ThreadBarrier]] — the in-kernel intra-block barrier (`__syncthreads`).
- [[AtomicOperation]] — alternative for non-barrier inter-block coordination.
- [[CUDA]] — substrate.
- [[parproc-ch05-cuda-gpu-programming]] — §5.3 / §5.5.
