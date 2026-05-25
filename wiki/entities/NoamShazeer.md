---
title: "Noam Shazeer"
type: entity
tags: [person, researcher, transformer, google]
sources: [hands-on-llm-ch03-looking-inside-llms]
last_updated: 2026-05-23
---

# Noam Shazeer

Co-author of the original [[1706.03762-attention-is-all-you-need|*Attention Is All You Need*]] paper (Vaswani et al., 2017) and a recurring author of transformer-efficiency improvements cited across [[hands-on-llm-ch03-looking-inside-llms|*Hands-On LLMs* Ch 3]]:

- **Multi-Query Attention** — *"Fast transformer decoding: One write-head is all you need"* (2019). The K/V-shared-across-heads attention variant; basis for [[multiqueryattention|MQA]].
- **SwiGLU and other GLU variants** — *"GLU Variants Improve Transformer"*. The gated-activation family that replaces ReLU in modern LLMs; see [[SwiGLU]].
- **Sparsely-gated mixture-of-experts** — *"Outrageously Large Neural Networks"* (Shazeer et al., 2017). The MoE layer cited on the [[MixtureOfExperts|MoE concept page]].

## Connections

- [[1706.03762-attention-is-all-you-need]] — co-author of the original Transformer paper.
- [[multiqueryattention]] — author of the MQA paper.
- [[SwiGLU]] — author of the GLU-variants paper.
- [[MixtureOfExperts]] — author of the sparsely-gated MoE paper.
- [[transformer]] — the architecture his work has repeatedly extended.
- [[hands-on-llm-ch03-looking-inside-llms|*Hands-On LLMs* Ch 3]] — citation context.
