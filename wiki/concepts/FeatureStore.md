---
title: "Feature Store"
type: concept
tags: [mlops, data, infrastructure]
sources: []
last_updated: 2026-05-15
---

# Feature Store

A centralized system (Feast, Tecton, Vertex FS) that materializes [[FeatureEngineering]] outputs once and serves them to both training and online inference, eliminating train/serve skew. Provides versioning, freshness SLAs, and discovery; integrates with [[DataPipeline]] and [[ExperimentTracking]].
