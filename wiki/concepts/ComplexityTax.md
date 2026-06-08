---
title: "Complexity Tax"
type: concept
tags: [ml-systems, engineering, mlops, mlsysbook]
sources: [mlsysbook-ch02-ml-systems]
last_updated: 2026-06-05
---

# Complexity Tax

The operational overhead — data pipelines, monitoring, retraining infrastructure — that **every ML deployment carries and that simpler heuristic systems avoid**, which must be repaid by measurably better outcomes. A decision gate in [[VijayJanapaReddi|Reddi]]'s *Machine Learning Systems* ([[mlsysbook-ch02-ml-systems|Vol 1, Ch 2]]).

Worked contrast for a classification problem:

- **Heuristic**: ~50 lines of if-then rules, near-zero compute, ~1 h/month maintenance, no drift.
- **ML system**: ~50 lines of model code + ~2,000 lines of infrastructure (data pipelines, monitoring, GPU drivers), ~40 h/month debugging drift and managing infra.

"An ML system that improves accuracy from 90% to 95% may still be a poor engineering choice if it introduces a 40× increase in complexity." The principle: *ML is not always the right choice.* If the operational cost of maintaining model quality over time (against [[SystemEntropy|system entropy]]) is unaffordable, the simpler heuristic is the superior systems choice. ML systems engineering is "the art of minimizing this tax through robust architecture." Decision gates: measure a heuristic baseline before training a deep network; weigh a 2% accuracy gain against a 10× inference/maintenance cost.

## Connections

- [[SystemEntropy]] — the post-deployment decay that makes the tax recurring.
- [[DeploymentDecisionFramework]] — the complexity tax is the "should you use ML at all?" pre-check.
- [[MLOps]] — the operational machinery whose cost the tax measures.
- [[mlsysbook-ch02-ml-systems]] — source.
