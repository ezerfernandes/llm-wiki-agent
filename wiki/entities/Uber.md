---
name: Uber
title: "Uber"
type: entity
tags: [company, ride-sharing, ml-platform]
sources: [dmls-ch03-data-engineering, dmls-ch07-model-deployment, dmls-ch10-infrastructure-mlops]
last_updated: 2026-05-23
---

# Uber

US ride-sharing and delivery company. Featured in [[ChipHuyen|Huyen]]'s *Designing ML Systems* as a primary example of an organization running thousands of ML models in production.

## Key DMLS data points
- **~10K features across teams by 2017** (DMLS Ch 10) — the feature-store motivating data point; [[Uber]]'s [[MichelangeloPlatform|Michelangelo]] ML platform was built specifically to manage feature reuse at that scale.
- **Tens of TB/day to the data lake by 2018** (DMLS Ch 10).
- **Three-services microservices example** (DMLS Ch 3) — driver-management + ride-management + price-optimization as a canonical microservices ML architecture.
- **Unified [[ApacheFlink|Flink]] batch + stream pipeline** (DMLS Ch 3, Ch 7) — Uber is the canonical example of using a single streaming engine for both batch and streaming feature computation.
- **[[Ludwig]]** — Uber's declarative ML framework (specify data + max_models, get an AutoML leaderboard).

## Connections
- [[ChipHuyen]] — DMLS author who anchored the Uber case studies.
- [[MichelangeloPlatform]] — Uber's internal ML platform.
- [[ApacheFlink]] — Uber's unified-pipeline streaming engine.
- [[Ludwig]] — Uber's declarative ML framework.
- [[FeatureStore]] — Michelangelo was an early industrial feature store.
- [[MLPlatform]] — the canonical reference implementation.
