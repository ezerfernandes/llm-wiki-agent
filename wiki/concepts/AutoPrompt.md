---
title: "AutoPrompt"
type: concept
tags: [prompt-tuning, gradient-based]
sources: [2406.11695-mipro]
last_updated: 2026-05-22
---

# AutoPrompt

Shin et al. (EMNLP 2020, arXiv:2010.15980). Gradient-based discrete prompt search — selects prompt tokens by maximizing a gradient-derived saliency objective.

[[2406.11695-mipro|MIPRO]] cites AutoPrompt alongside [[PrefixTuning|Prefix Tuning]] as a **gradient-based prompt-tuning** method excluded from the LM-program setting because it requires gradient / log-prob access that modern API-only LMs no longer expose.

## Connections

- [[PromptOptimization]] — parent task.
- [[PrefixTuning]] — sibling gradient-based method.
- [[2406.11695-mipro|MIPRO]] — the wiki's reference paper that excludes this method class.
