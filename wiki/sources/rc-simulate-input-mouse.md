---
title: "Simulate input/Mouse (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, gui, automation]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Simulate_input/Mouse
---

## Summary
This GUI task asks the programmer to programmatically simulate a mouse-button click as if the user had performed it, rather than handling a real input event. The key insight is that mouse simulation requires operating-system or windowing-system level APIs that synthesize input events, and the solution should note whether the targeted GUI may be one created by an external (third-party) application.

## Task Requirements
- Simulate the click of a mouse button as though triggered by the user.
- Specify whether the target GUI may be externally created (i.e., not owned by the simulating program).

## Language Coverage
24 languages implement this task, spanning systems languages, scripting languages, and automation-focused tools. Representative implementations include C, Go, Rust, Java, Kotlin, Scala, Python, Racket, Tcl, and the automation tool AutoHotkey.

## Connections
- [[GUIAutomation]] — synthesizing user input events programmatically
- [[EventDrivenProgramming]] — injecting events into a windowing system's event loop
- [[OperatingSystemAPI]] — OS-level calls required to post mouse events
- [[InputSimulation]] — the general technique of faking keyboard/mouse input

## Contradictions
- None — reference task page.
