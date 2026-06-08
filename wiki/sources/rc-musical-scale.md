---
title: "Musical scale (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, audio, music, acoustics]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Musical_scale
---

## Summary
This Rosetta Code task asks the programmer to play the eight notes of the C major diatonic scale (C, D, E, F, G, A, B, and C one octave higher) through the system's default sound device. The pitches must follow 12-tone equal temperament tuned to the modern standard of A=440Hz, with Middle C (about 261.63 Hz) as the starting note. The key insight is mapping each scale degree to its correct frequency, where each semitone is a factor of the twelfth root of two and the octave doubling produces a 2:1 frequency ratio.

## Task Requirements
- Output the 8 notes of the C major diatonic scale (Do, Re, Mi, Fa, Sol, La, Si/Ti, Do) to the default musical sound device.
- Tune pitches to 12-tone equal temperament (12TET) with A=440Hz.
- Use Middle C (~261.63 Hz) as the starting note; any note duration is acceptable.
- If a language cannot drive a sound device, output a musical score, a MIDI file, or omit the task.

## Language Coverage
61 languages implement this task, reflecting broad coverage that spans systems languages, retro BASIC dialects, and dedicated music tooling. Representative implementations include C, C++, Java, Python, Go, Perl, Raku, Lua, and the music-specific LilyPond and Pure Data, alongside vintage platforms like ZX Spectrum Basic and Commodore BASIC.

## Connections
- [[EqualTemperament]] — the 12TET tuning system the task mandates
- [[Frequency]] — pitches expressed as Hz values derived from A=440
- [[DiatonicScale]] — the C major scale structure being played
- [[MIDI]] — an accepted output format for languages lacking direct audio
- [[ExponentialFunction]] — semitone spacing uses the twelfth root of two

## Contradictions
- None — reference task page.
