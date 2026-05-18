---
title: "Teacher Forcing"
type: concept
tags: [training, sequence-models, rnn, language-models]
sources: [d2l-recurrent-neural-networks, d2l-recurrent-modern]
last_updated: 2026-05-16
---

# Teacher Forcing

A training scheme for autoregressive sequence models: at every time step, **feed the ground-truth previous token** as input rather than the model's own previous prediction ([[d2l-recurrent-neural-networks]] §language-model).

## Mechanics in D2L's RNN LM

Given a length-$n$ subsequence $\mathbf{x}_t = [x_t, \ldots, x_{t+n-1}]$:
- **Input**: $\mathbf{x}_t$.
- **Target**: $\mathbf{x}_{t+1} = [x_{t+1}, \ldots, x_{t+n}]$ (the input shifted by one token).
- The RNN processes the input *in parallel* across time steps (within the unrolled graph), predicting the next token at every position.

Because the targets are the ground-truth next tokens, errors at step $t$ do not propagate as wrong inputs to step $t+1$ during training — gradients flow cleanly through BPTT.

## Trade-offs

- **Pro:** Training is fast and stable. The model never sees its own (potentially wrong) predictions during training.
- **Con: Exposure bias.** At inference time the model *must* feed its own predictions; if early predictions are slightly wrong, the model drifts into states it never saw during training. This is the well-known exposure-bias / scheduled-sampling problem ([[1409.3215-seq2seq]] and follow-ups).

## Seq2seq variant

For [[SeqToSeq|seq2seq]] training ([[d2l-recurrent-modern]] §seq2seq) the recipe extends: decoder *input* is `<bos>` concatenated with the target sequence minus its last token; decoder *target* is the target sequence shifted by one (so position $t$'s target is position $t+1$'s token). The loss is **masked** beyond each sequence's `valid_len` — padded positions contribute zero gradient (D2L extends [[CrossEntropyLoss|cross-entropy]] with a `valid_len` argument). At inference, the model feeds its own predictions autoregressively (the exposure-bias scenario below).

## Used everywhere

Teacher forcing is the default training recipe for autoregressive sequence-to-sequence and language models: [[RNN]] LMs, [[transformer|Transformer]] LMs (next-token prediction with shifted targets and causal masking), seq2seq translation models.

## Connections

- [[d2l-recurrent-neural-networks]] — the partitioning + shifted-target scheme (§language-model).
- [[AutoregressiveModel]] — what teacher forcing is the training mode for.
- [[LanguageModel]] / [[CharacterLevelLanguageModel]] — primary application.
- [[RNN]] / [[Transformer]] — architectures trained with teacher forcing.
- [[1409.3215-seq2seq]] — early seq2seq teacher-forcing exemplar.
