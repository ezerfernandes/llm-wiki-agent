---
title: "Local / Sparse Attention"
type: concept
tags: [attention, efficiency, long-context]
sources: [hands-on-llm-ch03-looking-inside-llms, ai-engineering-ch09-inference-optimization]
last_updated: 2024-12-04
---

# Local / Sparse Attention

An efficient-attention family that **limits the previous tokens each position can attend to** — instead of full quadratic attention over all prior positions. Introduced for long-context efficiency as Transformers grew in size; primary citations from [[hands-on-llm-ch03-looking-inside-llms|*Hands-On LLMs* Ch 3]]:

- **Sparse attention** — *"Generating long sequences with sparse transformers"* (Child et al.). Used by [[GPT3|GPT-3]].
- **Sliding window attention** — *"Longformer: The long-document transformer"* (Beltagy et al.). See [[SlidingWindowAttention]].

## The GPT-3 interleaved recipe

> "One model that incorporates such a mechanism is GPT-3. But it does not use that for all the Transformer blocks — the quality of the generation would vastly degrade if the model could only see a small number of previous tokens. The GPT-3 architecture interweaved full-attention and efficient-attention Transformer blocks. So the Transformer blocks alternate between full attention (e.g., blocks 1 and 3) and sparse attention (e.g., blocks 2 and 4)." — Ch 3

The interleave pattern preserves the model's ability to access long-range context (through the full-attention blocks) while saving compute on the alternating sparse blocks.

## Trade-off

- **Saves**: attention compute scales sub-quadratically in sequence length.
- **Costs**: each sparse-attention block sees only a window of prior tokens; quality degrades if used everywhere; full-attention interleaving recovers quality.

## See also

- [[SlidingWindowAttention]] — the Longformer variant.
- [[FlashAttention]] — the orthogonal IO-side optimization.
- [[multiqueryattention]] / [[GroupedQueryAttention]] — head-side attention optimizations.
- [[selfattention]] / [[multiheadattention]] — the base attention this family modifies.
- [[GPT3]] — the canonical deployment.
- [[hands-on-llm-ch03-looking-inside-llms|*Hands-On LLMs* Ch 3]] — primary source.

## From [[ai-engineering-ch09-inference-optimization|AI Engineering Ch 9]]

Ch 9 treats local windowed attention (Longformer, Beltagy et al. 2020) as one of four **attention-mechanism redesigns** that reduce [[KVCache|KV-cache]] memory.

### Cache-reduction math

> *"If the average sequence length is 10,000 tokens, attending to a window size of 1,000 tokens reduces the KV cache size by 10 times."* — Ch 9

→ A 10× cache reduction at window=1,000 vs avg-seq=10,000.

### Pairing with global attention

Ch 9 reiterates the interleave pattern:

> *"Local windowed attention can be interleaved with global attention, with local attention capturing nearby context; the global attention captures task-specific information across the document."*

This is the same recipe Ch 3 attributes to GPT-3 (alternating full/sparse blocks).

### CharacterAI's stack

[[CharacterAI]] (2024) — interleaved local + global attention is **one of three** techniques (with [[multiqueryattention|MQA]] and [[CrossLayerAttention|cross-layer attention]]) that cut their KV cache **> 20×**, removing memory as a bottleneck for large batches.
