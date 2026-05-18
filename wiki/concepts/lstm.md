---
title: "Long Short-Term Memory (LSTM)"
type: concept
tags: [rnn, architecture, foundational]
sources: [1409.3215-seq2seq, d2l-recurrent-modern]
last_updated: 2026-05-16
---

# Long Short-Term Memory (LSTM)

A recurrent neural network architecture introduced by [[SeppHochreiter|Hochreiter]] & [[JurgenSchmidhuber|Schmidhuber]] (1997) designed to learn long-range temporal dependencies that standard [[RNN|RNNs]] cannot, by replacing the simple sigmoid update with a **gated [[MemoryCell|memory cell]]** whose self-connected recurrent edge has fixed weight 1 — so gradients can pass through many time steps without [[VanishingGradient|vanishing]] ([[d2l-recurrent-modern]] §lstm).

## Architecture (D2L formulation)

For input $\mathbf{X}_t\in\mathbb{R}^{n\times d}$ and previous hidden state $\mathbf{H}_{t-1}\in\mathbb{R}^{n\times h}$, the cell computes four pre-activations of the same form $\mathbf{X}_t\mathbf{W}_\textrm{x\cdot} + \mathbf{H}_{t-1}\mathbf{W}_\textrm{h\cdot} + \mathbf{b}_\cdot$:

- **[[InputGate|Input gate]]** $\mathbf{I}_t = \sigma(\cdot)\in(0,1)^{n\times h}$ — how much new content enters the cell.
- **[[ForgetGate|Forget gate]]** $\mathbf{F}_t = \sigma(\cdot)\in(0,1)^{n\times h}$ — how much old cell state persists.
- **[[OutputGate|Output gate]]** $\mathbf{O}_t = \sigma(\cdot)\in(0,1)^{n\times h}$ — how much of the cell is exposed as the hidden state.
- **Input node (candidate)** $\tilde{\mathbf{C}}_t = \tanh(\cdot)\in(-1,1)^{n\times h}$.

Then:

$$\mathbf{C}_t = \mathbf{F}_t\odot \mathbf{C}_{t-1} + \mathbf{I}_t\odot \tilde{\mathbf{C}}_t, \quad \mathbf{H}_t = \mathbf{O}_t\odot \tanh(\mathbf{C}_t).$$

If $\mathbf{F}_t\!\to\!1$ and $\mathbf{I}_t\!\to\!0$, the cell carries state unchanged indefinitely — the structural mechanism that defeats vanishing gradients. Only $\mathbf{H}_t$ feeds the output layer; $\mathbf{C}_t$ is entirely internal.

## Why "long short-term memory"

[[d2l-recurrent-modern]]'s pedagogical framing: weights are *long-term memory* (slow gradient updates encode general knowledge), activations are *short-term memory* (ephemeral). The cell adds an *intermediate* tier — controllable memory that lasts longer than activations but updates faster than weights.

## Role in this wiki

[[1409.3215-seq2seq]] uses two stacked 4-layer LSTMs (encoder + decoder), 1000 cells per layer, 384M total parameters, to map English sentences to French. Key empirical findings:

- **Depth helps.** Each added LSTM layer reduced perplexity by ~10%.
- **Exploding gradients are the real risk.** LSTMs do not suffer from *vanishing* gradients but can still explode; the paper clips gradient norm to 5.
- **Source reversal** (mapping `c,b,a → α,β,γ` instead of `a,b,c → α,β,γ`) drops perplexity 5.8 → 4.7 and lifts BLEU 25.9 → 30.6 — interpreted as reducing the "minimal time lag" between aligned tokens.
- **Long sentences are not a structural problem** for an LSTM trained on reversed inputs — contrary to other groups' contemporaneous findings with similar architectures.

## Successor

LSTMs were the default sequence-modeling backbone from 2011 until the rise of [[transformer|Transformer]] models in 2017 ([[d2l-recurrent-modern]] §lstm summary). [[1706.03762-attention-is-all-you-need]] showed that pure attention is faster to train (O(1) sequential ops per layer vs. O(n) for RNNs) and reaches higher BLEU. Per D2L: "Even Transformers owe some of their key ideas to architecture design innovations introduced by the LSTM."

[[2001.08361-scaling-laws]] (Kaplan et al., 2020) supplies the empirical scaling argument for the displacement: with matched non-embedding parameter counts, LSTMs and Transformers tie on the first ~100 tokens of a 1024-token context, but **LSTMs plateau** while Transformers keep improving across the full context.

## See also
- [[SeqToSeq]]
- [[EncoderDecoder]]
- [[Transformer]]
- [[GRU]] — the streamlined variant
- [[MemoryCell]] / [[InputGate]] / [[ForgetGate]] / [[OutputGate]] — internal components
- [[BidirectionalRNN]] — composable with LSTM (Graves & Schmidhuber 2005)
- [[DeepRNN]] — multi-layer LSTM is the canonical deep-RNN instance
