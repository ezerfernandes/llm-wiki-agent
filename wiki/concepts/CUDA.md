---
title: "CUDA"
type: concept
tags: [gpu, infrastructure, nvidia]
sources: [d2l-installation, d2l-builders-guide, d2l-computational-performance, d2l-appendix-tools, parproc-ch05-cuda-gpu-programming]
last_updated: 2026-05-17
---

# CUDA

[[NVIDIA|NVIDIA's]] parallel-computing platform and API exposing GPU compute to applications. The execution substrate beneath [[PyTorch]], [[TensorFlow]], [[JAX]], [[flashattention]], and most [[DistributedTraining]] runtimes; understanding its memory hierarchy (see [[gpumemoryhierarchy]]) is critical for [[kernelfusion]] and performance work.

For practical install workflows ([[d2l-installation]]) the CUDA toolkit version (queried via `nvcc --version` or `cat /usr/local/cuda/version.txt`) determines which framework wheel to `pip install` — e.g. `mxnet-cu112` for CUDA 11.2, `jax[cuda11_pip]` for JAX, etc.

## Device handles in PyTorch

[[d2l-builders-guide]] §`use-gpu.md` documents the user-facing API: `torch.device('cuda')` (or `torch.device(f'cuda:{i}')` for the $i$-th card), `torch.cuda.device_count()`, and the `tensor.cuda(i)` / `module.to(device='cuda:i')` migration calls. The CUDA runtime is what underlies every one of those. Same-device-operand rule (see [[GPU]]) is enforced by CUDA's memory model — kernels cannot dereference pointers from other devices.

## CUDA at the kernel level

[[parproc-ch05-cuda-gpu-programming]] is the wiki's most detailed treatment of CUDA below the PyTorch layer. Key elements:

### Programming model

- **Host/device split.** `main()` runs on the CPU (host); kernels run on the GPU (device). Kernels are declared with `__global__ void`; device-only helpers with `__device__`. No host C library, no function pointers, no call stack on the device side.
- **Grid/Block/Thread/Warp hierarchy.** A [[Grid]] (the totality of threads for one launch) contains [[Block|blocks]] (the assignment unit, each bound to one [[StreamingMultiprocessor|SM]]); each block is divided into [[Warp|warps]] of 32 threads that execute in [[SIMT]] lockstep.
- **[[KernelLaunch|Kernel launch syntax]]**: `kernel<<<dimGrid, dimBlock, sharedBytes>>>(args)` — angle-bracket triple is CUDA's only major syntactic extension to C.
- **Asynchronous launch.** Kernel calls return immediately; `cudaThreadSynchronize()` is the explicit host barrier, `cudaMemcpy()` blocks implicitly.

### Memory tiers

| Tier | Scope | Location | Lifetime | Speed |
|---|---|---|---|---|
| Registers | Per-thread | On-chip | Kernel | Fast |
| [[SharedMemory|Shared]] | Per-block | On-chip | Kernel | Fast |
| [[GlobalMemory|Global]] | Per-app | Off-chip | App | Slow (cached on Fermi+) |
| [[ConstantMemory|Constant]] | Per-app (RO from device) | Off-chip, cached | App | Fast on hit |
| [[TextureMemory|Texture]] | Per-app (RO, 2D-cached) | Off-chip, cached | App | Fast on hit |
| Local | Per-thread | Off-chip (= global) | Kernel | Slow ([[RegisterSpill|register spill]]) |
| [[UnifiedMemory|Managed]] (Pascal+) | Host + device | Migrated | App | Convenience |

Shared memory is the central performance lever: *"shared memory is used essentially as a programmer-managed cache"* — explicit staging from global → shared → compute → global.

### Synchronization

- **Intra-block**: `__syncthreads()` (also called [[ThreadBarrier]]).
- **Inter-block**: no native barrier. Options are `atomicAdd` / `atomicCAS` / `atomicExch` etc. (cheap one-shot ops) or return to host between kernels (`cudaThreadSynchronize()` + relaunch).

### Performance levers

- **[[MemoryCoalescing|Coalescing]]** — half-warp threads accessing consecutive words coalesce into one transaction.
- **[[LatencyHiding|Latency hiding]]** — the SM's "[[OSInHardware|OS in hardware]]" swaps to another warp on memory stall.
- **[[ThreadDivergence|Avoid thread divergence within a warp]]** — same-warp branches serialize.
- **[[LoopUnrolling|Loop unrolling]]** (`#pragma unroll k`) for register allocation.
- **[[ShortVectors|Short vectors]]** (`int4`, `char2`) for 4× memory bandwidth.

### Higher-level libraries

[[CUBLAS]] (linear algebra, column-major), [[CUFFT]] (FFT), [[Thrust]] (STL-style algorithms, also OpenMP backend).

### Compilation

`nvcc -g -G x.cu` — `.cu` file extension; `-g` debug host, `-G` debug device. Modern device debugger is `cuda-gdb` (Unix: X11 must be off).
