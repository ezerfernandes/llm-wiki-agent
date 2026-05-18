---
title: "SGLang"
type: entity
tags: [framework, llm, inference-server, gpu, oss]
sources: [dspy-language-models]
last_updated: 2026-05-17
---

# SGLang

**SGLang** ([docs.sglang.ai](https://docs.sglang.ai/), [github.com/sgl-project/sglang](https://github.com/sgl-project/sglang)) is an open-source **GPU inference server for open-weight LLMs**, distributed via `pip install "sglang[all]"` and launched as a long-running daemon that exposes an **OpenAI-compatible HTTP endpoint**. The recommended launch command is:

```bash
CUDA_VISIBLE_DEVICES=0 python -m sglang.launch_server --port 7501 \
    --model-path meta-llama/Meta-Llama-3-8B-Instruct
```

It pairs with `flashinfer` (`pip install flashinfer -i https://flashinfer.ai/whl/cu121/torch2.4/`) for fused attention kernels.

## Place in the wiki

SGLang is the **self-hosted-GPU deployment regime** [[DSPy]] explicitly recommends in [[dspy-language-models|the Language Models page]] (page 3 of 13 of DSPy *Learn*):

> *"To host accurate open models on your own GPU(s), we recommend SGLang."*

Because SGLang's server speaks OpenAI's wire protocol, DSPy reaches it through the **OpenAI-compatible-endpoint** pattern — prefix the model name with `openai/` and point `api_base` at the SGLang URL:

```python
lm = dspy.LM("openai/meta-llama/Meta-Llama-3-8B-Instruct",
             api_base="http://localhost:7501/v1",
             api_key="",
             model_type='chat')
dspy.configure(lm=lm)
```

This is the middle regime in [[dspy-language-models|the page's]] managed-API → self-hosted-GPU → local-laptop matrix: more accurate and faster than [[Ollama]], more controllable and cheaper-at-scale than a managed [[openai|OpenAI]] / [[anthropic|Anthropic]] API.

## Connections

- [[DSPy]] — framework that recommends SGLang for self-hosted-GPU deployment.
- [[dspy-language-models]] — canonical source for the DSPy-on-SGLang integration recipe and the "we recommend SGLang" quote.
- [[DSPyLM]] — the DSPy abstraction SGLang plugs into via the OpenAI-compatible-endpoint pattern.
- [[LiteLLM]] — provides the `openai/` prefix + `api_base` pattern SGLang relies on.
- [[Ollama]] — laptop-class peer regime [[dspy-language-models|the Language Models page]] pairs SGLang against.
