---
title: "GPT-3"
type: entity
tags: [model, llm, openai, gpt]
sources: [ai-engineering-ch02-foundation-models, hands-on-llm-ch03-looking-inside-llms]
last_updated: 2026-05-23
---

# GPT-3

[[openai|OpenAI]]'s **175B-parameter autoregressive language model** (Brown et al., 2020) — *"Language Models Are Few-Shot Learners"*. The model whose scale and few-shot-prompting capabilities ignited the modern LLM era.

## Headline numbers (from [[ai-engineering-ch02-foundation-models|AI Engineering Ch 2]])

| Quantity | Value |
|---|---|
| Parameters | **175 billion** |
| Training tokens | **300 billion** |
| Training compute | **3.14 × 10²³ [[FLOPs|FLOPs]]** |
| Notable activation function | **GELU** (vs ReLU in GPT-2) |

## Worked cost calculation (Ch 2)

Training GPT-3-175B today, on 256 [[NVIDIA|NVIDIA]] H100s at 70% utilization at $2/h:

$$3.14 \times 10^{23} \text{ FLOPs} / (256 \times 5.2 \times 10^{18} \text{ FLOPs/day}) \approx 236 \text{ days}$$

$$\$2/h \times 256 \times 24 \times 256 / 0.7 \approx \$4{,}142{,}811$$

≈**$4.14M and ≈236 days** — *if* you make no training mistakes.

## Position in scaling history (Ch 2)

Per Ch 2's GPT scale arc:
- GPT (June 2018): 117M params.
- GPT-2 (Feb 2019): 1.5B — order-of-magnitude jump.
- **GPT-3 (June 2020): 175B — two orders of magnitude past GPT-2.**

Three orders of magnitude in 3 years. Ch 2's open question: how many more orders of magnitude is feasible? (See [[ScalingBottlenecks]].)

## Compute-(sub)optimality

By [[ChinchillaScalingLaw|Chinchilla scaling]] standards (≈20 tokens/param), GPT-3 at 175B params should have been trained on **≈3.5T tokens** — vastly more than its actual 300B. GPT-3 was **substantially under-trained on tokens** relative to its parameter count. This is one of the empirical bases for the Chinchilla revision.

## Connections
- [[openai|OpenAI]] — the builder.
- [[ChinchillaScalingLaw]] — the scaling law GPT-3 falls short of.
- [[scalinglaws]] — the broader power-law framework.
- [[FLOPs]] — the compute unit.
- [[CommonCrawl]] — GPT-3's primary training data source.
- [[ai-engineering-ch02-foundation-models]] — primary source.
- [[LargeLanguageModel]] / [[AutoregressiveLanguageModel]] / [[FoundationModel]] — the broader categories.

## From [[hands-on-llm-ch03-looking-inside-llms|*Hands-On LLMs* Ch 3]]

Ch 3 names GPT-3 as **the canonical model that interleaves full and sparse attention blocks** rather than using full attention throughout:

> "One model that incorporates such a mechanism is GPT-3. But it does not use that for all the Transformer blocks — the quality of the generation would vastly degrade if the model could only see a small number of previous tokens. The GPT-3 architecture interweaved full-attention and efficient-attention Transformer blocks. So the Transformer blocks alternate between full attention (e.g., blocks 1 and 3) and sparse attention (e.g., blocks 2 and 4)." — Ch 3

GPT-3's sparse-attention blocks follow the recipe from *"Generating long sequences with sparse transformers"* (Child et al.). The interleave with full-attention blocks is how the model preserves long-range context while saving compute.

Ch 3 also names GPT-3 (and GPT-2 / Llama 2) implicitly as **"raw language models"** that *"are difficult for people to properly utilize"* — contrasted with chat-fine-tuned models like [[GPT4|GPT-4]] that follow instructions. *"This is why the language model is then trained on instruction-tuning and human preference and feedback fine-tuning to match people's expectations of what the model should output."*

See [[LocalAttention]] for the wiki's broader local/sparse-attention coverage.
