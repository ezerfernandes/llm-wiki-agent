---
title: "Warp"
type: concept
tags: [gpu, cuda, simt, hardware]
sources: [parproc-ch05-cuda-gpu-programming]
last_updated: 2026-05-17
---

# Warp

A **warp** is a group of **32 threads** that the [[NVIDIA]] GPU hardware schedules and executes as a unit under [[SIMT]] lockstep. The hardware assigns an entire [[Block]] to one [[StreamingMultiprocessor|SM]], then partitions that block into warps of 32; the SM's warp scheduler then picks one warp at a time to issue instructions on its [[StreamingProcessor|SPs]] ([[parproc-ch05-cuda-gpu-programming]] §5.4.2.1).

## Key properties

- **Size is always 32** on NVIDIA hardware — across Tesla / Fermi / Kepler / Pascal / Volta / Ampere / Hopper.
- **All threads in a warp run the same instruction.** Branch divergence is handled by predication (off-branch threads execute nothing during the on-branch cycle) — this is [[ThreadDivergence]].
- **Each warp has its own register file.** Context switching between warps on an SM is nearly free — *"a context switch does very little saving and restoring of context, quite a contrast to the OS case"* (§5.4.2.3).
- **Warps are the unit of latency hiding.** When a warp blocks on a long [[GlobalMemory|global-memory]] access, the SM schedules another warp; this is the "[[OSInHardware|OS in hardware]]" pattern.
- **Half-warp = 16 threads.** [[MemoryCoalescing|Memory coalescing]] operates at half-warp granularity on Tesla — *"all memory accesses in a half-warp simultaneously"*. Shared-memory bank conflicts also resolve at half-warp scope on Tesla; newer architectures use full warps.

## Implications for block sizing

- **Block size should be a multiple of 32.** A block of 17 threads consumes one full warp of SP cycles, wasting 15.
- **Block size ≥ 32.** Below this, the SM uses only part of its SP cluster.
- **Many warps per SM helps latency hiding.** The more ready-to-run warps an SM has, the more memory latency it can hide by swapping. *"This argues for a larger block size."* (§5.6)

## See also

- [[SIMT]] — the execution model.
- [[Block]] — the parent unit; one block = one or more warps.
- [[ThreadDivergence]] — what happens when threads in a warp branch differently.
- [[MemoryCoalescing]] — half-warp consecutive-word access optimization.
- [[StreamingMultiprocessor]] — the SM that schedules warps.
- [[parproc-ch05-cuda-gpu-programming]] — §5.4.2.1 / §5.4.2.3 / §5.6.
