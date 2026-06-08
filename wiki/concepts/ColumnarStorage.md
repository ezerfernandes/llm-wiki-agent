---
title: "Columnar Storage"
type: concept
tags: [ml-systems, mlsysbook, data-engineering, storage, format, io]
sources: [mlsysbook-ch04-data-engineering]
last_updated: 2026-06-05
---

# Columnar Storage

Organizing data by column rather than by row, so a reader loads only the specific columns a computation needs (Reddi, [[mlsysbook-ch04-data-engineering|Vol 1, Ch 4]]). [[Parquet]] and ORC are the canonical formats; warehouses like BigQuery, Redshift, and Snowflake use columnar layouts internally.

Columnar storage delivers **5–10× I/O reduction** for typical ML workloads via two mechanisms: reading only required columns (a fraud model using 20 of 100 columns achieves 80% I/O reduction before compression), and column-level compression that exploits within-column value patterns (a 200-value country code compresses 20–50× via dictionary encoding; sorted columns compress via run-length encoding). Combined, 20–100× total I/O reduction. Framed as **format efficiency**: Effective Bandwidth = Physical Bandwidth × η_format, so switching CSV→Parquet "is mathematically equivalent to buying a 5× faster hard drive." This is a direct consequence of [[DataGravity|data gravity]] — when data is too massive to move, minimize bytes read per training step.

## Connections

- [[Parquet]] — the canonical columnar format.
- [[Snappy]] — the fast-decompression codec often paired with it.
- [[DataGravity]] — the constraint columnar storage answers.
- [[StorageArchitecture]] / [[DataWarehouse]] — where columnar layouts live.
- [[mlsysbook-ch04-data-engineering]] — source.
