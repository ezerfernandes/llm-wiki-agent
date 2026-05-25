---
title: "TDP (Thermal Design Power)"
type: concept
tags: [hardware, power, gpu, cpu]
sources: [ai-engineering-ch09-inference-optimization]
last_updated: 2024-12-04
---

# TDP — Thermal Design Power

**A proxy metric for a chip's expected power consumption: the maximum heat a cooling system needs to dissipate when the chip operates under typical workloads.** Per [[ai-engineering-ch09-inference-optimization|*AI Engineering* Ch 9]]:

> *"TDP represents the maximum heat a cooling system needs to dissipate when the chip operates under typical workloads. While it's not an exact measure of power consumption, it's an indication of the expected power draw. For CPUs and GPUs, the maximum power draw can be roughly 1.1 to 1.5 times the TDP, though the exact relationship varies depending on the specific architecture and workload."*

## TDP vs maximum power draw

Ch 9 distinguishes:

- **Maximum power draw** — peak power the chip can draw under full load (the safety upper bound).
- **TDP** — expected power for typical workloads (the engineering planning number).

Roughly, **max power draw ≈ 1.1× to 1.5× TDP**, depending on architecture.

## Why it matters for AI workloads

Data center planning is increasingly **power-constrained**. From Ch 9:

> *"A main challenge in building data centers with tens of thousands of GPUs is finding a location that can guarantee the necessary electricity. Building large-scale data centers requires navigating electricity supply, speed, and geopolitical constraints."*

Aggregated TDP across a GPU cluster determines:
- Cooling system sizing.
- Power-delivery infrastructure.
- Geographic site selection.

## Sample numbers (referenced in Ch 9)

- An NVIDIA H100 running at peak for a year: ~7,000 kWh.
- Average US household annual electricity use: 10,000 kWh.

→ A single H100 at sustained peak draws roughly **70% of a US household's** annual electricity.

## TDP and "peak FLOP/s hacking"

Higher TDP often correlates with higher peak FLOP/s claims — the more power you can deliver into a chip, the more you can clock its compute units. Chip-maker peak claims are bounded above by what TDP allows the chip to sustain.

## Connections

- [[GPU]] / [[AIAccelerator]] — the chips TDP characterizes.
- [[NVIDIA]] — H100 TDP numbers.
- [[MFU]] / [[MBU]] — utilization metrics that determine actual power draw vs TDP.
- [[InferenceOptimization]] — broader discipline (because power = cost).
- [[ai-engineering-ch09-inference-optimization]] — primary source.
