---
title: "Momentum"
type: concept
tags: [optimization, deep-learning, foundational]
sources: [mml-book, d2l-optimization]
last_updated: 2026-05-16
---

# Momentum

[[GradientDescent|Gradient descent]] variant that replaces the instantaneous gradient with a **leaky average** over past gradients. Originally proposed by [[BorisPolyak|Polyak]] in 1964 ("heavy-ball method"); refined by [[YuriiNesterov|Nesterov]] 1983 ([[NesterovMomentum|Nesterov accelerated gradient]]). The single most important variance-reduction / acceleration technique in modern optimization — every modern DL optimizer ([[Adam]], [[RMSProp]] variants, SGD-with-momentum) inherits Polyak's update form.

## The update

Maintain a **velocity** state $\mathbf{v}_t$ alongside the parameters:

$$\begin{aligned}
\mathbf{v}_t &\leftarrow \beta\,\mathbf{v}_{t-1} + \mathbf{g}_t, \\
\mathbf{x}_t &\leftarrow \mathbf{x}_{t-1} - \eta\,\mathbf{v}_t,
\end{aligned}$$

with $\beta \in [0, 1)$ controlling the memory length and $\mathbf{v}_0 = \mathbf{0}$. Setting $\beta = 0$ recovers plain [[GradientDescent]].

## Recursive expansion

Unrolling the velocity recursion ([[d2l-optimization]] §momentum):

$$\mathbf{v}_t = \sum_{\tau=0}^{t-1} \beta^\tau \mathbf{g}_{t-\tau, t-\tau-1}.$$

Past gradients are weighted with geometrically decaying coefficients. The **effective sample weight** is:

$$\sum_{\tau=0}^\infty \beta^\tau = \frac{1}{1-\beta}.$$

So $\beta = 0.9$ ⇒ ~10 effective past gradients; $\beta = 0.99$ ⇒ ~100; $\beta = 0.5$ ⇒ ~2.

## Two benefits

1. **Variance reduction** ([[StochasticGradientDescent|SGD]] regime): noisy gradients average toward the true direction. Effective sample size $\frac{1}{1-\beta}$.
2. **Acceleration on ill-conditioned problems**: on the elliptic objective $f(\mathbf{x}) = 0.1 x_1^2 + 2 x_2^2$ (D2L's running example), plain GD oscillates wildly in $x_2$ and crawls in $x_1$; momentum cancels the oscillating-direction velocities and accumulates the consistent-direction ones, dramatically improving convergence.

## Convex-quadratic analysis

[[d2l-optimization]] §momentum-theoretical-analysis: on a convex quadratic $h(\mathbf{x}) = \tfrac{1}{2}\mathbf{x}^\top\mathbf{Q}\mathbf{x} + \mathbf{x}^\top\mathbf{c} + b$ with $\mathbf{Q} \succ 0$ eigendecomposed as $\mathbf{Q} = \mathbf{O}^\top\boldsymbol{\Lambda}\mathbf{O}$, both plain GD and GD-with-momentum **decompose into coordinate-wise optimization along the eigenvectors of $\mathbf{Q}$**. For each eigendirection $\lambda$:

- **Plain GD**: $x_{t+1} = (1 - \eta\lambda) x_t$ — stable for $|1-\eta\lambda| < 1$, i.e. $0 < \eta\lambda < 2$.
- **GD with momentum**: governed by the $2\times 2$ matrix $\mathbf{R}(\beta, \eta, \lambda)$ — stable for $0 < \eta\lambda < 2 + 2\beta$.

The wider stable range explains why **large $\beta$ is desirable**: it tolerates larger learning rates in well-conditioned directions while damping oscillation in ill-conditioned ones.

## Authors and historical roots

- **[[BorisPolyak]] 1964**: "Some methods of speeding up the convergence of iteration methods" — the heavy-ball method.
- **[[YuriiNesterov]] 1983 / 2018**: [[NesterovMomentum|accelerated gradient]] — optimal $\mathcal{O}(1/T^2)$ convergence rate.
- **Sutskever, Martens, Dahl & Hinton 2013**: "On the importance of initialization and momentum in deep learning" — the empirical case for momentum in DL.

## Practical usage

- **PyTorch**: `torch.optim.SGD(..., momentum=0.9)` — heavy-ball; add `nesterov=True` for NAG.
- **[[Adam]]**: $\mathbf{v}_t$ *is* the first-moment Adam state; $\beta_1 = 0.9$ is the standard momentum.
- **[[RMSProp]] (no momentum) vs Adam (= RMSProp + momentum)**: Adam's first-moment term is essentially classical momentum on top of RMSProp's second-moment scaling.

## Connections

- [[mml-book]] — §7.1.2 (classical treatment).
- [[d2l-optimization]] — §momentum (DL-pragmatic treatment with eigendecomposition analysis).
- [[BorisPolyak]] / [[YuriiNesterov]] — foundational authors.
- [[GradientDescent]] — parent algorithm.
- [[NesterovMomentum]] — accelerated variant.
- [[Adam]] / [[RMSProp]] / [[StochasticGradientDescent]] — descendants / users of the momentum form.
- [[ConditionNumber]] — what momentum mitigates on ill-conditioned objectives.
- [[SaddlePoint]] — momentum carries iterates through zero-gradient saddles.
