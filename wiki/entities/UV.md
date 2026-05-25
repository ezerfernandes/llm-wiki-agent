---
title: "uv"
type: entity
tags: [tool, python, dependency-management, packaging, rust]
sources: [leh-ch02-tooling-and-installation]
last_updated: 2026-05-22
---

## What it is
`uv` is an extremely fast Python package and project manager written in Rust by Astral (the makers of [[Ruff]]). It aims to be a drop-in replacement for `pip` / `pip-tools` / [[PoetryPython|Poetry]] / [[Pyenv]] / virtualenv with significantly faster install times.

## In LLM Engineer's Handbook
Ch. 2 ([[leh-ch02-tooling-and-installation]]) flags uv as a Rust-based, faster potential successor to [[PoetryPython|Poetry]] that the authors think is worth testing. The book itself sticks with Poetry 1.8.3 for its mature ecosystem, but explicitly notes uv as a future migration target.

## Connections
- [[PoetryPython]] — current package manager the book uses; uv is positioned as the successor.
- [[Pipenv]] / [[Conda]] — older alternatives.
- [[Python]] — language.
- [[Pyenv]] — adjacent (Python version management).
