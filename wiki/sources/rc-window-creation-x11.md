---
title: "Window creation/X11 (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, graphics, gui, system-programming]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Window_creation/X11
---

## Summary
The task is to build a minimal X11 GUI application that opens a window, draws a box, and renders the text "Hello World" inside it. The key constraint is to talk directly to the X11 display server through a low-level protocol library such as Xlib or XCB, deliberately avoiding higher-level widget toolkits. This exposes the raw mechanics of window management: connecting to the display, creating and mapping a window, and handling the expose event loop to perform drawing.

## Task Requirements
- Create a simple X11 application that opens a window.
- Draw a box and the text "Hello World" inside that window.
- Use an X11 protocol library (e.g. Xlib or XCB) rather than a GUI toolkit.
- Avoid using a toolkit as much as possible.

## Language Coverage
35 languages implement this task, spanning low-level assembly bindings to high-level scripting and functional languages. Representative implementations include C, Go, Haskell, OCaml, Python, Perl, Racket, Common Lisp, ARM Assembly, and Nim, most binding directly to Xlib or XCB.

## Connections
- [[X11]] — the display server protocol the task targets
- [[Xlib]] — the canonical low-level C client library used by many solutions
- [[XCB]] — the alternative asynchronous X11 binding mentioned as acceptable
- [[GraphicalUserInterface]] — the broader category this task belongs to
- [[EventLoop]] — the expose/event handling pattern required to draw and keep the window alive

## Contradictions
- None — reference task page.
