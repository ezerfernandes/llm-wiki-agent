---
title: "history Command"
type: concept
tags: [unix, shell, bash]
sources: [dis-app2-11-history]
last_updated: 2026-05-18
---

# `history` Command

The bash `history` built-in displays a numbered list of previously executed commands:

```
$ history
  501  ls
  502  cd projects
  503  git status
  504  vim README.md
```

Each entry is indexed and can be recalled with `!<n>` (e.g., `!503` re-runs `git status`).

## Connections

- [[BashHistory]] — umbrella concept.
- [[BangBang]] — `!!` / `!n` shortcut syntax.
- [[Bash]] — host shell.
- [[dis-app2-11-history]] — source.
