---
title: "UltraFeedback"
type: concept
tags: [llm-engineering]
sources: [leh-ch05-supervised-fine-tuning]
last_updated: 2026-05-22
---

## Definition
Data augmentation that uses GPT-4 to critique and score model responses.

## In LLM Engineer's Handbook
UltraFeedback (OpenBMB) evolves answers rather than instructions: it samples a large pool of diverse instructions, generates many candidate responses from multiple models, then uses GPT-4 (or comparable) to produce detailed critiques and numerical scores along instruction-following / truthfulness / honesty / helpfulness. Per [[leh-ch05-supervised-fine-tuning]] the chosen/rejected pairs feed SFT (best-of-N) and preference-alignment ([[DirectPreferenceOptimization]] / [[rlhf]]).
