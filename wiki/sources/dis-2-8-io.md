---
title: "Dive into Systems — Ch 2.8 Input / Output in C"
type: source
tags: [book, textbook, c, io, file-io, stdio, systems]
date: 2026-05-17
source_file: https://diveintosystems.org/book/C2-C_depth/IO.html
---

## Summary

Chapter 2.8 of *[[DiveIntoSystems]]* by [[SuzanneJMatthews|Matthews]] / [[TiaNewhall|Newhall]] / [[KevinCWebb|Webb]] returns to [[CLanguage|C]] **input / output** with the depth [[dis-1-2-input-output|Ch 1.2]] deferred. The chapter is in three movements: (1) a deepened recap of **standard I/O** — the three default streams ([[StandardInput|`stdin`]] / [[StandardOutput|`stdout`]] / [[StandardError|`stderr`]]), shell **stream redirection** (`< > 2>`), and an expanded [[FormatSpecifier|format-specifier]] table for [[Printf|`printf`]] / [[Scanf|`scanf`]] including width / precision / justification modifiers; (2) the full **file-I/O** API on top of [[FilePointer|`FILE *`]] — [[Fopen|`fopen`]] / [[Fclose|`fclose`]], the [[FileMode|mode strings]] `"r"` / `"w"` / `"a"`, the four function families [[Fgetc|`fgetc`]]/[[Fputc|`fputc`]], [[Fgets|`fgets`]]/[[Fputs|`fputs`]], [[Fprintf|`fprintf`]]/[[Fscanf|`fscanf`]], and position primitives [[Fseek|`fseek`]] / [[Rewind|`rewind`]]; (3) the **expanded `fscanf` specifier set** — [[ScanfCharClass|`%[...]`]] / `%[^...]` / `%20s` character-class and width specs that fix the [[Scanf|fragility]] [[dis-1-2-input-output|Ch 1.2]] warned about. The headline payoff is the **standard-I/O ↔ file-I/O symmetry**: `printf`/`fprintf`, `scanf`/`fscanf`, `getchar`/`fgetc`, `putchar`/`fputc` differ only in whether they take an explicit [[FilePointer|`FILE *`]] argument — `stdin`/`stdout`/`stderr` *are* `FILE *` values, making the standard streams a special case of the file API.

## Key Claims

- **Three default streams.** Every running process begins with [[StandardInput|`stdin`]] (FD 0), [[StandardOutput|`stdout`]] (FD 1), and [[StandardError|`stderr`]] (FD 2) opened by the shell. All three are [[FilePointer|`FILE *`]] values exposed by [[StandardIOLibrary|`<stdio.h>`]].
- **Shell-level redirection** rebinds these streams without any code change: `./a.out < in.txt`, `./a.out > out.txt`, `./a.out &> all.txt`, `./a.out < in 1> out 2> err`.
- **Expanded `printf` specifiers.** Beyond [[dis-1-2-input-output|Ch 1.2]]'s `%d`/`%g`/`%s`/`%c`: `%u` (unsigned), `%p` (pointer/address), `%ld` (long), `%lld` (long long), `%x` (hex), `%o` (octal), `%e` (scientific), plus **width / precision / justification** modifiers (`%5.3f`, `%20s`, `%-20s`, `%-8d`).
- **A file is a persistent character stream with a current position.** The [[EOF|`EOF`]] sentinel signals end-of-file; functions returning a character return [[CPrimitiveType|`int`]] (not `char`) precisely so they can also return [[EOF|`EOF`]] without aliasing a valid byte.
- **The [[FilePointer|`FILE *`]] four-step protocol.** (1) declare `FILE *fp;`; (2) [[Fopen|`fopen("path", mode)`]] returning [[NullPointer|`NULL`]] on failure (always check); (3) do I/O with the `f*` functions; (4) [[Fclose|`fclose(fp)`]] to release.
- **Three [[FileMode|file modes]]**: `"r"` (read — fails if file missing), `"w"` (write — truncates / creates), `"a"` (append — creates if needed, writes at end).
- **Standard ↔ file symmetry.** Each standard-I/O function has a file-I/O sibling that takes a [[FilePointer|`FILE *`]] first argument: `printf` ↔ [[Fprintf|`fprintf`]], `scanf` ↔ [[Fscanf|`fscanf`]], `getchar` ↔ [[Fgetc|`fgetc`]], `putchar` ↔ [[Fputc|`fputc`]]. The standard streams are just three pre-opened `FILE *` values — `fprintf(stdout, ...)` is `printf(...)`.
- **String-level I/O**: [[Fgets|`fgets(s, n, f)`]] reads up to `n-1` chars, stops at newline (inclusive) or EOF, always [[NullTerminator|null-terminates]] — the **robust line reader** that [[Scanf|`scanf`]] is not. [[Fputs|`fputs(s, f)`]] writes a string without auto-newline.
- **File position primitives.** [[Rewind|`rewind(f)`]] resets to start; [[Fseek|`fseek(f, offset, whence)`]] with `SEEK_SET` / `SEEK_CUR` / `SEEK_END` does arbitrary positioning.
- **Expanded `fscanf` specifiers fix [[Scanf|`scanf`]] fragility.** [[ScanfCharClass|`%[abc]`]] reads only characters in the set; `%[^abc]` reads characters *not* in the set; `%[^\n]` reads everything up to (but not including) the next newline; `%20s` caps a string read at 20 chars. The character-class / max-width forms give the precise control [[dis-1-2-input-output|Ch 1.2]] deferred.
- **The trailing-character footgun**: when mixing numeric and `%c` reads, you must explicitly consume the trailing `\n` — `fscanf("%ld %d%c", &x, &b, &c)` — because numeric specifiers skip leading whitespace but `%c` does not.
- **`stderr` is for diagnostics.** `fprintf(stderr, "Error: %d\n", ret)` — separating error output from `stdout` so it survives `> file` redirection of the normal output.
- **Character-I/O functions return `int`, not `char`.** [[Fgetc|`fgetc`]] / [[Getchar|`getchar`]] return `int` so they can encode [[EOF|`EOF`]] (a value distinct from any of the 256 possible byte values). Storing the result in `char ch = fgetc(f);` *before* the EOF test is a corpus-wide bug — [[EOF|`EOF`]] truncates to a valid byte.

