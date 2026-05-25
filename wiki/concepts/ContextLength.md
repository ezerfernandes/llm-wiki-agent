---
title: "Context Length"
type: concept
tags: [llm, inference, capacity, generation]
sources: [hands-on-llm-ch01-introduction-to-llms, ai-engineering-ch05-prompt-engineering, hands-on-llm-ch03-looking-inside-llms, hands-on-llm-ch07-advanced-text-generation]
last_updated: 2026-05-23
---

# Context Length

The **maximum number of tokens** an LLM can process in a single forward pass. Also called **context window**. Introduced as a defining property of [[GenerativeModel|generative LLMs]] in *[[HandsOnLLM|Hands-On LLMs]]* ([[hands-on-llm-ch01-introduction-to-llms|Ch 1]]):

> "A vital part of these completion models is something called the context length or context window. The context length represents the maximum number of tokens the model can process. ... A large context window allows entire documents to be passed to the LLM. Note that due to the autoregressive nature of these models, the current context length will increase as new tokens are generated." — Ch 1

## Why it matters

- **Document-scale work depends on it.** Long context lets entire articles, contracts, or codebases fit in a single prompt — the substrate for in-context learning, [[rag|RAG]] over large retrieved passages, and long-form code generation.
- **It bounds the maximum sequence the [[selfattention|self-attention]] mechanism processes.** Standard attention is O(n²) in sequence length; doubling context length quadruples attention compute and memory. This is the structural reason context-length extension is engineering-expensive.
- **For autoregressive generation, the *used* context length grows during decoding.** Each generated token is appended to the input for the next step — so a 4K-context model running a long generation will hit the limit if input + output exceeds 4K.

## Typical values (as of 2024)

The chapter (and the broader wiki — see [[transformer]] for the Llama 2 / Llama 3 context-length table) implies a wide spread:

- [[Phi3Mini|Phi-3-mini-4k-instruct]] — **4K tokens** (the `4k` in the model name).
- [[Llama|Llama 2]] family — **4K** (per the wiki's existing Transformer page).
- [[Llama|Llama 3]] family — **128K**.
- Frontier proprietary models — **200K+** ([[anthropic|Claude]]), **1M+** ([[gemini|Gemini]]).

## Transformer alternatives and context length

Ch 1 introduces [[Mamba]] and [[RWKV]] as 2023-era Transformer-alternative architectures that *"attempt to reach Transformer-level performance with additional advantages, like larger context windows or faster inference."* The structural reason: state-space models (Mamba) and modernized RNNs (RWKV) have linear (not quadratic) inference scaling, so they don't pay the O(n²) attention penalty for long sequences. Caveat per the wiki's existing [[Mamba]] / [[RWKV]] pages: *no context-length limit ≠ strong long-context performance* — architectural support is necessary but not sufficient.

## Connections

- [[GenerativeModel]] / [[CompletionModel]] — the model class context length is a property of.
- [[Tokenization]] — context length is measured in tokens.
- [[transformer|Transformer]] — the dominant architecture whose attention cost scales O(n²) in context length.
- [[Mamba]] / [[RWKV]] — Transformer alternatives that target larger context.
- [[selfattention|Self-attention]] — the mechanism that makes long context expensive.
- [[FlashAttention]] / [[ContinuousBatching]] — engineering techniques that mitigate the O(n²) cost.
- [[rag|RAG]] — the technique for handling information that doesn't fit in the context window.
- [[hands-on-llm-ch01-introduction-to-llms]] — primary source for the term.

## From [[ai-engineering-ch05-prompt-engineering|AI Engineering Ch 5]]

Ch 5 provides the headline **2,000× growth chart**:

> "Context length expansion soon became a race among model providers and practitioners. Figure 5-2 shows how quickly the context length limit is expanding. Within five years, it grew 2,000 times from GPT-2's 1K context length to Gemini-1.5 Pro's 2M context length." — Ch 5

**Reference data points**:
- The first three GPT generations had 1K, 2K, and 4K context lengths respectively — *"barely long enough for a college essay and too short for most legal documents or research papers."*
- 100K context length ≈ a moderate-sized book.
- *AI Engineering* itself is ≈120,000 words ≈ 160,000 tokens — fits in 200K-context models.
- 2M context length ≈ 2,000 Wikipedia pages or a reasonably complex codebase such as PyTorch.

**Important caveat — advertised context ≠ usable context.** Ch 5 uses the [[NeedleInAHaystack|NIAH]] test (Liu et al. 2023) and [[RULERBenchmark|RULER]] (Hsieh et al. 2024) to demonstrate the [[MiddleContextDegradation|"lost in the middle"]] phenomenon: models retrieve information much better at the start and end of long prompts than in the middle.

> "If the model's performance grows increasingly worse with a longer context, then perhaps you should find a way to shorten your prompts." — Ch 5

This means context-length-driven application architecture decisions (e.g., "we'll just fit all the docs in the prompt") need to be validated against task-specific NIAH/RULER tests — not against the marketing-number context length.

## From [[hands-on-llm-ch03-looking-inside-llms|*Hands-On LLMs* Ch 3]]

Ch 3 re-frames context length as the **count of [[TokenStream|token-processing streams]]** through the model:

> "Current Transformer models have a limit for how many tokens they can process at once. That limit is called the model's context length. A model with 4K context length can only process 4K tokens and would only have 4K of these streams." — Ch 3

This grounding makes precise why long context is expensive: each stream carries a `d_model`-sized vector through every Transformer block. With [[GroupedQueryAttention|GQA]] / [[multiqueryattention|MQA]] + [[KVCache|KV cache]] + [[FlashAttention|FlashAttention]] the per-stream cost is reduced — these are the engineering levers behind modern long-context models. [[SequencePacking|Sequence packing]] (the training-time efficiency technique covered in Ch 3) is how training makes use of these streams without wasting compute on padding.

## From [[hands-on-llm-ch07-advanced-text-generation|*Hands-On LLMs* Ch 7]]

Ch 7 makes context length **the operational bound on conversation memory**. The three [[LangChain]] memory classes the chapter walks ([[ConversationBufferMemory]] / [[ConversationBufferWindowMemory]] / [[ConversationSummaryMemory]]) are three concrete strategies for **trading conversation tokens against context length**:

| Strategy | Token usage | Bound |
|---|---|---|
| `ConversationBufferMemory` | Full history | Hits context length quickly |
| `ConversationBufferWindowMemory(k)` | Last k turns | Bounded regardless of conversation length |
| `ConversationSummaryMemory` | Single rolling summary | Bounded; LM-call overhead |

Ch 7's worked example uses [[LangChainLlamaCpp|`LlamaCpp`]] with `n_ctx=2048` (a 2K context window) — explicit in the code listings. The choice motivates the chapter's interest in windowed and summarized memory: 2K is small enough that buffer memory genuinely exhausts in tutorial-length conversations.
