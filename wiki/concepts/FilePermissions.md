---
title: "File Permissions"
type: concept
tags: [unix, security, permissions, access-control]
sources: [dis-app2-7-permissions]
last_updated: 2026-05-18
---

# File Permissions

The **Unix file-permission model** is a 3×3 matrix: three permission bits (**r** read / **w** write / **x** execute) for each of three principal categories (**u**ser / **g**roup / **o**ther).

Per [[dis-app2-7-permissions|DIS Appendix 2.7]], every object in the [[UnixFileSystem|filesystem]] carries this 9-bit attribute, visible via `ls -l` as the familiar `-rwxr-xr--`-style string.

## The three permission bits

| Bit | On a regular file | On a directory |
|---|---|---|
| `r` | view contents | list entries (`ls`) |
| `w` | modify contents | create / rename / delete entries |
| `x` | execute as program | enter / traverse (`cd`) |

## The three principal categories

| Category | Letter | Who |
|---|---|---|
| owner | `u` | the file's owner (set at creation) |
| group | `g` | members of the file's group |
| other | `o` | everyone else with system access |

## `ls -l` decoding

```
-rwxr-xr--  1 ezer  staff  4096 May 18 10:24 script.sh
^ ^^^^^^^^^
| └── 9 permission bits: u=rwx g=r-x o=r--
└── file type: `-` regular, `d` directory, `l` symlink
```

## Mutation
See [[Chmod]] for the octal and symbolic forms used to change these bits, and `chgrp` / `chown` for changing the group / owner.

## Sources
- [[dis-app2-7-permissions]] — DIS Appendix 2.7 *File Permissions and chmod*.
