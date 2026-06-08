---
title: "Run-length encoding (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, compression, string-processing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Run-length_encoding
---

## Summary
The task asks the programmer to implement run-length encoding (RLE), a simple lossless compression scheme that replaces consecutive runs of the same character with a count followed by that character. A matching decoder must reconstruct the original string exactly. The key insight is that RLE only saves space when the data has long repeated runs, and the per-run count step is identical to one step of the look-and-say sequence.

## Task Requirements
- Given a string of uppercase letters (A-Z), compress runs of the same character into a count plus the character (e.g. `WWWW` becomes `4W`).
- Provide a decompression function that reverses the encoding to recover the original string exactly.
- Output format is unconstrained as long as the input can be losslessly recreated; the canonical example maps `WWWWWWWWWWWWB...` to `12W1B12W3B24W1B14W`.

## Language Coverage
131 languages implement this task, reflecting its status as a classic introductory compression exercise spanning everything from low-level assembly to high-level functional and scripting languages. Representative implementations include C, C++, Python, Haskell, Java, Go, Rust, Perl, Ruby, and APL.

## Connections
- [[RunLengthEncoding]] — the compression algorithm being implemented
- [[DataCompression]] — the broader category of lossless encoding techniques
- [[LookAndSaySequence]] — RLE's count step is one step of this sequence
- [[StringProcessing]] — the task is fundamentally run detection over a character sequence

## Contradictions
- None — reference task page.
