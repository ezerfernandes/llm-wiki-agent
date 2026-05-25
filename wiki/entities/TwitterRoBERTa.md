---
title: "Twitter-RoBERTa (cardiffnlp)"
type: entity
tags: [model, sentiment-analysis, roberta, huggingface, cardiffnlp]
sources: [hands-on-llm-ch04-text-classification]
last_updated: 2026-05-23
---

# Twitter-RoBERTa (cardiffnlp)

A [[RoBERTa]] checkpoint fine-tuned on tweets for **3-class sentiment analysis** (negative / neutral / positive), distributed by [[CardiffNLP]] on the [[HuggingFace|Hugging Face]] Hub as `cardiffnlp/twitter-roberta-base-sentiment-latest`. The canonical example of a **task-specific representation model** — *"a RoBERTa model fine-tuned on tweets for sentiment analysis."*

## From [[hands-on-llm-ch04-text-classification|*Hands-On LLMs* Ch 4]]

Ch 4 uses Twitter-RoBERTa as its **task-specific representation-model** demo for sentiment classification on the [[RottenTomatoes|rotten_tomatoes]] dataset:

```python
from transformers import pipeline

model_path = "cardiffnlp/twitter-roberta-base-sentiment-latest"
pipe = pipeline(
    model=model_path,
    tokenizer=model_path,
    return_all_scores=True,
    device="cuda:0"
)
```

The model returns three score outputs per input — `[negative, neutral, positive]` — which the chapter collapses to binary by `argmax([negative_score, positive_score])`.

**Result on Rotten Tomatoes test split**: **F1 = 0.80** weighted average — *"great for a model not trained specifically on our domain data!"* The ~5 F1-point gap to the embedding + logistic regression recipe motivates the chapter's pivot to embedding models.

The chapter notes an in-domain alternative would have been `distilbert-base-uncased-finetuned-sst-2-english` (DistilBERT fine-tuned on Stanford Sentiment Treebank), but deliberately picks Twitter-RoBERTa to demonstrate **how a pretrained task-specific model generalizes across domain** (Twitter → movie reviews).

## Connections

- [[hands-on-llm-ch04-text-classification]] — primary source.
- [[CardiffNLP]] — the research group that produced this checkpoint.
- [[RoBERTa]] — the underlying architecture.
- [[bert]] — the architectural ancestor.
- [[SentimentAnalysis]] / [[TextClassification]] — the task.
- [[RottenTomatoes]] — Ch 4's evaluation dataset.
- [[HuggingFace]] — distribution channel.
- [[TaskSpecificModel]] — the model-flavor category.
- [[DistilBERT]] — the in-domain alternative Ch 4 names (SST-2 fine-tuned).
