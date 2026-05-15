---
title: "Machine Translation"
type: concept
tags: [task, nlp, foundational]
sources: [1409.3215-seq2seq, 1706.03762-attention-is-all-you-need]
last_updated: 2026-05-10
---

# Machine Translation

The task of automatically translating text from one natural language to another. Historically dominated by **statistical machine translation (SMT)** — phrase-based systems built on word alignments, phrase tables, and n-gram language models — and now by neural machine translation (NMT) built on the encoder-decoder pattern.

## Why it matters to this wiki

Machine translation is the foundational testbed for sequence transduction in deep learning. The two papers that define modern sequence modeling in this wiki both validate their architectures on WMT'14 EN→FR:

- **[[1409.3215-seq2seq]]** (2014) — first pure neural system to beat a phrase-based SMT baseline at scale (BLEU 34.81 vs. 33.30). Used deep [[LSTM]] encoder-decoder.
- **[[1706.03762-attention-is-all-you-need]]** (2017) — supersedes recurrence entirely with self-attention. BLEU 41.8 on the same task at ~1/4 the training cost of the prior best.

The progression `SMT → recurrent seq2seq → attention → Transformer` plays out almost entirely on WMT translation benchmarks and is the load-bearing example of how architectural changes drive language-modeling progress.

## Standard benchmarks
- **WMT (Workshop on Machine Translation)** — annual shared task. EN↔FR and EN↔DE are the canonical pairs.
- Evaluation: [[BLEU]] (cased, on tokenized output, via `multi-bleu.pl` for results in this wiki).

## See also
- [[SeqToSeq]]
- [[EncoderDecoder]]
- [[Transformer]]
- [[BLEU]]
