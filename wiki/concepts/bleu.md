---
title: "BLEU"
type: concept
tags: [evaluation, machine-translation, metric]
sources: [1409.3215-seq2seq, 1706.03762-attention-is-all-you-need, d2l-recurrent-modern, hands-on-llm-ch12-fine-tuning-generation-models]
last_updated: 2026-05-24
---

# BLEU

**Bilingual Evaluation Understudy** — an automatic metric for machine translation introduced by [[KishorePapineni|Papineni]] et al. (ACL 2002). BLEU measures the modified n-gram precision of a candidate translation against one or more reference translations, multiplied by a brevity penalty to discourage short outputs. Scores range 0–100; higher is better.

## D2L formulation

[[d2l-recurrent-modern]] §seq2seq gives the explicit form

$$\textrm{BLEU} = \exp\left(\min\left(0, 1 - \frac{\textrm{len}_\textrm{label}}{\textrm{len}_\textrm{pred}}\right)\right) \prod_{n=1}^k p_n^{1/2^n},$$

where $p_n$ = ratio of matched $n$-grams to total $n$-grams in the prediction, and $k$ = longest $n$-gram for matching. Two pedagogical observations from D2L: (i) the score is 1 iff prediction equals target; (ii) the exponent $1/2^n$ gives **higher weight to longer $n$-gram matches** (since $p_n^{1/2^n}$ increases in $n$ when $p_n$ is fixed near 1); (iii) the leading exponential factor is the **brevity penalty** — for target length 6 and prediction length 2 with $p_1 = p_2 = 1$, the penalty is $\exp(1 - 3) \approx 0.14$, collapsing BLEU.

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

## Beyond MT — generation evaluation

BLEU is reused outside MT as one component of generation-evaluation reward composites, often alongside semantically-richer metrics that cover its blind spots:

- **[[2025-bionlp-archehr-qa-neural|ArchEHR-QA 2025 (Neural)]]** uses BLEU + [[ROUGE]] + [[SARI]] + [[BERTScore]] + [[AlignScore]] + [[MEDCON]] (six-metric mean) as the Stage-2 [[MIPROv2]]-optimized [[EvidenceGroundedQA|clinical-QA]] reward.

## From [[hands-on-llm-ch12-fine-tuning-generation-models|Hands-On LLMs Ch 12]]

Ch 12 of *Hands-On LLMs* names BLEU (Papineni et al. 2002) as one of **four canonical word-level metrics** for generative-LLM evaluation — alongside [[Perplexity]], [[ROUGE]], and [[BERTScore]]. The chapter's caveat applies in full: *"They do not account for consistency, fluency, creativity, or even correctness of the generated text."* Ch 12's evaluation discipline pivots from word-level metrics to **public benchmarks** ([[MMLU]] / [[GSM8K]] / [[HellaSwag]] / [[TruthfulQA]] / [[HumanEval]]), then [[LLMAsAJudge|LLM-as-a-judge]], then human evaluation via [[ChatbotArena|Chatbot Arena]].

## See also
- [[MachineTranslation]]
- [[SeqToSeq]]
- [[Transformer]]
- [[KishorePapineni]] — BLEU author.
- [[d2l-recurrent-modern]] — textbook exposition + reference Python implementation.
- [[ROUGE]] / [[SARI]] / [[BERTScore]] / [[AlignScore]] / [[MEDCON]] — sibling generation metrics often co-reported with BLEU.
- [[2025-bionlp-archehr-qa-neural]] — clinical-QA reward-composite application.
