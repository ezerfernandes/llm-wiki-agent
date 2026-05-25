---
title: "GLUE (General Language Understanding Evaluation)"
type: concept
tags: [benchmark, nlp, evaluation, dataset]
sources: [hands-on-llm-ch10-creating-text-embedding-models, hands-on-llm-ch12-fine-tuning-generation-models]
last_updated: 2026-05-24
---

# GLUE (General Language Understanding Evaluation)

**GLUE** — the **General Language Understanding Evaluation** benchmark, a suite of nine English language-understanding tasks introduced by Wang, Singh, Michael, Hill, Levy & Bowman 2018 (*"GLUE: A Multi-Task Benchmark and Analysis Platform for Natural Language Understanding,"* ICLR Workshop / EMNLP).

Per [[hands-on-llm-ch10-creating-text-embedding-models|*Hands-On LLMs* Ch 10]]: *"This GLUE benchmark consists of nine language understanding tasks to evaluate and analyze model performance."*

## The nine tasks

| Task | Type | Description |
|---|---|---|
| **CoLA** | single-sentence | Grammatical acceptability |
| **SST-2** | single-sentence | Sentiment (Stanford Sentiment Treebank) |
| **MRPC** | sentence-pair | Paraphrase (Microsoft Research Paraphrase Corpus) |
| **QQP** | sentence-pair | Question paraphrase (Quora Question Pairs) |
| **[[STSB\|STS-B]]** | sentence-pair (regression) | Semantic textual similarity |
| **[[MNLI\|MNLI]]** | sentence-pair | Multi-genre NLI |
| **QNLI** | sentence-pair | Question-answer NLI (from SQuAD) |
| **RTE** | sentence-pair | Recognizing textual entailment |
| **WNLI** | sentence-pair | Winograd schemas as NLI |

## Use in Ch 10

Ch 10 uses **two GLUE tasks**:

- **[[MNLI]]** — as the training data source (50,000-pair subset for the loss-function ladder).
- **[[STSB|STS-B]]** — as the evaluator (Pearson cosine on the validation split, label rescaled to `[0,1]`).

The chapter loads both via Hugging Face Datasets:

```python
from datasets import load_dataset
train_dataset = load_dataset("glue", "mnli", split="train").select(range(50_000))
val_sts = load_dataset("glue", "stsb", split="validation")
```

## Position in the wiki

GLUE is the canonical pre-MTEB benchmark for sentence-pair / NLI tasks. SuperGLUE (Wang et al. 2019) is the harder follow-up. For modern embedding-model evaluation, [[MTEB]] has largely replaced GLUE — MTEB covers more tasks (58 datasets vs 9), more languages (112 vs English-only), and more embedding-specific scoring (clustering, retrieval, reranking). But GLUE remains the **standard source of NLI training data** (MNLI) and the **standard quick-eval for STS** (STS-B).

## Connections

- [[MNLI]] / [[STSB]] — the two GLUE tasks Ch 10 uses.
- [[SNLI]] — the single-genre NLI predecessor (not part of GLUE).
- [[NaturalLanguageInference]] — the task family.
- [[SemanticTextualSimilarity]] — the task family STS-B belongs to.
- [[MTEB]] — the modern embedding-evaluation successor.
- [[SamuelBowman]] — GLUE co-author.
- [[hands-on-llm-ch10-creating-text-embedding-models]] — primary source.

## From [[hands-on-llm-ch12-fine-tuning-generation-models|Hands-On LLMs Ch 12]]

Ch 12 of *Hands-On LLMs* names GLUE in **Table 12-1** as one of six canonical public benchmarks for evaluating generative LLMs (alongside [[MMLU]], [[GSM8K]], [[TruthfulQA]], [[HellaSwag]], [[HumanEval]]) — *"language understanding (multi-task)."*

Ch 12 also surfaces GLUE in the **[[adapterlayers|Houlsby et al. 2019]] PEFT result** that anchors the chapter's adapter framing: fine-tuning **3.6% of BERT's parameters** with adapter layers reaches within **0.4% of full fine-tuning on GLUE** — the empirical motivator for the entire PEFT family Ch 12 walks ([[lora|LoRA]] / [[QLoRA]]).
