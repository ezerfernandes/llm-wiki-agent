---
title: "Password generator (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, string-processing, randomness, security]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Password_generator
---

## Summary
The task asks the programmer to build a program that generates random passwords drawn from four character groups: lower-case letters, upper-case letters, digits, and a set of "other" printable ASCII symbols (excluding white-space, backslash, and grave). The key constraint is that each generated password must contain at least one character from every group, which means a naive uniform draw is insufficient and the program must either guarantee or reject-and-retry until all groups are represented.

## Task Requirements
- Draw characters from four groups: a-z, A-Z, 0-9, and the printable set ``!"#$%&'()*+,-./:;<=>?@[]^_{|}~``.
- Guarantee every password includes at least one lower-case letter, one upper-case letter, one digit, and one "other" character.
- Let the user specify password length and the number of passwords to generate.
- Output the passwords one per line (display or write to file).
- Source randomness from a system source or library (not a weak/ad-hoc generator).
- Provide a help option/button describing the program and its options.
- Optionally support a user-supplied seed and an option to exclude visually similar characters (e.g. Il1, O0, 5S, 2Z).

## Language Coverage
66 languages implement this task, spanning systems, scripting, functional, and assembly families. Representative implementations include C, C++, Rust, Go, Java, Python, JavaScript, Haskell, Perl, Ruby, and even 6502/x86-64 Assembly.

## Connections
- [[RandomNumberGeneration]] — relies on a system or library RNG, optionally seeded
- [[StringProcessing]] — assembling and shuffling characters into the output string
- [[CharacterSets]] — categorizing and selecting from ASCII character groups
- [[PasswordSecurity]] — the practical security domain motivating the task
- [[RejectionSampling]] — common technique to enforce the at-least-one-per-group constraint

## Contradictions
- None — reference task page.
