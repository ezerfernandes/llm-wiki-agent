---
title: "Transliterate English text using the Greek alphabet (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, string-processing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Transliterate_English_text_using_the_Greek_alphabet
---

## Summary
A playful string-substitution exercise that maps English text onto the Greek alphabet using an approximate, context-sensitive phonetic ruleset. The key insight is that the mapping is not one-to-one: many Greek letters cover multiple English spellings (e.g. eta for "h" or "ee", chi for "ch" or "kh"), and digraphs like "th", "ph", "ps", "ch", and "ck" must be matched before single letters, making it essentially a longest-match transliteration problem.

## Task Requirements
- Apply the given Greek-letter-to-English-letter(s) substitution table to transliterate English text.
- Honor the digraph rules and exclusions (e.g. "th" maps to theta, but plain "t" maps to tau; "ee" maps to eta, not double epsilon).
- Use final sigma "ς" when "s" ends an English word, and "σ" otherwise.
- Ignore Greek diacritics, but preserve the original capitalization, spacing, and punctuation.
- Transliterate the supplied multi-line passage (or the fallback pangram "sphinx of black quartz, judge my vow." with bracketed letter names if non-ASCII output is unsupported).

## Language Coverage
23 languages implement this task, a moderate spread spanning scripting, functional, BASIC-family, and mathematical languages. Representative entries include Python, Perl, Raku, Ruby, Java, JavaScript, Julia, J, Nim, Phix, and Wren.

## Connections
- [[StringSubstitution]] — the core operation of replacing English letter sequences with Greek glyphs
- [[Transliteration]] — the broader named technique of mapping text between writing systems
- [[LongestMatchRule]] — multi-character digraphs must be matched ahead of single letters
- [[UnicodeHandling]] — emitting non-ASCII Greek characters and final-sigma casing

## Contradictions
- None — reference task page.
