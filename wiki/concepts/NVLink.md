---
title: "NVLink"
type: concept
tags: [hardware, gpu, nvidia, interconnect]
sources: [d2l-computational-performance, mlsysbook-ch11-hardware-acceleration]
last_updated: 2026-06-05
---

# NVLink

NVIDIA's proprietary high-bandwidth GPU-to-GPU (and GPU-to-CPU on Power9) interconnect. Replaces / augments [[PCIe]] for tightly-coupled multi-GPU servers ([[d2l-computational-performance]] §`hardware`).

## Bandwidth

- **Per link:** 300 Gbit/s ≈ 18 GB/s per direction (bidirectional).
- **Server GPU (V100):** 6 links → ~100 GB/s aggregate per GPU.
- **Consumer GPU (RTX 2080 Ti):** 1 link at reduced 100 Gbit/s.
- **Modern A100/H100:** 12 links, NVLink 4.0 at 900 GB/s aggregate.

Compare: [[PCIe]] 4.0 ×16 ≈ 32 GB/s, 100 GbE Ethernet ≈ 10 GB/s. **NVLink is ~3–10× faster than the next-best interconnect available to the CPU.**

## Why it matters

[[d2l-computational-performance]]'s [[RingAllReduce|ring-allreduce]] analysis: 160 MB across 8× V100 takes ~6 ms over NVLink — *better than PCIe even at 8 GPUs*, because the ring exploits NVLink's aggregate bandwidth.

NVLink is what makes large dense-LLM training feasible: gradient all-reduce traffic on a 70B-parameter model is hundreds of GB per step, and only NVLink-grade fabric can sustain this within a step budget.

## Topology

- **DGX-1 (8× V100):** hybrid cube-mesh with 6 NVLinks per GPU; not all GPU pairs have direct NVLink — the topology decomposes into two rings ([[d2l-computational-performance]] §`parameterserver` Fig. `nvlink-twoloop`).
- **DGX-2 / HGX (8–16× GPU):** NVSwitch — a full-bandwidth NVLink crossbar, every GPU has full bandwidth to every other GPU.
- **DGX H100 / B200:** NVLink 4/5 + NVSwitch 3; can extend across racks via NVLink Switch System.

## See also
- [[NCCL]] — the library that routes over NVLink.
- [[PCIe]] — the slower fallback.
- [[RingAllReduce]] — the algorithm that exploits NVLink topology.
- [[GPU]] / [[NVIDIA]] — the hardware.
- [[d2l-computational-performance]] §`hardware`.
