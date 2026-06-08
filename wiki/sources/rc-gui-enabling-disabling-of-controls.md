---
title: "GUI enabling/disabling of controls (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, gui, event-driven]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/GUI_enabling/disabling_of_controls
---

## Summary
This task extends basic GUI component interaction by requiring an application to dynamically enable and disable controls based on the current state, guiding the user and preventing inappropriate actions. The program shows a numeric field plus "increment" and "decrement" buttons, and the key insight is that widget enabled-state must be recomputed in response to every value change rather than set once at startup.

## Task Requirements
- Present a form with a numeric input field ("Value"), an "increment" button, and a "decrement" button.
- Initialize the field to zero; allow manual entry, increment, or decrement.
- Enable the input field only when its value is zero.
- Enable "increment" only while the value is less than 10; disable it at 10.
- Enable "decrement" only while the value is greater than zero.
- Manually entered out-of-range values remain legal, but the buttons must enable/disable to reflect the new state.

## Language Coverage
44 languages implement this task, spanning desktop GUI toolkits, BASIC dialects, and functional languages. Representative implementations include Ada, C#, C++, Java, Python, Tcl, Go, Kotlin, Ruby, Perl, and Racket.

## Connections
- [[GraphicalUserInterface]] — the task targets GUI toolkits and widget controls.
- [[EventDrivenProgramming]] — button/field state updates are triggered by user-input events.
- [[StateMachine]] — control availability is derived from the application's current value state.
- [[GUIComponentInteraction]] — this task directly extends that companion Rosetta Code task.

## Contradictions
- None — reference task page.
