---
title: "Terminal control/Ringing the terminal bell (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, terminal-control, character-encoding]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Terminal_control/Ringing_the_terminal_bell
---

## Summary
This task asks the programmer to make the terminal running the program ring its "bell" — historically a physical bell in the terminal, now often a beep, a title-bar flash, or a screen-color inversion on modern emulators. The key insight is that ringing the bell is simply a matter of printing the ASCII Bell character (code 7, written `\a` in C) to standard output; the behavior is a function of the terminal itself and is largely independent of the programming language.

## Task Requirements
- Cause the controlling terminal to ring (or otherwise signal) its bell.
- This is conventionally achieved by writing the ASCII Bell control character (decimal 7, `\a`) to standard out.
- Any equivalent way the language can emit that byte to the terminal is acceptable.

## Language Coverage
95 languages implement this task, spanning the full spectrum from low-level assembly to high-level scripting and esoteric languages. Representative implementations include C, Python, Ruby, Java, Go, Rust, Perl, Lua, Haskell, and even minimalist/esoteric languages like Brainf*** and Binary Lambda Calculus, reflecting how trivially the single Bell byte can be emitted almost anywhere.

## Connections
- [[ASCIIControlCharacters]] — the Bell character is ASCII control code 7 (`\a`).
- [[TerminalControl]] — part of the broader family of terminal-control tasks.
- [[StandardOutput]] — the bell is triggered by writing the byte to stdout.
- [[CharacterEncoding]] — relies on the conventional meaning of a specific control code.

## Contradictions
- None — reference task page.
