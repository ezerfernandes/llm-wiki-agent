---
title: "ACI-Bench"
type: concept
tags: [dataset, medical-nlp, dialogue, summarization, stub]
sources: [2507.03152-medval]
last_updated: 2026-05-22
---

# ACI-Bench

**Ambient Clinical Intelligence Benchmark** — Yim, Fu, Ben Abacha, Snider, Lin & Yetisgen, *Scientific Data* 10(1):586, 2023. Refs [53-55] in [[2507.03152-medval]]. Same first-author family as [[MEDCON]] (which originates from the AciBench data).

Provides:
1. 207 doctor-patient conversations.
2. Corresponding patient visit notes.

Used in [[MedVALBench]] as the source for the **`dialogue2note`** task: doctor-patient dialogue → SOAP-style "assessment and plan" note. Out-of-distribution test only, **85 test samples**, **avg 1,497±445 tokens — the longest task** in the benchmark. **2 physicians** annotated. Sampled from the test split defined by [[DaveVanVeen|Van Veen et al. 2024]].

Despite the longest input context and zero training overlap, MedVAL distillation displays **strong improvements** on dialogue2note (e.g. Llama-3.2-3B: 0.146 → 0.448, **+207%**; GPT-4o Mini: 0.586 → 0.692, **+18%**).

## Connections
- [[2507.03152-medval]] — the application paper.
- [[MedVALBench]] — uses ACI-Bench for dialogue2note.
- [[MEDCON]] — clinical-NLP metric originating from the same data family.
- [[DaveVanVeen]] — defined the canonical splits used here.
