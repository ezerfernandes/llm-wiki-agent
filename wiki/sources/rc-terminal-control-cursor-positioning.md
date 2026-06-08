---
title: "Terminal control/Cursor positioning (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, terminal-control]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Terminal_control/Cursor_positioning
---

## Summary
This task asks the programmer to move the terminal cursor to an absolute screen position and print text there. Specifically, the cursor must be placed at column 3, row 6, and the word "Hello" displayed so that its leading letter "H" lands at that exact cell. The key insight is that absolute cursor positioning on most terminals is achieved by emitting an ANSI escape sequence (CSI `row;col H`) or by calling a terminal library such as curses/conio rather than relying on ordinary newlines and spaces.

## Task Requirements
- Move the cursor to column 3, row 6.
- Display the word "Hello" (without quotes) starting at that position so the "H" occupies column 3, row 6.

## Language Coverage
58 languages implement this task, spanning shells and scripting languages, system languages, and even raw assembly. Representative examples include C/C++, Python, Ruby, Perl, Go, C#, Common Lisp, Forth, COBOL, UNIX Shell, and AArch64 Assembly, with esoteric entries like Befunge and Whitespace also present.

## Connections
- [[AnsiEscapeCodes]] — the standard CSI sequence used for absolute positioning
- [[TerminalControl]] — broader family of cursor and screen manipulation tasks
- [[Curses]] — terminal library offering portable cursor addressing
- [[EscapeSequence]] — control characters that drive terminal behavior

## Contradictions
- None — reference task page.
