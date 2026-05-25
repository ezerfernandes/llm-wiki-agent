---
title: "HITS (Hyperlink-Induced Topic Search)"
type: concept
tags: [information-retrieval, link-analysis, web-search, eigenvector]
sources: [iir-ch21-link-analysis]
last_updated: 2026-05-23
---

Query-dependent link-analysis algorithm by [[JonKleinberg]] (1998). For each query, computes two scores per page: a **hub** score $h(v)$ and an **authority** score $a(v)$, with mutually reinforcing definitions:

$$h(v) = \sum_{(v,u)\in E} a(u) \qquad a(v) = \sum_{(u,v)\in E} h(u)$$

Hubs are pages that point to many good authorities; authorities are pages pointed to by many good hubs. Iterating these updates with normalization converges to the principal [[Eigenvector]] of $AA^T$ (for hubs) and $A^TA$ (for authorities), where $A$ is the adjacency matrix of the query-specific subgraph.

**Workflow** (per query):
1. Retrieve a root set of pages matching the query (e.g. top-K by [[TfIdf]]).
2. Expand to a base set by including pages linking to / linked from the root set.
3. Run the iteration above to convergence.
4. Return top-authority pages as primary results, top-hub pages as good link directories.

Contrast with [[PageRank]]: HITS is **query-dependent** (must run online for each query) and produces **two** scores; PageRank is **query-independent** (computed once offline) and produces **one**. The two algorithms were proposed contemporaneously (1998); PageRank's offline computation made it operationally cheaper and it won the production-search race. Full derivation in [[iir-ch21-link-analysis]].
