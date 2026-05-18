---
title: "Made With ML — Exploratory Data Analysis (EDA)"
type: source
tags: [mlops, made-with-ml, eda, visualization]
date: 2026-05-15
source_file: raw/madewithml/mlops-exploratory-data-analysis.md
---

## Summary
This lesson reframes EDA as a goal-driven, cyclical process — not a fixed checklist of plots — used to *convince* yourself the dataset has enough signal for the task. It demonstrates two specific checks for the content-tagging example: a tag-distribution barplot (using `collections.Counter` + [[seaborn]]) and a per-class wordcloud (using `wordcloud.WordCloud` with NLTK stopwords) to verify that titles and descriptions carry class-discriminative tokens.

## Key Claims
- EDA is not "a prescribed set of plots" but a process for answering specific questions about your data's adequacy.
- EDA is cyclical — repeat it as data grows to catch distribution shifts and anomalies.
- The tag distribution (NLP 310, CV 285, other 106, mlops 63) shows mild imbalance that can be handled with over/under-sampling, class weights, or left as-is.
- Wordclouds confirmed the `title` feature carries strong class-discriminative signal for the running task.
- Tools used: `collections.Counter` for tag frequencies, [[matplotlib]] + [[seaborn]] for barplots, `wordcloud` for class-conditional token visualizations, and jupyter widgets for interactivity.
- The goal of every EDA pass is to validate (or refute) prior hypotheses about feature quality before moving to preprocessing.

## Key Quotes
> "Not just to visualize a prescribed set of plots (correlation matrix, etc.). Goal is to convince yourself that the data you have is sufficient for the task."

> "Not a one time process; as your data grows, you want to revisit EDA to catch distribution shifts, anomalies, etc."

## Connections
- [[MadeWithML]] — parent course.
- [[GokuMohandas]] — author.
- [[Anyscale]] — publisher.
- [[pandas]] — DataFrame manipulation.
- [[matplotlib]] — base plotting library.
- [[seaborn]] — barplot styling layer.
- [[Wordcloud]] — visualization library used for class-conditional tokens.
- [[NLTK]] — supplies the `STOPWORDS` set.
- [[ExploratoryDataAnalysis]] — the technique this lesson teaches.
- [[ClassImbalance]] — observed in the tag distribution.
- [[DataDrift]] — implicit motivation for repeating EDA over time.
- [[FeatureQuality]] — primary thing EDA validates.
- [[MLOps]] — surrounding discipline.
- [[Jupyter]] — interactive widgets used for tag selection.

## Contradictions
- None identified.
