---
title: "ParProcBook Ch14: Parallel Computation in Statistics/Data Mining"
type: source
tags: [textbook, parallel-computing, data-mining, statistics, machine-learning]
date: 2026-05-17
source_file: raw/parproc-matloff.pdf
---

# ParProcBook Ch14: Parallel Computation in Statistics/Data Mining

Chapter 14 (book pp. 291–304, PDF pp. 311–324) of *Programming on Parallel Machines: GPU, Multicore, Clusters and More* by [[NormMatloff]] of [[UCDavis]]. The chapter surveys five statistical/data-mining workloads — itemset analysis, probability density estimation, clustering, PCA, and Monte Carlo simulation — and explains how each maps to parallel execution, primarily via [[Snow]], [[OpenMP]], and [[CUDA]].

## Summary

The chapter opens by framing the rise of "data mining" as classical statistics at scale: datasets of tens of millions of observations with thousands of variables demand parallel computation. §14.1 covers itemset analysis, introducing the [[MarketBasketProblem]] as the motivating example, defining association rules with support and confidence thresholds, and presenting the [[AprioriAlgorithm]] as a breadth-first search that prunes infrequent itemsets; the inner loops are embarrassingly parallel but coordination costs grow as refinements accumulate. §14.2 treats [[KernelDensityEstimation]]: the histogram is a crude density estimate; kernel-based estimation weights nearby samples via a kernel function (typically Gaussian) to produce a smooth density curve; parallelization distributes t-values across workers or exploits the convolution structure to reduce to parallel FFT (Ch13). §14.2.2 covers [[Histogram]] computation for images in CUDA, detailing Podlozhnyuk's histogram64/histogram256 algorithm for managing shared-memory bank conflicts. §14.3 revisits [[KMeansClustering]], providing the complete [[Snow]] parallel implementation (distance computation + centroid aggregation via `clusterCall` + `Reduce`). §14.4 covers [[PrincipalComponentAnalysis]]: correlated variables lie near a lower-dimensional subspace; PCA extracts the r leading eigenvectors of a covariance matrix, reducing p variables to r < p; parallelization reuses Ch11 eigenvector methods. §14.5 treats [[MonteCarloSimulation]]: embarrassingly parallel by design but requires independent random number streams per thread — naive use of `random()` gives correlated or identical streams; the chapter surveys parallel RNG libraries (CURAND, RngStream, SPRNG, OpenMP Mersenne Twister).

## Key Claims

- **Data mining is statistics at scale.** The shift from "statistics" to "data mining" is a matter of scale — datasets easily reach tens of millions of observations and thousands of variables, making parallel methods necessary. The overfitting risk grows with variable count and is under-acknowledged. (§14.1.1, p. 291)

- **The Apriori algorithm is a breadth-first itemset search with monotone pruning.** Starting from frequent 1-itemsets, it generates candidate (i+1)-itemsets from size-i frequent itemsets and prunes any candidate whose support falls below the threshold. The pruning is valid because support is monotone decreasing under set extension. Both inner `for` loops are embarrassingly parallel in the basic form; synchronization on shared F_i sets is the coordination cost. (§14.1.3–14.1.4, pp. 293–294)

- **Parallelizing Apriori becomes harder as refinements accumulate.** The basic loops are embarrassingly parallel. But with refinements (e.g. hash trees for accounting), the storage for F_i and associated data structures may exceed one node's memory in the message-passing case, requiring a manager node and increasing coordination complexity. (§14.1.4, p. 294)

- **Kernel density estimation produces a smooth density curve by weighting data points near the evaluation target.** The estimator is f̂(t) = (1/nh) Σ k((t − Xᵢ)/h), where k is a kernel (typically Gaussian) and h is the bandwidth (analogous to histogram bin width). Parallelization: distribute blocks of t-values across workers, or recognize that the estimator has convolution form and reduce to parallel FFT (Ch13). (§14.2.1, pp. 295–297)

- **Histogram computation for images is embarrassingly parallel but CUDA-hard.** The outer intensity loop is trivially parallel; in CUDA, individual pixels can be assigned to individual threads. The bottleneck is shared-memory bank conflicts when accumulating subhistograms. Podlozhnyuk's histogram64 uses per-thread subhistograms (64 intensity levels, 6-bit granularity, 1 byte per count, 192 threads/block for 85 bytes/thread); histogram256 switches to per-warp subhistograms (256 levels, 4 bytes per count) to handle the full 8-bit data. (§14.2.2, pp. 298–299)

