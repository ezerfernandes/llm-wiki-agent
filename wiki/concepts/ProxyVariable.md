---
name: ProxyVariable
title: "Proxy Variable"
type: concept
tags: [responsible-ai, fairness, bias, data]
sources: [mlsysbook-ch15-responsible-engineering]
last_updated: 2026-06-05
---

# Proxy Variable

A feature that correlates with a protected attribute (or with the true target) without directly encoding it. Per [[mlsysbook-ch15-responsible-engineering|mlsysbook Vol 1 Ch 15]], proxies are the reason removing protected attributes does not eliminate [[AlgorithmicBias|bias]]: "other correlated features carry the same signal."

## Two failure patterns
1. **Proxy for a protected attribute** — ZIP code ↔ race (residential segregation), first names ↔ gender/ethnicity, healthcare utilization ↔ socioeconomic status. [[Amazon]]'s recruiting tool reconstructed gender from college names, activity descriptions, and career gaps despite explicit gender removal. Models recover protected attributes at **70–90% accuracy** from "neutral" features. The result — discriminating while appearing compliant — is **fairness laundering**.
2. **Proxy for the target** — optimizing a measurable stand-in for an unobservable goal inherits the biases of the system that generated it. The Optum healthcare algorithm (Obermeyer et al. 2019) used *cost* as a proxy for *need*; because the US system spends less on Black patients at equal illness, reformulating to predict illness directly raised Black-patient enrollment from **17.7% → 46.5%**. This is the [[GoodhartsLaw|Goodhart's Law]] mechanism applied to fairness.

## Defense
Continuous per-group outcome monitoring is "the only reliable defense"; feature removal without causal analysis creates false confidence.

## Connections
- [[AlgorithmicBias]] — proxies are why bias survives attribute removal.
- [[Fairness]] / [[DisparateImpact]] — the harms proxies produce.
- [[GoodhartsLaw]] — proxy-target decoupling under optimization.
- [[DisaggregatedEvaluation]] — the monitoring that catches proxy harm.
- [[COMPAS]] — base-rate proxy harm in criminal justice.
- [[mlsysbook-ch15-responsible-engineering]] — source.
