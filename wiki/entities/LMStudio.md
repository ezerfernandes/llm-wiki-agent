---
title: "LM Studio"
type: entity
tags: [tool, local-inference, gui, llm-frontend]
sources: [hands-on-llm-ch01-introduction-to-llms]
last_updated: 2026-05-23
---

# LM Studio

Desktop GUI application for running open-weights LLMs locally — provides a [[ChatGPT]]-like chat interface backed by [[llamacpp|llama.cpp]] / GGUF models running on the user's own hardware. Cited in [[hands-on-llm-ch01-introduction-to-llms|*Hands-On LLMs* Ch 1]] as one of three GUI alternatives to the book's primary code-first workflow:

> "Sometimes you just want a ChatGPT-like interface with a local LLM. Fortunately, there are many incredible frameworks that allow for this. A few examples include text-generation-webui, KoboldCpp, and LM Studio." — Ch 1

The book itself uses Python + `transformers` rather than GUIs, but mentions LM Studio for readers who want a turn-key local-chat experience.

## Connections

- [[TextGenerationWebui]] / [[KoboldCpp]] — sibling local-LLM GUIs cited together in Ch 1.
- [[llamacpp]] — the inference backend LM Studio commonly ships.
- [[HuggingFace]] — the model hub LM Studio pulls weights from.
- [[HandsOnLLM]] / [[hands-on-llm-ch01-introduction-to-llms]] — the source citing it.
