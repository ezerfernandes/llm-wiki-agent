---
title: "Naive Bayes"
type: concept
tags: [classification, probabilistic-models, foundational]
sources: [d2l-appendix-mathematics]
last_updated: 2026-05-16
---

# Naive Bayes Classifier

A probabilistic classifier that applies [[BayesTheorem|Bayes' rule]] with the **naive conditional-independence assumption**: all input features are mutually independent given the class label ([[d2l-appendix-mathematics]] §naive-bayes). Given features $\mathbf{x}=(x_1,\ldots,x_d)$ and label $y$:

$$P(y\mid\mathbf{x}) \;\propto\; P(y)\,P(\mathbf{x}\mid y) \;=\; P(y)\,\prod_{i=1}^d P(x_i\mid y).$$

The product factorization is the "naive" part — true conditional independence almost never holds in practice (pixels in an image, words in a sentence are not actually independent given the class), yet the classifier remains surprisingly competitive.

## Why the assumption helps

Estimating the full joint $P(\mathbf{x}\mid y)$ requires $\mathcal{O}(2^d)$ parameters for binary features — infeasible for $d > 30$. The independence assumption reduces this to $\mathcal{O}(d)$ per-feature counts. *"Learning is all about making assumptions"* ([[d2l-appendix-mathematics]] §naive-bayes); naive Bayes is the most aggressive feasible assumption.

## Training and inference

**Training** (binary features, $K$ classes):

- Class prior: $\hat P(y=c) = n_c/n$.
- Per-feature conditionals: $\hat P(x_i=1\mid y=c) = (n_{c,i}+1) / (n_c+2)$ with **[[LaplaceSmoothing|Laplace smoothing]]** to avoid zero probabilities.

**Inference** (in log-space to avoid underflow):

$$\hat y = \arg\max_c \;\log\hat P(y=c) + \sum_{i=1}^d \log\hat P(x_i\mid y=c).$$

## D2L MNIST demonstration

[[d2l-appendix-mathematics]] §naive-bayes trains naive Bayes on **binarized** MNIST (threshold pixels at 128). The classifier reaches roughly **84% test accuracy** — vastly better than the 10% uniform baseline, despite the absurd assumption that all 784 pixels are independent given the digit. This is the classic "naive Bayes works in practice even though it shouldn't" empirical result.

## Variants by likelihood

| Variant | Likelihood | Domain |
|---|---|---|
| Bernoulli naive Bayes | $x_i\in\{0,1\}$ | binary features (e.g., presence/absence of words) |
| Multinomial naive Bayes | $x_i\in\mathbb{Z}_{\geq 0}$ | counts (bag-of-words text classification) |
| Gaussian naive Bayes | $x_i\in\mathbb{R}$, $P(x_i\mid y)=\mathcal{N}(\mu_{c,i},\sigma_{c,i}^2)$ | continuous features |

## Why naive Bayes works despite wrong assumptions

The argmax classifier only needs *correct ranking* of class log-probabilities, not correct probabilities — so calibration can be terrible while accuracy stays high. This is **Domingos & Pazzani 1997**'s result that naive Bayes is *optimal* under zero-one loss even when the independence assumption is wrong.

## Limitations

- Probability calibration is poor — predictions are overconfident.
- Cannot capture feature interactions — XOR-like patterns are invisible.
- Zero-probability features (without smoothing) make the entire log-posterior $-\infty$.

## Connections

- [[d2l-appendix-mathematics]] — §naive-bayes canonical reference.
- [[BayesTheorem]] — the rule naive Bayes applies.
- [[MaximumLikelihoodEstimation]] — what the parameter estimates are.
- [[LaplaceSmoothing]] — the canonical fix for zero-probability features.
- [[BernoulliDistribution]] / [[GaussianDistribution]] — common per-feature likelihoods.
- [[MNIST]] — D2L's running benchmark for the demo.
- [[LogSpace|log-space computation]] — required for numerical stability over many features.
