---
title: "Animation (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, gui, string-processing, event-handling]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Animation
---

## Summary
This task asks the programmer to build a minimal animation system in a GUI: display the string "Hello World! " and make it appear to scroll by periodically moving the last character to the front of the string. The key insight is the classic animation loop — repeatedly mutating the displayed state on a timer while keeping the program responsive to user input. Clicking the text must reverse the scroll direction.

## Task Requirements
- Create a window containing the string "Hello World! " (the trailing space is significant).
- Periodically remove one letter from the end of the string and attach it to the front, so the text appears to rotate to the right.
- Detect a user click on the windowed text and reverse the rotation direction in response.

## Language Coverage
82 languages implement this task, reflecting broad coverage across GUI toolkits, BASIC dialects, and web technologies. Representative implementations include C, C++, C#, Java, Python, JavaScript + HTML, JavaScript + SVG, Haskell, Ruby, Rust, Tcl, and Scratch.

## Connections
- [[EventDrivenProgramming]] — relies on a click event handler to reverse direction
- [[GraphicalUserInterface]] — renders text in a window and repaints on a timer
- [[StringRotation]] — the visual effect is a cyclic rotation of characters
- [[GameLoop]] — periodic state update plus redraw is the core of any animation engine

## Contradictions
- None — reference task page.
