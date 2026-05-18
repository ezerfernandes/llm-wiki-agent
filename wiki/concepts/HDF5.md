---
title: "HDF5"
type: concept
tags: [format, binary, io, scientific-computing]
sources: [pydata-accessing-data, pydata-advanced-numpy]
last_updated: 2026-05-15
---

# HDF5

Hierarchical Data Format v5 — a binary container holding a tree of *datasets* (typed multidimensional arrays) and *groups* (folders). Self-describing schema, per-dataset chunking + compression, and partial / random IO of large arrays. Long-time scientific-computing standard (NASA, neuroscience, climate, NIST).

## In Python
- `h5py` — low-level NumPy-like interface to HDF5.
- `PyTables` — higher-level, supports compressed table-like queryable storage.
- pandas — `pd.HDFStore`, `df.to_hdf(path, key=, format="table"/"fixed")`, `pd.read_hdf`. `format="table"` supports `where=` query expressions on the disk file.

## When to choose HDF5 vs [[Parquet]]
- **HDF5**: multidimensional scientific arrays; random partial read of large arrays; in-process workflow.
- **Parquet**: row-oriented tabular data; interchange across tools; query engines (Spark / DuckDB).

## Connections
- [[NumPy]] — typical underlying array dtype.
- [[pandas]] — `HDFStore`.
- [[Parquet]] — sibling columnar format.
