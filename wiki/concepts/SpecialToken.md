---
title: "Special Token"
type: concept
tags: [nlp, tokenization, llm]
sources: [hands-on-llm-ch02-tokens-and-embeddings]
last_updated: 2026-05-23
---

# Special Token

A token in a [[Tokenizer|tokenizer's]] vocabulary that **does not represent natural-language text**. Instead, special tokens encode model-system protocol: where text begins / ends, how segments separate, which positions are padded or unknown, and (for chat / code / scientific models) what kind of payload follows.

## From [[hands-on-llm-ch02-tokens-and-embeddings|*Hands-On LLMs* Ch 2]]

Ch 2 enumerates the **common categories** of special tokens an LLM designer chooses among at model-design time:

- **Beginning-of-text** — `<s>` (Llama / Phi-3 / Galactica), `[CLS]` ([[bert|BERT]]).
- **End-of-text / end-of-generation** — `</s>` (T5 / Galactica), `<|endoftext|>` ([[GPT2|GPT-2]] / [[GPT4|GPT-4]] / [[StarCoder2]] / [[Phi3Mini|Phi-3]]).
- **Padding** — `[PAD]` (BERT), `<pad>` (Flan-T5 / Galactica). Used to align variable-length sequences to a fixed input size.
- **Unknown** — `[UNK]` (BERT), `<unk>` (Flan-T5 / Galactica). Falls back to this when the tokenizer encounters characters/words it can't represent.
- **Classification token** — `[CLS]` (BERT); the aggregate-sequence representation; see [[ClsToken]] / [[ClassificationToken]].
- **Separator** — `[SEP]` (BERT); separates the two segments of a sentence-pair input. *"used to separate sentences in some applications that require passing two sentences to a model (For example, in Chapter 8, we will use a `[SEP]` token to separate the text of the query and a candidate result.)"*
- **Masking** — `[MASK]` (BERT); the placeholder used during [[maskedlanguagemodel|masked-language-model]] training.

**Newer categories** that emerged with chat and code models:

- **[[ChatTemplate|Chat role tokens]]** — `<|user|>` / `<|assistant|>` / `<|system|>` ([[Phi3Mini|Phi-3]] / [[Llama]] 2 / [[GPT4|GPT-4]]) signal turn boundaries and speaker role.
- **[[FillInTheMiddle|Fill-in-the-middle (FIM)]] tokens** — `<|fim_prefix|>` / `<|fim_middle|>` / `<|fim_suffix|>` ([[GPT4|GPT-4]]), `<fim_prefix>` / `<fim_middle>` / `<fim_suffix>` / `<fim_pad>` ([[StarCoder2]]) — enable the model to complete code given both prefix and suffix context.
- **Code repository tokens** — `<filename>` / `<reponame>` / `<gh_stars>` ([[StarCoder2]]) disambiguate cross-file references in a multi-file repo.
- **Scientific tokens** — `[START_REF]` / `[END_REF]` ([[Galactica]]) wrap citations; `<work>` ([[Galactica]]) marks chain-of-thought reasoning spans.

> "LLM designer can add tokens that help better model the domain of the problem they're trying to focus on, as we've seen with Galactica's `<work>` and `[START_REF]` tokens." — *Hands-On LLMs* Ch 2

## Why they matter

Special tokens are **the protocol layer** between application code and the language model. Three failure modes the wiki has accumulated evidence for:

1. **Wrong [[ChatTemplate|chat template]]** silently degrades quality (per [[ai-engineering-ch05-prompt-engineering|AI Engineering Ch 5]] — *"Accidentally using the wrong template can lead to bewildering performance issues"*).
2. **Stripping the `<s>` / `[CLS]`** — many tokenizers add it automatically (the chapter's Phi-3 example starts with token ID 1, `<s>`); manually-built `input_ids` that omit it can produce subtly worse outputs.
3. **Mismatched `</s>` / `<|endoftext|>`** — generation that does not terminate on the expected end-of-text token will overrun the intended response.

## Connections

- [[Tokenizer]] / [[Tokenization]] — special tokens live in the tokenizer's vocabulary.
- [[ClsToken]] / [[ClassificationToken]] — the classification special token, expanded.
- [[SepToken]] / [[PadToken]] / [[UnkToken]] / [[MaskToken]] — per-token detail pages.
- [[ChatTemplate]] — how role tokens are composed into a full prompt.
- [[FillInTheMiddle]] — the GPT-4 / StarCoder2 code-completion training objective.
- [[bert]] / [[GPT2]] / [[GPT4]] / [[StarCoder2]] / [[Galactica]] / [[Phi3Mini]] — tokenizer-by-tokenizer special-token treatment.
- [[hands-on-llm-ch02-tokens-and-embeddings]] — the source page.
