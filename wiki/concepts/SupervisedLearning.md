---
title: "Supervised Learning"
type: concept
tags: [paradigm, statistical-learning]
sources: [islr-seventh-printing, d2l-introduction]
last_updated: 2026-05-16
---

# Supervised Learning

Building a model that predicts an output $Y$ from inputs $X$, given training pairs $\{(x_i, y_i)\}_{i=1}^n$ — "the supervision comes from the supervisors who provide the labeled examples" ([[d2l-introduction]]). Splits by response type into [[Regression]] (continuous $Y$) and [[Classification]] (categorical $Y$). The dominant branch of [[StatisticalLearning]] and the subject of ISLR Chapters 2–9; [[d2l-introduction]] states it "accounts for the majority of successful applications of machine learning in industry."

## Sub-tasks per [[d2l-introduction]]

Beyond the basic regression / classification distinction, the chapter catalogs a richer taxonomy:

- **Tagging / multi-label classification** — classes are not mutually exclusive (Town Musicians of Bremen image: cat *and* dog *and* donkey *and* rooster). Extreme case: PubMed's 28k-tag MeSH ontology.
- **Hierarchical classification** — labels form a taxonomy (Linnaean phylogeny); not all errors are equal.
- **Search and ranking** — order a set of relevant items (PageRank was an early scoring system).
- **[[RecommenderSystems|Recommender systems]]** — search + personalization.
- **Sequence learning** — variable-length inputs/outputs ([[machinetranslation|machine translation]], [[SpeechRecognition|speech recognition]], part-of-speech tagging).

## Connections
- [[StatisticalLearning]] — parent (ISLR framing).
- [[MachineLearning]] — parent (D2L framing).
- [[Regression]], [[Classification]] — sub-paradigms.
- [[BiasVarianceTradeoff]] — central diagnostic.
- [[RecommenderSystems]], [[machinetranslation]] — applied sequence/personalization variants.
- [[islr-seventh-printing]], [[d2l-introduction]] — survey-textbook coverage.
