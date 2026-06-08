---
title: "Speech synthesis (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, audio, text-to-speech]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Speech_synthesis
---

## Summary
This task asks the programmer to render the fixed text "This is an example of speech synthesis" as audible speech. The key insight is that this is rarely solved from scratch — solutions almost always shell out to a platform text-to-speech (TTS) engine or library (e.g. `say` on macOS, SAPI on Windows, `espeak`/`festival` on Linux), so the core challenge is interfacing with the host system's speech facility rather than implementing synthesis algorithms.

## Task Requirements
- Render the literal text "This is an example of speech synthesis" as speech (audio output).

## Language Coverage
48 languages implement this task, spanning systems languages, scripting languages, and many BASIC dialects that target specific platform speech APIs. Representative implementations include C, C#, Go, Haskell, Python, Perl, Ruby, JavaScript, PowerShell, and Tcl.

## Connections
- [[TextToSpeech]] — the core capability being exercised
- [[SpeechSynthesis]] — the named technique this task demonstrates
- [[AudioOutput]] — solutions must produce playable sound
- [[ForeignFunctionInterface]] — many solutions bind to native OS speech APIs (SAPI, NSSpeechSynthesizer)

## Contradictions
- None — reference task page.
