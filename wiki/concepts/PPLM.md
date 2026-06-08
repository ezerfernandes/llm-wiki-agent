---
title: "PPLM"
type: concept
tags: [cs324, llm]
sources: [cs324-harms-2]
last_updated: 2026-06-04
---

PPLM (Plug-and-Play Language Model) is a decoding-time attribute-control method that steers a frozen LM's generations using gradients from an attribute classifier, enabling detoxification or topic control without retraining. It operates at inference rather than modifying model weights.

## Connections
- [[Toxicity]] — a target attribute for control
- [[DAPT]] — data-based detoxification alternative
- [[cs324-harms-2]] — discussed in this CS324 lecture
