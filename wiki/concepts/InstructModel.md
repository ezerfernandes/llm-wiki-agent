---
title: "Instruct Model"
type: concept
tags: [llm, instruction-tuning, chat, post-training]
sources: [hands-on-llm-ch01-introduction-to-llms]
last_updated: 2026-05-23
---

# Instruct Model

In *[[HandsOnLLM|Hands-On LLMs]]* ([[hands-on-llm-ch01-introduction-to-llms|Ch 1]]), **instruct model** (a.k.a. **chat model**) is the term for a [[GenerativeModel|generative LLM]] that has been fine-tuned to **follow directions** rather than blindly autocomplete text. The book frames this as the second step of a two-step training paradigm:

1. **[[pretraining|Pretraining]]** — produces a [[FoundationModel|base model]] / [[CompletionModel|completion model]] via next-token prediction over internet-scale text.
2. **[[FineTuning|Fine-tuning]]** on instruction / dialog data — converts the base model into an instruct model that answers questions and follows tasks.

> "By fine-tuning these models, we can create instruct or chat models that can follow directions. ... the resulting model could take in a user query (prompt) and output a response that would most likely follow that prompt." — Ch 1

## Concrete example from the chapter

The book's recurring worked model is **`microsoft/Phi-3-mini-4k-instruct`** (see [[Phi3Mini]]) — the `-instruct` suffix indicates the instruction-tuned variant, as distinct from the base Phi-3-mini that would only do next-token completion.

Ch 1's worked code formats prompts as a list of role-content dictionaries:

```python
messages = [
    {"role": "user", "content": "Create a funny joke about chickens."}
]
output = generator(messages)
```

The `role: "user"` framing is the visible signature of an instruct model — the model expects a conversational structure, not a raw completion prefix.

## Position in the training paradigm

The chapter's training-paradigm framing (per Figure 1-30):

> "Creating LLMs, in contrast [to classical ML], typically consists of at least two steps: ... Language modeling [pretraining] ... Fine-tuning."

Additional fine-tuning steps can align the model further with user preferences — the chapter forward-references Ch 12 for [[rlhf|RLHF]] / [[DirectPreferenceOptimization|DPO]] and related preference-alignment techniques.

## Connections

- [[CompletionModel]] — the base / un-instruction-tuned variant.
- [[GenerativeModel]] — the parent category.
- [[FoundationModel]] — the pretrained model instruction-tuning starts from.
- [[FineTuning]] — the mechanism that produces instruct models.
- [[pretraining]] — the first training phase.
- [[posttraining]] — the second training phase, which Ch 1 sometimes calls fine-tuning.
- [[InstructionTuning]] — the technical training procedure.
- [[ChatTemplate]] / [[ChatML]] — the prompt structuring conventions instruct models expect.
- [[rlhf|RLHF]] / [[DirectPreferenceOptimization|DPO]] — further-alignment techniques downstream of instruction tuning.
- [[Phi3Mini]] / [[Llama3_8BInstruct]] / [[Mistral7BInstructV02]] / [[ChatGPT]] — example instruct models.
- [[hands-on-llm-ch01-introduction-to-llms]] — primary source.
