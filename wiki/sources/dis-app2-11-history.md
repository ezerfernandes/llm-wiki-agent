---
title: "Dive into Systems — App 2.11 Shell History"
type: source
tags: [book, unix, shell, bash]
date: 2026-05-18
source_file: https://diveintosystems.org/book/Appendix2/history.html
---

## Summary
Eleventh subchapter of [[DiveIntoSystems]] Appendix 2 *Using Unix*. Codifies the [[BashHistory|bash command history]] mechanism: the [[HistoryCommand|`history`]] built-in lists recently executed commands with numeric indices, and the `!`-prefix re-execution syntax (`!!`, `!n`) recalls previous commands without retyping.

## Key Claims
- `history` displays numbered list of recent commands (with timestamps).
- `!n` re-executes command number `n` from history.
- `!!` re-runs the **most recent** command — *"particularly useful for easily re-running commands that have a long list of command line arguments."*
- When `!n` runs, the actual expanded command (not the `!n` shorthand) is recorded in history.

## Connections
- [[BashHistory]] — minted here.
- [[HistoryCommand]] — `history` built-in.
- [[BangBang]] — `!!` and `!n` shortcuts.
- [[UnixShell]] / [[Bash]] — host shell features.
- [[DiveIntoSystems]] — Appendix 2.11.
