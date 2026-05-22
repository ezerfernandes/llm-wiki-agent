---
title: "find"
type: concept
tags: [unix, search, filesystem, command-line]
sources: [dis-app2-6-grep-find]
last_updated: 2026-05-18
---

# find

**`find`** recursively walks the [[UnixFileSystem|filesystem]] looking for files whose attributes match a query. Where [[Grep|`grep`]] searches *inside* files, `find` searches *for* files.

## Syntax

```bash
find <path> [predicates...]
```

## Common predicates

| Predicate | Effect |
|---|---|
| `-name "<pat>"` | filename matches glob pattern (`*.c`, etc.) |
| `-iname "<pat>"` | case-insensitive name match |
| `-type f` / `-type d` | regular file / directory only |
| `-mtime -7` | modified in the last 7 days |
| `-size +1M` | larger than 1 megabyte |
| `-exec <cmd> {} \;` | run a command on each match |

Per [[dis-app2-6-grep-find|DIS Appendix 2.6]], the canonical pattern: `find ./ -name "*.c"` enumerates every C source file under the current directory.

## Composition with grep

```bash
find . -name "*.py" -exec grep -l TODO {} \;   # files containing TODO
find . -name "*.log" | xargs grep ERROR        # search log contents
```

## Related
- [[Grep]] — content search.
- [[UnixCommandLine]] — invocation context.
- [[DiveIntoSystems]] — Appendix 2.6.

## Sources
- [[dis-app2-6-grep-find]] — DIS Appendix 2.6 *grep and find*.
