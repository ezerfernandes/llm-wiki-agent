---
title: "RMSProp"
type: concept
tags: [optimization, deep-learning]
sources: [d2l-optimization]
last_updated: 2026-05-16
---

# RMSProp

Root Mean Square Propagation — proposed by Tieleman & [[GeoffreyHinton|Hinton]] (2012) in Coursera lecture notes (never formally published as a paper). The simple fix to [[Adagrad]]'s unbounded squared-gradient accumulator: replace the linear sum with an **exponential moving average**, decoupling the rate schedule from coordinate adaptivity.

## The algorithm

$$\begin{aligned}
\mathbf{s}_t &\leftarrow \gamma\,\mathbf{s}_{t-1} + (1-\gamma)\,\mathbf{g}_t^2, \\
\mathbf{x}_t &\leftarrow \mathbf{x}_{t-1} - \frac{\eta}{\sqrt{\mathbf{s}_t + \epsilon}}\odot \mathbf{g}_t.
\end{aligned}$$

Standard hyperparameters: $\gamma = 0.9$ (10-step half-life), $\eta$ as the global learning rate (now schedulable separately), $\epsilon \approx 10^{-6}$.

## Why it fixes Adagrad

Adagrad's $\mathbf{s}_t = \mathbf{s}_{t-1} + \mathbf{g}_t^2$ grows linearly forever, eventually shrinking the effective learning rate to zero regardless of the loss landscape. RMSProp's $\gamma$ caps the effective memory at $\frac{1}{1-\gamma}$ steps (e.g. $\gamma=0.9$ ⇒ ~10 past squared gradients). The accumulator stabilizes around the current gradient variance, so the experimenter can schedule $\eta$ independently of the coordinate scaling ([[d2l-optimization]] §rmsprop).

## Position in the optimizer family

- **vs Adagrad.** Same per-coordinate scaling, leaky accumulator instead of linear.
- **vs Momentum.** Same leaky-average trick — but RMSProp averages the *squared* gradient (a second-moment / preconditioner) where momentum averages the *raw* gradient (a first-moment / direction).
- **vs Adam.** Adam = RMSProp + Momentum + bias correction. RMSProp uses only the second moment; Adam adds the first.

## Connections

- [[d2l-optimization]] — canonical D2L reference (§rmsprop).
- [[GeoffreyHinton]] — RMSProp co-introducer.
- [[Adagrad]] — what RMSProp fixes.
- [[Momentum]] — same leaky-average trick on a different statistic.
- [[Adam]] / [[Adadelta]] — direct descendants.
- [[LearningRateScheduler]] — RMSProp decouples scheduling from coordinate adaptivity, making schedulers more useful.
