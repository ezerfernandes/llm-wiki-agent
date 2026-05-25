---
title: "Usefulness Threshold"
type: concept
tags: [planning, metrics, evaluation, ai-engineering]
sources: [ai-engineering-ch01-intro]
last_updated: 2024-12-04
---

# Usefulness Threshold

**The metric bar an AI product has to clear before it can be put in front of customers.** Per [[ai-engineering-ch01-intro|*AI Engineering* Ch 1]], the usefulness threshold is the cross-functional output of *use-case evaluation* — it converts "we want to build this" into "we'll ship it when these numbers reach these values."

## Four metric groups

1. **Quality metrics** — how good the model's responses are. Task-specific (accuracy, F1, BLEU, [[SemanticF1]], LLM-as-judge scores, etc.).

2. **Latency metrics**:
   - **[[TTFT]]** — time to first token.
   - **[[TPOT]]** — time per output token.
   - **Total latency**.
   - Acceptable latency depends on the use case. Huyen's heuristic: *"if all of your customer requests are currently being processed by humans with a median response time of an hour, anything faster than this might be good enough."*

3. **Cost metrics** — how much it costs per inference request.

4. **Other** — interpretability, fairness, and other domain-specific bars.

## Business-metric coupling

Above the usefulness threshold sits the **business metric** — *"how this will impact your business."* For a customer-support chatbot, examples:

- % of customer messages the chatbot can automate.
- Throughput multiplier (how many more messages can be processed).
- Response-time reduction.
- Labor savings.
- Customer satisfaction (the easy-to-forget metric — *"A chatbot can answer more messages, but that doesn't mean it'll make users happy"*).

The usefulness threshold serves the business metric — quality / latency / cost bars are tuned so that the business metric improves.

## Connections

- [[UseCaseEvaluation]] — parent planning framework.
- [[Evaluation]] — discipline-level home; Chs 3–4 of the book.
- [[InferenceOptimization]] — latency + cost metrics are what inference optimization moves.
- [[TTFT]] / [[TPOT]] — specific latency metrics.
- [[LastMileChallenge]] — the slowdown that hits when you're trying to push usefulness from 80% to 95%.
- [[ai-engineering-ch01-intro]] — primary source.
