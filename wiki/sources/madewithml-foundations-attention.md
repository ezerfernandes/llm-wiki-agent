---
title: "Made With ML — Attention"
type: source
tags: [foundations, made-with-ml, deep-learning, attention, nlp]
date: 2026-05-15
source_file: raw/madewithml/foundations-attention.md
---

## Summary
Foundations lesson introducing attention as a learned weighted-pooling mechanism over RNN hidden states. Instead of using only the final RNN output (which loses information from earlier timesteps and is hurt by vanishing gradients), the model computes attention weights `α = softmax(W_attn h)` over every encoded position and uses the weighted sum `c_t = Σ α_{t,i} h_i` as a context-aware representation for classification. Closes with an interpretability section that visualizes per-token attention weights and a taxonomy of attention variants (soft / global, hard, local, [[selfattention]]).

## Key Claims
- Attention solves a key RNN limitation: using only the last hidden state forces the model to compress the whole sequence into one vector, which hurts on long inputs and amplifies vanishing-gradient effects.
- The attention pattern is: project encoder outputs through a learned weight matrix, apply softmax to produce non-negative weights summing to one, and use those weights to form a weighted sum of the encoder outputs.
- Attention weights are directly interpretable as token importance — the lesson visualizes them per example to show which words the model focused on.
- Soft / global attention attends to all positions (differentiable, expensive); hard attention picks discrete positions (not differentiable, requires REINFORCE); local attention is a windowed compromise.
- Self-attention attends within a single sequence (each token attends to every other token in the same sequence) — this is the variant the next lesson generalizes into the [[Transformer]].
- Attention adds a learnable weight matrix and a softmax to the model — a small compute cost for a large representational gain.
- The architecture in this lesson is RNN + attention; in the next lesson the RNN is removed entirely and replaced with stacked self-attention.

## Key Quotes
> "We were constrained to using the representation at the very end but what if we could give contextual weight to each encoded input (h_i) when making our prediction? This is also preferred because it can help mitigate the vanishing gradient issue which stems from processing very long sequences." — Overview

> "At it's core, attention is about learning how to weigh a group of encoded representations to produce a context-aware representation to use for downstream tasks. This is done by learning a set of attention weights and then using softmax to create attention values that sum to 1." — Objective

> "Several state-of-the-art approaches extend on basic attention to deliver highly context-aware representations (ex. self-attention)." — Miscellaneous

## Connections
- [[MadeWithML]] — course this lesson belongs to
- [[GokuMohandas]] — author
- [[PyTorch]] — framework
- [[Attention]] — central concept
- [[selfattention]] — single-sequence variant, transformer building block
- [[Softmax]] — produces normalized attention weights
- [[RNN]] — encoder this lesson attends over
- [[GRU]] — specific RNN variant used here
- [[Transformer]] — next-lesson successor, built entirely from self-attention
- [[VanishingGradient]] — problem partially mitigated by attention
- [[Interpretability]] — per-token attention-weight visualization
- [[ContextVector]] — weighted-sum output of attention

## Contradictions
- None identified.
