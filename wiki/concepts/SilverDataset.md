---
title: "Silver Dataset"
type: concept
tags: [data-quality, labeling, training-data, augmented-sbert, pseudo-labeling]
sources: [hands-on-llm-ch10-creating-text-embedding-models]
last_updated: 2026-05-23
---

# Silver Dataset

A **silver dataset** is a **model-labeled (not human-labeled) dataset** — *"fully annotated but not necessarily the ground truth as it was generated through predictions"* of a stronger model. The cheap, large counterpart to the [[GoldDataset|gold dataset]] in hybrid data pipelines.

Per [[hands-on-llm-ch10-creating-text-embedding-models|*Hands-On LLMs* Ch 10]]: *"A silver dataset is also fully annotated but is not necessarily the ground truth as it was generated through predictions of the cross-encoder."*

## In [[AugmentedSBERT]]

Ch 10's worked example generates the silver dataset by **using a cross-encoder fine-tuned on the gold dataset to predict labels for a larger pool of unlabeled sentence pairs**:

```python
# After training the cross-encoder on the gold dataset
output = cross_encoder.predict(pairs, apply_softmax=True, show_progress_bar=True)
silver = pd.DataFrame({
    "sentence1": silver["premise"],
    "sentence2": silver["hypothesis"],
    "label": np.argmax(output, axis=1),
})
```

In the worked example: 10k gold pairs trained a cross-encoder; the remaining 40k MNLI pairs (unlabeled, simulated) were labeled by the cross-encoder → 40k silver pairs. **Combined gold + silver = 50k training pairs** for the bi-encoder, with the bi-encoder reaching STS-B = 0.71 (vs 0.72 for the full-50k-labeled baseline).

## Quality-of-silver diagnostic

Per Ch 10: *"You can test the quality of your silver data by also training your embedding model only on the gold dataset. The difference in performance indicates how much your silver dataset potentially adds to the quality of the model."*

The diagnostic is intuitive: if gold-only and gold+silver produce similar performance, the silver pairs aren't adding signal — either the cross-encoder labeler is too noisy, or the silver pool is too topically narrow.

## Related — synthetic data

The silver-dataset concept is closely related to **[[AIPoweredDataSynthesis|AI-powered data synthesis]]** (per [[ai-engineering-ch08-dataset-engineering|Huyen Ch 8]]): both substitute model-generated labels for human-generated labels at scale, trading some quality for much more data. The difference: silver datasets typically **re-label an existing unlabeled pool**; synthetic data typically **generates new examples from scratch**.

## Connections

- [[GoldDataset]] — the complement.
- [[AugmentedSBERT]] — the Ch 10 technique that uses silver labels for bi-encoder training.
- [[CrossEncoder]] — the cross-encoder is the canonical silver-labeler.
- [[AIPoweredDataSynthesis]] / [[DataAugmentation]] — adjacent data-engineering concepts.
- [[PseudoLabeling]] — the broader ML term for model-labeled training data.
- [[hands-on-llm-ch10-creating-text-embedding-models]] — primary source.
