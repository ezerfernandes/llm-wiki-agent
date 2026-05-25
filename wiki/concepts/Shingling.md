---
title: "Shingling"
type: concept
tags: [information-retrieval, near-duplicate-detection, web-search, hashing]
sources: [iir-ch19-web-search-basics]
last_updated: 2026-05-23
---

Document fingerprinting technique for **near-duplicate detection** on the web. Represent each document as a set of overlapping **$k$-shingles** — consecutive $k$-word subsequences (typically $k = 4$ to $9$):

$$S_k(d) = \{ w_i\,w_{i+1}\,\ldots\,w_{i+k-1} : i = 1, \ldots, |d| - k + 1\}$$

The similarity of two documents is then estimated by the **Jaccard similarity** of their shingle sets:

$$J(S_k(d_1), S_k(d_2)) = \frac{|S_k(d_1) \cap S_k(d_2)|}{|S_k(d_1) \cup S_k(d_2)|}$$

Documents above a threshold (typically $J \geq 0.9$) are near-duplicates and one is dropped from the index — important because the open web contains many machine-generated mirror sites, scraped copies, and templated boilerplate.

**Scaling problem**: comparing every document pair is $O(N^2)$ in document set size; computing the Jaccard exactly is $O(|S|)$ per pair. **[[MinHash]]** sketches reduce both — a fixed-length signature (say 100 hash values) per document, whose collision probability under a random hash family equals the Jaccard similarity:

$$\Pr[\min_{s\in S_1} h(s) = \min_{s\in S_2} h(s)] = J(S_1, S_2)$$

A bank of 100 such hashes gives an unbiased estimator of $J$ at $\pm 0.05$ precision. Locality-sensitive hashing on the signatures further reduces candidate-pair generation to $O(N)$ expected.

Shingling + min-hash is the canonical pre-neural near-duplicate stack used at production web-search scale. Full treatment in [[iir-ch19-web-search-basics]] §19.6.
