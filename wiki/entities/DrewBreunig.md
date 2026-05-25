---
title: "Drew Breunig"
type: entity
tags: [person, blogger, practitioner, dspy, llm]
sources: [dbreunig-pipelines-prompt-optimization-dspy]
last_updated: 2026-05-24
---

# Drew Breunig

**Drew Breunig** is a writer and engineer who blogs at [dbreunig.com](https://www.dbreunig.com/) on AI, LLM tooling, mapping, and weather. The wiki's first **third-party (non-Stanford, non-academic) DSPy practitioner voice** — Breunig adopted [[DSPy]] while building a small agent for his weather-forecasting website and has documented a practical end-to-end run of [[MIPROv2|`dspy.MIPROv2`]] on a local-Ollama stack.

## Connections

- [[dbreunig-pipelines-prompt-optimization-dspy]] — *Pipelines & Prompt Optimization with DSPy* (2024-12-12), a hands-on third-party tutorial walking through [[DSPy]] [[DSPySignatures|Signatures]], [[DSPyPredict|`dspy.Predict`]], and [[MIPROv2|`dspy.MIPROv2`]] for a Wikipedia-sourced historic-event classification task. Lifts [[Llama|Llama 3.2 1b]] from **51.9% → 63.0%** with `auto="light"` in 0-shot mode; also runs a two-model variant (`prompt_model=Llama 3.3, task_model=Llama 3.2 1b`) that trades a little numerical accuracy for less overfitting.
- [[DSPy]] — framework Breunig adopted.
- [[MIPROv2]] — optimizer Breunig's tutorial uses; the post is the wiki's first source for the `prompt_model=` / `task_model=` kwarg split.
- [[Ollama]] — local runtime Breunig's stack runs on.
- [[Llama]] — both task LM and prompt-proposer in the tutorial are Llama 3.x via Ollama.
