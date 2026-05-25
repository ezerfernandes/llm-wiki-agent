---
title: "Dynamic or Static"
type: concept
tags: [planning, ux, apple, ai-engineering, personalization]
sources: [ai-engineering-ch01-intro]
last_updated: 2024-12-04
---

# Dynamic or Static

**One of [[Apple|Apple's]] three axes for classifying the role of AI in a product**, surfaced in [[ai-engineering-ch01-intro|*AI Engineering* Ch 1]]. Asks: *does the AI update continually with user feedback, or only periodically with software updates?*

## The axis

- **Dynamic**: AI is updated continually based on per-user feedback. **Example**: Face ID — adapts as faces change over time. ChatGPT's *memory feature* — remembers each user's preferences.
- **Static**: AI is updated periodically. **Example**: object detection in Google Photos — only changes when Google Photos itself is upgraded.

## Engineering implication

Dynamic features imply either:
1. **Per-user finetuned models** — every user has their own model, continually adjusted with their data.
2. **Other personalization mechanisms** — context-window memory (e.g., ChatGPT's memory), retrieval-augmented personalization, per-user prompt templates.

This is a much higher engineering surface than static features, which can be served from a single shared model checkpoint.

## Where this sits

One of three role axes; the others are:
- **[[CriticalOrComplementary]]** — does the app still work without AI?
- **[[ReactiveOrProactive]]** — does AI respond to requests or surface insights?

## Connections

- [[Apple]] — framework source.
- [[CriticalOrComplementary]] / [[ReactiveOrProactive]] — companion axes.
- [[UseCaseEvaluation]] — parent planning framework.
- [[FineTuning]] — per-user finetuning is one realization of dynamic.
- [[rag]] — retrieval-augmented memory is another realization.
- [[ai-engineering-ch01-intro]] — primary source.
