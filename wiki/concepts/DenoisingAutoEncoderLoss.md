---
title: "Denoising Auto-Encoder Loss"
type: concept
tags: [loss-function, unsupervised, embeddings, tsdae, sentence-transformers]
sources: [hands-on-llm-ch10-creating-text-embedding-models]
last_updated: 2026-05-23
---

# Denoising Auto-Encoder Loss

**Denoising auto-encoder loss** — the loss function for [[TSDAE]] (Transformer-based Sequential Denoising Auto-Encoder). The encoder consumes a **damaged sentence** (a sentence with a percentage of words deleted), produces a sentence embedding via [[CLSPooling|[CLS]-pooling]], and the decoder must reconstruct the **original** (undamaged) sentence from that embedding.

Per [[hands-on-llm-ch10-creating-text-embedding-models|*Hands-On LLMs* Ch 10]]: *"We will need a loss function that attempts to reconstruct the original sentence using the noise sentence, namely DenoisingAutoEncoderLoss. By doing so, it will learn how to accurately represent the data. It is similar to masking but without knowing where the actual masks are."*

## Mechanism

For each `(damaged_sentence, original_sentence)` pair:

1. Encoder encodes the `damaged_sentence` with [[CLSPooling|[CLS]-pooling]] → sentence embedding.
2. Decoder generates a sequence token-by-token, conditioned on the encoder's embedding.
3. Loss = cross-entropy of the decoder's output against the `original_sentence`.

The intuition: if the encoder can produce an embedding from which the decoder can reconstruct the full undamaged sentence, then that embedding **must contain sufficient semantic information** about the original — making it a useful sentence representation.

Per Ch 10: *"the more accurate the sentence embedding is, the more accurate the reconstructed sentence will be."*

## Encoder/decoder weight tying

Per Ch 10's recipe: *"we tie the parameters of both models. Instead of having separate weights for the encoder's embedding layer and the decoder's output layer, they share the same weights. This means that any updates to the weights in one layer will be reflected in the other layer as well."*

In code:

```python
train_loss = losses.DenoisingAutoEncoderLoss(
    embedding_model, tie_encoder_decoder=True
)
train_loss.decoder = train_loss.decoder.to("cuda")
```

## Memory cost

Per Ch 10: *"training our model works the same as we have seen several times before but we lower the batch size as memory increases with this loss function."* — Ch 10 drops `per_device_train_batch_size` from 32 to **16** for the TSDAE run.

## Discarding the decoder at inference

Per Ch 10: *"after training, we can use the encoder to generate embeddings from text since the decoder is only used for judging whether the embeddings can accurately reconstruct the original sentence."* — the decoder is a **training-only structural device**.

## Pooling — [CLS] not mean

The Ch 10 / TSDAE-paper recommendation: **use [[CLSPooling|[CLS]-pooling]], not [[MeanPooling|mean-pooling]]**. *"In the TSDAE paper, this was shown to be more effective since mean pooling loses the position information, which is not the case when using the [CLS] token."* This is the **only place in the wiki** where [CLS]-pooling is preferred over mean-pooling for a sentence-embedding regime.

## Worked result in Ch 10

Trained on 50,000 unlabeled MNLI sentences (premise + hypothesis flattened and deduplicated), starting from `bert-base-uncased` with [[CLSPooling|[CLS]]-pooling]:

- Loss: `sentence_transformers.losses.DenoisingAutoEncoderLoss(model, tie_encoder_decoder=True)`
- Result: STS-B Pearson cosine = **0.70** — *"quite impressive considering we did all this training with unlabeled data."*

## Connections

- [[TSDAE]] — the unsupervised technique this loss implements.
- [[MaskedLanguageModel]] — the predecessor; TSDAE is its sentence-level analog.
- [[CLSPooling]] — the recommended pooling for this loss.
- [[ContrastiveLearning]] — TSDAE is **not** contrastive in the InfoNCE sense, but it is a **representation-learning objective** that produces similar-quality embeddings.
- [[SentenceTransformers]] — implements `losses.DenoisingAutoEncoderLoss`.
- [[DomainAdaptation]] / [[AdaptivePretraining]] — TSDAE's primary production use case.
- [[KexinWang]] / [[NilsReimers]] / [[IrynaGurevych]] — TSDAE authors.
- [[hands-on-llm-ch10-creating-text-embedding-models]] — primary source.
