---
title: "plasTeX"
type: concept
tags: [stub, tool, latex, document-generation]
sources: [2408.08849-ecg-chat]
last_updated: 2026-05-22
---

# plasTeX

*Stub — LaTeX-pipeline tool used by ECG-Chat.*

**Smith (GitHub, accessed 2024-08-11) — *"plasTeX Documentation."*** A Python LaTeX document-processing framework. Used by [[2408.08849-ecg-chat|ECG-Chat]] (Appendix C) to render structured ECG diagnostic reports from a template with six sections: Patient Information / Medical History / ECG Data Analysis / Pathological Analysis / Diagnosis / Recommendations. The pipeline takes LLM-generated content + classifier outputs + retrieved knowledge and produces a single typeset report (Figures 5 & 6 in the paper).

The LaTeX template is the third critic in ECG-Chat's hallucination-mitigation stack (after GraphRAG knowledge and DDP classifier facts) — it imposes a fixed structural form on the output.

## Connections
- [[2408.08849-ecg-chat]] — primary user; powers the structured-report pipeline.
- [[LLMModuloFramework]] — the LaTeX template plays the *format critic* role.
