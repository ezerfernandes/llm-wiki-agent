---
title: "PCIe"
type: concept
tags: [hardware, interconnect, infrastructure]
sources: [d2l-computational-performance, mlsysbook-ch11-hardware-acceleration]
last_updated: 2026-06-05
---

# PCIe (PCI Express)

The standard expansion bus connecting peripherals — [[GPU|GPUs]], SSDs, NICs — to the CPU. Point-to-point dedicated lanes; bandwidth scales with lane count ([[d2l-computational-performance]] §`hardware`).

## Bandwidth

| Gen | Per lane (each direction) | ×16 slot (each direction) |
|---|---|---|
| PCIe 3.0 | 1 GB/s | 16 GB/s |
| PCIe 4.0 | 2 GB/s | 32 GB/s |
| PCIe 5.0 | 4 GB/s | 64 GB/s |

GPUs typically use 16 lanes per card. Latency is ~5 µs.

## Lane budgets

CPU PCIe lane counts ([[d2l-computational-performance]] §`hardware`):

- AMD EPYC 3 — 128 lanes.
- Intel Xeon — up to 48 lanes per chip.
- Ryzen 9 — 20 lanes (desktop).
- Core i9 — 16 lanes (desktop).

Since each high-end GPU wants 16 lanes, **desktop CPUs cannot drive more than 1–2 GPUs at full bandwidth**. Server boards use PCIe switches (multiplexers) to oversubscribe lanes when full simultaneous bandwidth isn't required.

## Latency / bandwidth profile

- 1 MB GPU↔CPU transfer ≈ 80 µs at ~12 GB/s on PCIe 3.0 ×16.
- Compare [[NVLink]] 40 GB transfer ≈ 30 µs at ~33 GB/s.

Bulk transfers are preferred — packet overhead matters. The "transfers are slow" rule of thumb across [[GPU]] / [[d2l-builders-guide]] / [[FlashAttention]] is rooted in PCIe's bandwidth-to-compute ratio.

## See also
- [[NVLink]] — the higher-bandwidth alternative for GPU↔GPU.
- [[GPU]] / [[CUDA]] — what PCIe connects.
- [[gpumemoryhierarchy]] — the within-GPU equivalent of this latency story.
- [[d2l-computational-performance]] §`hardware`.
