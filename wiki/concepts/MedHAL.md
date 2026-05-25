---
title: "MedHAL"
type: concept
tags: [benchmark, medical-nlp, hallucination, prior-art, stub]
sources: [2507.03152-medval]
last_updated: 2026-05-22
---

# MedHAL

**Evaluation dataset for medical hallucination detection** — Mehenni & Zouaq, arXiv:2504.08596 (2025). Ref [35] in [[2507.03152-medval]].

Relies on **physician-error annotations limited to specific curated medical tasks**. [[2507.03152-medval]] §4 positions MedHAL as a representative of the "physician-in-the-loop supervision" family that MedVAL drops as a requirement — MedVAL trains its validators from synthetic generator-validator consistency signals without expert-labeled training data.

## Connections
- [[2507.03152-medval]] — the paper that contrasts itself with MedHAL.
- [[Hallucination]] — the failure mode targeted.
- [[MedVAL]] / [[MedVALBench]] — the self-supervised successor.
- [[MedicalTextValidation]] — the broader task family.
