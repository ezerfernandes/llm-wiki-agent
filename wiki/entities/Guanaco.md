---
title: "Guanaco"
type: entity
tags: [model, qlora, finetuning, llama-2]
sources: [ai-engineering-ch07-finetuning]
last_updated: 2024-12-04
---

# Guanaco

A family of models (7B, 13B, 33B, 65B) produced by [[QLoRA|QLoRA]] finetuning of Llama base models, released alongside [[Dettmers2023QLoRA|Dettmers et al. (NeurIPS 2023)]] as the paper's empirical demonstration. Per [[ai-engineering-ch07-finetuning|*AI Engineering* Ch 7]]:

> "The authors finetuned a variety of models, including Llama 7B to 65B, in the 4-bit mode. The resulting family of models, called Guanaco, showed competitive performance on both public benchmarks and comparative evaluation."

## May 2023 Elo ratings (Ch 7's Table 7-7, GPT-4 as judge)

| Model | Size | Elo |
|---|---|---|
| GPT-4 | — | **1348 ± 1** |
| Guanaco 65B | 41 GB | 1022 ± 1 |
| Guanaco 33B | 21 GB | 992 ± 1 |
| Vicuna 13B | 26 GB | 974 ± 1 |
| ChatGPT | — | 966 ± 1 |
| Guanaco 13B | 10 GB | 916 ± 1 |
| Bard | — | 902 ± 1 |
| Guanaco 7B | 6 GB | 879 ± 1 |

The headline: **Guanaco 65B was preferred over ChatGPT** by GPT-4 judging (1022 vs 966), but didn't reach GPT-4's own performance.

## Why Guanaco matters as a result

- **Demonstrated QLoRA's viability**: a 65B model finetuned on a single 48 GB GPU producing ChatGPT-competitive outputs was a moment-defining result.
- **Mainstreamed quantized finetuning**: by being open-source and reproducible, Guanaco showed practitioners that quality wasn't a fundamental casualty of 4-bit base + LoRA adapter training.
- **Set the trajectory** that led to [[Bitsandbytes]] being adopted across the [[HuggingFace]] ecosystem.

## Hardware cost (Ch 7)

> "These techniques [NF4 + paged optimizers] allow a 65B-parameter model to be finetuned on a single 48 GB GPU."

Before Guanaco, a 65B finetune was a multi-GPU cluster operation. After Guanaco, it was a single-A6000/A100 operation.

## Connections

- [[QLoRA]] / [[NormalFloat4|NF4]] / [[Bitsandbytes]] — the techniques that produced Guanaco.
- [[Llama]] — the base model family.
- [[TimDettmers]] — the lead author.
- [[Vicuna]] — sibling Llama-derivative model.
- [[ai-engineering-ch07-finetuning]] — wiki source.
