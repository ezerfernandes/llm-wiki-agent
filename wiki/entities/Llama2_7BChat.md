---
title: "llama-2-7b-chat"
type: entity
tags: [stub, llm, model, llama, meta, open-weights]
sources: [2407.10930-better-together]
last_updated: 2026-05-22
---

# llama-2-7b-chat

7B-parameter chat-tuned LM from [[meta|Meta]] (Touvron et al. 2023, *Llama 2: Open Foundation and Fine-Tuned Chat Models*). HuggingFace `meta-llama/Llama-2-7b-chat-hf`, Meta Llama 2 Community License. One of three LMs evaluated in [[2407.10930-better-together|Soylu, Potts & Khattab (2024)]]; the canonical "hard case" of the paper — vanilla zero-shot on Iris scores **0.0%**, so weight-first strategies (Θ-only, Θ→Θ, Θ→Π) have no bootstrap traces to fine-tune on. Prompt-first strategies fix this: Π → Θ → Π lifts Iris from 0.0 → 65.3.

## Connections
- [[2407.10930-better-together]]
- [[BetterTogether]]
- [[meta]]
