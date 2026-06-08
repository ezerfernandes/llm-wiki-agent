---
title: "Michelangelo (Uber ML Platform)"
type: entity
tags: [platform, mlops, feature-store, uber, mlsysbook]
sources: [mlsysbook-ch04-data-engineering, mlsysbook-ch14-ml-operations]
last_updated: 2026-06-05
---

# Michelangelo (Uber ML Platform)

[[Uber]]'s internal end-to-end ML platform, cited in Reddi's *Machine Learning Systems* ([[mlsysbook-ch04-data-engineering|Vol 1, Ch 4]]) as the platform that pioneered the integrated [[FeatureStore|feature store]] to eliminate [[TrainingServingSkew|training-serving skew]].

A study of production ML systems found that **30–40% of initial deployments at Uber suffered from training-serving skew**, motivating Michelangelo's feature store. It established the **dual-interface pattern**: a batch interface for training and a low-latency online interface for serving, both reading from the same precomputed feature values — eliminating the class of silent divergence where training and serving compute features differently.

## Connections

- [[Uber]] — the company that built it (~10K features across teams by 2017).
- [[FeatureStore]] — the dual-store pattern Michelangelo pioneered.
- [[TrainingServingSkew]] / [[TrainingServingConsistency]] — the failure mode it addresses.
- [[mlsysbook-ch04-data-engineering]] — source.
- [[mlsysbook-ch14-ml-operations]] — Ch 14 credits Michelangelo with pioneering the feature store (2017): DSL-defined features served to Hive (train) + Cassandra (serve), 5,000+ features across 100+ teams, point-in-time correctness, near-eliminating skew incidents.

