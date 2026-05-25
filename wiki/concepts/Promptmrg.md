---
title: "Promptmrg"
type: concept
tags: [stub, radiology, mllm, ddp]
sources: [2408.08849-ecg-chat]
last_updated: 2026-05-22
---

# Promptmrg

*Stub — referenced by ECG-Chat as the radiology precedent for [[DiagnosisDrivenPrompt|DDP]].*

**Jin, Che, Yin & Chen (AAAI 2024) — *"Promptmrg: Diagnosis-driven prompts for medical report generation."*** Introduces the **classifier-into-prompt** pattern: a separate disease classifier produces text-rendered diagnostic facts that are prepended to the LLM's report-generation prompt. [[2408.08849-ecg-chat|ECG-Chat]] adapts this directly for the ECG modality.

## Connections
- [[2408.08849-ecg-chat]] — extends Promptmrg's pattern to ECG.
- [[DiagnosisDrivenPrompt]] — the technique itself.
- [[Diallama]] — sibling radiology-MLLM with similar diagnosis-driven prompting.
