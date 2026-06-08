---
title: "Simulate input/Keyboard (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, gui-automation, input-simulation]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Simulate_input/Keyboard
---

## Summary
This task asks the programmer to send simulated (synthetic) keystrokes to a GUI window or terminal, as if a user were physically typing on the keyboard. The key distinction the task draws is whether the target window may be externally created — i.e., whether the keystrokes are delivered to a separate application rather than the one generating them, which requires OS-level input injection rather than internal event posting.

## Task Requirements
- Send simulated keystrokes to a GUI window or terminal.
- Specify whether the target window may be externally created (a different application than the one sending the input).

## Language Coverage
29 languages implement this task, reflecting broad coverage across general-purpose languages and OS automation tools. Representative implementations include AutoHotkey, AutoIt, C, Go, Java, Python, PowerShell, Perl, Rust, Tcl, and VBScript — many relying on platform-specific APIs (e.g., Windows SendInput / SendKeys, X11) or dedicated automation toolkits.

## Connections
- [[GUIAutomation]] — the broader domain of programmatically driving graphical interfaces
- [[InputSimulation]] — synthesizing keyboard/mouse events at the OS level
- [[EventLoop]] — simulated keystrokes are injected into an application's input event queue
- [[InterProcessCommunication]] — delivering input to an externally created target process

## Contradictions
- None — reference task page.
