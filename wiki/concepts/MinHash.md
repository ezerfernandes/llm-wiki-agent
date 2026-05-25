---
title: "MinHash"
type: concept
tags: [information-retrieval, hashing, near-duplicate-detection, set-similarity]
sources: [iir-ch19-web-search-basics]
last_updated: 2026-05-23
---

Locality-sensitive hash family for estimating the **Jaccard similarity** of two sets. For a random permutation $\pi$ of the universe of possible elements (in practice a random hash function), define the **min-hash** of a set $S$ as:

$$h_\pi(S) = \min_{x\in S} \pi(x)$$

The defining property:

$$\Pr_\pi[h_\pi(S_1) = h_\pi(S_2)] = J(S_1, S_2) = \frac{|S_1 \cap S_2|}{|S_1 \cup S_2|}$$

**Sketches**: pick $k$ independent hash functions $\pi_1, \ldots, \pi_k$ and compute the $k$-tuple $(h_{\pi_1}(S), \ldots, h_{\pi_k}(S))$ — a fixed-length **signature** for $S$. The fraction of positions where two signatures agree is an unbiased estimator of $J(S_1, S_2)$ with standard error $O(1/\sqrt{k})$.

**Operational impact**: full-set Jaccard requires $O(|S|)$ work per comparison; signature comparison is $O(k)$. With $k = 100$ and a billion documents, near-duplicate detection becomes tractable.

**Composition with [[Shingling]]**: each document is converted to a set of $k$-word shingles, then to a min-hash signature; near-duplicates are documents whose signature agreement exceeds a threshold. Used at production web-search scale by [[AndreiBroder]] et al. at AltaVista in the late 1990s and inherited by every web search index since.

**LSH banding**: split each signature into $b$ bands of $r$ rows; hash each band to a bucket; pairs colliding in *any* band are candidates. Tuning $(b, r)$ gives a sigmoid-shaped probability curve over Jaccard — useful for tuning the precision/recall tradeoff in candidate generation. Full treatment in [[iir-ch19-web-search-basics]] §19.6.
