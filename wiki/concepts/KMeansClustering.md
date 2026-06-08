---
title: "K-Means Clustering"
type: concept
tags: [unsupervised, clustering, parallel-computing]
sources: [islr-seventh-printing, parproc-ch09-mapreduce-computation, parproc-ch14-statistics-data-mining, hands-on-llm-ch05-text-clustering-topic-modeling, mml-ch11-density-estimation-gmm]
last_updated: 2026-06-05
---

# K-Means Clustering

Partition $n$ observations into a pre-specified $K$ non-overlapping clusters that minimize within-cluster sum-of-squares. Lloyd's algorithm alternates: assign each point to the nearest centroid; recompute centroids. Local optimum depends on initialization — restart multiple times.

## Parallel Implementation via Snowdoop

[[Snowdoop]] provides a parallel k-means over chunked data files. Each worker calls `findnrst(xname, ctrs)` — which uses `pdist` for distances and `tapply` for per-centroid statistics — via `clusterCall`. The manager `Reduce`s per-worker centroid-count/sum vectors with `addlists`, then recomputes centroids. Each iteration's data persists in worker RAM across iterations, unlike Hadoop (disk re-read per pass) or Spark (requires explicit caching). (§9.4.2, [[parproc-ch09-mapreduce-computation]]).

## Parallel Implementation via Snow (Ch14)

[[parproc-ch14-statistics-data-mining]] §14.3.1 provides a second Snow parallel implementation using Manhattan distance (sum of absolute differences). Each worker receives a chunk of data rows (`mchunk`) and computes `findnewgrps(currctrs)`: for each row, find the nearest center via `dst()`, accumulate per-group coordinate sums and counts into `sumcounts`, and return. The manager calls `clusterCall(cls, findnewgrps, centers)`, then `Reduce("+", sumcounts)` to aggregate, and recomputes centers as `tmp[,1:spacedim] / tmp[,spacedim+1]`. Empty groups are assigned center 0 (`centers[is.nan(centers)] <- 0`). This implementation differs from the Ch9 Snowdoop version (which used `pdist`/Euclidean distance and `tapply`); both are valid parallel k-means but over different distance metrics and frameworks.

## From [[hands-on-llm-ch05-text-clustering-topic-modeling|*Hands-On LLMs* Ch 5]]

Ch 5 contrasts k-means with [[HDBSCAN]] as the **centroid-based** vs **density-based** clustering alternatives in [[BERTopic]]'s modular pipeline:

| | k-means | [[HDBSCAN]] |
|---|---|---|
| Requires `K` (# clusters) | Yes | No |
| Forces every point into a cluster | Yes | **No** — outliers labeled `-1` |
| Cluster shape | Convex / spherical | Arbitrary density-based |
| Handles noise | Poorly | **Designed for it** |

Ch 5 chooses HDBSCAN because (a) the number of NLP-research subfields in 44,949 arXiv abstracts is unknown in advance, and (b) niche papers should be marked as outliers, not forced into clusters. **But** Ch 5 also notes that k-means is a valid swap-in for the BERTopic pipeline when outliers are undesired: *"to eliminate outliers, swap HDBSCAN for k-means."* This makes k-means the standard fallback clustering primitive even in BERTopic's modern stack.

## From [[mml-ch11-density-estimation-gmm|MML Ch 11]] (k-means as the hard-assignment GMM)

[[mml-ch11-density-estimation-gmm|MML §11.5]] (p. 368) places $K$-means as the **hard-assignment special case of a [[GaussianMixtureModel|GMM]]**: "$K$-means also uses the EM algorithm to assign data points to clusters. If we treat the means in the GMM as cluster centers and ignore the covariances (or set them to $\mathbf I$), we arrive at $K$-means." The canonical framing it quotes (MacKay 2003): "$K$-means makes a 'hard' assignment of data points to cluster centers $\boldsymbol\mu_k$, whereas a GMM makes a 'soft' assignment via the [[Responsibility|responsibilities]]." In other words, $K$-means is GMM-[[EMAlgorithm|EM]] with the responsibilities forced to be one-hot ($r_{nk}\in\{0,1\}$, each point assigned to its nearest/most-likely center) and isotropic equal covariance — the GMM's E-step soft posterior collapsed to a single argmax. The full GMM is strictly more expressive: ellipsoidal clusters of varying size and orientation, and probabilistic (soft) membership for points in cluster overlaps (MML Fig. 11.10(b) shows boundary points with responsibilities $\approx0.5$).

## Connections
- [[mml-ch11-density-estimation-gmm]] — §11.5, k-means as the hard-assignment GMM (the soft-vs-hard framing).
- [[GaussianMixtureModel]] — the soft-assignment generalization (covariances + responsibilities).
- [[EMAlgorithm]] — both k-means and the GMM are EM instances.
- [[Responsibility]] — the soft assignment k-means hardens to one-hot.
- [[islr-seventh-printing]] — Ch.10.3.1 (sequential description).
- [[parproc-ch09-mapreduce-computation]] — §9.4.2 Snowdoop parallel implementation (Euclidean distance).
- [[parproc-ch14-statistics-data-mining]] — §14.3.1 Snow parallel implementation (Manhattan distance).
- [[hands-on-llm-ch05-text-clustering-topic-modeling]] — Ch 5 contrasts k-means against HDBSCAN.
- [[Snowdoop]] — the R framework used in the Ch9 implementation.
- [[Snow]] — R cluster framework used in the Ch14 implementation.
- [[HierarchicalClustering]] — sibling clustering method that needs no pre-specified $K$.
- [[HDBSCAN]] / [[DensityBasedClustering]] / [[CentroidBasedClustering]] — the family contrast.
- [[BERTopic]] — k-means swap-in mentioned in Ch 5.
- [[UnsupervisedLearning]] — parent paradigm.
