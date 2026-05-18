---
title: "Word Embedding"
type: concept
tags: [nlp, embeddings, representation-learning]
sources: [d2l-nlp-pretraining]
last_updated: 2026-05-16
---

# Word Embedding

The technique of mapping each word in a vocabulary to a fixed-length dense real vector that encodes its meaning and relationships with other words. Replaces sparse one-hot encodings, which have identically-zero cosine similarity between any two distinct words and so cannot represent semantic structure.

Two broad families:
- **Static / context-independent** embeddings — every occurrence of a word maps to the *same* vector regardless of surrounding context. Examples: [[Word2Vec|word2vec]] ([[SkipGram]] / [[CBOW]]), [[GloVe]], [[FastText]]. Trained by some form of self-supervised co-occurrence objective on a large unlabeled corpus.
- **Contextual / context-sensitive** embeddings — the representation of a token depends on the full sentence. Examples: [[ELMo]], [[GPT]], [[BERT]]. Produced by a neural encoder (LSTM or [[Transformer]]) pretrained on a self-supervised objective; per [[ContextualEmbedding]].

Evaluated *intrinsically* by [[WordSimilarity|word-similarity]] and [[AnalogyTask|analogy]] tasks (cosine-similarity nearest neighbours; $\textrm{vec}(c)+\textrm{vec}(b)-\textrm{vec}(a)$ analogy completion) and *extrinsically* by downstream task accuracy after the embedding is used as the input layer of a tagger / classifier / parser.

Per [[d2l-nlp-pretraining]] §word2vec: word embedding has become "the basic knowledge of natural language processing." It is the conceptual ancestor of every modern NLP representation — including the token-embedding layer of [[BERT]] and every decoder LLM.
