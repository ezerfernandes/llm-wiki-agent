---
title: "Morse code (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, encoding, audio, string-processing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Morse_code
---

## Summary
This task asks the programmer to take an input string and play it as audible Morse code through an audio device, such as the PC speaker. Each character is mapped to its dot-dash pattern and rendered as timed tones (dots being short, dashes long) separated by silences. The key insight is combining a lookup table of character-to-Morse mappings with platform-specific sound generation and correct timing for dots, dashes, and inter-element/inter-character gaps.

## Task Requirements
- Send a string as audible Morse code to an audio device (e.g., the PC speaker).
- Since standard Morse code does not cover all possible characters, either ignore unknown characters or indicate them somehow (e.g., with a different pitch).

## Language Coverage
79 languages implement this task, a broad cross-section spanning systems languages, scripting languages, and esoteric ones; representative implementations include C, C++, Rust, Go, Java, Python, Perl, Haskell, Ruby, and Tcl.

## Connections
- [[MorseCode]] — the encoding scheme being rendered
- [[CharacterEncoding]] — mapping characters to dot-dash patterns
- [[AudioSynthesis]] — generating timed tones on an audio device
- [[LookupTable]] — typical implementation maps each character via a table

## Contradictions
- None — reference task page.
