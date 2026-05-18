---
title: "Thread Divergence"
type: concept
tags: [gpu, cuda, performance, simt]
sources: [parproc-ch05-cuda-gpu-programming]
last_updated: 2026-05-17
---

# Thread Divergence

When threads **within the same 32-thread [[Warp]]** take different branches of an `if/else`, they cannot execute in [[SIMT]] lockstep. The hardware serializes the divergent paths — threads on the *then* branch execute while *else*-branch threads idle, then they swap — *"This renders the code at that point somewhat serial rather than parallel"* ([[parproc-ch05-cuda-gpu-programming]] §5.4.2.2). Matloff cites a CUDA web tutorial calling thread divergence a *"performance killer."*

## The crucial scope rule

Divergence only costs performance **within a warp**. Threads in the same [[Block]] but **different warps** can diverge freely — each warp has its own program counter and runs on the [[StreamingMultiprocessor|SM]]'s warp scheduler independently. The optimization heuristic follows directly:

- **Bad**: threads 0 and 1 of a block take different branches → both are warp 0 → serialization.
- **Fine**: threads 0 and 32 take different branches → different warps → no penalty.

## Programming consequences

- **Arrange branches by warp boundaries.** When threads are doing fundamentally different work (e.g. boundary cells vs interior cells), align the partition with multiples of 32.
- **Replace branches with predication where cheap.** A `result = cond ? a : b` may compile to a masked operation that all threads execute, avoiding the divergence cost.
- **Lockstep-friendly algorithm restructuring.** The Sieve of Eratosthenes in [[parproc-ch05-cuda-gpu-programming]] §5.10 is rewritten *"so that the second version will be more amenable to lockstep execution, thus causing less thread divergence"* — instead of one thread per prime, all threads cooperate on each prime's multiples, smoothing per-thread work.
- **Smaller blocks can help when work is divergent.** ([[parproc-ch05-cuda-gpu-programming]] §5.6) *"Two threads doing unrelated work, or the same work but with many if/elses, would cause a lot of thread divergence if they were in the same block. This argues for a smaller block size."*

## Related concerns

- [[MemoryCoalescing|Memory coalescing]] has an analogous warp-boundary structure: it cares about half-warp address patterns.
- [[LoopUnrolling]] can eliminate branches in inner loops, indirectly reducing divergence opportunities.

## See also

- [[Warp]] — the lockstep unit divergence harms.
- [[SIMT]] — the execution model that makes divergence costly.
- [[Block]] — divergence across blocks/warps within a block is free.
- [[parproc-ch05-cuda-gpu-programming]] — §5.4.2.2 / §5.6 / §5.10.
