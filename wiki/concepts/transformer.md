---
title: "Transformer"
type: concept
tags: [architecture, attention, foundational]
sources: [1706.03762-attention-is-all-you-need, 1810.04805-bert, 1910.10683-t5, 2001.08361-scaling-laws, d2l-attention-and-transformers, ai-engineering-ch02-foundation-models, hands-on-llm-ch01-introduction-to-llms, hands-on-llm-ch03-looking-inside-llms, hands-on-llm-ch09-multimodal-llms, mlsysbook-ch06-network-architectures]
last_updated: 2026-06-05
---

# Transformer

A sequence transduction architecture introduced in [[1706.03762-attention-is-all-you-need]] (Vaswani et al., 2017) that relies entirely on attention mechanisms — no recurrence, no convolutions. The Transformer is now the default architecture for large language models. It directly inherits the encoder-decoder framing of [[1409.3215-seq2seq]] (Sutskever, Vinyals & Le, 2014), but replaces the [[LSTM]] backbone with stacked [[SelfAttention]] and resolves the fixed-vector bottleneck structurally via encoder-decoder attention.

## Structure

The Transformer follows an encoder-decoder design ([[EncoderDecoder]]) but replaces the recurrent layers of prior seq2seq models with stacked self-attention plus position-wise feed-forward sub-layers.

- **Encoder.** A stack of N=6 identical layers. Each layer has two sub-layers: a [[MultiHeadAttention]] self-attention sub-layer and a position-wise fully-connected feed-forward network. Each sub-layer is wrapped in a residual connection followed by layer normalization: `LayerNorm(x + Sublayer(x))`. All sub-layers and embeddings produce outputs of dimension d_model = 512 (base model).
- **Decoder.** Also N=6 layers. Each adds a third sub-layer that performs multi-head attention over the encoder output. The decoder self-attention is **masked** (set to −∞ before softmax) so position i can only attend to positions ≤ i — preserving the auto-regressive property.
- **Position-wise FFN.** `FFN(x) = max(0, xW₁ + b₁)W₂ + b₂` — applied identically to each position, with d_ff = 2048 inner dimension. Equivalent to two convolutions with kernel size 1.
- **Embeddings.** Input and output token embeddings share weights with the pre-softmax linear transformation; embeddings are scaled by √d_model.
- **[[PositionalEncoding]].** Sinusoidal encodings added to embeddings to inject order information.

## Why it works

[[1706.03762-attention-is-all-you-need]] motivates the design via three desiderata:
1. **Total computational complexity per layer.** Self-attention is O(n²·d), faster than recurrent O(n·d²) when n < d (typical for sentence-level NMT).
2. **Parallelizable computation.** Self-attention requires O(1) sequential operations vs. O(n) for recurrent layers — enabling much higher GPU utilization.
3. **Maximum path length for long-range dependencies.** Self-attention connects all positions with O(1) maximum path length; recurrent layers require O(n).

## Variants and constants

- Base: N=6, d_model=512, d_ff=2048, h=8 heads, d_k=d_v=64, P_drop=0.1, ε_ls=0.1, ~65M params.
- Big: N=6, d_model=1024, d_ff=4096, h=16 heads, P_drop=0.3, ~213M params.

Ablation findings (Table 3 of [[1706.03762-attention-is-all-you-need]]):
- Single-head attention is 0.9 BLEU worse than 8-head; too many heads also hurt.
- Reducing d_k hurts quality — compatibility is hard.
- Bigger models are better; dropout is critical to avoid over-fitting.
- Learned positional embeddings produce "nearly identical" results to sinusoidal.

## Role in the wider wiki

Every paper in the AI/LLM corpus assumes the Transformer as the base architecture. [[1810.04805-bert]] (2018) used the encoder half alone for [[maskedlanguagemodel]] pre-training; [[1910.10683-t5]] (2020) vindicated the full encoder-decoder structure at scale via [[spancorruption]] on [[c4]] and the [[texttotextframework]]. The 2026 papers extend it via training recipes ([[2601.21343-self-improving-pretraining]], [[2605.02572-long-horizon-llm-training]]), agentic harnesses ([[2605.02396-heavyskill]], [[2604.20987-cos-play]]), or coordination overlays ([[2512.04388-conductor]], [[2605.03310-coordination-architectural-layer]]) — but the substrate they all build on is defined here.

