---
title: "Prompt-Based Adaptation"
type: concept
tags: [ai-engineering, adaptation, prompt-engineering, rag]
sources: [ai-engineering-ch01-intro]
last_updated: 2024-12-04
---

# Prompt-Based Adaptation

[[ModelAdaptation|Model adaptation]] techniques that **do not update the model's weights** — adaptation is achieved entirely through what you send into the model's context window. Per [[ai-engineering-ch01-intro|*AI Engineering* Ch 1]]:

> *"Prompt-based techniques, which include prompt engineering, adapt a model without updating the model weights. You adapt a model by giving it instructions and context instead of changing the model itself."*

## The two main techniques

1. **[[PromptEngineering|Prompt engineering]]** — instructions, examples, system messages, output-format specs.
2. **[[rag|RAG]]** — supplement instructions with retrieved data (database lookups, document chunks, search results).

## Why teams start here

- **Cheap to iterate**: a prompt change costs nothing in training compute.
- **Low data requirements**: often a handful of examples suffices.
- **Easy to compare models**: the same prompt can be sent to any model exposed through an API — lets you sample many models before committing.

> *"Many successful applications have been built with just prompt engineering. Its ease of use allows you to experiment with more models, which increases your chance of finding a model that is unexpectedly good for your applications."* — Ch 1

## When prompt-based isn't enough

- **Complex tasks** the base model can't reliably do regardless of prompt.
- **Strict performance bars** — quality, latency, or cost requirements that prompt-only solutions can't meet.
- **Tasks not seen during pretraining** — you can't prompt-engineer a model into capabilities it never learned.

In those cases, [[FineTuning|finetuning]] is required.

## Connections

- [[ModelAdaptation]] — the parent.
- [[PromptEngineering]] / [[rag]] — the two concrete techniques.
- [[FineTuning]] — the alternative when prompt-based is insufficient.
- [[AIEngineering]] — the discipline using these techniques.
- [[ai-engineering-ch01-intro]] — primary source.
