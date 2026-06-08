---
title: "Forced Alignment"
type: concept
tags: [ml-systems, mlsysbook, data-engineering, speech, labeling]
sources: [mlsysbook-ch04-data-engineering]
last_updated: 2026-06-05
---

# Forced Alignment

A speech-processing technique that, given a **known** transcription, aligns specific words to audio frames with millisecond precision using dynamic programming (the Viterbi algorithm), bypassing the harder problem of recognizing what was said (Reddi, [[mlsysbook-ch04-data-engineering|Vol 1, Ch 4]]).

This distinction is what makes automated [[KeywordSpotting|KWS]] corpus construction feasible: because the transcription is already known from paired text, forced alignment converts sentence-level audio into word-level training samples at near-zero marginal cost. It is the engine behind the **Multilingual Spoken Words Corpus (MSWC)** — 23.4M one-second examples, 340K keywords, 50 languages. Manual labeling at 10 s/example would take ~65,000 hours ≈ 32+ person-years; forced alignment makes it automatic.

The extraction system uses the timing markers to generate clean keyword samples while handling background noise, speakers stretching/compressing words beyond the 500–800 ms target duration, and words exceeding the one-second boundary.

## Connections

- [[KeywordSpotting]] — the workload it enables at corpus scale.
- [[DataLabeling]] / [[AIAssistedLabeling]] — automated labeling context.
- [[MFCC]] / [[Spectrogram]] — the audio features the aligned samples become.
- [[mlsysbook-ch04-data-engineering]] — source.
