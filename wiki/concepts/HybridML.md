---
title: "Hybrid ML"
type: concept
tags: [ml-systems, deployment, architecture, mlsysbook]
sources: [mlsysbook-ch02-ml-systems]
last_updated: 2026-06-05
---

# Hybrid ML

The deployment strategy that **splits an ML pipeline across multiple [[DeploymentSpectrum|paradigm]] tiers**, assigning latency-critical stages to local hardware and compute-intensive stages to remote data centers. The state of the art for production systems in [[VijayJanapaReddi|Reddi]]'s *Machine Learning Systems* ([[mlsysbook-ch02-ml-systems|Vol 1, Ch 2]]) — "rarely does one paradigm suffice."

Hybrid architectures exploit the [[IronLawOfMLSystems|iron law]]'s additive structure: the edge tier minimizes $L_{lat}$ for time-sensitive stages, the cloud tier provides $R_{peak}$ for training/retraining/batch inference, with the split governed by the [[DataLocalityInvariant|data locality invariant]]. The defining feature is **bidirectional flow**: models deploy *down* (cloud → edge → mobile → tiny), data/telemetry flows *up*. Tiers must share synchronized state (feature definitions, model versions, preprocessing) or [[TrainingServingSkew|training-serving skew]] emerges at the boundary.

## Three integration patterns

| Pattern | Trade-off | Choose when |
|---|---|---|
| **Train-Serve Split** | Training cost vs. inference latency | Training needs scale inference doesn't; inference privacy matters (≥1,000,000× cost asymmetry) |
| **Hierarchical Processing** | Local autonomy vs. global optimization | Data volume exceeds transmission capacity; decisions at multiple timescales |
| **Progressive Deployment** | Model quality vs. deployment reach | Same model needed at multiple capability levels; graceful degradation required |

[[WakeWordDetection|Voice assistants]] combine all three; autonomous vehicles combine Hierarchical Processing + Progressive Deployment. Federated/collaborative learning extends the menu to privacy-preserving distributed training. Hybrids work because the paradigms differ in *resource budget*, not in the underlying systems jobs — which is why optimizations ([[Quantization|quantization]], operator fusion, binary networks) transfer between scales.

## Connections

- [[DeploymentSpectrum]] / [[CloudML]] / [[EdgeML]] / [[MobileML]] / [[TinyML]] — the tiers hybrid systems span.
- [[DeploymentDecisionFramework]] — selects the single best paradigm; hybrids combine the survivors.
- [[DataLocalityInvariant]] / [[IronLawOfMLSystems]] — govern where each stage runs.
- [[WakeWordDetection]] — the voice-assistant pipeline exemplifies all three patterns.
- [[FederatedLearning]] — the privacy-preserving distributed-training extension.
- [[TrainingServingSkew]] — the failure mode without synchronized tier state.
- [[mlsysbook-ch02-ml-systems]] — source.
