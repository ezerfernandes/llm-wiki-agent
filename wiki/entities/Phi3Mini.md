---
title: "Phi-3-mini"
type: entity
tags: [model, llm, microsoft, small-model, mit-licensed]
sources: [hands-on-llm-ch01-introduction-to-llms, hands-on-llm-ch02-tokens-and-embeddings, hands-on-llm-ch03-looking-inside-llms, hands-on-llm-ch06-prompt-engineering, hands-on-llm-ch07-advanced-text-generation, hands-on-llm-ch08-semantic-search-and-rag]
last_updated: 2026-05-23
---

# Phi-3-mini

[[microsoft|Microsoft's]] **3.8-billion-parameter** language model — *"a relatively small but quite performant model"* (Abdin et al., 2024, *"Phi-3 technical report: A highly capable language model locally on your phone"*, arXiv:2404.14219). The variant used as the recurring worked model in *Hands-On LLMs* ([[hands-on-llm-ch01-introduction-to-llms]]) is `microsoft/Phi-3-mini-4k-instruct` — the 4K-context instruction-tuned chat variant.

## Why the book chose it

1. **Small enough for "GPU-poor" readers.** Runs on devices with less than 8 GB of VRAM; with [[Quantization|quantization]] (covered in book Chs 7 and 12), under 6 GB — fitting the free [[GoogleColab|Google Colab]] T4 (16 GB VRAM) target.
2. **MIT-licensed.** *"the model is licensed under the MIT license, which allows the model to be used for commercial purposes without constraints."*
3. **Performant despite small size.** Strong relative scores on standard benchmarks make it a credible representative of "what a 4-billion-param model can do in 2024."

## Worked code from Ch 1

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained(
    "microsoft/Phi-3-mini-4k-instruct",
    device_map="cuda",
    torch_dtype="auto",
    trust_remote_code=True,
)
tokenizer = AutoTokenizer.from_pretrained("microsoft/Phi-3-mini-4k-instruct")
```

Plus the `pipeline()` wrapper:

```python
from transformers import pipeline

generator = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    return_full_text=False,
    max_new_tokens=500,
    do_sample=False,
)
```

`do_sample=False` makes the model always pick the most probable next token — [[GreedyDecoding|greedy decoding]]. The chapter forward-references Ch 6 for sampling strategies.

## First generated output in the book

Prompt: *"Create a funny joke about chickens."*

Output: *"Why don't chickens like to go to the gym? Because they can't crack the egg-sistence of it!"*

## Connections

- [[microsoft|Microsoft]] — model provider.
- [[HuggingFace]] — model hub (`microsoft/Phi-3-mini-4k-instruct`).
- [[HandsOnLLM]] — the book that uses Phi-3-mini as its recurring worked model.
- [[hands-on-llm-ch01-introduction-to-llms]] — Ch 1 introduces it.
- [[Quantization]] — the technique that brings VRAM under 6 GB.
- [[GoogleColab]] — the assumed runtime environment.
- [[GreedyDecoding]] — the default sampling strategy in Ch 1's example.
- [[InstructModel]] — Phi-3-mini-4k-instruct is the instruction-tuned variant.

## In *Hands-On LLMs* Ch 2 (tokenizer)

[[hands-on-llm-ch02-tokens-and-embeddings|Ch 2]] surveys Phi-3's tokenizer — which **reuses the [[Llama|Llama 2]] tokenizer** with added chat-role tokens:

- **Method**: [[BPE]].
- **Vocabulary size**: 32,000 (inherited from Llama 2).
- **Special tokens**:
  - `<|endoftext|>` — end of generation.
  - **Chat role tokens** added by Phi-3 on top of Llama 2: `<|user|>`, `<|assistant|>`, `<|system|>`. *"As chat LLMs rose to popularity in 2023, the conversational nature of LLMs started to be a leading use case. Tokenizers have been adapted to this direction by the addition of tokens that indicate the turns in a conversation and the roles of each speaker."*

Ch 2's worked tokenizer example uses Phi-3-mini to demonstrate the basic tokenize-then-decode round-trip. The prompt *"Write an email apologizing to Sarah for the tragic gardening mishap. Explain how it happened.`<|assistant|>`"* tokenizes as `[<s>, Write, an, email, apolog, izing, to, Sarah, for, the, trag, ic, garden, ing, m, ish, ap, ., Exp, lain, how, it, happened, ., <|assistant|>]` — illustrating subword decomposition for `apologizing` → `apolog ##izing`-style, `tragic` → `trag ic`, `mishap` → `m ish ap`.

## In *Hands-On LLMs* Ch 3 (architectural dissection)

[[hands-on-llm-ch03-looking-inside-llms|Ch 3]] uses Phi-3-mini as **the worked model for the Transformer-internals dissection**. The full PyTorch module print-out from `print(model)`:

```
Phi3ForCausalLM(
  (model): Phi3Model(
    (embed_tokens): Embedding(32064, 3072, padding_idx=32000)
    (embed_dropout): Dropout(p=0.0, inplace=False)
    (layers): ModuleList(
      (0-31): 32 x Phi3DecoderLayer(
        (self_attn): Phi3Attention(
          (o_proj): Linear(in_features=3072, out_features=3072, bias=False)
          (qkv_proj): Linear(in_features=3072, out_features=9216, bias=False)
          (rotary_emb): Phi3RotaryEmbedding()
        )
        (mlp): Phi3MLP(
          (gate_up_proj): Linear(in_features=3072, out_features=16384, bias=False)
          (down_proj): Linear(in_features=8192, out_features=3072, bias=False)
          (activation_fn): SiLU()
        )
        (input_layernorm): Phi3RMSNorm()
        (resid_attn_dropout): Dropout(p=0.0, inplace=False)
        (resid_mlp_dropout): Dropout(p=0.0, inplace=False)
        (post_attention_layernorm): Phi3RMSNorm()
      )
    )
    (norm): Phi3RMSNorm()
  )
  (lm_head): Linear(in_features=3072, out_features=32064, bias=False)
)
```

Key dimensional facts:

- **Embedding table**: 32,064 tokens × 3,072-dim embeddings.
- **32 × `Phi3DecoderLayer`** (the stack of Transformer blocks).
- **Fused QKV projection**: `qkv_proj: Linear(3072 → 9216)` — the 3× factor packs [[QueryProjection|Q]], [[KeyProjection|K]], and [[ValueProjection|V]] projections into one matmul.
- **Output projection**: `o_proj: Linear(3072 → 3072)`.
- **[[RoPE|Rotary positional embedding]]**: `Phi3RotaryEmbedding` — applied at the attention step, not at input.
- **Gated MLP**: `gate_up_proj: Linear(3072 → 16384)` + `down_proj: Linear(8192 → 3072)` + `SiLU` activation — consistent with the [[SwiGLU|SwiGLU]] gated structure (the 16384 output splits into two 8192-dim streams; one is SiLU-gated against the other).
- **[[RMSNorm|RMSNorm]]** (`Phi3RMSNorm`) used for **both pre-attention and pre-MLP** normalization — the modern **[[PreNorm|pre-norm]]** placement.
- **[[LMHead|LM head]]**: `Linear(3072 → 32064, bias=False)`.

The Ch 3 worked example for `"The capital of France is"` produces `Paris` as the highest-probability next token via `lm_head_output[0, -1].argmax(-1)` over the `[1, 6, 32064]` logits tensor.

### KV-cache wall-clock measurement

On a [[GoogleColab|Colab]] T4 GPU generating 100 tokens with Phi-3-mini:
- `use_cache=True`: **4.5 s**
- `use_cache=False`: **21.8 s**

A ~5× speedup from caching K/V across decode steps — see [[KVCache|KV Cache]] for the full discussion. `use_cache` defaults to `True` in [[HuggingFace|Hugging Face]] Transformers.

### Position in the 2024-era block recipe

Phi-3-mini's architecture instantiates the modern Transformer block recipe: **pre-norm + [[RMSNorm]] + [[SwiGLU]] + [[RoPE]]** (with the attention head sharing tag depending on the exact Phi-3 release; the chapter's print-out only shows the fused `qkv_proj` shape, not whether K/V are shared across heads).

