---
title: "Terminal control/Coloured text (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, terminal-control, ansi-escape-codes]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Terminal_control/Coloured_text
---

## Summary
This task asks the programmer to display a word in various colours on the terminal, drawing from the system palette or named colours such as red, green, blue, magenta, cyan, and yellow. The key insight is that text colour on most terminals is controlled by emitting ANSI/VT100 escape sequences (e.g. `ESC[31m` for red) rather than by any built-in colour API.

## Task Requirements
- Display a word rendered in several different colours on the terminal.
- Use either the system palette or named colours (red, green, blue, magenta, cyan, yellow).
- Optionally: detect whether the terminal supports colour at all.
- Optionally: set the background colour as well as the foreground.
- Optionally: trigger blinking or flashing text where the terminal supports it.

## Language Coverage
65 languages implement this task, spanning systems languages, scripting languages, and a wide range of BASIC dialects, reflecting how universal terminal output is. Representative implementations include C, C++, Rust, Go, Python, Ruby, Perl, Haskell, Java, and the UNIX Shell.

## Connections
- [[ANSIEscapeCodes]] — the standard mechanism for selecting foreground/background colours and attributes.
- [[TerminalControl]] — the broader family of tasks for manipulating terminal state.
- [[StandardOutput]] — coloured text is emitted by writing escape sequences to stdout.
- [[CapabilityDetection]] — optional check for whether the terminal supports colour.

## Contradictions
- None — reference task page.
