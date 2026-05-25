---
title: "TSDAE (Transformer-based Sequential Denoising Auto-Encoder)"
type: concept
tags: [unsupervised, embeddings, sentence-transformers, domain-adaptation, denoising-auto-encoder]
sources: [hands-on-llm-ch10-creating-text-embedding-models]
last_updated: 2026-05-23
---

# TSDAE (Transformer-based Sequential Denoising Auto-Encoder)

**TSDAE** — an **unsupervised** technique for training [[SentenceTransformers|sentence-transformers]]-style embedding models without any labels. Introduced by Wang, Reimers & Gurevych 2021 (arXiv:2104.06979 — *"TSDAE: Using Transformer-based Sequential Denoising Auto-Encoder for Unsupervised Sentence Embedding Learning"*).

Per [[hands-on-llm-ch10-creating-text-embedding-models|*Hands-On LLMs* Ch 10]]: *"TSDAE is a very elegant approach to creating an embedding model with unsupervised learning. The method assumes that we have no labeled data at all and does not require us to artificially create labels."*

## The core mechanism

Per Ch 10: *"The underlying idea of TSDAE is that we add noise to the input sentence by removing a certain percentage of words from it. This 'damaged' sentence is put through an encoder, with a pooling layer on top of it, to map it to a sentence embedding. From this sentence embedding, a decoder tries to reconstruct the original sentence from the 'damaged' sentence but without the artificial noise. The main concept here is that the more accurate the sentence embedding is, the more accurate the reconstructed sentence will be."*

The procedure for each training sentence:

1. Sample a random fraction of the sentence's words and **delete them** → `damaged_sentence`.
2. Encoder produces a sentence embedding from `damaged_sentence` using [[CLSPooling|[CLS]-pooling]] (NOT [[MeanPooling|mean-pooling]]).
3. Decoder generates a token sequence conditioned on that embedding.
4. Loss = cross-entropy of the decoder's output against the **original** (undamaged) sentence.

After training, **only the encoder is used at inference** — *"the decoder is only used for judging whether the embeddings can accurately reconstruct the original sentence."* The decoder is a structural training-only device.

## Why [CLS]-pooling, not mean-pooling

This is the **only place in the wiki where [[CLSPooling|[CLS]-pooling]] is recommended over [[MeanPooling|mean-pooling]]** for a sentence-embedding regime. Per Ch 10: *"in the TSDAE paper, this was shown to be more effective since mean pooling loses the position information, which is not the case when using the [CLS] token."* The reconstruction objective requires getting positions right — mean-pooling averages over positions and discards order; [CLS]-pooling retains a position-aware summary via self-attention.

## Encoder/decoder weight tying

Per Ch 10: *"We tie the parameters of both models. Instead of having separate weights for the encoder's embedding layer and the decoder's output layer, they share the same weights."* — `tie_encoder_decoder=True` in `losses.DenoisingAutoEncoderLoss`.

## Relationship to MLM

Per Ch 10: *"This method is very similar to masked language modeling, where we try to reconstruct and learn certain masked words. Here, instead of reconstructing masked words, we try to reconstruct the entire sentence."* TSDAE is the **sentence-level analog of [[MaskedLanguageModel|MLM]]** — same denoising idea, applied at the sentence level rather than the token level.

## Worked result in Ch 10

Trained on 50,000 unlabeled MNLI sentences (premise + hypothesis flattened and deduplicated), starting from `bert-base-uncased` with [[CLSPooling|[CLS]-pooling]]:

- Setup: `models.Transformer("bert-base-uncased")` + `models.Pooling(dim, "cls")`
- Loss: `losses.DenoisingAutoEncoderLoss(model, tie_encoder_decoder=True)`
- Noise: `DenoisingAutoEncoderDataset` from `sentence_transformers.datasets` (uses NLTK `punkt` tokenizer for word boundaries)
- Batch size: **16** (vs the chapter's usual 32; TSDAE uses more memory)
- Result: STS-B Pearson cosine = **0.70** — *"quite impressive considering we did all this training with unlabeled data."*

## Primary production use: domain adaptation

Per Ch 10: *"This is where domain adaptation comes in. ... You start by pretraining your domain-specific corpus using an unsupervised technique, such as the previously discussed TSDAE or masked language modeling. Then ... you fine-tune that model using a training dataset that can be either outside or in your target domain."*

The pipeline:

1. **Adaptive pretraining**: TSDAE on the target-domain corpus (unlabeled, abundant).
2. **Fine-tuning**: standard supervised contrastive training (MNR loss) on whatever labeled pairs are available (in-domain preferred, out-of-domain works because TSDAE has already adapted the encoder to the target domain).

See [[DomainAdaptation]] / [[AdaptivePretraining]] for the broader framing.

## Position in the unsupervised landscape

Per Ch 10, four named unsupervised techniques for sentence embeddings:

- **[[SimCSE]]** (Gao, Yao & Chen 2021, arXiv:2104.08821) — contrastive learning over dropout-as-augmentation.
- **[[ContrastiveTension|Contrastive Tension (CT)]]** (Carlsson et al. ICLR 2021) — train two copies of a model and a contrastive loss between them.
- **TSDAE** (Wang, Reimers & Gurevych 2021, arXiv:2104.06979) — denoising auto-encoder. Ch 10 focuses on this one.
- **[[GPL|Generative Pseudo-Labeling (GPL)]]** (Wang et al. 2021, arXiv:2112.07577) — generate pseudo queries for a domain corpus, then train via contrastive learning.

Ch 10 picks TSDAE because *"it has shown great performance on unsupervised tasks as well as domain adaptation."*

## Connections

- [[DenoisingAutoEncoderLoss]] — the loss function TSDAE uses.
- [[CLSPooling]] — the regime-specific pooling choice.
- [[MaskedLanguageModel]] — the token-level analog; TSDAE is the sentence-level version.
- [[DomainAdaptation]] / [[AdaptivePretraining]] — TSDAE's primary production use case.
- [[SimCSE]] / [[ContrastiveTension]] / [[GPL]] — the alternative unsupervised techniques named in Ch 10.
- [[ContrastiveLearning]] — the broader paradigm (though TSDAE is not contrastive in the InfoNCE sense).
- [[SentenceTransformers]] — implements TSDAE via `DenoisingAutoEncoderDataset` + `DenoisingAutoEncoderLoss`.
- [[KexinWang]] / [[NilsReimers]] / [[IrynaGurevych]] — TSDAE authors.
- [[hands-on-llm-ch10-creating-text-embedding-models]] — primary source.
