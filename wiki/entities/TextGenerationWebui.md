---
title: "text-generation-webui"
type: entity
tags: [tool, local-inference, gui, llm-frontend, open-source]
sources: [hands-on-llm-ch01-introduction-to-llms]
last_updated: 2026-05-23
---

# text-generation-webui

Open-source Gradio-based web UI for running and chatting with local LLMs — maintained by oobabooga (the project is often referred to as "the oobabooga UI"). Supports multiple backends (Hugging Face transformers, [[llamacpp|llama.cpp]], ExLlamaV2, AutoGPTQ, AutoAWQ, etc.) and is widely used as the *Stable Diffusion WebUI for LLMs* — a community-favorite hub for trying any HF-hosted model in a browser. Cited in [[hands-on-llm-ch01-introduction-to-llms|*Hands-On LLMs* Ch 1]] as one of three GUI alternatives to the book's primary code-first workflow:

> "Sometimes you just want a ChatGPT-like interface with a local LLM. Fortunately, there are many incredible frameworks that allow for this. A few examples include text-generation-webui, KoboldCpp, and LM Studio." — Ch 1

## Connections

- [[KoboldCpp]] / [[LMStudio]] — sibling local-LLM GUIs cited together in Ch 1.
- [[llamacpp]] — one of its supported inference backends.
- [[HuggingFace]] — the model hub it pulls weights from.
- [[HandsOnLLM]] / [[hands-on-llm-ch01-introduction-to-llms]] — the source citing it.
