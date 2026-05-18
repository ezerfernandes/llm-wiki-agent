---
title: "Adadelta"
type: concept
tags: [optimization, deep-learning]
sources: [d2l-optimization]
last_updated: 2026-05-16
---

# Adadelta

[[MatthewZeiler|Zeiler]] 2012 — an [[Adagrad]] variant that **has no global learning rate**. Instead of a single $\eta$, it uses a leaky-average estimate of past *parameter changes* as the unit-matching numerator, while keeping a [[RMSProp]]-style leaky second-moment of gradients in the denominator.

## The algorithm

Two state variables per parameter: $\mathbf{s}_t$ (leaky avg of squared gradient) and $\Delta\mathbf{x}_t$ (leaky avg of squared parameter change).

$$\begin{aligned}
\mathbf{s}_t &= \rho\,\mathbf{s}_{t-1} + (1-\rho)\,\mathbf{g}_t^2, \\
\mathbf{g}'_t &= \frac{\sqrt{\Delta\mathbf{x}_{t-1} + \epsilon}}{\sqrt{\mathbf{s}_t + \epsilon}}\odot \mathbf{g}_t, \\
\mathbf{x}_t &= \mathbf{x}_{t-1} - \mathbf{g}'_t, \\
\Delta\mathbf{x}_t &= \rho\,\Delta\mathbf{x}_{t-1} + (1-\rho)\,(\mathbf{g}'_t)^2.
\end{aligned}$$

Standard hyperparameters: $\rho = 0.9$ (half-life 10), $\epsilon \approx 10^{-5}$. Initialize $\mathbf{s}_0 = \Delta\mathbf{x}_0 = \mathbf{0}$.

## Why no learning rate

The numerator $\sqrt{\Delta\mathbf{x}_{t-1}+\epsilon}$ has the same units as the parameter $\mathbf{x}$ (whereas $\sqrt{\mathbf{s}_t}$ has units of the gradient). Dividing one by the other yields a *unit-matching* rescaling factor — the algorithm self-calibrates the step size from the magnitude of recent updates. No $\eta$ to tune ([[d2l-optimization]] §adadelta).

In practice the framework defaults often *re-introduce* a learning rate (e.g. TensorFlow's `Adadelta` defaults to `learning_rate=0.001`) because pure Adadelta does not always converge fast enough on DL problems.

## Connections

- [[d2l-optimization]] — canonical D2L reference (§adadelta).
- [[MatthewZeiler]] — author.
- [[Adagrad]] / [[RMSProp]] — the family Adadelta extends.
- [[Adam]] — sibling per-coordinate adaptive optimizer with bias correction instead of unit-matching.