## T5's minor deviations

[[1910.10683-t5]] uses the Transformer essentially as proposed, with two small changes worth recording:
- LayerNorm bias removed; layer normalization is placed *outside* the residual path (pre-norm with no bias).
- Relative position embeddings replaced with a single learned scalar per (head, bucket) added to attention logits, with 32 log-spaced buckets up to offset 128 and parameters shared across all layers.

## Empirical scaling

[[2001.08361-scaling-laws]] (Kaplan, McCandlish et al., 2020) studies decoder-only Transformer LMs from $10^3$ to $1.5 \times 10^9$ non-embedding parameters and establishes that test loss obeys clean [[PowerLaw]] relations in non-embedding parameter count $N$, dataset size $D$ (tokens), and training compute $C$ — see [[ScalingLaws]]. Two findings specific to the Transformer:

- **Shape is second-order.** At fixed $N$, varying depth-to-width ratio, attention-head count, and feed-forward ratio moves loss by only a few percent. Architecture design for LMs is mostly about choosing $N$.
- **Asymptotic dominance over LSTMs.** With matched non-embedding $N$, LSTMs match Transformers on early tokens of a 1024-token context but plateau after ~100 tokens; Transformers keep improving across the full context. Per-token loss obeys a power law in context position with a larger exponent for larger models — i.e. bigger Transformers exploit long context more effectively.

The [[ComputeEfficientTraining]] prescription derived from these laws — $N \propto C^{0.73}$, $S \propto C^{0.03}$ — is the quantitative basis for scaling Transformers up rather than training them longer.

## Default implementation: FlashAttention

The attention operation as written in [[1706.03762-attention-is-all-you-need]] is **memory-bound** on modern GPUs; the standard PyTorch implementation reads/writes the N×N matrix to HBM and is dominated by that traffic. [[2205.14135-flashattention]] (Dao et al., 2022) introduces **[[FlashAttention]]** — an IO-aware, exact, fused-kernel implementation of the same operation that runs many times faster and scales to much longer sequences. FlashAttention (and its successors -2/-3) is now the de-facto attention kernel behind essentially every modern Transformer training and inference stack. The architecture described above is unchanged; only its implementation is.

## See also
- [[SelfAttention]]
- [[MultiHeadAttention]]
- [[ScaledDotProductAttention]]
- [[PositionalEncoding]]
- [[EncoderDecoder]]
- [[FlashAttention]]
- [[mlsysbook-ch06-network-architectures]] — systems view: training is *compute-bound* ($\mathcal{O}(S^2)$, the "quadratic wall"); autoregressive inference is *memory-bandwidth-bound* (reload all weights per token + read/write the [[KVCache|KV cache]], which grows linearly with $S$ and concurrency). The transformer is framed as a *recombination* of portable building blocks — [[GEMM]] feedforward + [[SkipConnection|skip connections]] + [[LayerNormalization|LayerNorm]] + [[Attention|softmax-attention gating]] — atop the adaptive [[InductiveBias|inductive bias]] (no spatial prior; learn all pairwise relations).

## From [[ai-engineering-ch02-foundation-models|AI Engineering Ch 2]]

[[ChipHuyen|Chip Huyen]] in Ch 2 supplies the **practitioner-grade walkthrough** of the Transformer:

### Two-phase inference

- **[[Prefill|Prefill]]** — input tokens processed in parallel; produces K, V vectors for every input token.
- **[[Decode|Decode]]** — output tokens generated sequentially, one at a time.

Even though Transformers eliminated the *input-side* sequential bottleneck of seq2seq, autoregressive LMs still have the *output-side* sequential bottleneck. This asymmetry motivates inference-optimization techniques (Ch 9 of the book).

### Why context-length is expensive

> "Because each previous token has a corresponding key and value vector, the longer the sequence, the more key and value vectors need to be computed and stored. This is one reason why it's so hard to extend context length for transformer models."

### Llama 2 / Llama 3 dimensions (Ch 2 Table 2-4)

