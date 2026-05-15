---
title: "BLEU"
type: concept
tags: [evaluation, machine-translation, metric]
sources: [1409.3215-seq2seq, 1706.03762-attention-is-all-you-need]
last_updated: 2026-05-10
---

# BLEU

**Bilingual Evaluation Understudy** — an automatic metric for machine translation introduced by Papineni et al. (ACL 2002). BLEU measures the modified n-gram precision of a candidate translation against one or more reference translations, multiplied by a brevity penalty to discourage short outputs. Scores range 0–100; higher is better.

```
BLEU = BP · exp( Σ_{n=1..N} w_n · log p_n )
```
where `p_n` is the modified n-gram precision (clipped to the max count in any reference) and `BP = min(1, exp(1 − r/c))` penalizes outputs shorter than the reference length `r`.

## Variants

There are many script-defined variants of BLEU; results are only comparable when computed by the same script. Both [[1409.3215-seq2seq]] and [[1706.03762-attention-is-all-you-need]] use `multi-bleu.pl` for cased BLEU on tokenized output, which reproduces the 33.30 SMT baseline of Schwenk 2014 on WMT'14 EN→FR.

## Reference numbers in this wiki (WMT'14)

| System | EN→FR | EN→DE |
|---|---|---|
| Phrase-based SMT baseline ([[1409.3215-seq2seq]] / Schwenk 2014) | 33.30 | — |
| Seq2seq LSTM ensemble of 5, B=12 ([[1409.3215-seq2seq]]) | 34.81 | — |
| Seq2seq LSTM rescoring of SMT 1000-best ([[1409.3215-seq2seq]]) | 36.5 | — |
| Best WMT'14 result (Durrani et al.) | 37.0 | — |
| Transformer base ([[1706.03762-attention-is-all-you-need]]) | 38.1 | 27.3 |
| Transformer big ([[1706.03762-attention-is-all-you-need]]) | 41.8 | 28.4 |

## Limits

BLEU correlates with human judgment well enough to drive a decade of MT progress but is known to under-rate fluent paraphrases that diverge lexically from references and to over-rate literal token-matching translations. Modern MT evaluation supplements it with COMET, chrF, and human evaluation.

## See also
- [[MachineTranslation]]
- [[SeqToSeq]]
- [[Transformer]]
