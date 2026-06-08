---
title: "TensorFlow Extended (TFX)"
type: concept
tags: [mlops, pipelines, tensorflow, cicd]
sources: [mlsysbook-ch14-ml-operations]
last_updated: 2026-06-05
---

# TensorFlow Extended (TFX)

[[Google]]'s production ML pipeline platform, which productionized the patterns powering Search, Ads, and YouTube recommendations after teams kept rebuilding bespoke pipelines with inconsistent approaches. Core components: **ExampleGen** (ingest/split), **StatisticsGen + SchemaGen** (infer statistics/schema), **ExampleValidator** (detect [[TrainingServingSkew|training-serving skew]] and anomalies), **Transform** (consistent feature engineering for train + serve), **Trainer**, **Evaluator** (validation vs baseline with sliced metrics), **Pusher** (conditional deployment gates).

TFX enforces that every pipeline step produces artifacts with metadata, enabling full lineage from raw data to deployed model. Cited in [[mlsysbook-ch14-ml-operations]] as an exemplar of how shared pipeline components reduce glue code and [[TechnicalDebt|technical debt]] (Google Play case study).

## Connections
- [[CICD]] / [[ContinuousTraining]] — TFX implements ML CI/CD at scale.
- [[TrainingServingSkew]] — ExampleValidator/Transform address it directly.
- [[GreatExpectations]] — alternative for data-validation tests.
- [[Google]] — origin and operator.
- [[MLOps]] — development-infrastructure tooling.
- [[mlsysbook-ch14-ml-operations]] — source chapter.
