---
title: "Activation Recomputation"
type: concept
tags: [memory, training, finetuning]
sources: [ai-engineering-ch07-finetuning]
last_updated: 2024-12-04
---

# Activation Recomputation

Alternative name for **[[GradientCheckpointing|gradient checkpointing]]** — the memory-saving training technique that doesn't store activations on the forward pass but recomputes them during the backward pass. Per [[ai-engineering-ch07-finetuning|*AI Engineering* Ch 7]], the two terms are used interchangeably; the Korthikanti et al. (2022) paper Ch 7 cites uses *"Reducing Activation Recomputation in Large Transformer Models"* as its title.

See [[GradientCheckpointing]] for the full treatment.

## Connections

- [[GradientCheckpointing]] — the canonical name on this wiki.
- [[ActivationMemory]] — what activation recomputation reduces.
- [[Korthikanti2022ActivationRecomputation]] — the foundational paper.
- [[ai-engineering-ch07-finetuning]] — primary source.
