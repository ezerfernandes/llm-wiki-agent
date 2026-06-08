---
title: "Population Stability Index"
type: concept
tags: [monitoring, drift, mlops, statistics, mlsysbook]
sources: [mlsysbook-ch03-ml-workflow, mlsysbook-ch04-data-engineering, mlsysbook-ch14-ml-operations]
last_updated: 2026-06-05
---

# Population Stability Index

**PSI** is a lightweight statistic for detecting **distribution drift**: it bins a feature and computes the divergence between a baseline and a current distribution (Reddi, [[mlsysbook-ch03-ml-workflow|Vol 1, Ch 3]]). Standard interpretation: **PSI < 0.1 = stable, 0.1–0.2 = moderate drift, > 0.2 = significant drift.**

PSI is cheap enough to run in real time, which is the property that lets it serve as an **early-warning system** — detecting drift days or weeks before it degrades model accuracy, enabling proactive retraining rather than reactive incident response. Often paired with the [[KolmogorovSmirnovTest|Kolmogorov-Smirnov test]] in production [[MLOps|monitoring]] pipelines (DR system: alert if PSI > 0.2, or KS test $p < 0.01$).

## Connections

- [[KolmogorovSmirnovTest]] — the companion drift detector.
- [[DataDrift]] / [[DistributionShift]] — what PSI measures.
- [[MultiScaleFeedback]] — PSI powers the weekly drift-detection loop.
- [[MLOps]] — drift-detection pipelines (Ch 14).
- [[KullbackLeiblerDivergence]] — the continuous-distribution companion metric ([[mlsysbook-ch04-data-engineering|Ch 4]]); both operationalize the degradation equation's $\mathcal{D}(P_t \lVert P_0)$.
- [[DataDebt]] — [[mlsysbook-ch04-data-engineering|Ch 4]] uses PSI >0.1/>0.25 as freshness-debt warning/critical thresholds.
- [[mlsysbook-ch03-ml-workflow]] / [[mlsysbook-ch04-data-engineering]] — sources.
- [[mlsysbook-ch14-ml-operations]] — mlsysbook Vol 1 Ch 14 gives the PSI formula, credit-risk thresholds (<0.1 / 0.1–0.2 / >0.2), and a worked age-distribution example (total PSI 0.029 stable despite 3pp bin shifts).