## Key Quotes

> "A file stores persistent data beyond program execution." — §2.8.2, the framing distinction between a transient process and a file.

> "Every running program begins with three default I/O streams: `stdin`, `stdout`, `stderr`." — §2.8.1, the universally-inherited shell convention.

> "When mixing numeric and character reads with `fscanf`, explicitly reading the trailing character (often `\n`) ensures proper stream position for subsequent calls." — the §2.8.4 footgun.

> "EOF is `int`, not `char`." — the load-bearing reason every character-I/O function in the chapter returns `int`.

## Connections

### Source position

- [[DiveIntoSystems]] — the textbook this section belongs to.
- [[dis-1-2-input-output]] — **Ch 1.2 *Input/Output (`printf` and `scanf`)*** — this chapter is the *deeper return*. Ch 1.2 introduced the I/O-pair vocabulary ([[FormatSpecifier|`%`-specifiers]] + [[AddressOfOperator|`&`]] + [[StandardInput|`stdin`]] / [[StandardOutput|`stdout`]]) and flagged [[Scanf|`scanf`]] fragility as *"deferred to Ch 2"* — Ch 2.8 now delivers (1) the expanded specifier vocabulary, (2) the file-I/O surface area, (3) the [[ScanfCharClass|`%[...]`]] / max-width forms that fix the fragility.
- [[dis-2-7-structs]] — the prior section. Ch 2.7 closed the *struct* story; Ch 2.8 opens the *I/O* story.

### Standard-I/O surface (updated / deepened)

- [[Printf]] / [[Scanf]] / [[StandardIOLibrary]] / [[StandardInput]] / [[StandardOutput]] — Ch 1.2 introductions, deepened here with width / precision / justification modifiers and the full specifier table (`%u` / `%p` / `%ld` / `%lld` / `%x` / `%o` / `%e`).
- [[FormatSpecifier]] — extended with the width / precision / justification syntax.
- [[Getchar]] / [[Putchar]] — single-character standard-stream I/O, the per-byte primitives Ch 1.2 left out.
- [[StandardError]] — the third default stream, used for diagnostics so they survive `> file` redirection of `stdout`.
- [[StreamRedirection]] — the shell-level `<` / `>` / `2>` / `&>` mechanism that rebinds the three default streams without recompilation.

### File-I/O surface (new)

- [[FilePointer]] (`FILE *`) — the opaque handle type that abstracts both files and standard streams.
- [[Fopen]] / [[Fclose]] — open-and-close lifecycle. `fopen` returns [[NullPointer|`NULL`]] on failure (must check); `fclose` releases the resource.
- [[FileMode]] — the `"r"` / `"w"` / `"a"` mode strings to `fopen`.
- [[Fgetc]] / [[Fputc]] — single-character file I/O; the `getchar`/`putchar` siblings.
- [[Fgets]] / [[Fputs]] — line / string file I/O; [[Fgets|`fgets`]] is the **robust line reader** that fixes [[Scanf|`scanf`]]'s `%s` whitespace problem.
- [[Fprintf]] / [[Fscanf]] — formatted file I/O; the `printf`/`scanf` siblings.
- [[EOF]] — the end-of-file sentinel returned by character-reading functions; an [[CPrimitiveType|`int`]] distinct from any byte value.
- [[Feof]] — predicate to check whether a [[FilePointer|`FILE *`]] has hit end-of-file.
- [[Ungetc]] — pushes a character back onto a stream for re-reading.
- [[Fseek]] / [[Rewind]] — file position primitives; `SEEK_SET` / `SEEK_CUR` / `SEEK_END` whence anchors.
- [[ScanfCharClass]] — the `%[abc]` / `%[^abc]` / `%[^\n]` character-class specifier and the `%20s` max-width form — the [[dis-1-2-input-output|Ch 1.2]]-deferred robust-input fix.

### Cross-references

- [[CLanguage]] — the language.
- [[FileIO]] — the concept name (already populated for ML-framework tensor save/load; the C-level treatment lives in [[FilePointer]] and the `F*` concept pages).
- [[NullPointer]] — `fopen` returns it on failure; every call site must test.
- [[NullTerminator]] — `fgets` always appends it, in contrast to [[Strncpy|`strncpy`]]'s non-termination footgun.
- [[OperatingSystem]] — the entity that opens the three default streams when the shell `exec`s the process.

## Contradictions

None with existing wiki pages. **Reframes** the [[StandardInput|`stdin`]] / [[StandardOutput|`stdout`]] / [[StandardError|`stderr`]] streams from "OS-level abstractions wrapped by the C library" ([[dis-1-2-input-output|Ch 1.2]]) into "three pre-opened [[FilePointer|`FILE *`]] values exposed by [[StandardIOLibrary|`<stdio.h>`]]" — the same statement at a more concrete level. **Resolves** the [[Scanf|`scanf`]]-fragility deferral [[dis-1-2-input-output|Ch 1.2]] flagged: the robust recipe is [[Fgets|`fgets`]] + `sscanf`, and the [[ScanfCharClass|`%[...]`]] / `%Ns` specifiers give per-field bounded input.
