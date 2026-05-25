---
title: "Dzmitry Bahdanau"
type: entity
tags: [person, researcher, nlp, attention, neural-machine-translation]
sources: [hands-on-llm-ch01-introduction-to-llms]
last_updated: 2026-05-23
---

# Dzmitry Bahdanau

NLP researcher; first author (with [[KyunghyunCho|Kyunghyun Cho]] and [[YoshuaBengio|Yoshua Bengio]]) of *"Neural Machine Translation by Jointly Learning to Align and Translate"* (arXiv 1409.0473, 2014) — the paper that introduced **attention** to recurrent encoder-decoder neural machine translation, solving the fixed-context-vector bottleneck that had limited [[encoderdecoder|RNN-based seq2seq]] models. Cited in [[hands-on-llm-ch01-introduction-to-llms|*Hands-On LLMs* Ch 1]] as the originator of the attention mechanism that the [[1706.03762-attention-is-all-you-need|2017 Transformer paper]] subsequently distilled into the pure-attention architecture.

## In *Hands-On LLMs* Ch 1

The chapter walks through the Bahdanau-Cho-Bengio 2014 attention mechanism *before* the Transformer — describing how attention "selectively determines which words are most important in a given sentence" and lets a decoder attend to multiple encoder hidden states rather than just the final context vector.

## Connections

- [[KyunghyunCho]] / [[YoshuaBengio]] — co-authors of the 2014 attention paper.
- [[Attention]] — the mechanism he introduced.
- [[encoderdecoder|Encoder-Decoder]] / [[RNN]] — the architectures the 2014 paper extended.
- [[transformer|Transformer]] — the architecture that built on his attention idea.
- [[hands-on-llm-ch01-introduction-to-llms]] — Ch 1 anchors attention's introduction to Bahdanau et al. 2014.
