---
title: "dspy.Audio"
type: concept
tags: [dspy, primitive, audio, multimodal]
sources: [dspy-audio-tutorial, dspy-image-generation-prompting-tutorial]
last_updated: 2026-05-24
---

# dspy.Audio

`dspy.Audio` is [[DSPy]]'s first-class **audio primitive** — the type used inside [[DSPySignatures|Signatures]] to declare audio-bearing `InputField` / `OutputField`s. **First wiki receipt: [[dspy-audio-tutorial]]** (the dspy.ai *Audio* tutorial) builds two `dspy.Module` programs around it — a [[SpokenQA|spoken-QA]] program with `passage_audio: dspy.Audio = dspy.InputField()` and an [[EmotionGuidedTTS|emotion-guided TTS]] program that emits `dspy.Prediction(audio=dspy.Audio(...))` outputs.

Structural sibling to [[DSPyImage|`dspy.Image`]] in the wiki's multimodal-primitive taxonomy; the two non-text primitives use **opposite transport disciplines** — `dspy.Audio` stores base64-encoded WAV bytes in `data` (the wire shape is base64-inlined), while [[DSPyImage|`dspy.Image`]] stores a hosted URL and the wire shape is URL passthrough (`<image_url: https://...>`). The opposition tracks the common provenance of each modality: audio datasets deserialize into NumPy arrays that have no canonical URL, image generators return hosted URLs whose bytes do not need to travel. See [[dspy-image-generation-prompting-tutorial]] for the URL-passthrough disclosure on the image side.

## Construction paths

| Path | Source data | Use case |
|---|---|---|
| `dspy.Audio.from_array(array, sampling_rate)` | NumPy / list array + integer sampling rate | Decoding [[HuggingFace]] datasets where audio columns deserialize to `{"array": ndarray, "sampling_rate": int}` (e.g. [[SpokenSQuAD]] via `AudioLLMs/spoken_squad_test`). |
| `dspy.Audio(data=<base64-encoded WAV bytes>)` | Pre-encoded base64 | Round-trip through HTTP APIs (e.g. wrapping an OpenAI TTS response). |

The instance stores audio in `data` as base64-encoded WAV bytes. The canonical decode idiom (used by the [[dspy-audio-tutorial|tutorial]]'s [[Wav2Vec2]] metric):

```python
import base64, io, soundfile as sf, torch
audio_bytes = base64.b64decode(dspy_audio.data)
array, sr = sf.read(io.BytesIO(audio_bytes), dtype="float32")
tensor = torch.tensor(array).unsqueeze(0)
```

## Modality-axis status

- **InputField (audio-in)**: supported end-to-end via audio-capable LMs ([[GPT4oMiniAudio|`gpt-4o-mini-audio-preview-*`]]). The LM client handles base64 transport in the chat-completion request.
- **OutputField (audio-out)**: **not** first-class — [[dspy-audio-tutorial|the tutorial]] calls the [[GPT4oMiniTTS|`gpt-4o-mini-tts`]] HTTP endpoint *outside* the DSPy `LM` abstraction inside a manual `forward()` method and packs the bytes into a `dspy.Prediction(audio=dspy.Audio(...))`. DSPy's LM client does not multiplex audio-output endpoints as of the tutorial date.

## Optimizer constraints

- **[[MIPROv2]]'s [[DataAwareProposer|`data_aware_proposer`]] must be disabled** (`data_aware_proposer=False`) when any `InputField` is a `dspy.Audio` (or other non-textual modality) — the proposer's dataset summarizer cannot read audio bytes. First receipt: [[dspy-audio-tutorial]] §2.2.
- **Audio tokens dominate per-call cost** vs text. The tutorial recommends 0–2 few-shot examples (`max_bootstrapped_demos=2, max_labeled_demos=2`) and conservative `num_candidate_programs` settings.

## Tutorials

Tutorials that exercise this concept (roughly increasing depth):

- [[dspy-audio-tutorial]] — minting tutorial; first wiki receipt of `dspy.Audio.from_array(array, sampling_rate)` (decoding [[SpokenSQuAD]] [[HuggingFace]] audio columns into a `passage_audio: dspy.Audio = dspy.InputField()` for [[SpokenQA|spoken-QA]] against [[GPT4oMiniAudio|`gpt-4o-mini-audio-preview`]]) and of the **base64-WAV-bytes output path** wrapping [[GPT4oMiniTTS|`gpt-4o-mini-tts`]] in a manual `forward()` as `dspy.Prediction(audio=dspy.Audio(...))` for [[EmotionGuidedTTS|emotion-guided TTS]] over [[CREMAD]]; also mints the `data_aware_proposer=False` [[MIPROv2]] constraint for any Signature with a non-textual InputField, scored against a [[Wav2Vec2]] cosine-similarity metric.
- [[dspy-image-generation-prompting-tutorial]] — cross-reference receipt for the **opposite transport discipline**: the image-side `dspy.Image.from_url(...)` URL-passthrough wire shape (`<image_url: ...>` visible in `dspy.inspect_history`) is named as the structural foil for `dspy.Audio`'s base64-in-`data` storage path, and the [[FAL]]-hosted [[FluxPro|Flux Pro]] generator is named as the symmetric "non-`dspy.LM` HTTP service outside the LM abstraction" mirror of `dspy-audio-tutorial`'s OpenAI TTS wrapper.

## Connections

- [[DSPy]] / [[DSPySignatures]] / [[DSPyModules]] / [[DSPyPrediction]] — the primitive composes into the standard DSPy programming model.
- [[GPT4oMiniAudio]] — audio-input LM compatible with `dspy.Audio` InputFields.
- [[GPT4oMiniTTS]] — TTS endpoint wrapped manually to emit `dspy.Audio` outputs.
- [[Wav2Vec2]] — the audio encoder used to score `dspy.Audio` similarity in [[dspy-audio-tutorial]].
- [[SpokenSQuAD]] / [[CREMAD]] — datasets that decode into `dspy.Audio` via `from_array`.
- [[MIPROv2]] / [[BootstrapFewShotWithRandomSearch]] — optimizers exercised on audio programs with the `data_aware_proposer=False` / conservative-budget caveats.
- [[EmotionGuidedTTS]] — pattern for TTS-as-`dspy.Module` minted in [[dspy-audio-tutorial]].
- [[dspy-audio-tutorial]] — first wiki receipt.
