---
title: "K-Means Clustering"
type: concept
tags: [unsupervised, clustering, parallel-computing]
sources: [islr-seventh-printing, parproc-ch09-mapreduce-computation, parproc-ch14-statistics-data-mining]
last_updated: 2026-05-17
---

# K-Means Clustering

Partition $n$ observations into a pre-specified $K$ non-overlapping clusters that minimize within-cluster sum-of-squares. Lloyd's algorithm alternates: assign each point to the nearest centroid; recompute centroids. Local optimum depends on initialization — restart multiple times.

## Parallel Implementation via Snowdoop

[[Snowdoop]] provides a parallel k-means over chunked data files. Each worker calls `findnrst(xname, ctrs)` — which uses `pdist` for distances and `tapply` for per-centroid statistics — via `clusterCall`. The manager `Reduce`s per-worker centroid-count/sum vectors with `addlists`, then recomputes centroids. Each iteration's data persists in worker RAM across iterations, unlike Hadoop (disk re-read per pass) or Spark (requires explicit caching). (§9.4.2, [[parproc-ch09-mapreduce-computation]]).

## Parallel Implementation via Snow (Ch14)

[[parproc-ch14-statistics-data-mining]] §14.3.1 provides a second Snow parallel implementation using Manhattan distance (sum of absolute differences). Each worker receives a chunk of data rows (`mchunk`) and computes `findnewgrps(currctrs)`: for each row, find the nearest center via `dst()`, accumulate per-group coordinate sums and counts into `sumcounts`, and return. The manager calls `clusterCall(cls, findnewgrps, centers)`, then `Reduce("+", sumcounts)` to aggregate, and recomputes centers as `tmp[,1:spacedim] / tmp[,spacedim+1]`. Empty groups are assigned center 0 (`centers[is.nan(centers)] <- 0`). This implementation differs from the Ch9 Snowdoop version (which used `pdist`/Euclidean distance and `tapply`); both are valid parallel k-means but over different distance metrics and frameworks.

## Connections
- [[islr-seventh-printing]] — Ch.10.3.1 (sequential description).
- [[parproc-ch09-mapreduce-computation]] — §9.4.2 Snowdoop parallel implementation (Euclidean distance).
- [[parproc-ch14-statistics-data-mining]] — §14.3.1 Snow parallel implementation (Manhattan distance).
- [[Snowdoop]] — the R framework used in the Ch9 implementation.
- [[Snow]] — R cluster framework used in the Ch14 implementation.
- [[HierarchicalClustering]] — sibling clustering method that needs no pre-specified $K$.
- [[UnsupervisedLearning]] — parent paradigm.
