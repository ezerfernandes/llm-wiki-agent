---
title: "Format Specifier (C)"
type: concept
tags: [c-language, stdlib, io]
sources: [dis-1-2-input-output]
last_updated: 2026-05-17
---

# Format Specifier (C)

A **format specifier** is a `%`-prefixed conversion token inside a [[CLanguage|C]] [[StandardIOLibrary|`<stdio.h>`]] format string that names the type and presentation of one interpolated value. Used identically by [[Printf|`printf`]] on output and [[Scanf|`scanf`]] on input.

## Core specifiers introduced in [[dis-1-2-input-output|DIS Ch 1.2]]

| Specifier | Type | Notes |
|---|---|---|
| `%d` | decimal `int` (also `short` / `char` after default promotion) | prints / reads as base-10 integer; for a `char`, displays the numeric ASCII code |
| `%g` | `float` or `double` | floating-point; chooses between fixed and scientific automatically |
| `%s` | C string (`char *`) | null-terminated character array |
| `%c` | single `char` | displays as the ASCII **glyph**, not the numeric code |

The same `char` value can therefore appear two ways:

```c
char ch = 'A';
printf("ch value is %d which is the ASCII value of  %c\n", ch, ch);
/* ch value is 65 which is the ASCII value of  A */
```

## The matched-arity rule

The number of `%`-specifiers in the format string **must equal** the number of arguments that follow it, and each argument's type must match its specifier. Mismatches are not caught by every compiler at the language level (modern `gcc -Wall` catches many) and silently corrupt output or memory at runtime.

## In `scanf` vs `printf`

- In [[Printf|`printf`]], the argument is the **value** to display.
- In [[Scanf|`scanf`]], the argument is the **address** ([[AddressOfOperator|`&var`]]) of the variable to fill — the specifier names *what type to parse* and the address names *where to store the result*.

## Beyond the chapter

The standard provides many more specifiers (`%i`, `%u`, `%x`, `%o`, `%e`, `%f`, `%p`, `%ld`, `%lld`, `%zu`, width / precision / flag modifiers) — Ch 1.2 intentionally limits the introductory surface to four; later chapters extend it.

## Connections

- [[Printf]] — output-side consumer.
- [[Scanf]] — input-side consumer; same specifiers, address-of arguments.
- [[StandardIOLibrary]] — where both functions are declared.
- [[CPrimitiveType]] — types the specifiers correspond to (`int` ↔ `%d`, `double` ↔ `%g`, `char` ↔ `%c`).
- [[EscapeSequence]] — the other class of `%`-free magic tokens inside a format string (backslash-prefixed character codes).
- [[CLanguage]] — the language.
- [[dis-1-2-input-output]] — introducing source.
