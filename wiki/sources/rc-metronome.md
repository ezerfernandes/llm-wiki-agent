---
title: "Metronome (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, audio, timing, concurrency]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Metronome
---

## Summary
The task asks the programmer to build a working metronome that emits high and low audio beats accompanied by a visual beat indicator, with a configurable beat pattern (e.g. accent every N beats) and tempo. The central insight is decoupling concerns: sound production (which may use external players or sound files) must not block or distort the metronome's timing loop, so the beat scheduler needs accurate, non-interfering timekeeping.

## Task Requirements
- Produce high and low audio beats; playing sound files via an external player is acceptable.
- Sound playback must not interfere with the metronome's timing.
- Provide a visual beat indicator (e.g. a blinking red/green region for high/low beats); a terminal or graphical display is fine.
- Make both the beat pattern and the tempo configurable.
- If the language cannot output sound, a visual-only indicator is permissible.

## Language Coverage
44 languages implement this task. Coverage is broad, spanning systems and application languages alongside scripting and BASIC dialects, with representative entries including C, C++, C#, Java, Python, Go, Ruby, Perl, Haskell, Racket, and Pure Data.

## Connections
- [[RealTimeScheduling]] — beats must fire at precise tempo-derived intervals
- [[Concurrency]] — separating the timing loop from non-blocking sound playback
- [[Tempo]] — BPM configuration drives the inter-beat interval
- [[AudioSynthesis]] — generating or triggering high/low beat tones

## Contradictions
- None — reference task page.
