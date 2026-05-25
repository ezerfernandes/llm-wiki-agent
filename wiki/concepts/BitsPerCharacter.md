---
title: "Bits-per-Character (BPC)"
type: concept
tags: [language-modeling, evaluation, information-theory, metric]
sources: [ai-engineering-ch03-evaluation-methodology]
last_updated: 2024-12-04
---

# Bits-per-Character (BPC)

**Bits-per-character (BPC)** is a normalized form of [[CrossEntropy|cross entropy]] in which the total bits the language model needs to encode a sequence are divided by the *number of characters* in that sequence. Per [[ai-engineering-ch03-evaluation-methodology|*AI Engineering* Ch 3]], BPC addresses the problem that **different models tokenize differently** — one model's "token" might be a word, another's might be a subword — so raw bits-per-token isn't comparable across models. *"If the number of bits per token is 6 and on average, each token consists of 2 characters, the BPC is 6/2 = 3."*

## Why character-normalization isn't enough

BPC standardizes across tokenization schemes but still depends on the **character-encoding scheme**: with ASCII, each character is 7 bits, but with UTF-8 a character can take anywhere from 8 to 32 bits. This is the structural reason [[BitsPerByte|bits-per-byte (BPB)]] is the more cross-encoding-comparable choice for modern LMs that operate over UTF-8 text.

## Position in the four-metric family

[[ai-engineering-ch03-evaluation-methodology|Ch 3]] presents BPC alongside [[CrossEntropy|cross entropy]], [[Perplexity|perplexity]], and [[BitsPerByte|BPB]] as **four variants of the same underlying quantity**. *"If you know the value of one, you can compute the other three, given the necessary information."*

## Connections

- [[ai-engineering-ch03-evaluation-methodology]] — primary source.
- [[CrossEntropy]] — what BPC normalizes.
- [[BitsPerByte]] — the byte-normalized sibling; more cross-encoding-comparable.
- [[Perplexity]] — the exponentiated form.
- [[LanguageModel]] — what these metrics evaluate.
- [[Tokenization]] — the difference BPC normalizes away.
