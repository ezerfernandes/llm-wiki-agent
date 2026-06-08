---
title: "Data Lake"
type: concept
tags: [data, storage, infrastructure]
sources: [mlsysbook-ch04-data-engineering]
last_updated: 2026-06-05
---

# Data Lake

A storage architecture (typically object storage like S3) that holds raw, semi-structured, and structured data without enforcing schema-on-write. Contrast with [[DataWarehouse]] (schema-on-write) and the hybrid [[Lakehouse|lakehouse]] pattern; common substrate for [[DataPipeline]] and ML feature backfills.

Reddi's *Machine Learning Systems* ([[mlsysbook-ch04-data-engineering|Vol 1, Ch 4]]) positions data lakes as the **capacity + schema-on-read** option in the [[StorageArchitecture|storage decision]]: ideal for petabyte-scale unstructured training data (images, audio, text, embeddings) where the schema is unknown at collection time. The risk is governance — without disciplined metadata/cataloging (AWS Glue, Apache Atlas, Databricks Unity Catalog), lakes degrade into "data swamps" (`userdata_v2_final_ACTUALLY_FINAL`).

## Connections

- [[DataWarehouse]] / [[Lakehouse]] — the schema-on-write and hybrid alternatives.
- [[StorageArchitecture]] — the IOPS-vs-throughput decision lakes anchor.
- [[DataGovernance]] — what prevents the data-swamp failure.
- [[mlsysbook-ch04-data-engineering]] — source.
