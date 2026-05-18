---
title: "Information Theory"
type: concept
tags: [information-theory, foundational]
sources: [d2l-appendix-mathematics]
last_updated: 2026-05-16
---

# Information Theory

The mathematical study of information storage, transmission, and manipulation — founded by [[ClaudeShannon|Claude Shannon]]'s 1948 *A Mathematical Theory of Communication*. The discipline that turned "how much can a channel carry?", "how compressible is this signal?", and "how surprising is this observation?" into precise, quantitative questions ([[d2l-appendix-mathematics]] §information-theory).

## Core quantities

| Quantity | Definition | What it measures |
|---|---|---|
| [[SelfInformation\|Self-information]] | $I(X)=-\log_2 p(X)$ | bits of surprise from a single observed event |
| [[Entropy\|Entropy]] | $H(X)=-\mathbb{E}[\log p(X)]$ | expected self-information of a random variable |
| Joint entropy | $H(X,Y)$ | uncertainty about $(X,Y)$ jointly |
| Conditional entropy | $H(Y\mid X)=H(X,Y)-H(X)$ | residual uncertainty about $Y$ after observing $X$ |
| [[MutualInformation\|Mutual information]] | $I(X;Y)=H(X)+H(Y)-H(X,Y)$ | information shared between $X$ and $Y$ |
| [[KullbackLeiblerDivergence\|KL divergence]] | $D_{KL}(P\|Q)=\mathbb{E}_P[\log p/q]$ | directional gap from $Q$ to $P$ |
| [[CrossEntropy\|Cross-entropy]] | $H(P,Q)=H(P)+D_{KL}(P\|Q)$ | NLL of $Q$ under data $P$ |

## Why ML cares

- **Every classification loss is a cross-entropy.** Cross-entropy $=$ negative-log-likelihood under a categorical likelihood, so [[CrossEntropyLoss|cross-entropy loss]] is exactly [[MaximumLikelihoodEstimation|MLE]] for classification.
- **Every autoregressive [[LanguageModel|LM]] is trained on cross-entropy.** [[GPT]] / [[Claude]] / [[BERT]]-style models minimize $\mathbb{E}[-\log p_\theta(x_t\mid x_{<t})]$. **Perplexity** $= 2^H$ is the standard LM eval metric.
- **Contrastive / self-supervised representation learning maximizes [[MutualInformation|mutual information]].** [[InfoNCE]] (van den Oord et al. 2018) is a tractable MI lower bound that powers SimCLR / MoCo / CLIP.
- **[[VariationalInference|Variational inference]] / [[VariationalAutoencoder|VAEs]] minimize reverse [[KullbackLeiblerDivergence|KL divergence]]** to an intractable posterior.
- **[[RLHF]] / [[GRPO]] / [[PPO]] regularize policy updates with a KL penalty** to the reference / prior policy.
- **[[Diffusion]] models** decompose their training objective as a chain of conditional KLs.
- **Max-entropy reasoning** justifies common distributions (Gaussian, Exponential) as least-committal under moment constraints.

## Historical note

[[d2l-appendix-mathematics]] credits the **bit** terminology to [[JohnTukey|John Tukey]] and the full theoretical apparatus (self-information / entropy / channel capacity / source coding) to [[ClaudeShannon|Shannon]] 1948. Modern ML cross-entropy / KL / MI all trace back to this single 1948 *Bell System Technical Journal* article.

## Connections

- [[d2l-appendix-mathematics]] — §information-theory canonical reference.
- [[ClaudeShannon]] — originator.
- [[Entropy]] / [[CrossEntropy]] / [[KullbackLeiblerDivergence]] / [[MutualInformation]] / [[SelfInformation]] — core quantities.
- [[CrossEntropyLoss]] — operational ML loss derived from cross-entropy.
- [[MaximumLikelihoodEstimation]] — what cross-entropy minimization implements.
- [[LogSumExp]] — numerical-stability primitive used in entropy / softmax computations.
