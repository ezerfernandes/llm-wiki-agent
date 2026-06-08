---
title: "SIMT (Single Instruction, Multiple Thread)"
type: concept
tags: [gpu, cuda, parallelism, execution-model]
sources: [parproc-ch05-cuda-gpu-programming, mlsysbook-ch11-hardware-acceleration]
last_updated: 2026-06-05
---

# SIMT (Single Instruction, Multiple Thread)

NVIDIA's name for the execution pattern in which all 32 threads of a [[Warp]] run the **same instruction in lockstep**. During each instruction fetch cycle, the same instruction is fetched for every thread in the warp; during the execution cycle, each thread either executes that instruction or executes nothing (when masked off by a branch). This is the classical [[SIMD]] pattern (used historically in the ILLIAC IV); on GPUs it is renamed **SIMT** because the lockstep group is a hardware-managed thread bundle rather than a vector lane ([[parproc-ch05-cuda-gpu-programming]] §5.4.2.1).

## Why "multiple thread" and not "multiple data"

Each thread in a SIMT warp has its own:

- **registers** — a context switch among warps on the same [[StreamingMultiprocessor|SM]] does almost no save/restore work because each warp's registers are physically distinct.
- **program counter** (logically) — when threads diverge on an `if/else`, the warp serializes through both branches with the off-branch threads masked. This is **[[ThreadDivergence|thread divergence]]**, the *"performance killer"*.
- **memory operand addresses** — coalescable when consecutive, but not required to be.

In pure SIMD vector hardware, the "threads" are vector lanes that share a single program counter — divergence is impossible and addresses are usually structured. SIMT is the more permissive model: the programmer writes scalar thread code; the hardware groups 32 threads and runs them in lockstep when possible.

## SIMT vs SIMD vs MIMD

| Model | Execution unit | Address space | Branch divergence | Examples |
|---|---|---|---|---|
| [[SIMD]] | Vector lane | Shared (one stream) | Impossible | ILLIAC IV, SSE/AVX, ARM SVE |
| **SIMT** | Thread within warp | Per-thread, in shared memory tier | Possible (serializes) | NVIDIA warps, AMD wavefronts |
| MIMD | Independent thread | Per-thread | Free | CPU [[Multicore]], [[Pthreads]], [[OpenMP]] |

## Performance implications

- **Block sizes should be multiples of 32.** A block of 17 threads still consumes a full warp's worth of SP cycles, wasting 15.
- **Concentrate divergent code across warps, not within.** Two threads in **different warps** of the same [[Block]] can take different branches with no penalty. Two threads in the **same warp** doing the same will serialize.
- **Warps are the unit of latency hiding.** The SM's "[[OSInHardware|OS in hardware]]" schedules warps on its [[StreamingProcessor|SPs]] in fixed-length timeslices; on a long [[GlobalMemory|global-memory]] stall it swaps to another ready warp.

## See also

- [[Warp]] — the 32-thread SIMT unit.
- [[ThreadDivergence]] — the cost when threads in one warp branch differently.
- [[CUDA]] — the programming model SIMT runs underneath.
- [[StreamingMultiprocessor]] — the SM hosts warps and applies SIMT scheduling.
- [[SIMD]] — the ancestor architecture.
- [[parproc-ch05-cuda-gpu-programming]] — the §5.4.2 source.
