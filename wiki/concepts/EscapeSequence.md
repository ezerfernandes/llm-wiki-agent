---
title: "Escape Sequence (C)"
type: concept
tags: [c-language, syntax, io]
sources: [dis-1-2-input-output]
last_updated: 2026-05-17
---

# Escape Sequence

An **escape sequence** in a [[CLanguage|C]] string or character literal is a **backslash-prefixed token** that stands in for a single character — usually one that cannot be typed literally inside quotes (newline, tab) or that would otherwise terminate the literal (quote, backslash).

[[dis-1-2-input-output|DIS Ch 1.2]] foregrounds the most important one: **`\n`** — `printf` does not append a newline automatically, so `"hello\n"` is required to advance the cursor. Restated and made operational from [[dis-1-1-getting-started|Ch 1.1]].

## Common escape sequences

| Sequence | Meaning |
|---|---|
| `\n` | newline (LF, 0x0A) |
| `\t` | horizontal tab (0x09) |
| `\\` | a literal backslash |
| `\"` | a literal `"` inside `"..."` |
| `\'` | a literal `'` inside `'...'` |
| `\0` | the null character (string terminator) |
| `\r` | carriage return |

A character literal `'\n'` is a single `char` of numeric value 10; a string literal `"\n"` is a two-byte array containing the byte `'\n'` and the `'\0'` terminator — the same `'h'`-vs-`"h"` shape as in [[dis-1-1-getting-started|Ch 1.1]]'s [[CPrimitiveType]] discussion.

## Distinction from [[FormatSpecifier|format specifiers]]

A format string mixes two classes of magic tokens:

| Token | Prefix | Resolved by | Example |
|---|---|---|---|
| Escape sequence | `\` | compiler / preprocessor (at compile time) | `\n`, `\t` |
| [[FormatSpecifier|Format specifier]] | `%` | `printf` / `scanf` (at run time) | `%d`, `%c` |

The escape sequence is baked into the binary as a literal byte; the format specifier is interpreted on every call.

## Connections

- [[CLanguage]] — the language.
- [[Printf]] / [[Scanf]] — the chapter's I/O functions whose format strings carry escape sequences.
- [[FormatSpecifier]] — the other class of in-string magic; resolved at run time, not compile time.
- [[CPrimitiveType]] — `'\n'` is a 1-byte `char`; `"\n"` is a 2-byte string literal.
- [[dis-1-2-input-output]] — introducing source.
