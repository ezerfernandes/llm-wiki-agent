---
name: SmoothFailing
title: "Smooth Failing"
type: concept
tags: [ux, ml-systems-design, latency, fallback]
sources: [dmls-ch11-human-side]
last_updated: 2026-05-23
---

# Smooth Failing

UX pattern from [[ChipHuyen|Huyen]]'s [[dmls-ch11-human-side|DMLS Ch 11]]: when a request to the main (accurate but slow) ML model exceeds a latency budget, **route it to a fast [[BackupModel|backup model]]** (heuristic, cache, or simpler model) rather than wait or fail. The user gets a slightly-less-accurate answer in time rather than a timeout or a hung UI.

## Why
The [[SpeedAccuracyTradeoff|speed–accuracy trade-off]] is real but not uniform across requests. Most requests should hit the main model and benefit from its accuracy; the long-tail slow requests should fall back. Smooth failing operationalizes that asymmetry without rewriting the model or sacrificing average accuracy.

## Typical fallback choices
- **Cached recent predictions** for the same input or a similar input.
- **A simpler in-process model** (linear classifier, decision tree) deployed alongside the main model.
- **A heuristic** ("when in doubt, recommend the most popular item").
- **The mean / median / mode** prediction of the main model's training distribution.

## When to apply
- Online prediction with hard latency SLAs (search, ad ranking, real-time recommendation).
- Mobile / edge deployment where slow network round-trips push some requests over budget.
- Systems where degraded responses are clearly better than timeout (in contrast: medical diagnosis, where a wrong fast answer is worse than no answer).

## Related patterns
- [[CircuitBreaker|Circuit breaker]] — the operational engineering pattern smooth failing borrows from.
- [[ChampionChallengerPattern]] — runs main + alternative; smooth failing is the latency-side variant.
- [[ShadowDeployment]] — runs main + alternative for evaluation, not fallback.

## Connections
- [[BackupModel]] — the artifact smooth failing requires.
- [[SpeedAccuracyTradeoff]] — the trade-off smooth failing addresses.
- [[Latency]] / [[InferenceOptimization]] — operational substrate.
- [[ResponsibleAI]] — Ch 11 frames smooth failing as part of UX trade-off discipline.
