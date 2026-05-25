---
title: "KeyBERTInspired"
type: concept
tags: [bertopic, representation-model, keyword-extraction, embeddings]
sources: [hands-on-llm-ch05-text-clustering-topic-modeling]
last_updated: 2026-05-23
---

# KeyBERTInspired

**KeyBERTInspired** is a [[BERTopic]] representation model — a **keyword reranker** that uses embeddings to improve the initial [[ClassBasedTFIDF|c-TF-IDF]] topic keywords. It is named after and methodologically inspired by [[KeyBERT]] (Grootendorst 2020), Grootendorst's standalone keyword-extraction package.

## Algorithm (per *Hands-On LLMs* Ch 5)

1. For each topic, compute the **average document embedding** across the topic's most representative documents (selected via cosine similarity between document c-TF-IDF and topic c-TF-IDF).
2. Embed the candidate keywords (from c-TF-IDF).
3. **Rerank** keywords by **cosine similarity** to the topic embedding.
4. Return the top-K reranked keywords.

*"BERTopic uses a similar approach [to KeyBERT]. KeyBERTInspired uses c-TF-IDF to extract the most representative documents per topic by calculating the similarity between a document's c-TF-IDF values and those of the topic they correspond to. ... The average document embedding per topic is calculated and compared to the embeddings of candidate keywords to rerank the keywords."*

## Strength: removes stopwords automatically

Stopwords have weak embedding-similarity signal to a topic's semantic centroid. KeyBERTInspired removes them naturally — *"KeyBERTInspired especially tends to remove nearly all stop words since it focuses on the semantic relationships between words and documents."*

## Weakness: drops domain abbreviations

Domain-specific abbreviations (e.g., *"nmt"* for neural machine translation, *"asr"* for automatic speech recognition) often have **poor general-purpose embeddings** — embedding models trained on web text don't know them well. Ch 5 explicitly flags this:

> *"Words in the original model, like nmt (topic 3), which stands for neural machine translation, are removed as the model could not properly represent the entity. For domain experts, these abbreviations are highly informative."*

So KeyBERTInspired trades stopword cleanup for abbreviation loss. Run **side-by-side** with the original c-TF-IDF representation to keep both signals.

## Usage in BERTopic

```python
from bertopic.representation import KeyBERTInspired

# Update topic representations without re-clustering
representation_model = KeyBERTInspired()
topic_model.update_topics(abstracts, representation_model=representation_model)
```

Because BERTopic's clustering and representation stages are decoupled, KeyBERTInspired can be applied **after** training without redoing the UMAP / HDBSCAN steps — a major modularity advantage.

## Example outputs (per Ch 5)

| Topic | c-TF-IDF (original) | KeyBERTInspired |
|---|---|---|
| 0 (ASR) | speech \| asr \| recognition \| end \| acoustic | speech \| encoder \| phonetic \| language \| transcription |
| 1 (medical) | medical \| clinical \| biomedical \| patient \| health | nlp \| ehr \| clinical \| biomedical \| language |
| 3 (NMT) | translation \| nmt \| machine \| neural \| bleu | translation \| translating \| translate \| transliteration \| ... |

Note how *"nmt"* and *"bleu"* — both informative for domain experts — are removed in the KeyBERTInspired column.

## Connections

- [[hands-on-llm-ch05-text-clustering-topic-modeling]] — primary source.
- [[BERTopic]] — the parent framework.
- [[KeyBERT]] — the keyword-extraction package this method is inspired by.
- [[ClassBasedTFIDF]] — the upstream representation KeyBERTInspired refines.
- [[MaximalMarginalRelevance]] / [[GenerativeTopicLabeling]] — sibling BERTopic representation models.
- [[CosineSimilarity]] — the underlying similarity metric.
- [[SentenceTransformers]] / [[Embedding]] — the embedding backbone.
- [[MaartenGrootendorst]] — author.
