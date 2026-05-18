---
title: "Subword Embedding"
type: concept
tags: [nlp, embeddings, tokenization, morphology]
sources: [d2l-nlp-pretraining]
last_updated: 2026-05-16
---

# Subword Embedding

Word-representation approach that decomposes each word into smaller pieces — **character-$n$-grams**, [[BPE|BPE]] merges, [[WordPiece]] pieces, or SentencePiece units — and represents the word as a (sum / lookup of the) embeddings of those pieces. Motivations:

- **Out-of-vocabulary (OOV)** robustness — never seen "tokenization" but seen "token" + "##ization"? Still get a representation.
- **Morphological sharing** — "helps", "helped", "helping" share their stem subword and so share parameters; "boy" / "boyfriend" / "girl" / "girlfriend" share their root sub-pieces.
- **Fixed-size vocabulary** with variable-length tokens — combines the open coverage of character models with the parameter efficiency of word models.

[[FastText]] ([[PiotrBojanowski|Bojanowski]] et al. 2017) is the canonical subword-embedding model: each word's vector is $\mathbf{v}_w=\sum_{g\in\mathcal{G}_w}\mathbf{z}_g$ over all its 3- to 6-character $n$-grams plus the whole-word symbol. [[BPE]] and [[WordPiece]] (used by [[BERT]]) instead learn a **fixed subword vocabulary** by greedy merging, and downstream models look up one embedding per subword piece. Subword embeddings underpin essentially every modern LLM input layer.

See [[d2l-nlp-pretraining]] §subword-embedding.
