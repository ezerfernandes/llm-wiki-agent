---
title: "Rosetta Code/Fix code tags (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, string-processing, text-processing, regular-expressions]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Rosetta_Code/Fix_code_tags
---

## Summary
This meta-task asks the programmer to write a converter that updates Rosetta Code's deprecated source-markup tags to the current MediaWiki syntax. Specifically, it must rewrite `<lang X>` tags into `<syntaxhighlight lang=X>`, turn closing `</lang>` tags into `</syntaxhighlight>`, and treat a bare `<lang>` (no language) as `lang=text`. The task was revised after Rosetta Code's August 2022 hosting change, which switched the wiki from the old `<lang>` convention to MediaWiki's standard `<syntaxhighlight>` extension.

## Task Requirements
- Change `<lang %s>` to `<syntaxhighlight lang=%s>` (carrying the language name through).
- Change `</lang>` to `</syntaxhighlight>`.
- Change a bare `<lang>` (no specified language) to `<syntaxhighlight lang=text>`.
- Demonstrate the conversion on the supplied example snippets.

## Language Coverage
33 languages implement this task. Coverage is broad across scripting and functional languages, with most solutions leaning on regular-expression substitution; representative entries include Python, Perl, Raku, Ruby, Go, Rust, JavaScript, OCaml, Racket, and REXX.

## Connections
- [[StringProcessing]] — the core operation is search-and-replace over text.
- [[RegularExpressions]] — the natural tool for matching and rewriting the tag patterns.
- [[TextProcessing]] — the task is categorized under text processing on Rosetta Code.
- [[MediaWiki]] — the migration targets MediaWiki's `<syntaxhighlight>` extension syntax.

## Contradictions
- None — reference task page.
