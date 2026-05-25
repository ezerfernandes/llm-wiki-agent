---
title: "Diagnosis-Driven Prompt (DDP)"
type: concept
tags: [prompt-engineering, medical, classifier-into-prompt, ecg-chat]
sources: [2408.08849-ecg-chat]
last_updated: 2026-05-22
---

# Diagnosis-Driven Prompt (DDP)

A **classifier-into-prompt** technique for grounding MLLM medical report generation. Originally developed for radiology (Promptmrg, Dia-LLaMA), adapted to ECG by [[2408.08849-ecg-chat|ECG-Chat]].

**The DDP recipe** (ECG version):
1. Run a **linear classifier** on the [[ECGEncoder]]'s output feature vector, producing SCP-Code probabilities for ~40 disease + form + rhythm labels.
2. Group labels into three categories (Disease, Form, Rhythm) and threshold each. Include any disease/form label above threshold; treat rhythm as single-label (top-1).
3. Render the surviving labels as **English-sentence facts**: *"The {label description} is present."* — e.g. *"Sinus rhythm is present; Left bundle branch block is present."*
4. **Insert these sentences into the LLM prompt** before the report-generation instruction.

DDP is structurally a [[LLMModuloFramework|generate-test-critique]] move: a deterministic classifier supplies the *test* output, and the LLM is forced to write a report consistent with it. Without DDP, [[Vicuna13B]] *"prefers only a few specific responses"* and ignores rare labels.

## Empirical effect (Table II, [[2408.08849-ecg-chat|ECG-Chat]])

Same model, same data, same evaluation; the only delta is whether the DDP block is in the prompt:

| | CE-Disease F1 | CE-Form F1 | CE-Rhythm F1 | BLEU-1 | BLEU-4 | ROUGE-L | METEOR |
|---|---|---|---|---|---|---|---|
| ECG-Chat (no DDP) | 1.76 | 0.98 | 13.04 | 15.91 | 2.32 | 23.87 | 29.39 |
| **ECG-Chat (+ DDP)** | **22.33** | **17.35** | **43.39** | **32.27** | **11.19** | **29.93** | **35.10** |

DDP roughly **doubles BLEU and triples Rhythm F1**. The paper concedes recall remains low on rare labels — DDP fixes refusal-to-mention but not classifier accuracy.

## Connections
- [[2408.08849-ecg-chat]] — the ECG instantiation; paper Figure 2(a) is the canonical diagram.
- [[Promptmrg]] / [[Diallama]] — the radiology predecessors.
- [[LLMModuloFramework]] — DDP is the *deterministic classifier-as-critic* pattern, applied at prompt-construction time rather than post-hoc verification.
- [[Hallucination]] — the failure mode DDP mitigates (LLM ignoring rare diagnoses).
- [[ECGEncoder]] — the feature source for the DDP classifier.
