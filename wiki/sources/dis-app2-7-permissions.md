---
title: "Dive into Systems — Appendix 2.7 File Permissions and chmod"
type: source
tags: [unix, security, permissions]
date: 2026-05-18
source_file: https://diveintosystems.org/book/Appendix2/chmod.html
---

## Summary
Seventh subchapter of [[DiveIntoSystems]] Appendix 2. Codifies the **Unix discretionary-access-control model**: three permission bits (**r**/**w**/**x**) × three principal categories (**u**ser / **g**roup / **o**ther), and the [[Chmod|`chmod`]] command that mutates them in either octal or symbolic notation.

## Key Claims
- **Three permissions**: **r** (read) view contents, **w** (write) modify, **x** (execute) run a file *or* enter a directory.
- **Three principal categories**: **u** (owner), **g** (group), **o** (others — everyone else).
- **Display**: `ls -l` prints permissions as `-rwxr-xr--`. First char is the file type (`-` regular, `d` directory). Next 9 chars are u/g/o rwx triplets.
- **Octal notation**: each digit is `4r + 2w + 1x`; `chmod 755` = owner rwx (7), group r-x (5), other r-x (5).
- **Symbolic notation**: `chmod u+w file` grants write to owner; `chmod o-r file` removes read from others. More readable than octal.
- Related: `chgrp` changes a file's group association — composes with permissions for collaborative access.

## Connections
- [[FilePermissions]] — the rwx × ugo model.
- [[Chmod]] — the mutation command.
- [[UnixFileSystem]] — permissions are an attribute of every file-system object.
- [[DiveIntoSystems]] — 158th ingested chapter.

## Contradictions
- None.
