---
title: "Transformer"
type: concept
tags: [architecture, attention, foundational]
sources: [1706.03762-attention-is-all-you-need, 1810.04805-bert, 1910.10683-t5, 2001.08361-scaling-laws]
last_updated: 2026-05-10
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
