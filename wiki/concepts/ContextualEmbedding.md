---
title: "Contextual Embedding"
type: concept
tags: [nlp, embeddings, transformers]
sources: [d2l-nlp-pretraining, 1810.04805-bert]
last_updated: 2026-05-16
---

# Contextual Embedding

A token representation whose value depends on surrounding context — formally $f(x, c(x))$ for token $x$ in context $c(x)$ — produced by [[BERT]], [[ELMo]], [[GPT]], and any [[transformer]] encoder/decoder; in contrast to **static / context-independent** [[WordEmbedding|word embeddings]] like [[Word2Vec|word2vec]] / [[GloVe]] / [[FastText]] which assign the same vector to "bank" in both *"deposit cash at the bank"* and *"sit down on the bank"*.

Per [[d2l-nlp-pretraining]] §bert, the 2018 pretraining-architecture lineage is: [[TagLM]] (Peters et al. 2017) → CoVe (McCann et al. 2017) → [[ELMo]] (Peters et al. 2018, bidirectional LSTM, frozen pretrained features added to task-specific architecture) → [[GPT]] (Radford et al. 2018, Transformer decoder, task-agnostic but unidirectional) → [[BERT]] (Devlin et al. 2018, Transformer encoder, bidirectional and task-agnostic — "the best of both worlds"). Contextual embeddings enable homonyms ("bank" / "crane") to receive different vectors per usage; central to modern NLP transfer learning and the input layer of every decoder LLM (GPT-3/4/5, Claude, Gemini, Llama).
