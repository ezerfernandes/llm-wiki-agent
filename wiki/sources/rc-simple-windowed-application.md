---
title: "Simple windowed application (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, gui, event-handling]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Simple_windowed_application
---

## Summary
This task asks the programmer to build a minimal graphical desktop application: a window containing a label initially reading "There have been no clicks yet" and a button labeled "click me". Each time the button is clicked, the label updates to display the running click count. The key insight is wiring a button's click event to a handler that mutates shared state (the counter) and refreshes the label, the canonical "hello world" of event-driven GUI programming.

## Task Requirements
- Create a window that contains a label initially showing "There have been no clicks yet".
- The window must contain a button labeled "click me".
- Clicking the button changes the label to show how many times the button has been clicked.

## Language Coverage
100 languages implement this task, demonstrating broad cross-platform GUI toolkit coverage from low-level to high-level. Representative implementations include C (Win32/GTK), C# and Visual Basic (WinForms), Java and Scala (Swing), Python (Tkinter), Tcl/Tk, Haskell, Go, Rust, Lua, and even visual environments like Scratch.

## Connections
- [[EventDrivenProgramming]] — the click handler responds to a user-generated event
- [[GraphicalUserInterface]] — the task exercises window, label, and button widgets
- [[CallbackFunction]] — the button's action is bound to a callback that updates state
- [[StateMutation]] — the click counter is shared mutable state refreshed in the label

## Contradictions
- None — reference task page.
