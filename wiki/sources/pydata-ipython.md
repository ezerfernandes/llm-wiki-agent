---
title: "Python for Data Analysis 3E — Appendix B: More on the IPython System"
type: source
tags: [book, ipython, jupyter, debugging, profiling, pydata]
date: 2026-05-15
source_file: raw/pydata-book-web/ipython.md
book: "Python for Data Analysis, 3rd Edition"
author: "Wes McKinney"
url: https://wesmckinney.com/book/ipython.html
chapter: B
---

## Summary
Deeper [[IPython]] productivity features beyond chapter 2: terminal keyboard shortcuts (Emacs/bash style), the magic-command catalog, command history, OS integration, and software-development tools (interactive debugger `%debug`/`%pdb`, timing `%time`/`%timeit`, profiling `%prun`/`%lprun`, module-reloading workflow). Closes with profile configuration via `~/.ipython/profile_default`.

## Key Claims
- **Keyboard shortcuts** — Ctrl-P / Ctrl-N (history nav), Ctrl-R (reverse search), Ctrl-A/Ctrl-E (line start/end), Ctrl-K (kill to end), Ctrl-U (kill line), Ctrl-L (clear screen). Jupyter has a separate set.
- **Magic commands** — `%`-prefixed. Inspection: `%magic`, `%cmd?`. Common: `%run script.py`, `%paste`, `%cpaste`, `%timeit expr`, `%time expr`, `%debug` (post-mortem), `%pdb` (auto-enter debugger on exception), `%who`/`%whos` (vars in namespace), `%reset`, `%hist`, `%matplotlib`. Run line magic without `%` if `automagic` is on.
- **History** — `_`, `__`, `___` are last three Out values; `_N` and `_iN` are Out and In for cell N. `%hist` prints history; `%save mysession.py 1-15` writes a range to a file.
- **OS integration** — Shell commands via `!cmd`; capture output into a Python list via `output = !ls *.py`. Aliases: `%alias cm chrome`. Directory bookmarks: `%bookmark name path`; `cd name`.
- **Debugger** — `%debug` after an exception drops into post-mortem `pdb`; `%run -d script.py` runs under debugger; `%pdb on` makes future exceptions auto-trigger debugger. Commands: `n` next, `s` step in, `c` continue, `u`/`d` move up/down stack, `p var` print, `l` list source.
- **Timing** — `%time stmt` runs once; `%timeit stmt` runs many times and reports best/mean/stdev. Cell magic `%%timeit` for multi-line.
- **Profiling** — `%prun -l 10 -s cumulative func()` cProfile run + sorted by cumulative time; `%run -p` does the same on a script. Line profiler: install `line_profiler`, enable via `%load_ext line_profiler`, then `%lprun -f func func()`.
- **Workflow** — `%run` re-imports modules that have changed (when modules autoreload extension is loaded). Recommended: enable `%load_ext autoreload` + `%autoreload 2` for live edits.
- **Profiles / config** — IPython stores per-profile config under `~/.ipython/profile_default/ipython_config.py`. Create alternates via `ipython profile create myprofile`.

## Key Quotes
> See `source_file` for full text. Quotes omitted in bulk ingest; pull on demand.

## Connections
- [[IPython]] — core subject.
- [[Jupyter]] — shares the IPython kernel.
- [[pydata-python-basics]] — chapter 2 covers the basics.

## Contradictions
- None.
