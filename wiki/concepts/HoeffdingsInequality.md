---
title: "Hoeffding's Inequality"
type: concept
tags: [probability, learning-theory, concentration, foundational]
sources: [d2l-linear-classification]
last_updated: 2026-05-16
---

# Hoeffding's Inequality

A finite-sample concentration bound for bounded random variables. For $n$ IID random variables $X_1,\ldots,X_n \in [a, b]$ with mean $\mu$ and sample mean $\bar X$:

$$
P(\bar X - \mu \geq t) \leq \exp\!\left(-\frac{2 n t^2}{(b-a)^2}\right).
$$

In the special case of the 0/1 classification indicator (one classifier $f$, $X_i = \mathbf 1[f(\mathbf x_i)\neq y_i]\in\{0,1\}$), [[d2l-linear-classification]] writes

$$
P\big(\epsilon_{\mathcal D}(f) - \epsilon(f) \geq t\big) \leq \exp(-2 n t^2).
$$

## Why it matters

Hoeffding gives a **valid finite-sample** bound on test-set error estimation — strictly stronger than the [[CentralLimitTheorem|central-limit-theorem]] asymptotic $\mathcal O(1/\sqrt n)$ rate, which only holds in the limit. Concretely, to be 95% confident that a classifier's test-set error is within ±0.01 of its population error:

| Method | Required samples |
|---|---|
| CLT / Bernoulli variance bound (asymptotic) | ≈ 10,000 |
| Hoeffding's inequality (finite-sample) | ≈ 15,000 |

The ~10k test-set sizes on standard ML benchmarks ([[FashionMNIST|Fashion-MNIST]] / CIFAR-10 / ImageNet validation) are roughly the CLT-implied minimum for credible 1%-difference claims; this is not coincidence.

## Connection to uniform convergence

Hoeffding bounds **one fixed classifier's** error estimate. Generalization to **every classifier in a hypothesis class simultaneously** ([[UniformConvergence|uniform convergence]]) requires a union bound over $\mathcal F$ — finite for finite classes, but for continuous classes (e.g. linear models in $\mathbb R^d$) needs a complexity measure like [[VCDimension|VC dimension]]:

$$
P\big(R(f) - R_{\mathrm{emp}}(f) < \alpha\big) \geq 1 - \delta \quad\text{for}\quad \alpha \geq c\sqrt{\tfrac{\mathrm{VC} - \log\delta}{n}}.
$$

## Connections

- [[UniformConvergence]] — the multi-classifier generalization that builds on Hoeffding.
- [[VCDimension]] — complexity measure used in the uniform-convergence union bound.
- [[Generalization]] / [[GeneralizationGap]] — what concentration bounds protect.
- [[CentralLimitTheorem]] — the asymptotic counterpart.
- [[TestSetReuse]] — what happens when Hoeffding's IID assumption is violated by re-using the test set.
- [[d2l-linear-classification]] — corpus anchor (Section *The Test Set*).
