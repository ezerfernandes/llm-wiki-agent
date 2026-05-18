---
title: "Bahdanau Attention"
type: concept
tags: [attention, machine-translation, seq2seq, foundational]
sources: [d2l-attention-and-transformers]
last_updated: 2026-05-16
---

# Bahdanau Attention

The first widely-adopted differentiable [[Attention|attention mechanism]], introduced by **Bahdanau, Cho & Bengio 2014** to fix the fixed-vector bottleneck of the [[1409.3215-seq2seq|Sutskever-Vinyals-Le 2014]] encoder–decoder for [[MachineTranslation|neural machine translation]].

## The fix

Pre-Bahdanau, the encoder compressed the entire source sentence into a single fixed-shape state $\mathbf{c}$ that the decoder used as its only source of information about the input. This breaks down for long sentences — eventually there is "not enough space" in $\mathbf{c}$.

Bahdanau redefines the decoder context as a **per-step weighted sum of encoder hidden states**:

$$\mathbf{c}_{t'} = \sum_{t=1}^T \alpha(\mathbf{s}_{t'-1}, \mathbf{h}_t)\,\mathbf{h}_t$$

where:
- $\mathbf{s}_{t'-1}$ — previous decoder hidden state, plays the role of the **query**;
- $\mathbf{h}_t$ — encoder hidden state at source position $t$, plays the role of both **key** and **value**;
- $\alpha$ — softmax over an [[AdditiveAttention|additive]] scoring function $a(\mathbf{q},\mathbf{k}) = \mathbf{w}_v^\top\tanh(\mathbf{W}_q\mathbf{q} + \mathbf{W}_k\mathbf{k})$.

The decoder can now *dynamically* focus on different source positions at each generation step. The whole pipeline remains end-to-end differentiable.

## Significance

[[d2l-attention-and-transformers|D2L]]: "While quite innocuous in its description, this Bahdanau attention mechanism has arguably turned into one of the most influential ideas of the past decade in deep learning, giving rise to [[Transformer|Transformers]] and many related new architectures."

Two qualitative effects:
1. **Better long-sentence MT.** Bahdanau models outperformed fixed-context seq2seq, especially on long sentences.
2. **Apparent interpretability.** Attention heatmaps recover plausible cross-lingual alignments — e.g. high weight on *feet* when generating *pieds* in "my feet hurt" → "j'ai mal aux pieds". (Whether this constitutes interpretability remains contested.)

Bahdanau attention is the direct ancestor of [[SelfAttention|self-attention]]: same QKV machinery, same softmax-of-scores aggregation — just with queries also drawn from the input sequence.

## See also

- [[Attention]] · [[AdditiveAttention]] · [[QueryKeyValue]] · [[EncoderDecoder]] · [[SeqToSeq]] · [[MachineTranslation]] · [[KyunghyunCho]] · [[Transformer]] · [[1409.3215-seq2seq]]
