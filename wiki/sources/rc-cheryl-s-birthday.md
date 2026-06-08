---
title: "Cheryl's birthday (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, logic-puzzle, constraint-solving]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Cheryl's_birthday
---

## Summary
Given a list of ten candidate dates, the program must deduce Cheryl's birthday from three statements made by Albert (who knows only the month) and Bernard (who knows only the day). The key insight is that each statement encodes a logical constraint that progressively eliminates candidates: Albert's certainty that Bernard cannot yet know rules out months containing a unique day, Bernard's subsequent knowledge rules out remaining ambiguous days, and Albert's final knowledge rules out remaining ambiguous months — leaving exactly one date.

## Task Requirements
- Encode the ten possible dates (May 15/16/19, June 17/18, July 14/16, August 14/15/17).
- Model Albert knowing only the month and Bernard knowing only the day.
- Apply the three statements as successive elimination steps:
  1. Albert knows Bernard doesn't know — eliminate months that contain any day appearing only once.
  2. After step 1, Bernard now knows — eliminate days that remain ambiguous.
  3. After step 2, Albert now knows — eliminate months that remain ambiguous.
- Output the single surviving date.

## Language Coverage
51 languages implement this task, showing broad coverage across functional, imperative, and scripting paradigms. Representative implementations include Python, Haskell, J, C++, Go, Rust, Java, JavaScript, Common Lisp, and Raku.

## Connections
- [[ConstraintSatisfaction]] — successive elimination over a candidate set
- [[EpistemicLogic]] — reasoning about what each agent knows and doesn't know
- [[DeductiveReasoning]] — the puzzle is solved by iterated logical inference
- [[SetFiltering]] — each statement is a filter over the remaining dates

## Contradictions
- None — reference task page.
