---
title: "K-Nearest Neighbors"
type: concept
tags: [classical-ml, nonparametric, classification, regression]
sources: [islr-seventh-printing]
last_updated: 2026-05-16
---

# K-Nearest Neighbors (KNN)

Non-parametric predictor: for input $x_0$, find the $K$ training points nearest to $x_0$ and average (regression) or vote (classification). No model assumption; dominates when the true decision boundary is highly non-linear and $n$ is large, but suffers in high dimensions ([[CurseOfDimensionality]]).

## Connections
- [[islr-seventh-printing]] — Ch.2 (intro), Ch.3.5 (regression), Ch.4.6.5 (classification).
- [[CurseOfDimensionality]] — KNN's failure mode in large $p$.
- [[LinearRegression]] — parametric counterpart compared in §3.5.
