---
title: "Adaptive Pretraining"
type: concept
tags: [pretraining, domain-adaptation, unsupervised, mlm, tsdae]
sources: [hands-on-llm-ch10-creating-text-embedding-models]
last_updated: 2026-05-23
---

# Adaptive Pretraining

**Adaptive pretraining** — the technique of running **unsupervised pretraining on a target-domain corpus** as a preparatory step before supervised fine-tuning. The standard mechanism for [[DomainAdaptation|domain adaptation]] of pretrained models.

Per [[hands-on-llm-ch10-creating-text-embedding-models|*Hands-On LLMs* Ch 10]]: *"One method for domain adaptation is called adaptive pretraining. You start by pretraining your domain-specific corpus using an unsupervised technique, such as the previously discussed [[TSDAE]] or [[MaskedLanguageModel|masked language modeling]]. Then ... you fine-tune that model using a training dataset that can be either outside or in your target domain."*

## The two-stage pattern

1. **Adaptive pretraining (unsupervised)**: Take a pretrained model (e.g., `bert-base-uncased`). Run unsupervised training on the **target-domain unlabeled corpus** using [[TSDAE]], [[MaskedLanguageModel|MLM]], or another unsupervised technique. This shifts the encoder's vocabulary coverage and syntactic priors toward the target domain.
2. **Supervised fine-tuning**: Run standard supervised contrastive training ([[MultipleNegativesRankingLoss|MNR loss]] / [[CosineSimilarityLoss|cosine loss]] / [[AugmentedSBERT]]) on whatever labeled pairs are available. After Stage 1, **out-of-domain labeled pairs work** because the encoder has already been adapted to the target vocabulary.

## Why this works

Pretrained models are vocabulary-biased toward their training distribution (Wikipedia / Common Crawl for most foundation models). When deployed on out-of-distribution domains (medical, legal, niche-scientific), the encoder's embeddings degrade because:

- **Vocabulary mismatch**: target-domain rare tokens are under-trained.
- **Distributional mismatch**: syntactic/discourse patterns differ.
- **Topical mismatch**: the implicit topic prior is wrong.

Adaptive pretraining addresses the first two problems via unsupervised training on the target corpus, which moves the model's parameters into the target-domain neighborhood.

## TSDAE vs MLM as Stage-1 choices

- **[[TSDAE]]** (Ch 10): denoising auto-encoder objective on sentences; trains the encoder to produce sentence-level representations that reconstruct deleted words.
- **[[MaskedLanguageModel|MLM]]** (Ch 11): token-level masked-token prediction; trains the encoder to predict 15% randomly-masked tokens from context.

Both produce domain-adapted encoders ready for Stage-2 fine-tuning. TSDAE is more useful for direct sentence-embedding applications (the encoder is already sentence-aware); MLM is more general-purpose.

## Connections

- [[DomainAdaptation]] — the broader problem this technique solves.
- [[TSDAE]] / [[MaskedLanguageModel]] — the Stage-1 unsupervised methods.
- [[FineTuning]] / [[TransferLearning]] — the broader family.
- [[pretraining]] — the broader concept.
- [[MultipleNegativesRankingLoss]] / [[CosineSimilarityLoss]] / [[AugmentedSBERT]] — Stage-2 supervised options.
- [[hands-on-llm-ch10-creating-text-embedding-models]] — primary source.
