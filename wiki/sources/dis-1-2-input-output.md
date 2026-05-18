---
title: "Dive into Systems — Ch 1.2 Input/Output (printf and scanf)"
type: source
tags: [book, dive-into-systems, c-language, io]
date: 2026-05-17
source_file: https://diveintosystems.org/book/C1-C_intro/input_output.html
---

## Summary

Section 1.2 of [[DiveIntoSystems]] introduces hosted [[CLanguage|C]] I/O via the [[StandardIOLibrary|`<stdio.h>`]] pair [[Printf|`printf`]] / [[Scanf|`scanf`]]. The chapter formalizes the [[FormatSpecifier|format-string + placeholder]] model (`%d`, `%g`, `%s`, `%c`), the matched-arity rule between specifiers and arguments, and the [[EscapeSequence|`\n`-not-automatic]] property of `printf`. It then introduces the [[AddressOfOperator|address-of operator `&`]] — needed because [[Scanf|`scanf`]] must be told **where** to deposit the value it reads, not just **what type** to read — and surveys `scanf`'s whitespace-skipping behavior, multi-value reads, and its [[Scanf|brittleness]] under malformed user input. The section is the *minimum hosted-I/O machinery* the rest of Ch 1 ([[dis-1-1-getting-started|control flow]] / arrays / strings / pointers) needs to actually be interactive.

## Key Claims

- **`printf` and `scanf` are the two basic hosted-I/O calls** in [[CLanguage|C]], declared in [[StandardIOLibrary|`<stdio.h>`]] — `printf` writes formatted text to [[StandardOutput|stdout]], `scanf` reads formatted input from [[StandardInput|stdin]].
- **Output is format-string-driven**: `printf("...", arg1, arg2, ...)` interpolates each [[FormatSpecifier|placeholder]] (`%d` int, `%g` float/double, `%s` string, `%c` char) with the corresponding argument. **The number of placeholders must match the number of arguments**, and types must match.
- **`printf` does NOT auto-append a newline** — unlike [[Python]]'s `print`. The programmer must put [[EscapeSequence|`\n`]] in the format string explicitly. Restated and reinforced from [[dis-1-1-getting-started|Ch 1.1]].
- **The same character can be printed two ways**: `%d` prints the **numeric code** of a `char` (`65` for `'A'`); `%c` prints it as the **ASCII glyph** (`A`). A `char` is an integer all the way down; the specifier picks the display.
- **`scanf` requires the [[AddressOfOperator|address-of operator `&`]]** in front of each receiver variable — `scanf("%d", &num1)` — because the function needs the **memory address** at which to store the value it reads, not the variable's current value. The book's first sighting of an [[CMemoryAddress|address as a first-class value]].
- **`scanf` skips leading and trailing whitespace** (spaces, tabs, newlines) between numeric reads — so multi-value calls like `scanf("%d%g", &x, &pi)` accept arbitrary whitespace between user inputs.
- **`scanf` is fragile to malformed input** — providing a non-numeric character where a number is expected can leave the program in a bad state, sometimes spinning until interrupted with **Ctrl-C**. Robust user input requires the more elaborate techniques in Ch 2's I/O section.
- **Python ≠ C input model**: Python's `input()` returns a **string** the program must explicitly convert (`int(...)`, `float(...)`); C's `scanf` directly parses **typed** values into typed memory locations via the [[FormatSpecifier|format string]].

## Key Quotes

> "The caller specifies a format string to print." — frames [[Printf|`printf`]] / [[Scanf|`scanf`]] as **format-string-driven** rather than value-driven, the principle that organizes every later [[FormatSpecifier|`%`-conversion]] discussion.

> "The `&` operator produces the location of that variable in the program's memory — the memory address of the variable." — the textbook's first formal introduction of the [[AddressOfOperator|address-of operator]] and, transitively, of [[CMemoryAddress|memory addresses as values]] — the conceptual root the later pointer chapter will graft onto.

> "`scanf` can be a bit picky about the exact format in which the user enters data." — explicit acknowledgment that [[Scanf|`scanf`]] is *fragile by design*; the chapter recommends Ctrl-C for the resulting hangs and forward-references Ch 2 for production input handling.

## Worked examples

Two-faced character display (`%d` vs `%c`):

```c
#include <stdio.h>
int main(void) {
    char ch = 'A';
    printf("ch value is %d which is the ASCII value of  %c\n", ch, ch);
    /* Output: ch value is 65 which is the ASCII value of  A */
    return 0;
}
```

Single-value read with `&`:

```c
int num1;
printf("Enter a number: ");
scanf("%d", &num1);   /* store the int at num1's address */
```

Multi-value read with whitespace-skipping:

```c
int x;
float pi;
scanf("%d%g", &x, &pi);   /* user types: 42  3.14   — any whitespace OK */
```

## Connections

- [[DiveIntoSystems]] — the book; this is Ch 1.2.
- [[dis-1-1-getting-started]] — Ch 1.1; provided `printf`/`#include`/`main`; this section adds **input** and **address-of**.
- [[SuzanneJMatthews]] / [[TiaNewhall]] / [[KevinCWebb]] — co-authors.
- [[CLanguage]] — the language.
- [[StandardIOLibrary]] — `<stdio.h>`; declares both `printf` and `scanf`.
- [[HeaderFile]] — `<stdio.h>` is one; [[PreprocessorDirective|`#include <stdio.h>`]] pulls it in.
- [[Printf]] — output side; updated by this section with the [[FormatSpecifier|`%`-specifier]] / [[EscapeSequence|`\n`-is-explicit]] story.
- [[Scanf]] — input side; **new in this section**.
- [[FormatSpecifier]] — `%d` / `%g` / `%s` / `%c`; the shared vocabulary of both functions.
- [[EscapeSequence]] — `\n` / `\t` / `\\` / `\"`; backslash-prefixed character codes inside string literals.
- [[AddressOfOperator]] — unary `&`; produces the memory address of a variable. **New in this section** — first time the book treats an address as a value.
- [[CMemoryAddress]] — the abstract concept the `&` operator names; the foundation for the later pointer chapter.
- [[StandardInput]] — the default input stream `scanf` reads from.
- [[StandardOutput]] — the default output stream `printf` writes to.
- [[CPrimitiveType]] — the types `%d` / `%g` / `%s` / `%c` correspond to; `'A'` is a `char` with value 65.
- [[Python]] — contrast: Python `input()` returns a string requiring explicit conversion; C `scanf` parses typed values directly.

## Contradictions

- None with existing wiki content. This section **extends** the [[Printf]] page from [[dis-1-1-getting-started]] (which mentioned `printf` only briefly) with the full [[FormatSpecifier|specifier]] vocabulary, and **adds** [[Scanf]] / [[AddressOfOperator]] / [[StandardInput]] / [[StandardOutput]] / [[EscapeSequence]] / [[FormatSpecifier]] as net-new concepts. Complementary to the embedded-Rust track's [[ARMSemihosting|semihosting]] I/O — both are *hosted* I/O models in the sense that they assume something on the other side of the call (an [[OperatingSystem|OS]] for `printf`, a debug probe for semihosting); they differ in *who* hosts.
