---
title: "Standardization"
type: concept
tags: [preprocessing, features]
sources: [madewithml-preprocessing]
last_updated: 2026-05-15
---

# Standardization

Rescaling features to zero mean and unit variance. Stabilizes optimization for [[NeuralNetwork]] and distance-based models; computed on train and applied identically to val/test in a [[TrainValTestSplit]].
