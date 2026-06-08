---
title: "Keyboard input/Flush the keyboard buffer (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, terminal-control, input-handling]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Keyboard_input/Flush_the_keyboard_buffer
---

## Summary
This task asks the programmer to discard any characters already sitting in the keyboard input buffer until none remain buffered, then continue execution. The crucial constraint is that the program must not block waiting for the user to type something — it only drains whatever is already pending. The key insight is that flushing requires non-blocking input detection (polling for available keystrokes) rather than ordinary blocking reads.

## Task Requirements
- Read and discard characters from the keyboard input until the buffer is empty.
- Allow the program to continue once no more characters are buffered.
- The program must not wait for the user to type anything (no blocking).

## Language Coverage
49 languages implement this task, spanning low-level assembly through high-level scripting and functional languages. Representative implementations include C, Ada, Go, Haskell, Python, Ruby, Perl, Tcl, Kotlin, and several assembly variants (6502, 8086, AArch64, ARM).

## Connections
- [[TerminalControl]] — flushing depends on terminal/console driver behavior
- [[NonBlockingIO]] — must poll for input without blocking on a read
- [[BufferManagement]] — the task is fundamentally about draining an input buffer
- [[KeyboardInput]] — part of the broader keyboard input task family

## Contradictions
- None — reference task page.
