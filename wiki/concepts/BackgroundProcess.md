---
title: "Background Process"
type: concept
tags: [unix, shell, process]
sources: [dis-app2-9-process-control]
last_updated: 2026-05-18
---

# Background Process

A **background process** is a [[UnixShell|shell]]-started process that does **not** block the shell's prompt — the shell returns immediately and can accept further commands. Started by appending `&`:

```bash
./simulation &
```

## Manipulation

- `jobs` lists background/suspended jobs with `[N]` identifiers.
- `fg %N` brings job `N` to the **foreground**.
- `bg %N` resumes a stopped job in the background.
- `CTRL-Z` then `bg` is the canonical *"oops, I should have run this with `&`"* recovery.

## Connections

- [[JobControl]] — the umbrella mechanism.
- [[Ps]] — inspect background processes' [[ProcessID|PIDs]].
- [[Kill]] — terminate a background process.
- [[dis-app2-9-process-control]] — source.
