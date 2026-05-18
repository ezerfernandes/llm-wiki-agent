---
title: "Ollama"
type: entity
tags: [tool, llm, local-inference, oss, laptop]
sources: [dspy-language-models]
last_updated: 2026-05-17
---

# Ollama

**Ollama** ([ollama.ai](https://ollama.ai/)) is an open-source tool for **running open-weight LLMs locally on a laptop or workstation**. Distributed as a single binary, it ships a local HTTP server (default port `11434`) plus a model-pull CLI; one-line install (`curl -fsSL https://ollama.ai/install.sh | sh`) and one-line run (`ollama run llama3.2:1b`) get a quantized open model serving on `http://localhost:11434`.

## Place in the wiki

Ollama is the **local-laptop deployment regime** [[DSPy]] explicitly supports in [[dspy-language-models|the Language Models page]] (page 3 of 13 of DSPy *Learn*). The recommended wiring is:

```python
import dspy
lm = dspy.LM('ollama_chat/llama3.2', api_base='http://localhost:11434', api_key='')
dspy.configure(lm=lm)
```

The `ollama_chat/` model-string prefix is the [[LiteLLM]] convention for routing through a running Ollama server. From DSPy's perspective, Ollama is interchangeable with [[openai|OpenAI]] / [[anthropic|Anthropic]] / [[SGLang]] — the entire program stays the same; only the [[DSPyLM|`dspy.LM`]] construction line changes. This is the laptop-end of [[dspy-language-models|the Language Models page's]] three-regime story: managed API → self-hosted GPU ([[SGLang]]) → local laptop (Ollama).

## Connections

- [[DSPy]] — framework that integrates Ollama as one of its supported [[DSPyLM|`dspy.LM`]] backends.
- [[dspy-language-models]] — canonical source for the DSPy-on-Ollama integration recipe.
- [[DSPyLM]] — the DSPy abstraction Ollama plugs into.
- [[LiteLLM]] — provides the `ollama_chat/` model-string convention.
- [[SGLang]] — the *next regime up* (self-hosted GPU) that [[dspy-language-models|the Language Models page]] pairs Ollama against.
