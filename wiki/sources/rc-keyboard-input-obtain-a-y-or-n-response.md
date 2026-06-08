---
title: "Keyboard input/Obtain a Y or N response (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, keyboard-input, terminal-io]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Keyboard_input/Obtain_a_Y_or_N_response
---

## Summary
This task asks the programmer to obtain a single valid Y or N keystroke from the keyboard. The key insight is that input must be captured in raw/unbuffered mode: the response should register the moment Y or N is pressed, with no need to hit enter, and the input buffer must first be flushed so any stale key-presses cannot be misread as the answer.

## Task Requirements
- Read a single key directly from the keyboard rather than a buffered line.
- Flush the keyboard buffer first so outstanding key-presses are discarded before reading.
- Accept the response immediately on Y or N press, without requiring the enter key.
- Restrict the accepted answer to a valid Y or N.

## Language Coverage
89 languages implement this task, spanning low-level assembly and BASIC dialects up through modern scripting and functional languages. Representative implementations include C, C++, Python, Go, Rust, Java, Haskell, Ruby, Perl, and several assembly variants (8080/8086/Z80, ARM).

## Connections
- [[RawTerminalMode]] — disabling line buffering/canonical mode to read single keystrokes
- [[InputBufferFlushing]] — clearing pending keystrokes before reading
- [[KeyboardInput]] — the general category of direct device input
- [[BlockingIO]] — waiting for a single key event before proceeding

## Contradictions
- None — reference task page.
