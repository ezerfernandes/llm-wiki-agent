---
title: "Domain Adaptation"
type: concept
tags: [domain-adaptation, fine-tuning, embeddings, transfer-learning]
sources: [hands-on-llm-ch10-creating-text-embedding-models, hands-on-llm-ch11-fine-tuning-representation-models]
last_updated: 2026-05-23
---

# Domain Adaptation

**Domain adaptation** — *"updating existing embedding models to a specific textual domain that contains different subjects from the source domain."* The recipe for taking a general-purpose pretrained model (trained on Wikipedia, Common Crawl, etc.) and making it work on a specialized vocabulary (medical, legal, financial, scientific).

Per [[hands-on-llm-ch10-creating-text-embedding-models|*Hands-On LLMs* Ch 10]]: *"When you have very little or no labeled data available, you typically use unsupervised learning to create your text embedding model. However, unsupervised techniques are generally outperformed by supervised techniques and have difficulty learning domain-specific concepts. This is where domain adaptation comes in. Its goal is to update existing embedding models to a specific textual domain that contains different subjects from the source domain."*

## Source vs target (in-domain vs out-domain)

Per Ch 10: *"The target domain, or out-domain, generally contains words and subjects that were not found in the source domain or in-domain."*

The naming convention can be confusing — Ch 10 uses **"in-domain"** for the original pretraining domain (source) and **"out-domain"** for the target deployment domain. Different fields invert these terms; Ch 10's usage is consistent within the chapter.

## Adaptive pretraining — the canonical recipe

Per Ch 10: *"One method for domain adaptation is called [[AdaptivePretraining|adaptive pretraining]]. You start by pretraining your domain-specific corpus using an unsupervised technique, such as the previously discussed [[TSDAE]] or [[MaskedLanguageModel|masked language modeling]]. Then ... you fine-tune that model using a training dataset that can be either outside or in your target domain. Although data from the target domain is preferred, out-domain data also works since we started with unsupervised training on the target domain."*

The two-stage pipeline:

1. **Stage 1 — Adaptive pretraining (unsupervised)**: TSDAE or MLM on the target-domain corpus. No labels needed; just lots of target-domain text. The encoder learns the vocabulary and syntactic patterns of the target domain.
2. **Stage 2 — Supervised fine-tuning**: standard contrastive training (e.g., [[MultipleNegativesRankingLoss|MNR loss]]) on whatever labeled pairs are available — **in-domain preferred but out-of-domain works** because Stage 1 has already adapted the encoder.

## Why both stages are needed

- **Adaptive pretraining alone** produces good vocabulary coverage but limited downstream task signal — the encoder knows medical terms but doesn't know which sentences are semantically similar.
- **Supervised fine-tuning alone (on out-of-domain data)** produces good similarity signal but poor vocabulary coverage — the encoder knows that *"these two sentences mean the same thing"* but doesn't recognize medical jargon.
- **Combined**: both vocabulary coverage AND similarity signal.

## The Ch 10 close-out recipe

Per Ch 10's closing summary: *"Using everything you have learned in this chapter, you should be able to reproduce this pipeline! First, you can start with TSDAE to train an embedding model on your target domain and then fine-tune it using either general supervised training or Augmented SBERT."*

The combinatorics:

| Stage 1 (unsupervised) | Stage 2 (supervised) |
|---|---|
| TSDAE | Standard MNR-loss fine-tuning |
| TSDAE | [[AugmentedSBERT]] |
| [[MaskedLanguageModel\|MLM]] (Ch 11) | Standard MNR-loss fine-tuning |
| MLM | Augmented SBERT |

Ch 10 promises Ch 11 will walk the MLM half of this matrix.

## Connections

- [[AdaptivePretraining]] — the canonical method.
- [[TSDAE]] / [[MaskedLanguageModel]] — the unsupervised Stage-1 techniques.
- [[MultipleNegativesRankingLoss]] / [[AugmentedSBERT]] — Stage-2 supervised options.
- [[TransferLearning]] / [[FineTuning]] — the broader paradigm domain adaptation lives in.
- [[GPL]] — the alternative dense-retrieval domain-adaptation method.
- [[hands-on-llm-ch10-creating-text-embedding-models]] — primary source.

## From [[hands-on-llm-ch11-fine-tuning-representation-models|*Hands-On LLMs* Ch 11]]

Ch 11 delivers the **MLM half of the domain-adaptation matrix** Ch 10 promised. The Ch 11 framing emphasizes the **three-stage pipeline** for representation-model classification:

> *"It is like going from a general BERT model to a BioBERT model specialized for the medical domain, to a fine-tuned BioBERT model to classify medication."*

The recipe:

1. **Stage 0** — Generic pretraining (provided — base `bert-base-cased`).
2. **Stage 1** — [[ContinuedPretraining|Continued pretraining]] with [[MaskedLanguageModel|MLM]] on the **target domain corpus** via `AutoModelForMaskedLM` + [[DataCollatorForLanguageModeling]]. *"This will update the subword representations to be more tuned toward words it would not have seen before."*
3. **Stage 2** — Supervised fine-tuning for classification via `AutoModelForSequenceClassification.from_pretrained("mlm", num_labels=2)`.

Ch 11's worked example uses the same Rotten Tomatoes corpus for both Stage 1 (unlabeled, with labels stripped) and Stage 2 (labeled). The qualitative diagnostic on *"What a horrible [MASK]!"* — base BERT predicts `idea / dream / day`, MLM-continued predicts `movie / film / mess` — verifies Stage 1 actually moved the model toward the target domain.

This matches the Ch 10 / Ch 11 recipe-matrix:

| Stage 1 (unsupervised) | Stage 2 (supervised) | Walked at code level in |
|---|---|---|
| [[TSDAE]] | MNR-loss FT | [[hands-on-llm-ch10-creating-text-embedding-models|Ch 10]] |
| [[TSDAE]] | [[AugmentedSBERT]] | [[hands-on-llm-ch10-creating-text-embedding-models|Ch 10]] (via composition) |
| **[[MaskedLanguageModel\|MLM]]** | **Sequence-classification FT** | **[[hands-on-llm-ch11-fine-tuning-representation-models\|Ch 11]]** |
| MLM | MNR-loss FT | (compositional — both halves are walked) |

**Reference cited in Ch 11**: Chi Sun et al. *"How to Fine-Tune BERT for Text Classification?"* (CCL 2019) — the paper that established continued-pretraining-then-finetune as a worthwhile addition to the standard BERT-fine-tuning pipeline.