| Model | # blocks | Model dim | FFN dim | Vocab | Context |
|---|---|---|---|---|---|
| Llama 2-7B | 32 | 4,096 | 11,008 | 32K | 4K |
| Llama 2-13B | 40 | 5,120 | 13,824 | 32K | 4K |
| Llama 2-70B | 80 | 8,192 | 22,016 | 32K | 4K |
| Llama 3-7B | 32 | 4,096 | 14,336 | 128K | 128K |
| Llama 3-70B | 80 | 8,192 | 28,672 | 128K | 128K |
| Llama 3-405B | 126 | 16,384 | 53,248 | 128K | 128K |

Llama 2-7B's attention: 4096 hidden dim / 32 heads → 128-dim per head.

### Activation functions

ReLU (GPT-2) vs **GELU** (GPT-3). Ch 2's observation: sophisticated activation functions don't beat simple ones at LLM scale — *"the model just needs a nonlinear function to break the linearity from the feedforward layers."*

### Three transformer alternatives gaining traction (Ch 2)

- **[[RWKV]]** — RNN-based, parallelizable training.
- **[[StateSpaceModel|SSMs]]** — S4 → H3 → [[Mamba]]; linear-time inference.
- **[[Jamba]]** — hybrid Transformer–Mamba MoE.

> "While transformer-based models are dominating, as of this writing, several alternative architectures are gaining traction." — Ch 2

### Why developing a transformer-replacement is hard

Ch 2 cites Ilya Sutskever's argument: gradient descent is a *search algorithm* over programs a neural network can simulate. **For new architectures to outperform existing ones, they have to simulate programs existing architectures cannot.** Plus: the Transformer has been heavily optimized since 2017 — first on [[google|Google]]'s TPUs, then on NVIDIA GPUs — raising the bar for a successor.

## From [[hands-on-llm-ch01-introduction-to-llms|*Hands-On LLMs* Ch 1]]

[[JayAlammar|Alammar]] and [[MaartenGrootendorst|Grootendorst]] frame the Transformer in Ch 1 as **the central pivot in the history of [[LanguageAI|Language AI]]** — the architecture that *"could be trained in parallel, which tremendously sped up training"* and removed the recurrence that had limited prior [[encoderdecoder|RNN encoder-decoder]] models with attention.

Ch 1's structural framing:

- **The encoder block** = self-attention + feedforward neural network. Self-attention *"can attend to different positions within a single sequence, thereby more easily and accurately representing the input sequence ... Instead of processing one token at a time, it can be used to look at the entire sequence in one go."*
- **The decoder block** = masked self-attention + encoder-attention + feedforward. Masked self-attention *"masks future positions so it only attends to earlier positions to prevent leaking information when generating the output."*
- **The architecture remains autoregressive** — *"needing to consume each generated word before creating a new word."*

The chapter explicitly names the two descendant family lines the Transformer spawned in 2018:

- **Encoder-only descendants** ([[bert|BERT]], 2018) → [[RepresentationModel|representation models]] for embedding-producing tasks.
- **Decoder-only descendants** ([[GPT|GPT-1]], 2018) → [[GenerativeModel|generative models]] for text-generating tasks.

> "Together, these building blocks create the Transformer architecture and are the foundation of many impactful models in Language AI, such as BERT and GPT-1." — Ch 1

The chapter forward-references Chs 2 and 3 for *"multi-head attention, positional embeddings, and layer normalization"* — the additional Transformer mechanics it deliberately defers.

## From [[hands-on-llm-ch03-looking-inside-llms|*Hands-On LLMs* Ch 3]]

Ch 3 is the book's **Transformer-internals deep-dive** — the intuition-first walkthrough of the decoder-only generative LLM with a runnable dissection of [[Phi3Mini|Phi-3-mini]]'s 32 decoder layers.

### Three top-level components

> "A Transformer LLM is made up of a tokenizer, a stack of Transformer blocks, and a language modeling head." — Ch 3

- **[[Tokenizer|Tokenizer]]** — vocabulary → token IDs (covered in [[hands-on-llm-ch02-tokens-and-embeddings|Ch 2]]).
- **Stack of Transformer blocks** — the bulk of processing; typically 6 (original Transformer) to 100+ (large LLMs).
- **[[LMHead|LM head]]** — a single linear layer mapping the final hidden state to vocab-sized logits.

### Phi-3-mini structural read-out

For `microsoft/Phi-3-mini-4k-instruct`, Ch 3 prints the live PyTorch module tree:

