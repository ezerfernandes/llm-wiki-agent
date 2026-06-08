---
title: "Efficiency Framework"
type: concept
tags: [ml-systems, efficiency, mlsysbook, optimization]
sources: [mlsysbook-ch01-introduction]
last_updated: 2026-06-05
---

# Efficiency Framework

The three complementary efficiency dimensions in Reddi's *Machine Learning Systems* ([[mlsysbook-ch01-introduction|Vol 1, Ch 1]]), each mapping to one axis of the [[DAMTaxonomy|D·A·M taxonomy]] and changing a different term of the [[IronLawOfMLSystems|iron law]]:

- **Algorithmic efficiency** (Algorithm axis) — more capability per FLOP via [[ModelCompression|model compression]] ([[Pruning|pruning]], [[Quantization|quantization]], [[KnowledgeDistillation|distillation]]), efficient architectures ([[MobileNetV2|MobileNet]]), and [[NeuralArchitectureSearch|NAS]]. EfficientNet was ~44.5× more compute-efficient than [[AlexNet]] over 2012–2019 (halving ~every 16 months).
- **Compute efficiency** (Machine axis) — maximize hardware [[GPUUtilization|utilization]] by aligning algorithmic logic with machine physics; CPUs → GPUs/TPUs and hardware-software co-design.
- **[[DataSelection|Data selection]]** (Data axis) — extract more learning signal per example via [[TransferLearning|transfer learning]], [[ActiveLearning|active learning]], and curriculum design, reducing the operation count $O$.

## The efficiency paradox

Per-FLOP efficiency improved ~44.5× while *total* AI training compute grew by ~10⁷× (doubling every 3.4 months — ~7× faster than [[MooresLaw|Moore's Law]]). Resolution: efficiency gains are *reinvested into scale* rather than cost reduction (the savings from EfficientNet funded larger models like [[GPT3|GPT-3]]). This feedback loop — efficiency enables scale, scale demands efficiency — defines modern AI economics.

## Connections

- [[DAMTaxonomy]] — one efficiency dimension per axis.
- [[IronLawOfMLSystems]] — each dimension changes a different term.
- [[BitterLesson]] — the scaling pressure efficiency counters.
- [[ModelCompression]] / [[DataSelection]] / [[NeuralArchitectureSearch]] — the techniques.
- [[MooresLaw]] — the hardware baseline outpaced by AI compute demand.
- [[mlsysbook-ch01-introduction]] — source.
