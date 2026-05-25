---
title: "Poetry (Python)"
type: entity
tags: [tool, python, dependency-management, packaging, open-source]
sources: [leh-ch02-tooling-and-installation, leh-ch03-data-engineering, leh-ch11-mlops-and-llmops]
last_updated: 2026-05-22
---

## What it is
Poetry is a Python dependency-management and packaging tool that declares dependencies in `pyproject.toml`, creates virtual environments, and writes a `poetry.lock` that pins exact transitive versions for reproducibility.

## In LLM Engineer's Handbook
Ch. 2 ([[leh-ch02-tooling-and-installation]]) pins **Poetry 1.8.3** as the project's package manager and contrasts it with `requirements.txt`-based [[Conda]] / Venv / [[Pipenv]] flows, plus the Rust-based [[UV]] as a potential successor. Poetry also installs the [[PoeThePoet]] plugin (`poetry self add 'poethepoet[poetry_plugin]'`) which centralizes all CLI commands. Ch. 3 ([[leh-ch03-data-engineering]]) and Ch. 11 ([[leh-ch11-mlops-and-llmops]]) continue using Poetry for the entire dev loop — `poetry install --without aws`, `poetry shell`, `poetry run`, and inside the production `Dockerfile` (with `poetry config virtualenvs.create false`).

## Connections
- [[PoeThePoet]] — Poetry plugin / task runner installed on top.
- [[UV]] — Rust-based alternative the authors flag for testing.
- [[Pipenv]] / [[Conda]] — alternatives the authors compare against.
- [[Pyenv]] — Python version manager used alongside Poetry.
- [[Python]] — the language Poetry manages.
- [[Reproducibility]] — primary value `poetry.lock` provides.
