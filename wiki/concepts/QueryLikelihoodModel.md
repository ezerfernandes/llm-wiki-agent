---
title: "Query Likelihood Model"
type: concept
tags: [information-retrieval, language-model, ranking, smoothing]
sources: [iir-ch12-language-models-ir]
last_updated: 2026-05-23
---

Probabilistic retrieval model that ranks documents by the probability that the query was *generated* by the document's language model:

$$\text{score}(q, d) = P(q \mid M_d) = \prod_{t \in q} P(t \mid M_d)^{\text{tf}_{t,q}}$$

where $M_d$ is a multinomial unigram [[LanguageModel|language model]] estimated from document $d$. Introduced by [[JayPonte]] & [[BruceCroft]] (SIGIR 1998).

**Smoothing is essential** — without it, any query term absent from $d$ zeroes the entire score. Two standard smoothings:

- **Jelinek-Mercer (linear interpolation)**:
  $$P(t \mid d) = \lambda\, P_{\text{mle}}(t \mid M_d) + (1-\lambda)\, P_{\text{mle}}(t \mid M_c)$$
  with $M_c$ the collection language model and $\lambda \in [0,1]$ tuned per task.
- **Dirichlet**:
  $$P(t \mid d) = \frac{\text{tf}_{t,d} + \mu\, P(t \mid M_c)}{L_d + \mu}$$
  with $\mu$ a smoothing prior (typically a few hundred to a few thousand).

**Disambiguation — critical for this wiki**: the "language model" in chapter 12 of [[iir-ch12-language-models-ir|IIR]] is the **2008-era statistical** sense (multinomial unigram + count-based MLE + JM / Dirichlet smoothing). It is **not** the neural [[LanguageModel]] sense used elsewhere in this wiki (autoregressive transformer decoders trained by gradient descent). The shared name is a historical accident — both models compute $P(\text{text})$, but the mechanism, training procedure, and scale are unrelated.

The query likelihood model is competitive with [[BM25]] on standard test collections and is the foundation for later extensions (translation models, divergence-from-randomness, position-aware LMs).
