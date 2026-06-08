---
title: "Keyboard input/Keypress check (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, keyboard-input, non-blocking-io]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Keyboard_input/Keypress_check
---

## Summary
This task asks the programmer to determine whether a key has currently been pressed and store that result in a variable. The defining constraint is that the check must be non-blocking: if no key is pressed, the program continues immediately rather than waiting for input. This requires polling the keyboard rather than using a conventional blocking read, which on most platforms means querying terminal state or an event queue directly.

## Task Requirements
- Determine whether a key has been pressed and store the result in a variable.
- If no key has been pressed, the program must continue without waiting (non-blocking check).

## Language Coverage
63 languages implement this task, spanning systems languages, scripting languages, and retro/BASIC dialects. Representative implementations include C, Go, Rust-adjacent assembly (6502 Assembly, ARM Assembly), Python, Perl, Raku, Java, C#, Haskell, and Ruby.

## Connections
- [[NonBlockingIO]] — checking for input without halting execution
- [[KeyboardInput]] — the broader category of reading keystrokes
- [[Polling]] — repeatedly querying device state rather than blocking
- [[EventLoop]] — common context where a non-blocking keypress check is used

## Contradictions
- None — reference task page.
