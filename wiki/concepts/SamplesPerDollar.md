---
title: "Samples per Dollar"
type: concept
tags: [ml-systems, economics, mlsysbook, foundations]
sources: [mlsysbook-ch01-introduction]
last_updated: 2026-06-05
---

# Samples per Dollar

The systems engineer's economic objective in Reddi's *Machine Learning Systems* ([[mlsysbook-ch01-introduction|Vol 1, Ch 1]]): whereas researchers optimize for *accuracy*, systems engineers optimize for **samples per dollar**, unifying the three [[DAMTaxonomy|D·A·M]] axes into a single cost equation:

$$\text{Cost} \propto \frac{\text{Model Size} \times \text{Dataset Size}}{\text{Hardware Efficiency}}$$

- **Data** — better data quality raises each sample's learning value, reducing the numerator.
- **Algorithm** — more efficient architectures (transformers vs. RNNs) cut compute per sample.
- **Machine** — specialized hardware (GPUs/TPUs) raises FLOP/s per dollar, the denominator.

Systems engineering is the art of balancing this equation. The closely related **Return on Compute (RoC)** = ΔAccuracy / ΔCompute Cost flags over-engineered systems where a marginal accuracy gain isn't worth its compute multiple.

## Connections

- [[DAMTaxonomy]] / [[AITriad]] — the three axes the metric unifies.
- [[IronLawOfMLSystems]] — the time/cost decomposition (RoC).
- [[EfficiencyFramework]] — the levers that move the equation.
- [[SystemArchetype]] — the cost gap across deployment tiers.
- [[mlsysbook-ch01-introduction]] — source.
