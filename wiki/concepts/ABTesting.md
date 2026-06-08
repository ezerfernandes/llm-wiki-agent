---
title: "A/B Testing"
type: concept
tags: [evaluation, deployment, statistics]
sources: [mlsysbook-ch03-ml-workflow, mlsysbook-ch14-ml-operations, agentic-design-patterns-ch19-evaluation]
last_updated: 2026-06-07
---

# A/B Testing

A controlled experiment that compares two variants (A and B) of a model or feature on live traffic to determine which performs better on a target metric. Used during [[CanaryDeployment]] and [[CICD]] rollouts to validate model improvements before full release, often paired with [[ChiSquaredTest]] for significance.

In Reddi's *Machine Learning Systems* ([[mlsysbook-ch03-ml-workflow|Vol 1, Ch 3]]), A/B testing is the final stage of progressive [[ModelValidation|validation]] (offline → [[ShadowDeployment|shadow]] → [[CanaryDeployment|canary]] → A/B), catching *user-facing* issues. Its binding systems constraint is sample size: detecting a 0.5% sensitivity lift in a low-throughput [[DiabeticRetinopathyScreening|DR]] deployment can take weeks, directly gating iteration velocity — which is why offline paired tests (not A/B) are used for routine model comparison.

## A/B testing for agent improvements ([[agentic-design-patterns-ch19-evaluation|Gulli Ch 19]])

[[EvaluationAndMonitoring|Ch 19 (Evaluation and Monitoring)]] lists **"A/B testing for agent improvements"** as a core application of the pattern: *"systematically comparing the performance of different agent versions or strategies in parallel to identify optimal approaches (e.g., trying two different planning algorithms for a logistics agent)."* It is the agentic-systems instance of the same controlled-experiment method — comparing whole agent strategies (planners, prompts, model choices) on live traffic.

- [[EvaluationAndMonitoring]] — Ch 19 uses A/B testing to compare agent versions/strategies.
