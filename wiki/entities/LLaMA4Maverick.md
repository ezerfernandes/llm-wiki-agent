---
title: "LLaMA-4 Maverick"
type: entity
tags: [model, llm, open-weights, llama, meta]
sources: [2603.19247-prompt-optimization-jailbreaking]
last_updated: 2026-05-22
---

# LLaMA-4 Maverick

Open-weights LLM from [[meta|Meta]]. HuggingFace: `meta-llama/Llama-4-Maverick-17B-128E-Instruct`. Mixture-of-experts; 17B active params over 128 experts (per the cited HF URL).

## In this wiki

- [[2603.19247-prompt-optimization-jailbreaking]] — one of four target models. **Baseline danger 0.215 → SIMBA-optimized danger 0.623** (3× rise); [[MIPROv2]] reaches **0.581** (within 0.04 of SIMBA), making LLaMA-4 Maverick the cell where MIPROv2 most narrowly trails SIMBA. The qualitative case study shows a "medical exploitation" prompt category — baseline refusal → SIMBA-optimized list of financial-exploitation tactics.

## Connections

- [[meta]] — developer.
- [[Llama2_7BChat]] / [[Llama3_8BInstruct]] — earlier LLaMA-family open-weights models in the wiki.
- [[2603.19247-prompt-optimization-jailbreaking]] — paper using it.
- [[Jailbreak]] / [[AdversarialPromptSearch]] — vulnerability profile.
