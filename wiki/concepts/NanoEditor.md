---
title: "Nano Editor"
type: concept
tags: [unix, editor, beginner-friendly]
sources: [dis-app2-4-editors]
last_updated: 2026-05-18
---

# Nano Editor

**Nano** is a single-mode, beginner-friendly terminal editor. Per [[dis-app2-4-editors|DIS Appendix 2.4]], its key distinguishing feature is that *the available shortcuts are listed on-screen at all times* — no memorization required.

## Essentials
- `C-x` — exit (prompts to save if buffer is modified).
- `C-o` — write (save).
- `C-w` — search.
- `C-k` — cut line; `C-u` — uncut (paste).

(Notation: `C-x` = `CTRL` + `x`.)

## When to use
Nano is the right default for *"I just need to edit one config file"* sessions over [[SSH]] where a Vim/Emacs setup isn't worth bootstrapping. Most Linux distributions ship it as `nano` and use it as the default `crontab` / `visudo` editor when the user's `EDITOR` isn't set.

## Related
- [[VimEditor]] — modal, power-user default.
- [[EmacsEditor]] — chord-based.
- [[DiveIntoSystems]] — Appendix 2.4.

## Sources
- [[dis-app2-4-editors]] — DIS Appendix 2.4 *Editors*.
