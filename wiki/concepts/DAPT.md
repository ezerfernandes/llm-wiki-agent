---
title: "DAPT"
type: concept
tags: [cs324, llm]
sources: [cs324-harms-2]
last_updated: 2026-06-04
---

DAPT (domain-adaptive pretraining) is a data-based detoxification approach that continues pretraining a model on filtered non-toxic text to steer its generations toward safer outputs. It modifies the model's parameters rather than intervening only at decoding time.

## Connections
- [[Toxicity]] — the harm it mitigates
- [[PPLM]] — decoding-time detoxification alternative
- [[cs324-harms-2]] — discussed in this CS324 lecture
