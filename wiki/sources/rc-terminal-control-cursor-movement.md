---
title: "Terminal control/Cursor movement (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, terminal-control, ansi-escape-codes]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Terminal_control/Cursor_movement
---

## Summary
This task asks the programmer to move the terminal cursor in eight distinct ways without overwriting any existing characters or attributes on screen. The key insight is that pure cursor relocation (left, right, up, down, line start/end, and the screen corners) must be achieved through control sequences rather than by emitting visible output such as spaces. On most systems this is done with ANSI/VT100 escape codes, though some platforms expose dedicated console APIs instead.

## Task Requirements
- Move the cursor one position left, and one position right.
- Move the cursor up one line and down one line, preserving the horizontal position.
- Move the cursor to the beginning of the line and to the end of the line.
- Move the cursor to the top-left corner and to the bottom-right corner of the screen.
- Do not overwrite any characters or attributes; emitting a space to simulate rightward movement is explicitly disallowed.
- Out-of-bounds behavior is left to the implementer's discretion, with explanatory notes permitted.

## Language Coverage
40 languages implement this task, ranging from low-level assembly to high-level scripting and several BASIC dialects. Representative implementations include C, Python, Go, Perl, Ruby, Kotlin, Common Lisp, Forth, AArch64 Assembly, and BBC BASIC.

## Connections
- [[AnsiEscapeCodes]] — the standard control sequences used to reposition the cursor
- [[TerminalControl]] — the broader family of console manipulation tasks
- [[Vt100]] — the terminal protocol whose escape sequences these codes derive from
- [[ControlCharacters]] — non-printing bytes that drive terminal behavior

## Contradictions
- None — reference task page.
