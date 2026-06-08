---
title: "Terminal control/Inverse video (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, terminal-control, ansi-escape-codes]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Terminal_control/Inverse_video
---

## Summary
This task asks the programmer to print a word in inverse (reverse) video — swapping the foreground and background colors so the text stands out — immediately followed by a word rendered in normal video. The key insight is that this is controlled by terminal escape sequences rather than the language itself: on ANSI/VT100-compatible terminals the SGR code `ESC[7m` enables reverse video and `ESC[0m` (or `ESC[27m`) resets it back to normal.

## Task Requirements
- Display one word in inverse (reverse) video.
- Display a second word, after it, in normal video.

## Language Coverage
47 languages implement this task, spanning high-level scripting languages, systems languages, and low-level assembly. Representative implementations include C, Python, Ruby, Perl, Raku, Go, Kotlin, Common Lisp, Tcl, REXX, and even 6502/Z80/ARM Assembly for direct hardware control.

## Connections
- [[ANSIEscapeCodes]] — the standard mechanism for reverse video on most terminals
- [[TerminalControl]] — the broader family of Rosetta Code terminal tasks
- [[SGRParameters]] — Select Graphic Rendition codes (7 = reverse, 0 = reset)
- [[VT100]] — the terminal standard whose control sequences these emulate

## Contradictions
- None — reference task page.
