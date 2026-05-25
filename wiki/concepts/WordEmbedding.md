---
title: "Word Embedding"
type: concept
tags: [nlp, embeddings, representation-learning]
sources: [d2l-nlp-pretraining, hands-on-llm-ch01-introduction-to-llms, hands-on-llm-ch02-tokens-and-embeddings]
last_updated: 2026-05-23
---

# Word Embedding

The technique of mapping each word in a vocabulary to a fixed-length dense real vector that encodes its meaning and relationships with other words. Replaces sparse one-hot encodings, which have identically-zero cosine similarity between any two distinct words and so cannot represent semantic structure.

Two broad families:
- **Static / context-independent** embeddings — every occurrence of a word maps to the *same* vector regardless of surrounding context. Examples: [[Word2Vec|word2vec]] ([[SkipGram]] / [[CBOW]]), [[GloVe]], [[FastText]]. Trained by some form of self-supervised co-occurrence objective on a large unlabeled corpus.
- **Contextual / context-sensitive** embeddings — the representation of a token depends on the full sentence. Examples: [[ELMo]], [[GPT]], [[BERT]]. Produced by a neural encoder (LSTM or [[Transformer]]) pretrained on a self-supervised objective; per [[ContextualEmbedding]].

Evaluated *intrinsically* by [[WordSimilarity|word-similarity]] and [[AnalogyTask|analogy]] tasks (cosine-similarity nearest neighbours; $\textrm{vec}(c)+\textrm{vec}(b)-\textrm{vec}(a)$ analogy completion) and *extrinsically* by downstream task accuracy after the embedding is used as the input layer of a tagger / classifier / parser.

Per [[d2l-nlp-pretraining]] §word2vec: word embedding has become "the basic knowledge of natural language processing." It is the conceptual ancestor of every modern NLP representation — including the token-embedding layer of [[BERT]] and every decoder LLM.

## From [[hands-on-llm-ch01-introduction-to-llms|*Hands-On LLMs* Ch 1]]

Ch 1's taxonomy of embedding granularities (Figure 1-10):

- **Word embeddings** — one vector per token; [[Word2Vec|word2vec]] is the canonical example.
- **Sentence embeddings** — one vector per sentence; produced by encoder LLMs.
- **Document embeddings** — one vector per document; [[BagOfWords|bag-of-words]] produces these, as do mean-pooled sentence embeddings.

> "Bag-of-words, for instance, creates embeddings at a document level since it represents the entire document. In contrast, word2vec generates embeddings for words only." — Ch 1

Ch 1's intuitive framing for what embeddings encode:

> "Embeddings attempt to capture meaning by representing the properties of words. For instance, the word 'baby' might score high on the properties 'newborn' and 'human' while the word 'apple' scores low on these properties. ... In practice, these properties are often quite obscure and seldom relate to a single entity or humanly identifiable concept. However, together, these properties make sense to a computer and serve as a good way to translate human language into computer language." — Ch 1

— with the explicit caveat that **embedding dimensions don't correspond to humanly identifiable concepts**, even though pedagogically it helps to imagine them that way.

## From [[hands-on-llm-ch02-tokens-and-embeddings|*Hands-On LLMs* Ch 2]]

Ch 2 places word embeddings in a **three-layer taxonomy** relative to modern LLMs:

1. **[[StaticEmbedding|Static word embeddings]]** ([[Word2Vec|word2vec]], [[GloVe]], [[FastText]]) — pre-LLM era; one vector per word, context-independent. *"Before LLMs, word embedding methods like word2vec, GloVe, and fastText were popular. In language processing, this has largely been replaced with contextualized word embeddings produced by language models."*
2. **[[TokenEmbedding|Token embeddings]]** — the LLM-input-layer special case; each row of the embedding matrix is the static embedding for one vocabulary token.
3. **[[ContextualEmbedding|Contextualized word embeddings]]** — produced by Transformer attention layers; *"represent a word with a different token based on its context."*

Ch 2 also names **embeddings-beyond-language** as a first-class application: *"Embeddings, or assigning meaningful vector representations to objects, turns out to be useful in many domains, including recommender engines and robotics."* The [[Word2VecRecommender|song-embedding recommender]] worked example demonstrates the same word2vec algorithm trained on **playlists-as-sentences, songs-as-words** — producing a useful recommendation system without any text NLP component.

**Pretrained word embeddings via [[Gensim]]** in Ch 2:
```python
import gensim.downloader as api
model = api.load("glove-wiki-gigaword-50")
model.most_similar([model['king']], topn=11)
# [('king', 1.0), ('prince', 0.82), ('queen', 0.78), ('emperor', 0.77), ...]
```
