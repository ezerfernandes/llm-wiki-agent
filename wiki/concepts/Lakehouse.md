---
title: "Data Lakehouse"
type: concept
tags: [ml-systems, mlsysbook, data-engineering, storage, architecture]
sources: [mlsysbook-ch04-data-engineering]
last_updated: 2026-06-05
---

# Data Lakehouse

A storage architecture that combines [[DataLake|data lake]] storage (cheap, schema-less) with [[DataWarehouse|warehouse]] query semantics (ACID transactions, schema enforcement) using open table formats like Delta Lake and Apache Iceberg (Reddi, [[mlsysbook-ch04-data-engineering|Vol 1, Ch 4]]; Zaharia et al. 2021).

For ML workloads the lakehouse is **a direct response to [[DataGravity|data gravity]]**: it eliminates the [[ETL]] copy between lake and warehouse, enabling feature computation directly on the storage layer where data already resides. Moving petabytes to a separate warehouse would double the $D_{\text{vol}}/\text{BW}$ cost; the lakehouse keeps processing engines (Spark, Presto) co-located with storage. It is cited alongside [[DataMesh|data mesh]] as one of the two architectural patterns motivated by the engineering cost of moving petabyte datasets.

## Connections

- [[DataGravity]] — the constraint the lakehouse answers.
- [[DataLake]] / [[DataWarehouse]] — the two patterns it fuses.
- [[DataMesh]] — the organizational alternative response.
- [[StorageArchitecture]] — the broader decision space.
- [[mlsysbook-ch04-data-engineering]] — source.
