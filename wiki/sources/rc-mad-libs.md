---
title: "Mad Libs (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, string-processing, text-templating]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Mad_Libs
---

## Summary
Implement the Mad Libs word game: read an arbitrary multiline story (terminated by a blank line) that contains placeholders delimited by angle brackets, such as `<name>` or `<noun>`. For each distinct placeholder, prompt the user for a substitute word, then replace every occurrence and print the completed story. The key insight is that repeated placeholders of the same name must share a single user-supplied value, so the program collects unique tokens before substituting.

## Task Requirements
- Read an arbitrary multiline story from input, terminated by a blank line.
- Detect each replacement placeholder embedded in the story (e.g. `<name>`, `<he or she>`, `<noun>`).
- Prompt the user once per distinct placeholder for a replacement word.
- Replace all occurrences of each placeholder with the supplied word (same value for repeats).
- Print the final substituted story.

## Language Coverage
65 languages implement this task, spanning systems, scripting, functional, and many BASIC dialects. Representative examples include Python, C, C++, Java, Rust, Go, Haskell, Perl, Ruby, Lua, and Tcl.

## Connections
- [[StringProcessing]] — core operation is scanning and substituting substrings
- [[TextTemplating]] — placeholders filled from user input mirror template engines
- [[RegularExpressions]] — common technique for matching `<...>` tokens
- [[StandardInput]] — story and answers are read interactively from stdin

## Contradictions
- None — reference task page.
