---
title: "IIR Ch. 17: Hierarchical Clustering"
type: source
tags: [iir, information-retrieval, textbook, hierarchical-clustering, hac, dendrogram]
date: 2026-05-23
source_file: "https://nlp.stanford.edu/IR-book/html/htmledition/hierarchical-clustering-1.html"
---

## Summary

Chapter 17 of *Introduction to Information Retrieval* (Manning, Raghavan, Schütze, 2008) covers **[[HierarchicalClustering]]** — methods that, unlike flat clustering ([[KMeansClustering]], EM), produce a **hierarchy** of nested clusterings instead of a single partition. Two paradigms are covered: **agglomerative** (bottom-up, called **[[HAC]]** — Hierarchical Agglomerative Clustering) and **divisive** (top-down). The bulk of the chapter dissects HAC's four linkage criteria — **[[SingleLinkClustering]]**, **[[CompleteLinkClustering]]**, **[[GroupAverageClustering]]** (GAAC), and **[[CentroidBasedClustering]]** — each producing different cluster shapes from the same data. The chapter develops the efficient O(N² log N) priority-queue HAC algorithm, proves which linkages satisfy **monotonicity**, exhibits the **inversion** pathology of centroid linkage, contrasts the **chaining effect** of single-link with the **outlier sensitivity** of complete-link, and introduces **[[DivisiveClustering]]** via **[[BisectingKMeans]]** for large-scale settings. The chapter closes with **[[ClusterLabeling]]** techniques (differential vs internal labeling) for making clusterings interpretable, since unlabeled clusters are nearly useless to end users.

## Key Claims

- Hierarchical clustering outputs a **[[Dendrogram]]** — a tree of nested merges — which is "more informative than the unstructured set of clusters returned by flat clustering."
- HAC offers three advantages over flat clustering: **no preset K**, **deterministic** output (no random seed sensitivity), and **richer structure**. The cost: at least quadratic in N.
- The four standard HAC linkages differ only in how they define inter-cluster similarity: **single-link** uses max-of-pairs (closest pair), **complete-link** uses min-of-pairs (farthest pair), **group-average** uses mean of all pairwise similarities, **centroid** uses centroid-to-centroid similarity.
- **Single-link** suffers from the **chaining effect**: long, straggly clusters form because a single nearby bridge point can chain two otherwise distant groups together. It is a *local* criterion — only the touching ends matter.
- **Complete-link** avoids chaining and yields tight, small-diameter clusters but is **highly sensitive to outliers**: one distant document can dominate cluster diameter and reshape the dendrogram.
- **Group-average** (GAAC) considers *all* pairwise similarities, balancing the extremes of single- and complete-link; typically the recommended general-purpose method for IR.
- **Centroid clustering** equals the average similarity over pairs from *different* clusters only (excluding within-cluster pairs); this asymmetry is exactly what causes **inversions** — points where similarity *increases* as clusters grow, producing non-monotonic dendrograms with crossing merge bars.
- **Monotonicity** holds for single-link, complete-link, and group-average; **fails** for centroid linkage.
- Naive HAC is Θ(N³); using **priority queues** over rows of the similarity matrix C reduces it to **Θ(N² log N)**.
- **Single-link** has a special property — **best-merge persistence** — that allows an even faster Θ(N²) algorithm via a next-best-merge (NBM) array. Complete-link, GAAC, and centroid do *not* have best-merge persistence.
- **Single-link is *optimal*** with respect to its own combination-similarity criterion (provable by induction). Complete-link, GAAC, and centroid can fail to find the optimal partition — but optimal under the *wrong* criterion is not necessarily useful, and single-link's optimality is more theoretical than practical given chaining.
- **Divisive clustering** (top-down, e.g. **bisecting K-means**) has the opposite information profile from HAC: it makes top-level splits with **global** information about the dataset, whereas HAC makes its earliest merge decisions with only **local** information. Divisive is often **linear** in N if a full hierarchy is not required.
- **Cluster labeling** is essential for interpretability. **Differential labeling** (using [[MutualInformation]] or chi-squared against other clusters) outperforms naive frequency-based **internal labeling**, which is polluted by globally-common terms ("year", "Tuesday").
- For very large corpora, the **Buckshot algorithm** combines HAC on a √N sample (to obtain stable seeds) with K-means on the full corpus, achieving overall Θ(N) runtime while inheriting HAC's deterministic quality.

