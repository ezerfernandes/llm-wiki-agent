---
title: "Unix Command Line"
type: concept
tags: [unix, shell, command-line]
sources: [dis-app2-1-cmdline-basics]
last_updated: 2026-05-18
---

# Unix Command Line

The **Unix command line** is the text-based interface to a Unix-family operating system, mediated by a **shell** program (commonly `bash` or `zsh`) that runs a *read-eval-print loop*: read a line, parse and execute the command, print output, repeat. The prompt is conventionally `$`.

Per [[dis-app2-1-cmdline-basics|Appendix 2.1]] of [[DiveIntoSystems]], the shell exposes a small, sharp command vocabulary over the [[UnixFileSystem|Unix file system]].

## Core command vocabulary

| Category | Commands |
|---|---|
| Navigation | `pwd`, `cd`, `ls` |
| Directory mgmt | `mkdir`, `rmdir` |
| File mgmt | `cp`, `mv`, `rm`, `touch` |
| Viewing | `cat`, `less`, `more`, `wc` |
| Discovery | `man` ([[ManPages]]), [[Find|`find`]], [[Grep|`grep`]] |
| Permissions | `ls -l`, [[Chmod|`chmod`]], `chgrp` |
| Archive | [[Tar|`tar`]] |
| Remote | [[SSH|`ssh`]], [[SCP|`scp`]] |

## Path shortcuts
- `.` — current directory
- `..` — parent directory
- `~` — user's home directory
- `/` — root of the [[UnixFileSystem|file-system tree]]

## Discipline
- Filenames are **case-sensitive**.
- `rm` is **permanent** (no recycle bin) — `rm -i` prompts before each deletion.
- Use [[ManPages|`man <cmd>`]] for full flag reference.

## Sources
- [[dis-app2-1-cmdline-basics]] — DIS Appendix 2.1 *Command Line Basics*.
