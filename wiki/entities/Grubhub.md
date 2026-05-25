---
name: Grubhub
title: "Grubhub"
type: entity
tags: [company, food-delivery, ml-case-study]
sources: [dmls-ch07-model-deployment, dmls-ch09-continual-learning]
last_updated: 2026-05-23
---

# Grubhub

US food-delivery marketplace. Cited extensively in [[ChipHuyen|Huyen]]'s *Designing Machine Learning Systems* (2022) as a canonical case study for two production-ML patterns:

## DMLS Ch 7 case study — request-density counterexample to "batch is always cheaper"
Grubhub has ~31M users and serves ~622K orders/day → only ~2% of users place an order on any given day. Huyen uses Grubhub as the counterexample to the lazy assumption that [[BatchInference|batch prediction]] is always cheaper than [[OnlineInference|online prediction]]: pre-computing recommendations for the 98% of users who won't visit today is wasteful. The right pattern in low-request-density domains is **online prediction with streaming features**, not batch.

## DMLS Ch 9 case study — stateful training compute win
Grubhub reported a **45× compute reduction and 20% click-through-rate (PTR) lift** by switching from [[StatelessRetraining|stateless daily retraining]] to [[StatefulTraining|stateful incremental training]] (fine-tuning from the previous day's checkpoint on fresh data only). Cited as the canonical motivation for moving up Huyen's continual-learning maturity ladder.

## Connections
- [[ChipHuyen]] — DMLS author who anchored the case studies.
- [[BatchInference]] / [[OnlineInference]] / [[StreamingPrediction]] — three modes whose trade-offs Grubhub illustrates.
- [[StatefulTraining]] / [[StatelessRetraining]] — the retraining-mode choice Grubhub publicized.
- [[ContinualLearning]] — the broader discipline.
- [[CTRPrediction]] — the modeled task.
