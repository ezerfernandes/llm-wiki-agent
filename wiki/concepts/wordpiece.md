---
title: "WordPiece"
type: concept
tags: [concept, tokenization, subword]
sources: [1810.04805-bert, d2l-nlp-pretraining, hands-on-llm-ch02-tokens-and-embeddings]
last_updated: 2026-05-23
---

# WordPiece

Subword tokenization scheme used by [[BERT]] ([[1810.04805-bert]]) with a 30,000-token vocabulary. Originated in Google's neural machine translation system (Wu et al., 2016) and built on the same statistical principle as Byte-Pair Encoding: start from a character vocabulary, greedily merge the pair whose merge most improves the unigram likelihood of the training data, until the target vocab size is reached.

WordPiece sits between word-level tokenization (which fails on rare and morphologically rich words) and character-level (which produces very long sequences). Out-of-vocabulary words decompose into `##`-prefixed continuation pieces — e.g. `playing → play ##ing`. BERT's input representation sums the WordPiece **token embedding**, a **segment embedding** (A or B), and a learned **positional embedding** per position.

Closely related: BPE (Sennrich et al.), SentencePiece (Kudo & Richardson) — the latter is the de-facto choice in many later decoder-style LLMs, but the conceptual machinery is the same.

## From [[hands-on-llm-ch02-tokens-and-embeddings|*Hands-On LLMs* Ch 2]]

Ch 2 introduces WordPiece via the original Schuster & Nakajima paper *"Japanese and Korean voice search"* and uses [[bert|BERT]] (uncased + cased) as the canonical WordPiece example in its comparative tokenizer tour.

**Observed vocabulary sizes** in Ch 2's tour: **BERT-base uncased = 30,522**; **BERT-base cased = 28,996**.

**Five BERT [[SpecialToken|special tokens]]** Ch 2 enumerates: `[UNK]` ([[UnkToken|unknown]]), `[SEP]` ([[SepToken|separator]]), `[PAD]` ([[PadToken|padding]]), `[CLS]` ([[ClsToken|classification]]), `[MASK]` ([[MaskToken|masking]] for MLM training).

**Continuation marker**: `##` prefixes WordPiece pieces that connect to the preceding token without a space. The chapter's example: `capitalization` → `capital ##ization`. *"The `##` characters are used to indicate this token is a partial token connected to the token that precedes it. This is also a method to indicate where the spaces are, as it is assumed tokens without `##` in front have a space before them."*

The chapter highlights two WordPiece-specific failure modes in BERT's tokenizer:
- **Newlines disappear** — making BERT *"blind to information encoded in newlines (e.g., a chat log when each turn is in a new line)."*
- **Emoji and non-Latin characters become `[UNK]`** — *"The emoji and Chinese characters are gone and replaced with the `[UNK]` special token."* In contrast to [[GPT2|GPT-2]]'s byte-fallback [[BPE]].
