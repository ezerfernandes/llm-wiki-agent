---
title: "Procedural Generation"
type: concept
tags: [data-generation, gaming, algorithm]
sources: [ai-engineering-ch08-dataset-engineering]
last_updated: 2024-12-04
---

# Procedural Generation

**Algorithmic content creation — the umbrella term for non-manual data generation across software engineering, gaming, robotics, and now AI training.** Per [[ai-engineering-ch08-dataset-engineering|*AI Engineering* Ch 8]]: "Using algorithms to generate data is also called procedural generation, as opposed to manual generation."

## Outside AI

- **Gaming** — Minecraft, No Man's Sky use noise functions and fractal algorithms to create vast immersive worlds. Dungeons & Dragons procedurally generates dungeons, quests, encounters.
- **Software testing** — generated test cases ([[Faker]], Chance libraries).
- **Robotics** — joint-movement scenarios, environment variants.

## Inside AI training

Most data-generation techniques used in these industries can be applied to AI:

- Template-based synthesis ([[RuleBasedDataSynthesis]])
- Simulated environments ([[Simulation]])
- Self-play scenarios ([[SelfPlay]])

## The headline AI training result

[[AlphaGeometry]] (Trinh et al. 2024) — 100M procedurally-generated Olympiad-level geometry problems trained a DeepMind model to Olympiad-level performance.

## Connections

- [[DataSynthesis]] / [[DataAugmentation]] — modern AI-specific subclasses.
- [[RuleBasedDataSynthesis]] — the template-based form.
- [[Simulation]] — the virtual-environment form.
- [[AlphaGeometry]] — the headline AI-training success.
- [[ai-engineering-ch08-dataset-engineering]] — primary source.
