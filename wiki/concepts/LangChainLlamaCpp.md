---
title: "langchain.LlamaCpp"
type: concept
tags: [langchain, llamacpp, gguf, local-inference, model-loader]
sources: [hands-on-llm-ch07-advanced-text-generation]
last_updated: 2026-05-23
---

# `langchain.LlamaCpp`

**`from langchain import LlamaCpp`** — [[LangChain]]'s wrapper around [[llamacpp|llama-cpp-python]] for loading [[GGUF]]-quantized models behind LangChain's universal `llm.invoke(prompt)` interface. The first model-loader primitive in [[hands-on-llm-ch07-advanced-text-generation|*Hands-On LLMs* Ch 7]].

## Canonical signature

```python
from langchain import LlamaCpp

llm = LlamaCpp(
    model_path="Phi-3-mini-4k-instruct-fp16.gguf",
    n_gpu_layers=-1,    # -1 = all layers on GPU; 0 = CPU-only
    max_tokens=500,
    n_ctx=2048,         # context window
    seed=42,
    verbose=False,
)
llm.invoke("Hi! My name is Maarten. What is 1 + 1?")
```

## The empty-output gotcha

The single most surprising thing Ch 7 surfaces about `LlamaCpp` — **`llm.invoke()` does NOT auto-apply the model's chat template**. Calling `llm.invoke("Hi! My name is Maarten. What is 1 + 1?")` on [[Phi3Mini|Phi-3]] returns an **empty string** because the raw prompt has no `<s><|user|>...<|end|><|assistant|>` wrapping. Per Ch 7:

> *"Note that the output is empty. To use this LLM, we need to apply its prompt template. We can do this with `PromptTemplate`."*

This is a **structural difference** from `transformers.pipeline`, which auto-applies the chat template via `apply_chat_template`. The downstream consequence: every `LlamaCpp`-using application must explicitly wrap inputs in the model's [[ChatTemplate|chat template]] via [[PromptTemplate|PromptTemplate]] — this is the motivation for the first chain Ch 7 builds:

```python
template = """<s><|user|>
{input_prompt}<|end|>
<|assistant|>"""
prompt = PromptTemplate(template=template, input_variables=["input_prompt"])
basic_chain = prompt | llm
basic_chain.invoke({"input_prompt": "Hi! My name is Maarten. What is 1 + 1?"})
# Now produces actual output.
```

## Position in the stack

| Layer | Component |
|---|---|
| Application | [[LangChain]] chain / agent |
| Loader | **`langchain.LlamaCpp`** ← this page |
| Inference | [[llamacpp|llama-cpp-python]] (Python bindings) |
| Engine | [[llamacpp|llama.cpp]] (C++ GGUF runtime) |
| Model | [[GGUF]]-quantized weights |

## Connections

- [[LangChain]] — the framework providing this loader.
- [[llamacpp]] — the underlying inference engine.
- [[GGUF]] — the model format LlamaCpp loads.
- [[Phi3Mini]] — Ch 7's worked model loaded through LlamaCpp.
- [[PromptTemplate]] — required to wrap inputs in the [[ChatTemplate|chat template]] (LlamaCpp doesn't auto-apply it).
- [[Quantization]] — the compression that makes GGUF small enough to run locally.
- [[LCEL]] — the `prompt | llm` composition that LlamaCpp participates in.
- [[hands-on-llm-ch07-advanced-text-generation]] — primary source.

## From Hands-On LLMs Ch 7

Ch 7's Model-I/O primitive. The chapter uses it to load `Phi-3-mini-4k-instruct-fp16.gguf` for all of the chains and memory examples, then switches to `ChatOpenAI` for the agent example (where Phi-3-mini is *"not powerful enough to follow complex instructions"*). The **empty-output behavior** is the chapter's most pedagogically loaded gotcha — it forces the reader to confront chat-template plumbing explicitly and motivates the [[PromptTemplate]] abstraction immediately rather than as an afterthought.
