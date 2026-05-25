---
title: "Sim2Real"
type: concept
tags: [robotics, simulation, transfer-learning]
sources: [ai-engineering-ch08-dataset-engineering]
last_updated: 2024-12-04
---

# Sim2Real

**The subfield of ML focused on adapting algorithms trained in [[Simulation|simulation]] to the real world.** Per [[ai-engineering-ch08-dataset-engineering|*AI Engineering* Ch 8]]:

> "No matter how sophisticated your simulations are, however, they are simplifications of the real world. Sim2Real is a subfield that focuses on adapting algorithms that have been trained in simulations to the real world."

## The sim2real gap

The performance loss when an algorithm trained purely in simulation is deployed in reality. Caused by:

- **Visual differences** — simulated textures vs real surfaces.
- **Physical-model errors** — friction, deformation, sensor noise.
- **Distribution shift** — simulator covers expected scenarios; reality includes long-tail unexpected ones.

## Why it matters

If a robot fails in simulation, it'll likely fail in reality. But the converse is **not** true: a robot that succeeds in simulation may still fail in reality. Closing the sim2real gap is the bottleneck for sim-trained robotics moving to production.

## Connections

- [[Simulation]] — parent technique.
- [[TransferLearning]] — sim2real is a special case (source domain = simulator; target = reality).
- [[DataSynthesis]] — simulation is one of three traditional approaches.
- [[ai-engineering-ch08-dataset-engineering]] — primary source.
