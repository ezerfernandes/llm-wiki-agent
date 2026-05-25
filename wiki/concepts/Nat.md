---
title: "Nat (natural-log unit)"
type: concept
tags: [information-theory, units, language-modeling]
sources: [ai-engineering-ch03-evaluation-methodology]
last_updated: 2024-12-04
---

# Nat

The **nat** is the unit of [[Entropy|entropy]] and [[CrossEntropy|cross entropy]] when the natural logarithm is used as the base instead of `log₂`. One nat = `log₂(e)` ≈ 1.44 bits.

## Why ML frameworks use nats

Per [[ai-engineering-ch03-evaluation-methodology|*AI Engineering* Ch 3]], *"Popular ML frameworks, including TensorFlow and PyTorch, use nat (natural log) as the unit for entropy and cross entropy."* The mathematical convenience: *"the derivative of natural log `ln(x)` is `1/x`"* — a cleaner gradient than `log₂(x)`'s `1/(x ln 2)`.

## Effect on perplexity formula

The unit choice changes the exponential base of perplexity:

- **Bits (base-2):** `PPL = 2^H`
- **Nats (base-e):** `PPL = e^H`

Ch 3 notes that *"due to the confusion around bit and nat, many people report perplexity, instead of cross entropy, when reporting their language models' performance"* — because perplexity is dimensionless once exponentiated, it dodges the bit/nat ambiguity.

## In practice

If a paper reports cross entropy = 1.4 without specifying units, the corresponding perplexity could be `2^1.4 ≈ 2.64` (bits) or `e^1.4 ≈ 4.06` (nats) — a factor-of-1.5 ambiguity. PyTorch's `F.cross_entropy` returns nats by default.

## Connections

- [[ai-engineering-ch03-evaluation-methodology]] — primary source.
- [[CrossEntropy]] / [[Entropy]] — the quantities the nat units.
- [[Perplexity]] — `e^H` in nats, `2^H` in bits.
- [[BitsPerByte]] / [[BitsPerCharacter]] — the bit-based normalizations.
- [[CrossEntropyLoss]] — PyTorch's `F.cross_entropy` returns nats.
