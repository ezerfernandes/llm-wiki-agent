---
title: "Magic 8-ball (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, random-number-generation]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Magic_8-ball
---

## Summary
This task asks the programmer to simulate the classic Magic 8-Ball toy: prompt the user for a yes/no question, then return one of the toy's fixed set of canned fortune-telling answers chosen at random. The core insight is trivial — uniformly pick a random element from a fixed list of response strings — making it an introductory exercise in random selection and basic user I/O.

## Task Requirements
- Re-create the Magic 8-Ball experience (referencing the Wikipedia description of the toy).
- Accept a question from the user.
- Respond with a randomly selected answer drawn from the standard pool of 20 possible Magic 8-Ball replies (e.g. "It is certain", "Reply hazy, try again", "Don't count on it").

## Language Coverage
83 languages implement this task, spanning a very broad range from low-level assembly to scripting and functional languages. Representative implementations include C, C++, Python, Java, JavaScript, Ruby, Rust, Go, Haskell, Perl, and several BASIC dialects.

## Connections
- [[RandomNumberGeneration]] — selecting a uniformly random response index
- [[PseudorandomNumberGenerator]] — the typical source of randomness
- [[StandardInputOutput]] — prompting for and reading the user's question

## Contradictions
- None — reference task page.
