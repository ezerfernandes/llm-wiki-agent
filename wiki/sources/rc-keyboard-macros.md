---
title: "Keyboard macros (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, gui, event-handling, keybinding]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Keyboard_macros
---

## Summary
This task asks the programmer to demonstrate how to link user-defined methods (handlers) to user-defined keys, the way Emacs lets you bind keys to commands. The core idea is registering a callback that fires when a particular key or key combination is pressed. Solutions must state whether the binding is application-specific or system-wide, since the mechanism differs sharply between the two.

## Task Requirements
- Show how to associate user-defined functions/methods with user-defined keys.
- Use key bindings analogous to the Emacs facility (e.g., binding a key to invoke a command).
- State explicitly whether the implemented binding is application-specific or system-wide.

## Language Coverage
32 languages implement this task, spanning GUI toolkits, scripting hotkey utilities, and terminal/editor macro systems. Representative implementations include AutoHotkey, C, Java, JavaScript, Python, Ruby, Perl, Tcl, Go, and Kotlin.

## Connections
- [[EventDrivenProgramming]] — key bindings dispatch handlers in response to input events.
- [[CallbackFunction]] — a method is registered to run when a key fires.
- [[GraphicalUserInterface]] — most application-specific bindings live inside a GUI event loop.
- [[Emacs]] — the canonical key-binding model the task references.

## Contradictions
- None — reference task page.
