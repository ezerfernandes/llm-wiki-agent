---
title: "IPython"
type: concept
tags: [tool, repl, python]
sources: [pydata-preliminaries, pydata-python-basics, pydata-ipython]
last_updated: 2026-05-15
---

# IPython

An enhanced interactive Python shell. Started by [[FernandoPerez]] in 2001. Adds tab completion, object introspection (`?` / `??`), magic commands (`%run`, `%timeit`, `%debug`, `%pdb`, `%lprun`, …), shell integration (`!cmd`), persistent input/output history (`_`, `_N`), and a colorized prompt. Encourages an *execute-explore* workflow rather than *edit-compile-run*.

## Relationship to Jupyter
- IPython is the Python kernel powering the [[Jupyter]] notebook (and the broader Jupyter ecosystem, which supports 40+ languages).
- Almost everything in this article works identically in a Jupyter notebook cell.

## Connections
- [[FernandoPerez]] — original author.
- [[Jupyter]] — broader notebook project IPython became a kernel for.
- [[pydata-ipython]] — Appendix B deep-dive on advanced features.
