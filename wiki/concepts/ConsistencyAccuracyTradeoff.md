---
name: ConsistencyAccuracyTradeoff
title: "Consistency–Accuracy Trade-off"
type: concept
tags: [ux, ml-systems-design, recommender-systems]
sources: [dmls-ch11-human-side]
last_updated: 2026-05-23
---

# Consistency–Accuracy Trade-off

The principle from [[ChipHuyen|Huyen]]'s [[dmls-ch11-human-side|DMLS Ch 11]] that **predictably-consistent ML output can produce better user experience than the accuracy-maximizing prediction** — because consistency is itself a UX property users value.

## Canonical case study
[[BookingCom|Booking.com]] filter recommendation: when a user opens the app twice, the optimal-accuracy recommender will surface slightly different filter suggestions each time based on micro-fluctuations in the user-history features. Users find this disorienting ("the option I just saw is gone"). Booking.com explicitly traded a small accuracy hit for a stable per-user filter set across short time windows.

## Why it matters
Many ML systems implicitly assume that maximizing prediction accuracy maximizes user value. For systems with **repeat user interactions**, this is wrong: users build mental models of the system's behavior, and inconsistency erodes those models faster than accuracy gains repair them. The trade-off has to be made explicit.

## Mitigations
- **Caching predictions per user/session** for repeated identical queries.
- **Hysteresis** on threshold-based decisions (e.g., don't flip a flagged-fraud classification on the same user across short windows).
- **Multi-arm experiments** to measure the actual user-value impact of consistency vs accuracy.

## Sibling concept
[[SpeedAccuracyTradeoff]] — the other major UX trade-off Ch 11 enumerates; mitigated by [[SmoothFailing|smooth failing]] to a [[BackupModel|backup model]] past a latency budget.

## Connections
- [[ResponsibleAI]] — Ch 11 frames UX trade-offs as part of responsible deployment.
- [[BookingCom]] — the canonical case study.
- [[RecommenderSystems]] — most affected domain.
- [[ABTesting]] — the operational tool to measure trade-off impact.
