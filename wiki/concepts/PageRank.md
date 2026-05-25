---
title: "PageRank"
type: concept
tags: [information-retrieval, link-analysis, web-search, markov-chain]
sources: [iir-ch07-complete-search-system, iir-ch19-web-search-basics, iir-ch21-link-analysis]
last_updated: 2026-05-23
---

Query-independent measure of web page importance, defined as the **stationary distribution** of a teleporting random walk on the web graph. Originally [[LarryPage]] & [[SergeyBrin]]'s thesis work at [[stanforduniversity|Stanford]] and the founding ranking signal of [[google|Google]].

Transition matrix:

$$P = (1-\alpha)A + \alpha\frac{E}{N}$$

where $A$ is the row-normalized link-adjacency matrix, $E$ is the all-ones matrix (uniform teleport), $\alpha \approx 0.15$ is the teleportation probability. Solved by **power iteration**:

$$\pi_{t+1} = \pi_t P \quad\text{until}\quad \|\pi_{t+1} - \pi_t\| < \varepsilon$$

Ergodicity (guaranteed by the teleport term) ensures a unique stationary $\pi$. Each $\pi_i$ is interpreted as the long-run probability of a random surfer being at page $i$ — high PageRank pages are those that many other high-PageRank pages link to. Combined at query time with [[TfIdf]] / [[BM25]] / cosine relevance as a [[StaticQualityScore]] $g(d)$ in `net-score(q,d) = g(d) + sim(q,d)` (see [[iir-ch07-complete-search-system]]).

**Variants**: topic-sensitive PageRank (per-topic teleport vectors combined at query time), personalized PageRank (user-specific teleport). Conceptual sibling: [[HITS]] (query-dependent, hubs + authorities). Full derivation in [[iir-ch21-link-analysis]].
