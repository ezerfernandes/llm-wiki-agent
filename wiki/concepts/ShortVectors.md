---
title: "Short Vectors (CUDA)"
type: concept
tags: [gpu, cuda, performance, simd, bandwidth]
sources: [parproc-ch05-cuda-gpu-programming]
last_updated: 2026-05-17
---

# Short Vectors (CUDA)

[[CUDA]] built-in types — `int2`, `int4`, `uint4`, `char2`, `float4`, etc. — that pack 2–4 elements into a single word for memory access and instruction processing ([[parproc-ch05-cuda-gpu-programming]] §5.16).

> *"A short vector can be treated as a single word in terms of memory access and GPU instructions. It may be possible to reduce time by a factor of 4 by dividing arrays into chunks of four contiguous words and making short vectors from them."*

## Examples

| Type | Lanes | Per-lane type | Total bits |
|---|---|---|---|
| `int2` | 2 | `int` | 64 |
| `int4` | 4 | `int` | 128 |
| `char2` | 2 | `char` | 16 |
| `uint4` | 4 | `unsigned int` | 128 |
| `float4` | 4 | `float` | 128 |

## Why it works

GPU memory-access width and instruction width can each handle 128-bit operands. A loop that reads four `int`s individually takes four global-memory transactions in the worst case; the same loop reading one `int4` takes one transaction, potentially **4× the bandwidth**. This stacks with [[MemoryCoalescing|coalescing]] — half-warp threads each reading `int4`s coalesce just like half-warp threads reading `int`s, but at 4× the total data.

## Tradeoffs

- Requires the **array layout** to be 4-element aligned in memory; mid-array offsets break the trick.
- Loop bodies must do **per-lane work** (e.g. `sum += v.x + v.y + v.z + v.w`) — extra unpack work in the kernel.
- Beneficial when the kernel is **bandwidth-bound**; less help when compute-bound.

## See also

- [[CUDA]] — defines these types.
- [[MemoryCoalescing]] — the orthogonal half-warp coalescing optimization.
- [[LoopUnrolling]] — sibling small-scope optimization.
- [[parproc-ch05-cuda-gpu-programming]] — §5.16.
