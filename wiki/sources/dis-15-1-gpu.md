---
title: "Dive into Systems — Ch 15.1 Hardware Acceleration and CUDA"
type: source
tags: [dive-into-systems, textbook, parallel-programming, gpu, cuda, heterogeneous-computing]
date: 2026-05-18
source_file: https://diveintosystems.org/book/C15-Parallel/gpu.html
---

## Summary

**Opening leaf of Ch 15** *Looking Ahead: Other Parallel Systems* of *[[DiveIntoSystems]]* — pivots from Ch 14's shared-memory [[Pthreads]] / [[OpenMP]] CPU-thread world into the **heterogeneous-computing** chapter. Codifies the **host/device split** that defines [[GPGPU|GPGPU computing]]: *"Heterogeneous computing is computing using multiple, different processing units found in a computer ... support for parallel computing using the computer's CPU cores and one or more of its accelerator units such as graphics processing units (GPUs)."* The [[GPU]] is presented as a massively-parallel co-processor organized as [[StreamingMultiprocessor|streaming multiprocessors]] (SMs), each holding multiple [[StreamingProcessor|scalar processor cores]] + a [[Warp|warp scheduler]] + L1 cache + [[SharedMemory|shared memory]]. [[CUDA]] (NVIDIA's *Compute Unified Device Architecture*) is the programming model: kernels declared `__global__`, launched from host with the `<<<grid, block>>>` syntax, with **separate host and device memory spaces** explicitly managed via [[CudaMalloc|`cudaMalloc`]] / [[CudaMemcpy|`cudaMemcpy`]] / [[CudaFree|`cudaFree`]]. The [[SIMT]] execution model has 32-thread [[Warp|warps]] executing the same instruction in lockstep on different data — the **141st ingested DIS chapter — opens Ch 15.**

## Key Claims

- **[[SIMT|SIMT execution model]]** — *"In lockstep execution, each thread in a warp executes the same instruction each cycle but on different data ... each thread in the warp executes these instructions on a different pixel data value."* A variation of [[SIMD]] where the lockstep group is a hardware-managed thread bundle (the [[Warp]]) rather than a vector lane.
- **[[StreamingMultiprocessor|SM]] architecture** — NVIDIA GPUs organize processors into streaming multiprocessors, each containing multiple [[StreamingProcessor|scalar processor cores]], a [[Warp|warp scheduler]], L1 cache, and [[SharedMemory|shared memory]] for coordinated thread execution.
- **Three-level thread hierarchy** — CUDA threads are organized into [[Block|blocks]], which are organized into [[Grid|grids]]; threads within a block execute in lockstep as [[Warp|warps]] of 32, enabling fine-grained synchronization **only within blocks**, not across the entire grid.
- **Heterogeneous memory model** — *"The host operating system does not manage the GPU's processors or memory ... space for program data needs to be allocated on the GPU and the data copied between the host memory and the GPU memory by the programmer."* Explicit allocation via [[CudaMalloc|`cudaMalloc`]], deallocation via [[CudaFree|`cudaFree`]], data transfer via [[CudaMemcpy|`cudaMemcpy`]].
- **Kernel function model** — Functions annotated with `__global__` execute on the device; each thread computes its data slice using thread identifiers ([[CudaThreadIndex|`threadIdx`]], `blockIdx`) and block dimensions (`blockDim`). [[KernelLaunch|Launch syntax]] is `kernel<<<numBlocks, threadsPerBlock>>>(args)`.
- **Implicit kernel synchronization** — CUDA guarantees all threads from one kernel call complete before subsequent kernel calls begin; intra-block synchronization via [[CudaThreadSynchronize|`__syncthreads()`]] but **no native inter-block barrier within a single kernel**.
- **Multidimensional thread layouts** — Programmers can organize blocks and threads into one-, two-, or three-dimensional layouts to match data structure dimensionality (e.g., matrix work uses 2-D grids/blocks).
- **GPGPU sweet spot** — GPUs excel at **embarrassingly parallel** workloads or large independent stream-based computations; they **struggle** when CPU↔GPU data transfer dominates execution time or when fine-grained synchronization is needed.

## Key Quotes

> *"Heterogeneous computing is computing using multiple, different processing units found in a computer ... Typically, heterogeneous computing means support for parallel computing using the computer's CPU cores and one or more of its accelerator units such as graphics processing units (GPUs)."*

> *"In lockstep execution, each thread in a warp executes the same instruction each cycle but on different data ... each thread in the warp executes these instructions on a different pixel data value."*

> *"The host operating system does not manage the GPU's processors or memory ... space for program data needs to be allocated on the GPU and the data copied between the host memory and the GPU memory by the programmer."*

## Connections

- [[DiveIntoSystems]] — parent textbook; **opening leaf of Ch 15** *Looking Ahead: Other Parallel Systems*.
- [[GPU]] / [[GPGPU]] / [[CUDA]] / [[SIMT]] / [[Warp]] / [[Block]] / [[Grid]] / [[StreamingMultiprocessor]] / [[StreamingProcessor]] — the [[ParallelProcessorsAlgorithms|ParProc Ch 5]] CUDA-corpus pages this chapter reuses; DIS gives the introductory framing, ParProc gives the depth.
- [[KernelLaunch]] / [[CudaThreadSynchronize]] / [[SharedMemory]] / [[GlobalMemory]] / [[gpumemoryhierarchy]] — the CUDA execution and memory machinery underneath kernel launches.
- [[CudaThreadIndex]] — **new** concept page for the `threadIdx` / `blockIdx` / `blockDim` indexing scheme that maps threads to data.
- [[SIMD]] — SIMT's vector-lane ancestor.
- [[ConcurrencyVsParallelism]] / [[ParallelSpeedup]] / [[AmdahlsLaw]] — the Ch 14 performance lenses now applied to a *different* parallel substrate.

## Contradictions

None — DIS Ch 15.1 is the **textbook introductory framing** of CUDA / GPU programming; consistent with the deeper [[parproc-ch05-cuda-gpu-programming|ParProc Ch 5]] treatment.

## Notes

- **141st ingested DIS chapter — opens Ch 15** *Looking Ahead: Other Parallel Systems*.
- **Reuses extensively** from ParProc Ch 5 CUDA corpus: [[CUDA]], [[GPU]], [[GPGPU]], [[SIMT]], [[Warp]], [[Block]], [[Grid]], [[StreamingMultiprocessor]], [[StreamingProcessor]], [[KernelLaunch]], [[SharedMemory]], [[GlobalMemory]], [[CudaThreadSynchronize]], [[gpumemoryhierarchy]].
- **Mints 1 new concept page**: [[CudaThreadIndex]] (the `threadIdx` / `blockIdx` / `blockDim` indexing scheme — ParProc covered it in passing but lacked a dedicated page).
