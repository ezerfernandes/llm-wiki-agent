---
title: "Subword Embedding"
type: concept
tags: [nlp, embeddings, tokenization, morphology]
sources: [d2l-nlp-pretraining, hands-on-llm-ch02-tokens-and-embeddings]
last_updated: 2026-05-23
---

# Subword Embedding

Word-representation approach that decomposes each word into smaller pieces — **character-$n$-grams**, [[BPE|BPE]] merges, [[WordPiece]] pieces, or SentencePiece units — and represents the word as a (sum / lookup of the) embeddings of those pieces. Motivations:

- **Out-of-vocabulary (OOV)** robustness — never seen "tokenization" but seen "token" + "##ization"? Still get a representation.
- **Morphological sharing** — "helps", "helped", "helping" share their stem subword and so share parameters; "boy" / "boyfriend" / "girl" / "girlfriend" share their root sub-pieces.
- **Fixed-size vocabulary** with variable-length tokens — combines the open coverage of character models with the parameter efficiency of word models.

[[FastText]] ([[PiotrBojanowski|Bojanowski]] et al. 2017) is the canonical subword-embedding model: each word's vector is $\mathbf{v}_w=\sum_{g\in\mathcal{G}_w}\mathbf{z}_g$ over all its 3- to 6-character $n$-grams plus the whole-word symbol. [[BPE]] and [[WordPiece]] (used by [[BERT]]) instead learn a **fixed subword vocabulary** by greedy merging, and downstream models look up one embedding per subword piece. Subword embeddings underpin essentially every modern LLM input layer.

See [[d2l-nlp-pretraining]] §subword-embedding.

## From [[hands-on-llm-ch02-tokens-and-embeddings|*Hands-On LLMs* Ch 2]]

Ch 2 names **subword tokenization** as the modern default — *"the most commonly used tokenization scheme."* Pedagogical framing:

> "This method contains full and partial words. In addition to the vocabulary expressivity ... another benefit of the approach is its ability to represent new words by breaking down the new token into smaller characters, which tend to be a part of the vocabulary." — Ch 2

Motivating example: instead of separate vocabulary slots for `apology`, `apologize`, `apologetic`, `apologist`, a subword tokenizer keeps a shared root `apolog` plus suffixes `-y`, `-ize`, `-etic`, `-ist`. Result: a more expressive vocabulary at a smaller size.

**Context-length tradeoff** Ch 2 quantifies:

> "Subword tokens often average three characters per token. ... With a model with a context length of 1,024, you may be able to fit about three times as much text using subword tokenization than using character tokens." — Ch 2

The chapter surveys three subword-tokenization **algorithms** ([[BPE]], [[WordPiece]], [[SentencePiece]]) and tabulates how seven actual tokenizers ([[bert|BERT]], [[GPT2]], [[FLANT5]], [[GPT4]], [[StarCoder2]], [[Galactica]], [[Phi3Mini|Phi-3]]) tokenize the same contrived test string differently.
