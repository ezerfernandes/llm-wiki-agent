---
title: "Concept Drift"
type: concept
tags: [drift, monitoring, mlops]
sources: []
last_updated: 2026-05-15
---

# Concept Drift

A shift in the conditional distribution P(y|x) over time — the relationship between inputs and labels itself changes, even if feature distributions stay constant. Detected via [[BlackBoxShiftDetection]] or label-aware monitoring; contrast with [[DataDrift]] which moves P(x).
