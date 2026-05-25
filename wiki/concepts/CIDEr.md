---
title: "CIDEr"
type: concept
tags: [evaluation, metric, image-captioning]
sources: [ai-engineering-ch03-evaluation-methodology]
last_updated: 2024-12-04
---

# CIDEr

**CIDEr** — *Consensus-based Image Description Evaluation* (Vedantam, Zitnick & Parikh 2015) — is a [[LexicalSimilarity|lexical-similarity]] metric originally designed for **image-captioning** evaluation. Per [[ai-engineering-ch03-evaluation-methodology|*AI Engineering* Ch 3]], CIDEr is one of the *"common metrics for lexical similarity"* alongside [[bleu|BLEU]], [[ROUGE]], [[METEOR]], and [[TER]].

## Design

CIDEr computes TF-IDF-weighted n-gram overlap between a candidate caption and a *set* of reference captions. The "consensus" angle: an n-gram that appears in many reference captions is weighted higher than one that appears in only one — capturing what humans agree on.

## Position

- Used by benchmarks like **COCO Captions** (named explicitly in Ch 3 alongside WMT and GEMv2).
- Like its lexical-similarity siblings, has been partly displaced by [[BERTScore]] / [[CLIPScore]] / [[LLMAsAJudge|AI-as-judge]] in the foundation-model era.

## Connections

- [[ai-engineering-ch03-evaluation-methodology]] — primary source.
- [[bleu|BLEU]] / [[ROUGE]] / [[METEOR]] / [[TER]] — sibling lexical-similarity metrics.
- [[LexicalSimilarity]] / [[NGramSimilarity]] — parent.
- [[BERTScore]] — semantic-similarity successor.
- [[CLIP]] — image-text embedding model often used for CLIP-Score, a CIDEr alternative.
