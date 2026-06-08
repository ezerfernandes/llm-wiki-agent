---
title: "Dataloader Choke Point"
type: concept
tags: [ml-systems, mlsysbook, data-engineering, training, io]
sources: [mlsysbook-ch04-data-engineering]
last_updated: 2026-06-05
---

# Dataloader Choke Point

The training-throughput bottleneck that arises when the data pipeline cannot feed an accelerator fast enough to keep it busy (Reddi, [[mlsysbook-ch04-data-engineering|Vol 1, Ch 4]]). Training step time is governed by $T_{\text{step}} = \max(T_{\text{compute}}, T_{\text{io}})$, so when CPU-side data loading (decoding JPEGs, computing features) is slower than GPU compute, the expensive silicon sits idle in a "starvation region" where **adding more GPUs yields zero speedup**.

Related framing: the **feeding tax** (wall-clock time lost to I/O wait, reducing system efficiency $\eta_{\text{hw}}$) and the **feeding problem** (saturating a high-throughput "Machine" from a low-bandwidth "Data" source). A standard cloud disk can leave a 300-TFLOP/s accelerator >80% idle; training ResNet-50 on an A100 needs ≥8 CPU dataloader workers just to keep the GPU from starving.

Mitigations: faster storage ([[TieredStorage|NVMe]]), parallel workers (PyTorch DataLoader), prefetching/caching (tf.data), GPU-side augmentation (NVIDIA DALI), and efficient formats ([[Parquet]]).

## Connections

- [[IronLawOfMLSystems]] — the system-efficiency term the choke point degrades.
- [[TieredStorage]] / [[StorageArchitecture]] — the storage side of the bottleneck.
- [[Parquet]] / [[Snappy]] — format/compression levers that raise effective bandwidth.
- [[DataIngestion]] — the pipeline stage where the IO bottleneck lives.
- [[mlsysbook-ch04-data-engineering]] — source.
