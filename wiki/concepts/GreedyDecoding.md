---
title: "Greedy Decoding"
type: concept
tags: [decoding, inference, sequence-models]
sources: [d2l-recurrent-modern]
last_updated: 2026-05-16
---

# Greedy Decoding

The simplest auto-regressive decoding strategy: at each time step $t'$, emit the token with the highest conditional probability under the model:

$$y_{t'} = \operatorname*{argmax}_{y \in \mathcal{Y}} P(y \mid y_1, \ldots, y_{t'-1}, \mathbf{c}).$$

Continue until the end-of-sequence token `<eos>` is emitted or the maximum length $T'$ is reached ([[d2l-recurrent-modern]] §beam-search).

## Cost

$\mathcal{O}(|\mathcal{Y}|T')$ — one softmax per step. *Miraculously cheap but far from optimal* (D2L). For $|\mathcal{Y}|=10000$ and $T'=10$ this is $10^5$ evaluations — vs. $10^{40}$ for exhaustive search.

## Why it isn't optimal

Greedy decoding chooses the locally most likely token *given the prefix it has committed to*. The globally most likely sequence may begin with a slightly less likely token whose continuation has much higher joint probability. D2L's worked example with vocabulary {A, B, C, `<eos>`}: greedy yields sequence probability $0.5\cdot 0.4\cdot 0.4\cdot 0.6 = 0.048$, but the alternative starting with the second-best token at step 2 yields $0.5\cdot 0.3\cdot 0.6\cdot 0.6 = 0.054$ — strictly better.

## Relationship to beam search

Greedy decoding is exactly **[[BeamSearch|beam search]] with beam size $k = 1$**. Beam search with $k > 1$ keeps multiple partial hypotheses to recover from locally-suboptimal choices.

## When to use

- **OK** for many open-ended generation tasks where a "good enough" continuation is acceptable.
- **OK** for short sequences where local and global optima often coincide.
- **Suboptimal** for tasks with a well-defined correct answer (translation, summarization) where small early errors compound — beam search is the standard there.

## See also
- [[BeamSearch]] — the $k > 1$ generalization.
- [[SeqToSeq]] / [[EncoderDecoder]] — primary deployment context.
- [[TeacherForcing]] — the training-time analog (where ground truth replaces argmax).
