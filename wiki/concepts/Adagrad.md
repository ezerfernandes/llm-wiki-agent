---
title: "Adagrad"
type: concept
tags: [optimization, deep-learning]
sources: [d2l-optimization]
last_updated: 2026-05-16
---

# Adagrad

Adaptive subgradient method ([[JohnDuchi|Duchi]], Hazan & Singer 2011, JMLR) — the first widely-used **per-coordinate adaptive learning rate** algorithm. Treats accumulated squared gradients as a cheap proxy for the diagonal of the [[Hessian]], yielding automatic per-feature [[Preconditioning|preconditioning]] without forming the second-derivative matrix.

## The algorithm

Initialize $\mathbf{s}_0 = \mathbf{0}$; at each step:

$$\begin{aligned}
\mathbf{g}_t &= \partial_{\mathbf{w}}\, \ell(y_t, f(\mathbf{x}_t, \mathbf{w})), \\
\mathbf{s}_t &= \mathbf{s}_{t-1} + \mathbf{g}_t^2, \\
\mathbf{w}_t &= \mathbf{w}_{t-1} - \frac{\eta}{\sqrt{\mathbf{s}_t + \epsilon}}\odot \mathbf{g}_t.
\end{aligned}$$

All operations are **coordinate-wise** ($\mathbf{g}_t^2$ has entries $g_{t,i}^2$, etc.). $\epsilon \approx 10^{-6}$ guards against division by zero.

## Why it works

- **Per-coordinate scaling.** Coordinates with consistently large gradients accumulate large $\mathbf{s}_t$ and get *smaller* effective learning rates; coordinates with rarely-large gradients (sparse features) retain near-original $\eta$. This is exactly diagonal preconditioning.
- **Cheap Hessian proxy.** Computing $\textrm{diag}(\nabla^2 f)$ is infeasible for DL ($\mathcal{O}(d^2)$ storage). Adagrad uses *gradient* magnitudes as a stand-in — at optimality the gradient variance still encodes Hessian scale, so this works ([[d2l-optimization]] §adagrad).
- **Sparse features.** Critical for language models / collaborative filtering / computational advertising where rare words / users only update their parameters occasionally and need *not* to have their learning rate decay alongside frequent features.

## The drawback

$\mathbf{s}_t$ grows monotonically — essentially **linearly** with $t$. This forces the effective per-coordinate learning rate to decay at $\mathcal{O}(t^{-1/2})$. Fine for *convex* problems (and provably optimal for them); typically **too aggressive** for nonconvex DL where one wants slower decay. Motivates [[RMSProp]] (leaky-average replacement for $\mathbf{s}_t$) and [[Adadelta]] (no global learning rate).

## Connections

- [[d2l-optimization]] — canonical D2L reference (§adagrad).
- [[JohnDuchi]] — Adagrad lead author.
- [[Preconditioning]] / [[Hessian]] — Adagrad's theoretical foundation.
- [[RMSProp]] — fixes the unbounded accumulator with a leaky average.
- [[Adadelta]] — further removes the global learning rate.
- [[Adam]] — combines Adagrad-style second-moment scaling with [[Momentum]] + bias correction.
- [[StochasticGradientDescent]] / [[MinibatchSGD]] — the underlying gradient method.
