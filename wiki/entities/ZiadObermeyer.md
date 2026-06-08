---
title: "Ziad Obermeyer"
type: entity
tags: [responsible-ai, fairness, researcher, healthcare, person]
sources: [mlsysbook-ch15-responsible-engineering]
last_updated: 2026-06-05
---

# Ziad Obermeyer

Ziad Obermeyer is a physician and health-policy researcher (UC Berkeley) and lead author of the 2019 *Science* study auditing the [[Optum|Optum]] healthcare risk-stratification algorithm. He is cited in [[mlsysbook-ch15-responsible-engineering|mlsysbook Vol 1 Ch 15]] for the canonical [[ProxyVariable|proxy-variable]] bias case.

## Why he matters here
- Obermeyer et al. (2019, ~50K patients) showed that predicting **cost** as a proxy for **need** systematically under-scored Black patients at equal illness; reformulating the target raised the Black share flagged for high-risk care from **17.7% → 46.5%**, demonstrating that "optimizing for a proxy inherits the biases of the system that generated the proxy."

## Connections
- [[Optum]] — the algorithm his team audited.
- [[ProxyVariable]] — the failure mechanism his study defined.
- [[AlgorithmicBias]] / [[DisparateImpact]] — the harm documented.
- [[mlsysbook-ch15-responsible-engineering]] — source.
