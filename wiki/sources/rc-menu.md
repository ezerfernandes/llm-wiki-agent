---
title: "Menu (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, string-processing, user-input]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Menu
---

## Summary
This task asks the programmer to build a reusable function that presents an interactive textual menu. Given a prompt and a list of option strings, the function prints each option preceded by its index, asks the user to type a number, and returns the chosen string. The key challenge is robust input validation: any input that is not an integer or is outside the valid range must cause the whole menu to be redisplayed and the prompt repeated, while an empty option list must return an empty string immediately.

## Task Requirements
- Print a textual menu where each item is shown as an index value followed by its string.
- Prompt the user to enter a number.
- Return the string corresponding to the selected index.
- Reject non-integer or out-of-range input by redisplaying the menu and asking again.
- Return an empty string when called with an empty list.
- Test with the four phrases: "fee fie", "huff and puff", "mirror mirror", "tick tock".
- Modeled on the behavior of the Bash `select` statement.

## Language Coverage
100 languages implement this task, spanning systems languages, scripting languages, assembly, and BASIC dialects, reflecting how universal interactive console input is. Representative implementations include C, C++, Python, Ruby, Go, Rust, Java, Haskell, Perl, and the UNIX Shell.

## Connections
- [[StringProcessing]] — formatting and returning option strings
- [[InteractiveInput]] — reading and looping on user console input
- [[InputValidation]] — rejecting non-integer or out-of-range entries
- [[ControlFlow]] — the redisplay loop mirrors Bash's `select` construct

## Contradictions
- None — reference task page.
