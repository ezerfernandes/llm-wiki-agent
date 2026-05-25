---
title: "Bits-per-Byte (BPB)"
type: concept
tags: [language-modeling, evaluation, information-theory, metric]
sources: [ai-engineering-ch03-evaluation-methodology]
last_updated: 2024-12-04
---

# Bits-per-Byte (BPB)

**Bits-per-byte (BPB)** is *"the number of bits a language model needs to represent one byte of the original training data"* ([[ai-engineering-ch03-evaluation-methodology|*AI Engineering* Ch 3]]). It standardizes [[CrossEntropy|cross-entropy]] reporting across **both tokenization schemes** ([[BitsPerCharacter|BPC]] already did this) **and character-encoding schemes** (which BPC did not).

## Computation

If a model's [[BitsPerCharacter|BPC]] is 3 and each character occupies ⅞ of a byte (7 bits, as in ASCII), then `BPB = 3 / (7/8) = 3.43`.

## Cross-entropy = compression efficiency

Per Ch 3: *"Cross entropy tells us how efficient a language model will be at compressing text. If the BPB of a language model is 3.43, meaning it can represent each original byte (8 bits) using 3.43 bits, this language model can compress the original training text to less than half the text's original size."*

This is the chapter's load-bearing interpretation of cross entropy — *language modeling is compression*. A model that achieves lower BPB on a corpus is, in an information-theoretic sense, a better compressor of that corpus.

## In the GPT-2 perplexity table

Ch 3 Table 3-1 reports BPB on the **enwiki8** benchmark for GPT-2 sizes:
- SOTA (pre-GPT-2): 0.99
- GPT-2 117M: 1.16
- GPT-2 345M: 1.01
- GPT-2 762M: 0.97
- GPT-2 1542M: **0.93**

The monotonic decrease with model size is the data the chapter uses to argue that **larger models give lower perplexity / BPB across the board** (OpenAI, 2018).

## Position in the four-metric family

[[ai-engineering-ch03-evaluation-methodology|Ch 3]] presents BPB alongside [[CrossEntropy|cross entropy]], [[Perplexity|perplexity]], and [[BitsPerCharacter|BPC]] as four variants of the same underlying quantity. BPB is the most-cross-comparable of the four.

## Connections

- [[ai-engineering-ch03-evaluation-methodology]] — primary source.
- [[CrossEntropy]] — what BPB normalizes.
- [[BitsPerCharacter]] — the character-normalized sibling.
- [[Perplexity]] — the exponentiated form.
- [[LanguageModel]] — what these metrics evaluate.
- [[ClaudeShannon]] — the information-theoretic origin (entropy = optimal-code length per symbol).
