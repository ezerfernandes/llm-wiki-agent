---
title: "IIR Ch. 16: Flat Clustering"
type: source
tags: [iir, information-retrieval, textbook, clustering, k-means, em-algorithm, evaluation]
date: 2026-05-23
source_file: "https://nlp.stanford.edu/IR-book/html/htmledition/flat-clustering-1.html"
---

## Summary

Chapter 16 of Manning, Raghavan, and Schütze's *Introduction to Information Retrieval* (2008) introduces **flat (partitional) clustering**, the family of unsupervised algorithms that partition a document collection into a flat set of `K` groups with no hierarchical structure. The chapter motivates clustering through the **cluster hypothesis** — the foundational claim that documents in the same cluster behave similarly with respect to relevance to information needs — and surveys five concrete IR applications: search result clustering, Scatter-Gather browsing, collection-wide static clustering (e.g., Google News), cluster-based language modeling, and cluster-based retrieval acceleration. The bulk of the chapter develops two algorithms: **K-means** (the canonical hard, centroid-based method whose objective is to minimize the **residual sum of squares (RSS)**) and the **EM algorithm** for **model-based clustering** (a soft generalization in which documents have fractional membership). The chapter also gives a careful treatment of two evaluation regimes — internal (RSS itself) and external (purity, NMI, Rand index, F-measure against gold labels) — and discusses how to choose the cardinality `K`, including the elbow heuristic and penalized objectives like **AIC** and the generic penalized RSS.

## Key Claims

- **Cluster hypothesis**: *"Documents in the same cluster behave similarly with respect to relevance to information needs."* This is the central justification for using clustering in IR, originally articulated by Jardine and van Rijsbergen (1971).
- **Clustering is the most common form of unsupervised learning** — no human-labeled training data is required, in contrast with classification (Chapter 13).
- A clustering problem is defined by three inputs: a document set `D = {d₁,…,d_N}`, a desired number of clusters `K`, and an **objective function** that scores candidate partitions.
- **Hard clustering** assigns each document to exactly one cluster via a surjective map `γ : D → {1,…,K}`; **soft clustering** assigns fractional memberships and is naturally produced by probabilistic models like EM.
- **Flat clustering** produces a set of clusters with no explicit structure, in contrast with the hierarchical clustering of Chapter 17.
- **K-means** is *"perhaps the most widely used flat clustering algorithm due to its simplicity and efficiency."* Its objective is to minimize RSS, equivalently to minimize the average squared Euclidean distance from documents to their centroid.
- K-means is guaranteed to **converge monotonically** (RSS never increases between iterations) but only to a **local optimum**; initialization matters and outliers can produce singleton clusters.
- The K-means iteration is **linear in all relevant parameters**: time complexity is `O(IKNM)` where `I` = iterations, `K` = clusters, `N` = documents, `M` = vocabulary dimensionality.
- **EM** generalizes K-means to a probabilistic mixture model; for vector-space documents with Gaussian mixtures, K-means is the limiting case of EM as the variance approaches zero.
- **Choosing K** is fundamentally ill-posed — *"there is seldom a single best number of clusters."* Practical heuristics include the elbow method on the RSS curve and penalized objectives such as `RSS_min(K) + λK` (with AIC the special case `λ = 2M`).
- **External evaluation** requires gold classes. Purity is intuitive but trivially gameable by setting `K = N`. NMI corrects for this by normalizing by entropy. RI weights every pair equally. F-measure permits penalizing false negatives more heavily than false positives (typically with `β > 1`).
- **Distance choice matters**: *"Different distance measures give rise to different clusterings."* Euclidean distance is the default in K-means; cosine similarity is also common for text.

## Section Notes

### 16.1 Clustering in Information Retrieval

The chapter opens by enumerating five application areas where clustering pays off in IR:

