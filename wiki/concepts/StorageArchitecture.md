---
title: "Storage Architecture (ML)"
type: concept
tags: [ml-systems, mlsysbook, data-engineering, storage, infrastructure]
sources: [mlsysbook-ch04-data-engineering]
last_updated: 2026-06-05
---

# Storage Architecture (ML)

The choice of storage system for ML data, framed in Reddi's *Machine Learning Systems* ([[mlsysbook-ch04-data-engineering|Vol 1, Ch 4]]) as a decision about which performance metric to optimize for the dominant access pattern, and as minimizing the [[IronLawOfMLSystems|iron law]]'s data term $D_{\text{vol}}/\text{BW}$.

Two core metrics: **IOPS** (distinct requests/s — limits random access like fetching small batches or user profiles) and **Throughput/Bandwidth** (volume/s — limits sequential access like scanning a [[Parquet]] file). The three architectures map to ML workflow stages:

- **Databases (OLTP)** — high IOPS, small blocks → online feature serving (millisecond point lookups). Struggle on repeated full scans (row-oriented reads whole rows for a few columns).
- **[[DataWarehouse|Data warehouses]] (OLAP, columnar)** — high throughput → batch training and feature engineering (5–10× I/O reduction reading only needed columns). Assume stable schemas.
- **[[DataLake|Data lakes]]** — capacity + schema-on-read → petabyte raw/unstructured training data. Degrade into "data swamps" without metadata/cataloging.

Choosing the wrong system creates order-of-magnitude penalties no software fix can overcome. Mature orgs use all three behind a unified catalog. Storage performance is the iteration-speed lever: NVMe loads ~50× faster than object storage, and saturating an A100 demands multiple GB/s (SATA SSD leaves it at ~13% utilization). [[FeatureStore|Feature stores]] sit atop this layer to enforce train/serve consistency.

## Connections

- [[IronLawOfMLSystems]] — the $D_{\text{vol}}/\text{BW}$ term storage governs.
- [[DataLake]] / [[DataWarehouse]] / [[Lakehouse]] — the three architectures.
- [[TieredStorage]] — hot/warm/cold cost-performance tiers.
- [[Parquet]] / [[ColumnarStorage]] / [[Snappy]] — format/compression levers.
- [[FeatureStore]] — the consistency layer above storage.
- [[DataGravity]] — the physics constraining storage placement.
- [[mlsysbook-ch04-data-engineering]] — source.
