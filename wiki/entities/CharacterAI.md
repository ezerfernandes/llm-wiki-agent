---
title: "Character.AI"
type: entity
tags: [company, llm, training, int8, inference]
sources: [ai-engineering-ch07-finetuning, ai-engineering-ch09-inference-optimization]
last_updated: 2024-12-04
---

# Character.AI

LLM-powered consumer AI company (founded 2021 by Noam Shazeer and Daniel De Freitas). Cited in [[ai-engineering-ch07-finetuning|*AI Engineering* Ch 7]] for an unusual technical claim: **training their models entirely in [[INT8]]**.

> "Character.AI (2024) shared that they were able to train their models entirely in INT8, which helped eliminate the training/serving precision mismatch while also significantly improving training efficiency. However, training in lower precision is harder to do, as backpropagation is more sensitive to lower precision." — Ch 7

## Why this is notable

- **Most teams use [[INT8]] only for inference**, not training. Backprop is more precision-sensitive than forward passes.
- Character.AI trained natively in INT8 — eliminating the train/serve precision mismatch (where models trained in FP16/BF16 lose quality when deployed in INT8).
- **Significant training-efficiency win**: lower precision = more parallel compute per cycle + smaller memory footprint = bigger batches + faster training.

## Larger context

In August 2024, [[google|Google]] paid roughly $2.7B to license Character.AI's technology and hire its leadership team (Noam Shazeer is now a Gemini co-lead). The INT8 training infrastructure is one of the technical assets that made the deal valuable.

## Connections

- [[INT8]] / [[Quantization]] / [[MixedPrecisionTraining]] — the techniques involved.
- [[FineTuning]] / [[Pretraining]] — the operations Character.AI did in INT8.
- [[ai-engineering-ch07-finetuning]] — wiki source.

## From [[ai-engineering-ch09-inference-optimization|AI Engineering Ch 9]]

Ch 9 cites Character.AI for the **most-quoted KV-cache reduction case study** in the chapter:

### The 180-message dialogue history

> *"Character.AI, an AI chatbot application, shares that their average conversation has a dialogue history of 180 messages (2024). Given the typically long sequences, the primary bottleneck for inference throughput is the KV cache size."*

### The > 20× KV-cache reduction stack

Three stacked attention-mechanism redesigns:

1. **[[multiqueryattention|Multi-query attention]]** (head-side K/V sharing).
2. **Interleaved local + global attention** ([[LocalAttention]]).
3. **[[CrossLayerAttention|Cross-layer attention]]** (layer-side K/V sharing).

> *"Three attention mechanism designs ... help them reduce KV cache by over 20 times. More importantly, this significant KV cache reduction means that memory is no longer a bottleneck for them for serving large batch sizes."* — Ch 9

This combination is now a canonical template for any team facing KV-cache memory pressure at long-context dialogue serving.

### Composing with INT8 training

Character.AI's INT8-end-to-end training (Ch 7) and KV-cache-reduction-stack (Ch 9) are **complementary**: training in INT8 cuts memory & bandwidth per parameter; KV-cache redesigns cut the per-token state size. The combined effect is what makes their massive concurrent-user serving economically viable.
