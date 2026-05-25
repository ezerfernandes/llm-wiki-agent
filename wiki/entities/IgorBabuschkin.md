---
title: "Igor Babuschkin"
type: entity
tags: [person, xai, researcher, grok]
sources: [ai-engineering-ch02-foundation-models]
last_updated: 2024-12-04
---

# Igor Babuschkin

Core developer behind **Grok** (xAI's LLM). Cited in [[ai-engineering-ch02-foundation-models|*AI Engineering* Ch 2]] for one comment that captures a key [[ScalingBottlenecks|scaling-bottleneck]] worry:

## The Grok / ChatGPT incident (December 2023)

> "In December 2023, Grok, a model trained by X, was caught refusing a request by saying that it goes against OpenAI's use case policy. This caused some people to speculate that Grok was trained using ChatGPT outputs. Igor Babuschkin, a core developer behind Grok, responded that it was because **Grok was trained on web data, and 'the web is full of [[ChatGPT|ChatGPT]] outputs.'**"

## Why this matters in the wiki

Babuschkin's quote is one of the clearest practitioner acknowledgments of **AI-generated content polluting future training data**:

- The web is being rapidly populated with [[ChatGPT|ChatGPT]] outputs.
- New models trained on web data are partially trained on AI-generated data.
- Whether this degrades models recursively (Shumailov et al. 2023 — "model collapse") is an active research question Ch 8 of the book engages.

This is one component of the chapter's broader [[ScalingBottlenecks|scaling-bottlenecks]] argument on the data side.

## Connections
- [[ScalingBottlenecks]] — the bottleneck Babuschkin's comment illustrates.
- [[ChatGPT]] — the model whose outputs are polluting training data.
- [[ai-engineering-ch02-foundation-models]] — primary source.
