---
title: "Pseudo-Relevance Feedback (PRF)"
type: concept
tags: [information-retrieval, relevance-feedback, query-expansion]
sources: [iir-ch09-relevance-feedback-query-expansion]
last_updated: 2026-05-23
---

Automatic ("blind") relevance feedback. Run the initial query, treat the top-$k$ returned documents as if they were judged relevant (typical $k = 5$ to $20$), and apply a feedback algorithm (most commonly the [[RocchioAlgorithm|Rocchio update]]) to expand or reweight the query. Re-run the modified query, return its top results.

**Why it works**: the top-$k$ documents are usually genuinely on-topic even without judgments, so their term distribution gives a useful signal about what the query was *trying* to express — surfacing synonyms and related terms the original query missed.

**Why it fails**:
- **Topic drift**: if the initial query is ambiguous or the top-$k$ are off-topic, PRF amplifies the wrong signal. Example: query *"jaguar"* returning car articles → expanded query becomes more car-biased, never recovering the animal sense.
- **Query-effort tradeoff**: PRF takes 2× the query latency (initial run + re-run) and adds memory pressure (more candidate documents).

**Mitigations**:
- Mixture-model PRF: model top-$k$ docs as a mixture of a topic LM and a background LM, only use topic terms for expansion.
- Selective PRF: apply only to queries that look ambiguous (high entropy in top-$k$ scores, low result agreement).
- Combine with explicit (judged) feedback when available.

PRF is the bridge between fully manual [[RelevanceFeedback|relevance feedback]] (impractical for web search) and global [[QueryExpansion|query expansion]] from thesauri. Used as a competitive baseline for any new retrieval method. Full treatment in [[iir-ch09-relevance-feedback-query-expansion]] §9.1.6.