## Section Notes

### 17.1 Hierarchical Agglomerative Clustering

Start with each of N documents as a **singleton cluster**. At each step, merge the **two most similar clusters** under the chosen linkage SIM. Continue until a single cluster remains, recording every merge. The output is a **dendrogram** with similarity (or distance) on the y-axis and documents on the x-axis. The dendrogram can be "cut" at any horizontal level to yield a flat clustering:

1. Cut at a preset similarity threshold (e.g., similarity ≥ 0.4).
2. Cut where the largest *gap* between consecutive merge similarities occurs (suggesting a natural cluster count).
3. Apply a penalized criterion balancing fit and cluster count.
4. Prespecify K and cut to produce exactly K clusters.

**Combination similarity** of a cluster ω is the similarity at which it was last merged (or 1.0 for singletons under cosine on unit-normalized vectors). **Monotonicity** requires that the sequence of combination similarities along any root-to-leaf path is non-increasing — i.e., merges only ever combine *less* similar things as the tree grows.

Naive HAC computes the N×N similarity matrix once (Θ(N² M) where M is feature dimensionality), then performs N−1 merges; each merge scans the matrix in Θ(N²), yielding **Θ(N³)** overall.

### 17.2 Single-Link and Complete-Link Clustering

**Single-link** defines `SIM(ωᵢ, ωⱼ) = max{sim(dₐ, d_b) : dₐ ∈ ωᵢ, d_b ∈ ωⱼ}` — the closest pair. Graph-theoretically, single-link clusters are **connected components** in the graph of edges with similarity above the merge threshold.

**Complete-link** uses `min` instead — the farthest pair. Complete-link clusters correspond to **maximal cliques** in the same thresholded graph.

The **chaining effect** in single-link: imagine a string of points where each consecutive pair is close but the endpoints are far. Single-link greedily merges along the chain, producing one long, thin cluster that ignores macro-structure. Complete-link refuses to merge once the farthest-pair similarity drops, producing rounder clusters — but a single far-flung outlier inflates the diameter of any cluster it might join, distorting the rest of the hierarchy.

### 17.2.1 Time complexity of HAC

The efficient algorithm **EFFICIENT-HAC** keeps each row C[k] of the similarity matrix as a **priority queue P[k]** sorted by similarity. To find the next merge, scan the N heads of the priority queues — Θ(N). After merging clusters i and j into a new cluster, update row k of the matrix and the priority queue for each remaining k (Θ(log N) per insertion/deletion). Total: **Θ(N² log N)**.

