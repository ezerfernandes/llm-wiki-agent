---
title: "HDFS"
type: concept
tags: [distributed-systems, file-system, hadoop, fault-tolerance]
sources: [parproc-ch09-mapreduce-computation]
last_updated: 2026-05-17
---

# HDFS

The **Hadoop Distributed File System** is [[Hadoop]]'s built-in distributed storage layer, built on top of the native OS file system of each cluster node. It stores data in fixed-size blocks distributed across the cluster's disks and replicates each block on at least 3 separate disks for fault tolerance. Very large files are possible, spanning multiple disks/machines.

## Role in MapReduce

In a [[MapReduce]] job:
- **Input** is read from a file in HDFS. Each HDFS block becomes one map task's input, scheduled preferentially on the node that holds the block (*data locality*).
- **Intermediate** mapper-to-shuffler output goes to temporary files on the native OS file system of each node (not HDFS).
- **Final output** is written back to HDFS, one file per reducer: `part-00000`, `part-00001`, etc. A `_SUCCESS` marker file indicates job completion.

The design slogan is *"Moving computation is cheaper than moving data"* — distributing the input data across the cluster and running computation where the data lives avoids large network transfers.

## Fault Tolerance

Each block is replicated on at least 3 disks. If a node fails, Hadoop re-executes its tasks on a node that holds a replica. This replication also allows speculative execution: Hadoop can run a slow "straggler" task on a second node and use whichever finishes first.

## Connections

- [[Hadoop]] — the system HDFS is part of.
- [[MapReduce]] — the computation model that uses HDFS for input and output.
- [[parproc-ch09-mapreduce-computation]] — §9.1 and §9.1.5 describe HDFS architecture and its role in the word-count example.
- [[Cluster]] — the hardware substrate.
- [[NetworkOfWorkstations]] — the commodity-hardware context in which HDFS distributes storage.
