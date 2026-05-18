---
title: "Bidirectional RNN"
type: concept
tags: [rnn, architecture, sequence-encoding]
sources: [d2l-recurrent-modern, d2l-nlp-applications]
last_updated: 2026-05-16
---

# Bidirectional RNN

A **bi-RNN** ([[MikeSchuster|Schuster]] & [[KuldipPaliwal|Paliwal]] 1997) is an RNN architecture in which two unidirectional RNNs scan the same input *in opposite directions* and their hidden states are concatenated at each time step ([[d2l-recurrent-modern]] §bi-rnn).

## Recurrence

Forward and backward states use separate parameter sets:

$$\overrightarrow{\mathbf{H}}_t = \phi(\mathbf{X}_t\mathbf{W}_\textrm{xh}^{(f)} + \overrightarrow{\mathbf{H}}_{t-1}\mathbf{W}_\textrm{hh}^{(f)} + \mathbf{b}_\textrm{h}^{(f)}),$$
$$\overleftarrow{\mathbf{H}}_t = \phi(\mathbf{X}_t\mathbf{W}_\textrm{xh}^{(b)} + \overleftarrow{\mathbf{H}}_{t+1}\mathbf{W}_\textrm{hh}^{(b)} + \mathbf{b}_\textrm{h}^{(b)}).$$

Concatenate: $\mathbf{H}_t = [\overrightarrow{\mathbf{H}}_t; \overleftarrow{\mathbf{H}}_t] \in \mathbb{R}^{n\times 2h}$. Output layer's input dimension doubles: $\mathbf{W}_\textrm{hq}\in\mathbb{R}^{2h\times q}$.

## When to use (and when not to)

**Use** when the prediction at each step is allowed to depend on the full bidirectional context — sequence labeling (POS tagging, NER), encoder-side blocks of [[SeqToSeq|seq2seq]] models, masked-token pretraining ([[bert|BERT]]-style MLM).

**Do not use** for next-token / autoregressive prediction at inference time. The backward pass requires the entire future of the sequence, which does not exist during left-to-right generation. This is the structural reason bi-RNNs appear in *encoders* but never in *decoders*, and is the foundation for [[CausalMask|causal masking]] in [[Transformer|Transformer]] decoders.

## Cost

Per D2L: "Bidirectional RNNs are very costly to train due to long gradient chains." Each direction propagates gradients across the full sequence; with $L$ stacked layers, gradient computation scales as $\mathcal{O}(2LT)$ matrix products forward and backward.

## Composes with gating

Bi-RNN is an orthogonal axis to cell choice — Graves & Schmidhuber 2005 introduced **bidirectional LSTM** (BiLSTM) for phoneme classification; Graves 2008 used bidirectional LSTMs for handwriting recognition. Bi-GRU is similarly common. The PyTorch / MXNet `bidirectional=True` flag composes with any gated cell.

## See also
- [[RNN]] / [[LSTM]] / [[GRU]] — composable cell types.
- [[DeepRNN]] — orthogonal architectural axis (depth).
- [[MikeSchuster]] / [[KuldipPaliwal]] — original authors (1997).
- [[EncoderDecoder]] — bi-RNN's natural deployment site (encoder side).
- [[CausalMask]] — the Transformer-era equivalent of the "no future at inference" constraint.
- [[bert]] — masked-language-modeling pretraining is the conceptual successor to bi-RNN sequence encoding.
- [[d2l-nlp-applications]] §`sentiment-analysis-rnn` — the canonical bi-RNN + frozen [[GloVe]] [[SentimentAnalysis|sentiment-analysis]] baseline (2-layer BiLSTM, concat initial+final hidden states → FC head).
