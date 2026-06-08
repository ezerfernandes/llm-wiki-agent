---
title: "Data Drift"
type: concept
tags: [drift, monitoring, mlops]
sources: [mlsysbook-ch03-ml-workflow, mlsysbook-ch04-data-engineering, mlsysbook-ch14-ml-operations]
last_updated: 2026-06-05
---

# Data Drift

A shift in the input distribution P(x) over time — production features no longer match training-time statistics. Detected with the [[KolmogorovSmirnovTest]], [[PopulationStabilityIndex]], [[ChiSquaredTest]], or [[BlackBoxShiftDetection]]; mitigated by retraining and [[ImportanceWeighting]]. Distinct from [[ConceptDrift]] which moves P(y|x).

In Reddi's *Machine Learning Systems* ([[mlsysbook-ch03-ml-workflow|Vol 1, Ch 3]]), data (covariate) drift is the mechanism of **silent degradation**: a [[DiabeticRetinopathyScreening|DR model]] lost 8% sensitivity after a clinic upgraded to sharper cameras — no code changed, the pixel distribution simply drifted beyond the training envelope. This is why deployment is the *beginning* of the [[MachineLearningLifecycle|lifecycle]], not the end.

The data-engineering chapter ([[mlsysbook-ch04-data-engineering|Vol 1, Ch 4]]) makes drift detection a core responsibility (30–40% of ongoing ML-ops effort) and gives the full taxonomy: [[CovariateShift|covariate shift]] (P(x) changes), [[LabelShift|label shift]] (P(y) changes), [[ConceptDrift|concept drift]] (P(y∣x) changes), plus a fourth meta-level **label-quality drift** (annotation reliability degrades while data is stable — invisible to feature monitoring, detected via [[CohensKappa|Cohen's κ]]). It operationalizes the degradation equation's divergence term $\mathcal{D}(P_t \lVert P_0)$ via [[PopulationStabilityIndex|PSI]] (>0.2) and [[KullbackLeiblerDivergence|KL divergence]].
