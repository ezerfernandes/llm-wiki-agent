---
title: "scikit-learn"
type: entity
tags: [library, python, classical-ml]
sources: [hands-on-llm-ch04-text-classification, hands-on-llm-ch05-text-clustering-topic-modeling, mechanics-of-ml]
last_updated: 2026-06-04
---

# scikit-learn

The de-facto Python library for **classical machine learning** — linear models, tree methods, SVMs, clustering, dimensionality reduction, and the metric / evaluation utilities used across almost every NLP / LLM application stack. Originated as a Google Summer of Code 2007 project (David Cournapeau); now maintained by a broad open-source community.

## From [[hands-on-llm-ch04-text-classification|*Hands-On LLMs* Ch 4]]

Ch 4 is the **first wiki worked example where scikit-learn is the explicit classifier on top of LLM embeddings**. Three sklearn primitives are used:

- `sklearn.linear_model.LogisticRegression` — the **classification head** trained on top of frozen [[AllMPNetBaseV2|sentence-transformers]] embeddings (8,530 × 768 feature matrix). Result on [[RottenTomatoes|Rotten Tomatoes]]: F1 = 0.85.
- `sklearn.metrics.classification_report` — generates the per-class precision / recall / F1-score / support table the chapter uses as its **evaluation primitive throughout**. Used to compute the F1 = 0.80 / 0.85 / 0.78 / 0.84 / 0.91 progression across the four model regimes.
- `sklearn.metrics.pairwise.cosine_similarity` — used to assign labels in **[[ZeroShotClassification|zero-shot embedding classification]]**: `cosine_similarity(test_embeddings, label_embeddings)` → `argmax` along the label axis.

```python
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.metrics.pairwise import cosine_similarity

clf = LogisticRegression(random_state=42)
clf.fit(train_embeddings, data["train"]["label"])
y_pred = clf.predict(test_embeddings)
print(classification_report(data["test"]["label"], y_pred,
    target_names=["Negative Review", "Positive Review"]))
```

## Why it matters in the LLM stack

The chapter's pedagogical commitment to **classical baselines** — *"it is highly advised to compare these examples against classic, but strong baselines such as representing text with TF-IDF and training a logistic regression classifier on top of that"* — depends entirely on scikit-learn as the substrate. Even when the embeddings come from a 2024 sentence-transformer, the head is a 2007-vintage logistic regression with `random_state=42`.

## From [[hands-on-llm-ch05-text-clustering-topic-modeling|*Hands-On LLMs* Ch 5]]

Ch 5 adds **`sklearn.feature_extraction.text.CountVectorizer`** to the wiki's scikit-learn footprint. CountVectorizer is the bag-of-words primitive [[BERTopic]] uses **internally** for the [[ClassBasedTFIDF|c-TF-IDF]] step — concatenate documents within a cluster, count tokens, multiply by the cluster-IDF weight. Optionally strip English stopwords via `CountVectorizer(stop_words="english")` to clean up topic representations before the c-TF-IDF reweighting:

```python
from sklearn.feature_extraction.text import CountVectorizer
vectorizer_model = CountVectorizer(stop_words="english")
topic_model.update_topics(abstracts, vectorizer_model=vectorizer_model)
```

This makes scikit-learn the consistent thread across both Ch 4 (logistic-regression head + classification_report + cosine_similarity) and Ch 5 (CountVectorizer for c-TF-IDF) — establishing the **second wiki appearance of sklearn as an LLM-stack dependency**.

## From [[mechanics-of-ml|*The Mechanics of Machine Learning*]]

This is the wiki's **classical-ML, tabular-data** use of scikit-learn — the library is the book's modeling engine throughout. The workhorses are `sklearn.ensemble.RandomForestRegressor` / `RandomForestClassifier` (with `oob_score=True` for the built-in [[OutOfBagScore|OOB]] estimate, `n_jobs=-1` for parallelism), benchmarked against `LogisticRegression`, `Lasso`, and `GradientBoostingRegressor`. The book leans on sklearn's RF hyperparameters (`n_estimators`, `max_features`, `min_samples_leaf`) for its sequential-tuning recipe and on `feature_importances_` for iterative feature pruning. Pairs with the `category_encoders` library for [[TargetEncoding|target encoding]]. Establishes sklearn's role beyond the LLM stack — as the substrate for the wiki's Random-Forest-first applied-ML source.

## Connections

- [[mechanics-of-ml]] — RandomForest{Regressor,Classifier} as the book's default model.
- [[RandomForests]] / [[OutOfBagScore]] — the RF estimator and its OOB metric.
- [[LogisticRegression]] — the chapter's chosen classifier.
- [[F1Score]] / [[ConfusionMatrix]] / [[Precision]] / [[Recall]] — the metrics sklearn computes via `classification_report`.
- [[CosineSimilarity]] — used for zero-shot label assignment.
- [[TFIDF]] / [[ClassBasedTFIDF]] — TF-IDF as a classical baseline (Ch 4) and as BERTopic's class-based variant (Ch 5).
- [[BagOfWords]] — what `CountVectorizer` produces.
- [[BERTopic]] — Ch 5 BERTopic uses sklearn's `CountVectorizer` internally.
- [[HuggingFace]] / [[SentenceTransformers]] — the upstream embedding source in Ch 4's pipeline.
- [[hands-on-llm-ch04-text-classification]] — primary source.
- [[hands-on-llm-ch05-text-clustering-topic-modeling]] — Ch 5 source (CountVectorizer + c-TF-IDF).
