---
title: "Global Factual Consistency"
type: concept
tags: [evaluation, factuality, hallucination]
sources: [ai-engineering-ch04-evaluate-ai-systems]
last_updated: 2024-12-04
---

# Global Factual Consistency

One of two settings for [[FactualConsistency|factual consistency]] per [[ai-engineering-ch04-evaluate-ai-systems|*AI Engineering* Ch 4]]. **The output is evaluated against open knowledge.** *"If the model outputs 'the sky is blue' and it's a commonly accepted fact that the sky is blue, this statement is considered factually correct."*

## Use cases

- General chatbots.
- Fact-checking applications.
- Market research.
- Tasks with broad scopes where no specific context is provided.

## The hard part: identifying facts

> "Often, the hardest part of factual consistency verification is determining what the facts are. Whether any of the following statements can be considered factual depends on what sources you trust: 'Messi is the best soccer player in the world', 'climate change is one of the most pressing crises of our time', 'breakfast is the most important meal of the day'."

Two failure modes Huyen flags:
- **Internet noise** — false marketing claims, statistics made up for political agendas, sensational social-media posts.
- **Absence-of-evidence fallacy** — *"One might take the statement 'there's no link between X and Y' as factually correct because of a failure to find the evidence that supported the link."*

## What evidence AI models find convincing

Wan et al. 2024 finding cited by Ch 4: *"models rely heavily on the relevance of a website to the query, while largely ignoring stylistic features that humans find important such as whether a text contains scientific references or is written with a neutral tone."* Open research question.

## Detection methods

For global, the dominant approach is [[SAFEEvaluator|search-augmented verification]] (DeepMind 2024): decompose response → revise → fact-check queries → search → verify. *"You'll have to first search for reliable sources, derive facts, and then validate the statement against these facts."*

## Benchmark

[[TruthfulQA]] is the canonical global-factual-consistency benchmark — 817 questions across 38 categories targeting common human misconceptions.

## Connections

- [[ai-engineering-ch04-evaluate-ai-systems]] — primary source.
- [[FactualConsistency]] — parent.
- [[LocalFactualConsistency]] — sibling setting (easier).
- [[SAFEEvaluator]] — the dominant detection method.
- [[TruthfulQA]] — canonical benchmark.
