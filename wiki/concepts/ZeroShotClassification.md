---
title: "Zero-Shot Classification"
type: concept
tags: [llm, classification, zero-shot, embeddings, nli]
sources: [hands-on-llm-ch04-text-classification, hands-on-llm-ch09-multimodal-llms]
last_updated: 2026-05-23
---

# Zero-Shot Classification

The specialization of [[ZeroShotLearning|zero-shot learning]] to **classification tasks** — assigning input text to one of a fixed set of candidate labels **without any labeled training data**. The model has access only to the **label names / descriptions** themselves, not labeled examples.

## Three implementations (in the wiki)

1. **[[NaturalLanguageInference|NLI]]-based zero-shot.** Cast `(input_text, "This text is about <label>")` as an NLI (premise, hypothesis) pair; assign the label with the highest entailment probability. Dominant approach before sentence-transformer embeddings became commodity.
2. **Embedding-based zero-shot via [[LabelEmbedding|label embeddings]] + [[CosineSimilarity|cosine similarity]]** — the recipe [[hands-on-llm-ch04-text-classification|*Hands-On LLMs* Ch 4]] illustrates. Embed both documents and label descriptions in the same vector space; assign the label whose embedding is closest in cosine distance.
3. **Prompt-based zero-shot with a generative LM** — instruct an instruction-tuned generative model to output the label directly (e.g. *"Classify this review as positive or negative: ..."*). Closest to [[ZeroShotLearning|zero-shot learning]] in the prompt-engineering sense; covered as [[GenerativeClassification|generative classification]] in Ch 4.

## From [[hands-on-llm-ch04-text-classification|*Hands-On LLMs* Ch 4]]

Ch 4 demonstrates the **embedding-based** approach as a **versatile and underestimated** alternative to NLI-based zero-shot:

> "To perform zero-shot classification with embeddings, there is a neat trick that we can use. We can describe our labels based on what they should represent. For example, a negative label for movie reviews can be described as 'This is a negative movie review.' By describing and embedding the labels and documents, we have data that we can work with." — Ch 4

The recipe:

```python
# Embed both documents and label descriptions in the same space
label_embeddings = model.encode(["A negative review", "A positive review"])

# Assign label by max cosine similarity
from sklearn.metrics.pairwise import cosine_similarity
sim_matrix = cosine_similarity(test_embeddings, label_embeddings)
y_pred = np.argmax(sim_matrix, axis=1)
```

**Result on [[RottenTomatoes|Rotten Tomatoes]] with `all-mpnet-base-v2`**: F1 = 0.78 weighted average — *"impressive considering we did not use any labeled data at all!"* Only 7 F1 points below the supervised logistic-regression baseline.

## Why embeddings work as zero-shot classifiers

A pretrained sentence-embedding model places **semantically similar text near each other** in the embedding space, regardless of whether the texts are documents or label descriptions. So *"This movie was incredible"* and *"A positive review"* will be closer than *"This movie was incredible"* and *"A negative review"* — even though no document-label training pairs were seen.

## Label description is a hyperparameter

Per Ch 4: tune the label description as you would tune a prompt. *"We decided upon 'A negative/positive review' as the name of our labels but that can be improved. Instead, we can make them a bit more concrete and specific toward our data by using 'A very negative/positive movie review' instead. This way, the embedding will capture that it is a movie review and will focus a bit more on the extremes of the two labels."*

## Why Ch 4 chose embeddings over NLI

> "If you are familiar with zero-shot classification with Transformer-based models, you might wonder why we choose to illustrate this with embeddings instead. Although natural language inference models are amazing for zero-shot classification, the example here demonstrates the flexibility of embeddings for a variety of tasks. As you will see throughout the book, embeddings can be found in most Language AI use cases and are often an underestimated but incredibly vital component." — Ch 4

The choice is pedagogical, not performance-based. NLI-based zero-shot remains a strong alternative — and is the basis of Hugging Face's `pipeline("zero-shot-classification")` default (which uses an NLI model under the hood).

## Connections

- [[ZeroShotLearning]] — parent concept.
- [[LabelEmbedding]] — the embedded-label-description primitive.
- [[CosineSimilarity]] — the label-assignment metric.
- [[NaturalLanguageInference]] — the prior dominant zero-shot approach.
- [[EmbeddingModel]] / [[SentenceTransformers]] / [[AllMPNetBaseV2]] — the embedding backbone.
- [[GenerativeClassification]] — the prompt-based generative alternative.
- [[FewShotLearning]] — the next regime up (a few labeled examples).
- [[hands-on-llm-ch04-text-classification]] — primary source.

## From [[hands-on-llm-ch09-multimodal-llms|*Hands-On LLMs* Ch 9]]

Ch 9 extends zero-shot classification from **text-only label-embedding** (Ch 4) to **image classification via multimodal label-embedding**. Among [[CLIP]]'s four named applications, zero-shot classification is the first:

> *"Multimodal embedding models, like CLIP, can be used to do **zero-shot classification**: we can compare the embedding of an image to that of the description of its possible classes."* — Ch 9

Mechanism: embed the candidate image once via `CLIPModel.get_image_features(...)`; embed each class description (e.g., `"a photo of a dog"`, `"a photo of a cat"`) once via `CLIPModel.get_text_features(...)`; pick the class whose text embedding has the highest cosine similarity to the image embedding. **No labeled image-class training data required** — the only inputs are the class descriptions themselves.

This is the wiki's **second worked instance** of the *embed-the-labels-and-compare-by-cosine* primitive — Ch 4 ran it on text inputs ([[RottenTomatoes]] sentiment via `all-mpnet-base-v2`); Ch 9 runs the same primitive on **image** inputs (via CLIP). The structural symmetry is the punchline: **once a model produces embeddings in a [[MultimodalEmbeddingSpace|shared vector space]], zero-shot classification is modality-agnostic** — the label-assignment loop is the same code regardless of whether the input is text, image, or any other modality whose embedding shares the space.
