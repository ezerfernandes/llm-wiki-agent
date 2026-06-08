---
title: "Stochastic Gradient Descent"
type: concept
tags: [optimization, deep-learning, foundational]
sources: [mml-ch07-continuous-optimization, mml-book, d2l-linear-regression, d2l-optimization]
last_updated: 2026-06-05
---

# Stochastic Gradient Descent (SGD)

The variant of [[GradientDescent]] that estimates the loss gradient from a **single example** (or, in practice, a [[MinibatchSGD|minibatch]]) at each step rather than the full dataset. Workhorse of deep learning ([[mml-book]] §7.1.3; [[d2l-linear-regression]] §3.1.4).

## The pure-SGD update

For a loss $L(\boldsymbol\theta) = \frac{1}{n}\sum_{i=1}^n \ell^{(i)}(\boldsymbol\theta)$, pure SGD samples one $i_t \sim \{1,\dots,n\}$ per step and updates:

$$\boldsymbol\theta_{t+1} = \boldsymbol\theta_t - \eta\,\nabla \ell^{(i_t)}(\boldsymbol\theta_t).$$

## Why SGD over batch GD

[[d2l-linear-regression]] frames it as the resolution to two pathologies:

1. **Redundancy**: in any large dataset, examples overlap; a full-batch gradient wastes work — "if there is a lot of redundancy in the training data, the benefit of a full update is limited."
2. **Cost per step**: a single-example gradient is $n\times$ cheaper than a full-batch one. Even with noisier estimates, more frequent updates dominate in walltime.

The classical reference is :cite:`Bottou.2010` (also cited by D2L). Pure SGD's drawback — single-sample updates underuse hardware (matrix-vector ops are ~10× faster per element than scalar ops) and break layers like [[BatchNormalization|batch norm]] — motivates **minibatch SGD** as the universal compromise.

## Why SGD works in non-convex settings

In convex problems SGD's noise averages out and the iterates converge to the global minimum. In non-convex deep-learning losses, SGD finds *good* but not *optimal* parameters; the noise actively helps by escaping saddle points and flat regions. [[d2l-linear-regression]]: "Fortunately, even on difficult optimization problems, stochastic gradient descent can often find remarkably good solutions, owing partly to the fact that, for deep networks, there exist many configurations of the parameters that lead to highly accurate prediction."

## SGD as the universal DL optimizer

Every neural network in [[d2l-preface|D2L]] is trained by some flavor of minibatch SGD ([[Adam]] / [[Momentum]] / AdaGrad / RMSProp are SGD with preconditioning + momentum). The chapter on linear regression introduces SGD *despite* linear regression having a closed-form solution, precisely because every later architecture will need it: "our goal here is to illustrate how to train more general neural networks, and that requires that we teach you how to use minibatch SGD."

## From [[mml-ch07-continuous-optimization|MML Ch 7]]

§7.1.3 (pp. 231–233) gives the cleanest *theoretical* license for SGD. For an objective that is a **sum of per-example losses** $L(\boldsymbol\theta)=\sum_{n=1}^N L_n(\boldsymbol\theta)$ (Eq. 7.13) — e.g. the regression NLL $L=-\sum_n\log p(y_n\mid\mathbf{x}_n,\boldsymbol\theta)$ (Eq. 7.14, forward to Ch 9) — the batch update sums all $N$ gradients (Eq. 7.15), which is expensive at scale. SGD sums over a **mini-batch** (extreme case: one term). MML's framing of "stochastic": *"we acknowledge that we do not know the gradient precisely, but instead only know a noisy approximation."*

**The key insight** ([[mml-ch07-continuous-optimization|MML Ch 7]] p. 232): GD converges as long as the gradient is an **unbiased estimate** of the true gradient. The full sum $\sum_n\nabla L_n$ is an empirical estimate of the *expected* gradient (§6.4.1), so *any* unbiased subsample suffices. With an appropriately decreasing [[LearningRate|learning rate]] and mild assumptions, SGD converges almost surely to a local minimum (Bottou 1998). Mini-batch size is a **variance/cost trade-off**: large batches → accurate, low-variance, hardware-friendly, costlier; small batches → cheap, noisy, and the noise can **escape bad local optima** (acceptable since ML targets generalization, Ch 8, not exact minimization). "The current workhorse of large-scale machine learning" (Bottou et al. 2018).

## Connections

- [[mml-ch07-continuous-optimization]] — §7.1.3 canonical deep dive (unbiased-estimate argument).
- [[mml-book]] — umbrella source.
- [[d2l-linear-regression]] — pedagogical introduction of SGD as the universal DL optimizer.
- [[GradientDescent]] — the deterministic parent algorithm.
- [[MinibatchSGD]] — practical default; the form used in every framework.
- [[LearningRate]] — the step size $\eta$.
- [[Momentum]] — first-moment smoothing of the SGD update.
- [[Adam]] — adaptive-per-parameter SGD descendant.
- [[BatchNormalization]] — layer that depends on minibatch statistics, requiring `|B|>1`.
- [[Backpropagation]] — how the per-example gradient is computed.
