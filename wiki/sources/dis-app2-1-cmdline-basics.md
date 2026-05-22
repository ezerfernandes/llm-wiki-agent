---
title: "Dive into Systems — Appendix 2.1 Command Line Basics"
type: source
tags: [unix, shell, command-line, systems]
date: 2026-05-18
source_file: https://diveintosystems.org/book/Appendix2/cmdln_basics.html
---

## Summary
First subchapter of [[DiveIntoSystems]] Appendix 2 *Using Unix*. Introduces the [[UnixShell|shell]] as a read-eval-print loop (typically `bash` / `zsh`) over the [[UnixFileSystem|Unix file system]] hierarchy rooted at `/`. Codifies the **navigation + file-manipulation command vocabulary** every later appendix subchapter builds on.

## Key Claims
- The **shell** is a program that reads user commands and dispatches them — a *read-eval-print loop* with a `$` prompt.
- The [[UnixFileSystem|file system]] is a single tree rooted at `/`; home is `/home/<user>`; every non-root directory has exactly one parent.
- **Paths** are either *absolute* (start at `/`) or *relative* (resolved against the current working directory).
- **Shortcuts**: `.` = current dir, `..` = parent, `~` = home.
- **Names are case-sensitive**; `rm` is permanent — use `rm -i` for confirmation.

## Key Commands
| Command | Purpose |
|---|---|
| `pwd` | print working directory |
| `cd <path>` | change directory |
| `ls [path]` | list directory contents |
| `mkdir <dir>` | create directory |
| `rmdir <dir>` | remove empty directory |
| `cp <src> <dest>` | copy |
| `mv <src> <dest>` | move / rename |
| `rm <file>` | delete (permanent) |
| `touch <file>` | create empty file |
| `cat <file>` | print contents |
| `less` / `more` | page through a file |
| `wc` | count lines / words / bytes |

## Connections
- [[UnixCommandLine]] — the umbrella concept this subchapter mints.
- [[UnixFileSystem]] — the tree this vocabulary navigates.
- [[ManPages]] — looking up flags for any of these commands (next subchapter).
- [[DiveIntoSystems]] — 152nd ingested chapter; opens Appendix 2.

## Contradictions
- None.
