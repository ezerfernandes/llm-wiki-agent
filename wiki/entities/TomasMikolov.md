---
title: "Tomáš Mikolov"
type: entity
tags: [person, researcher, nlp, word-embeddings]
sources: [d2l-nlp-pretraining, hands-on-llm-ch01-introduction-to-llms]
last_updated: 2026-05-23
---

# Tomáš Mikolov

NLP / representation-learning researcher; first author of the two 2013 [[Word2Vec|word2vec]] papers ([[SkipGram|skip-gram]] *Mikolov, Sutskever, Chen et al. 2013* and [[CBOW|continuous bag-of-words]] *Mikolov, Chen, Corrado et al. 2013*) that introduced shallow, scalable, self-supervised learning of dense word vectors and the [[AnalogyTask|king − man + woman ≈ queen]]-style analogy structure those vectors exhibit. The single most-cited author in [[d2l-nlp-pretraining|D2L's NLP Pretraining chapter]]; word2vec is its opening model and the conceptual ancestor of every later embedding (including [[GloVe]], [[FastText]], and the input layer of [[BERT]]).

## Connections
- [[Word2Vec]], [[SkipGram]], [[CBOW]] — the model family he introduced.
- [[NegativeSampling]] — the approximate-training trick from the same 2013 papers.
- [[GloVe]], [[FastText]] — successor static-embedding models.
- [[d2l-nlp-pretraining]] — D2L chapter that operationalizes word2vec end-to-end on [[PTB]].
- [[google|Google]] (at the time of the word2vec papers), later [[fair|Facebook AI Research]] and [[CzechTechnicalUniversity]].
