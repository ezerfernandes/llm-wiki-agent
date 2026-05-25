---
title: "Probability Ranking Principle (PRP)"
type: concept
tags: [information-retrieval, probabilistic-ir, ranking, decision-theory]
sources: [iir-ch11-probabilistic-ir]
last_updated: 2026-05-23
---

Foundational theorem of probabilistic IR, stated by [[StephenRobertson]] (1977):

> If a retrieval system's response to each request is a ranking of the documents in the collection in order of decreasing probability of relevance to the user who submitted the request, where the probabilities are estimated as accurately as possible on the basis of whatever data have been made available to the system for this purpose, the overall effectiveness of the system to its user will be the best that is obtainable on the basis of those data.

In other words: under a **1/0 loss** function (correct retrieval costs 0, missed retrieval costs 1) and the assumption that document relevance is independent across documents, ranking by $P(R=1 \mid q, d)$ is **optimal** — no other ranking achieves higher expected precision at any cutoff.

**Extension with retrieval costs**: when retrieving a non-relevant document has cost $C_1$ and missing a relevant document has cost $C_2$, the optimal decision is to retrieve $d$ iff $\frac{P(R=1 \mid q,d)}{P(R=0 \mid q,d)} \geq \frac{C_1}{C_2}$. With equal costs this reduces to the standard PRP.

The PRP licenses the entire **probabilistic retrieval** family (see [[iir-ch11-probabilistic-ir]]): [[BinaryIndependenceModel]], [[OkapiBM25]], two-Poisson models, language-modeling approaches under specific assumptions. **Caveats** that motivate later research: relevance is treated as document-independent (ignores diversity / novelty / user information needs); the optimality holds only when probabilities are accurate, which they rarely are in practice.
