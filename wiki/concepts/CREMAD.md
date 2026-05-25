---
title: "CREMA-D (Crowd-sourced Emotional Multimodal Actors Dataset)"
type: concept
tags: [dataset, audio, emotion, speech, benchmark, tts]
sources: [dspy-audio-tutorial]
last_updated: 2026-05-24
---

# CREMA-D

**Crowd-sourced Emotional Multimodal Actors Dataset** — corpus of audio clips in which actors speak the same line with one of **six target emotions**: `neutral`, `happy`, `sad`, `anger`, `fear`, `disgust`. The fixed-line × variable-emotion design makes it a clean test bed for paralinguistic / emotion-style modeling because **content is held constant** across the emotion axis.

## Label set

```python
label_map = ['neutral', 'happy', 'sad', 'anger', 'fear', 'disgust']
```

Six classes; canonical multi-class emotion benchmark in the speech-emotion-recognition literature.

## Wiki receipts

- **[[dspy-audio-tutorial]]** — first wiki receipt. Used not as an emotion-classification benchmark but **inverted**: the tutorial uses CREMA-D's `(raw_line, emotion_label, reference_audio)` triplets as training data for [[EmotionGuidedTTS|emotion-guided TTS]] — given a target emotion and a line, generate audio that sounds like CREMA-D's reference for that (line, emotion). The reference audio acts as the gold target for a [[Wav2Vec2|Wav2Vec 2.0]] cosine-similarity metric. Headline: optimized TTS instructions lift similarity from **~0.57 → ~0.67**.

## Standard split

The tutorial does not pin a canonical split — uses ad-hoc train/eval slices via `dspy.datasets.DataLoader`. The dataset's classical use is *classification* (audio → emotion label), but the tutorial inverts it to *generation* (emotion label + line → audio) — a non-standard use direction.

## Connections

- [[DSPyAudio]] — the primitive encoding both the reference and the generated audio.
- [[EmotionGuidedTTS]] — the prompt-optimization pattern minted on this dataset in [[dspy-audio-tutorial]].
- [[Wav2Vec2]] — the embedding model used for the similarity metric.
- [[GPT4oMiniTTS]] — the TTS endpoint whose `instructions=` parameter is optimized against this dataset.
- [[MIPROv2]] — the optimizer used.
- [[CosineSimilarity]] — the scoring reduction over Wav2Vec2 embeddings.
- [[dspy-audio-tutorial]] — first wiki receipt.
