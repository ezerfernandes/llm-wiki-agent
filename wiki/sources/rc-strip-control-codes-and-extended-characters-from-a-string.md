---
title: "Strip control codes and extended characters from a string (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, string-processing, character-encoding]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Strip_control_codes_and_extended_characters_from_a_string
---

## Summary
This task asks the programmer to filter unwanted characters out of a string, producing two variants: one with only ASCII control codes removed, and one with both control codes and extended (non-printable-ASCII) characters removed. The key insight is that "control codes" are ASCII decimal 0–31 plus 127, while printable characters fall in the 32–126 range, so stripping reduces to a per-character range test on the underlying code point.

## Task Requirements
- Produce a version of the string with control codes stripped but extended characters retained.
- Produce a version with both control codes and extended characters stripped.
- Treat decimal codes 0–31 and 127 as ASCII control codes.
- After stripping controls only, remaining characters should still allow values above 126 (extended); after stripping both, characters should lie within 32–126 decimal.
- On non-ASCII systems, treat any character without a glyph in the printable ASCII range as an extended character.

## Language Coverage
83 languages implement this task, spanning low-level assembly through high-level scripting and functional languages. Representative entries include C, C++, Rust, Go, Python, Java, JavaScript, Haskell, Perl, Raku, Ruby, and sed.

## Connections
- [[StringProcessing]] — the task is fundamentally character-level filtering of a string.
- [[CharacterEncoding]] — distinguishing control, printable ASCII, and extended characters depends on the code-point model.
- [[ASCII]] — the numeric ranges (0–31, 127, 32–126) are defined by the ASCII table.
- [[Filtering]] — implementations apply a predicate over each character to keep or discard it.

## Contradictions
- None — reference task page.
