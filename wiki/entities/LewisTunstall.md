---
title: "Lewis Tunstall"
type: entity
tags: [person, researcher, huggingface]
sources: [ai-engineering-ch04-evaluate-ai-systems, hands-on-llm-ch11-fine-tuning-representation-models]
last_updated: 2026-05-23
---

# Lewis Tunstall

Researcher at [[HuggingFace]]. Cited in [[ai-engineering-ch04-evaluate-ai-systems|*AI Engineering* Ch 4]] as the source of the benchmark-selection rationale for the [[OpenLLMLeaderboard|Open LLM Leaderboard]]:

> "When I posted a question on Hugging Face's Discord about why they chose certain benchmarks, Lewis Tunstall responded that they were guided by the benchmarks that the then popular models used."

## Significance

The "guided by what popular models used" rationale is itself an **interesting data point on leaderboard self-perpetuation** — popular models are evaluated on benchmarks → those benchmarks become the leaderboard → leaderboard rankings drive what's "popular" next.

## Connections

- [[ai-engineering-ch04-evaluate-ai-systems]] — primary source.
- [[HuggingFace]] — employer.
- [[OpenLLMLeaderboard]] — benchmark-selection process he explained.

## From [[hands-on-llm-ch11-fine-tuning-representation-models|*Hands-On LLMs* Ch 11]]

Ch 11 cites Lewis Tunstall as the **first author of [[SetFit]]** — *"Efficient few-shot learning without prompts,"* arXiv:2209.11055 (2022). SetFit is Ch 11's recommended approach for **few-shot text classification** — three-step pipeline (in-class/out-class sentence-pair sampling → [[ContrastiveLearning|contrastive]] [[SentenceTransformers|SentenceTransformer]] fine-tuning → classifier head). Ch 11's worked example demonstrates 32 labeled examples → F1 = 0.85 on Rotten Tomatoes — matching the F1 from training on the full 8,500-example dataset.

Tunstall is also a co-author of the *Natural Language Processing with Transformers* O'Reilly book (with Leandro von Werra and Thomas Wolf) and a regular contributor to Hugging Face's open-source NLP tooling.
