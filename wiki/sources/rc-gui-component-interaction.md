---
title: "GUI component interaction (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, gui, event-driven, input-validation]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/GUI_component_interaction
---

## Summary
The task asks the programmer to build a minimal graphical application whose components interact with each other and with the user. The form holds a numeric field plus two buttons; the buttons must read, validate, and mutate the field's state, and one of them must route through a confirmation dialog before acting. The key insight is wiring program logic to GUI widgets: pushing values into fields under program control, validating user input, and querying the user with pop-up dialogs.

## Task Requirements
- Present a form with three components: a numeric input field ("Value"), an "increment" button, and a "random" button.
- Initialize the field to zero.
- Allow the user to manually type a new value, or raise the value via the "increment" button.
- Either prevent non-numeric input or issue an error message for it.
- On "random", show a confirmation dialog and only reset the field to a random value if the user answers "Yes".

## Language Coverage
57 languages implement this task, spanning compiled, scripting, and functional ecosystems with their varied GUI toolkits. Representative entries include Ada, C++, C# (C_sharp), Java, Python, Ruby, Tcl, Go, Haskell, Racket, and Common Lisp.

## Connections
- [[EventDrivenProgramming]] — buttons fire callbacks that mutate shared field state
- [[GraphicalUserInterface]] — the form, fields, and dialogs are GUI widgets
- [[InputValidation]] — rejecting or flagging non-numeric entries
- [[ModalDialog]] — the confirmation prompt gating the random action
- [[SimpleWindowedApplication]] — the base task this one extends

## Contradictions
- None — reference task page.
