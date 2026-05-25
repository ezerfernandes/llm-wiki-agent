---
title: "MedVAL-4B"
type: concept
tags: [model, open-source, distilled, qwen, medical-nlp, validator]
sources: [2507.03152-medval]
last_updated: 2026-05-22
---

# MedVAL-4B

The **best-performing open-source distilled validator** released with [[2507.03152-medval|MedVAL (Aali et al. 2026)]]. Built by applying the [[MedVAL]] three-stage pipeline ([[BootstrapFinetune|`dspy.BootstrapFinetune`]] + [[QLoRA]]) to a **[[qwen|Qwen3-4B]]** base model, with GPT-4o as the synthetic data curator.

## Headline performance

- **4-class F1 = 0.527** on [[MedVALBench]] — highest of all open-source LMs tested.
- **Exceeds zero-shot baselines** of much larger / proprietary models:
  - GPT-4o Mini (0.474), Gemini 2.0 Flash (0.515), MedGemma-27B (0.482), Llama-3.3-70B (0.480), Gemma3-27B (0.459), Llama-3.1-8B (0.259), Llama-3.2-3B (0.128).
- **Binary safety F1 = 0.823, accuracy = 0.800** — exceeds Llama-3.2-3B / Llama-3.1-8B MedVAL versions; close to GPT-4o Mini MedVAL (0.855 F1).
- **Ensemble (Llama-3.2-3B + Llama-3.1-8B + Qwen3-4B) MedVAL** = 0.837 F1 / 0.805 accuracy — best open-source-only configuration.

## Why a 4B model is the right shape

> *"Improving small/open models is directly relevant for real-world deployment as hospital systems face barriers to using proprietary APIs at scale. In agentic workflows, validation is a high-frequency step (per section, per note, per agent action), so efficient models are a practical path for routine validation, with frontier models reserved for escalations."* — [[2507.03152-medval]] §4.

Trained on a single **NVIDIA A6000** GPU using 4-bit quantization via `BitsAndBytesConfig`, 5 epochs, batch size 1, Adam lr $1\times 10^{-5}$ linear decay — easily reproducible on consumer-grade hardware.

## Release

- **HuggingFace model**: [stanfordmimi/MedVAL-4B](https://huggingface.co/stanfordmimi/MedVAL-4B)
- **Demo space**: [stanfordmimi/MedVAL](https://huggingface.co/stanfordmimi/MedVAL)
- License governed by the underlying [[qwen|Qwen3]] base license + the Stanford MIMI release terms.

## Connections

- [[2507.03152-medval]] — the paper.
- [[MedVAL]] — the distillation method that trained this model.
- [[MedVALBench]] — the benchmark it tops in the open-source category.
- [[qwen|Qwen3-4B]] — the base model.
- [[QLoRA]] — the PEFT method used for training.
- [[StanfordMIMI]] — the lab that releases the artifacts.
- [[BootstrapFinetune]] — the DSPy weight-tuning optimizer that drives the training loop.
- [[LLMAsAJudge]] — the validation paradigm the model instantiates.
