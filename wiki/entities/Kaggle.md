---
title: "Kaggle"
type: entity
tags: [platform, competition, ml-community]
sources: [d2l-multilayer-perceptrons, ai-engineering-ch08-dataset-engineering, mechanics-of-ml]
last_updated: 2026-06-04
---

# Kaggle

Online platform hosting machine-learning competitions; founded 2010, acquired by [[Google]] in 2017. Each competition centres on a dataset, often sponsored by industry stakeholders offering prize purses; participants submit predictions and are ranked on a held-out leaderboard.

## Role in this wiki

- **D2L MLP capstone.** [[d2l-multilayer-perceptrons]] §Predicting House Prices on Kaggle uses the **House Prices: Advanced Regression Techniques** competition (Ames, Iowa 2006–2010; data collected by [[Cock-2011|De Cock 2011]]) as the chapter's end-to-end real-data case study — Pandas preprocessing + MLP-with-dropout pipeline.
- **Community function.** Forums, public notebooks, and "Discussions" tabs make Kaggle a primary code-sharing venue for applied ML beyond the research / arxiv axis.

## D2L's framing

> "While leaderboard chasing often spirals out of control, with researchers focusing myopically on preprocessing steps rather than asking fundamental questions, there is also tremendous value in the objectivity of a platform that facilitates direct quantitative comparisons among competing approaches as well as code sharing so that everyone can learn what did and did not work."

## From [[mechanics-of-ml|*The Mechanics of Machine Learning*]]

Both of the book's running datasets are Kaggle competitions: the **Two Sigma Connect rental-listing** data (NYC apartment-rent regression) and **"Blue Book for Bulldozers"** (heavy-equipment auction-price, time-series regression). The bulldozer chapter benchmarks the final [[RandomForests|Random Forest]] against the public leaderboard — test [[RMSLE]] 0.2396 places it ≈ top 5% of competitors — and uses Kaggle as a cautionary tale of [[Overfitting|overfitting]]: 108 of 475 competitors achieved perfect validation scores yet collapsed on the hidden test set, illustrating why a held-out test set is irreplaceable.

## Connections

- [[mechanics-of-ml]] — Two Sigma rentals + Blue Book for Bulldozers as the book's datasets.
- [[d2l-multilayer-perceptrons]] — uses Kaggle as the chapter capstone.
- [[Google]] — current owner (2017 acquisition).
- [[FashionMNIST]] / [[MNIST]] — adjacent canonical benchmarks within the wiki.

## From [[ai-engineering-ch08-dataset-engineering|AI Engineering Ch 8]]

Ch 8 names Kaggle as one of the top public-dataset sources for AI engineering:

> "Hugging Face and Kaggle each host hundreds of thousands of datasets."

Within Ch 8's [[DataAcquisition|data-acquisition]] discussion, Kaggle sits alongside [[HuggingFace|Hugging Face]], Google Dataset Search, Data.gov, ICPSR, UCI ML Repository, OpenML, Open Data Network, AWS Open Data, [[EleutherAI|Eleuther]] lm-evaluation-harness, and the [[SNAP|Stanford Network Dataset Collection]] as primary resources for sourcing training data — with the standing caveat that **you should never fully trust available data without inspection**.

The chapter also references the Kaggle CIFAR-10 test dataset in the [[OnePixelAttack|one-pixel attack]] discussion (Su et al. 2017) — single-pixel perturbations misclassified 67.97% of natural Kaggle CIFAR-10 test images.
