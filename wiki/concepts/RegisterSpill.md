---
title: "Register Spill"
type: concept
tags: [compilers, performance, gpu, cuda]
sources: [parproc-ch05-cuda-gpu-programming]
last_updated: 2026-05-17
---

# Register Spill

When a function's live variables exceed the available registers, the compiler **spills** the excess to memory. On a CPU the spill destination is the stack frame; on a [[NVIDIA]] GPU under [[CUDA]] the spill destination is **local memory** — *which is physically part of [[GlobalMemory|global memory]]* ([[parproc-ch05-cuda-gpu-programming]] §5.4.3.5):

> *"Local memory is physically part of global memory, but is an area within that memory that is allocated by the compiler for a given thread. As such, it is slow, and accessible only by that thread. The compiler allocates this memory for local variables in a device function if the compiler cannot store them in registers. This is called register spill."*

## Why register spill is especially bad on GPUs

- **Local memory ≡ global memory.** Spilled variables incur hundreds-of-cycle latency per access, not the single-cycle register latency.
- **No L1 cache on Tesla.** Pre-Fermi, the spilled values are not cached — every access pays full global-memory cost. Post-Fermi (see [[TrueCaching]]), L1 may help.
- **Per-thread cost multiplies.** Each thread's spill region adds up across thousands of in-flight threads, consuming bandwidth that could be used for actual data.

## Causes

- **Arrays with variable indices.** *"An array won't be placed in registers if the array is too large, or if the array has variable index values, such as `int z[20], i; ... y = z[i];` — since registers are not indexable by the hardware, the compiler cannot allocate `z` to registers in this case."* Constant indices (`z[8]`) allow register allocation.
- **Too many simultaneous live variables.** Even with all-constant indices, the live set may exceed the SM's per-thread register budget.

## Mitigations

- **Constant-index everything possible.** Hand-unroll loops over small arrays so indices become compile-time constants ([[LoopUnrolling]]).
- **`#pragma unroll`** — converts loop array accesses into constant-index accesses.
- **Reduce live-variable count.** Restructure the kernel to compute and immediately consume intermediate values rather than holding them.
- **Increase block-level register budget.** Fewer blocks per SM → more registers per thread, but worse [[LatencyHiding|latency hiding]] — tradeoff.

## See also

- [[GlobalMemory]] — where spills land.
- [[LoopUnrolling]] — primary mitigation.
- [[CUDA]] — context.
- [[parproc-ch05-cuda-gpu-programming]] — §5.4.3.5 / §5.15.
