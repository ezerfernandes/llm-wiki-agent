---
title: "Emergent Abilities"
type: concept
tags: [scaling, llm, capabilities]
sources: [ai-engineering-ch02-foundation-models]
last_updated: 2024-12-04
---

# Emergent Abilities

**Capabilities that are only present at scale** and might not be observable on smaller models trained on smaller datasets. Term coined by **Wei et al. (2022)**, cited in [[ai-engineering-ch02-foundation-models|*AI Engineering* Ch 2]] in the context of [[ScalingExtrapolation|scaling extrapolation]]:

> "Emergent abilities refer to those that are only present at scale [and] might not be observable on smaller models trained on smaller datasets."

## Implication for scaling extrapolation

Emergent abilities are **the central obstacle to [[ScalingExtrapolation|hyperparameter transfer]] from small models to large ones**. If a capability discontinuously appears at, say, 60B parameters, no amount of small-scale experimentation will predict its emergence — or the hyperparameter settings that maximize it.

## In the broader debate

Emergent abilities are a contested phenomenon — some later work (Schaeffer et al. 2023) argued that many "emergent" capabilities are artifacts of discontinuous evaluation metrics rather than true model-level discontinuities. Ch 2 doesn't engage that controversy; it cites Wei et al.'s framing as established.

## Connections
- [[ScalingExtrapolation]] — the practice emergence makes harder.
- [[scalinglaws]] — the broader scaling framework emergence sits inside.
- [[ChinchillaScalingLaw]] — compute-optimal training assumes smooth behavior, which emergence challenges.
- [[LargeLanguageModel]] — the model class where emergence is observed.
- [[ai-engineering-ch02-foundation-models]] — primary source.
