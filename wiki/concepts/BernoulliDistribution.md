---
title: "Bernoulli Distribution"
type: concept
tags: [probability, distributions, foundational]
sources: [d2l-appendix-mathematics]
last_updated: 2026-05-16
---

# Bernoulli Distribution

The simplest non-trivial random variable: a single coin flip ([[d2l-appendix-mathematics]] §distributions). $X\sim\text{Bernoulli}(p)$ takes the value $1$ with probability $p$ and $0$ with probability $1-p$, where $p\in[0,1]$.

## Densities and moments

- **PMF**: $P(X=k) = p^k(1-p)^{1-k}$ for $k\in\{0,1\}$.
- **Mean**: $\mu_X = p$.
- **Variance**: $\sigma_X^2 = p(1-p)$ — maximized at $p=1/2$ (the maximally uncertain coin).
- **Entropy** (in bits): $H(X) = -p\log_2 p - (1-p)\log_2(1-p)$ — also maximized at $p=1/2$ where $H=1$ bit.

## Where Bernoulli appears in ML

- **Binary classification**: a [[LogisticRegression|logistic regression]] / sigmoid-headed classifier outputs a Bernoulli distribution; the loss is its NLL — [[BinaryCrossEntropy|binary cross-entropy]] = $-[y\log\hat p + (1-y)\log(1-\hat p)]$.
- **[[Dropout]]**: each activation is multiplied by an independent Bernoulli($1-p_{\text{drop}}$) mask at training time.
- **[[NaiveBayes|Bernoulli naive Bayes]]** for binary-feature text classification (presence / absence of words).
- **Sampling from binary policies** in [[reinforcementlearning|RL]].
- **Bernoulli sums = Binomial**: $X_1+\ldots+X_n\sim\text{Binomial}(n,p)$, which for large $n$ converges (via the [[CentralLimitTheorem|CLT]]) to $\mathcal{N}(np, np(1-p))$.

## Connection to GAN discriminators

The [[Discriminator]] in a [[GenerativeAdversarialNetwork|GAN]] outputs the parameter of a Bernoulli — real-vs-fake — and is trained against the [[CrossEntropy|binary cross-entropy]] of that Bernoulli. The whole adversarial loss is two coupled Bernoulli NLLs.

## Connections

- [[d2l-appendix-mathematics]] — §distributions canonical reference.
- [[NaiveBayes]] — Bernoulli is the per-feature likelihood for binary inputs.
- [[CrossEntropyLoss]] — binary case = Bernoulli NLL.
- [[LogisticRegression]] — model whose output is a Bernoulli parameter.
- [[GaussianDistribution]] / [[PoissonDistribution]] — sibling fundamental distributions.
- [[CentralLimitTheorem]] — explains Binomial → Gaussian under large $n$.
- [[Dropout]] — the canonical Bernoulli use in neural-network regularization.
