---
title: "Together AI"
type: entity
tags: [company, llm, inference-provider, managed-api]
sources: [dspy-language-models]
last_updated: 2026-05-17
---

# Together AI

**Together AI** ([together.ai](https://www.together.ai/)) is a managed-API LLM inference provider hosting open-weight models (Llama family, Mistral family, Qwen family, and others) behind a unified HTTP API. Reached on the wiki only as one of the managed-provider examples in [[dspy-language-models|the DSPy Language Models page]] (page 3 of 13 of DSPy *Learn*):

```python
lm = dspy.LM('together_ai/togethercomputer/llama-2-70b-chat',
             api_key='TOGETHERAI_API_KEY')
```

Routed through [[LiteLLM]] under DSPy's [[DSPyLM|`dspy.LM`]] facade.

## Connections

- [[DSPy]] — uses Together AI as one of the [[DSPyLM|`dspy.LM`]]-supported managed providers.
- [[dspy-language-models]] — canonical source recording the integration.
- [[LiteLLM]] — provides the `together_ai/` model-string convention.
- [[DSPyLM]] — the DSPy abstraction Together AI plugs into.
