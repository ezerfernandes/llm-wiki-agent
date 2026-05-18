---
title: "Hadoop"
type: entity
tags: [software, distributed-computing, mapreduce, apache, java]
sources: [parproc-ch09-mapreduce-computation]
last_updated: 2026-05-17
---

# Hadoop

Apache Hadoop is the dominant open-source [[MapReduce]] framework. Written in Java; most efficiently used from Java or C++, but its *streaming* interface ([[HadoopStreaming]]) enables programs in any language (R, Python, shell) to serve as mappers and reducers by reading from **stdin** and writing to **stdout** in tab-separated text format.

Hadoop bundles its own distributed file system ([[HDFS]]), which replicates each data block across at least three disks for fault tolerance, stores data across the cluster for locality scheduling, and writes final output as numbered part files (`part-00000`, `part-00001`, ...). The primary execution model is the [[MapReduce]] paradigm: map tasks run in parallel on input chunks, a shuffle/sort phase groups output by key, and reduce tasks aggregate per-key results.

## Key Limitations (as of ~2014)

- Intermediate results cannot be kept in memory between Hadoop runs — every pass re-reads from disk. This makes iterative algorithms such as [[KMeansClustering]] significantly slower than in-memory frameworks.
- Requires Java, HDFS infrastructure setup, and careful cluster configuration. R users in particular must bridge via [[HadoopStreaming]] or wrapper packages (rmr, RHIPE).
- Always performs a distributed sort (shuffle phase), even when the application does not require sorted keys.

## Connections

- [[MapReduce]] — the paradigm Hadoop implements.
- [[HDFS]] — Hadoop's distributed file system.
- [[HadoopStreaming]] — language-agnostic stdin/stdout interface.
- [[WordCount]] — the canonical Hadoop "Hello World" example.
- [[parproc-ch09-mapreduce-computation]] — Ch9 introduces Hadoop with an R streaming word-count example.
- [[ApacheSpark]] — successor system that adds in-memory intermediate storage, faster for iterative algorithms.
- [[Snowdoop]] — Matloff's lightweight R alternative that avoids Hadoop's configuration overhead.
- [[Cluster]] — the hardware substrate.
