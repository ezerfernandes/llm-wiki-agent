---
title: "GPL (Generative Pseudo-Labeling)"
type: concept
tags: [unsupervised, domain-adaptation, embeddings, dense-retrieval, pseudo-labeling]
sources: [hands-on-llm-ch10-creating-text-embedding-models]
last_updated: 2026-05-23
---

# GPL (Generative Pseudo-Labeling)

**GPL — Generative Pseudo-Labeling** — an unsupervised technique for **domain adaptation of dense retrieval models**, introduced by Wang, Thakur, Reimers & Gurevych 2021 (arXiv:2112.07577 — *"GPL: Generative Pseudo Labeling for Unsupervised Domain Adaptation of Dense Retrieval"*).

Per [[hands-on-llm-ch10-creating-text-embedding-models|*Hands-On LLMs* Ch 10]]: GPL is one of four named unsupervised techniques (alongside [[SimCSE]], [[ContrastiveTension]], [[TSDAE]]) for creating sentence embeddings without labels. Ch 10 names GPL but does not walk a code example.

## The GPL trick

For a target domain corpus without labeled query-document pairs:

1. **Generate pseudo-queries** for each document using a query-generation model (typically a T5-style model trained on MS-MARCO).
2. **Mine hard negatives** for each (query, document) pair using a pretrained dense retrieval model.
3. **Score the (query, document, negative) triplets** with a cross-encoder to get fine-grained similarity scores.
4. **Train the bi-encoder** via [[knowledgedistillation|MarginMSE knowledge distillation]] against the cross-encoder scores.

The structural insight: dense-retrieval domain adaptation needs query-document pairs, but the target domain doesn't have them. GPL synthesizes them via query generation, then distills cross-encoder quality into a bi-encoder.

## GPL vs TSDAE

Both target [[DomainAdaptation|domain adaptation]] but via different mechanisms:

- **TSDAE**: pure denoising auto-encoder on the target corpus (no queries needed); produces a domain-adapted encoder ready for downstream fine-tuning.
- **GPL**: synthesizes query-document pairs in the target domain via query generation + cross-encoder scoring; trains the bi-encoder directly on retrieval-style data.

Ch 10 focuses on TSDAE for its broader applicability but flags GPL as the alternative when **dense retrieval** is the specific downstream task.

## Connections

- [[DomainAdaptation]] / [[AdaptivePretraining]] — the broader problem GPL solves.
- [[TSDAE]] / [[SimCSE]] / [[ContrastiveTension]] — the other unsupervised techniques Ch 10 names.
- [[DenseRetrieval]] — the downstream task GPL targets.
- [[knowledgedistillation]] — the cross-encoder → bi-encoder mechanism.
- [[CrossEncoder]] / [[BiEncoder]] — the architectural pair GPL bridges.
- [[HardNegatives]] — mined during the GPL pipeline.
- [[ContrastiveLearning]] — the paradigm.
- [[KexinWang]] / [[NandanThakur]] / [[NilsReimers]] / [[IrynaGurevych]] — GPL authors.
- [[hands-on-llm-ch10-creating-text-embedding-models]] — primary source for the named-but-not-walked mention.
