---
title: "Contrastive Learning"
type: concept
tags: [paradigm, representation-learning, self-supervised]
sources: [2408.08849-ecg-chat, hands-on-llm-ch09-multimodal-llms, hands-on-llm-ch10-creating-text-embedding-models, hands-on-llm-ch11-fine-tuning-representation-models]
last_updated: 2026-05-23
---

# Contrastive Learning

A representation-learning paradigm that trains an encoder to **pull paired (anchor, positive) embeddings together while pushing unpaired (anchor, negative) embeddings apart** under a similarity metric (typically cosine). Foundational to vision-language pretraining ([[CoCa]], CLIP, ALIGN) and biomedical-text retrieval ([[MedCPT]]).

The standard loss form (InfoNCE / NT-Xent):
$$\mathcal{L}_{a \to b} = \sum_i \log \frac{\exp(x_i^\top y_i / \sigma)}{\sum_j \exp(x_i^\top y_j / \sigma)}$$
with a symmetric counterpart $\mathcal{L}_{b \to a}$ and a temperature $\sigma$.

## In [[2408.08849-ecg-chat|ECG-Chat]]

The [[ECGEncoder|1d-ViT]] and [[MedCPT]] text encoder are trained under the [[CoCa]] dual-loss objective ($\mathcal{L}_{con} + 2\mathcal{L}_{cap}$) on 805K ECG-text pairs. **Without text-side augmentation ([[WaveformDataEnhancement|WDE]]), the contrastive loss fails to converge** because templated medical reports collapse positive/negative distinctions — WDE adds per-record waveform morphology to the text side to artificially distinguish samples.

## In [[hands-on-llm-ch09-multimodal-llms|*Hands-On LLMs* Ch 9]]

Ch 9 introduces contrastive learning as the **training paradigm behind [[CLIP]]** — *"this method is called contrastive learning, and we will go in depth into its inner workings in Chapter 10 where we will create our own embedding model."* The chapter walks the three-step CLIP recipe (encode image + text → cosine similarity → optimize encoders to maximize-similarity-for-paired / minimize-for-unpaired) and explicitly flags the **negatives are required** observation:

> *"to make sure the representations are as accurate as possible, negative examples of images and captions that are not related should also be included in the training process. Modeling similarity is not only knowing what makes things similar to one another, but also what makes them different and dissimilar."*

[[BLIP2|BLIP-2]]'s [[QFormer|Q-Former]] generalizes the contrastive idea by training on **three** related objectives simultaneously: [[ImageTextContrastive]] (the CLIP-style anchor-positive-negative loss), [[ImageTextMatching]] (binary classification of pair compatibility), and [[ImageGroundedTextGeneration]] (text-from-image generation). Ch 9 frames these as *"contrastive-like tasks"* — contrastive learning extended into a multi-objective representation-learning regime.

## Connections
- [[CoCa]] — the contrastive-captioner architecture.
- [[CLIP]] — the canonical contrastive multimodal embedding model.
- [[MedCPT]] — biomedical contrastive text encoder pretrained on PubMed search logs.
- [[WaveformDataEnhancement]] — the augmentation trick that rescues ECG contrastive training from convergence failure.
- [[NoiseContrastiveEstimation]] — historical predecessor of the InfoNCE-style losses.
- [[ImageTextContrastive]] / [[ImageTextMatching]] / [[ImageGroundedTextGeneration]] — the three [[QFormer|Q-Former]] objectives Ch 9 walks as *"contrastive-like"*.
- [[2408.08849-ecg-chat]] — wiki's first record of contrastive learning applied to ECG-text alignment.
- [[hands-on-llm-ch09-multimodal-llms]] — Ch 9's multimodal-embedding pedagogy.
- [[hands-on-llm-ch10-creating-text-embedding-models]] — the end-to-end contrastive-training chapter (now ingested — see section below).

## From [[hands-on-llm-ch10-creating-text-embedding-models|*Hands-On LLMs* Ch 10]]

Ch 10 is the **wiki's first runnable-code resolution** of contrastive learning — Chs 1, 2, 9 framed it as a paradigm; Ch 10 walks the full training procedure on a [[bert|BERT]] base with three loss functions on a [[GLUE]] [[MNLI]] subset:

