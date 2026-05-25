---
title: "VeriFact"
type: concept
tags: [evaluation, factuality, ehr, retrieval, prior-art, stub]
sources: [2507.03152-medval]
last_updated: 2026-05-22
---

# VeriFact

**Verifying facts in LLM-generated clinical text using electronic health records** — Chung, Swaminathan, Goodell et al., arXiv:2501.16672 (2025). Ref [37] in [[2507.03152-medval]].

**Retrieval-based factuality verification** — pulls evidence statements from EHR data to verify generated claims. [[2507.03152-medval]] §4 positions VeriFact as a **retrieval-dependent method oriented toward multi-document summarization** that *"lacks the capability to train LMs."* MedVAL drops the retrieval dependency and adds the LM-training pipeline.

## Connections
- [[2507.03152-medval]] — the paper that contrasts with VeriFact.
- [[MedVAL]] — the LM-trainable, retrieval-free successor.
- [[MedicalTextValidation]] — the task family.
- [[MIMIC]] — EHR data source family relevant to both.
