---
title: "ParProcBook Ch9: MapReduce Computation"
type: source
tags: [textbook, parallel-computing, mapreduce, hadoop, distributed-computing]
date: 2026-05-17
source_file: raw/parproc-matloff.pdf
---

# ParProcBook Ch9: MapReduce Computation

Chapter 9 (book pp. 213–222, PDF pp. 233–242) of *Programming on Parallel Machines: GPU, Multicore, Clusters and More* by [[NormMatloff]] of [[UCDavis]]. The [[MapReduce]] chapter: motivates the paradigm as a scatter/gather-with-sorting specialization suited for physically distributed datasets, walks Apache [[Hadoop]] via a streaming word-count example in R, covers the [[HDFS]] disk-file architecture, briefly surveys alternative systems (Spark), catalogues R interfaces to MapReduce (**rmr**, RHIPE, **sparkr**), and introduces Matloff's own [[Snowdoop]] approach as a lightweight alternative built on [[Snow]] and standard R.

## Summary

§9.1 introduces [[Hadoop]] as the dominant MapReduce implementation, written in Java but accessible from any language via its *streaming* interface (stdin/stdout, tab-separated `key \t data` format); the Hadoop Distributed File System ([[HDFS]]) provides replicated, fault-tolerant distributed storage used for both input and final output. §9.1.2–§9.1.4 walk a complete [[WordCount]] example in R — mapper emits `(word, 1)` pairs, reducer accumulates counts — explaining the role of the *combiner* for network-latency reduction. §9.2 notes Spark as Hadoop's principal challenger (in-memory intermediate results, faster for iterative algorithms). §9.3 lists R-language interfaces (rmr, RHIPE, sparkr). §9.4 proposes [[Snowdoop]] as a simpler alternative: chunk the input files manually, run [[Snow]]'s `clusterCall` on the chunks, and combine with `Reduce` — all in pure R with no Java or configuration overhead. §9.4.2 extends Snowdoop to [[KMeansClustering]] using `clusterCall` + `Reduce` across iterations, with data that persists in worker memory across iterations (unlike Hadoop's mandatory disk reads).

## Key Claims

- **[[MapReduce]] is a scatter/gather pattern with a sorting phase added.** *"MapReduce is really a form of the scatter-gather pattern we've seen frequently in this book, with the added feature of a sorting operation added in the middle."* (§9 intro, p. 213). The three phases are map (parallel per-line transformation), shuffle/sort (grouping by key), and reduce (per-key aggregation).
- **Mapper output format is `key \t data`.** Input to mappers is from an [[HDFS]] file; output from reducers goes back to an [[HDFS]] file, one chunk per reducer. The streaming line format is `key \t data` where `\t` is a tab character. (§9.1.1, p. 214).
- **[[Hadoop]] streaming uses stdin/stdout, enabling use from any language.** *"Hadoop can work with programs in any language under Hadoop's streaming option, by reading from stdin and writing to stdout, in text, line-oriented form in both cases."* (§9.1.1, p. 214). The text-format conversion carries a numeric-performance cost but Hadoop is not designed for maximum efficiency.
- **The [[WordCount]] example is Hadoop's canonical "Hello World."** The mapper reads a line, emits `(word, 1)` pairs via `cat(w, "\t 1\n")`; the reducer accumulates counts from presorted key groups via `count <- count + as.integer(inln[2])`. (§9.1.2, pp. 214–215).
- **Combiners reduce network traffic by pre-aggregating mapper output.** *"The solution is to have each mapper try to coalesce its messages before sending to the shuffler."* (§9.1.4, p. 217). The combiner is often identical to the reducer; it runs on the mapper's own output before the network hop, so a reducer's `inln[2]` count field may arrive as a value greater than 1.
- **[[HDFS]] replicates each block on at least 3 disks for fault tolerance.** *"It is replicated for the sake of reliability, with each HDFS block existing in at least 3 copies, i.e. on at least 3 separate disks."* (§9.1.5, p. 217). Output is stored as part-00000, part-00001, etc.
- **HDFS data locality minimizes communication cost.** *"Note that by having the input and output files in HDFS, we minimize communications costs in shipping the data between nodes of a cluster. The slogan used is 'Moving computation is cheaper than moving data.'"* (§9.1.5, p. 218). All disk I/O carries a runtime cost.
- **Hadoop cannot keep intermediate results in memory between runs.** *"One of the problems is that one cannot keep intermediate results in memory between Hadoop runs. This is a serious problem, for instance, with iterative or even multi-pass algorithms."* (§9.2, p. 218). This is Hadoop's primary limitation for iterative workloads.
- **Spark retains HDFS compatibility and adds in-memory caching.** *"The Spark package now being developed aims to remedy many of Hadoop's shortcomings. Early reports indicate some drastic speed improvements, while retaining the ability to read HDFS files, and continuing to have fault tolerance features."* (§9.2, p. 218).
- **R interfaces to MapReduce include rmr (Revolution Analytics), RHIPE, and sparkr.** (§9.3, p. 218). These exist because of R's widespread use in data analysis.
- **Hadoop's two core features are distributed data access and distributed file sort.** *"What does Hadoop really give us? The two main features are (a) distributed data access and (b) an efficient distributed file sort."* (§9.4, p. 218). Both Spark and Snowdoop address the distributed-data-access goal.
- **[[Snowdoop]] trades fault tolerance for simplicity and R-nativeness.** *"Here is an alternative, a general approach rather than a package, which I call 'Snowdoop': One simply does one's own chunking of files into distributed mini-files, and then uses Snow or some other general R tool on those files."* (§9.4, p. 219). All in pure R — no Java, no configuration.
- **Snowdoop word count uses `clusterCall` + `addlists` + `Reduce`.** The worker function `wordcensus` reads its file chunk and calls `tapply(words, words, length)`; the manager calls `clusterCall(cls, wordcensus, ...)`, then reduces per-worker lists with `addlists` (element-wise sum combining non-null keys). (§9.4.1, pp. 219–220).
- **Snowdoop k-means data persists in worker memory across iterations.** *"The data at each worker persists across iterations. In Hadoop, it would be reread from disk at each iteration, and in Spark, we'd need to request caching, but here it comes for free, no special effort needed."* (§9.4.2, p. 221). Each iteration calls `findnrst` (nearest centroid via `pdist`) via `clusterCall`, then `Reduce`s per-worker centroid statistics with `addlists`.
- **Snowdoop does not achieve full parallel reading if file chunks share a disk.** *"Note that neither Hadoop, Spark nor Snowdoop will achieve full parallel reading if the file chunks are all on the same disk."* (§9.4.2, p. 220, footnote 2). Distributed benefit requires physically distributed storage.
- **Snowdoop lacks fault tolerance.** *"Of course, this approach lacks the fault tolerance feature of Hadoop and Spark can, which can be quite advantageous."* (§9.4.2, p. 220). Appropriate for clusters without hard failure-tolerance requirements.

## Key Quotes

> *"MapReduce is really a form of the scatter-gather pattern we've seen frequently in this book, with the added feature of a sorting operation added in the middle."* — §9 intro, p. 213. The paradigm's positioning.

> *"Hadoop can work with programs in any language under Hadoop's streaming option, by reading from stdin and writing to stdout, in text, line-oriented form in both cases."* — §9.1.1, p. 214. The streaming interface that makes R mappers/reducers possible.

> *"Note that by having the input and output files in HDFS, we minimize communications costs in shipping the data between nodes of a cluster. The slogan used is 'Moving computation is cheaper than moving data.'"* — §9.1.5, p. 218. The data-locality design philosophy.

> *"One cannot keep intermediate results in memory between Hadoop runs. This is a serious problem, for instance, with iterative or even multi-pass algorithms."* — §9.2, p. 218. Hadoop's core limitation for iterative computation.

> *"Here is an alternative, a general approach rather than a package, which I call 'Snowdoop': One simply does one's own chunking of files into distributed mini-files, and then uses Snow or some other general R tool on those files."* — §9.4, p. 219. The Snowdoop thesis.

> *"All pure R! No Java, no configuration."* — §9.4.1, p. 219. The value proposition of Snowdoop vs Spark/Hadoop.

> *"The data at each worker persists across iterations. In Hadoop, it would be reread from disk at each iteration, and in Spark, we'd need to request caching, but here it comes for free, no special effort needed."* — §9.4.2, p. 221. Snowdoop's free in-memory persistence advantage for iterative algorithms.

## Connections

- [[NormMatloff]] — author; Snowdoop is his own framework.
- [[UCDavis]] — author's institution.
- [[parproc-ch01-intro-parallel-processing]] — Ch1 introduced MapReduce / Snow / scatter/gather. Ch9 is the dedicated MapReduce chapter Ch1 forward-referenced.
- [[parproc-ch07-message-passing-systems]] — Ch7 framed scatter/gather as a higher-level paradigm bridging MPI / Snow / MapReduce; Ch9 operationalizes the MapReduce side.
- [[parproc-ch08-introduction-to-mpi]] — Ch8's `MPI_Scatter` / `MPI_Gather` are the low-level primitives underlying the MapReduce scatter/gather pattern described in Ch9.
- [[MapReduce]] — chapter subject; expanded from stub to full reference.
- [[Hadoop]] — primary MapReduce implementation covered in §9.1.
- [[HDFS]] — Hadoop's distributed file system; stores input, intermediate, and final output.
- [[HadoopStreaming]] — the stdin/stdout interface enabling non-Java programs to act as mappers/reducers.
- [[WordCount]] — the canonical MapReduce "Hello World" example, implemented in R.
- [[Snowdoop]] — Matloff's lightweight R-based MapReduce alternative introduced in §9.4.
- [[KMeansClustering]] — second Snowdoop worked example (§9.4.2); expanded with Snowdoop parallel implementation notes.
- [[Snow]] — the R parallel package Snowdoop builds on (`clusterCall` / `clusterApply`).
- [[ScatterGather]] — the underlying paradigm; MapReduce adds sorting in the middle.
- [[Cluster]] — the execution substrate.
- [[NetworkOfWorkstations]] — the hardware context for HDFS data locality.

## Contradictions

- **No outright contradictions with prior wiki content.** Ch9 extends the MapReduce / Snow / scatter/gather thread established in Ch1 and Ch7, and is consistent with the [[KMeansClustering]] description from the ISLR corpus.
- **Snowdoop vs Spark framing is as of ~2014.** The chapter notes "as of late 2014" for Spark concerns and the Snowdoop introduction. Current state of these systems may differ; the wiki entries for [[Hadoop]] and Snowdoop are grounded in the textbook's historical perspective.
