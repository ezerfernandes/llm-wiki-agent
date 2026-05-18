---
title: "Hinge Loss (Ranking)"
type: concept
tags: [recommender-systems, ranking, loss-function]
sources: [d2l-recommender-systems]
last_updated: 2026-05-16
---

# Hinge Loss (for Ranking)

Pairwise ranking loss used as an interchangeable alternative to [[BPR]] in implicit-feedback recommenders. **Different from the SVM hinge loss** for classification — the recommender-systems variant operates on `(positive, negative)` score differences:

$$\mathcal{L} = \sum_{(u,i,j)\in D}\max(m - \hat{y}_{ui} + \hat{y}_{uj}, 0)$$

with margin $m$ (typically $1$). Pushes the positive's score to exceed the negative's by at least $m$; saturates beyond that.

## vs BPR

[[d2l-recommender-systems]]: *"These two losses are interchangeable for personalized ranking in recommendation."* Both target relative-order rather than absolute-score, both train on $(u, i^+, j^-)$ triples sampled via [[NegativeSampling]]. Empirically interchangeable on most benchmarks; BPR's log-sigmoid is smoother near the decision boundary, Hinge's clipping zeroes out already-correct pairs' gradients.

## Connections
- [[BPR]] — interchangeable pairwise sibling.
- [[PersonalizedRanking]] — target task.
- [[ImplicitFeedback]] — data regime.
- [[NegativeSampling]] — training mechanic.
- [[NeuMF]], [[CaserModel]] — D2L models that can be trained with either Hinge or BPR.
- [[d2l-recommender-systems]] — source §ranking.
