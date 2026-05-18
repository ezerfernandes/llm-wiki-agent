---
title: "Black-Box Shift Detection"
type: concept
tags: [drift, monitoring, evaluation]
sources: []
last_updated: 2026-05-15
---

# Black-Box Shift Detection

Detecting [[DataDrift]] or [[ConceptDrift]] using only the model's outputs (predictions, confidence) without inspecting its internals. Useful when raw features are sensitive or the model is third-party; pairs with [[ImportanceWeighting]] for correction and [[KolmogorovSmirnovTest]] for statistical comparison.
