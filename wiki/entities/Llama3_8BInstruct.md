---
title: "llama-3-8b-instruct"
type: entity
tags: [stub, llm, model, llama, meta, open-weights]
sources: [2407.10930-better-together]
last_updated: 2026-05-22
---

# llama-3-8b-instruct

8B-parameter instruction-tuned LM from [[meta|Meta]] (MetaAI 2024, *Meta Llama 3*). HuggingFace `meta-llama/Meta-Llama-3-8B-Instruct`, Meta Llama 3 Community License. The strongest baseline of the three LMs in [[2407.10930-better-together|Soylu, Potts & Khattab (2024)]] — vanilla zero-shot already hits 31.6 / 72.7 / 48.0 on HotPotQA / GSM8K / Iris. **The lone (dataset, LM) cell where prompts-only beats BetterTogether** is HotPotQA-llama-3 (Π only = 46.9 vs Π → Θ → Π = 46.7), suggesting that for the strongest base LM the marginal value of the weight step shrinks.

## Connections
- [[2407.10930-better-together]]
- [[BetterTogether]]
- [[meta]]
