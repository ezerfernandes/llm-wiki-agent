---
title: "NVIDIA Pascal"
type: concept
tags: [gpu, nvidia, architecture]
sources: [parproc-ch05-cuda-gpu-programming]
last_updated: 2026-05-17
---

# NVIDIA Pascal

[[NVIDIA]]'s 2016 GPU architecture, succeeding Maxwell and preceding Volta. The flagship card was the **P100** (GP100 die, 16 GB HBM2, NVLink 1.0); the consumer line spans the GTX 10x0 series.

## Why Pascal matters for [[CUDA]]

[[parproc-ch05-cuda-gpu-programming]] §5.17.2 cites Pascal as the first architecture with **hardware-assisted [[UnifiedMemory|Unified Memory]]**:

> *"Starting with the Pascal model series, there is hardware assist for [Unified Memory], using something similar to virtual memory page tables."*

Pre-Pascal Unified Memory was a software-managed convenience with coarse-grained migration and substantial overhead. Pascal's page-fault hardware enables on-demand migration at page granularity, comparable to CPU virtual memory — making `__managed__` data a viable starting point for porting CPU code to GPU.

## Position in NVIDIA's lineage

| Architecture | Card | Year | Highlight |
|---|---|---|---|
| Tesla | G80 / GT200 | 2006–2008 | First CUDA; [[parproc-ch05-cuda-gpu-programming|Ch5]] baseline |
| Fermi | GF100 | 2010 | First L1 cache ([[TrueCaching]]) |
| Kepler | GK100/110 | 2012 | Dynamic parallelism |
| Maxwell | GM200 | 2014 | Power efficiency |
| **Pascal** | **P100** | **2016** | **HW-assisted [[UnifiedMemory]]; NVLink; HBM2** |
| Volta | V100 | 2017 | First Tensor Cores |
| Turing | TU102 | 2018 | RT cores |
| Ampere | A100 | 2020 | bf16, MIG, 40/80 GB HBM2e |
| Hopper | H100 | 2022 | FP8, Transformer Engine |
| Blackwell | B200 | 2024–2025 | FP4, NVLink fabric |

## See also

- [[NVIDIA]] — vendor.
- [[CUDA]] — programming model.
- [[UnifiedMemory]] — the headline Pascal feature for general-purpose CUDA users.
- [[parproc-ch05-cuda-gpu-programming]] — §5.17.2.
