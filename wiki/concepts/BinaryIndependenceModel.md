---
title: "Binary Independence Model (BIM)"
type: concept
tags: [information-retrieval, probabilistic-ir, ranking]
sources: [iir-ch11-probabilistic-ir]
last_updated: 2026-05-23
---

Probabilistic retrieval model that applies the [[ProbabilityRankingPrinciple]] under two simplifying assumptions:

1. **Binary** — each term either occurs in a document or it does not (no frequency information).
2. **Independence** — given relevance, term occurrences are conditionally independent across the vocabulary.

Under these assumptions, ranking by $P(R=1 \mid q, d)$ is equivalent to ranking by the **Retrieval Status Value**:

$$\text{RSV}_d = \sum_{t \in q \cap d} \log \frac{p_t (1 - u_t)}{u_t (1 - p_t)}$$

where $p_t = P(t \in d \mid R=1, q)$ (probability term $t$ appears in a *relevant* doc) and $u_t = P(t \in d \mid R=0, q)$ (probability it appears in a *non-relevant* doc).

**Probability estimation**:
- **Theoretical** (if relevance set known): $p_t = |D_r \cap D_t| / |D_r|$, $u_t = (|D_t| - |D_r \cap D_t|) / (N - |D_r|)$ — used in [[RelevanceFeedback|relevance feedback]] iterations.
- **Practical** (cold start, no relevance judgments): assume $p_t = 0.5$ (no prior info per term), $u_t \approx \text{df}_t / N$ (most docs are non-relevant) — recovers idf-like weighting. Add Laplace smoothing (+½) to avoid zero/one estimates.

BIM is the direct ancestor of [[OkapiBM25]] — BM25 relaxes the binary assumption (uses tf) and adds length normalization (parameters $k_1$, $b$). Originated with [[StephenRobertson]] & [[KarenSparckJones]] in the 1970s. Full derivation in [[iir-ch11-probabilistic-ir]] §11.3.
