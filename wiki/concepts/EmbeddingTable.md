---
title: "Embedding Table"
type: concept
tags: [deep-learning, recommendation, dlrm, systems, memory, mlsysbook]
sources: [mlsysbook-ch06-network-architectures]
last_updated: 2026-06-05
---

# Embedding Table

A large lookup table mapping each value of a **high-cardinality categorical feature** (user ID, item ID, video ID) to a dense [[Embedding|embedding]] vector. Embedding tables are the defining component of [[DLRM]] and recommendation systems, and the reason those workloads are **memory-capacity-bound** rather than compute- or bandwidth-bound. Detailed in [[mlsysbook-ch06-network-architectures]] (Reddi, *Machine Learning Systems* Vol 1, Ch 6).

## Why it matters (systems view)

- **Capacity wall.** A table for 1 billion users × 128-dim FP32 vectors ≈ **512 GB** ($10^9 \times 128 \times 4$ bytes); industrial RecSys tables reach terabytes to petabytes — far beyond a single GPU (e.g. a 100M-item × 128-dim table ≈ 51 GB already consumes ~60% of an 80 GB A100).
- **Memory-light compute.** Each lookup is an *index-based memory copy* (a gather) with no arithmetic — distinct from compute-heavy [[CNN|CNNs]]/[[Transformer|transformers]].
- **Random access defeats caching.** Each training sample touches a different set of rows, so the access pattern is effectively random, defeating the prefetching/caching that benefits dense architectures.
- **Forces distributed memory.** Tables are sharded across many GPUs ([[ModelParallelism]] / embedding sharding) while dense MLPs are replicated; gathering the needed rows induces an [[AllToAllCommunication|all-to-all]] exchange limited by bisection bandwidth (NVLink/InfiniBand).

## Connections

- [[mlsysbook-ch06-network-architectures]] — analyzes embedding tables as the capacity-bound bottleneck of RecSys.
- [[DLRM]] — the recommendation Lighthouse Model built around dense MLPs + sparse embedding tables.
- [[Embedding]] — the dense vectors stored in the table (word2vec origin).
- [[ModelParallelism]] / [[AllToAllCommunication]] — how sharded tables are gathered at scale.
- [[MemoryBound]] — embedding lookups are memory-bandwidth-bound at the operation level; the table size is the capacity constraint.
