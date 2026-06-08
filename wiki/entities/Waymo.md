---
title: "Waymo"
type: entity
tags: [company, autonomous-vehicles, deployment-case-study, mlsysbook]
sources: [mlsysbook-ch01-introduction]
last_updated: 2026-06-05
---

# Waymo

Alphabet's autonomous-vehicle division, operating a fleet of self-driving taxis. In Reddi's *Machine Learning Systems* ([[mlsysbook-ch01-introduction|Ch 1]]) Waymo is the **high-stakes hybrid** deployment case study: on-vehicle perception runs at the [[EdgeML|edge]] with **<10 ms latency** while massive cloud infrastructure trains on **petabytes** of driving data.

Each vehicle is a "roving data center" processing **1–2+ TB/hour** across LiDAR, radar, and cameras. Its binding constraints are **safety-critical latency** and **data freshness**: the deployed model must be frozen for safety certification while the cloud continuously trains improved versions, creating a version gap that demands rigorous regression testing before any OTA update. Radar (~77 GHz, all-weather) compensates for camera failure in rain/fog. Models trained on sunny Phoenix roads may fail in New York snowstorms — a [[DistributionShift|distribution-shift]] hazard.

## Connections

- [[mlsysbook-ch01-introduction]] — the case-study source.
- [[FarmBeats]] / [[AlphaFold]] — the other two deployment case studies.
- [[EdgeML]] / [[DeploymentSpectrum]] — its hybrid deployment pattern.
- [[DistributionShift]] / [[SilentDegradation]] — its operational risks.
- [[google|Alphabet/Google]] — parent.
