---
title: "Rocchio Algorithm"
type: concept
tags: [information-retrieval, relevance-feedback, query-expansion]
sources: [iir-ch09-relevance-feedback-query-expansion, iir-ch14-vector-space-classification]
last_invoked: 2026-05-23
last_updated: 2026-05-23
---

Vector-space update rule for **relevance feedback**, due to [[Rocchio]] (1971). Given a query $q_0$, a set of judged-relevant documents $D_r$, and a set of judged-non-relevant documents $D_{nr}$, modify the query toward the relevant centroid and away from the non-relevant centroid:

$$q_m = \alpha\, q_0 + \frac{\beta}{|D_r|}\sum_{d_j\in D_r} d_j - \frac{\gamma}{|D_{nr}|}\sum_{d_j\in D_{nr}} d_j$$

Typical settings: $\alpha=1$, $\beta=0.75$, $\gamma=0.15$. Negative components in $q_m$ are usually clipped to zero (terms in the original query are not removed even if they appear in non-relevant docs).

**Variants**:
- **Ide dec-hi**: subtract only the top-ranked non-relevant document (a sharper signal than averaging all non-relevant docs).
- **[[PseudoRelevanceFeedback]]** (a.k.a. blind feedback): treat the top-k initial results as $D_r$ without asking the user — fragile under topic drift but operationally automatic.

When repurposed for **classification** (one class per centroid, classify by nearest centroid), the same construction is called **[[RocchioClassification]]** — convex and fast but cannot represent multi-modal classes (see [[iir-ch14-vector-space-classification]]). Full treatment of feedback in [[iir-ch09-relevance-feedback-query-expansion]].