**Single-link** admits a faster **Θ(N²)** algorithm via a **next-best-merge (NBM)** array. The reason: single-link satisfies **best-merge persistence** — if d's best merge partner was d', and we merge d' with some d'', then the new best partner for d is just `max(sim(d, d'), sim(d, d''))`. No re-scan needed. Complete-link breaks this: after a merge, the new max-pair distance can shoot up arbitrarily, so the NBM trick fails. The example in the text: d₃'s best merge candidate d₂ gets merged with cluster d₁; afterward, an *unrelated* d₄ becomes d₃'s new best candidate.

In practice, the gap between Θ(N²) and Θ(N² log N) is dwarfed by the cost of computing similarities themselves — similarity is "an order of magnitude slower than comparing two scalars in sorting."

### 17.3 Group-Average Agglomerative Clustering (GAAC)

GAAC defines the similarity of two clusters as the **average similarity over all pairs**, including within-cluster pairs:

$$
\text{SIM-GA}(\omega_i, \omega_j) = \frac{1}{(N_i + N_j)(N_i + N_j - 1)} \sum_{d_m \in \omega_i \cup \omega_j} \sum_{d_n \in \omega_i \cup \omega_j, d_n \neq d_m} \vec{d_m} \cdot \vec{d_n}
$$

(Self-similarities are excluded from the average.)

GAAC requires three things that single-link and complete-link do not: vectors (not just a distance matrix), **length-normalized** vectors (so self-similarities = 1.0), and **dot-product** similarity (i.e. cosine). The payoff is computational: by precomputing the **sum vector** `s(ω) = Σ d_m∈ω` for each cluster, the merged-cluster sum is just `s(ωᵢ ∪ ωⱼ) = s(ωᵢ) + s(ωⱼ)`, and the average can be derived in constant time per cluster pair. Overall complexity matches complete-link: Θ(N² log N).

GAAC avoids both chaining (it considers all pairs, not just the touching ends) and outlier sensitivity (one outlier is diluted by the rest). It is the most-recommended general method in the chapter.

### 17.4 Centroid Clustering

**Centroid clustering** defines cluster similarity as the **similarity between centroids**:

$$
\text{SIM-CENT}(\omega_i, \omega_j) = \vec{\mu}(\omega_i) \cdot \vec{\mu}(\omega_j)
$$

Algebraically, this equals the **average dot product over pairs from *different* clusters** — i.e., GAAC *without* the within-cluster pairs:

$$
\text{SIM-CENT}(\omega_i, \omega_j) = \frac{1}{N_i N_j} \sum_{d_m \in \omega_i} \sum_{d_n \in \omega_j} \vec{d_m} \cdot \vec{d_n}
$$

That asymmetric exclusion is exactly the source of **inversions**: after a merge, the new cluster's centroid can end up *more* similar to some other cluster than the most recently merged pair was to each other. In the dendrogram, this shows up as a merge bar drawn *below* an earlier one — the lines cross. The classic worked example uses three points; the second merge has *higher* similarity than the first, violating monotonicity.

Despite this defect, centroid clustering is popular because the centroid-to-centroid concept is **intuitively simpler** than GAAC's "average of all pairwise" — and it works fine when inversions don't occur in practice.

### 17.5 Optimality of HAC

A clustering is optimal (under a given combination-similarity criterion) if no other K-clustering achieves a higher minimum combination similarity. The chapter proves by induction that **single-link HAC is optimal** for its own min-over-bipartition combination similarity. The proof relies on the fact that the greedy merge step *cannot* exclude any optimal merge later.

**Complete-link** and **GAAC** are *not* optimal: a counterexample shows both greedily merging a unit-distance pair first, locking themselves out of a better two-cluster solution available later.

**Centroid** is not even monotonic, so the notion of optimality (over a chain of merges with non-increasing similarity) doesn't apply cleanly.

| Method | Optimal? | Monotonic? | Primary issue |
|---|---|---|---|
| Single-link | yes | yes | chaining effect |
| Complete-link | no | yes | outlier sensitivity |
| Group-average | no | yes | (best practical performance overall) |
| Centroid | no | **no** (inversions) | inversions in dendrogram |

### 17.6 Divisive Clustering

**[[DivisiveClustering]]** flips HAC upside down: start with one cluster containing all documents and **recursively split** until each document is alone. Splitting requires a flat clustering subroutine — most commonly **[[BisectingKMeans]]** (K-means with K=2 applied recursively).

Two advantages over HAC:

1. **Speed.** Each bisection is linear in the documents in that node; if the full leaf-level hierarchy isn't required, total time is linear in N.
2. **Global information at decision time.** HAC's first merges are made knowing only local pairwise similarities; by the time it has global context, it has already committed irreversible early merges. Divisive's top-level split has full visibility into the whole corpus, so the most-important partition decision is made with the most information.

The cost: greater conceptual complexity (need a flat clustering inside), and the splits are themselves heuristic (K-means is non-deterministic and non-optimal).

### 17.7 Cluster Labeling

A clustering is unusable without labels for each cluster. Two families:

**[[ClusterLabeling|Differential labeling]]:** Find terms that distinguish the target cluster from *other* clusters. Use [[MutualInformation]], chi-squared, or odds ratio — the same statistics used in feature selection for classification. Output is a few terms (e.g., 3–5) per cluster. Works well but requires comparison against the full clustering.

**Internal labeling:** Use only the target cluster's own statistics:

- **Centroid terms:** Highest-weighted terms in the cluster's centroid vector — more representative than any single document.
- **Title labels:** Title of the document closest to the centroid — more readable but possibly idiosyncratic.
- **Hybrid:** Mix terms and titles.

Internal methods are cheaper but pollute labels with **globally common terms** ("year", "Tuesday", "said") that appear in every cluster and discriminate nothing. Differential labeling solves this naturally.

For hierarchical clusterings, labeling must also account for parent–child relationships — a child cluster's label should distinguish it from its *parent* and *siblings*, not just from the whole corpus.

### 17.8 Implementation notes

- **Inverted indexes** help when the similarity matrix is sparse (many zero similarities).
- For large corpora with **dense centroids**, complete-link clustering may outperform GAAC: complete-link is Θ(M_ave · N² log N) (M_ave = avg vocabulary per document), GAAC is Θ(M · N² log N) (M = total vocabulary). Truncating centroids or using **sparse medoids** as cluster prototypes can mitigate this.
- For corpora with ≥ 1 million documents, HAC alone is infeasible. The **Buckshot algorithm** runs HAC on a √N-sized sample to produce K stable seeds, then runs K-means on the full corpus from those seeds — Θ(N) overall, retains HAC's seed quality.
- The chapter references the **R environment** and **CLUTO** as practical clustering software.

## Algorithms & Formulas

**EFFICIENT-HAC (priority-queue HAC), Θ(N² log N):**

```
1. For each pair (i, j), compute C[i][j] = sim(dᵢ, dⱼ).
2. For each i, build priority queue P[i] from row C[i] (max-heap on similarity).
3. Mark all clusters as active. Each singleton is its own cluster.
4. Repeat N−1 times:
     a. Find the active cluster i whose P[i].max similarity is highest;
        let j be the cluster that achieves it.
     b. Merge i and j into a new cluster k. Mark i, j inactive.
     c. For each remaining active cluster m:
          - Remove old entries for i and j from P[m].
          - Compute SIM(k, m) under the chosen linkage.
          - Insert (k, SIM(k, m)) into P[m].
        Also build P[k] from row C[k].
     d. Record the merge in the dendrogram with combination similarity = SIM(i, j).