- **Embedding**: `Embedding(32064, 3072, padding_idx=32000)` — 32,064-token vocabulary, 3,072-dim embeddings.
- **32 × Phi3DecoderLayer**, each containing:
  - `Phi3Attention(qkv_proj=Linear(3072 → 9216), o_proj=Linear(3072 → 3072), rotary_emb=Phi3RotaryEmbedding)` — fused [[QueryProjection|Q]] / [[KeyProjection|K]] / [[ValueProjection|V]] projection (3,072 × 3 = 9,216 output features) and [[RoPE|RoPE]] applied at the attention step.
  - `Phi3MLP(gate_up_proj=Linear(3072 → 16384), down_proj=Linear(8192 → 3072), activation_fn=SiLU)` — gated MLP consistent with [[SwiGLU|SwiGLU]]; [[SiLU]] activation.
  - Two `Phi3RMSNorm` ([[RMSNorm|RMSNorm]]) in pre-norm placement (`input_layernorm` before attention, `post_attention_layernorm` before MLP).
- **`lm_head: Linear(3072 → 32064, bias=False)`** — projects final hidden state to vocab logits.

### The 2024-era block recipe

Ch 3 codifies the **modern Transformer block** as the bundle of: **[[PreNorm|pre-normalization]] + [[RMSNorm]] + [[SwiGLU]] + [[GroupedQueryAttention|GQA]] + [[RoPE]]** (used by [[Llama|Llama 2]] / [[Llama|Llama 3]]). Differences from the 2017 original:

| Component | Original Transformer (2017) | Modern LLM (2024) |
|---|---|---|
| Normalization placement | Post-norm | **Pre-norm** |
| Normalization function | LayerNorm | **RMSNorm** |
| FFN activation | ReLU | **SwiGLU** (gated, SiLU-based) |
| Positional encoding | Sinusoidal / learned, added at input | **RoPE**, applied at attention step (per layer) |
| Attention | Multi-head, full | **GQA**, full per block (or local/sparse interleaved as in [[GPT3|GPT-3]]) |
| Inference-time cache | — | **[[KVCache|KV cache]]** + FlashAttention kernel |

### Parallel token streams

> "Each token is processed through its own stream of computation (with some interaction between them in attention steps)." — Ch 3

The number of [[TokenStream|streams]] equals the [[ContextLength|context length]]. Cross-stream interaction happens only in attention sub-layers; the [[FeedForwardNetwork|FFN]] processes each stream independently. **Only the last stream's output** is fed to the [[LMHead|LM head]], but every earlier stream's intermediate computations are needed in attention — which is what makes the [[KVCache|KV cache]] such a high-leverage optimization (5× speedup on Phi-3-mini / Colab T4 / 100 tokens).

## From [[hands-on-llm-ch09-multimodal-llms|*Hands-On LLMs* Ch 9]]

Ch 9 supplies the **wiki's cleanest statement of the structural reason the Transformer generalizes across modalities** — the [[VisionTransformer|Vision Transformer]] (Dosovitskiy et al. 2020) is the encoder applied to images by **tokenizing the image into patches** and treating patch embeddings the same way as text token embeddings:

> *"What is so interesting about this approach is that the moment the embeddings are passed to the encoder, they are treated as if they were textual tokens. From that point forward, there is no difference in how a text or image trains."* — Ch 9

The structural punchline is that the Transformer's attention machinery is **modality-agnostic once the embeddings are produced** — it operates on a sequence of vectors regardless of whether they came from text tokenization, [[PatchEmbedding|image patching]], audio framing, or any other modality. This sameness-after-tokenization is the **structural precondition for adapter-style multimodal LLMs** ([[BLIP2|BLIP-2]] / [[LLaVA15|LLaVA]] / [[Idefics2|Idefics 2]]) to work — a [[QFormer|Q-Former]] or MLP projector only needs to bring visual features into the LLM's embedding space; from there, the Transformer treats them as soft visual prompts indistinguishable from text-derived inputs.

Ch 9 is also the wiki's first explicit walk of the **Transformer encoder applied to images** ([[VisionTransformer|ViT]] is encoder-only) and of the parallel between text tokenization and image patching as structurally identical operations from the encoder's point of view.
