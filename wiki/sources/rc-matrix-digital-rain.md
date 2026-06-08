---
title: "Matrix digital rain (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, terminal-graphics, animation]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Matrix_digital_rain
---

## Summary
This task asks the programmer to reproduce the "digital rain" visual effect from the film *The Matrix*: columns of glowing characters that cascade down a terminal screen. The core challenge is animating the terminal — repeatedly drawing falling streams of randomly chosen characters at varied speeds and lengths, typically using cursor positioning and timed redraws rather than any single algorithm. A reference implementation in Common Lisp is provided as a starting point.

## Task Requirements
- Implement the Matrix digital rain effect as described on Wikipedia.
- Render the effect in a terminal (the supplied reference is a terminal program).

## Language Coverage
27 languages implement this task, spanning systems languages, scripting languages, and many BASIC dialects, which reflects how terminal animation is approachable across very different ecosystems. Representative implementations include C, Go, Rust, Java, JavaScript, Python, Perl, Raku, Common Lisp, and REXX.

## Connections
- [[TerminalAnimation]] — the effect is built from timed redraws of a text display.
- [[ANSIEscapeCodes]] — cursor positioning and color control drive terminal output.
- [[RandomNumberGeneration]] — characters, stream lengths, and speeds are chosen randomly.
- [[GameLoop]] — a continuous update/render loop produces the cascading motion.

## Contradictions
- None — reference task page.
