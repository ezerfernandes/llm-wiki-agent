---
title: "llama.cpp"
type: entity
tags: [tool]
sources: [leh-ch08-inference-optimization, hands-on-llm-ch01-introduction-to-llms, hands-on-llm-ch06-prompt-engineering, hands-on-llm-ch07-advanced-text-generation]
last_updated: 2026-05-23
---

## What it is
Open-source C/C++ LLM inference library; runs quantized models on CPU, Android, and GPU-offloaded setups using GGUF.

## In LLM Engineer's Handbook
llama.cpp (by [[GeorgiGerganov]], 2023) is the open-source C/C++ LLM inference library that runs on CPUs, Android, and GPUs (via CUBLAS/Metal offload). Defines the [[GGUF]] quantization file format dominant in community-quantized models on Hugging Face. Per [[leh-ch08-inference-optimization]] it is compatible with [[FlashAttention2]] and [[SpeculativeDecoding]].

## In *Hands-On LLMs* Ch 1

[[hands-on-llm-ch01-introduction-to-llms|Ch 1]] of *Hands-On LLMs* names llama.cpp as one of three **backend packages** the book focuses on (alongside [[HuggingFace|Hugging Face]] Transformers and [[LangChain]]):

> "More specifically, we focus on backend packages. These are packages without a GUI (graphical user interface) that are created for efficiently loading and running any LLM on your device, such as llama.cpp, LangChain, and the core of many frameworks, Hugging Face Transformers." — Ch 1

llama.cpp is also the runtime layer underneath the GUI alternatives Ch 1 mentions ([[TextGenerationWebui]], [[KoboldCpp]], [[LMStudio]]).

## In *Hands-On LLMs* Ch 6 (runnable worked example)

[[hands-on-llm-ch06-prompt-engineering|Ch 6]] uses the Python binding **`llama-cpp-python`** as the wiki's first runnable demonstration of **[[GrammarConstrainedDecoding|grammar-constrained decoding]]** producing valid JSON. The chapter loads [[Phi3Mini|Phi-3-mini]] in [[GGUF]] form:

```python
from llama_cpp.llama import Llama
llm = Llama.from_pretrained(
    repo_id="microsoft/Phi-3-mini-4k-instruct-gguf",
    filename="*fp16.gguf",
    n_gpu_layers=-1, n_ctx=2048, verbose=False,
)
output = llm.create_chat_completion(
    messages=[{"role": "user", "content": "Create a warrior for an RPG in JSON format."}],
    response_format={"type": "json_object"},
    temperature=0,
)['choices'][0]['message']["content"]
```

The `response_format={"type": "json_object"}` parameter is an **OpenAI-API-compatible** option that `llama-cpp-python` honors by applying a JSON grammar at sampling time. *"It is generally used to efficiently load and use compressed models (through quantization; see Chapter 12) but we can also use it to apply a JSON grammar."* The chapter also gives the **VRAM-cleanup recipe** required before switching from the `transformers` model to the GGUF one:

```python
import gc, torch
del model, tokenizer, pipe
gc.collect(); torch.cuda.empty_cache()
```

The `n_gpu_layers=-1` parameter routes all model layers to GPU; `n_ctx=2048` is the context-window size. Ch 6 places llama.cpp / `llama-cpp-python` as the **quantized-inference + grammar-constrained-decoding** companion to the `transformers.pipeline` workflow used elsewhere in the book.

## In *Hands-On LLMs* Ch 7 (via LangChain's `LlamaCpp` wrapper)

[[hands-on-llm-ch07-advanced-text-generation|Ch 7]] uses [[LangChain]]'s **`from langchain import LlamaCpp`** wrapper rather than the raw `llama-cpp-python` API — Ch 7's `LlamaCpp` is the LangChain abstraction over the same library. The loader signature is similar to Ch 6's but wrapped for LangChain's `invoke()` interface:

```python
from langchain import LlamaCpp
llm = LlamaCpp(
    model_path="Phi-3-mini-4k-instruct-fp16.gguf",
    n_gpu_layers=-1,
    max_tokens=500,
    n_ctx=2048,
    seed=42,
    verbose=False
)
llm.invoke("Hi! My name is Maarten. What is 1 + 1?")  # empty output without a chat-template wrapper
```

**Critical Ch 7 finding**: LangChain's `LlamaCpp.invoke()` **does not auto-apply chat templates** — unlike `transformers.pipeline` which calls `apply_chat_template` under the hood, `LlamaCpp` returns empty output when the input is not pre-wrapped in Phi-3's `<s><|user|>...<|end|><|assistant|>` template. This is the chapter's motivation for [[PromptTemplate|LangChain `PromptTemplate`]] + chains as the first abstraction layer above raw LLM I/O.

Ch 7 also uses an **8-bit Phi-3 GGUF variant** (vs the 16-bit fp16 variant Ch 6 used) — *"cutting the memory requirements almost in half."* The chapter recommends *"at least 4-bit quantized models"* as a general rule, with 3-bit and 2-bit considered too lossy. Deep quantization treatment is deferred to Ch 12.
