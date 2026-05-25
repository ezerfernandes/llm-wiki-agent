---
title: "Open-Source LLM"
type: concept
tags: [llm, open-source, licensing, deployment]
sources: [hands-on-llm-ch01-introduction-to-llms]
last_updated: 2026-05-23
---

# Open-Source LLM

LLMs whose **weights and architecture are shared publicly** — typically with code for running (and sometimes training) the model. Defined in *[[HandsOnLLM|Hands-On LLMs]]* ([[hands-on-llm-ch01-introduction-to-llms|Ch 1]]) as the counterpart to [[ProprietaryLLM|proprietary LLMs]]:

> "Open LLMs are models that share their weights and architecture with the public to use. They are still developed by specific organizations but often share their code for creating or running the model locally — with varying levels of licensing that may or may not allow commercial usage of the model." — Ch 1

## Canonical examples cited in Ch 1

- **[[Cohere|Cohere's]] Command R** — open-weights with commercial-use conditions.
- **[[Mistral]] models** (Mistral 7B, Mixtral 8x7B, etc.) — Apache 2.0 licensed.
- **[[microsoft|Microsoft's]] Phi family** (including [[Phi3Mini|Phi-3-mini]]) — MIT licensed.
- **[[meta|Meta's]] [[Llama]] models** — custom non-OSI license with commercial-use conditions.

## The "is it really open source?" caveat

Ch 1 explicitly flags the licensing complexity:

> "There are ongoing discussions as to what truly represents an open source model. For instance, some publicly shared models have a permissive commercial license, which means that the model cannot be used for commercial purposes. For many, this is not the true definition of open source, which states that using these models should not have any restrictions. Similarly, the data on which a model is trained as well as its source code are seldom shared." — Ch 1

So "open-source LLM" is **a spectrum**, not a binary:

1. **Open weights** — weights are downloadable. Most "open" LLMs in 2024.
2. **Open weights + code** — inference / training scripts also published.
3. **Open license** — weights usable commercially without restriction (e.g., Apache 2.0, MIT — Phi-3-mini qualifies).
4. **Truly open source** — weights + code + training data + recipe all public. Rare (OLMo, LLM360 / K2 are examples not cited in Ch 1).

## Trade-offs (per Ch 1)

| Dimension | Open LLM | [[ProprietaryLLM|Proprietary LLM]] |
|---|---|---|
| Control over model | Full | None |
| Fine-tunability | Yes | Limited / paid only |
| Data privacy | Local — never leaves your hardware | Sent to provider |
| Hardware required | Powerful local GPU | None — provider hosts |
| Setup expertise | Yes — requires specific knowledge | Minimal — call an API |
| Peak quality | Lower (typically) | Higher (typically) |
| Cost model | Capex (GPU) + opex (electricity) | Per-token / per-call API fees |

The book's stated preference: *"We generally prefer using open source models wherever we can. The freedom this gives to play around with options, explore the inner workings, and use the model locally arguably provides more benefits than using proprietary LLMs."* — Ch 1

## Community infrastructure

[[HuggingFace|Hugging Face]] is named in Ch 1 as the canonical model-hub-and-community-enabler: *"This benefit is enhanced by the large communities that enable these processes, such as Hugging Face, demonstrating the possibilities of collaborative efforts."*

## Connections

- [[ProprietaryLLM]] — the counterpart category.
- [[HuggingFace]] — the canonical open-LLM distribution channel.
- [[Cohere]] / [[Mistral]] / [[microsoft|Microsoft]] / [[meta|Meta]] — example open-LLM providers.
- [[Llama]] / [[Phi3Mini]] / [[Mistral7BInstructV02]] — example open-weights models.
- [[GPU]] / [[VRAM]] / [[Quantization]] — the hardware vocabulary for running open LLMs locally.
- [[llamacpp]] / [[LangChain]] / [[LMStudio]] / [[TextGenerationWebui]] / [[KoboldCpp]] — open-LLM runtimes.
- [[hands-on-llm-ch01-introduction-to-llms]] — primary source.
