---
title: "SGLang"
type: entity
tags: [framework, llm, inference-server, gpu, oss]
sources: [dspy-language-models, papillon-colab-tutorial]
last_updated: 2026-05-24
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

## Receipt as DSPy serving backend for [[PAPILLON]]

The [[papillon-colab-tutorial|Columbia-NLP-Lab PAPILLON Colab]] is the **first wiki receipt of SGLang serving a [[CompoundAISystem|compound AI system]] in a tutorial-grade DSPy pipeline.** Default port `7501`, paired with `flashinfer` from `https://flashinfer.ai/whl/cu121/torch2.4/` (cu121 / torch 2.4 wheel index). The local LM is addressed with a **triple-segment identifier** — `openai/sglang/Llama-3.1-8B-Instruct` — where the middle `sglang/` segment is **author-chosen labeling for traceability** rather than a [[LiteLLM]] convention. The DSPy program ([[PAPILLON]]) uses this local-trusted LM for both `CreateOnePrompt` ([[chainofthought|ChainOfThought]]) and `InfoAggregator` ([[DSPyPredict|Predict]]) modules; GPT-4o-mini is the untrusted external LM that sits between the two trainable modules. **First wiki demonstration of SGLang as the local-trusted-LM side of an untrusted-external-LM compound AI program.**

## Connections

- [[DSPy]] — framework that recommends SGLang for self-hosted-GPU deployment.
- [[dspy-language-models]] — canonical source for the DSPy-on-SGLang integration recipe and the "we recommend SGLang" quote.
- [[papillon-colab-tutorial]] — **first wiki tutorial-grade DSPy receipt of SGLang** as the local-trusted-LM serving backend for a compound AI system ([[PAPILLON]] on [[PUPA]]); `Llama-3.1-8B-Instruct` on port 7501 with `flashinfer` cu121/torch2.4 wheel.
- [[DSPyLM]] — the DSPy abstraction SGLang plugs into via the OpenAI-compatible-endpoint pattern.
- [[LiteLLM]] — provides the `openai/` prefix + `api_base` pattern SGLang relies on.
- [[Ollama]] — laptop-class peer regime [[dspy-language-models|the Language Models page]] pairs SGLang against.
- [[PAPILLON]] — the canonical compound AI program hosted on SGLang in the [[papillon-colab-tutorial|Columbia-NLP-Lab Colab tutorial]].
