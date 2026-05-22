---
title: "Dive into Systems — Appendix 2.4 Unix Editors"
type: source
tags: [unix, editor, vim, emacs, nano]
date: 2026-05-18
source_file: https://diveintosystems.org/book/Appendix2/editors.html
---

## Summary
Fourth subchapter of [[DiveIntoSystems]] Appendix 2. Surveys the three terminal-resident text editors students will encounter: **[[VimEditor|Vim]]** (modal), **[[EmacsEditor|Emacs]]** (chord-based), **[[NanoEditor|Nano]]** (beginner-friendly). Closes with the `EDITOR` / `VISUAL` environment-variable convention for setting the system default.

## Key Claims
- **Vim** has two modes — *insert* (keystrokes add text) and *command/escape* (keystrokes are commands). `i` enters insert, `ESC` returns to command. Navigation: `h j k l` (left/down/up/right); editing: `dd` delete line, `yy` yank, `p` paste, `u` undo; file: `:w` save, `:q` quit, `:q!` quit-no-save; search: `/pattern` + `n`. `vimtutor` is a 20-minute interactive tutorial.
- **Emacs** is *modeless*; every command is a `CTRL`/`ALT` chord. `C-x C-s` save, `C-x C-c` exit, `C-n`/`C-p` next/prev line, `C-k` kill line, `C-y` yank, `C-s` search.
- **Nano** is single-mode and lists shortcuts on-screen; `C-x` exits.
- Default editor is set via `~/.bashrc`: `export EDITOR=vim` + `export VISUAL=vim`.

## Connections
- [[VimEditor]] / [[EmacsEditor]] / [[NanoEditor]] — three new concept pages.
- [[UnixCommandLine]] — editors are invoked from the shell.
- [[DiveIntoSystems]] — 155th ingested chapter.

## Contradictions
- None.
