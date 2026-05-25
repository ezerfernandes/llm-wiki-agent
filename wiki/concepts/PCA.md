---
title: "PCA"
type: concept
tags: [dimensionality-reduction, statistics]
sources: [madewithml-preprocessing, hands-on-llm-ch05-text-clustering-topic-modeling]
last_updated: 2026-05-23
---

# PCA

Principal Component Analysis — a linear projection onto orthogonal directions of maximal variance. See [[PrincipalComponentAnalysis]] for the full treatment; used to mitigate [[CurseOfDimensionality]].

## From [[hands-on-llm-ch05-text-clustering-topic-modeling|*Hands-On LLMs* Ch 5]]

Ch 5 names PCA ([[HaroldHotelling|Hotelling]], 1933, footnote 1) as the **linear-projection baseline** against which [[UMAP]] is contrasted in the [[BERTopic]] pipeline. The chapter chooses UMAP because *"it tends to handle nonlinear relationships and structures a bit better than PCA"* — but explicitly notes that PCA remains a valid alternative in BERTopic's modular pipeline (`umap_model` can be swapped for any reducer with a compatible API).

## Connections

- [[madewithml-preprocessing]] — preprocessing source.
- [[hands-on-llm-ch05-text-clustering-topic-modeling]] — Ch 5 contrasts PCA against UMAP.
- [[UMAP]] — the nonlinear successor used in BERTopic.
- [[DimensionalityReduction]] / [[CurseOfDimensionality]] — parent concepts.
- [[PrincipalComponentAnalysis]] — the full treatment.
- [[HaroldHotelling]] — the 1933 originator.
