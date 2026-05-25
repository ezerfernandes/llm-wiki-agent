---
title: "Augmented SBERT"
type: concept
tags: [data-augmentation, embeddings, sbert, fine-tuning, cross-encoder, bi-encoder]
sources: [hands-on-llm-ch10-creating-text-embedding-models]
last_updated: 2026-05-23
---

# Augmented SBERT

**Augmented SBERT** — a data-augmentation procedure for fine-tuning [[SBERT|Sentence-BERT]] embedding models when **only a small amount of labeled data is available**. Introduced by Thakur, Reimers, Daxenberger & Gurevych 2020 (arXiv:2010.08240 — *"Augmented SBERT: Data Augmentation Method for Improving Bi-Encoders for Pairwise Sentence Scoring Tasks"*).

Per [[hands-on-llm-ch10-creating-text-embedding-models|*Hands-On LLMs* Ch 10]]: *"A disadvantage of training or fine-tuning these embedding models is that they often require substantial training data. Many of these models are trained with more than a billion sentence pairs. ... Fortunately, there is a way to augment your data such that an embedding model can be fine-tuned when there is only a little labeled data available. This procedure is referred to as Augmented SBERT."*

## The four-step recipe

Per Ch 10:

1. **Fine-tune a [[CrossEncoder|cross-encoder]] (BERT)** on a small, annotated **[[GoldDataset|gold dataset]]**.
2. **Create new sentence pairs** (either by random cross-product of the gold dataset or by mining semi-hard candidates with a pretrained embedding model).
3. **Label the new sentence pairs with the fine-tuned cross-encoder** → **[[SilverDataset|silver dataset]]**.
4. **Train a [[BiEncoder|bi-encoder]] (SBERT)** on the **gold + silver** union.

## Why it works

The structural trick: **the cross-encoder is slow but accurate; the bi-encoder is fast but lower-quality**. Augmented SBERT uses the cross-encoder's accuracy at training time (one-time, offline) to label data that then trains a fast bi-encoder for inference time. You get the cross-encoder's labeling quality with the bi-encoder's inference cost.

## Gold vs silver

Per Ch 10: *"A gold dataset is a small but fully annotated dataset that holds the ground truth. A silver dataset is also fully annotated but is not necessarily the ground truth as it was generated through predictions of the cross-encoder."*

The "gold/silver" naming is the chapter's wiki-first contribution as a **data-quality taxonomy** — it generalizes beyond Augmented SBERT to any pipeline that combines small high-quality data with larger model-labeled data.

## Generating unlabeled pairs

Ch 10 offers **two strategies** for producing the candidate pairs the cross-encoder will label:

1. **Random cross-product** — take the premise of row A with the hypothesis of row B. *"This allows you to easily generate 10 times as many sentence pairs that can be labeled with the cross-encoder. This strategy, however, likely generates significantly more dissimilar than similar pairs."*
2. **Pretrained-embedding-model semantic-search reranking** — embed all candidate pairs with a pretrained sentence-transformer; retrieve top-$k$ similar for each input. *"This rough reranking process allows us to focus on sentence pairs that are likely to be more similar. Although the sentences are still chosen based on an approximation since the pretrained embedding model was not trained on our data, it is much better than random sampling."*

## Worked result in Ch 10

- Gold dataset: 10,000 MNLI pairs (entailment → label 1, neutral/contradiction → label 0).
- Train cross-encoder: `CrossEncoder("bert-base-uncased", num_labels=2)` for 1 epoch on the 10k gold examples.
- Silver dataset: 40,000 additional MNLI pairs labeled by the trained cross-encoder via `cross_encoder.predict(pairs, apply_softmax=True)` → `np.argmax(output, axis=1)`.
- Train bi-encoder: `bert-base-uncased` with `CosineSimilarityLoss` on **gold + silver** (50k total after dedup).
- Result: STS-B Pearson cosine = **0.71**.

Compared to the chapter's cosine-similarity-loss baseline (full 50k labeled MNLI → 0.72), Augmented SBERT reaches **0.71 with only 10k labeled examples (20% of the data)** by augmenting with 40k cross-encoder-labeled silver pairs. *"Using only 20% of that data, we managed to get a score of 0.71!"*

## Diagnostic: silver-quality measurement

Per Ch 10: *"You can test the quality of your silver data by also training your embedding model only on the gold dataset. The difference in performance indicates how much your silver dataset potentially adds to the quality of the model."*

This is a practical diagnostic for whether the cross-encoder is producing useful silver labels — if gold-only training matches gold+silver training, the silver pairs aren't adding signal.

## Connections

- [[GoldDataset]] / [[SilverDataset]] — the data-quality taxonomy this technique introduces.
- [[CrossEncoder]] — the labeling model.
- [[BiEncoder]] / [[SBERT]] — the trained model.
- [[CosineSimilarityLoss]] — the loss function for the bi-encoder.
- [[ContrastiveLearning]] — the broader paradigm.
- [[HardNegatives]] — Augmented SBERT can produce hard-negative-like silver labels.
- [[NandanThakur]] / [[NilsReimers]] / [[IrynaGurevych]] — Augmented SBERT authors.
- [[DataAugmentation]] — the broader concept family.
- [[knowledgedistillation]] — related idea: a stronger model labels data for a weaker (faster) model.
- [[hands-on-llm-ch10-creating-text-embedding-models]] — primary source.
