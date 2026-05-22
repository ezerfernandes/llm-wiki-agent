---
title: "Emacs Editor"
type: concept
tags: [unix, editor, chord-editor]
sources: [dis-app2-4-editors]
last_updated: 2026-05-18
---

# Emacs Editor

**Emacs** is a modeless terminal editor (in contrast to [[VimEditor|Vim]]'s two-mode design). All commands are chord combinations involving `CTRL`, `ALT`, and `SHIFT`.

Per [[dis-app2-4-editors|DIS Appendix 2.4]], every keystroke either inserts text directly or — when combined with a modifier — executes a command.

## Essential chords

| Category | Keys |
|---|---|
| File | `C-x C-s` save; `C-x C-c` exit |
| Navigation | `C-n` / `C-p` next / prev line; `C-f` / `C-b` forward / back char |
| Editing | `C-d` delete char; `C-k` kill to end of line; `C-y` yank (paste) |
| Search | `C-s` incremental search forward |

(Notation: `C-x` = `CTRL` + `x`.)

## Related
- [[VimEditor]] — the modal alternative.
- [[NanoEditor]] — the beginner-friendly alternative.
- [[DiveIntoSystems]] — Appendix 2.4.

## Sources
- [[dis-app2-4-editors]] — DIS Appendix 2.4 *Editors*.
