---
title: "Adapters"
type: concept
tags: [cs324, llm]
sources: [cs324-adaptation]
last_updated: 2026-06-04
---

Adapters are a parameter-efficient fine-tuning method that inserts small bottleneck residual layers into a frozen pretrained model (Houlsby et al. 2019), training less than 1% of the parameters. This allows task adaptation with minimal added storage per task.

## Connections
- [[FineTuning]] — the full-parameter alternative
- [[LoRA]] — related parameter-efficient method
- [[PrefixTuning]] — related parameter-efficient method
- [[cs324-adaptation]] — discussed in this CS324 lecture
