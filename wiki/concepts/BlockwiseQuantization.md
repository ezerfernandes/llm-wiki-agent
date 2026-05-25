---
title: "Blockwise Quantization"
type: concept
tags: [quantization, qlora, hands-on-llm]
sources: [hands-on-llm-ch12-fine-tuning-generation-models]
last_updated: 2026-05-23
---

# Blockwise Quantization

**Blockwise quantization** maps groups (blocks) of higher-precision weights to lower-precision values with **per-block quantization constants**, rather than applying a single global mapping. The per-block scale lets each block of weights cluster around different value ranges, preserving the per-block dynamic range that a global mapping would crush.

## In Hands-On LLMs Ch 12

[[hands-on-llm-ch12-fine-tuning-generation-models|Ch 12]] introduces blockwise quantization as one of two **mechanisms** that prevent QLoRA's 4-bit weights from being lossy:

> *"They used blockwise quantization to map certain blocks of higher precision values to lower precision values. Instead of directly mapping higher precision to lower precision values, additional blocks are created that allow for quantizing similar weights ... this results in values that can be accurately represented with lower precision."* — Ch 12

Diagrammatically, the chapter contrasts:
- **Direct higher → lower mapping**: multiple distinct higher-precision values collapse to the same lower-precision value, removing differentiating factors.
- **Blockwise mapping**: similar weights are grouped into blocks; each block has its own quantization constants → values in a tightly clustered block can be represented accurately at lower precision.

When combined with the **[[NormalFloat4|NF4]]** distribution-aware binning (more bins near zero, fewer in the tails — because pre-trained weights are normally distributed between –1 and 1), blockwise quantization is what lets 16-bit weights compress down to a **4-bit normalized float** with minimal accuracy loss.

## Connections

- [[QLoRA]] — the parent technique.
- [[NormalFloat4|NF4]] / [[DoubleQuantization]] / [[PagedOptimizer]] — the QLoRA innovations stack.
- [[Quantization]] — parent concept.
- [[bitsandbytes]] — implementation library.
- [[hands-on-llm-ch12-fine-tuning-generation-models]] — primary source.
