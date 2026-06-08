---
title: "Logits"
type: concept
tags: [neural-networks, classification, softmax, deep-learning]
sources: [mlsysbook-ch05-neural-computation]
last_updated: 2026-06-05
---

# Logits

Short for "log-odds units" — the raw, unnormalized real-valued scores a network's output layer produces *before* [[Softmax|softmax]] turns them into probabilities. Per [[mlsysbook-ch05-neural-computation|mlsysbook Vol 1 Ch 5]], logits preserve the relative ordering of class evidence.

## Systems consequence

Because **argmax over logits and argmax over softmax probabilities always select the same class**, optimized inference pipelines **skip the softmax computation entirely when only the top prediction is needed**, saving K exponentiations per sample. Logits are also where the [[Softmax|softmax]] numerical-stability hazard lives: a logit greater than ~88 overflows standard FP32 during exponentiation, producing a silent NaN — mitigated by the log-sum-exp trick (subtract the max logit before exponentiating).

## Connections

- [[Softmax]] — normalizes logits into a probability distribution.
- [[CrossEntropy]] — the loss applied over softmax(logits) vs [[OneHotEncoding|one-hot]] labels.
- [[Inference]] — where the skip-softmax optimization applies.
- [[FP32]] / [[NumericalRepresentation]] — the overflow context.
- [[mlsysbook-ch05-neural-computation]] — source.
