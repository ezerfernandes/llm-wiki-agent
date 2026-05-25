---
title: "Vicuna-13B"
type: concept
tags: [llm, open-weight, llama-derivative, instruction-tuned]
sources: [2408.08849-ecg-chat]
last_updated: 2026-05-22
---

# Vicuna-13B

**Zheng, Chiang, Sheng, Zhuang, Wu, Zhuang, Lin, Li, Xing, Zhang, Gonzalez & Stoica (UC Berkeley / CMU / Stanford / UCSD / MBZUAI, 2024) — *"Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena."*** Open-weight chat model fine-tuned from LLaMA on user-shared ChatGPT conversations. The 13B variant is the standard mid-size open-weight LLM for academic vision-language adapters: it is the LLM backbone of [[LLaVA15|LLaVA-v1.5]], which [[2408.08849-ecg-chat|ECG-Chat]] follows directly for the signal-language adapter pattern.

## Used in [[2408.08849-ecg-chat]]

ECG-Chat's two-stage training freezes the [[ECGEncoder]] and trains:
1. **Feature alignment** (1 epoch): projector (2-layer MLP) only, LLM frozen.
2. **Instruction tuning** (3 epochs): projector + Vicuna-13B under [[lora]]; AdamW + cosine LR; [[ZeRO]] memory optimization on 8×V100 32GB GPUs.

Vicuna-13B was chosen for parity with [[LLaVA15]]'s architecture — the paper's adapter pattern is *"resembles LLaVA-v1.5"* — making this the wiki's first record of a Vicuna-based vision-language extension applied to a **physiological-signal** modality.

## Connections
- [[2408.08849-ecg-chat]] — the LLM backbone for ECG report generation under LoRA tuning.
- [[LLaVA15]] — the visual-multimodal precedent ECG-Chat directly mirrors.
- [[lora]] — the parameter-efficient fine-tuning method used to specialize Vicuna for ECG.
- [[ZeRO]] — memory optimizer enabling 13B + ECG encoder + projector training on V100s.
- [[LLMAsAJudge]] — Vicuna's original evaluation contribution (MT-Bench).
