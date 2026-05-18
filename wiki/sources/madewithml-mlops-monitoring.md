---
title: "Made With ML — Monitoring Machine Learning Systems"
type: source
tags: [mlops, made-with-ml, monitoring, drift-detection, observability, course]
date: 2026-05-15
source_file: raw/madewithml/mlops-monitoring.md
---

## Summary
Comprehensive Made With ML lesson on monitoring deployed ML systems. Layers monitoring as: (1) system health (latency, throughput, CPU/GPU utilization via [[Grafana]] / [[Datadog]]), (2) sliding-window performance metrics against a threshold, (3) handling delayed ground-truth via approximate signals or labeled subsets, (4) [[ImportanceWeighting]] when no outcomes are available (Mandoline-style slice matrices), and (5) drift detection across three flavors: data drift `P(X)`, target drift `P(y)`, and concept drift `P(y|X)`. Walks through univariate tests (Kolmogorov-Smirnov, chi-squared) using `alibi-detect`, multivariate drift via dimensionality reduction (PCA, autoencoders, BBSD) plus Maximum Mean Discrepancy, and online detectors (`MMDDriftOnline`). Closes with outlier detection (OutlierVAE), alerting workflows, root-cause analysis, and managed/open-source monitoring platforms.

## Key Claims
- Cumulative metrics hide performance degradation; sliding-window metrics catch it sooner — same hourly F1 stream gave 93.7 cumulative vs 88.6 sliding on the last day.
- Three drift entities to monitor: inputs (`P(X)` → data drift / covariate shift), outputs (`P(y)` → target drift / label shift), and the input-output relation (`P(y|X)` → concept drift). All three can co-occur.
- Same-source feature retrieval at train and serve time (i.e. a [[FeatureStore]]) eliminates training-serving skew so monitoring can focus on real distribution shift.
- The "reduce-then-measure" pattern from *Failing Loudly* is the canonical approach for high-dimensional drift detection: PCA / untrained autoencoders / BBSD reduce to ~32 dims, then KS or MMD operates in the reduced space.
- ↓ p-value = ↑ confidence that distributions differ; KS handles continuous features, chi-squared handles categorical, MMD handles multivariate via kernel embeddings.
- Online drift detection needs a fixed reference window and a sliding test window; smaller test windows catch sudden drift faster, larger test windows catch gradual drift — monitor several sizes in parallel.
- Outlier detection is unsupervised and typically streaming ([[PyOD]], [[AlibiDetect]], [[WhyLogs]]); a group of non-anomalous points can still drift a distribution.
- Alerting must include enough context (triggered alert, thresholds, drift test, reference/test windows, logs) for **root-cause analysis (RCA)** — many alerts often share one underlying cause.
- Acting on drift ≠ always retraining: first verify expectations, check schema, then choose between retraining, reweighting the reference window, or treating outliers as valid signal.

## Key Quotes
> "If we wait to catch the model decay based on the performance, it may have already caused significant damage to downstream business pipelines that are dependent on it."

> "As data starts to drift, we may not yet notice significant decay in our model's performance, especially if the model is able to interpolate well. However, this is a great opportunity to potentially retrain before the drift starts to impact performance."

> "Detecting drift on multivariate text embeddings is still quite difficult so it's typically more common to use these methods applied to tabular features or images."

## Connections
- [[GokuMohandas]] — author.
- [[MadeWithML]] — parent course.
- [[ModelMonitoring]] — umbrella concept.
- [[DataDrift]] — `P(X) ≠ P_ref(X)`.
- [[TargetDrift]] — `P(y) ≠ P_ref(y)`.
- [[ConceptDrift]] — `P(y|X) ≠ P_ref(y|X)`.
- [[TrainingServingSkew]] — failure mode the FeatureStore pattern addresses.
- [[FeatureStore]] — single source of truth across train/serve.
- [[KolmogorovSmirnovTest]] — univariate continuous drift test.
- [[ChiSquaredTest]] — univariate categorical drift test.
- [[MaximumMeanDiscrepancy]] — kernel-based multivariate drift test.
- [[ImportanceWeighting]] — Mandoline approach when labels are unavailable.
- [[AlibiDetect]] / [[WhyLogs]] / [[PyOD]] / [[EvidentlyAI]] / [[TorchDrift]] — drift/outlier libraries.
- [[GreatExpectations]] — rule-based expectations on production data.
- [[Grafana]] / [[Datadog]] — system-health dashboards.
- [[PrincipalComponentAnalysis]] / [[Autoencoder]] / [[BlackBoxShiftDetection]] — dimensionality reduction for multivariate drift.
- [[RootCauseAnalysis]] — required follow-up on alerts.
- [[ApacheKafka]] / [[ApacheFlink]] / [[KNative]] — streaming substrates for production monitoring.

## Contradictions
None internal. Adds the missing trigger to `madewithml-mlops-cicd`: a drift alert is the natural event that should kick off a new `workloads` CI run.
