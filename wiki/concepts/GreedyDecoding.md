---
title: "Greedy Decoding"
type: concept
tags: [decoding, inference, sequence-models]
sources: [d2l-recurrent-modern, ai-engineering-ch02-foundation-models, hands-on-llm-ch03-looking-inside-llms]
last_updated: 2026-05-23
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

## From [[ai-engineering-ch02-foundation-models|AI Engineering Ch 2]]

[[ChipHuyen|Chip Huyen]] frames greedy decoding as **the LLM-sampling baseline that's not quite right for open-ended generation**:

> "For a language model, greedy sampling creates boring outputs. Imagine a model that, for whatever question you ask, always responds with the most common words."

Ch 2 ties greedy decoding to **[[Temperature|temperature]] = 0** — technically temperature can never be zero (division by zero), but in practice T=0 is implemented as argmax over logits, skipping the softmax entirely. Ch 2's debugging tip: *"It's common practice to set the temperature to 0 for the model's outputs to be more consistent."*

This is the chapter's bridge between greedy decoding (a degenerate sampling strategy) and the broader [[Sampling]] section.

## From [[hands-on-llm-ch03-looking-inside-llms|*Hands-On LLMs* Ch 3]]

Ch 3 introduces greedy decoding as the LM-internals counterpart of this page's seq2seq formalization:

> "The easiest decoding strategy would be to always pick the token with the highest probability score. In practice, this doesn't tend to lead to the best outputs for most use cases. A better approach is to add some randomness and sometimes choose the second or third highest probability token." — Ch 3

> "Choosing the highest scoring token every time is called greedy decoding. It's what happens if you set the temperature parameter to zero in an LLM." — Ch 3

The chapter names the umbrella concept — **[[DecodingStrategy|decoding strategy]]** — and positions greedy as the baseline strategy that [[Sampling|sampling]] strategies depart from. Ch 6 of the same book is forward-referenced for the deeper coverage of [[Temperature|temperature]] and other sampling variants.
