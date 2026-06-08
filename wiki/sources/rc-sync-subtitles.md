---
title: "Sync subtitles (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, text-processing, time-arithmetic, file-io]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Sync_subtitles
---

## Summary
The task asks the programmer to write a program that reads a SubRip (`.srt`) subtitle file and shifts every subtitle's timestamps forward or backward by a given number of seconds, fixing audio/subtitle desync. The key insight is parsing the `HH:MM:SS,mmm --> HH:MM:SS,mmm` timecode lines, converting them to a total time unit (often milliseconds), adding the signed offset, and re-formatting them back into the SRT layout while leaving the index numbers and caption text untouched.

## Task Requirements
- Take a `movie.srt` file as input and shift all subtitles by `n` seconds.
- Demonstrate fast-forwarding the subtitles by 9 seconds.
- Demonstrate rolling them back by 9 seconds.
- Preserve the SubRip structure: numbered entries, `start --> end` timecode lines, and the caption text.

## Language Coverage
18 languages implement this task, spanning scripting, systems, and niche languages. Representative implementations include AWK, C++, COBOL, Go, Java, Julia, Lua, Perl, Python, Raku, Rust, and Wren.

## Connections
- [[SubRip]] — the `.srt` subtitle file format being manipulated
- [[StringProcessing]] — parsing and reformatting the timecode and text lines
- [[TimeArithmetic]] — converting timecodes to a base unit and applying a signed offset
- [[FileIO]] — reading the source file and writing the synchronized output
- [[RegularExpressions]] — common technique for matching the timestamp lines

## Contradictions
- None — reference task page.
