---
title: "Snowdoop"
type: concept
tags: [r-package, parallel-computing, mapreduce, distributed-computing]
sources: [parproc-ch09-mapreduce-computation]
last_updated: 2026-05-17
---

# Snowdoop

A lightweight, pure-R approach to [[MapReduce]]-style distributed computation introduced by [[NormMatloff]] of [[UCDavis]] as an alternative to [[Hadoop]] and Spark. Not a package per se but a general approach: manually chunk the input data into distributed mini-files (one per worker node), then use [[Snow]]'s `clusterCall` to run a worker function on each chunk, and combine results with standard R's `Reduce`.

Utility functions are included in Matloff's **partools** R package:

- `setclsinfo(cls)` — assigns each cluster node an ID and related metadata.
- `filechunkname(basename, ndigs, nodenum=NULL)` — forms the file name `basename.i` where `i` is this node's ID.
- `addlists(lst1, lst2, add)` — "adds" two lists by applying `add` to elements in common and copying non-null elements from either list.

## Word Count Example

```r
# each node executes this function
wordcensus <- function(basename, ndigs) {
  fname <- filechunkname(basename, ndigs)
  words <- scan(fname, what="")
  tapply(words, words, length, simplify=FALSE)
}

# manager
fullwordcount <- function(cls, basename, ndigs) {
  setclsinfo(cls)
  counts <- clusterCall(cls, wordcensus, basename, ndigs)
  addlistssum <- function(lst1, lst2) addlists(lst1, lst2, sum)
  Reduce(addlistssum, counts)
}
```

*"All pure R! No Java, no configuration."* (§9.4.1, p. 219).

## K-Means Clustering Example

Snowdoop's k-means iterates: each worker calls `findnrst(xname, ctrs)` to find the nearest centroid for each data point in its chunk (using `pdist` for distances), accumulates per-centroid count and coordinate sum vectors, and sends them to the manager. `Reduce(addlistssum, tmp)` combines across workers; the manager recomputes centroids. Crucially, **data persists in worker memory across iterations** — no disk re-read needed per iteration, unlike Hadoop, and no explicit caching request needed, unlike Spark.

## Trade-offs

| Dimension | Hadoop/Spark | Snowdoop |
|---|---|---|
| Fault tolerance | Yes (HDFS replication) | No |
| Distributed sort | Built-in (shuffle) | Not provided |
| Language | Java/C++ (streaming for others) | Native R |
| Configuration | Java, HDFS, cluster setup | None (pure R) |
| Iterative algorithms | Slow (disk re-read per pass) | Fast (data in worker RAM) |
| Parallel I/O | Yes (HDFS data locality) | Only if chunks on different disks |

## Connections

- [[NormMatloff]] — designer; Snowdoop is his own framework introduced in this chapter.
- [[parproc-ch09-mapreduce-computation]] — §9.4 introduces Snowdoop with word-count and k-means examples.
- [[Snow]] — the R parallel package (`clusterCall`, `clusterApply`) that Snowdoop builds on.
- [[MapReduce]] — the paradigm Snowdoop approximates without a sorting phase.
- [[Hadoop]] — the full-featured alternative Snowdoop trades fault tolerance against for simplicity.
- [[WordCount]] — the canonical worked example.
- [[KMeansClustering]] — the second worked example; iterative algorithm that benefits from in-memory persistence.
- [[ScatterGather]] — the underlying pattern (`clusterCall` = scatter; `Reduce` = gather).
