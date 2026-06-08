---
title: "KV Cache"
type: concept
tags: [llm-engineering, inference, attention]
sources: [leh-ch08-inference-optimization, hands-on-llm-ch03-looking-inside-llms, ai-engineering-ch09-inference-optimization, mlsysbook-ch06-network-architectures, mlsysbook-ch11-hardware-acceleration, mlsysbook-ch13-model-serving, mlsysbook-ch14-ml-operations]
last_updated: 2026-06-05
---

## Definition
Cache of key/value tensors from self-attention layers; central to efficient LLM decoding.

## In LLM Engineer's Handbook
The key-value cache stores per-layer K and V tensors produced by self-attention so each new decoded token only computes its own K and V rather than re-running attention over the entire prefix. Memory grows roughly as `tokens * layers * heads * head_dim * 2 bytes`. [[leh-ch08-inference-optimization]] distinguishes dynamic vs. [[StaticKVCache]] (compile-time-constant shape, enables [[TorchCompile]] for ~4x speedups); see also [[PagedAttention]] for paged variants.

## From [[hands-on-llm-ch03-looking-inside-llms|*Hands-On LLMs* Ch 3]]

Ch 3's intuition-first framing of the same mechanism:

> "If we give the model the ability to cache the results of the previous calculation (especially some of the specific vectors in the attention mechanism), we no longer need to repeat the calculations of the previous streams. This time the only needed calculation is for the last stream. This is an optimization technique called the keys and values (kv) cache and it provides a significant speedup of the generation process." — Ch 3

### Concrete wall-clock measurement

On a [[GoogleColab|Colab]] T4 GPU running [[Phi3Mini|Phi-3-mini]] (`microsoft/Phi-3-mini-4k-instruct`) generating 100 tokens:

| Config | Wall-clock |
|---|---|
| `use_cache=True` | **4.5 s** |
| `use_cache=False` | **21.8 s** |

A ~**5× speedup** purely from caching K/V projections across decode steps. This is the wiki's first concrete on-consumer-GPU KV-cache measurement to complement the formal memory-formula treatment from [[leh-ch08-inference-optimization|LEH Ch 8]].

### UX consequence

> "From a user experience standpoint, even the four-second generation time tends to be a long time to wait for a user that's staring at a screen and waiting for an output from the model. This is one reason why LLM APIs stream the output tokens as the model generates them instead of waiting for the entire generation to be completed." — Ch 3

In [[HuggingFace|Hugging Face]] Transformers, KV caching is **on by default** (`use_cache=True`).

## See also
- [[KeyProjection]] / [[ValueProjection]] — the projections whose outputs the cache stores.
- [[TokenStream]] — the per-position computation track the cache makes incremental.
- [[multiqueryattention]] / [[GroupedQueryAttention]] — head-side optimizations that **shrink** the cache.
- [[PagedAttention]] — the OS-paging-inspired memory layout for the cache.
- [[StaticKVCache]] — the pre-allocated variant enabling [[TorchCompile]] fusion.
- [[mlsysbook-ch06-network-architectures]] — frames the KV cache as the dominant memory consumer that makes [[Transformer]] inference *memory-bandwidth-bound*: it grows linearly $\mathcal{O}(N_L \cdot 2 \cdot N_{\text{heads}} \cdot S \cdot d_{\text{head}})$ (distinct from the $\mathcal{O}(S^2)$ training matrix); ~1 GB/request for a 32-layer/32-head/2048-token FP16 model — rivaling weight memory at modest concurrency, the final "Fallacies & Pitfalls" warning.

## From [[ai-engineering-ch09-inference-optimization|AI Engineering Ch 9]]

### The formula and the 54 GB / 3 TB numbers

Ch 9 gives the unoptimized KV-cache size formula:

```
KV-cache memory = 2 × B × S × L × H × M
```

- B = batch size
- S = sequence length
- L = number of transformer layers
- H = model dimension
- M = bytes per cache value (e.g. 2 for FP16)

**Worked example**: LLama-2 13B (L=40, H=5120), batch=32, seq=2048, FP16 (2 bytes): `2 × 32 × 2048 × 40 × 5120 × 2 = 54 GB`.

**The 3 TB number**: Pope et al. (2022) Google paper — a 500B+ MHA model with batch=512 and context=2048 has a **3 TB KV cache** — **three times the model's weights**.

### Scaling laws

- **KV-cache size grows *linearly* with sequence length × batch size × layers × model dim** — but the number of attention computations grows **quadratically** (O(n²)) with sequence length.
- This makes the KV cache the **structural bottleneck for long-context serving** — limited by hardware memory and made worse by load-time at strict latency budgets.

### Optimization buckets

Ch 9 groups attention/KV-cache optimization into three buckets:

1. **Redesign the attention mechanism** — [[LocalAttention]], [[CrossLayerAttention]], [[multiqueryattention|MQA]], [[GroupedQueryAttention|GQA]]. Requires retraining/finetuning.
2. **Optimize the KV cache** — [[PagedAttention]] (Kwon et al. 2023, vLLM), KV-cache quantization (Hooper 2024; Kang 2024), adaptive KV-cache compression (Ge 2023), selective KV cache (Liu 2024).
3. **Write kernels for attention computation** — [[FlashAttention]] (Dao 2022 for A100; Shah 2024 FlashAttention-3 for H100).

### CharacterAI's > 20× KV-cache reduction

[[CharacterAI]] (2024) — average conversation has **180 messages** of dialogue history. Stacking [[multiqueryattention|MQA]] + interleaved local/global attention + [[CrossLayerAttention|cross-layer attention]] **cut their KV cache > 20×**, removing memory as a bottleneck for large-batch serving.

### Training vs inference

> *"A KV cache is used only during inference, not training. During training, because all tokens in a sequence are known in advance, next token generation can be computed all at once instead of sequentially."* — Ch 9

## From [[mlsysbook-ch13-model-serving|mlsysbook Ch 13]]

Ch 13 treats the KV cache as **the dominant serving bottleneck for LLMs**: it is the *stateful* memory that distinguishes [[LLMServing|LLM serving]] from fixed-output serving, growing with every generated token and creating dynamic memory pressure (and fragmentation, addressed by [[PagedAttention]]). In the 70B-class figure, batch-32 hits the 80 GB OOM zone at just 8k context — forcing a hard batch-size-vs-context trade-off. **Memory capacity bounds concurrency; bandwidth bounds decode latency.** [[PrefixCaching]] reuses the KV state of shared prefixes, and KV-cache offloading spills inactive context to host RAM/NVMe to prevent OOM. [[ContinuousBatching]] must dynamically allocate/free the cache as sequences enter and exit. For 8B Llama 3 (GQA, INT4), ~0.31 MB/token at FP16 / much less at INT4 ⇒ ~2.2M tokens in 72 GB. See also [[mlsysbook-ch13-model-serving]].
