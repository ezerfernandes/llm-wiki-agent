---
title: "Kolmogorov-Smirnov Test"
type: concept
tags: [statistics, drift]
sources: [mlsysbook-ch03-ml-workflow]
last_updated: 2026-06-05
---

# Kolmogorov-Smirnov Test

A nonparametric test comparing two empirical distributions by the maximum gap between their CDFs ($\mathcal{O}(n \log n)$). Common signal for [[DataDrift]] on continuous features; paired with [[ChiSquaredTest]] for categorical features in [[DataObservability]] dashboards.

Reddi's *Machine Learning Systems* ([[mlsysbook-ch03-ml-workflow|Vol 1, Ch 3]]) pairs the KS test with the [[PopulationStabilityIndex|Population Stability Index]] as the two lightweight, real-time drift detectors in the production [[DiabeticRetinopathyScreening|DR]] monitoring stack (alert if $p < 0.01$) — cheap enough to act as early-warning systems before accuracy degrades.
