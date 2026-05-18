---
title: "Standard I/O Library (<stdio.h>)"
type: concept
tags: [c-language, stdlib, io]
sources: [dis-1-1-getting-started, dis-1-2-input-output]
last_updated: 2026-05-17
---

# Standard I/O Library (`<stdio.h>`)

**`<stdio.h>`** is the [[CLanguage|C]] standard library [[HeaderFile|header]] declaring the language's hosted I/O surface — formatted I/O ([[Printf|`printf`]] / [[Scanf|`scanf`]] / `fprintf` / `fscanf` / `sprintf` / `sscanf`), character I/O (`getchar` / `putchar` / `fgetc` / `fputc`), line I/O (`fgets` / `fputs`), file management (`fopen` / `fclose` / `fread` / `fwrite` / `fseek`), and the three default streams [[StandardInput|`stdin`]] / [[StandardOutput|`stdout`]] / `stderr`.

[[dis-1-1-getting-started|DIS Ch 1.1]] introduces the header via the canonical first line of every C program:

```c
#include <stdio.h>
```

[[dis-1-2-input-output|DIS Ch 1.2]] uses it for both halves of the I/O pair — `printf` for output and `scanf` for input.

## Why it's special

`<stdio.h>` is the part of the C standard library that *assumes a [[OperatingSystem|host OS]]*. On hosted platforms it is always available; on freestanding / [[BareMetalProgramming|bare-metal]] platforms (the [[TheEmbeddedRustBook|embedded Rust]] world, or C with [[NoStd|`-ffreestanding`]]) it isn't — there is no `stdin` or `stdout`. This is the load-bearing distinction between [[DiveIntoSystems]]' world (hosted, OS-backed `printf`) and the embedded-Rust track's ([[ARMSemihosting|semihosting]] in place of a [[OperatingSystem|kernel]]).

## Connections

- [[HeaderFile]] — `<stdio.h>` is the canonical example.
- [[PreprocessorDirective]] — pulled in by `#include <stdio.h>`.
- [[Printf]] / [[Scanf]] — the two functions Ch 1.1 and Ch 1.2 take from it.
- [[StandardInput]] / [[StandardOutput]] — the streams it exposes.
- [[CLanguage]] — the language.
- [[OperatingSystem]] — the host the library calls into.
- [[ARMSemihosting]] — the no-OS embedded-world counterpart.
- [[dis-1-1-getting-started]] — first appearance via `printf`.
- [[dis-1-2-input-output]] — full I/O-pair treatment.
