---
title: "Tiling (Loop Blocking)"
type: concept
tags: [hardware, accelerators, tiling, memory-optimization, compilers]
sources: [mlsysbook-ch11-hardware-acceleration]
last_updated: 2026-06-05
---

# Tiling (Loop Blocking)

**Tiling** restructures a computation into smaller blocks ("tiles") that fit within fast local memory (registers, SRAM, scratchpad), so each loaded value is reused many times before eviction. The core insight: *if we cannot make memory faster, we can at least make fewer trips to it.* A naive $N×N$ matrix multiply makes $\mathcal{O}(N^3)$ memory accesses, fetching the same elements repeatedly from slow DRAM; tiling fetches each tile once, yielding the **10–50× speedup** between naive and optimized [[GEMM]].

## The tiling principle: bridging graph and silicon ([[mlsysbook-ch11-hardware-acceleration]])

There is a mismatch between the computation graph (a single 4096×4096 matmul) and the physical [[SystolicArray|systolic array]] (a fixed 128×128 grid). The compiler decomposes the operation into 1,024 tiles, each staged HBM → SRAM → array, achieving 128× reuse per loaded byte. If a dimension is not a multiple of the tile size (e.g. width 129 on a 128 array), the system pays a **"fringe tax"**: 127 units idle while one finishes the remainder tile.

## Variants

- **Spatial tiling** — partition data into cache-friendly blocks (matmul, CNN feature maps).
- **Temporal tiling** — explicitly stage data in fast memory and reorder loops around it (convolution weight reuse, attention).
- **Hybrid tiling** — combine both, dynamically adjusting tile size.

Tile size is a trade-off: too small and memory fetches still dominate; too large and it spills fast memory or unbalances parallel load. [[XLA]], [[TVM]], and [[MLIR]] select tiling automatically.

## See also
- [[LoopTiling]] — the same technique under the loop-nest framing.
- [[KernelFusion]] — the complementary "combine operations" technique.
- [[FlashAttention]] — sequence-dimension tiling that avoids materializing the attention matrix in HBM.
- [[SystolicArray]] / [[MemoryHierarchy]] — what tiles map onto.
- [[mlsysbook-ch11-hardware-acceleration]] — the tiling principle, fringe tax, spatial/temporal/hybrid variants.
