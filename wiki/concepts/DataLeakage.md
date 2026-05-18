---
title: "Data Leakage"
type: concept
tags: [data, evaluation, pitfalls]
sources: []
last_updated: 2026-05-15
---

# Data Leakage

When information from outside the training set (test labels, future data, target-derived features) inadvertently enters training, inflating offline metrics and collapsing in production. Prevented via disciplined [[DataSplitting]], time-aware folds, and careful [[FeatureEngineering]] inside a [[FeatureStore]] boundary.
