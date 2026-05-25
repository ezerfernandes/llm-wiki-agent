---
title: "Generative Topic Labeling"
type: concept
tags: [bertopic, llm, topic-modeling, prompt-engineering, representation-model]
sources: [hands-on-llm-ch05-text-clustering-topic-modeling]
last_updated: 2026-05-23
---

# Generative Topic Labeling

**Generative topic labeling** is the [[BERTopic]] representation-model pattern where a **generative LLM produces a short natural-language label** for each topic from its keywords and most-representative documents. It is the *Hands-On LLMs* Ch 5 demonstration of how **decoder-only / encoder-decoder LLMs slot into topic modeling without being applied to every document**.

## The efficiency claim

[[hands-on-llm-ch05-text-clustering-topic-modeling|Ch 5]]: *"We only need to use the generative model once for every topic, of which there could be potentially hundreds, instead of once for each document, of which there could potentially be millions."*

Because [[BERTopic]]'s representation stage runs **once per topic** (`O(n_topics)`) rather than once per document (`O(n_documents)`), even an expensive cloud LLM ([[ChatGPT|GPT-3.5]], [[ChatGPT|GPT-4]]) is affordable for labeling — a few hundred API calls instead of millions.

## The prompt template

Two placeholders are filled per topic:
- **`[DOCUMENTS]`** — a small set (typically 4) of the most-representative documents, selected by **cosine similarity of c-TF-IDF representations** between candidate documents and the topic centroid.
- **`[KEYWORDS]`** — the top keywords for the topic (from [[ClassBasedTFIDF|c-TF-IDF]] or any of the reranking representation models).

Example template (Flan-T5 in Ch 5):

```text
I have a topic that contains the following documents:
[DOCUMENTS]

The topic is described by the following keywords: '[KEYWORDS]'.

Based on the documents and keywords, what is this topic about?
```

Example template (GPT-3.5 in Ch 5; structured output):

```text
I have a topic that contains the following documents:
[DOCUMENTS]

The topic is described by the following keywords: [KEYWORDS]

Based on the information above, extract a short topic label in the following
format:
topic: <short topic label>
```

## Two BERTopic backends demonstrated

```python
# Local: Flan-T5
from transformers import pipeline
from bertopic.representation import TextGeneration
generator = pipeline("text2text-generation", model="google/flan-t5-small")
representation_model = TextGeneration(
    generator, prompt=prompt, doc_length=50, tokenizer="whitespace"
)
topic_model.update_topics(abstracts, representation_model=representation_model)

# API: OpenAI GPT-3.5
import openai
from bertopic.representation import OpenAI
client = openai.OpenAI(api_key="YOUR_KEY")
representation_model = OpenAI(
    client, model="gpt-3.5-turbo", exponential_backoff=True, chat=True, prompt=prompt
)
topic_model.update_topics(abstracts, representation_model=representation_model)
```

## Quality tradeoffs

| Backend | Quality | Cost | Privacy |
|---|---|---|---|
| **[[FLANT5|Flan-T5-small]]** (local) | Fair; prone to overgeneric labels (e.g., *"Science/Tech"* for medical NLP) | Free | Full local |
| **[[ChatGPT|GPT-3.5-turbo]]** (API) | Strong; descriptive (*"Advancements in Aspect-Based Sentiment Analysis"*) | ~3¢ per few hundred topics | Cloud |
| **[[ChatGPT|GPT-4]]** / Claude / Gemini | Best; rarely off-topic | Higher | Cloud |
| **Local Llama / Phi-3** | Strong if model is large enough | Hardware-dependent | Full local |

## Why keep the keywords too

*"Although it seems like we do not need the keywords anymore, they are still representative of the input documents. No model is perfect and it is generally advised to generate multiple topic representations. BERTopic allows for all topics to be represented by different representations. You could, for example, use [[KeyBERTInspired]], [[MaximalMarginalRelevance|MMR]], and GPT-3.5 side by side to get different perspectives on the same topic."*

## Connections

- [[hands-on-llm-ch05-text-clustering-topic-modeling]] — primary source.
- [[BERTopic]] — the parent framework.
- [[ClassBasedTFIDF]] — provides keywords + representative document selection.
- [[KeyBERTInspired]] / [[MaximalMarginalRelevance]] — sibling representation models.
- [[PromptEngineering]] — the broader pattern.
- [[FLANT5]] / [[ChatGPT]] / [[GPT35Turbo]] / [[openai]] — the backends Ch 5 demonstrates.
- [[ReRanking]] — the abstraction (cheap-then-expensive refinement).
- [[GenerativeClassification]] — sibling per-task generative pattern from [[hands-on-llm-ch04-text-classification|Ch 4]].
