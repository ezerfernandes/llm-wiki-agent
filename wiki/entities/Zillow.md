---
title: "Zillow"
type: entity
tags: [company, real-estate, ml-failure, case-study, mlsysbook]
sources: [mlsysbook-ch02-ml-systems, mlsysbook-ch14-ml-operations]
last_updated: 2026-06-05
---

# Zillow

US real-estate marketplace, cited in [[VijayJanapaReddi|Reddi]]'s *Machine Learning Systems* ([[mlsysbook-ch02-ml-systems|Vol 1, Ch 2]]) as the **war-story exemplar of [[SystemEntropy|system entropy]]** — the business cost of [[DistributionShift|distribution shift]] in a production ML system.

Zillow launched "Zillow Offers," an iBuying business that bought homes directly based on ML home-price forecasts and resale economics. When forecasting became "more unpredictable than expected," scaling automated buying under that uncertainty created inventory and balance-sheet volatility the business could not tolerate. In 2021 Zillow wrote down **$304 million** in inventory, laid off **25% of its workforce (~2,000 people)**, and shut the Offers division entirely. The systems lesson: "distribution shift is not just a metric drop; it is a business risk" — automated decision systems in dynamic markets need rapid feedback loops and circuit breakers, not just accurate offline models.

## Connections

- [[SystemEntropy]] — Zillow is the chapter's evidence for post-deployment statistical decay.
- [[DistributionShift]] — the failure mechanism.
- [[MLOps]] — the monitoring/circuit-breaker discipline that could have caught it.
- [[mlsysbook-ch02-ml-systems]] — source.
- [[mlsysbook-ch14-ml-operations]] — Ch 14's canonical correction-cascade failure: Zestimate iBuying losses > $500M (Q3 2021), ~2,000 layoffs, iBuying shut down.

