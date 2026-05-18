---
title: "Attention"
type: concept
tags: [deep-learning, transformers]
sources: [d2l-attention-and-transformers]
last_updated: 2026-05-16
---

# Attention

A mechanism letting a model weight different parts of its input dynamically when computing each output, replacing fixed-context bottlenecks in [[seqtoseq]] models. Foundational to [[selfattention]], [[multiheadattention]], and the [[transformer]] architecture introduced in [[AttentionIsAllYouNeed]]; computed via [[scaleddotproductattention]] with an [[AttentionMask]].
