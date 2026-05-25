---
title: "GPT-4"
type: concept
tags: [model, llm, openai, foundation-model, multimodal]
sources: [ai-engineering-ch01-intro, hands-on-llm-ch02-tokens-and-embeddings]
last_updated: 2026-05-23
---

# GPT-4

[[openai|OpenAI's]] flagship foundation model (release: March 2023), including the **GPT-4V** multimodal variant (text + images, system-carded September 2023). Underlies [[ChatGPT|ChatGPT]] and many downstream products. Cited throughout [[ai-engineering-ch01-intro|*AI Engineering* Ch 1]] as **the canonical reference foundation model** for the 2024 era of [[AIEngineering|AI engineering]].

Note: distinct from [[GPT4_1|GPT-4.1]] (April 2025 successor used in DSPy / MIPROv2 / GEPA evaluation work elsewhere in the wiki).

## Ch 1 appearances

- **Tokenization anchor**: GPT-4 vocabulary is **100,256**. Average token length ≈ ¾ of a word (100 tokens ≈ 75 words). GPT-4 tokenizes *"I can't wait to build AI applications"* into 9 tokens, splitting *"can't"* into `can` and `'t`.
- **GPT-4V system card (2023)** is cited for the quote: *"incorporating additional modalities (such as image inputs) into LLMs is viewed by some as a key frontier in AI research and development"* — used by Huyen to justify the term "foundation model" over "LLM" when modalities expand.
- **MMLU comparison**: GPT-4 scored **86.4%** on MMLU with 5-shot prompting in the December 2023 Gemini technical report — the baseline Google was trying to beat with Gemini Ultra's CoT@32 score of 90.04%. With 5-shot only, **GPT-4 outperforms Gemini**, which becomes Huyen's anchor anecdote for the prompt-format sensitivity of [[Evaluation|evaluation]] results.
- **Multimodal exemplar**: GPT-4V is named alongside [[ClaudeOpus47|Claude 3]] and [[gemini|Gemini]] as a model that handles both images and text — the trio that justifies the [[FoundationModel|foundation model]] umbrella.

## In *Hands-On LLMs* Ch 2 (tokenizer)

[[hands-on-llm-ch02-tokens-and-embeddings|Ch 2]] surveys GPT-4's tokenizer in the comparative tour:

- **Method**: [[BPE]] (same family as GPT-2, expanded vocabulary).
- **Vocabulary size**: a little over **100,000** (consistent with [[ai-engineering-ch01-intro|Huyen Ch 1]]'s 100,256).
- **Special tokens**: `<|endoftext|>` plus **[[FillInTheMiddle|fill-in-the-middle]] tokens** `<|fim_prefix|>`, `<|fim_middle|>`, `<|fim_suffix|>`.

**Behavioral differences from GPT-2** Ch 2 highlights:
- **Single token for whitespace runs** — *"the GPT-4 tokenizer represents the four spaces as a single token. In fact, it has a specific token for every sequence of whitespaces up to a list of 83 whitespaces."*
- **`elif` as a single token** — *"The Python keyword `elif` has its own token in GPT-4. Both this and the previous point stem from the model's focus on code in addition to natural language."*
- **More compact tokenization overall** — `CAPITALIZATION` is 2 tokens (vs GPT-2's 4); `tokens` is 1 token (vs GPT-2's 3).

The chapter positions GPT-4's tokenizer as the **canonical example of a vocabulary-size-up + domain-aware (code) tokenization choice** — directly enabled by the bigger vocab budget.

## Connections

- [[openai|OpenAI]] — developer.
- [[ChatGPT]] — the consumer-facing product GPT-4 powers.
- [[FoundationModel]] / [[LargeLanguageModel]] / [[MultimodalLLM]] — model class.
- [[gemini]] / [[claudeopus47]] — frontier peers.
- [[mmlu]] — primary benchmark cited in Ch 1.
- [[GPT4_1]] — successor model (April 2025).
- [[GPT2]] — direct ancestor; GPT-4's tokenizer extends GPT-2's BPE.
- [[FillInTheMiddle]] — the special-token scheme GPT-4 supports.
- [[ai-engineering-ch01-intro]] / [[hands-on-llm-ch02-tokens-and-embeddings]] — primary sources.
