---
title: "Apache Parquet"
type: concept
tags: [format, columnar, binary, io]
sources: [pydata-accessing-data]
last_updated: 2026-05-15
---

# Apache Parquet

Columnar binary file format with embedded schema and per-column compression. Designed for analytics workloads — only reads the columns and row-groups the query needs. Now the de facto interchange format between data tools (Spark / DuckDB / pandas / Arrow / Polars / BigQuery / Snowflake).

## In pandas
- Reader: `pd.read_parquet(path, columns=[...])` — selective column read is cheap.
- Writer: `df.to_parquet(path, compression="snappy"/"gzip"/"zstd")`.
- Backend: `pyarrow` (preferred) or `fastparquet`.

## Connections
- [[pandas]] — reader/writer.
- [[ArrowProject]] — `pyarrow` is the canonical implementation.
- [[HDF5]] — older columnar / array on-disk format with overlapping use cases (better for arrays; Parquet is better for tables).
