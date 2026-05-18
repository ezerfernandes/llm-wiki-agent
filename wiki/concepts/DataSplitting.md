---
title: "Data Splitting"
type: concept
tags: [data, evaluation, ml-engineering]
sources: []
last_updated: 2026-05-15
---

# Data Splitting

Partitioning a [[Dataset]] into train, validation, and test (or [[HoldoutDataset]]) subsets so model selection and final evaluation do not see the same examples. Mishandling (random split on time-series data, leakage across groups) is a leading cause of [[DataLeakage]] and miscalibrated [[Generalization]] estimates.
