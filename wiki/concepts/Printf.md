---
title: "printf"
type: concept
tags: [c-language, stdlib, io]
sources: [dis-1-1-getting-started, dis-1-2-input-output]
last_updated: 2026-05-17
---

# printf

**`printf`** is the [[CLanguage|C]] standard-library **formatted-output** function, declared in [[StandardIOLibrary|`<stdio.h>`]]. It writes a [[FormatSpecifier|format-string]]-driven interpolation to [[StandardOutput|stdout]].

```c
#include <stdio.h>
int main(void) {
    char ch = 'A';
    printf("Hello, World!\n");
    printf("ch is %d which is the ASCII for %c\n", ch, ch);
    return 0;
}
```

## Defining properties

- **Does not auto-append a newline** (per [[dis-1-1-getting-started|DIS Ch 1.1]] and reinforced by [[dis-1-2-input-output|Ch 1.2]]). Explicit [[EscapeSequence|`\n`]] is required wherever Python's `print` would have added one.
- **Format-string-driven** (per [[dis-1-2-input-output|Ch 1.2]]). [[FormatSpecifier|`%`-specifiers]] inside the format string name the type and presentation of each subsequent argument:

| Specifier | Type |
|---|---|
| `%d` | decimal `int` (or `char` / `short` after promotion) |
| `%g` | `float` or `double` |
| `%s` | C string (`char *`) |
| `%c` | single `char` (printed as ASCII glyph) |

- **Matched arity.** Number and types of arguments must match the specifiers. Mismatches are undefined behavior (modern `gcc -Wall` catches many).
- **Same `char`, two displays.** `%d` prints the numeric code (`65`), `%c` prints the glyph (`A`).

## Key difference from Python's `print`

[[dis-1-1-getting-started|DIS Ch 1.1]] flags this explicitly: `printf` does not automatically append a newline. Python's `print` adds `\n` by default; the C programmer must put `\n` in the format string.

## Buffering caveat

When [[StandardOutput|`stdout`]] is connected to a terminal it is **line-buffered** (a `\n` flushes); when redirected to a pipe / file it is **fully buffered**. Mixing `printf` with [[Scanf|`scanf`]] sometimes needs an explicit `fflush(stdout)` to make a prompt appear before the read.

## Connections

- [[CLanguage]] — the language it belongs to.
- [[StandardIOLibrary]] — declared in `<stdio.h>`.
- [[HeaderFile]] — `<stdio.h>` is one.
- [[PreprocessorDirective]] — pulled in via `#include <stdio.h>`.
- [[Scanf]] — the input counterpart; shares the [[FormatSpecifier|specifier]] vocabulary.
- [[FormatSpecifier]] — `%d` / `%g` / `%s` / `%c`.
- [[EscapeSequence]] — `\n` is the most important; not added automatically.
- [[StandardOutput]] — the stream `printf` writes to.
- [[Python]] — the `print` contrast.
- [[dis-1-1-getting-started]] — first introduction.
- [[dis-1-2-input-output]] — full [[FormatSpecifier|specifier]] / [[EscapeSequence|escape]] treatment.
