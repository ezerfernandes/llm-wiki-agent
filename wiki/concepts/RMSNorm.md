---
title: "RMSNorm"
type: concept
tags: [normalization, transformer, architecture]
sources: [hands-on-llm-ch03-looking-inside-llms]
last_updated: 2026-05-23
---

# RMSNorm

**Root Mean Square Layer Normalization** — a simplified normalization scheme introduced by Zhang & Sennrich in *"Root mean square layer normalization"*. RMSNorm replaces [[LayerNormalization|LayerNorm]] in modern Transformer LLMs because it is *"simpler and more efficient than the LayerNorm used in the original Transformer"* ([[hands-on-llm-ch03-looking-inside-llms|*Hands-On LLMs* Ch 3]]).

## How it differs from LayerNorm

LayerNorm centers (subtracts the mean) and scales (divides by the standard deviation) of each observation's features. **RMSNorm drops the mean-centering step** and rescales by the root-mean-square of the features only. This removes one statistic and one subtraction per normalization op, saving compute without measurable quality loss.

In Phi-3's PyTorch module print-out from Ch 3, RMSNorm appears as `Phi3RMSNorm` used for both `input_layernorm` (before attention) and `post_attention_layernorm` (before the FFN) — the standard **pre-norm** placement inside each decoder block.

## Where it appears

- **[[Phi3Mini|Phi-3-mini]]** — `Phi3RMSNorm` in every decoder layer plus a final `Phi3Model.norm`.
- **[[Llama|Llama 2]] / [[Llama|Llama 3]]** — part of the modern 2024-era Transformer block recipe (pre-norm + RMSNorm + [[SwiGLU]] + [[GroupedQueryAttention|GQA]] + [[RoPE]]).

## See also

- [[LayerNormalization]] — the original-Transformer normalization RMSNorm replaces.
- [[PreNorm]] — the placement scheme RMSNorm is typically deployed in.
- [[transformer]] — the architecture.
- [[hands-on-llm-ch03-looking-inside-llms|*Hands-On LLMs* Ch 3]] — primary source.
