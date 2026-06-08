---
title: "GLaM"
type: entity
tags: [cs324, llm]
sources: [cs324-selective-architectures]
last_updated: 2026-06-04
---

GLaM (Generalist Language Model) is a Google 1.2-trillion-parameter Mixture-of-Experts language model with 64 experts per MoE layer. Because only a few experts activate per token, it outperforms GPT-3 on zero- and one-shot tasks while using roughly one-third the training compute.

## Connections
- [[MixtureOfExperts]] — GLaM is a sparsely-activated MoE language model
- [[GPT-3]] — outperforms GPT-3 at lower training cost
- [[cs324-selective-architectures]] — discussed in this CS324 lecture
