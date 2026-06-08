---
title: "Cross-Entropy"
type: concept
tags: [information-theory, foundational]
sources: [d2l-appendix-mathematics, mlsysbook-ch05-neural-computation]
last_updated: 2026-06-05
---

# Cross-Entropy

The expected [[SelfInformation|surprisal]] of an observer with subjective distribution $Q$ upon seeing data drawn from the true distribution $P$ ([[d2l-appendix-mathematics]] §information-theory):

$$H(P, Q) = -\mathbb{E}_{x\sim P}[\log q(x)] = -\sum_i p_i \log q_i.$$

The fundamental decomposition is

$$H(P, Q) = H(P) + D_{KL}(P \,\|\, Q),$$

which makes cross-entropy = [[Entropy|entropy]] + [[KullbackLeiblerDivergence|KL divergence]]. Minimizing $H(P, Q)$ w.r.t. $Q$ is identical to minimizing the KL since $H(P)$ does not depend on $Q$.

## Why minimizing cross-entropy = MLE

Under a categorical model $p_\theta(y\mid\mathbf{x}) = \text{softmax}_y f(\mathbf{x}; \theta)$ with one-hot empirical labels:

$$\text{NLL}(\theta) = -\sum_n \log p_\theta(y_n\mid\mathbf{x}_n) = \sum_n H\!\big(\delta_{y_n},\, p_\theta(\cdot\mid\mathbf{x}_n)\big).$$

This is exactly [[MaximumLikelihoodEstimation|MLE]] under a categorical likelihood — and exactly the [[CrossEntropyLoss|cross-entropy loss]] every PyTorch / JAX / TensorFlow classifier minimizes. The triple identity *cross-entropy = NLL = KL (up to $P$-only constant)* is the load-bearing bridge between information theory and supervised learning.

## Bits, nats, perplexity

- $\log_2$ → bits-per-symbol (information theory).
- $\ln$ → nats (PyTorch's `F.cross_entropy`).
- Perplexity = $\exp(H(P, Q))$ — the "effective vocabulary size" reading common in [[LanguageModel|LM]] evaluation.

## ML uses

- **Classification loss** (`F.cross_entropy`, `SparseCategoricalCrossentropy`, etc.).
- **[[LanguageModel|LM]] pretraining loss**: autoregressive cross-entropy on next-token distributions — every [[transformer|Transformer]] LM from [[GPT]] to [[Claude]] minimizes this.
- **Distillation loss** with teacher / student soft labels.
- **[[GAN]] discriminator** = binary cross-entropy classifier.

## Connections

- [[d2l-appendix-mathematics]] — §information-theory canonical reference.
- [[CrossEntropyLoss]] — the operational loss-function page; this page is the information-theoretic concept.
- [[Entropy]] — what $H(P, P)$ collapses to.
- [[KullbackLeiblerDivergence]] — the difference $H(P, Q) - H(P)$.
- [[MaximumLikelihoodEstimation]] — equivalent under categorical / Gaussian / etc. likelihoods.
- [[InformationTheory]] — parent field.
- [[mlsysbook-ch05-neural-computation]] — systems view: for [[OneHotEncoding|one-hot]] labels cross-entropy simplifies to `−log(ŷ_c)` (only correct-class probability matters), its gradient w.r.t. outputs is just (predicted − true) — strong gradients far from target — and the `log(0)→−∞/NaN` hazard motivates the epsilon and log-sum-exp safeguards.
- [[Logits]] / [[Softmax]] — softmax(logits) is the distribution cross-entropy scores.
