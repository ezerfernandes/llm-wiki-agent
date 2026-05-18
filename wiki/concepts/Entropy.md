---
title: "Entropy"
type: concept
tags: [information-theory, foundational]
sources: [d2l-appendix-mathematics]
last_updated: 2026-05-16
---

# Entropy (Shannon Entropy)

The expected [[SelfInformation|self-information]] of a random variable — the average number of bits required to encode one realization under the optimal code ([[ClaudeShannon|Shannon]] 1948; [[d2l-appendix-mathematics]] §information-theory).

For a discrete random variable $X\sim P$:

$$H(X) = -\mathbb{E}_{x\sim P}[\log p(x)] = -\sum_i p_i \log p_i.$$

For a continuous $X$ with density $p(x)$ this becomes the *differential entropy* $H(X)=-\int p(x)\log p(x)\,dx$ (no longer non-negative — it can be $-\infty$).

The base of the logarithm sets the unit: $\log_2$ gives **bits** (the standard in information theory), $\ln$ gives **nats**, $\log_{10}$ gives **dits**.

## Shannon's axiomatic characterization

[[d2l-appendix-mathematics]] §information-theory derives entropy from three common-sense axioms (informal version of *Csiszár 2008*):

1. Information is invariant under relabeling and the addition of probability-zero events.
2. Information from independent observations is *additive*; in general $H(X,Y)\leq H(X)+H(Y)$.
3. Information from (nearly) certain events is (nearly) zero.

Up to a choice of log base, these axioms uniquely determine $H$.

## Basic properties

- **Non-negative** (discrete): $H(X)\geq 0$, with equality iff $X$ is deterministic.
- **Maximum on uniform**: $H(X)\leq\log|\mathcal{X}|$, attained iff $P$ is uniform on $\mathcal{X}$ — *the uniform distribution has maximum entropy on a finite alphabet*.
- **Conditioning reduces entropy**: $H(X\mid Y)\leq H(X)$, with equality iff $X\perp Y$.

## ML uses

- **[[CrossEntropy|Cross-entropy]] = $H(P) + D_{KL}(P\|Q)$** — minimizing cross-entropy w.r.t. $Q$ is the same as minimizing the [[KullbackLeiblerDivergence|KL divergence]] (since $H(P)$ is a $Q$-independent constant). This is *the* link between classification with [[CrossEntropyLoss|cross-entropy loss]] and [[MaximumLikelihoodEstimation|MLE]] under a categorical likelihood.
- **Perplexity** of an [[LanguageModel|LM]] is $2^{H}$ — the effective vocabulary size if the model were uniform over its plausible next tokens.
- **Maximum-entropy distributions** as the "least-committal" choice under moment constraints (Gaussian = max-entropy under fixed mean + variance; Exponential = max-entropy under fixed positive mean).
- **Decision-tree splitting** (ID3 / C4.5) maximizes information gain $H(Y) - H(Y\mid X_j)$.

## Connections

- [[d2l-appendix-mathematics]] — §information-theory canonical reference.
- [[ClaudeShannon]] — originator (1948).
- [[SelfInformation]] — entropy is its expectation.
- [[CrossEntropy]] / [[CrossEntropyLoss]] — entropy generalization to two distributions.
- [[KullbackLeiblerDivergence]] — gap between cross-entropy and entropy.
- [[MutualInformation]] — symmetric entropy decomposition $I(X,Y)=H(X)+H(Y)-H(X,Y)$.
- [[InformationTheory]] — parent field.
- [[MaximumLikelihoodEstimation]] — minimizing NLL = minimizing cross-entropy = minimizing KL.
