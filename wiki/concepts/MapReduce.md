---
title: "MapReduce"
type: concept
tags: [parallel-computing, paradigm, distributed-systems, scatter-gather]
sources: [parproc-ch01-intro-parallel-processing, parproc-ch09-mapreduce-computation]
last_updated: 2026-05-17
---

# MapReduce

Programming paradigm for distributed batch processing on large, physically distributed datasets. Introduced by Google; [[Hadoop]] is the canonical open-source implementation. MapReduce is a specialization of the [[ScatterGather]] pattern with a sorting step inserted between the map and reduce phases.

## Three Phases

- **Map phase.** Multiple parallel *mapper* processes, each handling one chunk of the input. For each input record (line), the mapper emits one or more `(key, value)` pairs. In the streaming interface, the format is `key \t data` (tab-separated text). Mappers run concurrently across the [[Cluster]].
- **Shuffle/sort phase.** All mapper output lines sharing the same key are gathered together and sorted. This phase is handled by the framework (Hadoop's *shuffler*). A *combiner* may pre-aggregate a mapper's output before the network hop, reducing traffic when the reduce operation is associative and commutative.
- **Reduce phase.** Multiple parallel *reducer* processes, each working on one set of keys. For a given key, all mapper output lines with that key arrive at the same reducer, presorted. The reducer aggregates them and emits the final output to a file in the [[HDFS]].

## JobTracker / TaskTracker Terminology (Hadoop classic)

In Hadoop 1.x, a **JobTracker** (master daemon) accepts job submissions, splits input, schedules map and reduce tasks, monitors progress, and re-executes failed tasks. **TaskTracker** daemons run on each worker node, launch the actual map/reduce JVM processes, and report heartbeats to the JobTracker. (Hadoop 2.x / YARN replaces JobTracker with ResourceManager + ApplicationMaster, but the logical roles are the same.)

## HDFS Role

Input is read from a file in the [[HDFS]]; final output is written back to HDFS, one file chunk per reducer (`part-00000`, `part-00001`, ...). Intermediate mapper-to-shuffler traffic uses the native OS file system on each node. HDFS stores each block on at least 3 disks for fault tolerance; data locality is exploited by scheduling map tasks on the same node that holds their input block — *"Moving computation is cheaper than moving data."*

## Streaming Protocol

[[HadoopStreaming]] makes Hadoop language-agnostic: mappers and reducers are arbitrary executables that read from **stdin** and write to **stdout** in `key \t data` text format. This enables R, Python, or shell scripts as mapper/reducer code, at the cost of string-to-number conversion overhead.

## Locality Scheduling

Because HDFS distributes file blocks across the cluster, Hadoop schedules each map task preferentially on the node holding that block. This avoids shipping input data over the network — the dominant cost for large datasets. The principle generalises: it is cheaper to move the computation (a small program) than to move the data (potentially terabytes).

## Limitations and Alternatives

- **Iterative algorithms.** Hadoop cannot retain intermediate results in memory between runs; each pass re-reads from disk. Spark addresses this with in-memory RDDs and explicit caching.
- **Configuration overhead.** Hadoop requires Java, HDFS setup, and cluster configuration. Alternatives like [[Snowdoop]] trade fault tolerance and sorting for simplicity (pure R, no infrastructure).
- **Sorting cost.** The shuffle/sort phase is always performed. Applications that do not need a distributed sort pay this cost unnecessarily.

## Connections

- [[parproc-ch01-intro-parallel-processing]] — Ch1 introduced MapReduce as a scatter/gather instance: *"Hadoop/MapReduce Computing is basically a scatter/gather operation."*
- [[parproc-ch09-mapreduce-computation]] — Ch9 is the dedicated MapReduce chapter; provides the full map/shuffle/reduce breakdown, the Hadoop streaming word-count example, and the Snowdoop alternative.
- [[Hadoop]] — the canonical open-source MapReduce implementation.
- [[HDFS]] — Hadoop's distributed file system; used for input and output.
- [[HadoopStreaming]] — language-agnostic stdin/stdout interface to Hadoop.
- [[WordCount]] — the canonical MapReduce example.
- [[Snowdoop]] — Matloff's lightweight R-based MapReduce alternative.
- [[ScatterGather]] — the underlying paradigm; MapReduce adds sorting.
- [[Cluster]] — typical execution substrate.
- [[MPIScatter]] — the low-level MPI primitive underlying the scatter phase.
- [[MPIGather]] — the low-level MPI primitive underlying the gather/reduce phase.
