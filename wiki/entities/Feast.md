---
name: Feast
title: "Feast"
type: entity
tags: [tool, feature-store, mlops, open-source]
sources: [mlsysbook-ch14-ml-operations]
last_updated: 2026-06-05
---

# Feast

An open-source [[FeatureStore|feature store]] inspired by [[Uber]]'s [[MichelangeloPlatform|Michelangelo]]. It provides unified feature retrieval for both historical (training) and online (serving) access through a single set of feature definitions, eliminating the divergent code paths that cause [[TrainingServingSkew|training-serving skew]]. In [[mlsysbook-ch14-ml-operations]] (mlsysbook Vol 1, Ch 14) it is the worked example: `fs.get_historical_features(...)` for point-in-time-correct training data and `fs.get_online_features(...)` for serving, guaranteeing identical computation logic and reducing accuracy degradation by 5–15%.

## Connections
- [[FeatureStore]] — the concept Feast implements.
- [[TrainingServingSkew]] / [[TrainingServingConsistency]] — what it prevents.
- [[MichelangeloPlatform]] — the Uber platform that inspired it.
- [[Tecton]] — commercial feature-store counterpart.
- [[MLOps]] — development-infrastructure tooling.
- [[mlsysbook-ch14-ml-operations]] — source chapter.
