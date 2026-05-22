---
title: "xargs"
type: concept
tags: [unix, shell]
sources: [dis-app2-13-pipes]
last_updated: 2026-05-18
---

# `xargs`

`xargs` reads items from [[Stdin]] and uses them as **arguments** to a downstream command — turning a stream of input into per-item command invocations.

## Difference from a raw pipe

```bash
echo "foo bar baz" | cat        # cat gets "foo bar baz" as input data
echo "foo bar baz" | xargs cat  # cat gets foo, bar, baz as filename arguments
```

A pipe wires `stdout → stdin`; `xargs` wires `stdout → argv`.

## Idioms

```bash
find . -name "*.tmp" | xargs rm        # delete every matched file
ls *.txt | xargs -I {} mv {} /backup/  # per-item placeholder via -I
find . -print0 | xargs -0 grep TODO    # NUL-separated, safe for spaces
```

## Connections

- [[ShellPipe]] — the upstream side.
- [[Find]] — the most common upstream pair.
- [[dis-app2-13-pipes]] — source.
