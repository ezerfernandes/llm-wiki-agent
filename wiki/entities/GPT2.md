---
title: "GPT-2"
type: entity
tags: [model, llm, openai, gpt, generative-model]
sources: [hands-on-llm-ch01-introduction-to-llms, hands-on-llm-ch02-tokens-and-embeddings, hands-on-llm-ch09-multimodal-llms]
last_updated: 2026-05-23
---

# GPT-2

[[openai|OpenAI's]] **1.5-billion-parameter** autoregressive language model ([[AlecRadford|Radford]], Wu, Child, Luan, Amodei & Sutskever, 2019 — *"Language Models are Unsupervised Multitask Learners"*). The second generation of the [[GPT]] family, **10× larger than [[GPT|GPT-1]]** (117M params), trained on **WebText** — a corpus derived from Reddit-link-filtered [[CommonCrawl|Common Crawl]] (links with ≥3 upvotes as a proxy for "links people care about").

GPT-2 established the **"scale is the architecture"** thesis later formalized by [[2001.08361-scaling-laws|Kaplan et al. 2020]] — demonstrating that zero-shot task transfer emerges purely from scale of the next-token-prediction objective, with no task-specific supervision.

## In *Hands-On LLMs* Ch 1

[[hands-on-llm-ch01-introduction-to-llms|Ch 1]] cites GPT-2 as **the model that produced articles indiscernible from human-written ones**:

> "From 2012 onwards, developments in building AI systems (using deep neural networks) accelerated so that by the end of the decade, they yielded the first software system able to write articles indiscernible from those written by humans. This system was an AI model called Generative Pre-trained Transformer 2, or GPT-2." — Ch 1 (chapter opening)

And in the scale-history sequence:

> "As illustrated in Figure 1-25, GPT-2 had 1.5 billion parameters and GPT-3 used 175 billion parameters quickly followed." — Ch 1

## Position in the GPT scaling history

| Model | Year | Parameters |
|---|---|---|
| [[GPT|GPT-1]] | 2018 | 117M |
| **GPT-2** | **2019** | **1.5B** |
| [[GPT3|GPT-3]] | 2020 | 175B |
| [[GPT4|GPT-4]] | 2023 | (undisclosed, much larger) |

The chapter uses the scale-up arc to motivate the claim that *"more parameters greatly influence the capabilities and performance of language models."*

## Connections

- [[openai|OpenAI]] — model provider.
- [[GPT]] — model family.
- [[GPT3]] / [[GPT4]] — successor models.
- [[AlecRadford]] — first author.
- [[CommonCrawl]] — primary training-data source.
- [[GenerativeModel]] / [[CompletionModel]] / [[AutoregressiveLanguageModel]] — model class.
- [[transformer|Transformer]] — architecture.
- [[2001.08361-scaling-laws]] — the scaling-laws paper that formalized GPT-2's empirical observation.
- [[hands-on-llm-ch01-introduction-to-llms]] — primary source citing GPT-2 in this wiki.

## In *Hands-On LLMs* Ch 2 (tokenizer)

[[hands-on-llm-ch02-tokens-and-embeddings|Ch 2]] surveys GPT-2's tokenizer in the comparative tour:

- **Method**: [[BPE]] (Sennrich et al., *"Neural machine translation of rare words with subword units"*).
- **Vocabulary size**: 50,257.
- **Special tokens**: `<|endoftext|>`.

**Behaviors observed:**
- **Preserves newlines and capitalization** (unlike BERT uncased).
- **Byte-level fallback** — the 🎵 emoji is decomposed into 3 byte tokens (IDs 8582, 236, 113) that round-trip via `tokenizer.decode`. The first wiki documentation of GPT-2's byte-fallback behavior.
- **Whitespace inefficiency** — 4 spaces become 3 tokens (token 220 repeated), and 2 tabs become 2 separate tokens. The GPT-4 successor fixes this by encoding whitespace runs as single tokens.
- **Inconsistent numeric tokenization** — `870` is one token; `871` is two (`8` + `71`). The chapter flags this as the motivation behind [[StarCoder2]]'s per-digit tokenization choice.

## From [[hands-on-llm-ch09-multimodal-llms|*Hands-On LLMs* Ch 9]]

Ch 9 surfaces a structural reuse of **`GPT2TokenizerFast`** outside the GPT-2 model itself: it is the tokenizer wrapped by [[BLIP2|BLIP-2]]'s `Blip2Processor` because BLIP-2's LLM backbone is OPT-2.7b (from [[meta]]) which uses the GPT-2-family BPE byte-level encoder. Inspection of `blip_processor.tokenizer` shows `vocab_size=50265`, BOS/EOS/UNK = `</s>`, PAD = `<pad>`. Worked tokenization of *"Her vocalization was remarkably melodic"* → `['</s>', 'Her', 'Ġvocal', 'ization', 'Ġwas', 'Ġremarkably', 'Ġmel', 'odic']`.

Ch 9 also codifies the **Ġ-as-space byte-level convention** GPT-2's tokenizer introduced — *"this is actually supposed to be a space. However, an internal function takes characters in certain code points and moves them up by 256 to make them printable. As a result, the space (code point 32) becomes Ġ (code point 288)."* This is the wiki's first explicit narration of the [[BPE|BPE]] byte-level encoder's code-point-shift mechanism, with GPT-2 cited as the originating implementation.
