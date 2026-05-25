---
title: "SwiGLU"
type: concept
tags: [activation, transformer, architecture]
sources: [hands-on-llm-ch03-looking-inside-llms]
last_updated: 2026-05-23
---

# SwiGLU

A **gated activation function** based on the Gated Linear Unit (GLU) with [[SiLU|Swish/SiLU]] gating. Introduced as part of Shazeer's *"GLU Variants Improve Transformer"* survey of GLU-family activations, SwiGLU replaces the original Transformer's [[ReLU|ReLU]] activation inside the position-wise [[FeedForwardNetwork|feedforward network]] in many modern LLMs.

## Why modern LLMs use it

> "Lastly, instead of the original Transformer's ReLU activation function, newer variants like SwiGLU (described in 'GLU Variants Improve Transformer') are now more common." — [[hands-on-llm-ch03-looking-inside-llms|*Hands-On LLMs* Ch 3]]

The mechanism is a gated MLP: the input is projected into two streams; one stream passes through a SiLU/Swish activation and gates the other (element-wise multiply); the gated result is projected back to model dimension.

In [[Phi3Mini|Phi-3-mini]]'s PyTorch module print-out from Ch 3 the MLP is `Phi3MLP(gate_up_proj: Linear(3072 → 16384), down_proj: Linear(8192 → 3072), activation_fn: SiLU())` — the `gate_up_proj` fuses the gate and up-projection matrices (3072 → 8192 + 3072 → 8192 = 3072 → 16384) and the `down_proj` consumes the 8192 gated output. The activation is [[SiLU]].

## Where it appears

- **[[Phi3Mini|Phi-3-mini]]** — `Phi3MLP` with `SiLU` activation, gated structure.
- **[[Llama|Llama 2]] / [[Llama|Llama 3]]** — SwiGLU is part of the modern 2024-era block recipe.

## See also

- [[SiLU]] — the activation function inside the gate.
- [[ReLU]] — the original-Transformer activation SwiGLU replaces.
- [[FeedForwardNetwork]] — the sublayer SwiGLU lives in.
- [[transformer]] — the architecture.
- [[hands-on-llm-ch03-looking-inside-llms|*Hands-On LLMs* Ch 3]] — primary source.
