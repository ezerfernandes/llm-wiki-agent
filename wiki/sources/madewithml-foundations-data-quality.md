---
title: "Made With ML — Data Quality"
type: source
tags: [foundations, made-with-ml, machine-learning, data-quality]
date: 2026-05-15
source_file: raw/madewithml/foundations-data-quality.md
---

## Summary
A short, illustrative lesson making the case that **data quality dominates model quality**. Trains the same MLP on a synthetic tumor-classification dataset (leukocyte count + blood pressure → benign / malignant) twice — once on the full dataset and once on a deliberately reduced / poorly-representative subset — and shows that the reduced-data model achieves similar training metrics but produces wildly wrong predictions on a known-malignant point near the decision boundary. The takeaway: garbage in, garbage out, and "simple models → complex models".

## Key Claims
- Model quality is bounded by data quality: identical architectures trained on a representative vs. a sparse / skewed dataset behave very differently on edge cases even when headline accuracy looks similar.
- High accuracy on a non-representative test split is not evidence of a trustworthy model — the test set inherits whatever bias is in the data.
- Decision boundaries learned from small / unbalanced data can sit dangerously close to legitimate points of the minority class.
- Before any modeling, the practitioner should ask whether the dataset truly represents the task; if not, no amount of model complexity will fix it.
- Start with simple models and only add complexity when justified by the task and data — neural networks are not the right first choice for every problem.
- The lesson is intentionally synthetic and explicitly disclaims any clinical relevance — it is a teaching device for [[DataQuality]] intuition.

## Key Quotes
> "The quality of the predictions directly corresponds to the quality of data you train the model with; garbage in, garbage out." — Overview

> "Models are not crystal balls. So it's important that before any machine learning, we really look at our data and ask ourselves if it is truly representative for the task we want to solve. The model itself may fit really well and generalize well on your data but if the data is of poor quality to begin with, the model cannot be trusted." — Takeaway

> "Striking this balance in model complexity is one of the key tasks of your data scientists. simple models → complex models" — Takeaway

## Connections
- [[MadeWithML]] — course this lesson belongs to
- [[GokuMohandas]] — author
- [[PyTorch]] — used for the MLP
- [[DataQuality]] — central concept
- [[NeuralNetwork]] — model used to illustrate the point
- [[Overfitting]] — implicit risk when data is unrepresentative
- [[DecisionBoundary]] — visualized to show failure of the reduced-data model
- [[ModelComplexity]] — "simple models → complex models" mantra
- [[Generalization]] — what quality data enables and poor data prevents

## Contradictions
- None identified.
