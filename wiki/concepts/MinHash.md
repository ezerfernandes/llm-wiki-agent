---
title: "MinHash"
type: concept
tags: [information-retrieval, hashing, near-duplicate-detection, set-similarity, data-selection, mlsysbook]
sources: [iir-ch19-web-search-basics, mlsysbook-ch09-data-selection]
last_updated: 2026-06-05
---

Locality-sensitive hash family for estimating the **Jaccard similarity** of two sets. For a random permutation $\pi$ of the universe of possible elements (in practice a random hash function), define the **min-hash** of a set $S$ as:

$$h_\pi(S) = \min_{x\in S} \pi(x)$$

The defining property:

$$\Pr_\pi[h_\pi(S_1) = h_\pi(S_2)] = J(S_1, S_2) = \frac{|S_1 \cap S_2|}{|S_1 \cup S_2|}$$

**Sketches**: pick $k$ independent hash functions $\pi_1, \ldots, \pi_k$ and compute the $k$-tuple $(h_{\pi_1}(S), \ldots, h_{\pi_k}(S))$ — a fixed-length **signature** for $S$. The fraction of positions where two signatures agree is an unbiased estimator of $J(S_1, S_2)$ with standard error $O(1/\sqrt{k})$.

**Operational impact**: full-set Jaccard requires $O(|S|)$ work per comparison; signature comparison is $O(k)$. With $k = 100$ and a billion documents, near-duplicate detection becomes tractable.

**Composition with [[Shingling]]**: each document is converted to a set of $k$-word shingles, then to a min-hash signature; near-duplicates are documents whose signature agreement exceeds a threshold. Used at production web-search scale by [[AndreiBroder]] et al. at AltaVista in the late 1990s and inherited by every web search index since.

**LSH banding**: split each signature into $b$ bands of $r$ rows; hash each band to a bucket; pairs colliding in *any* band are candidates. Tuning $(b, r)$ gives a sigmoid-shaped probability curve over Jaccard — useful for tuning the precision/recall tradeoff in candidate generation. Full treatment in [[iir-ch19-web-search-basics]] §19.6.

## In ML pretraining ([[mlsysbook-ch09-data-selection|Machine Learning Systems Ch 9]])

MinHash is the workhorse of text [[DataDeduplication|near-duplicate detection]] in [[DataSelection|data-selection]] pipelines. For corpora of billions of documents it compresses each to a 128–256-value sketch, reducing dedup storage from terabytes of raw text to gigabytes of signatures and shifting the problem from $\mathcal{O}(D^2)$ toward $\mathcal{O}(D)$ when paired with [[LocalitySensitiveHashing|LSH]]. In distributed training, **distributed MinHash** lets each worker compute signatures independently, then aggregates to find cross-shard duplicates without any node seeing all data.

## Connections

- [[DataDeduplication]] / [[LocalitySensitiveHashing]] / [[JaccardSimilarity]] — the dedup machinery (Ch 9).
- [[DataSelection]] / [[DistributedTraining]] — pretraining and distributed dedup contexts.
- [[Shingling]] / [[AndreiBroder]] — the IR provenance.
- [[iir-ch19-web-search-basics]] / [[mlsysbook-ch09-data-selection]] — sources.
