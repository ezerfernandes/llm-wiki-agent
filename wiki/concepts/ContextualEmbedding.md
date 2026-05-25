---
title: "Contextual Embedding"
type: concept
tags: [nlp, embeddings, transformers]
sources: [d2l-nlp-pretraining, 1810.04805-bert, hands-on-llm-ch02-tokens-and-embeddings]
last_updated: 2026-05-23
---

# Contextual Embedding

A token representation whose value depends on surrounding context — formally $f(x, c(x))$ for token $x$ in context $c(x)$ — produced by [[BERT]], [[ELMo]], [[GPT]], and any [[transformer]] encoder/decoder; in contrast to **[[StaticEmbedding|static / context-independent]]** [[WordEmbedding|word embeddings]] like [[Word2Vec|word2vec]] / [[GloVe]] / [[FastText]] which assign the same vector to "bank" in both *"deposit cash at the bank"* and *"sit down on the bank"*.

Per [[d2l-nlp-pretraining]] §bert, the 2018 pretraining-architecture lineage is: [[TagLM]] (Peters et al. 2017) → CoVe (McCann et al. 2017) → [[ELMo]] (Peters et al. 2018, bidirectional LSTM, frozen pretrained features added to task-specific architecture) → [[GPT]] (Radford et al. 2018, Transformer decoder, task-agnostic but unidirectional) → [[BERT]] (Devlin et al. 2018, Transformer encoder, bidirectional and task-agnostic — "the best of both worlds"). Contextual embeddings enable homonyms ("bank" / "crane") to receive different vectors per usage; central to modern NLP transfer learning and the input layer of every decoder LLM (GPT-3/4/5, Claude, Gemini, Llama).

## From [[hands-on-llm-ch02-tokens-and-embeddings|*Hands-On LLMs* Ch 2]]

Ch 2 frames contextualized embeddings as **what the language model produces from static input embeddings** — *"A language model operates on raw, static embeddings as its input and produces contextual text embeddings."* (Figure 2-9.)

**Worked example using [[deberta|DeBERTa v3]]**:

```python
from transformers import AutoModel, AutoTokenizer
tokenizer = AutoTokenizer.from_pretrained("microsoft/deberta-base")
model = AutoModel.from_pretrained("microsoft/deberta-v3-xsmall")
tokens = tokenizer('Hello world', return_tensors='pt')
output = model(**tokens)[0]
output.shape  # torch.Size([1, 4, 384])
```

The 4 tokens are `[CLS] Hello world [SEP]`; each is mapped to a **384-dim contextualized vector** (the dimension of DeBERTa v3 xsmall's hidden state). *"This is the raw output of a language model. The applications of large language models build on top of outputs like this."*

**Downstream uses** Ch 2 enumerates: **named-entity recognition**, **extractive text summarization**, **text classification** — and notably, *"these contextualized vectors, for example, are what powers AI image generation systems like [[DALLE|DALL·E]], [[Midjourney]], and [[StableDiffusion|Stable Diffusion]]."* Contextualized text embeddings are the *conditioning input* to the diffusion / autoregressive image models.