## In *Hands-On LLMs* Ch 6 (prompt engineering — including GGUF variant)

[[hands-on-llm-ch06-prompt-engineering|Ch 6]] uses Phi-3-mini as the substrate for prompt-engineering experiments. The chapter **introduces the GGUF variant** as a new runtime option:

```python
from llama_cpp.llama import Llama
llm = Llama.from_pretrained(
    repo_id="microsoft/Phi-3-mini-4k-instruct-gguf",
    filename="*fp16.gguf",
    n_gpu_layers=-1,
    n_ctx=2048,
    verbose=False,
)
```

This is the **wiki's first chapter-level demonstration** of running Phi-3-mini through [[llamacpp|`llama-cpp-python`]] rather than through `transformers` — required for the grammar-constrained-decoding worked example (`response_format={"type": "json_object"}`). Both runtimes use the same underlying weights; the [[GGUF]] format is the quantization-friendly serialization the llama.cpp ecosystem expects.

Ch 6 also surfaces the **chat-template rendering** for Phi-3 directly via `pipe.tokenizer.apply_chat_template(messages, tokenize=False)`:

```
<s><|user|>
Create a funny joke about chickens.<|end|>
<|assistant|>
```

This is the **wiki's most concrete worked example** of the [[ChatTemplate|chat-template]] machinery the [[Phi3Mini|Phi-3 tokenizer]]'s `<|user|>` / `<|assistant|>` / `<|end|>` special tokens enable. The `<|end|>` token also serves as the **stopping token** signaling when the model should halt generation.

