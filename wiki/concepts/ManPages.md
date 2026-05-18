---
title: "Man Pages"
type: concept
tags: [unix, documentation, c-language, posix]
sources: [dis-2-6-strings]
last_updated: 2026-05-17
---

# Man Pages

**Man pages** (short for *manual pages*) are the canonical [[Unix|UNIX]] documentation surface — terminal-readable reference pages for commands, system calls, C library functions, file formats, and configuration files. Per [[dis-2-6-strings|Ch 2.6]] of [[DiveIntoSystems]]:

> *"For more information about these and other C library functions … see their man pages. For example, to view the [[Strcpy|`strcpy`]] man page, run: `$ man strcpy`."*

## How to use

```bash
$ man strcpy            # show the manual page for strcpy
$ man 3 printf          # explicitly section 3 (library functions)
$ man -k string         # search short descriptions for "string"
$ man man               # the manual page for man itself
```

## Section conventions

Man pages are organized into numbered sections; the same name can have entries in multiple sections:

| Section | Contents |
|---|---|
| 1 | User commands (e.g. `ls`, `gcc`) |
| 2 | System calls (e.g. `open`, `read`) |
| 3 | Library functions (e.g. `printf`, `strcpy`) |
| 4 | Special files / devices (e.g. `null`, `tty`) |
| 5 | File formats (e.g. `passwd`, `fstab`) |
| 6 | Games |
| 7 | Miscellaneous (e.g. `signal`, `regex`) |
| 8 | System administration (e.g. `mount`, `cron`) |

The conventional citation form is `name(section)` — `printf(3)` is the library function, `printf(1)` is the shell command.

## Page structure

A typical man page contains: **NAME**, **SYNOPSIS** (function signature + required `#include`s), **DESCRIPTION**, **RETURN VALUE**, **ERRORS** ([[Errno|`errno`]] codes), **CONFORMING TO** (POSIX / C standard), **SEE ALSO**, **EXAMPLES** (sometimes). For [[StringLibrary|`<string.h>`]] functions, the SYNOPSIS tells the programmer the required header and the exact parameter types — *"the parameter formats, return values, and required headers"* per the [[dis-2-6-strings|Ch 2.6]] framing.

## Why the textbook flags it

The standard-library surface area is large; [[DiveIntoSystems]] does not attempt to enumerate every function. [[dis-2-6-strings|Ch 2.6]] introduces a representative slice (the [[Strncpy|`strncpy`]] / [[Strcmp|`strcmp`]] / [[Strcat|`strcat`]] / [[Strchr|`strchr`]] / [[Strstr|`strstr`]] / [[Strtok|`strtok`]] family) and routes the reader to `man` for the rest — making `man` part of the corpus's *active-reading-by-typing-the-code* discipline.

## Sources

- [[dis-2-6-strings]] — Ch 2.6 §2.6.3 routes readers to `man` for documentation on the broader [[StringLibrary|`<string.h>`]] surface area.
