---
title: "grep"
type: concept
tags: [unix, search, regex, command-line]
sources: [dis-app2-6-grep-find]
last_updated: 2026-05-18
---

# grep

**`grep`** searches *inside* files for lines matching a pattern. Per [[dis-app2-6-grep-find|DIS Appendix 2.6]], it *"outputs every line in the file (or set of files) that has a matching occurrence of the pattern."*

## Syntax

```bash
grep [flags] <pattern> <file...>
```

## Key flags

| Flag | Effect |
|---|---|
| `-n` | prefix each match with its line number |
| `-i` | case-insensitive matching |
| `-r` | recurse into directories |
| `-H` | always show the filename (default off for a single-file search) |
| `-v` | invert — print lines that *don't* match |
| `-E` | extended regex |

## Pattern language

`grep` supports basic regex — character classes `[A-Z]`, word boundaries `\b`, quantifier `*` (zero-or-more), anchors `^` / `$`. `grep -E` enables extended regex (`+`, `?`, `|`).

## Composition

Routine usage pipes from another tool:

```bash
ps aux | grep python                # find running python processes
grep main *.c                        # find main() in all C files
find . -name "*.c" | xargs grep TODO # find TODOs in all C files
```

## Related
- [[Find]] — the file-*name* search counterpart.
- [[UnixCommandLine]] — invocation context.
- [[DiveIntoSystems]] — Appendix 2.6.

## Sources
- [[dis-app2-6-grep-find]] — DIS Appendix 2.6 *grep and find*.
