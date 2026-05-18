---
title: "Context Vector"
type: concept
tags: [nlp, seq2seq, attention]
sources: []
last_updated: 2026-05-15
---

# Context Vector

The fixed-size summary an encoder passes to a decoder in classic [[seqtoseq]] models, or the attention-weighted sum produced per decoding step in [[Attention]]-based models. The bottleneck nature of the static version motivated the development of [[selfattention]] and the [[transformer]].
