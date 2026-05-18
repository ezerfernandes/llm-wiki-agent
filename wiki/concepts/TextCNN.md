---
title: "TextCNN"
type: concept
tags: [model, nlp, cnn, sentiment-analysis, text-classification]
sources: [d2l-nlp-applications]
last_updated: 2026-05-16
---

# TextCNN

**textCNN** ([[YoonKim|Kim]] 2014, "Convolutional Neural Networks for Sentence Classification") — a 1-dimensional [[CNN]] architecture for sentence-level [[TextClassification|text classification]] (sentiment analysis, topic classification). The canonical CNN-for-NLP baseline. Per [[d2l-nlp-applications]] §`sentiment-analysis-cnn`: treat a sentence as a 1-D image of token embeddings, slide kernels of multiple widths to capture local $n$-gram features, max-pool over time, concatenate, classify.

## Architecture

1. **Input** — sentence with $n$ tokens, each represented by a $d$-dimensional vector (typically [[GloVe]] 100-d). Width = $n$, channels = $d$. Often two embedding "tracks" — one trainable, one frozen with pretrained vectors.
2. **Multiple 1-D convolutions** — kernels of widths 3 / 4 / 5 (canonical Kim 2014 setting), each with $\sim$100 output channels. Different widths capture different-length $n$-grams.
3. **[[MaxOverTimePooling|Max-over-time pooling]]** — per channel, take the maximum activation across time steps. Output: one scalar per output channel.
4. **Concatenate** the pooling outputs into a single vector.
5. **Dropout** ($p = 0.5$) for regularization.
6. **Fully connected** layer to the output classes (e.g. 2 for binary sentiment).

## Key insight

Multi-input-channel 1-D cross-correlation is **equivalent** to single-input-channel 2-D cross-correlation where the kernel height matches the input height — so the textCNN inherits all of D2L's CNN machinery from [[d2l-convolutional-neural-networks]] while looking like a "1-D image" model semantically.

## Connections

- [[CNN]] / [[OneByOneConvolution|1×1 conv]] / [[MaxPooling]] — generalized to the [[MaxOverTimePooling|max-over-time]] variant.
- [[GloVe]] — the typical pretrained input.
- [[SentimentAnalysis]] / [[TextClassification]] — the downstream tasks textCNN serves.
- [[BidirectionalRNN]] — the alternative architectural choice in [[d2l-nlp-applications]] (RNN-based sentiment baseline).
- [[YoonKim]] — author.
- [[d2l-nlp-applications]] §`sentiment-analysis-cnn` — D2L's canonical worked example.
