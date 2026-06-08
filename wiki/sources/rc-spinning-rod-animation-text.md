---
title: "Spinning rod animation/Text (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, terminal-animation, string-processing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Spinning_rod_animation/Text
---

## Summary
The task asks the programmer to render a simple text "spinner" by cycling through the frames `|`, `/`, `-` (or `─`), and `\` with a 0.25-second delay between frames, clearing the previous frame before drawing the next so the rod appears to rotate in place. The key insight is reusing a single character cell and overwriting it (typically via a carriage return or cursor control) rather than printing a new line per frame.

## Task Requirements
- Cycle through the frames `|`, `/`, `-`/`─`, `\` in that order, with substitute characters allowed if a glyph is unavailable.
- Insert a 0.25-second delay between frames.
- Clear/overwrite the previous frame before showing the next so the animation stays in one position.
- A looping stand-alone version and/or a non-looping version are both acceptable; the logic may also be structured as a per-frame HUD/GUI call.
- Optional richer frame sets are offered (dots, stars, clock faces, arrows, eclipse phases) and a ping-pong mode that plays frames forward then backward.

## Language Coverage
57 languages implement this task, showing broad reach across systems, scripting, and BASIC dialects. Representative examples include C, Go, Rust, Java, JavaScript, Python, Perl, Raku, Haskell, Lua, and Ruby.

## Connections
- [[TerminalControlCodes]] — carriage return and cursor manipulation to overwrite the frame in place
- [[StringProcessing]] — cycling through a fixed sequence of frame characters
- [[Animation]] — frame-based timing with a fixed inter-frame delay
- [[UnicodeCharacters]] — optional frame sets rely on Unicode glyphs (`─`, clock faces, arrows)

## Contradictions
- None — reference task page.
