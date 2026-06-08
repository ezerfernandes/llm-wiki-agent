---
title: "GShard"
type: entity
tags: [cs324, llm]
sources: [cs324-selective-architectures, cs324-environment]
last_updated: 2026-06-04
---

GShard (Lepikhin et al.) is a 600-billion-parameter top-2-routed Mixture-of-Experts model for massively multilingual machine translation across 100 languages. It also introduced sharding annotations that let the compiler automatically distribute the model across many accelerators.

## Connections
- [[MixtureOfExperts]] — GShard is a top-2-routed MoE model
- [[cs324-selective-architectures]] — discussed in this CS324 lecture
- [[cs324-environment]] — discussed in this CS324 lecture
