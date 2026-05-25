---
title: "Word Tokenization"
type: concept
tags: [nlp, tokenization]
sources: [hands-on-llm-ch02-tokens-and-embeddings]
last_updated: 2026-05-23
---

# Word Tokenization

The simplest [[Tokenization|tokenization]] scheme: every token in the vocabulary is **one whole word**. Splits text on whitespace (and punctuation) and looks up each word in a fixed vocabulary.

## From [[hands-on-llm-ch02-tokens-and-embeddings|*Hands-On LLMs* Ch 2]]

> "This approach was common with earlier methods like word2vec but is being used less and less in NLP. Its usefulness, however, led it to be used outside of NLP for use cases such as recommendation systems, as we'll see later in the chapter." — Ch 2

The chapter names **two failure modes** that motivated the move to [[Subword|subword]] tokenization:

1. **Out-of-vocabulary words** — a word the tokenizer wasn't trained on becomes `[UNK]` and the model loses information.
2. **Vocabulary bloat** — *"a vocabulary that has a lot of tokens with minimal differences between them (e.g., apology, apologize, apologetic, apologist)."* Each inflectional form occupies a separate vocabulary slot.

Subword tokenization solves both by sharing a single `apolog` token across all the inflected forms (suffixes `-y`, `-ize`, `-etic`, `-ist` themselves become their own tokens).

## Where word tokenization survives

- **[[Word2Vec|word2vec]]** and its derivatives — pure word-level by construction.
- **[[Word2VecRecommender|Recommendation systems]]** — songs, products, pages as "words"; subword decomposition makes no sense for opaque IDs.
- **Some classical NLP pipelines** — POS tagging, dependency parsing on languages with explicit word boundaries.

## Connections

- [[Tokenization]] — parent.
- [[SubwordEmbedding]] — the modern subword-tokenization replacement.
- [[CharacterTokenization]] / [[ByteLevelTokenization]] — finer-grained alternatives.
- [[Word2Vec]] / [[BagOfWords]] — classical word-level methods.
- [[Word2VecRecommender]] — non-NLP application.
- [[hands-on-llm-ch02-tokens-and-embeddings]] — source page.
