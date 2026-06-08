---
title: "Window creation (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, gui, graphics, event-handling]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Window_creation
---

## Summary
This task asks the programmer to open and display a graphical user interface window on screen. The window can be empty of content, but it must respond correctly to a request to be closed (for example, clicking the window's close button must terminate the program or dismiss the window). The key insight is that this is a minimal "hello world" for GUI toolkits, exercising window instantiation, the display/event loop, and wiring up the close event.

## Task Requirements
- Display a GUI window on screen.
- The window need not contain any contents (no widgets required).
- The window must respond to a request to be closed.

## Language Coverage
100 languages implement this task, showing very broad coverage across system, scripting, functional, and BASIC-family languages, each binding to its native or popular GUI toolkit. Representative implementations include C (GTK/Win32), C++ (Qt), C#, Java (Swing/AWT), Python (Tkinter), JavaScript, Ruby, Tcl/Tk, Haskell, and Rust.

## Connections
- [[GraphicalUserInterface]] — the task is a minimal GUI demonstration
- [[EventLoop]] — windows require a message/event loop to stay alive and handle input
- [[EventHandling]] — the close request is handled via a window-close event/callback
- [[WidgetToolkit]] — each language relies on a GUI/widget toolkit binding

## Contradictions
- None — reference task page.
