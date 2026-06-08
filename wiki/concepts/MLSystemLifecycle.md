---
title: "ML System Lifecycle"
type: concept
tags: [ml-systems, mlops, mlsysbook, foundations]
sources: [mlsysbook-ch01-introduction, mlsysbook-ch03-ml-workflow, mlsysbook-ch16-conclusion]
last_updated: 2026-06-05
---

# ML System Lifecycle

The **cyclical** development arc of an ML system, contrasted with the linear design→implement→test→deploy→maintain arc of traditional software in Reddi's *Machine Learning Systems* ([[mlsysbook-ch01-introduction|Vol 1, Ch 1]]).

**Data Collection → Preparation → Model Training → Evaluation → Deployment → Monitoring**, with two feedback loops that have no counterpart in traditional software:

- **Evaluation → Preparation** when results are insufficient ("needs improvement").
- **Monitoring → Collection** when production performance degrades ("performance degrades").

Because behavior is data-dependent, the cycle never ends: distribution shift silently alters behavior without code changes. Traditional tooling is insufficient — version control struggles with large evolving datasets, and deterministic test frameworks must be adapted for probabilistic outputs. In production the stages settle into **virtuous cycles** (good data → effective learning → better data collection) or **vicious cycles** (poor data → weak learning → worse collection), each compounding.

Deployment context reshapes every stage: cloud enables easy A/B testing and rapid iteration; edge requires OTA updates with bandwidth management and rollback.

## Connections

- [[SilentDegradation]] — why the monitoring → collection loop exists.
- [[DistributionShift]] / [[DataDrift]] — the drift the cycle responds to.
- [[MLOps]] / [[ModelMonitoring]] / [[ABTesting]] — operationalization.
- [[DeploymentSpectrum]] — how deployment context reshapes the lifecycle.
- [[FivePillarFramework]] — the disciplines that sustain the lifecycle.
- [[MLWorkflow]] / [[MachineLearningLifecycle]] — [[mlsysbook-ch03-ml-workflow|Ch 3]] expands this sketch into a fully specified six-stage process, distinguishing the *lifecycle* (what gets traversed) from the *workflow* (how it's managed), and adds the [[ConstraintPropagationPrinciple]], [[IterationTax]], and [[StageInterfaceSpecification]].
- [[mlsysbook-ch16-conclusion]] — the conclusion recasts the cycle as the four-Part **Foundations→Build→Optimize→Deploy** arc with a central [[ConservationOfComplexity|conservation-of-complexity]] hub and a critical **Deploy→Foundations feedback arrow**: verification failures, drift, skew, tail-latency violations, and bias amplification (invariants 9–13 of the [[ThirteenQuantitativeInvariants|thirteen]]) force the system back to new data, retraining, and fresh optimization passes.
- [[mlsysbook-ch01-introduction]] / [[mlsysbook-ch03-ml-workflow]] — sources.
