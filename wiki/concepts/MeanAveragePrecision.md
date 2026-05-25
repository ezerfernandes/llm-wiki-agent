---
title: "Mean Average Precision (MAP)"
type: concept
tags: [information-retrieval, evaluation, ranking-metric]
sources: [iir-ch08-ir-evaluation]
last_updated: 2026-05-23
---

Ranked-retrieval evaluation metric for **binary relevance**. For a single query, **Average Precision** is the mean of the precision scores computed at each rank where a relevant document appears:

$$\text{AP}(q) = \frac{1}{|D_r|} \sum_{k=1}^{|R|} \text{precision@}k \cdot \mathbb{1}[\text{doc at rank } k \text{ is relevant}]$$

where $|D_r|$ is the number of relevant documents for the query (the divisor), $|R|$ is the number of retrieved documents, and the indicator picks out the ranks at which a relevant doc lands. Equivalently, it is the area under the precision-recall curve interpolated at the relevant-doc recall points.

**Mean Average Precision** is the mean of AP over a set of queries:

$$\text{MAP} = \frac{1}{|Q|} \sum_{q \in Q} \text{AP}(q)$$

MAP is the canonical TREC ad-hoc retrieval metric and the dominant ranked-retrieval evaluation number for binary-relevance test collections. Properties: rewards both precision (high values when relevant docs land at the top) and recall (lower values if some relevant docs are never retrieved); insensitive to the order of non-relevant documents.

**Contrast with [[NDCG]]**: MAP is for binary relevance, NDCG is for graded relevance. For purely binary judgments, MAP and NDCG correlate strongly but MAP gives a slightly sharper signal in the high-precision regime. Full treatment in [[iir-ch08-ir-evaluation]] §8.4.
