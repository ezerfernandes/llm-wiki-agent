---
title: "Open-i"
type: concept
tags: [dataset, radiology, summarization, stub]
sources: [2507.03152-medval]
last_updated: 2026-05-22
---

# Open-i

**De-identified narrative chest x-ray reports** from the Indiana Network for Patient Care database. Ref [50] in [[2507.03152-medval]].

Used as the source for two [[MedVALBench]] tasks:
- **`report2impression`** — findings → impression. Train 500 / test 190; avg 50±22 tokens. **In-distribution.**
- **`report2simplified`** — findings → patient-friendly. Train 500 only (no test).

Train/test splits follow [[DaveVanVeen|Van Veen et al. 2024]] (ref [4]).

## Connections
- [[2507.03152-medval]] — the application paper.
- [[MedVALBench]] — uses Open-i for two radiology tasks.
- [[GREEN]] / [[ReXTrust]] / [[ReXErr]] / [[FineRadScore]] — sibling radiology evaluators in the prior-art landscape.
- [[DaveVanVeen]] — defined the canonical train/test splits.
