---
title: "MedicationQA"
type: concept
tags: [dataset, medical-nlp, question-answering, stub]
sources: [2507.03152-medval]
last_updated: 2026-05-22
---

# MedicationQA

**Medication-related consumer health Q&A dataset** — Abacha et al. Real-world questions sent to the U.S. National Library of Medicine about medications, paired with expert-written answers. Ref [48] in [[2507.03152-medval]].

Used as the **`medication2answer`** task source in [[MedVALBench]]: medication question → answer. Train 500 / test 135; avg 10±4 tokens. **In-distribution** for the MedVAL training set.

Unlike other MedVAL-Bench tasks, the **input (standalone question) often lacks sufficient context to validate the output** — this is the closest task in the suite to QA where the LM's knowledge base, not the input, must support the answer. MedVAL shows improved physician alignment on this task even so, suggesting the trained validator can leverage the underlying LM's knowledge to assess outputs.

## Connections
- [[2507.03152-medval]] — the application paper.
- [[MedVALBench]] — uses MedicationQA for the medication2answer task.
- [[MedicalTextValidation]] — the task family.