1. **Search result clustering** disambiguates polysemous queries (the textbook's running example is *jaguar* → car / cat / OS). Rather than scrolling a flat list, the user picks the cluster matching their intent.
2. **Scatter-Gather** is an interactive browsing interface (Cutting et al., 1992) in which the system clusters the collection, the user selects clusters of interest, and the system recursively re-clusters within that selection.
3. **Collection clustering** generates a static topical map of the whole corpus for exploratory browsing. Google News is the canonical industrial example.
4. **Cluster-based language modeling** smooths sparse term statistics by interpolating a cluster-specific model with the global model, attacking the data-sparsity problem in probabilistic IR.
5. **Cluster-based retrieval** speeds up search at scale: instead of scoring every document against the query, the system identifies the nearest cluster centroids and only scores documents within them, trading some precision for substantial latency wins.

### 16.2 Problem Statement

Formally, a hard flat clustering is a function `γ : {d₁,…,d_N} → {1,…,K}` satisfying surjectivity (no empty clusters). The objective function is *"often defined in terms of similarity or distance between documents,"* using cosine similarity or Euclidean distance. K-means specifically *"aims to minimize the average distance between documents and their centroids or, equivalently, to maximize the similarity between documents and their centroids."*

Because the number of possible partitions of `N` items into `K` groups grows combinatorially (Stirling numbers of the second kind), **exhaustive enumeration is infeasible** and all practical methods are heuristic local optimizers initialized from a starting partition.

### 16.3 Evaluation of Clustering

Two evaluation regimes are distinguished:

- **Internal criteria** (e.g., RSS itself) score a clustering using only its own structure. They are useful as objective functions but biased — minimizing them is what K-means does by construction.
- **External criteria** compare to a held-out gold partition `C = {c₁,…,c_J}`. Four classical external measures are introduced (formulas in the next section).

The chapter emphasizes that none of the external measures is universally correct: purity is easy to game; NMI penalizes too-fine clusterings; RI treats all pairs symmetrically (which may be undesirable when classes are imbalanced); F-measure with `β > 1` lets you express that missing a true pair is worse than introducing a spurious one.

### 16.4 K-means

K-means is the chapter's centerpiece. Given seeds `μ⃗₁,…,μ⃗_K`, it iterates two steps until convergence:

1. **Reassign** each document to its nearest centroid (creating clusters `ω₁,…,ω_K`).
2. **Recompute** each centroid as the mean of its members.

Convergence is guaranteed because both steps weakly decrease RSS and RSS is bounded below by zero. Termination conditions in practice: fixed iteration cap `I`, `γ` stabilizes, centroids stop moving, RSS falls below a threshold, or the per-iteration decrease in RSS falls below `θ`.

**Initialization** is the dominant source of variance. Recommended heuristics include:

- Excluding obvious outliers when sampling seeds.
- Multiple random restarts, picking the lowest-RSS run.
- Running a cheap hierarchical clustering on a subsample to seed K-means (the **Buckshot algorithm** of Cutting et al. 1992).
- Averaging several random vectors per cluster to produce a smoother seed.

**Computational notes**: text vectors are sparse but centroids become *dense* (the mean of sparse vectors usually has many nonzero coordinates), which dominates the cost of the reassignment step. A common engineering fix is to truncate each centroid to its top-`k` (e.g., `k = 1000`) coordinates by magnitude.

### 16.4.1 Cluster Cardinality in K-means

Because RSS is monotonically non-increasing in `K` (you can always lower it by adding clusters), simply minimizing RSS does not yield a useful `K`. The chapter discusses:

- **Elbow / knee** on the RSS vs. `K` curve: pick the `K` where the marginal RSS reduction drops sharply.
- **Penalized RSS**: choose `K` to minimize `RSS_min(K) + λK`. Larger `λ` favors fewer clusters.
- **AIC** as a principled instance of the penalized form: `λ = 2M` (twice the model dimensionality). The textbook warns that *"AIC can rarely be applied without modification in text clustering"* because its derivation assumes Gaussian noise that does not hold for high-dimensional sparse text vectors.
- **BIC** (Bayesian Information Criterion) is mentioned as a stricter alternative that penalizes complexity more heavily as `N` grows (`λ ∝ log N`).

### 16.5 Model-Based Clustering

Model-based clustering reframes clustering as **density estimation**: *"the data were generated by a model and tries to recover the original model from the data."* The generative model is a mixture: a latent cluster identity `k` is drawn with prior probability `α_k`, then the document is sampled from cluster `k`'s component distribution.

For Bernoulli text (binary term-occurrence vectors), the chapter develops the full EM update equations (see next section). The general structure is:

- **E-step**: compute soft responsibilities `r_{nk} = P(ω_k | d_n; Θ)` using the current parameters.
- **M-step**: update parameters `Θ = {α_k, q_{mk}}` by weighted maximum likelihood, treating `r_{nk}` as soft counts.

EM converges to a local maximum of the data log-likelihood. K-means is recovered as the limiting case of EM with Gaussian components whose variance goes to zero (responsibilities collapse to indicator functions).

### 16.6 References and Further Reading

K-means has a tangled history with multiple independent inventions: **Lloyd (1957, published 1982)**, **Ball (1965)**, **MacQueen (1967)**, and **Hartigan & Wong (1979)**. EM is **Dempster, Laird, and Rubin (1977)**, with the standard reference text being **McLachlan and Krishnan (1996)**. The cluster hypothesis is **Jardine and van Rijsbergen (1971)**: *"Associations between documents convey information about the relevance of documents to requests."* Cluster-based retrieval studies include Croft (1978), Salton (1971, 1975), and Voorhees (1985). The Rand index is **Rand (1971)**; the adjusted Rand index is **Hubert and Arabie (1985)**. Survey references: Berkhin (2006b), Duda et al. (2000), Anderberg (1973). Industrial applications: Google News and Columbia NewsBlaster (hierarchical); search-result clustering work by Hearst and Pedersen (1996) and Zamir and Etzioni (1999).

## Algorithms & Formulas

### K-means (Lloyd's Algorithm)

```
K-MEANS({x⃗₁,…,x⃗_N}, K):
  1. Select K seeds {s⃗₁,…,s⃗_K} from the dataset.
  2. For k = 1..K: μ⃗_k ← s⃗_k
  3. Repeat until stopping criterion:
       a. (Reassign)  For each document x⃗_n:
            γ(n) ← argmin_k ||x⃗_n − μ⃗_k||²
       b. (Recompute) For each cluster k:
            μ⃗_k ← (1 / |ω_k|) · Σ_{x⃗ ∈ ω_k} x⃗
  4. Return {μ⃗_k}, γ
```

### Residual Sum of Squares (RSS)

For a single cluster `k` with centroid `μ⃗(ω_k)`:

```
RSS_k = Σ_{x⃗ ∈ ω_k} ||x⃗ − μ⃗(ω_k)||²
```

Total objective:

```
RSS = Σ_{k=1..K} RSS_k
```

Centroid definition:

```
μ⃗(ω) = (1 / |ω|) · Σ_{x⃗ ∈ ω} x⃗
```

### Time Complexity

`O(I · K · N · M)` — linear in iterations, clusters, documents, and vocabulary dimensionality.

### Purity

Each cluster is assigned to its most frequent gold class; purity is the fraction of correctly assigned documents:

```
purity(Ω, C) = (1 / N) · Σ_k max_j |ω_k ∩ c_j|
```

Range `[0, 1]`. Trivially 1 when `K = N` (every doc its own cluster) — hence not used in isolation for model selection.

### Normalized Mutual Information (NMI)

```
NMI(Ω, C) = I(Ω; C) / [(H(Ω) + H(C)) / 2]
```

where mutual information `I(Ω; C) = Σ_k Σ_j (|ω_k ∩ c_j| / N) · log( N·|ω_k ∩ c_j| / (|ω_k|·|c_j|) )` and entropy `H(Ω) = − Σ_k (|ω_k| / N) · log(|ω_k| / N)`. NMI is `0` when the clustering carries no information about the gold classes and `1` for a perfect match. The denominator `(H(Ω) + H(C)) / 2` penalizes clusterings with extreme cardinality.

### Rand Index (RI)

For each pair of documents, classify as TP/TN/FP/FN by whether the clustering and the gold labels agree on putting them together:

```
RI = (TP + TN) / (TP + TN + FP + FN)
```

| | Same cluster | Different cluster |
|---|---|---|
| **Same class** | TP | FN |
| **Different class** | FP | TN |

### F-measure for Clustering

```
P = TP / (TP + FP)
R = TP / (TP + FN)
F_β = ((β² + 1) · P · R) / (β² · P + R)
```

With `β > 1`, the F-measure weights recall (catching true co-class pairs) more heavily than precision (avoiding spurious co-cluster pairs).

### Penalized RSS / AIC for Choosing K

General penalized form:

```
K* = argmin_K [ RSS_min(K) + λ · K ]
```

AIC (special case `λ = 2M` where `M` is dimensionality):

```
K* = argmin_K [ RSS_min(K) + 2 · M · K ]
```

### EM for a Mixture of Multivariate Bernoullis

Model: document `d` is generated by first picking cluster `k` with prior `α_k`, then independently flipping a coin with bias `q_{mk}` for each word `m` in the vocabulary.

Per-cluster document likelihood:

```
P(d | ω_k; Θ) = ( Π_{m: w_m ∈ d}  q_{mk} ) · ( Π_{m: w_m ∉ d} (1 − q_{mk}) )
```

Mixture likelihood:

```
P(d | Θ) = Σ_{k=1..K} α_k · P(d | ω_k; Θ)
```

**E-step** (soft responsibilities):

```
r_{nk} = ( α_k · Π_{w_m ∈ d_n} q_{mk} · Π_{w_m ∉ d_n} (1 − q_{mk}) )
       / ( Σ_{j=1..K} α_j · Π_{w_m ∈ d_n} q_{mj} · Π_{w_m ∉ d_n} (1 − q_{mj}) )
```

**M-step**:

```
q_{mk} = ( Σ_{n=1..N} r_{nk} · 1[w_m ∈ d_n] ) / ( Σ_{n=1..N} r_{nk} )
α_k   = ( Σ_{n=1..N} r_{nk} ) / N
```

The full maximum-likelihood objective being optimized:

```
Θ* = argmax_Θ L(D | Θ) = argmax_Θ Σ_{n=1..N} log P(d_n | Θ)
```

## Key Quotes

> "Documents in the same cluster behave similarly with respect to relevance to information needs."
> — The cluster hypothesis, as stated in §16.1.

> "Documents within a cluster should be as similar as possible; and documents in one cluster should be as dissimilar as possible from documents in other clusters."
> — Operational definition of clustering quality.

> "Clustering is the most common form of unsupervised learning."
> — §16, framing.

> "K-means is perhaps the most widely used flat clustering algorithm due to its simplicity and efficiency."
> — §16.4.

> "Different distance measures give rise to different clusterings."
> — §16.2, emphasizing that the metric is part of the model.

> "Model-based clustering assumes that the data were generated by a model and tries to recover the original model from the data."
> — §16.5, on EM.

> "There is seldom a single best number of clusters."
> — §16.4.1, on choosing K.

> "Associations between documents convey information about the relevance of documents to requests."
> — Jardine and van Rijsbergen (1971), as quoted in §16.6.

## Connections

- [[KMeansClustering]] — Lloyd's algorithm, RSS objective, and convergence properties are the centerpiece of this chapter.
- [[CentroidBasedClustering]] — K-means is the prototypical centroid-based method; this chapter formalizes the centroid `μ⃗(ω)` and the geometric intuition.
- [[InformationRetrieval]] — The five IR applications of clustering (result clustering, Scatter-Gather, collection clustering, language modeling, cluster-based retrieval) tie the chapter to the rest of the IIR book.
- [[HierarchicalClustering]] — The contrast partner to flat clustering; Chapter 17 of IIR covers it. The Buckshot initializer for K-means is a hierarchical/flat hybrid.
- [[FlatClustering]] — The chapter's own subject: partitional clustering without nested structure.
- [[ClusterHypothesis]] — Jardine and van Rijsbergen's foundational claim that motivates clustering in IR.
- [[EMAlgorithm]] — The general framework for soft, model-based clustering; K-means is the zero-variance Gaussian limit.
- [[ModelBasedClustering]] — Generative-model framing in which clustering becomes maximum-likelihood density estimation.
- [[GaussianMixtureModel]] — The continuous-vector counterpart to the Bernoulli mixture worked out in §16.5; the connection from EM to K-means runs through GMMs.
- [[Purity]] — Simple external evaluation; biased toward large `K`.
- [[NormalizedMutualInformation]] — Information-theoretic external evaluation that normalizes by entropy.
- [[RandIndex]] — Pair-counting external evaluation; the adjusted Rand index (Hubert & Arabie, 1985) corrects for chance agreement.
- [[AIC]] — Akaike Information Criterion, instantiated here as the penalty `2MK` on RSS.
- [[BIC]] — Bayesian Information Criterion, a stricter alternative to AIC.
- [[MixtureModel]] — The probabilistic structure underlying EM clustering.
- [[KullbackLeiblerDivergence]] — Underlies the EM derivation as the gap minimized between the variational and true posteriors (background for §16.5).
- [[Embedding]] — Vector-space document representations are the input to K-means; the chapter assumes Chapter 6's tf-idf vectors but applies equally to dense embeddings.

## Contradictions

- **None with existing wiki pages.** The chapter's treatment of K-means as a hard clustering with an Euclidean RSS objective is consistent with [[KMeansClustering]] and [[CentroidBasedClustering]]. Its framing of EM as a soft generalization is consistent with [[EMAlgorithm]] and [[GaussianMixtureModel]].
- One nuance worth flagging for future ingests: the chapter's claim that *"AIC can rarely be applied without modification in text clustering"* tempers the more enthusiastic AIC/BIC treatment in some classical statistics references. If a later ingest cites AIC uncritically for text clustering, this caveat from IIR should be cross-referenced.
- The cluster hypothesis itself has been challenged empirically in some IR studies (e.g., Voorhees 1985 found mixed effectiveness for cluster-based retrieval). The chapter acknowledges this in the References section; the wiki should note that the cluster hypothesis is a useful working assumption rather than an empirical certainty.
