---
title: "Spoken-SQuAD"
type: concept
tags: [dataset, audio, qa, benchmark, multimodal]
sources: [dspy-audio-tutorial]
last_updated: 2026-05-24
---

# Spoken-SQuAD

**Spoken question-answering benchmark** — audio-input variant of [[SQuAD|Stanford Question Answering Dataset]] where the **passage is delivered as a speech recording** rather than text. The hosted variant the wiki first encounters is `AudioLLMs/spoken_squad_test` on [[HuggingFace]] — three fields (`context`, `instruction`, `answer`) with `context` being a `{"array": ndarray, "sampling_rate": int}` audio object and `instruction` / `answer` plain text.

## Dataset fields (HuggingFace `AudioLLMs/spoken_squad_test`)

| Field | Type | Role |
|---|---|---|
| `context` | `{"array": ndarray, "sampling_rate": int}` | Audio recording of the passage — converted to [[DSPyAudio|`dspy.Audio`]] via `dspy.Audio.from_array(x.context["array"], x.context["sampling_rate"])`. |
| `instruction` | `str` | The question asked of the audio passage. |
| `answer` | `str` | Gold short-form factoid answer (1–5 words, evaluated by [[ExactMatch|exact match]]). |

## Wiki receipts

- **[[dspy-audio-tutorial]]** — first wiki receipt. Builds `dspy.ChainOfThought(SpokenQASignature)` over the dataset with [[GPT4oMiniAudio|`gpt-4o-mini-audio-preview-2024-12-17`]] as the audio-input task LM. **Headline lift: ~10% absolute** from [[BootstrapFewShotWithRandomSearch]] and [[MIPROv2]] (the latter requires `data_aware_proposer=False`).

## Relationship to [[SQuAD]]

Spoken-SQuAD shares the **passage + question + extractive-answer** structure of [[SQuAD]] but adds the speech-recognition burden to the task LM. Text-based SQuAD measures reading comprehension; Spoken-SQuAD measures end-to-end **speech understanding + reading comprehension** in a single model, distinguishing audio-native LLMs ([[GPT4oMiniAudio]]) from cascaded ASR-then-LLM pipelines.

## Connections

- [[SQuAD]] — text progenitor.
- [[DSPyAudio]] — the primitive used to encode `context`.
- [[GPT4oMiniAudio]] — the audio-input task LM in the wiki's first receipt.
- [[HuggingFace]] — dataset host.
- [[dspy-audio-tutorial]] — first wiki receipt.
- [[QuestionAnswering]] — broader task class.
- [[SpeechRecognition]] — implicit prerequisite for end-to-end audio-LLM solutions.
