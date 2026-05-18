---
title: "Mean Squared Error"
type: concept
tags: [loss-function, regression, metrics]
sources: [madewithml-training, d2l-linear-regression, d2l-appendix-mathematics]
last_updated: 2026-05-16
---

# Mean Squared Error (MSE)

A regression loss/metric averaging squared differences between predictions and targets:

$$L(\mathbf{w}, b) = \frac{1}{n}\sum_{i=1}^n \frac{1}{2}\left(\mathbf{w}^\top\mathbf{x}^{(i)} + b - y^{(i)}\right)^2.$$

The $\tfrac{1}{2}$ is purely notational — it cancels under differentiation ([[d2l-linear-regression]]). Penalizes large errors quadratically (sensitivity to outliers is the flip side); underlies most gradient-based regression learners; contrast with classification losses in [[ModelEvaluation]] / [[CrossEntropyLoss]].

## Why squared, not absolute

[[d2l-linear-regression]] §3.1.5: under additive Gaussian noise $\epsilon\sim\mathcal{N}(0,\sigma^2)$, minimizing MSE is exactly [[MaximumLikelihoodEstimation|maximum likelihood estimation]] (up to additive constants and a $1/\sigma^2$ scaling that the optimum is invariant to). [[Lasso|Absolute-value loss]] corresponds to Laplace-noise MLE — more robust to outliers but non-smooth at zero.

## Framework note

PyTorch's `nn.MSELoss` omits the $1/2$ factor, computing $\frac{1}{n}\sum(\hat y - y)^2$. A 2× difference in gradient magnitude vs. the textbook expression — absorbed into the learning rate in practice.

## Connections
- [[d2l-linear-regression]] — canonical introduction; both functional and probabilistic motivations.
- [[LinearRegression]] — the model that pairs with this loss.
- [[MaximumLikelihoodEstimation]] — MSE = Gaussian NLL.
- [[StochasticGradientDescent]] — typical optimizer over MSE.
- [[WeightDecay]] — extends MSE with an $\ell_2$ penalty.
