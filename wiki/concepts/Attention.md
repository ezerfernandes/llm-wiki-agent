---
title: "Attention"
type: concept
tags: [deep-learning, transformers]
sources: [d2l-attention-and-transformers, hands-on-llm-ch01-introduction-to-llms]
last_updated: 2026-05-23
---

# Attention

A mechanism letting a model weight different parts of its input dynamically when computing each output, replacing fixed-context bottlenecks in [[seqtoseq]] models. Foundational to [[selfattention]], [[multiheadattention]], and the [[transformer]] architecture introduced in [[AttentionIsAllYouNeed]]; computed via [[scaleddotproductattention]] with an [[AttentionMask]].

## From [[hands-on-llm-ch01-introduction-to-llms|*Hands-On LLMs* Ch 1]]

Ch 1 attributes attention to [[DzmitryBahdanau|Bahdanau]], [[KyunghyunCho|Cho]] & [[YoshuaBengio|Bengio]] 2014 (*"Neural Machine Translation by Jointly Learning to Align and Translate"*, arXiv:1409.0473) — introduced **before** the Transformer as a fix for the fixed-context-vector bottleneck in [[RNN]] encoder-decoder neural machine translation:

> "In 2014, a solution called attention was introduced that highly improved upon the original architecture. Attention allows a model to focus on parts of the input sequence that are relevant to one another ('attend' to each other) and amplify their signal. ... Attention selectively determines which words are most important in a given sentence." — Ch 1

The chapter's worked example: translating *"I love llamas"* → Dutch *"Ik hou van lama's"*. The attention between the input word *"llamas"* and the output word *"lama's"* is high; the attention between *"lama's"* and *"I"* is lower because they aren't as related. The chapter forward-references Ch 3 for the in-depth attention mechanism treatment.

Attention's payoff in this RNN+attention era: *"the hidden states of all input words are passed [to the decoder]"* — replacing the single context-vector bottleneck — but *"this sequential nature ... precludes parallelization during training of the model."* The [[transformer|Transformer]] (2017) resolves this by removing recurrence entirely.
