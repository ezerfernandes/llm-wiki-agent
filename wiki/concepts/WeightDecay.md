---
title: "Weight Decay"
type: concept
tags: [regularization, optimization, foundational]
sources: [d2l-linear-regression, d2l-multilayer-perceptrons]
last_updated: 2026-05-16
---

# Weight Decay

[[Regularization|Regularization]] technique that adds an $\ell_2$ penalty $\tfrac{\lambda}{2}\|\mathbf{w}\|^2$ to the loss, biasing the optimizer toward small-norm solutions. When optimized by minibatch [[StochasticGradientDescent|SGD]], weight decay is equivalent to $\ell_2$ regularization; [[d2l-linear-regression]] §3.7 calls it "the most widely used technique for regularizing parametric machine learning models."

## The penalty

Augment the training loss:

$$L_\text{reg}(\mathbf{w}, b) = L(\mathbf{w}, b) + \frac{\lambda}{2}\|\mathbf{w}\|^2.$$

The hyperparameter $\lambda \geq 0$ is selected on validation data (typical range: $10^{-6}$ to $10^{-2}$).

## SGD update reveals the "decay"

Plug into the minibatch update:

$$\mathbf{w} \leftarrow (1-\eta\lambda)\mathbf{w} - \frac{\eta}{|\mathcal{B}|}\sum_{i\in\mathcal{B}}\mathbf{x}^{(i)}\left(\mathbf{w}^\top\mathbf{x}^{(i)} + b - y^{(i)}\right).$$

The leading $(1-\eta\lambda)$ factor **shrinks $\mathbf{w}$ toward zero on every step**, even absent any data signal — hence "weight decay." For [[StochasticGradientDescent|SGD]] this is *exactly* equivalent to $\ell_2$ regularization; for adaptive optimizers ([[Adam]], etc.) the equivalence breaks and `weight_decay` vs `L2` become subtly different (motivating AdamW).

## Why $\ell_2$ over $\ell_1$

[[d2l-linear-regression]]:
- **$\ell_2$ (this concept; ridge in statistics)**: spreads weight evenly across many features, robust to single-feature measurement noise.
- **$\ell_1$ ([[Lasso|lasso]])**: zeroes out small weights, performs feature selection — different goal.

D2L uses the **squared** $\ell_2$ norm (not the unsquared Euclidean norm) for computational convenience: the derivative is linear in $\mathbf{w}$, so the gradient becomes the sum of derivatives.

## Bias usually not regularized

Standard practice across frameworks (PyTorch's `weight_decay` applied via parameter groups, MXNet's `wd_mult=0` for biases, Keras's `kernel_regularizer` not `bias_regularizer`): bias terms are typically excluded from the penalty. D2L justifies this loosely — bias has different geometric meaning (shift, not magnitude).

## Frameworks integrate it into the optimizer

[[d2l-linear-regression]] §3.7.4: "the deep learning framework makes it especially convenient, integrating weight decay into the optimization algorithm itself for easy use in combination with any loss function." Because every parameter must be touched once per SGD step anyway, weight decay adds zero overhead.

| Framework | API |
|---|---|
| [[PyTorch]] | `torch.optim.SGD(params, lr, weight_decay=wd)` (per-param-group) |
| Keras / [[TensorFlow]] | `tf.keras.regularizers.l2(wd)` via `kernel_regularizer` |
| Optax / [[JAX]] | `optax.chain(optax.additive_weight_decay(wd), optax.sgd(lr))` |
| Gluon / [[MXNet]] | `gluon.Trainer(..., {'wd': wd})` + `wd_mult=0` for biases |

## Equivalence with MAP under a Gaussian prior

[[WeightDecay]] = [[MAPEstimation|MAP]] estimation under a zero-mean Gaussian prior $\mathbf{w}\sim\mathcal{N}(0,\sigma_0^2 I)$. The Bayesian view: $\lambda = \sigma^2 / \sigma_0^2$ — large $\lambda$ corresponds to a sharply-peaked prior. This is the bridge to [[RidgeRegression]] (the Bayesian-MAP linear regression) and [[BayesianLinearRegression]].

## Practical heuristic adopted throughout D2L

"In this book we will often adopt the common heuristic whereby weight decay is applied to all layers of a deep network."

## Connections

- [[d2l-linear-regression]] — §3.7 canonical reference.
- [[Regularization]] — parent concept.
- [[RidgeRegression]] — the statistical name for the same procedure on a linear model.
- [[Lasso]] — $\ell_1$ counterpart.
- [[StochasticGradientDescent]] / [[MinibatchSGD]] — the optimizer whose update reveals the decay.
- [[MAPEstimation]] / [[BayesianLinearRegression]] — Bayesian interpretation under a Gaussian prior.
- [[Overfitting]] — what weight decay combats.
- [[Norm]] — $\|\cdot\|_2^2$ is the squared $\ell_2$ norm.
- [[Adam]] — `weight_decay` ≠ $\ell_2$ for adaptive optimizers (motivates AdamW).
