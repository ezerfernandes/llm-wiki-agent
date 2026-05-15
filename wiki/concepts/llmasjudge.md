---
title: "LLM-as-Judge"
type: concept
tags: [ml-method]
sources: [2601.21343-self-improving-pretraining, 2605.03808-agentic-imodels]
last_updated: 2026-05-10
---

# LLM-as-Judge

Pattern in which a (typically stronger) LLM scores or compares the outputs of another model. Self-Improving Pretraining elevates this to the pretraining stage by using a post-trained model to judge rollouts vs original / rewritten suffixes; AGENTIC-IMODELS uses LLM-graded simulatability as the interpretability metric for evolved models.

## Connections
- [[2601.21343-self-improving-pretraining]]
- [[2605.03808-agentic-imodels]]
- [[simulatability|Simulatability]]
