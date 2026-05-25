---
title: "Beam Search"
type: concept
tags: [decoding, inference]
sources: [1409.3215-seq2seq, d2l-recurrent-modern, ai-engineering-ch02-foundation-models]
last_updated: 2024-12-04
---

# Beam Search

An approximate decoding algorithm for auto-regressive sequence models that maintains the top-B partial hypotheses at each step instead of greedily committing to the single best token. Given a model `p(y_t | y_{<t}, x)`, beam search extends each of the B running hypotheses with every possible next token, then keeps the B highest-log-probability extensions. A hypothesis is removed from the beam and added to the completed set as soon as it emits the end-of-sequence token.

## Why it works

Greedy decoding (B=1) commits to a locally best token that may be globally suboptimal. Increasing B gives the model a chance to recover from an early mistake. Tradeoff: compute scales linearly with B and the beam can collapse to near-duplicates.

[[1409.3215-seq2seq]] reports that for their LSTM translation system **B=2 captures most of the benefit of beam search**, and even B=1 already produces useful translations. Their best result uses B=12. Ensemble + beam interactions matter: an ensemble of 5 LSTMs at B=2 is cheaper than a single LSTM at B=12 and produces higher BLEU (34.50 vs 26.17).

## Length penalty (D2L formulation)

[[d2l-recurrent-modern]] §beam-search selects the final sequence as the one maximizing the **length-normalized** log-likelihood:

$$\frac{1}{L^\alpha} \log P(y_1, \ldots, y_L \mid \mathbf{c}) = \frac{1}{L^\alpha} \sum_{t'=1}^{L} \log P(y_{t'} \mid y_{<t'}, \mathbf{c}),$$

with $\alpha \approx 0.75$. Without the $L^\alpha$ penalty, longer sequences (more negative-log-prob terms) are systematically dispreferred; with $\alpha$, the score becomes length-comparable.

## Cost spectrum

[[d2l-recurrent-modern]] frames the three strategies as points on a single spectrum:

| Strategy | Cost | Optimality |
|---|---|---|
| [[GreedyDecoding\|Greedy]] (beam = 1) | $\mathcal{O}(\|\mathcal{Y}\|T')$ | Locally optimal, often globally suboptimal |
| Beam search | $\mathcal{O}(k\|\mathcal{Y}\|T')$ | Approximation tuned by $k$ |
| Exhaustive | $\mathcal{O}(\|\mathcal{Y}\|^{T'})$ | Globally optimal, intractable |

For $|\mathcal{Y}|=10000$, $T'=10$: greedy $10^5$, exhaustive $10^{40}$. Beam search at $k=5$ adds a 5× factor to the cheap regime.

## Variants

- **Pure beam search** as in [[1409.3215-seq2seq]].
- **Length-normalized beam search** — divide log-prob by a function of length to counter the bias toward short outputs.
- **Diverse / group beam search** — penalize repetition across beams.
- **Sampling-based alternatives** (top-k, top-p / nucleus) are now standard for open-ended generation in modern LLMs; beam search remains common for tasks with a well-defined "correct" output (translation, summarization).

## See also
- [[SeqToSeq]]
- [[EncoderDecoder]]
- [[GreedyDecoding]] — beam search with $k=1$.
- [[d2l-recurrent-modern]] — textbook exposition with length penalty + greedy/exhaustive comparison.

## From [[ai-engineering-ch02-foundation-models|AI Engineering Ch 2]]

[[ChipHuyen|Chip Huyen]] places beam search inside the [[TestTimeCompute|test-time compute]] family:

> "Instead of generating all outputs independently, which might include many less promising candidates, you can use beam search to generate a fixed number of most promising candidates (the beam) at each step of sequence generation."

In Ch 2's framing, beam search is **the structured alternative to [[bestofn|best-of-N]]** — instead of N independent draws and then picking, beam search prunes at every decode step to keep only the most-promising partial sequences. Trades exploration for exploitation along the sequence-generation axis.

For modern LLMs Ch 2 notes that **sampling-based alternatives ([[Topk|top-k]], [[Topp|top-p]] / nucleus)** are now standard for open-ended generation, while beam search remains common for tasks with well-defined "correct" output (translation, summarization).
