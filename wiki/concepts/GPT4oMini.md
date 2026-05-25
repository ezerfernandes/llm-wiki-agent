---
title: "GPT-4o-mini"
type: concept
tags: [model, openai, gpt, vision, multimodal]
sources: [dspy-image-generation-prompting-tutorial]
last_updated: 2026-05-24
---

# GPT-4o-mini

`gpt-4o-mini` is [[OpenAI]]'s **small, vision-capable multimodal LLM** — the cost-efficient sibling of `gpt-4o`. Snapshot tag `gpt-4o-mini-2024-07-18` is the pinned variant used by several DSPy tutorials in the wiki (e.g. [[dspy-tutorial-games]]); the rolling alias `gpt-4o-mini` is the variant used by [[dspy-image-generation-prompting-tutorial]] for image-input critique.

Member of the broader [[GPT|GPT family]]; see [[GPT]] for the lineage. Sibling to [[GPT4oMiniAudio|`gpt-4o-mini-audio-preview-*`]] (audio-input variant) and [[GPT4oMiniTTS|`gpt-4o-mini-tts`]] (text-to-speech variant) in the wiki's GPT-4o-mini-modality-suffix taxonomy.

## In DSPy

- **As a critic LM with vision input** — [[dspy-image-generation-prompting-tutorial]] uses `dspy.LM(model="gpt-4o-mini", temperature=0.5)` as the critic in a [[IterativeImagePromptRefinement|critic-then-revise]] loop reading a [[DSPyImage|`dspy.Image`]] `InputField` (URL-passthrough wire shape via the [[DSPyAdapters|Adapter]]).
- **As a student / cost-efficient model** — [[dspy-tutorial-games]] fine-tunes `gpt-4o-mini-2024-07-18` via [[BootstrapFinetune]] using `gpt-4o` as the teacher; the fine-tuned `4o-mini` beats the `gpt-4o` zero-shot teacher on [[AlfWorld]] (71.5% vs 57.5%) at ~2.6× the wall-clock speed.
- **As a prompt-model for MIPROv2** — multiple tutorials (e.g. [[dspy-audio-tutorial]]) pin `prompt_model=gpt-4o-mini` as the prompt-proposer LM separate from the (often more expensive) task LM.

## Connections

- [[GPT]] — the family page.
- [[OpenAI]] — the provider.
- [[LiteLLM]] — DSPy's unified provider client; routes `gpt-4o-mini` calls.
- [[GPT4oMiniAudio]] / [[GPT4oMiniTTS]] — modality-suffixed siblings.
- [[DSPyLM]] — the DSPy abstraction that wraps `gpt-4o-mini` for use in Signatures.
- [[DSPyImage]] — `gpt-4o-mini` is a vision-capable LM that can consume `dspy.Image` InputFields.
- [[dspy-image-generation-prompting-tutorial]] — first wiki receipt of `gpt-4o-mini` as an explicit vision critic.
