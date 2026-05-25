---
title: "SetFit"
type: concept
tags: [few-shot, classification, fine-tuning, sentence-transformers, contrastive-learning]
sources: [hands-on-llm-ch11-fine-tuning-representation-models]
last_updated: 2026-05-23
---

# SetFit

**SetFit** is an efficient few-shot text-classification framework built on top of [[SentenceTransformers|sentence-transformers]] — introduced by [[LewisTunstall|Lewis Tunstall]] et al. in *"Efficient few-shot learning without prompts"* (arXiv:2209.11055, 2022). The headline claim from [[hands-on-llm-ch11-fine-tuning-representation-models|*Hands-On LLMs* Ch 11]]: *"Only a few labeled examples are needed for this framework to be competitive with fine-tuning a BERT-like model on a large, labeled dataset."*

## The three-step algorithm

1. **Sampling training data** — *"Based on in-class and out-class selection of labeled data it generates positive (similar) and negative (dissimilar) pairs of sentences."* Same-class pairs become positives, cross-class pairs become negatives.
2. **Fine-tuning embeddings** — *"Fine-tuning a pretrained embedding model based on the previously generated training data,"* via [[ContrastiveLearning|contrastive learning]] on the generated pairs.
3. **Training a classifier** — *"Create a classification head on top of the embedding model and train it using the previously generated training data."* Default: scikit-learn [[LogisticRegression|logistic regression]] on the fine-tuned embeddings.

## Combinatorial data expansion

Per Ch 11: *"When we have 16 sentences about sports, we can create 16 * (16 – 1) / 2 = 120 pairs that we label as positive pairs."* The combinatorial blow-up is what makes few-shot viable. Ch 11's worked example: **32 labeled sentences** (16 per class × 2 classes) → **1,280 generated sentence pairs** (`num_iterations=20` pair-combinations per sample × 32 samples × 2 [positive + negative]).

## Worked recipe (Ch 11)

```python
from setfit import sample_dataset, SetFitModel
from setfit import TrainingArguments as SetFitTrainingArguments
from setfit import Trainer as SetFitTrainer

# Simulate few-shot: 16 examples per class
sampled_train_data = sample_dataset(tomatoes["train"], num_samples=16)

# Pretrained embedding model
model = SetFitModel.from_pretrained("sentence-transformers/all-mpnet-base-v2")

# Training args
args = SetFitTrainingArguments(
    num_epochs=3,        # epochs for contrastive learning
    num_iterations=20    # text pairs to generate per sample
)
args.eval_strategy = args.evaluation_strategy

trainer = SetFitTrainer(
    model=model, args=args,
    train_dataset=sampled_train_data,
    eval_dataset=test_data,
    metric="f1"
)
trainer.train()
trainer.evaluate()  # {'f1': 0.8363988383349468}
```

## Result

**32 labels → F1 = 0.85 on Rotten Tomatoes.** *"With only 32 labeled documents, we get an F1 score of 0.85 ... in Chapter 2, we got the same performance but instead trained a logistic regression model on the embeddings of the full data. Thus, this pipeline demonstrates the potential of taking the time to label just a few instances."*

## Differentiable head alternative

Default head is logistic regression. For a differentiable head trained end-to-end:

```python
model = SetFitModel.from_pretrained(
    "sentence-transformers/all-mpnet-base-v2",
    use_differentiable_head=True,
    head_params={"out_features": num_classes},
)
```

## Zero-shot support

*"Not only can SetFit perform few-shot classification tasks, but it also has support for when you have no labels at all, also called zero-shot classification. SetFit generates synthetic examples from the label names to resemble the classification task and then trains a SetFit model on them."* Example: labels `happy / sad` → synthetic data `"The example is happy"` / `"This example is sad"`.

## Why SetFit works

The contrastive sentence-pair construction (Step 1) leverages a known property of class structure: same-class sentences are semantically similar, cross-class sentences are semantically dissimilar. The contrastive fine-tuning step (Step 2) reshapes the [[SentenceTransformers|SentenceTransformer]]'s embedding geometry to cluster the available classes; the simple downstream classifier (Step 3) then operates on a representation tuned for the task.

## Connections

- [[hands-on-llm-ch11-fine-tuning-representation-models]] — primary source.
- [[LewisTunstall]] — SetFit first author.
- [[FewShotLearning]] — the broader paradigm SetFit specializes for embedding-based classification.
- [[ContrastiveLearning]] — the underlying loss family.
- [[SentenceTransformers]] — the embedding-model substrate.
- [[AllMPNetBaseV2]] — Ch 11's worked SentenceTransformer base.
- [[LogisticRegression]] — default classification head.
- [[ZeroShotClassification]] — SetFit's no-labels extension.
- [[HuggingFace]] — distributes the `setfit` package.
