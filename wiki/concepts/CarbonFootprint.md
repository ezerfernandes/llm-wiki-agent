---
name: CarbonFootprint
title: "Carbon Footprint"
type: concept
tags: [responsible-ai, sustainability, carbon, green-ai, efficiency]
sources: [mlsysbook-ch15-responsible-engineering]
last_updated: 2026-06-05
---

# Carbon Footprint

The total greenhouse-gas emissions (in CO₂-equivalent) attributable to an ML system over its full lifecycle, treated by [[mlsysbook-ch15-responsible-engineering|mlsysbook Vol 1 Ch 15]] as a first-class engineering metric rather than an afterthought. Computed as **Carbon = Energy (kWh) × Carbon Intensity (kg CO₂/kWh)**.

## Key quantities from the chapter
- Worked carbon factor: a 400 W A100 at ~0.4 kg/kWh grid intensity ≈ **0.16 kg CO₂e per GPU-hour**.
- GPT-3-scale training (~1,287 MWh) ≈ **>500 tonnes CO₂e ≈ 100+ cars/year**.
- **Inference dominates training ~40–47:1** over a system's life, so measuring only training carbon is a named fallacy.
- Each **1% pipeline-efficiency gain ≈ ~1 car-year** of emissions removed; a 20% quantization-driven latency cut saves *a few tonnes of CO₂* plus ~$300K.
- Cloud-region selection and carbon-aware scheduling can matter more than algorithm choice.

## Connections
- [[Sustainability]] — the broader objective carbon footprint quantifies.
- [[GreenAI]] — the research agenda that elevates carbon to a reported metric (vs. Red AI).
- [[CarbonEmissions]] / [[CarbonIntensity]] — the components of the footprint calculation.
- [[TotalCostOfOwnership]] — carbon parallels TCO; inference dominates both.
- [[Quantization]] / [[Pruning]] / [[knowledgedistillation]] — efficiency levers that cut the footprint.
- [[mlsysbook-ch15-responsible-engineering]] — source.
