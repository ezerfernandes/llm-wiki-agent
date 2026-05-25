---
title: "Wav2Vec 2.0"
type: concept
tags: [model, speech, self-supervised, audio, encoder, meta, fair]
sources: [dspy-audio-tutorial]
last_updated: 2026-05-24
---

# Wav2Vec 2.0

**Self-supervised speech representation model** from [[meta|Meta]] FAIR (Baevski, Zhou, Mohamed & Auli, NeurIPS 2020) — pretrains a transformer audio encoder via a [[ContrastiveLearning|contrastive]] objective over masked quantized latents on unlabeled speech, fine-tunes on a small amount of labeled ASR data. The architecture's broader use in 2026 is as a **general-purpose speech encoder** whose intermediate hidden states are used as features for downstream tasks (classification, similarity, probing) without further fine-tuning.

## Wiki receipts

- **[[dspy-audio-tutorial]]** — first wiki receipt. **Not** used for ASR; used as a **frozen audio encoder for a similarity metric** in the [[EmotionGuidedTTS|emotion-guided TTS]] §3 task. The tutorial loads the base variant via `torchaudio.pipelines.WAV2VEC2_BASE.get_model().eval()` and computes a mean-pooled embedding to score generated audio against reference audio:

  ```python
  bundle = torchaudio.pipelines.WAV2VEC2_BASE
  model = bundle.get_model().eval()

  def extract_embedding(audio_tensor):
      with torch.inference_mode():
          return model(audio_tensor)[0].mean(dim=1)

  score = cosine_similarity(ref_embed, gen_embed)
  ```

  The metric returns `score > 0.8` when called inside a `trace`-context (DSPy optimizer-bootstrap branch) and the raw cosine otherwise (evaluation branch). Tutorial honest about the choice: *"audio reference comparisons is generally a non-trivial task due to subjective variations of evaluating speech, especially with emotional expression"* — Wav2Vec2 is a phonetic-content encoder, not an emotion encoder; a stronger paralinguistic-emotion encoder would likely give better metric signal.

## torchaudio bundle path

`torchaudio.pipelines.WAV2VEC2_BASE` ships the pretrained-only base variant (no labeled ASR fine-tune layer) — the right entry point when using Wav2Vec2 as a feature extractor rather than a transcriber. Sibling bundles in `torchaudio.pipelines.*` add ASR heads.

## Connections

- [[meta|Meta]] FAIR — origin.
- [[SelfSupervisedLearning]] / [[ContrastiveLearning]] — pretraining paradigm.
- [[Transformer]] — backbone architecture.
- [[SpeechRecognition]] — the task the original paper benchmarks (the wiki's first receipt uses it for a different task).
- [[CosineSimilarity]] — the reduction the [[dspy-audio-tutorial|tutorial]] uses over the embeddings.
- [[DSPyAudio]] — the primitive encoding both inputs to the metric.
- [[CREMAD]] — the dataset whose reference + generated audio are scored.
- [[EmotionGuidedTTS]] — the pattern the metric services.
- [[dspy-audio-tutorial]] — first wiki receipt.
