---
title: "TIFIN"
type: entity
tags: [company, fintech, ai-application]
sources: [ai-engineering-ch02-foundation-models]
last_updated: 2024-12-04
---

# TIFIN

US-based AI-in-finance company. Surfaced in the wiki via [[ai-engineering-ch02-foundation-models|*AI Engineering* Ch 2]] as the source of a clever **latency-hedging pattern for chain-of-thought queries**.

## The Ch 2 anecdote

> "Kittipat Kampa, head of AI at TIFIN, told me that his team asks their model to generate multiple responses in parallel and show the user the first response that is completed and valid."

This is **[[TestTimeCompute|test-time compute]] as a latency hedge** — generate N candidates in parallel, but instead of waiting for all of them and selecting, return the first one that finishes and validates. Particularly useful for slow CoT queries where a single chain might take a long time.

## Connections
- [[KittipatKampa]] — head of AI at TIFIN; source of the anecdote.
- [[TestTimeCompute]] — the broader pattern.
- [[bestofn]] — the close cousin (first-valid instead of best-of-N).
- [[ai-engineering-ch02-foundation-models]] — primary source.
