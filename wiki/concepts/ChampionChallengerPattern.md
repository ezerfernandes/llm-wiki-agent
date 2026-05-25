---
name: ChampionChallengerPattern
title: "Champion-Challenger Pattern"
type: concept
tags: [continual-learning, test-in-production, deployment]
sources: [dmls-ch09-continual-learning]
last_updated: 2026-05-23
---

# Champion-Challenger Pattern

Continual-learning deployment workflow in which a **candidate replica** ("challenger") of the existing production model ("champion") is trained on fresh data and **evaluated alongside** the champion before any promotion. Only after the challenger meets evaluation criteria is it promoted to production; otherwise it's discarded and the champion stays. Per [[ChipHuyen|Huyen]]'s [[dmls-ch09-continual-learning|DMLS Ch 9]] this is the **standard** continual-learning workflow.

## Why
Continual learning means models update frequently. Without a champion-challenger gate, every retraining can degrade production performance silently. The pattern enforces a safety contract: **no update goes live without an explicit comparison to the version it replaces**.

## Sibling patterns
- [[ShadowDeployment]] — the challenger sees real production traffic but its predictions don't affect users.
- [[ABTesting]] — challenger sees a fraction of traffic; user-side impact measured statistically.
- [[CanaryDeployment]] — challenger rolls out gradually.
- [[InterleavingExperiments]] — challenger and champion contribute to a single mixed ranking that the user sees.

## Evaluation criteria
Usually combines:
- **Offline metrics** ([[Backtest|backtests]] on recent past data).
- **Online metrics from a shadow / canary phase** (per-prediction outcome, latency, error rate).
- **Business / user metrics** (CTR, conversion, watch-time) from a small A/B slice.

## Connections
- [[ContinualLearning]] — the workflow this pattern protects.
- [[ShadowDeployment]] / [[ABTesting]] / [[CanaryDeployment]] / [[InterleavingExperiments]] — the test-in-production techniques the pattern composes.
- [[ModelRegistry]] — the lookup/promotion layer the pattern manipulates.
- [[Monitoring]] — the runtime substrate that surfaces the comparison metrics.
