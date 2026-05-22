---
title: "Dive into Systems — Appendix 2.2 Man Pages"
type: source
tags: [unix, documentation, command-line]
date: 2026-05-18
source_file: https://diveintosystems.org/book/Appendix2/man.html
---

## Summary
Second subchapter of [[DiveIntoSystems]] Appendix 2. Promotes [[ManPages|`man`]] from the cross-chapter forward reference (already minted via [[dis-2-6-strings|Ch 2.6]]) into a first-class subchapter: how to invoke `man`, how to navigate via `less`, the numbered-section convention, the page structure, and the `apropos` keyword search.

## Key Claims
- `man <name>` displays the manual page; `man <section> <name>` disambiguates by section (e.g. `man 2 write`).
- Man pages open in the [[Less|`less`]] pager — `q` quits, *space* pages down, `/` searches.
- Standard man-page sections include **NAME**, **SYNOPSIS**, **DESCRIPTION**, **RETURN VALUE**, **SEE ALSO**.
- **Numbered sections**: §1 commands, §2 system calls, §3 library functions (and more — see [[ManPages]]).
- `apropos <keyword>` searches one-line descriptions across all installed man pages.

## Connections
- [[ManPages]] — extended in place with the Appendix 2.2 discovery / `apropos` framing (prior coverage was [[dis-2-6-strings|Ch 2.6]] string-library only).
- [[UnixCommandLine]] — `man` is the in-place help system for every other command in Appendix 2.
- [[DiveIntoSystems]] — 153rd ingested chapter.

## Contradictions
- None. Reinforces the [[ManPages]] coverage already in the wiki.
