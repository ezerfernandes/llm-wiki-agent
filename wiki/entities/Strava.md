---
name: Strava
title: "Strava"
type: entity
tags: [company, fitness, privacy, ai-failure-case-study]
sources: [dmls-ch11-human-side]
last_updated: 2026-05-23
---

# Strava

US fitness-tracking app. Subject of the **[[StravaHeatmap|2018 global heatmap incident]]** — the canonical "anonymization is not enough" case study in [[ChipHuyen|Huyen]]'s [[dmls-ch11-human-side|DMLS Ch 11]].

## The 2018 incident
Strava published an aggregated "global heatmap" visualizing user-generated activity tracks worldwide. Each individual track was anonymized; the aggregate was meant to be privacy-safe. Result:
- **Military base locations were exposed** in conflict zones where the only Strava users were US/coalition soldiers running PT routes.
- The aggregate-level patterns revealed information no individual track did.
- Triggered policy reviews at US DoD and similar bodies; Strava added an opt-out.

## Why DMLS treats it as the canonical privacy example
The incident is the clean refutation of the engineering assumption that "anonymized + aggregated = safe." Per Huyen's Ch 11 [[ResponsibleAI|Responsible AI]] framework:
- [[PIIAnonymization|PII anonymization]] alone is insufficient when aggregate patterns can re-identify subgroups.
- [[DifferentialPrivacy|Differential privacy]] is the formal mechanism that addresses this, with its own [[PrivacyAccuracyTradeoff|accuracy trade-off]] that's non-uniform across subgroups.
- [[OptInVsOptOut|Opt-in vs opt-out]] data collection defaults are a core governance lever; Strava's pre-incident default was opt-in to heatmap, but most users didn't know.

## Connections
- [[StravaHeatmap]] — the incident specifically.
- [[ResponsibleAI]] — Ch 11 framework.
- [[PIIAnonymization]] — what the incident disproved.
- [[DifferentialPrivacy]] — the formal alternative.
- [[OptInVsOptOut]] — the governance lever.
- [[AIIncidentDatabase]] — public registry where this incident is logged.
