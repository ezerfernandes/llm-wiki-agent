---
title: "Alpaca Format"
type: concept
tags: [llm-engineering]
sources: [leh-ch05-supervised-fine-tuning, leh-ch06-preference-alignment]
last_updated: 2026-05-22
---

## Definition
Single-turn instruction-data storage format (and matching minimalist chat template) introduced by Stanford Alpaca.

## In LLM Engineer's Handbook
Named after the Stanford Alpaca dataset (Tahori et al. 2023). Both an instruction-storage format (JSONL with `{instruction, input (optional), output}` keys) and a minimalist [[ChatTemplate|chat template]] (`### Instruction:`, `### Response:`, `<EOS>`). Single-turn only — multi-turn uses [[ChatML]] or OpenAI format. [[leh-ch05-supervised-fine-tuning]] uses Alpaca for the Llama-3.1-8B fine-tune because it needs no additional special tokens (slightly worse performance than ChatML).
