---
title: "Vim Editor"
type: concept
tags: [unix, editor, modal-editor]
sources: [dis-app2-4-editors]
last_updated: 2026-05-18
---

# Vim Editor

**Vim** (*"Vi IMproved"*) is the canonical modal terminal editor. Per [[dis-app2-4-editors|DIS Appendix 2.4]], Vim has **two modes**:

- **Insert mode** — keystrokes add text to the file.
- **Command (escape) mode** — keystrokes execute editor commands.

Transitions: `i` enters insert mode; `ESC` returns to command mode.

## Essential commands (command mode)

| Category | Keys |
|---|---|
| Navigation | `h` `j` `k` `l` (←/↓/↑/→); `CTRL-f` page-down; `CTRL-u` page-up |
| Editing | `dd` delete line; `yy` yank line; `p` paste; `u` undo |
| File | `:w` save; `:q` quit; `:q!` quit-no-save; `:wq` save+quit |
| Search | `/pattern` find; `n` next match |

## Learning resource
`vimtutor` ships with most Vim installs — a 20-minute interactive tutorial.

## Related
- [[EmacsEditor]] / [[NanoEditor]] — alternatives.
- [[UnixCommandLine]] — launch context.
- [[DiveIntoSystems]] — Appendix 2.4.

## Sources
- [[dis-app2-4-editors]] — DIS Appendix 2.4 *Editors*.
