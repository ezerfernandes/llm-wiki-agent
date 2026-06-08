---
title: "Optum"
type: entity
tags: [responsible-ai, fairness, case-study, healthcare]
sources: [mlsysbook-ch15-responsible-engineering]
last_updated: 2026-06-05
---

# Optum

Optum is the health-services arm of UnitedHealth Group whose patient risk-stratification algorithm is the canonical **proxy-variable** fairness case study in [[mlsysbook-ch15-responsible-engineering|mlsysbook Vol 1 Ch 15]] (Obermeyer et al. 2019, ~50K patients).

## Why it matters here
- The algorithm predicted **future cost** as a proxy for **future need**. Because the US health system spends less on Black patients at equal illness, Black patients received lower risk scores at equal disease burden — a bias inherited from the proxy, not the code.
- Reformulating the target to predict illness markers directly raised the share of Black patients flagged for high-risk care management from **17.7% → 46.5%**.
- The chapter's lesson: "Optimizing for a proxy inherits the biases of the system that generated the proxy" — the proxy-target relationship must be audited across every demographic subgroup.

## Connections
- [[ProxyVariable]] — the failure mechanism this case defines.
- [[AlgorithmicBias]] / [[DisparateImpact]] — the resulting harm.
- [[ZiadObermeyer]] — lead author of the 2019 audit.
- [[DAMTaxonomy]] — an Algorithm-axis (proxy objective) failure.
- [[mlsysbook-ch15-responsible-engineering]] — source.
