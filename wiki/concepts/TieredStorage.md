---
title: "Tiered Storage"
type: concept
tags: [infrastructure, data, mlops, mlsysbook]
sources: [mlsysbook-ch03-ml-workflow, mlsysbook-ch04-data-engineering]
last_updated: 2026-06-05
---

# Tiered Storage

Placing data on different storage media by access frequency and performance requirement (Reddi, [[mlsysbook-ch03-ml-workflow|Vol 1, Ch 3]]):

- **Hot** — high-throughput NVMe SSD (~$0.10/GB-mo, 500K+ IOPS) for data in active training loops.
- **Warm** — S3-compatible object storage (~$0.023/GB-mo, 100–200 ms latency) for recent datasets and validation sets.
- **Cold** — low-cost archival (e.g., AWS Glacier) for regulatory-audit data rarely accessed.

The hot/cold price gap is ~4×. Boundaries are dynamic: a dataset migrates warm→hot when selected for the next training run, hot→cold when its model is superseded, managed by automated lifecycle policies. The systems stakes: for ML training loops needing sustained 1–10 GB/s sequential reads, **choosing the wrong tier converts a compute-bound pipeline into an I/O-bound one**, directly inflating the iron law's data term $D_{\text{vol}}/\text{BW}$.

## Connections

- [[IronLawOfMLSystems]] — the $D_{\text{vol}}/\text{BW}$ term the storage tier governs.
- [[DataVersioning]] / [[DataLineage]] — what migrates across tiers.
- [[DataEngineering]] — explored in depth in Ch 4.
- [[StorageArchitecture]] — [[mlsysbook-ch04-data-engineering|Ch 4]] situates these tiers within the database/warehouse/lake decision and quantifies the ~50× NVMe-vs-object-storage iteration-speed gap.
- [[DataLoaderChokePoint]] — the feeding tax these tiers must overcome to keep accelerators fed.
- [[mlsysbook-ch03-ml-workflow]] / [[mlsysbook-ch04-data-engineering]] — sources.
