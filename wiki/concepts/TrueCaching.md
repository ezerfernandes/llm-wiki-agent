---
title: "True Caching (CUDA)"
type: concept
tags: [gpu, cuda, memory, cache]
sources: [parproc-ch05-cuda-gpu-programming]
last_updated: 2026-05-17
---

# True Caching (CUDA)

The newer-[[CUDA]]-generation feature in which the on-chip memory of a [[StreamingMultiprocessor|streaming multiprocessor]] can be **apportioned between programmer-managed [[SharedMemory|shared memory]] and an automatic L1 cache** ([[parproc-ch05-cuda-gpu-programming]] §5.17.1).

> *"Shared memory is in essence a programmer-managed cache, but now on-chip memory can be apportioned to both shared memory and a true cache. This makes less work for the programmer, at a possible cost of reduced performance."*

## The framing

Pre-Fermi NVIDIA GPUs (the Tesla baseline Matloff covers) had **only** programmer-managed [[SharedMemory|shared memory]] on-chip — no automatic cache for [[GlobalMemory|global memory]]. Programmers explicitly copied data from global to shared, computed, and copied back. From Fermi onward, NVIDIA added a true L1 data cache; the on-chip storage is split between the two roles.

Programmer-cognitive-load progression:

| Generation | On-chip storage role | Programmer effort |
|---|---|---|
| Tesla | All [[SharedMemory|shared memory]] | High (manual staging) |
| Fermi+ | Split: shared + automatic L1 | Lower (cache handles common cases) |

## Performance tradeoff

The automatic L1 cache makes naive code faster (no staging), but **less predictable** — the programmer no longer fully controls what's on-chip. High-performance code typically:

- Still uses explicit shared memory for predictable, reuse-heavy patterns.
- Lets the L1 cache pick up incidental reuse.
- Tunes the split via runtime APIs (`cudaFuncSetCacheConfig` and successors).

## Relationship to other tiers

- [[ConstantMemory]] and [[TextureMemory]] have **their own** dedicated caches (separate from the L1 / shared split discussed here).
- [[GlobalMemory]] reads can now hit the L1 cache (on Fermi+) — Tesla baseline was "no cache."

## See also

- [[SharedMemory]] — the programmer-managed half of the split.
- [[GlobalMemory]] — what L1 caches.
- [[UnifiedMemory]] — the other Newer-Generations "programmer convenience" feature in §5.17.
- [[GPUMemoryHierarchy]] — full memory tier table.
- [[CUDA]] — substrate.
- [[parproc-ch05-cuda-gpu-programming]] — §5.17.1.
