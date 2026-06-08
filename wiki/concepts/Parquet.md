---
title: "Apache Parquet"
type: concept
tags: [format, columnar, binary, io]
sources: [pydata-accessing-data, mlsysbook-ch04-data-engineering]
last_updated: 2026-06-05
---

# Apache Parquet

Columnar binary file format with embedded schema and per-column compression. Designed for analytics workloads — only reads the columns and row-groups the query needs. Now the de facto interchange format between data tools (Spark / DuckDB / pandas / Arrow / Polars / BigQuery / Snowflake).

## In pandas
- Reader: `pd.read_parquet(path, columns=[...])` — selective column read is cheap.
- Writer: `df.to_parquet(path, compression="snappy"/"gzip"/"zstd")`.
- Backend: `pyarrow` (preferred) or `fastparquet`.

## In ML systems

Reddi's *Machine Learning Systems* ([[mlsysbook-ch04-data-engineering|Vol 1, Ch 4]]) frames format choice as a **direct consequence of [[DataGravity|data gravity]]**: Effective Bandwidth = Physical Bandwidth × η_format. Reading 20 of 100 columns gives Parquet η≈1.0 vs CSV's η=0.2 (wastes 80%) — "switching from CSV to Parquet is mathematically equivalent to buying a 5× faster hard drive." Paired with [[Snappy]] compression it feeds accelerators fast enough to avoid the [[DataLoaderChokePoint|dataloader choke point]]; JSON/CSV decode can be 10× slower, idling an H100.

## Connections
- [[pandas]] — reader/writer.
- [[ArrowProject]] — `pyarrow` is the canonical implementation.
- [[HDF5]] — older columnar / array on-disk format with overlapping use cases (better for arrays; Parquet is better for tables).
- [[ColumnarStorage]] / [[Snappy]] — the columnar paradigm and fast codec.
- [[DataGravity]] / [[DataLoaderChokePoint]] — why format efficiency matters for ML training throughput.
- [[mlsysbook-ch04-data-engineering]] — source.