The chapter's reasoning-prompting examples (CoT / self-consistency / tree-of-thought) all run on Phi-3-mini through `pipe()`, including the canonical cafeteria-apples problem where the model produces the step-by-step reasoning chain ending in *9 apples*.

## In *Hands-On LLMs* Ch 7 (LangChain chains + memory; **agent ceiling**)

[[hands-on-llm-ch07-advanced-text-generation|Ch 7]] uses an **8-bit Phi-3 GGUF** (vs Ch 6's fp16 variant — *"cutting the memory requirements almost in half"*) loaded via [[LangChain]]'s `LlamaCpp` wrapper:

```python
from langchain import LlamaCpp
llm = LlamaCpp(
    model_path="Phi-3-mini-4k-instruct-fp16.gguf",
    n_gpu_layers=-1, max_tokens=500, n_ctx=2048, seed=42, verbose=False,
)
```

Phi-3-mini handles **chains** and **memory** successfully across the chapter — the story-generation three-stage chain produces coherent title / character / story triples for *"a girl that lost her mother"*; `ConversationBufferMemory` and `ConversationSummaryMemory` both work with Phi-3-mini as both user-prompt LLM and summarization LLM.

**The capability ceiling is at agents.** For the [[react|ReAct]] agent example, Ch 7 explicitly switches from Phi-3-mini to [[ChatGPT|GPT-3.5-turbo]]: *"These autonomous processes generally require an LLM that is powerful enough to properly follow complex instructions. The LLM that we used thus far is relatively small and not sufficient to run these examples. Instead, we will be using OpenAI's GPT-3.5 model as it follows these complex instructions more closely."* This is the chapter's honest acknowledgment that the [[Phi3Mini|GPU-poor]] commitment has a ceiling — agents that require multi-step tool selection and complex reasoning currently need a more capable model. The chapter hedges: *"We would be anything but surprised if eventually smaller LLMs, like the one used in this chapter, would be capable enough to run this example."*

**Operational gotcha**: LangChain's `LlamaCpp.invoke()` does **not** auto-apply Phi-3's chat template (`<s><|user|>...<|end|><|assistant|>`) — unlike `transformers.pipeline`. The chapter demonstrates the empty-output failure mode: `llm.invoke("Hi! My name is Maarten. What is 1 + 1?")` returns `''`. This motivates the use of LangChain `PromptTemplate` as the first abstraction layer above raw `LlamaCpp` calls.
