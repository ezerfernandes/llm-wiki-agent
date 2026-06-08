---
title: "All-to-All Communication"
type: concept
tags: [distributed-systems, hardware, recommendation, dlrm, systems, mlsysbook]
sources: [mlsysbook-ch06-network-architectures]
last_updated: 2026-06-05
---

# All-to-All Communication

A collective communication pattern in which **every device must exchange data with every other device**. In [[mlsysbook-ch06-network-architectures]] (Reddi, *Machine Learning Systems* Vol 1, Ch 6) it is the dominant bottleneck of [[DLRM]]-style recommendation systems: when [[EmbeddingTable|embedding tables]] are sharded across hundreds of GPUs ([[ModelParallelism|embedding sharding]]), a GPU processing a local batch of users needs embedding vectors that live on many *other* GPUs, forcing a full all-to-all exchange to gather them.

## Why it matters

- **Bisection bandwidth, not FLOP/s, is the limiter.** DLRM performance is bounded by the network switch fabric's capacity to move data between all nodes simultaneously, motivating high-speed interconnects like **NVLink** and **InfiniBand** and specialized embedding caches.
- It is qualitatively different from the broadcast/reduce patterns of dense [[CNN|CNN]]/[[MultilayerPerceptron|MLP]] data parallelism — and is the reason recommendation workloads need *different* hardware optimization than vision or language models.

## Connections

- [[mlsysbook-ch06-network-architectures]] — identifies all-to-all as the DLRM communication bottleneck.
- [[DLRM]] / [[EmbeddingTable]] — the workload that induces the pattern.
- [[ModelParallelism]] — embedding sharding is what makes the exchange necessary.
- [[MemoryBound]] — the embedding gathers themselves are memory-bandwidth-bound; the network exchange is the scale-out bottleneck.