> *"Contrastive learning is a technique that aims to train an embedding model such that similar documents are closer in vector space while dissimilar documents are further apart. ... it's very similar to the word2vec method from Chapter 2."* — Ch 10

**The contrastive-explanation framing**: Ch 10 grounds the technique in **contrastive explanation theory** (Tim Miller 2021, *"Contrastive explanation: A structural-model approach,"* The Knowledge Engineering Review 36: e14): *"understanding a particular case, 'Why P?' in contrast to alternatives, 'Why P and not Q?'"* The chapter's anecdotal frame is the bank robber asked *"Why did you rob a bank?"* who answers *"Because that is where the money is"* — a question that would have produced more information when framed as *"Why rob banks (P) instead of obeying the law (Q)?"* The contrast is what teaches.

**The data-construction discipline**: [[NLI]] datasets (entailment / contradiction / neutral) map directly to contrastive learning data — entailments are positives, contradictions are negatives. *"If you look closely at entailment and contradiction, then they describe the extent to which two inputs are similar to one another. As such, we can use NLI datasets to generate negative examples (contradictions) and positive examples (entailments) for contrastive learning."*

**The loss-function ladder** Ch 10 walks on the same 50k MNLI subset (all evaluated on [[STSB|STS-B]] Pearson cosine):

| Loss | Result |
|---|---|
| [[SoftmaxLoss]] | 0.59 |
| [[CosineSimilarityLoss]] | 0.72 |
| [[MultipleNegativesRankingLoss\|MNR loss]] (a.k.a. [[InfoNCE]] / [[NTXentLoss]]) | 0.80 |

**Loss-function choice can move performance by 20+ points on the same data** — the chapter's central pedagogical claim.

**The [[HardNegatives|negatives taxonomy]]** Ch 10 codifies as a wiki first:

- **[[EasyNegatives|Easy negatives]]** — random documents (what [[InBatchNegatives|in-batch negatives]] from MNR loss produce).
- **[[SemiHardNegatives|Semi-hard negatives]]** — cosine-similar but not the right pair (minable from a pretrained model).
- **[[HardNegatives|Hard negatives]]** — related-but-wrong (require manual or generative labeling).

**Connections added by Ch 10**:
- [[SBERTArchitecture]] / [[SiameseNetwork]] / [[BiEncoder]] — the structural prerequisites.
- [[MultipleNegativesRankingLoss]] / [[CosineSimilarityLoss]] / [[SoftmaxLoss]] — the three losses walked.
- [[InBatchNegatives]] / [[HardNegatives]] / [[SemiHardNegatives]] / [[EasyNegatives]] — the negative-mining hierarchy.
- [[AugmentedSBERT]] — the few-labels regime extension.
- [[TSDAE]] / [[SimCSE]] / [[ContrastiveTension]] / [[GPL]] — the no-labels regime alternatives.
- [[MNLI]] / [[STSB]] / [[GLUE]] — the data and evaluation.
- [[NilsReimers]] / [[IrynaGurevych]] / [[NandanThakur]] / [[KexinWang]] / [[TianyuGao]] — the authors of the methods Ch 10 walks.


## From [[hands-on-llm-ch11-fine-tuning-representation-models|*Hands-On LLMs* Ch 11]]

Ch 11 uses contrastive learning as **the data-generation step inside [[SetFit]]** — a way to bootstrap from a few labeled examples into a much larger labeled-pair dataset for fine-tuning a [[SentenceTransformers|SentenceTransformer]].

Per Ch 11, SetFit Step 1: *"Based on in-class and out-class selection of labeled data it generates positive (similar) and negative (dissimilar) pairs of sentences."*

The combinatorial blow-up: 16 same-class sentences → `16 * (16-1) / 2 = 120` positive pairs. With `num_iterations=20` (default), 32 labeled sentences (16/class × 2 classes) generate 1,280 contrastive pairs (20 × 32 × 2 [positive + negative]).

Ch 11's contrastive-fine-tuning step **directly inherits Ch 10's machinery**: the same [[SentenceTransformers]] training loop, the same loss families. The conceptual contribution Ch 11 adds is that **a labeled classification dataset can be *converted* into a contrastive-learning dataset** by treating same-class pairs as positives and cross-class pairs as negatives — generalizing the [[NLI]]-as-contrastive-data trick from Ch 10 to any classification task with a finite label set.
