---
title: "Masked Language Model"
type: concept
tags: [concept, pretraining, objective]
sources: [1810.04805-bert, d2l-nlp-pretraining, hands-on-llm-ch01-introduction-to-llms, hands-on-llm-ch10-creating-text-embedding-models, hands-on-llm-ch11-fine-tuning-representation-models]
last_updated: 2026-05-23
---

# Masked Language Model

Pre-training objective introduced (or popularized) by [[BERT]] in [[1810.04805-bert]]. Inspired by the Cloze task (Taylor, 1953): randomly mask a fraction of input tokens and predict the originals from surrounding context. This breaks the dependency cycle that would otherwise prevent bidirectional conditioning — a deep bidirectional model trained on standard next-token prediction could trivially "see itself" through multiple layers.

## BERT's specific recipe
- Mask **15%** of WordPiece tokens per sequence.
- Of the chosen positions: **80%** replaced with `[MASK]`, **10%** with a random token, **10%** left unchanged.
- Only the masked positions contribute to the cross-entropy loss.

The 80/10/10 split mitigates the **pre-train / fine-tune mismatch** that arises because `[MASK]` never appears during fine-tuning. The "10% unchanged" branch biases the representation toward the actual observed token.

MLM converges marginally slower than left-to-right LM (since only 15% of positions contribute gradient per batch), but the absolute task accuracy crosses over almost immediately, and the deep bidirectionality is empirically responsible for the majority of BERT's improvement over GPT-style baselines.

Variants: SpanBERT (mask contiguous spans), ELECTRA (replaced-token detection), T5 (sentinel-token span corruption), and the implicit-MLM objective of many later encoder models all descend from this design.

## From [[hands-on-llm-ch01-introduction-to-llms|*Hands-On LLMs* Ch 1]]

Ch 1's intuitive framing for MLM:

> "Training these encoder stacks can be a difficult task that BERT approaches by adopting a technique called masked language modeling. ... this method masks a part of the input for the model to predict. This prediction task is difficult but allows BERT to create more accurate (intermediate) representations of the input." — Ch 1

The chapter ties MLM to [[bert|BERT]]'s status as a [[RepresentationModel|representation model]] — the masked-prediction objective forces the encoder to produce sequence-aware token representations that capture context bidirectionally, which is then exposed as the embedding output the downstream task head consumes.

## From [[hands-on-llm-ch10-creating-text-embedding-models|*Hands-On LLMs* Ch 10]]

Ch 10 names MLM in two roles:

1. **TSDAE's predecessor at the token level**: per Ch 10, [[TSDAE]]'s denoising auto-encoder objective *"is very similar to masked language modeling, where we try to reconstruct and learn certain masked words. Here, instead of reconstructing masked words, we try to reconstruct the entire sentence."* TSDAE is the **sentence-level analog of MLM**.
2. **A Stage-1 unsupervised technique for [[DomainAdaptation|domain adaptation]]**: per Ch 10's closing recipe, *"you can also perform masked language modeling on the pretrained BERT model to first adapt it to your domain. Then, you can use this fine-tuned BERT model as the base for training your embedding model. This is a form of domain adaptation. In the next chapter, we will apply masked language modeling on a pretrained model."*

Ch 10 explicitly forward-references **Ch 11** for the MLM-on-pretrained-BERT recipe. The two-stage pipeline:

- **Stage 1**: MLM (or [[TSDAE]]) on target-domain unlabeled text → domain-adapted BERT.
- **Stage 2**: Standard supervised contrastive fine-tuning ([[MultipleNegativesRankingLoss|MNR loss]]) on whatever labeled pairs are available → domain-adapted SBERT.

This is the **canonical [[AdaptivePretraining|adaptive pretraining]] recipe** for embedding-model domain adaptation that Ch 10 promises Ch 11 will walk at code level.

## From [[hands-on-llm-ch11-fine-tuning-representation-models|*Hands-On LLMs* Ch 11]]

Ch 11 walks **MLM as a continued-pretraining objective** (not as a from-scratch creation objective). The runnable code uses `transformers.AutoModelForMaskedLM` + [[DataCollatorForLanguageModeling]] with `mlm_probability=0.15`:

```python
from transformers import AutoModelForMaskedLM, DataCollatorForLanguageModeling

model = AutoModelForMaskedLM.from_pretrained("bert-base-cased")
data_collator = DataCollatorForLanguageModeling(
    tokenizer=tokenizer, mlm=True, mlm_probability=0.15
)
```

Ch 11 introduces the **[[TokenMasking|token masking]] vs [[WholeWordMasking|whole-word masking]]** distinction at runnable-code granularity — the latter via `DataCollatorForWholeWordMask`. Per Ch 11: *"Generally, predicting whole words tends to be more complicated than tokens, which makes the model perform better as it needs to learn more accurate and precise representations during training. However, it tends to take a bit more time to converge."*

The chapter's **qualitative MLM diagnostic** is `pipeline("fill-mask")` on a domain-relevant prompt — for Rotten Tomatoes, *"What a horrible [MASK]!"* shifts from `idea / dream / day` (base BERT) to `movie / film / mess` (MLM-continued BERT). See [[FillMaskPipeline]].

Ch 11 delivers on the Ch 10 promise — running MLM-on-pretrained-BERT as Stage 1 of [[DomainAdaptation|domain adaptation]], with the downstream classification fine-tune (Stage 2) loaded via `AutoModelForSequenceClassification.from_pretrained("mlm", num_labels=2)`. This completes the [[AdaptivePretraining|adaptive-pretraining]] recipe matrix Ch 10 left half-finished.
