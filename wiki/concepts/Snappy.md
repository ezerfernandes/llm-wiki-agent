---
title: "Snappy"
type: concept
tags: [ml-systems, mlsysbook, data-engineering, compression, format]
sources: [mlsysbook-ch04-data-engineering]
last_updated: 2026-06-05
---

# Snappy

A fast compression codec optimized for decompression speed over compression ratio (Reddi, [[mlsysbook-ch04-data-engineering|Vol 1, Ch 4]]). Snappy achieves only 2–3× compression but decompresses at ~500 MB/s — roughly 4× faster than gzip's ~120 MB/s (gzip reaches 6–8× compression).

For ML training, where throughput matters more than storage cost, Snappy's speed advantage usually wins. Decompressing a 100 GB dataset takes ~3.3 minutes with gzip vs ~3.3 GB-worth less with Snappy; over 50 epochs that difference compounds to ~7 hours — "potentially the difference between running experiments overnight vs waiting multiple days." Faster decompression also enables higher input throughput, less buffering, and better GPU utilization. Commonly the default codec for [[Parquet]] in ML pipelines.

## Connections

- [[Parquet]] / [[ColumnarStorage]] — the formats Snappy compresses.
- [[DataLoaderChokePoint]] — decompression speed feeds the GPU.
- [[mlsysbook-ch04-data-engineering]] — source.
