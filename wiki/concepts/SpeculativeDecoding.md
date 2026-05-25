---
title: "Speculative Decoding"
type: concept
tags: [llm-engineering, inference, decoding]
sources: [leh-ch08-inference-optimization, ai-engineering-ch09-inference-optimization]
last_updated: 2024-12-04
---

## Definition
Inference acceleration where a small draft model proposes multiple tokens and the target model verifies them in one forward pass.

## In LLM Engineer's Handbook
Speculative decoding (Leviathan, Kalman, Matias, 2023) accelerates inference by having a small draft model propose k candidate tokens, which the large target model validates in one forward pass, keeping the longest matching prefix. Per [[leh-ch08-inference-optimization]] ~90% acceptance can deliver 3-4x speedup. Constraint: draft and target must share the tokenizer. Variants: [[PromptLookupDecoding]] (draft tokens are prompt n-grams) and [[Medusa]] (fine-tuned speculation heads). Supported by [[TGI]].

## From [[ai-engineering-ch09-inference-optimization|AI Engineering Ch 9]]

### The algorithm (made explicit)

Given input tokens `x₁, x₂, …, xₜ`:

1. Draft model generates K tokens: `xₜ₊₁, xₜ₊₂, …, xₜ₊ₖ`.
2. Target model verifies all K tokens **in parallel**.
3. Target model accepts the longest left-to-right prefix it agrees with.
4. After accepting j tokens, target model generates one extra: `xₜ₊ⱼ₊₁`.
5. Loop with the new prefix.

Worst case (no acceptance): one token from the target model.
Best case (all K accepted): **K + 1 tokens** in one round.

### Why it works — three insights from Ch 9

> 1. **Verification is parallelizable; generation is sequential.** "Speculative decoding effectively turns the computation profile of decoding into that of prefilling."
> 2. **Some tokens are easier to predict than others.** A weaker draft model can hit a high acceptance rate on easy tokens.
> 3. **Decode is memory-bandwidth-bound — there are idle FLOPs available for free verification.**

### Chinchilla-70B numbers

DeepMind (Chen et al. 2023) trained a **4B-parameter draft model** of the same architecture for Chinchilla-70B:
- Draft generates **8× faster than target** (1.8 ms/token vs 14.1 ms/token).
- **Overall response latency cut > 50%** with no quality loss.

Similar speedup achieved for T5-XXL (Laviathan et al. 2022).

### Implementation cost

> *"It's possible to do so in 50 lines of code in PyTorch. It's been incorporated into popular inference frameworks such as vLLM, TensorRT-LLM, and llama.cpp."*

### Caveat: doesn't help if you're already maxed out

> *"This also means that if your MFU is already maxed out, speculative decoding makes less sense."* — Ch 9 footnote

The idle-FLOPs assumption breaks down at high [[MFU]] — there's no free compute to use for verification.

### Acceptance-rate dependencies

- **Domain matters** — code (structured) has higher acceptance than free-form prose.
- **Larger K** = fewer verifying calls, but lower acceptance rate.
- **Same vocabulary/tokenizer required** between draft and target.

### Family relationships

- **[[InferenceWithReference]]** — draft tokens from input context instead of draft model.
- **[[PromptLookupDecoding]]** — draft from prompt n-grams.
- **[[MedusaDecoding|Medusa]]** — multiple decoding heads (parallel decoding family, not strictly speculative).
- **[[LookaheadDecoding]]** — same decoder generates K parallel tokens (Jacobi verification).
