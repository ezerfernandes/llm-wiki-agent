---
title: "Concept Drift"
type: concept
tags: [drift, monitoring, mlops]
sources: [mlsysbook-ch04-data-engineering, mlsysbook-ch14-ml-operations, agentic-design-patterns-ch19-evaluation]
last_updated: 2026-06-05
---

# Concept Drift

A shift in the conditional distribution P(y|x) over time — the relationship between inputs and labels itself changes, even if feature distributions stay constant. Detected via [[BlackBoxShiftDetection]] or label-aware monitoring; contrast with [[DataDrift]] which moves P(x).

Reddi's *Machine Learning Systems* ([[mlsysbook-ch04-data-engineering|Vol 1, Ch 4]]) calls concept drift "the most challenging case": because $p(y\mid x)$ evolves (treatment protocols change, fraud patterns adapt, social trends shift), detection **requires ground-truth labels** to know whether the feature-to-label relationship moved — making it inherently more delayed than [[CovariateShift|covariate]] or [[LabelShift|label]] shift.

## Agent drift detection ([[agentic-design-patterns-ch19-evaluation|Gulli Ch 19]])

[[EvaluationAndMonitoring|Ch 19 (Evaluation and Monitoring)]] names **drift detection** as a core agent-monitoring application: *"monitoring the relevance or accuracy of an agent's outputs over time, detecting when its performance degrades due to changes in input data distribution (concept drift) or environmental shifts."* Because agents act in dynamic environments, this is paired with **anomaly detection in agent behavior** (unusual actions signalling errors, attacks, or emergent undesired behavior) as the post-deployment degradation safeguards of the pattern.

## Connections

- [[EvaluationAndMonitoring]] — Ch 19 monitors agent output for concept drift + environmental shifts post-deployment.
- [[CovariateShift]] / [[LabelShift]] — sibling shift types (detectable without ground truth).
- [[DataDrift]] / [[DistributionShift]] — the parent taxonomy.
- [[mlsysbook-ch04-data-engineering]] — source.
- [[mlsysbook-ch14-ml-operations]] — mlsysbook Vol 1 Ch 14 treats concept drift as $p(y\mid x)$ change, invisible until ground truth arrives (COVID-19 the canonical abrupt case); requires relabeling, not just fresh sampling.

