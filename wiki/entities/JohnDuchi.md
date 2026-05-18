---
title: "John Duchi"
type: entity
tags: [person, researcher, optimization, statistics]
sources: [d2l-optimization]
last_updated: 2026-05-16
---

# John C. Duchi

American statistician and machine-learning researcher; [[stanforduniversity|Stanford]] professor. Lead author of **[[Adagrad]]** (Duchi, Hazan & Singer 2011, "Adaptive Subgradient Methods for Online Learning and Stochastic Optimization", JMLR) — the per-coordinate adaptive-learning-rate algorithm that pioneered the family from which [[RMSProp]] / [[Adadelta]] / [[Adam]] descend.

## Why he matters here

- **Adagrad (2011).** $\mathbf{s}_t = \mathbf{s}_{t-1}+\mathbf{g}_t^2$, $\mathbf{x}_t = \mathbf{x}_{t-1}-\frac{\eta}{\sqrt{\mathbf{s}_t+\epsilon}}\mathbf{g}_t$ — particularly effective for sparse features ([[d2l-optimization]] §adagrad). Established the per-coordinate-adaptive-rate paradigm.

## Affiliations

- [[stanforduniversity|Stanford University]] — Statistics + EE.

## Connections

- [[d2l-optimization]] — cites Duchi, Hazan & Singer 2011 as Adagrad's origin.
- [[Adagrad]] — flagship contribution.
- [[RMSProp]] / [[Adadelta]] / [[Adam]] — descendants of Adagrad's per-coordinate scaling.
