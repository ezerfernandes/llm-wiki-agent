---
title: "Unix File System"
type: concept
tags: [unix, filesystem, hierarchy]
sources: [dis-app2-1-cmdline-basics, dis-app2-7-permissions]
last_updated: 2026-05-18
---

# Unix File System

The **Unix file system** is a single tree rooted at `/`. Every file and directory has exactly one *parent* (except the root itself), and every object has [[FilePermissions|rwx permissions]] tagged for three principal categories (owner, group, other).

Per [[dis-app2-1-cmdline-basics|DIS Appendix 2.1]]: *"every directory except root has exactly one parent directory."*

## Structure highlights
- `/` — root of the tree.
- `/home/<user>` — user's home directory (also addressable as `~`).
- Pathnames are **absolute** (start with `/`) or **relative** (resolved against the current working directory printed by `pwd`).
- Names are **case-sensitive** — `Foo` and `foo` are different objects.

## Attributes per file
- **Type** — regular file (`-`) / directory (`d`) / symlink / device (visible as the leading character of `ls -l`).
- **Permissions** — see [[FilePermissions]] and [[Chmod]].
- **Owner + group** — see `chgrp`, `chown`.
- **Modification time** — used by [[Make]] to decide what to rebuild.

## Navigation
See [[UnixCommandLine]] for the vocabulary (`pwd`, `cd`, `ls`, `mkdir`, `cp`, `mv`, `rm`, ...).

## Sources
- [[dis-app2-1-cmdline-basics]] — tree structure + path semantics.
- [[dis-app2-7-permissions]] — the per-file permission attributes.
