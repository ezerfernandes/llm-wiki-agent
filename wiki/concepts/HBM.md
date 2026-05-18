---
title: "HBM"
type: concept
tags: [hardware, gpu, memory]
sources: [d2l-computational-performance, 2205.14135-flashattention]
last_updated: 2026-05-16
---

# HBM (High Bandwidth Memory)

3D-stacked DRAM modules mounted on a silicon interposer next to the GPU die, connected via a very wide bus (1024+ bits) instead of a long PCB trace. Used in **server-grade GPUs** (NVIDIA V100, A100, H100, AMD MI series, Google TPU) where consumer GDDR can't keep up with the SM throughput ([[d2l-computational-performance]] §`hardware`).

## Why HBM

GPU memory needs to feed thousands of arithmetic units. Two scaling levers:

1. **Wider memory bus** — RTX 2080 Ti (consumer) has a 352-bit GDDR6 bus → ~500 GB/s aggregate. Server NVIDIA HBM2/3 has a 4096+ -bit interface → 1.5–3 TB/s aggregate.
2. **HBM stacks beside the die** — 3D-stacked DRAM connected directly via the silicon interposer.

> *"HBM […] modules use a very different interface and connect directly with GPUs on a dedicated silicon wafer. This makes them very expensive and their use is typically limited to high-end server chips."* — [[d2l-computational-performance]]

## Numbers

| GPU | Memory type | Capacity | Bandwidth |
|---|---|---|---|
| RTX 2080 Ti | GDDR6 | 11 GB | ~616 GB/s |
| RTX 4090 | GDDR6X | 24 GB | ~1.0 TB/s |
| V100 | HBM2 | 16/32 GB | ~900 GB/s |
| A100 | HBM2e | 40/80 GB | 1.6/2.0 TB/s |
| H100 | HBM3 | 80 GB | 3.0 TB/s |
| B200 | HBM3e | 192 GB | 8 TB/s |

## In the cost model

[[2205.14135-flashattention]] and [[gpumemoryhierarchy]] both rely on the HBM ↔ on-chip-SRAM asymmetry as their algorithm-design lever: SRAM is ~10× faster than HBM but ~10,000× smaller. The point of kernel fusion / FlashAttention / FlashAttention-2/3 is to keep the working set in SRAM and write only the final result back to HBM.

The chapter-level analogue ([[d2l-computational-performance]]) operates one tier higher: HBM↔host-DRAM via [[PCIe]] is ~100× slower than HBM bandwidth, so the rule "few large transfers, not many small ones" applies twice.

## See also
- [[gpumemoryhierarchy]] — the full per-tier breakdown.
- [[GPU]] / [[NVIDIA]] — the hardware.
- [[FlashAttention]] / [[2205.14135-flashattention]] — the within-GPU memory-aware algorithm.
- [[NVLink]] — what GPUs use to ship bytes *between* HBM banks across cards.
- [[d2l-computational-performance]] §`hardware`.
