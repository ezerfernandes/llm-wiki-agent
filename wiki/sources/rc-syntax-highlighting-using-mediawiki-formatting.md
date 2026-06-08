---
title: "Syntax highlighting using Mediawiki formatting (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, string-processing, lexical-analysis, text-formatting]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Syntax_highlighting_using_Mediawiki_formatting
---

## Summary
The task asks the programmer to write a lightweight syntax highlighter that emits MediaWiki-formatted markup rather than HTML. Given a source file, the program wraps keywords/reserved words in bold (triple single-quotes) and comments in italics (double single-quotes), using MediaWiki's repeated-apostrophe convention. The key insight is that this offers cheap highlighting without the costly `<syntaxhighlight>` tag, useful for languages not supported by Pygments. Crucially, the highlighter must be self-hosting: it is demonstrated by running it on its own source.

## Task Requirements
- Identify keywords/reserved words in the source and wrap them in MediaWiki bold (`'''...'''`).
- Identify comments and wrap them in MediaWiki italics (`''...''`).
- Prefix every source line (including blank lines) with a leading space so the wiki renders the whole thing as one preformatted block.
- Escape four characters: single-quote to `&apos;`, ampersand to `&amp;`, less-than to `&lt;`, greater-than to `&gt;`.
- Present the result by showing the highlighter's own source as processed by itself, without using `<syntaxhighlight>` tags.
- For languages lacking keywords or comments, use judgement about what to bold or italicize.

## Language Coverage
18 languages implement this task, spanning classic structured languages, scripting languages, and a few niche or esoteric entries. Representative implementations include ALGOL 68, ALGOL W, AWK, FreeBASIC, Julia, Perl, Phix, Python, Raku, Wren, and the line-editor language ed.

## Connections
- [[LexicalAnalysis]] — scanning source text into keyword, comment, and literal tokens
- [[StringProcessing]] — character escaping and markup insertion
- [[MediaWiki]] — the target markup syntax being generated
- [[Quine]] — related self-hosting idea, since the highlighter processes its own source
- [[CharacterEscaping]] — translating reserved characters into HTML entities

## Contradictions
- None — reference task page.
