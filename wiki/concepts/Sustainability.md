---
name: Sustainability
title: "Sustainability (ML Systems)"
type: concept
tags: [responsible-ai, sustainability, carbon, green-ai, efficiency]
sources: [mlsysbook-ch15-responsible-engineering]
last_updated: 2026-06-05
---

# Sustainability (ML Systems)

The treatment of an ML system's environmental and energy cost as a design objective on par with latency, throughput, and accuracy ([[mlsysbook-ch15-responsible-engineering|mlsysbook Vol 1 Ch 15]]). In the chapter's framing, **efficiency *is* responsibility**: the same techniques the book teaches for speed double as instruments for reducing harm via the [[CarbonFootprint|carbon footprint]] and accessibility.

## The argument
- Maps to the **Machine** axis of the [[DAMTaxonomy|D·A·M taxonomy]] — inadequate or energy-hungry infrastructure is a responsibility failure.
- [[GreenAI|Green AI]] vs. "Red AI": Schwartz et al. 2020 noted SOTA gains 2012–2018 required a **300,000×** compute increase; sustainability reframes this as a cost to be reported and minimized.
- Levers: model compression ([[Quantization|quantization]], [[Pruning|pruning]], [[knowledgedistillation|distillation]]), hardware acceleration (10–100× energy efficiency), and carbon-aware scheduling / cloud-region selection.
- Because **inference dominates training ~40:1**, sustainability gains compound over a deployed system's life.

## Connections
- [[CarbonFootprint]] — the primary quantified metric of sustainability.
- [[GreenAI]] — the research agenda promoting efficiency as a reported objective.
- [[TotalCostOfOwnership]] — the economic mirror of the environmental argument.
- [[Quantization]] / [[Pruning]] / [[knowledgedistillation]] — efficiency-as-responsibility techniques.
- [[DAMTaxonomy]] — the Machine axis locates sustainability failures.
- [[ResponsibleAIEngineering]] — sustainability is one of its objectives.
- [[mlsysbook-ch15-responsible-engineering]] — source.