```

**Single-link Θ(N²) via NBM array.** Maintain `NBM[i] = argmax_j SIM(i, j)`. On merging i, j → k, update `NBM[m]` for each m using just `max(SIM(m, i), SIM(m, j))` — best-merge persistence guarantees this is correct.

**Linkage formulas (over two clusters ω_i, ω_j):**

- **Single-link:** SIM(ω_i, ω_j) = max{sim(dₐ, d_b) : dₐ ∈ ω_i, d_b ∈ ω_j}
- **Complete-link:** SIM(ω_i, ω_j) = min{sim(dₐ, d_b) : dₐ ∈ ω_i, d_b ∈ ω_j}
- **Group-average (GAAC):** average dot product over *all* pairs in ω_i ∪ ω_j (excluding self-pairs), efficiently computed from sum vectors s(ω).
- **Centroid:** SIM(ω_i, ω_j) = μ(ω_i) · μ(ω_j), equivalent to average dot product over **cross-cluster** pairs only.

**Monotonicity condition:** A linkage is monotonic if for any merge sequence with combination similarities s₁, s₂, …, sₙ₋₁ (in order), we have s₁ ≥ s₂ ≥ … ≥ sₙ₋₁. Single-link, complete-link, and GAAC satisfy this. Centroid does not — example: three nearly-collinear points where merging the middle pair produces a centroid that is *more* similar to the third point than the original two were to each other.

**Dendrogram cut rules:** (a) cut at similarity threshold τ, (b) cut at the largest similarity gap, (c) cut to obtain prespecified K clusters, (d) cut to optimize a penalized in-cluster-similarity objective.

## Key Quotes

> "Hierarchical clustering outputs a hierarchy, a structure that is more informative than the unstructured set of clusters returned by flat clustering."

> "The most common hierarchical clustering algorithms have a complexity that is at least quadratic in the number of documents."

> "A chain of points can be extended for long distances without regard to the overall shape of the emerging cluster." — on the single-link **chaining effect**.

> "The complete-link merge criterion is non-local and can be affected by points at a great distance." — why complete-link lacks best-merge persistence.

> "Centroid clustering can give rise to inversions: similarity can increase during clustering."

> "Top-down [divisive] clustering benefits from complete information about the global distribution when making top-level partitioning decisions."

## Connections

- [[HierarchicalClustering]] — parent concept; this chapter is the canonical IR textbook treatment of bottom-up clustering with linkage variants. Single-link / complete-link / GAAC / centroid all live here.
- [[HAC]] — Hierarchical Agglomerative Clustering, the bottom-up workhorse defined in this chapter. New page.
- [[SingleLinkClustering]] — min-distance linkage; chaining effect; only linkage with best-merge persistence and Θ(N²) algorithm.
- [[CompleteLinkClustering]] — max-distance linkage; tight clusters, outlier-sensitive; maximal-clique interpretation.
- [[GroupAverageClustering]] — GAAC; mean of all pairs; the chapter's recommended default for IR.
- [[CentroidBasedClustering]] — existing page; this chapter contributes the **inversion** phenomenon and the cross-cluster-pairs algebraic identity.
- [[Dendrogram]] — existing page; this chapter formalizes monotonicity as a dendrogram property and shows inversions as crossing bars.
- [[DivisiveClustering]] — top-down complement to HAC; uses a flat subroutine. New page.
- [[BisectingKMeans]] — the standard divisive splitter; recursive K=2 K-means. New page.
- [[KMeansClustering]] — existing page; used as the bisecting subroutine and as the Buckshot follow-up after HAC seeding.
- [[ClusterLabeling]] — differential vs internal labeling; essential for interpretability. New page.
- [[InformationRetrieval]] — parent domain; clustering supports search results browsing, query-result reorganization, and corpus exploration.
- [[MutualInformation]] — used in differential cluster labeling to score candidate terms.
- [[iir-ch01-boolean-retrieval]], [[iir-ch02-term-vocabulary-postings]], [[iir-ch03-dictionaries-tolerant-retrieval]], [[iir-ch04-index-construction]], [[iir-ch05-index-compression]], [[iir-ch10-xml-retrieval]] — sibling chapters in the same textbook.

## Contradictions

- **Contradicts the framing in [[HierarchicalClustering]] (existing wiki page sourced from ISLR and Hands-On LLMs):** the existing page presents "average" linkage as a single, unproblematic option. IR Ch. 17 splits this into **GAAC** (includes within-cluster pairs, monotonic, recommended) and **centroid** (excludes within-cluster pairs, *non-monotonic*, produces inversions). The two are different methods that behave differently — they should not be conflated.
- **Refines [[CentroidBasedClustering]]:** the existing concept page presents centroid clustering as a clean, simple method. IR Ch. 17 explicitly identifies the **inversion / non-monotonicity** defect — a real practical pitfall absent from the existing wiki.
- **Tension with the optimization framing in [[KMeansClustering]]:** K-means produces a single flat partition optimized for K predetermined clusters and is non-deterministic across runs. HAC produces a *deterministic* hierarchy at all K simultaneously — a fundamentally different output product. Neither dominates: the chapter notes hybrid use (Buckshot — HAC on √N sample seeds K-means on full corpus).
- **Sense disambiguation for "hierarchical":** the existing [[HierarchicalClustering]] page already notes that [[HDBSCAN]] uses "hierarchical" in a *density-based* sense unrelated to linkage-based agglomerative merging. IR Ch. 17 belongs squarely to the linkage-based sense; the disambiguation in the existing page remains valid and important.
