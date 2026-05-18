---
title: "C Primitive Types"
type: concept
tags: [c-language, types, numeric]
sources: [dis-1-1-getting-started]
last_updated: 2026-05-17
---

# C Primitive Types

The **primitive numeric types** of [[CLanguage|C]] as introduced in [[dis-1-1-getting-started|DIS Ch 1.1]]:

| Type | Bytes | Range / use |
|---|---|---|
| `char` | 1 | small integer / single ASCII character |
| `short` | 2 | signed integer |
| `int` | 4 | signed integer (the default integer type) |
| `long` | 4 or 8 | signed integer (**platform-dependent**) |
| `long long` | 8 | signed integer |
| `float` | 4 | single-precision real |
| `double` | 8 | double-precision real |

Each integer type also has an **`unsigned`** variant (`unsigned int`, `unsigned char`, …) that omits the sign bit and doubles the positive range.

The [[SizeOf|`sizeof`]] operator returns the byte width at compile time: `sizeof(int)` → `4` on a typical platform.

## `'h'` vs `"h"` — char vs. string

A subtle but load-bearing distinction Ch 1.1 makes explicit:

- `'h'` — a single-byte `char` literal (numeric value `104`, the ASCII code for *h*).
- `"h"` — a two-byte **string literal** (the byte `'h'` followed by the null terminator `'\0'`).

The two have different types and different sizes; mixing them silently is a common beginner bug.

## `long` is the wart

`long`'s width is **platform-dependent** — typically 4 bytes on 32-bit and Windows-64, 8 bytes on most 64-bit Unix systems. Code that needs a specific width should use the `<stdint.h>` fixed-width types (`int32_t`, `int64_t`, …) introduced later in the book.

## Connections

- [[CLanguage]] — the host language.
- [[VariableDeclaration]] — uses these type names on its left-hand side.
- [[SizeOf]] — measures these types' widths.
- [[CArithmeticOperators]] — operate on values of these types.
- [[IntegerDivision]] — the integer/float subset distinction matters here.
- [[BinaryRepresentation]] — these types are the C-programmer-visible face of binary integer / float encodings, the next chapter's topic.
- [[dis-1-1-getting-started]] — introducing source.
