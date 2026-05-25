---
title: "Heaps' Law"
type: concept
tags: [information-retrieval, statistics, vocabulary-growth, power-law]
sources: [iir-ch05-index-compression]
last_updated: 2026-05-23
---

Empirical regularity describing how the vocabulary size of a text collection grows with the collection size:

$$M = k \cdot T^b$$

where $M$ is the number of distinct terms, $T$ is the total token count, and $k$, $b$ are corpus-dependent constants — typically $k \in [30, 100]$ and $b \approx 0.49$ on English newswire. **Implication**: vocabulary grows *sublinearly* — but it never saturates, even at web scale. A corpus 10× larger has roughly $\sqrt{10} \approx 3.2$× more distinct types.

Why it matters for IR:
- **Index-size planning**: dictionary memory grows as $T^{0.5}$ — affordable, but predictably non-bounded. Postings memory grows linearly in $T$.
- **OOV is permanent**: at any finite training corpus there will always be a long tail of unseen terms. Modern tokenization workarounds (BPE, [[SubwordEmbedding|subword embeddings]]) trade some vocab compactness for OOV robustness.
- **Compression headroom**: see [[DictionaryCompression]] for storing the $M$-term dictionary in ~$O(M \log L)$ bits where $L$ is average term length.

Named after Harold Stanley Heaps. Empirically inseparable from [[ZipfsLaw]] — both are power laws describing the same underlying phenomenon (some terms are dramatically more frequent than others) viewed from different angles: Zipf describes the *frequency* tail per type, Heaps describes the *count of types* as corpus grows. Full treatment in [[iir-ch05-index-compression]] §5.1.
