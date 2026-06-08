---
title: "Record sound (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, audio, digital-signal-processing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Record_sound
---

## Summary
This task asks the programmer to capture a monophonic 16-bit PCM audio stream and store it in memory, a file, or an array. The core challenge is interfacing with the platform's audio-capture API to digitize an analog signal into linear pulse-code-modulated samples. The task deliberately leaves the sample rate and signedness unspecified, so implementations may differ in their PCM format (e.g., signed vs. unsigned, 8000 Hz vs. 44100 Hz).

## Task Requirements
- Record sound from an audio input source.
- Use a monophonic (single-channel) signal.
- Encode samples as 16-bit PCM.
- Store the recording in memory, a file, or an array.
- Sample rate and sample signedness are left to the implementer.

## Language Coverage
29 languages implement this task, spanning systems languages, scripting languages, and BASIC dialects, since audio capture is inherently platform- and library-dependent. Representative implementations include C, C++, Ada, Go, Java, Python, Kotlin, OCaml, Common Lisp, and Tcl, alongside audio-specialized languages like ChucK.

## Connections
- [[PulseCodeModulation]] — the encoding scheme used to digitize the audio samples
- [[DigitalSignalProcessing]] — recording is the capture stage of audio DSP
- [[SampleRate]] — frequency at which the analog signal is sampled
- [[AudioIO]] — interfacing with platform sound-capture APIs

## Contradictions
- None — reference task page.