- **K-means clustering is embarrassingly parallel in distance computation.** The core per-iteration work — assigning each point to its nearest centroid — is independent across points. The [[Snow]] implementation distributes data chunks to workers via `clusterCall(cls, findnewgrps, centers)`, each worker returns per-group sums and counts, and the manager `Reduce`s them with `"+"` to recompute centroids. Empty groups are set to center 0. (§14.3.1, pp. 300–302)

- **PCA parallelization reduces to parallel eigenvector computation.** PCA finds the r < p eigenvectors corresponding to the r largest eigenvalues of the p×p covariance matrix. This is a matrix problem; parallel eigenvector algorithms from §11.6 apply directly. (§14.4, p. 303)

- **Monte Carlo simulation requires independent parallel random number streams.** The simulation loop is embarrassingly parallel, but using C's `random()` naively gives identical or correlated streams across threads. Purpose-built parallel RNG libraries are required: CURAND (CUDA SDK), RngStream (OpenMP/MPI), SPRNG (MPI-oriented), OpenMP Mersenne Twister. (§14.5, pp. 303–304)

## Key Quotes

> *"How did the word statistics get supplanted by data mining? In a word, it is a matter of scale."* — p. 291. Chapter motivation.

> *"The key point in the latter operation is that if an itemset is not frequent, i.e. has support less than the threshold, then adding further items to it will make it even less frequent."* — p. 293. Apriori pruning principle.

> *"Parallelizing the market basket problem can be very challenging. The interested reader is referred to the considerable literature which has developed on this topic."* — p. 294. Honest scope limitation.

> *"In other words, this reduces the problem to that of parallelizing Fourier transforms — something we know how to do, from Chapter 13."* — p. 297. KDE-as-convolution connecting Ch14 to Ch13.

> *"Note carefully that there is no 'correct' answer here. This is merely an exploratory data analysis tool."* — p. 300. Epistemics of clustering.

> *"A naive approach, say by calling random() in the C library, will not achieve such independence. With some random number libraries, in fact, you'll get the same stream for each thread."* — p. 303. Parallel RNG hazard.

## Connections

- [[NormMatloff]] — author.
- [[UCDavis]] — author's institution.
- [[AprioriAlgorithm]] — §14.1.3–14.1.4; new concept page; breadth-first frequent-itemset search with support-based pruning.
- [[MarketBasketProblem]] — §14.1.2; new concept page; retail transaction association rule mining.
- [[ItemsetAnalysis]] — §14.1; new concept page; general framework for finding frequent item co-occurrences.
- [[KernelDensityEstimation]] — §14.2.1; new concept page; smooth nonparametric density estimation via kernel-weighted sums.
- [[Histogram]] — §14.2.2; new concept page; discrete frequency table; CUDA histogram computation (Podlozhnyuk algorithm).
- [[KMeansClustering]] — §14.3.1; extended; full Snow parallel implementation added.
- [[PrincipalComponentAnalysis]] — §14.4; extended; parallel eigenvector approach noted.
- [[MonteCarloSimulation]] — §14.5; new concept page; parallel simulation requiring independent RNG streams.
- [[ProbabilityDensityFunction]] — §14.2; density estimation is the statistical task of recovering this function from samples.
- [[Snow]] — §14.3.1; used for parallel k-means via `clusterCall` + `Reduce`.
- [[OpenMP]] — §14.2.2 (histogram row parallelism), §14.5 (Mersenne Twister, RngStream).
- [[CUDA]] — §14.2.2 (Podlozhnyuk histogram64/256 CUDA algorithm), §14.5 (CURAND).
- [[FastFourierTransform]] — §14.2.1; KDE has convolution form; parallelization reduces to parallel FFT from Ch13.
- [[parproc-ch13-audio-image-processing]] — §14.2.1 explicitly references Ch13 for the FFT-based KDE parallelization.
- [[parproc-ch11-parallel-matrix-operations]] — §14.4 references §11.6 parallel eigenvector algorithms for PCA.
- [[parproc-ch09-mapreduce-computation]] — §14.3 Snow k-means extends the framework introduced in Ch9.

## Contradictions

- **No contradiction with [[KMeansClustering]].** Ch9 (Snowdoop, `findnrst` + `pdist` + `tapply`) and Ch14 (Snow, `findnewgrps` + explicit distance matrix + `Reduce`) present two distinct Snow-based parallel implementations. The Ch14 version uses Manhattan distance (sum of absolute differences) rather than Euclidean; both are valid. The ch14 implementation is *not* the same code as ch9 — readers should treat them as independent worked examples over the same algorithm.
- **Overfitting warning unusual for a parallel computing textbook.** §14.1.1 flags the overfitting problem in data mining ("Major, Major Warning") more prominently than most parallel-computing texts, which focus purely on computational structure. This is a pedagogical choice, not a technical contradiction.
