---
title: "MFCC (Mel-Frequency Cepstral Coefficients)"
type: concept
tags: [ml-systems, mlsysbook, audio, speech, features]
sources: [mlsysbook-ch04-data-engineering]
last_updated: 2026-06-05
---

# MFCC (Mel-Frequency Cepstral Coefficients)

A compact audio feature representation that distills raw waveforms into a handful of speech-relevant coefficients, used as the standard input transform for [[KeywordSpotting|KWS]] models (Reddi, [[mlsysbook-ch04-data-engineering|Vol 1, Ch 4]]).

MFCCs apply mel-scale filtering that selectively emphasizes the frequencies humans use to distinguish speech, reducing thousands of raw samples in a small time window (e.g., 25 ms) to just 13–39 coefficients — the aggressive dimensionality reduction required for always-on, kilobyte-scale hardware. The KWS design space trades 13 vs 40 coefficients: +3–5% accuracy for 3× feature compute and memory; the 64 KB always-on island forces 13.

Any mismatch in the transformation parameters (FFT window size, hop length, coefficient count) between training and serving creates **feature skew** that collapses accuracy — which is why [[DeterministicTransformation|deterministic]] processing versions these parameters with the code, and the [[TrainingServingConsistency|consistency imperative]] applies directly.

## Connections

- [[Spectrogram]] — the intermediate 2D representation MFCCs compress further.
- [[KeywordSpotting]] — the workload that consumes MFCCs.
- [[TrainingServingConsistency]] / [[DeterministicTransformation]] — why parameters must match.
- [[ForcedAlignment]] — produces the samples MFCCs are computed on.
- [[mlsysbook-ch04-data-engineering]] — source.
