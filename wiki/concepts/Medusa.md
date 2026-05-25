---
title: "Medusa"
type: concept
tags: [llm-engineering, inference, decoding, parallel-decoding]
sources: [leh-ch08-inference-optimization, ai-engineering-ch09-inference-optimization]
last_updated: 2024-12-04
---

## Definition
Speculative decoding via fine-tuned speculation heads attached to the target model.

## In LLM Engineer's Handbook
Medusa (Cai, Li, Geng, Peng, Lee, Chen, Dao, 2024, *Medusa: Simple LLM Inference Acceleration Framework with Multiple Decoding Heads*) attaches additional speculation heads directly to the target model instead of using a separate draft model. Medusa-1 fine-tunes only the speculation heads; Medusa-2 jointly fine-tunes heads + base. Per [[leh-ch08-inference-optimization]] natively supported by [[TGI]].

## From [[ai-engineering-ch09-inference-optimization|AI Engineering Ch 9]]

Ch 9 places Medusa in the **[[ParallelDecoding|parallel-decoding]] family** (distinct from speculative decoding) — both attack the autoregressive decoding bottleneck but with different verification mechanisms.

### Architecture

> *"In Medusa, the original model is extended with multiple decoding heads, and each head is a small neural network layer that is then trained to predict a future token at a specific position. If the original model is trained to predict the next token xₜ₊₁, the kth head will predict the token xₜ₊ₖ₊₁. These heads are trained together with the original model, but the original model is frozen."*

### Tree-based attention verification

Unlike [[LookaheadDecoding|Lookahead decoding's]] [[JacobiAlgorithm|Jacobi verification]], Medusa uses a **tree-based attention mechanism**:

> *"Each Medusa head produces several options for each position. These options are then organized into a tree-like structure to select the most promising combination."*

### Performance number

> *"NVIDIA claimed Medusa helped boost Llama 3.1 token generation by up to 1.9× on their HGX H200 GPUs (Eassa et al., 2024)."*

### Implementation difficulty

> *"Parallel decoding is not intuitive, and some techniques, like Medusa, can be challenging to implement."*

See [[MedusaDecoding]] for the Ch 9-specific deep-dive treatment.
