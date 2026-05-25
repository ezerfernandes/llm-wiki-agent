---
title: "gpt-4o-mini-audio (Audio-Input Model)"
type: concept
tags: [model, openai, llm, audio, multimodal, gpt4o]
sources: [dspy-audio-tutorial]
last_updated: 2026-05-24
---

# gpt-4o-mini-audio

[[openai|OpenAI]]'s **audio-input variant of GPT-4o-mini** — the smaller, cheaper sibling of `gpt-4o-audio-preview` capable of consuming **audio in the chat-completion `messages` array** alongside text. The wiki's first receipt pins the specific dated snapshot **`gpt-4o-mini-audio-preview-2024-12-17`**.

## Modality surface

- **Inputs**: text + audio (audio passed as base64-encoded WAV bytes inside the chat-completion request).
- **Outputs**: text only (this is **not** a TTS model — the speech-out sibling is [[GPT4oMiniTTS|`gpt-4o-mini-tts`]]).

## Wiki receipts

- **[[dspy-audio-tutorial]]** — first wiki receipt. Powers the [[SpokenQA|spoken-QA]] program over [[SpokenSQuAD]]:

  ```python
  dspy.configure(lm=dspy.LM(model='gpt-4o-mini-audio-preview-2024-12-17'))
  spoken_qa = dspy.ChainOfThought(SpokenQASignature)
  ```

  Compatible out of the box with [[DSPyAudio|`dspy.Audio`]] InputFields via [[DSPyLM|`dspy.LM`]] / [[LiteLLM]] transport. Tutorial reports ~10% absolute improvement from [[BootstrapFewShotWithRandomSearch]] / [[MIPROv2]] optimization on Spoken-SQuAD.

## Cost note

The [[dspy-audio-tutorial|tutorial]] flags *"audio tokens can be costly"* and recommends conservative optimizer budgets (0–2 few-shot examples, low `num_candidate_programs`). Audio tokenization rates exceed text tokenization on a per-second basis.

## Connections

- [[openai|OpenAI]] — provider.
- [[GPT4]] / [[GPT35Turbo]] — sibling lineage; this is the audio-input variant of the GPT-4o family.
- [[DSPyAudio]] — the primitive this model consumes on InputFields.
- [[DSPyLM]] / [[LiteLLM]] — the client layer that transports base64 audio.
- [[SpokenSQuAD]] / [[SpokenQA]] — the benchmark + task pattern of the first receipt.
- [[GPT4oMiniTTS]] — the TTS sibling for audio outputs (separate endpoint).
- [[dspy-audio-tutorial]] — first wiki receipt.
