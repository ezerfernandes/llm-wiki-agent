---
title: "Made With ML — Recurrent Neural Networks (RNN)"
type: source
tags: [foundations, made-with-ml, deep-learning, rnn, nlp]
date: 2026-05-15
source_file: raw/madewithml/foundations-recurrent-neural-networks.md
---

## Summary
Foundations lesson on recurrent neural networks. Implements a vanilla RNN cell with `h_t = tanh(W_hh h_{t-1} + W_xh X_t + b_h)`, applies it to a text-classification task, and then upgrades to gated RNNs ([[LSTM]] and [[GRU]]) to address vanishing / exploding gradients on long sequences. Closes with a bidirectional GRU that processes the sequence forward and backward and concatenates hidden states, plus an inference example.

## Key Claims
- An RNN processes a sequence one timestep at a time, maintaining a hidden state `h_t` that summarizes everything seen so far — giving the model a principled way to use sequential order.
- The vanilla RNN update is `h_t = tanh(W_hh h_{t-1} + W_xh x_t + b_h)`, where the same weights are reused at every timestep (weight sharing across time).
- Vanilla RNNs suffer from vanishing or exploding gradients on long sequences: repeated multiplication by the same recurrent weight either shrinks to zero or blows up.
- Gated RNNs ([[LSTM]] and [[GRU]]) introduce learned gates that selectively retain or forget information, mitigating the gradient problem and allowing longer-range dependencies.
- GRUs typically match LSTM performance with fewer parameters; the lesson defaults to GRU for that reason.
- Bidirectional RNNs run a forward and a backward RNN over the sequence and concatenate their hidden states, giving each position context from both directions.
- A practical detail: when sequences in a batch are padded to a common length, the relevant hidden state is the one at the **actual last token**, not at the padded position — hence the `gather_last_relevant_hidden` helper.
- RNNs are hard to parallelize because each step depends on the previous step's hidden state — a disadvantage that later motivates attention and transformers.

## Key Quotes
> "We can process each timestep, one at a time, and predict the class after the last timestep (token) has been processed. This is very powerful because the model now has a meaningful way to account for the sequential order of tokens in our sequence." — Overview

> "Each time step's prediction depends on the previous prediction so it's difficult to parallelize RNN operations. Processing long sequences can yield memory and computation issues." — Disadvantages

> "When deciding between LSTMs and GRUs, empirical performance is the best factor but in general GRUs offer similar performance with less complexity (less weights)." — Gated RNN

## Connections
- [[MadeWithML]] — course this lesson belongs to
- [[GokuMohandas]] — author
- [[PyTorch]] — framework
- [[RNN]] — main concept
- [[LSTM]] — gated variant
- [[GRU]] — simpler gated variant, preferred default
- [[BidirectionalRNN]] — forward + backward pass
- [[VanishingGradient]] — motivation for gating
- [[ExplodingGradient]] — same problem in the opposite direction
- [[Embedding]] — input representation feeding the RNN
- [[Padding]] — handled via `gather_last_relevant_hidden`
- [[Attention]] — next lesson, motivated as a fix for RNN limitations
- [[Transformer]] — successor architecture removing sequential bottleneck

## Contradictions
- None identified.
