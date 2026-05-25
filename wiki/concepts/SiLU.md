---
title: "SiLU (Swish)"
type: concept
tags: [activation, transformer, deep-learning]
sources: [hands-on-llm-ch03-looking-inside-llms]
last_updated: 2026-05-23
---

# SiLU (Swish)

**Sigmoid Linear Unit** (also known as **Swish**) — the activation function `SiLU(x) = x · sigmoid(x)`. Used inside the [[SwiGLU|SwiGLU]] gated MLP in modern Transformer LLMs.

## Where it appears

Visible in the [[Phi3Mini|Phi-3-mini]] PyTorch module print-out from [[hands-on-llm-ch03-looking-inside-llms|*Hands-On LLMs* Ch 3]] as `activation_fn: SiLU()` inside `Phi3MLP`. The gated structure — `gate_up_proj` produces two streams; SiLU gates one; element-wise multiply combines them; `down_proj` projects back — is consistent with the SwiGLU formulation from Shazeer's *"GLU Variants Improve Transformer"*.

## See also

- [[SwiGLU]] — the gated activation SiLU is the inner non-linearity of in modern LLMs.
- [[ReLU]] — the original-Transformer activation function.
- [[FeedForwardNetwork]] — the sublayer SiLU appears in.
- [[hands-on-llm-ch03-looking-inside-llms|*Hands-On LLMs* Ch 3]] — primary source.
