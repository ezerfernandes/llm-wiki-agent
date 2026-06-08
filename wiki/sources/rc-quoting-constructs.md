---
title: "Quoting constructs (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, string-processing, language-design]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Quoting_constructs
---

## Summary
This open-ended survey task asks implementers to catalog and explain the quoting constructs their language offers for embedding literal data — primarily strings, but also numbers and combinations — directly into source code. Rather than producing a single algorithm, each entry is a comprehensive prose summary of the available delimiters and their trade-offs. The central insight is that quoting design varies widely across languages along axes such as interpolation, escaping, multiline support, and heredoc availability.

## Task Requirements
- Show the quoting constructs available in the chosen language.
- Explain where each is typically used and its primary purpose.
- Describe limitations and reasons to prefer one style over another.
- Address whether a style interpolates (substitutes variables/expressions) versus being a raw/literal quote.
- Note any restrictions on the size, type, or format of the quoted data.
- Keep it self-contained: summarize comprehensively on the page rather than only linking to external language docs, while linking out for exhaustive detail.

## Language Coverage
33 languages implement this task, spanning assembly, BASIC dialects, functional and array languages, and modern scripting and systems languages. Representative entries include Perl, Raku, Java, C++, Go, Julia, Nim, Lua, J, BQN, and REXX, reflecting how differently quoting is handled from low-level assemblers to expressive scripting languages.

## Connections
- [[StringLiteral]] — the core construct being surveyed across languages
- [[StringInterpolation]] — distinguishes interpolating quotes from raw/literal ones
- [[Heredoc]] — multiline embedded-data syntax discussed by several entries
- [[EscapeSequence]] — escaping mechanisms that interact with delimiter choice
- [[LexicalAnalysis]] — how parsers recognize and delimit quoted tokens

## Contradictions
- None — reference task page.
