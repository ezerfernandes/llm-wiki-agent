---
title: "Compound AI Systems"
type: concept
tags: [ml-systems, mlsysbook, architecture, agi, agents, rag]
sources: [mlsysbook-ch16-conclusion]
last_updated: 2026-06-05
---

# Compound AI Systems

**Architectures that chain multiple AI components — models, retrievers, tools, and verifiers — into pipelines rather than relying on a single monolithic model.** The term was coined by researchers at Berkeley AI Research ([[UCBerkeley|BAIR]]) in 2024. Per [[mlsysbook-ch16-conclusion|mlsysbook Vol 1's conclusion]], compound systems are the systems-engineering answer to the [[AGI]] challenge: because universal generalization makes every one of the [[ThirteenQuantitativeInvariants|thirteen invariants]] simultaneously active and expands the [[ParetoFrontier|Pareto frontier]] from ~3 metrics to dozens (safety, fairness, factuality, multilinguality, reasoning quality), "no monolithic model can navigate this complexity alone."

## The trade-off

Rather than one model that does everything, compound systems decompose a task into specialized steps — a retrieval component finds relevant information, a reasoning component processes it, a verification component checks the output. The decomposition **trades latency and orchestration complexity for control and correctness** — a trade-off "the Pareto frontier predicts and the [[ConservationOfComplexity|conservation of complexity]] demands." Gains: independently updatable, monitorable, and debuggable components, plus the ability to enforce *deterministic* constraints alongside *probabilistic* generation. Canonical examples: [[RetrievalAugmentedGeneration|RAG]] and tool-augmented agents.

## Why it aligns with systems engineering

- Each modular component can be **independently compressed and accelerated** ([[mlsysbook-ch10-model-compression|compression]], [[mlsysbook-ch11-hardware-acceleration|acceleration]]).
- Each has its own **silicon contract and [[ArithmeticIntensity|arithmetic intensity]] profile**, allowing hardware-specific optimization.
- The **interfaces between components are natural monitoring points** for detecting [[DriftDetection|drift]], [[TrainingServingSkew|skew]], and degradation.
- The engineering challenges (reliable orchestration, request routing across specialized components, consistency across distributed state) demand full-stack integration.

## Connections

- [[AGI]] — the goal that compound systems pursue without a single model.
- [[ThirteenQuantitativeInvariants]] — every invariant becomes active under universal generalization, motivating composition.
- [[ParetoFrontier]] / [[ConservationOfComplexity]] — predict and demand the orchestration-for-correctness trade-off.
- [[RetrievalAugmentedGeneration]] — a canonical compound architecture.
- [[LargeLanguageModel]] / [[GenerativeAI]] — the model components most often composed.
- [[mlsysbook-ch16-conclusion]] — source.
