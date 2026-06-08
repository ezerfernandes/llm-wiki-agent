---
title: "Data Gravity"
type: concept
tags: [ml-systems, mlsysbook, data-engineering, storage, physics]
sources: [mlsysbook-ch04-data-engineering, mlsysbook-ch16-conclusion]
last_updated: 2026-06-05
---

# Data Gravity

The **cost of moving data**, a function of volume and bandwidth = the [[IronLawOfMLSystems|iron law]]'s data term $D_{\text{vol}}/\text{BW}$ (Reddi, [[mlsysbook-ch04-data-engineering|Vol 1, Ch 4]]). It is fixed by physics: moving 1 PB across a 10 Gbps link takes ~9 days, and ~$90K in egress at 2024 AWS rates.

This gravity dictates architecture. Because moving petabytes to the compute is slow and expensive, **the compute must move to the data** — the rationale behind [[Lakehouse|data lakehouse]] architectures (Spark/Presto running on storage nodes) and [[DataMesh|data mesh]] (decentralizing ownership). The rule of thumb: *for petabyte-scale data, code moves to data; for gigabyte-scale data, data moves to code.*

Data gravity pairs with [[InformationEntropy|information entropy]] (signal density) to define **Data Selection Gain ∝ Entropy / Gravity**: effective data engineering maximizes information per byte moved. A petabyte cloud migration is therefore "not just a bandwidth problem" — the wire cost is dwarfed by pipeline re-engineering, re-validation, schema migration, and downstream feature-store updates (months of human time vs weeks of wire time).

## Connections

- [[IronLawOfMLSystems]] — the $D_{\text{vol}}/\text{BW}$ term data gravity quantifies.
- [[InformationEntropy]] — the numerator of Data Selection Gain.
- [[Lakehouse]] / [[DataMesh]] — architectural responses to data gravity.
- [[TieredStorage]] / [[StorageArchitecture]] — where gravity shapes storage decisions.
- [[MapReduce]] — the compute-follows-data scheduling primitive.
- [[mlsysbook-ch16-conclusion]] — the conclusion makes data gravity invariant #2 of the [[ThirteenQuantitativeInvariants|thirteen]] ($C_{move}(D_{vol})\gg C_{move}(\text{Compute})$, "move compute to data"); [[DLRM]] is "data gravity embodied" (terabyte embedding tables force the architecture around where data resides), and it underpins the "more data always helps" fallacy (larger datasets cascade I/O, preprocessing, and feature-store costs).
- [[mlsysbook-ch04-data-engineering]] — source.
