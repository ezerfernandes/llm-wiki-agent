---
title: "Dave Van Veen"
type: entity
tags: [researcher, stanford, clinical-nlp, medical-summarization]
sources: [2507.03152-medval]
last_updated: 2026-05-22
---

# Dave Van Veen

[[stanforduniversity|Stanford]] researcher in adapted-LLM clinical text summarization. **First author of "Adapted large language models can outperform medical experts in clinical text summarization"**, *Nature Medicine* 30(4):1134–1142, 2024 (ref [4] in [[2507.03152-medval]]) — the paper that **defined the canonical train/test splits** [[2507.03152-medval|MedVAL]] inherits for the [[Openi]] / [[ACIBench]] / [[MeQSum]]-derived tasks.

## Tracked contributions

- **Van Veen et al. (Nature Medicine 2024)** — first cross-task demonstration that adapted LLMs can outperform medical experts in clinical-text summarization across radiology, BHC, dialogue, and patient-query domains. Established the dataset splits subsequent MedVAL-Bench experiments use, ensuring **no overlap between MedVAL's `report2impression` and `report2simplified` train sets**.
- **[[2507.03152-medval|MedVAL (2026)]]** — co-author. The MedVAL pipeline operationalizes the question Van Veen 2024 raises: *if adapted LLMs can summarize, who validates the summaries before clinical use?*

## Connections

- [[2507.03152-medval]] — co-author.
- [[stanforduniversity]] — affiliation.
- [[Openi]] / [[ACIBench]] / [[MeQSum]] — Van Veen 2024 defined the splits used for these MedVAL-Bench tasks.
- [[AsadAali]] — fellow Stanford clinical-NLP researcher and MedVAL first author.
- [[MedicalTextValidation]] — the task family that picks up where Van Veen 2024's generation work leaves off.
