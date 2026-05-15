---
title: "Prefix LM"
type: concept
tags: [concept, architecture, attention, transformer]
sources: [1910.10683-t5]
last_updated: 2026-05-10
---

# Prefix LM

A Transformer architecture variant — a single decoder-only stack — in which the self-attention mask is **fully visible over the prefix** (the input/context portion) and **causal over the suffix** (the target portion). Originally proposed by Liu et al. (2018) and explored systematically alongside encoder-decoder and pure decoder-only language models in [[1910.10683-t5]] §3.2.

## Attention mask

For input + target concatenated as `[x₁, x₂, …, xₙ, y₁, y₂, …, yₘ]`:
- Positions ≤ n (the prefix): can attend to all positions ≤ n (fully visible).
- Positions > n (the target): can attend to all positions ≤ themselves (causal).

This is the rightmost panel in T5's Figure 3 (the "causal with prefix" mask).

## Relationship to other architectures

- vs **encoder-decoder**: a prefix LM is equivalent to an encoder-decoder model where (1) encoder and decoder parameters are shared, and (2) the explicit encoder-decoder cross-attention is replaced by full attention within a single stack.
- vs **decoder-only (causal) LM**: lifts the causal restriction on the prefix portion, so the prefix representation depends bidirectionally on the entire prefix — not just on its own past. This eliminates the "left-only context for input" weakness of causal LMs in conditional generation.
- vs **[[bert]]**: closely resembles BERT for classification — the model "sees" the entire input bidirectionally and then emits a label. The main difference is that the classifier is integrated into the output softmax of the decoder, rather than being a separate head over a `[CLS]` token.

## T5's empirical finding

In the systematic comparison in [[1910.10683-t5]] Table 2, with matched compute:
- **Encoder-decoder (with denoising)** wins on all tasks (2P parameters, M FLOPs).
- **Encoder-decoder with shared parameters** is a close second (P, M).
- **Prefix LM (with denoising)** loses to both — by ~1–2 GLUE points, ~3 SuperGLUE points, ~0.5 BLEU.
- Among the three single-stack variants (LM / prefix LM / shared-param encoder-decoder), prefix LM ranks middle.

The interpretation: adding an explicit encoder-decoder cross-attention is beneficial even when the cost is paying for separate encoder/decoder parameters.

## See also

- [[1910.10683-t5]] — source paper.
- [[transformer]] — base architecture.
- [[encoderdecoder]] — the winning architecture in T5's ablation.
- [[selfattention]] — the underlying operation that masking modifies.
- [[t5]] — model family that uses encoder-decoder, not prefix LM.
