---
title: "Speech Recognition"
type: concept
tags: [application-domain]
sources: [d2l-preface, d2l-introduction]
last_updated: 2026-05-16
---

# Speech Recognition

Automatic transcription of spoken language. Per [[d2l-preface]], one of the application areas where [[DeepLearning]] had its earliest industrial impact (alongside [[ComputerVision]]) before generalizing to other domains.

## Why it's hard ([[d2l-introduction]])

Audio is sampled at 8–16 kHz, so a single spoken word may span **thousands** of samples — there is no 1:1 correspondence between audio frames and characters/words. Speech recognition is a sequence-to-sequence problem where the **output is much shorter than the input**. The chapter's wake-word example illustrates the elementary case: 44,000-Hz mic → binary {yes, no} decision.

[[d2l-introduction]] cites Xiong-Wu-Alleva et al. 2018 as the milestone where speech-recognition accuracy reached **parity with humans** for certain applications.

## Connections

- [[DeepLearning]] — the toolkit that closed the human-parity gap.
- [[RNN]], [[lstm|LSTM]], [[transformer]] — successive architecture generations.
- [[machinetranslation]] — sister sequence-to-sequence task.
- Siri, Alexa, Google Assistant — consumer-facing deployments cited by the chapter.
- [[d2l-preface]], [[d2l-introduction]] — corpus anchors.
