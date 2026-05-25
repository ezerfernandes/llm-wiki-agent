---
title: "CARLA"
type: entity
tags: [self-driving, simulator, dataset]
sources: [ai-engineering-ch08-dataset-engineering]
last_updated: 2024-12-04
---

# CARLA

**Open-source self-driving simulator** introduced by Dosovitskiy et al. (2017). Per [[ai-engineering-ch08-dataset-engineering|*AI Engineering* Ch 8]], CARLA is the canonical academic example of [[Simulation|simulation]]-based data generation for autonomous driving — alongside Waymo's SimulationCity and [[Tesla]]'s San Francisco simulation.

## Why it matters

Real-world driving experiments are dangerous (e.g., releasing a horse on the highway to test a self-driving car's reaction). CARLA provides a virtual environment to:

- Generate training data for rare or dangerous scenarios.
- Test policy behaviors without real-world risk.
- Run multiple controlled experiments cheaply.

The classic [[Sim2Real|sim2real]] caveat applies: a model that succeeds in CARLA may fail on real roads.

## Connections

- [[Simulation]] — the technique CARLA operationalizes.
- [[Sim2Real]] — the subfield bridging CARLA-trained policies to real driving.
- [[Tesla]] / Waymo — adjacent self-driving simulation efforts.
- [[Dosovitskiy]] — first author of the CARLA paper (also a [[ViT]] author).
- [[ai-engineering-ch08-dataset-engineering]] — primary source.
