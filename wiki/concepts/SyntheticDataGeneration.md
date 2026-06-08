---
title: "Synthetic Data Generation"
type: concept
tags: [ml-systems, mlsysbook, data-engineering, data-acquisition, augmentation]
sources: [mlsysbook-ch04-data-engineering, mlsysbook-ch09-data-selection]
last_updated: 2026-06-05
---

# Synthetic Data Generation

A [[DataAcquisition|data-acquisition]] strategy that produces training examples algorithmically, **changing the scaling constraint** from human labor to validation burden (Reddi, [[mlsysbook-ch04-data-engineering|Vol 1, Ch 4]]). Its value depends entirely on whether the generator covers the deployment conditions real collection would miss.

Particularly valuable for **rare-event coverage** (simulation environments generate edge cases impractical to collect) and **augmentation** — AutoAugment, RandAugment, and SpecAugment introduce noise, pitch shifts, and temporal variations that improve generalization. Synthetic data merges with historical data to produce training sets of impractical-to-collect size and diversity. For KWS, synthetic augmentation is ~10× cheaper than real collection.

The limit: synthetic data **augments but cannot fully replace** real-world collection — it inherits its generator's biases. A KWS system trained purely on synthesized speech fails on accent patterns, background noises, and pronunciation variations the generator never modeled. See also the broader [[syntheticdata|synthetic data]] taxonomy (Huyen Ch 8).

## Connections

- [[syntheticdata]] — the broader FM-era synthetic-data treatment.
- [[DataAcquisition]] — the parent strategy space.
- [[WebScraping]] / [[Crowdsourcing]] — sibling channels.
- [[DataAugmentation]] — the augmentation subset.
- [[DataSelection]] — [[mlsysbook-ch09-data-selection|Ch 9]] casts synthetic generation as pipeline stage 3 (creation, not curation): [[DataAugmentation|augmentation]], generative synthesis ([[GenerativeAdversarialNetwork|GANs]], [[DiffusionModel|diffusion]], simulators like [[CARLA]]), and [[KnowledgeDistillation|distillation]]. Supplement-not-replacement: best mixes are 50–80% synthetic, limited by the [[DomainGap|domain gap]] and [[ModelCollapse|model collapse]].
- [[mlsysbook-ch04-data-engineering]] / [[mlsysbook-ch09-data-selection]] — sources.
