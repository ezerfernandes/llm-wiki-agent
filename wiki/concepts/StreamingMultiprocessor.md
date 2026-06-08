---
title: "Streaming Multiprocessor (SM)"
type: concept
tags: [gpu, cuda, hardware, nvidia]
sources: [parproc-ch05-cuda-gpu-programming, mlsysbook-ch11-hardware-acceleration]
last_updated: 2026-06-05
---

# Streaming Multiprocessor (SM)

The **multiprocessor unit** of an [[NVIDIA]] GPU. A GPU contains many SMs; each SM contains many [[StreamingProcessor|streaming processors]] (SPs, individual cores). *"Since each SM is essentially a multicore machine in its own right, you might say the GPU is a multi-multiprocessor machine."* ([[parproc-ch05-cuda-gpu-programming]] §5.4.1).

## What an SM owns

- A set of [[StreamingProcessor|SPs]] (the actual ALUs).
- A slice of on-chip storage shared by the [[Block|blocks]] currently assigned to it — split between [[SharedMemory|shared memory]] and (on Fermi+) an L1 cache; see [[TrueCaching]].
- A large register file (more numerous than a CPU core's).
- A warp scheduler that picks among in-flight [[Warp|warps]] on each cycle ("[[OSInHardware|OS in hardware]]").

## Key constraints (Tesla baseline)

- Max **threads per SM**: 786.
- Max **threads per block**: 512.
- A block is bound to one SM for the lifetime of its kernel — **the programmer has no control over which SM**.
- Multiple blocks may share an SM, dividing the SM's shared-memory pool among them.
- **SMs cannot synchronize via barrier** with each other. *"This is actually a great advantage, as the independence of threads in separate SMs means that the hardware can run faster."* (§5.4.1).

## SM as scheduler

The SM runs threads in [[Warp|warps]] of 32 under [[SIMT]] lockstep. When a warp blocks on a long [[GlobalMemory|global-memory]] access, the SM schedules another ready warp — this is the basic **[[LatencyHiding|latency hiding]]** mechanism. Context switches between warps are nearly free because each warp has its own physical register set.

## See also

- [[StreamingProcessor]] — the SPs an SM contains.
- [[Block]] — the assignment unit; blocks bind to SMs.
- [[Warp]] — the SIMT execution unit the SM schedules.
- [[CUDA]] — programming model.
- [[NVIDIA]] — vendor.
- [[parproc-ch05-cuda-gpu-programming]] — §5.4.1 / §5.4.2.
