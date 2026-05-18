---
title: "Exit Status"
type: concept
tags: [c-language, operating-systems, processes]
sources: [dis-1-1-getting-started]
last_updated: 2026-05-17
---

# Exit Status

The **exit status** of a process is the integer it returns to its parent (typically the shell or another launcher) when it terminates. In a [[CLanguage|C]] program this is the value returned from [[MainFunction|`main`]] — or passed to `exit()`.

Convention ([[dis-1-1-getting-started|DIS Ch 1.1]]):

- **`0` = success** — *"running to completion without error."*
- **Non-zero = error**, with specific non-zero values free for the program to define as it likes (Unix tools often use `1` for general errors, `2` for misuse, and so on).

The shell exposes the last command's exit status as `$?`:

```sh
$ ./hello && echo ok || echo failed
```

Standard library helpers `EXIT_SUCCESS` (= `0`) and `EXIT_FAILURE` (= `1`), defined in [[HeaderFile|`<stdlib.h>`]], make the intent explicit.

## Connections

- [[MainFunction]] — the source of this integer in a typical C program.
- [[CLanguage]] — the host language.
- [[BinaryExecutable]] — the artifact whose process produces the status.
- [[OperatingSystem]] — the consumer of the status.
- [[dis-1-1-getting-started]] — introducing source.
