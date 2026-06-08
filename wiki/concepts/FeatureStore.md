---
title: "Feature Store"
type: concept
tags: [mlops, data, infrastructure]
sources: [mlsysbook-ch04-data-engineering, mlsysbook-ch14-ml-operations]
last_updated: 2026-06-05
---

# Feature Store

A centralized system (Feast, Tecton, Vertex FS) that materializes [[FeatureEngineering]] outputs once and serves them to both training and online inference, eliminating train/serve skew. Provides versioning, freshness SLAs, and discovery; integrates with [[DataPipeline]] and [[ExperimentTracking]].

Reddi's *Machine Learning Systems* ([[mlsysbook-ch04-data-engineering|Vol 1, Ch 4]]) defines the feature store as a **transformation engine** that stores the feature *logic*, not just data, decoupling computation from consumption. It enforces point-in-time correctness ($x_{t-\Delta}$ computed identically to $x_t$), eliminating [[TrainingServingSkew|training-serving skew]] by design. Two storage modes: an **offline store** (columnar/[[Parquet]], batch training) and an **online store** (key-value/Redis, single-digit-ms serving). Uber found **30–40% of initial deployments suffered training-serving skew**, motivating [[MichelangeloPlatform|Michelangelo]]'s feature store and its dual-interface pattern. Under [[CAPTheorem|CAP]], a feature store must choose CP (consistent but partition-fragile) or AP (available but stale-risking).

## Connections

- [[TrainingServingSkew]] / [[TrainingServingConsistency]] — the failure mode it eliminates.
- [[MichelangeloPlatform]] — Uber's platform that pioneered the dual-store pattern.
- [[FeatureEngineering]] — what the store materializes consistently.
- [[CAPTheorem]] — the CP-vs-AP trade-off.
- [[Parquet]] / [[ColumnarStorage]] — the offline-store format.
- [[mlsysbook-ch04-data-engineering]] — source.
- [[mlsysbook-ch14-ml-operations]] — mlsysbook Vol 1 Ch 14 frames the feature store as the mechanism enforcing the consistency imperative, eliminating 5–15% training-serving-skew accuracy loss (Uber Michelangelo, Feast).

