---
title: "System Archetype"
type: concept
tags: [ml-systems, deployment, hardware, mlsysbook]
sources: [mlsysbook-ch01-introduction]
last_updated: 2026-06-05
---

# System Archetype

The four reference deployment tiers that define the hardware/power/memory constraints for every chapter of Reddi's *Machine Learning Systems* ([[mlsysbook-ch01-introduction|Vol 1, Ch 1]]). They quantify the [[DeploymentSpectrum|deployment spectrum]] and expose the multi-order-of-magnitude span that prevents simple model reuse across tiers.

| Archetype | Example | RAM/Memory | Peak Compute | Power |
|---|---|---|---|---|
| **Cloud** | H100 GPU | ~80 GB | ~1,000 TFLOP/s | ~700 W |
| **Edge** | Jetson robotics | tens of GB | tens of TFLOP/s | tens of W |
| **Mobile** | Smartphone | 4–12 GB | TOPS-scale | 2–5 W |
| **TinyML** | ESP32-S3 | ~512 KB | sub-GFLOP/s | sub-watt (mW) |

The Cloud↔TinyML gap is **~10⁶× in memory and ~10⁷× in compute.** Each archetype is paired with a scenario workload to form an *engineering mission* (e.g. Frontier Training = Cloud + GPT-4; Autonomous Perception = Edge + YOLOv8-nano; Smart Doorbell = TinyML + Wake Vision). This is part of the book's **engineering crux** — a four-layer stack of Hardware → Systems → Workloads → Missions.

## Connections

- [[DeploymentSpectrum]] — the continuum these archetypes anchor.
- [[TinyML]] / [[EdgeML]] — the constrained tiers.
- [[LighthouseModel]] — the workloads mapped onto archetypes.
- [[SamplesPerDollar]] — the economic constraint spanning tiers.
- [[mlsysbook-ch01-introduction]] — source.
