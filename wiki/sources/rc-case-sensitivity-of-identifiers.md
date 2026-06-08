---
title: "Case-sensitivity of identifiers (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, language-semantics, identifiers]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Case-sensitivity_of_identifiers
---

## Summary
This task demonstrates whether a programming language treats the lettercase of identifiers as significant. Using the classic "three dogs" snippet, you declare three variables `dog`, `Dog`, and `DOG`. In a case-sensitive language these are three distinct identifiers; in a case-insensitive language they all refer to the same variable. The output reveals the language's behavior.

## Task Requirements
- Declare/assign the identifiers `dog`, `Dog`, and `DOG` (assigning names such as Benjamin, Samba, and Bernie).
- For a case-sensitive language, produce: `The three dogs are named Benjamin, Samba and Bernie.`
- For a case-insensitive language, produce: `There is just one dog named Bernie.`
- The output should accurately reflect how many distinct identifiers the language recognizes.

## Language Coverage
135 languages implement this task, spanning case-sensitive languages (C, Python, Java, Ruby, Rust, Go, Haskell, JavaScript) and case-insensitive ones (Fortran, COBOL, Pascal, REXX, PowerShell, AutoHotkey), illustrating a fundamental design split across language families.

## Connections
- [[CaseSensitivity]] — the central language-design property under test
- [[Identifiers]] — naming of variables and the rules governing them
- [[LexicalAnalysis]] — case folding happens during tokenization/symbol resolution
- [[ProgrammingLanguageSemantics]] — how identifier equivalence is defined

## Contradictions
- None — reference task page.
