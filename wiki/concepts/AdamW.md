---
title: "AdamW"
type: concept
tags: [cs324, llm]
sources: [cs324-training, mlsysbook-ch08-model-training]
last_updated: 2026-06-05
---

The decoupled-weight-decay variant of [[Adam]] (Loshchilov & Hutter 2017), noted in CS324 Training's further reading. See [[Adam]].

Per [[mlsysbook-ch08-model-training|mlsysbook Ch 8]], AdamW corrects a flaw where standard Adam's adaptive learning rate *weakens* regularization for parameters with large second-moment estimates $v_t$; decoupling the weight-decay shrinkage from the gradient update fixes this and **improves generalization at zero additional accelerator state** — a memory-neutral upgrade, making it the default for training large transformers.

## Connections
- [[Adam]] — base optimizer
- [[mlsysbook-ch08-model-training]] — memory-neutral decoupled-weight-decay framing; the transformer-training default.
