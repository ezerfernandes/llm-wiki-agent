---
title: "Bang-Bang (!!)"
type: concept
tags: [unix, shell, bash]
sources: [dis-app2-11-history]
last_updated: 2026-05-18
---

# `!!` and `!n` — History Expansion

Bash's **history expansion** lets you recall and re-run previous commands via the `!`-prefix syntax.

| Form | Effect |
|---|---|
| `!!` | Re-run the **last** command. |
| `!n` | Re-run history entry `n`. |
| `!string` | Re-run the most recent command **starting with** `string`. |
| `!?string` | Re-run the most recent command **containing** `string`. |
| `^old^new` | Re-run last command with `old` substituted by `new`. |

## Canonical example

*"I should have used sudo"*:

```bash
$ apt install vim
E: Could not open lock file — Permission denied
$ sudo !!
sudo apt install vim
```

## Connections

- [[BashHistory]] — umbrella.
- [[HistoryCommand]] — paired built-in.
- [[Bash]] — host.
- [[dis-app2-11-history]] — source.
