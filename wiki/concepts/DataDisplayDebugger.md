---
title: "Data Display Debugger (DDD)"
type: concept
tags: [debugging, gdb, gui, tooling]
sources: [dis-3-1-gdb, dis-3-4-gdb-advanced]
last_updated: 2026-05-17
---

# Data Display Debugger (DDD)

**DDD** (Data Display Debugger) is a GNU **graphical front-end** that wraps [[GDB]] (and other CLI debuggers like `dbx` / `wdb` / `jdb`) with a window-and-mouse interface. [[dis-3-1-gdb|DIS Ch 3.1]] mentions it as the *"point-and-click"* alternative to typing GDB commands at a terminal prompt.

## What DDD adds

A GUI layer that surfaces standard [[Debugger|debugger]] operations as menu items, toolbar buttons, and graphical panels:

- **Source view** — click in the margin to set a [[Breakpoint|breakpoint]].
- **Variable display window** — visualize struct / array / linked-list values as graphical boxes with arrows for pointer fields (its headline differentiator, hence the *data display* name).
- **Stack-frame panel** — clickable frames in the [[GdbBacktrace|call stack]].
- **Memory-region viewer** — hex / binary / ASCII inspection of memory ranges.

Under the hood, DDD is sending the same GDB commands ([[Breakpoint|`break`]] / [[GdbRun|`run`]] / [[StepDebug|`next`]] / [[GdbPrint|`print`]] / [[GdbBacktrace|`bt`]]) that a CLI user would type — DDD just translates clicks to commands and command output to graphical updates.

## When to use it

Per [[dis-3-1-gdb|Ch 3.1]]'s framing, DDD is a *preference* — the underlying debugger is GDB, the underlying operations are the same. Users who prefer visual breakpoint setting, persistent data-structure visualizations, and a separate console-and-source layout often choose DDD; users who prefer terminal-only workflows stay with GDB directly.

## Settings & troubleshooting

DDD stores its persistent settings (saved window layouts, command history, options) in `~/.ddd/`. [[dis-3-4-gdb-advanced|DIS Ch 3.4]] flags the canonical failure mode — *"Sometimes DDD hangs on startup with a 'Waiting until GDB ready' message. This often indicates an error in its saved settings files."* Fix: `rm -rf ~/.ddd` to reset to defaults (loses saved preferences but restores a working session).

## Status

DDD is GNU project software; development has been intermittent, and modern IDE-integrated debuggers (VS Code's debug pane, CLion, Emacs's `gud` / `dap-mode`, Vim's `termdebug`) have largely supplanted it for new developers. It remains shipped in most Linux distributions.

## Connections

- [[dis-3-1-gdb]] — introducing source.
- [[GDB]] — the underlying CLI debugger DDD wraps.
- [[Debugger]] — the operation category.
- [[Breakpoint]] / [[StepDebug]] / [[GdbBacktrace]] / [[GdbPrint]] — the GDB operations DDD exposes graphically.
