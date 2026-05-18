---
title: "Hit Rate (Hit@k)"
type: concept
tags: [recommender-systems, ranking, evaluation]
sources: [d2l-recommender-systems]
last_updated: 2026-05-16
---

# Hit Rate — Hit@k / Hit@$\ell$

Standard top-$k$ retrieval metric for implicit-feedback recommenders. For each test user, check whether the ground-truth held-out item appears in the model's top-$\ell$ ranked recommendation list:

$$\textrm{Hit}@\ell = \frac{1}{m}\sum_{u\in\mathcal{U}}\mathbf{1}(\textrm{rank}_{u, g_u}\le\ell)$$

where $g_u$ is the ground-truth held-out item for user $u$, $\textrm{rank}_{u,g_u}$ is its position in $u$'s ranked recommendation list, and $m=|\mathcal{U}|$.

## Pairing

[[d2l-recommender-systems]] pairs Hit@k with [[AUC]] — the latter captures full-list ranking quality, the former a top-$k$ retrieval cut-off. Alternatives: [[NDCG]] (rank-discounted), [[MRR]] (mean reciprocal rank), Precision@k / Recall@k.

## Used in chapter

- [[NeuMF]] (§neumf) — evaluation against held-out last-item-per-user.
- [[CaserModel]] — same protocol.

## Connections
- [[NeuMF]], [[CaserModel]] — models evaluated with Hit@k.
- [[AUC]] — companion metric.
- [[ImplicitFeedback]] — data regime.
- [[d2l-recommender-systems]] — source §neumf.
