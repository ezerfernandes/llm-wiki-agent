---
title: "fscanf (C)"
type: concept
tags: [c-language, stdlib, io, file-io]
sources: [dis-2-8-io]
last_updated: 2026-05-17
---

# fscanf

**`fscanf(fp, format, ...)`** is the [[CLanguage|C]] standard-library function — declared in [[StandardIOLibrary|`<stdio.h>`]] — that reads characters from a [[FilePointer|`FILE *`]], parses them per a [[FormatSpecifier|format string]], and stores the typed values at caller-provided addresses. The file-I/O sibling of [[Scanf|`scanf`]]. Per [[dis-2-8-io|DIS Ch 2.8]] §2.8.4.

```c
int x;
char c;
fscanf(infile, "%d,%c", &x, &c);
```

## Defining properties

- **First argument is a [[FilePointer|`FILE *`]].** Otherwise the format string and `&`-prefixed receivers are identical to [[Scanf|`scanf`]].
- **`scanf(fmt, ...)` ≡ `fscanf(stdin, fmt, ...)`.**
- **Returns the number of items successfully assigned**, or [[EOF|`EOF`]] on read error before any conversion.
- **Receivers are [[AddressOfOperator|`&`]]-prefixed addresses** — same rule [[dis-1-2-input-output|Ch 1.2]] established.

## Expanded specifier set (the Ch 2.8 deepening)

Beyond [[dis-1-2-input-output|Ch 1.2]]'s `%d` / `%g` / `%s` / `%c`:

| Specifier | Reads |
|---|---|
| `%lf` | `double` (vs. `%f` for `float`) |
| `%ld` / `%lld` | `long` / `long long` |
| `%Ns` (e.g. `%20s`) | string capped at `N` chars |
| `%[abc]` | string of characters **in** the set `{a,b,c}` |
| `%[^abc]` | string of characters **not in** the set |
| `%[^\n]` | everything up to (not including) newline |
| `%[0123456789]` | digits only |

The character-class and max-width forms are the [[Scanf|`scanf`]] **robustness fix** [[dis-1-2-input-output|Ch 1.2]] deferred — see [[ScanfCharClass]] for the full treatment.

## The trailing-character footgun

When mixing numeric and `%c` reads, the trailing newline left over from a numeric read becomes the next `%c`. The fix is to explicitly absorb it:

```c
fscanf(infile, "%ld %d%c", &x, &b, &c);  /* %c after %d eats the trailing char */
```

Numeric specifiers skip leading whitespace; `%c` does not.

## Connections

- [[Scanf]] — the [[StandardInput|`stdin`]]-specialized sibling.
- [[Fprintf]] — the writer counterpart.
- [[FilePointer]] — the source type.
- [[FormatSpecifier]] — the format-string vocabulary.
- [[ScanfCharClass]] — the `%[...]` / max-width extension specifier set.
- [[AddressOfOperator]] — `&`-prefix required on receivers.
- [[EOF]] — the error-return sentinel.
- [[StandardIOLibrary]] — declares the function.
- [[dis-2-8-io]] — introducing source.
