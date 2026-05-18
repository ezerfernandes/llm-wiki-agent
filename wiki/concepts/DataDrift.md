---
title: "Data Drift"
type: concept
tags: [drift, monitoring, mlops]
sources: []
last_updated: 2026-05-15
---

# Data Drift

A shift in the input distribution P(x) over time — production features no longer match training-time statistics. Detected with the [[KolmogorovSmirnovTest]], [[ChiSquaredTest]], or [[BlackBoxShiftDetection]]; mitigated by retraining and [[ImportanceWeighting]]. Distinct from [[ConceptDrift]] which moves P(y|x).
