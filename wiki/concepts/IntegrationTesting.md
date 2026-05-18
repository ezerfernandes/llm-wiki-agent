---
title: "Integration Testing"
type: concept
tags: [testing, software-engineering]
sources: []
last_updated: 2026-05-15
---

# Integration Testing

Exercising multiple components together (model + preprocessor + API + DB) to surface contract bugs that unit tests miss. Anchored by [[ArrangeActAssert]] structure and run in [[CICD]]; for ML, often the right level to catch training/serving skew and [[FeatureStore]] drift.
