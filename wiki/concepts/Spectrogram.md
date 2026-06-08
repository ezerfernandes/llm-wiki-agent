---
title: "Spectrogram"
type: concept
tags: [ml-systems, mlsysbook, audio, speech, features]
sources: [mlsysbook-ch04-data-engineering]
last_updated: 2026-06-05
---

# Spectrogram

A 2D image-like representation of audio (horizontal axis = time, vertical = frequency, color intensity = signal energy) computed via the Short-Time Fourier Transform (STFT), used to repurpose image-based CNNs for audio processing (Reddi, [[mlsysbook-ch04-data-engineering|Vol 1, Ch 4]]).

Converting a 1D waveform into a visual format lets standard convolutional architectures process speech. This repurposing creates a rigid dependency: any mismatch in STFT parameters (e.g., a 25 ms vs 30 ms window) between training and serving invalidates the learned patterns and causes performance to collapse — a concrete case of the [[TrainingServingConsistency|consistency imperative]]. Spectrograms are an intermediate step toward the more compact [[MFCC]] representation in the [[KeywordSpotting|KWS]] pipeline.

## Connections

- [[MFCC]] — the further-compressed representation.
- [[KeywordSpotting]] — the audio workload.
- [[TrainingServingConsistency]] — STFT parameter matching is mandatory.
- [[mlsysbook-ch04-data-engineering]] — source.
