---
title: "SimCSE (Simple Contrastive Learning of Sentence Embeddings)"
type: concept
tags: [unsupervised, supervised, embeddings, contrastive-learning, sentence-transformers]
sources: [hands-on-llm-ch10-creating-text-embedding-models]
last_updated: 2026-05-23
---

# SimCSE

**SimCSE** — *"Simple Contrastive Learning of Sentence Embeddings"* — a contrastive-learning technique for sentence embeddings, available in both **unsupervised** (dropout-as-augmentation) and **supervised** ([[NLI]]-based) flavors. Introduced by Gao, Yao & Chen 2021 (arXiv:2104.08821).

Per [[hands-on-llm-ch10-creating-text-embedding-models|*Hands-On LLMs* Ch 10]]: SimCSE is one of four named unsupervised sentence-embedding techniques (alongside [[ContrastiveTension]], [[TSDAE]], and [[GPL]]), though Ch 10 chooses to walk **TSDAE** in detail rather than SimCSE.

## The unsupervised SimCSE trick

The key insight: feed the same sentence through the encoder **twice** with different dropout masks. Treat the two embeddings as a positive pair (since they encode the same sentence) and all other in-batch sentences as negatives. Dropout-as-augmentation is the cheapest possible data augmentation — no token-level noise injection, no external augmentation library.

## The supervised SimCSE variant

For supervised SimCSE, use [[NLI]] data: entailment pairs as positives, contradictions as hard negatives. Closely related to the [[MultipleNegativesRankingLoss|MNR loss]] recipe Ch 10 walks, but with **explicit hard negatives** from contradictions rather than just in-batch easy negatives.

## Position in Ch 10's landscape

Ch 10 names SimCSE briefly in the unsupervised-techniques list but does not walk a code example. The chapter's focus is on TSDAE because *"it has shown great performance on unsupervised tasks as well as domain adaptation."*

## Connections

- [[ContrastiveLearning]] — the paradigm.
- [[TSDAE]] / [[ContrastiveTension]] / [[GPL]] — the other unsupervised techniques Ch 10 names.
- [[MultipleNegativesRankingLoss]] — closely related to supervised SimCSE.
- [[HardNegatives]] — supervised SimCSE uses NLI contradictions as hard negatives.
- [[SentenceTransformers]] — supports SimCSE via the `MultipleNegativesRankingLoss` (the in-batch sampling is the SimCSE mechanism).
- [[TianyuGao]] / [[XingchengYao]] / [[DanqiChen]] — SimCSE authors (Gao, Yao & Chen 2021).
- [[hands-on-llm-ch10-creating-text-embedding-models]] — primary source for the named-but-not-walked mention.
