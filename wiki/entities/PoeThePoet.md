---
title: "Poe the Poet"
type: entity
tags: [tool, python, task-runner, open-source]
sources: [leh-ch02-tooling-and-installation, leh-ch03-data-engineering, leh-ch11-mlops-and-llmops]
last_updated: 2026-05-22
---

## What it is
Poe the Poet (`poethepoet`) is a Python task runner that registers CLI command aliases inside `pyproject.toml` under `[tool.poe.tasks]`. Installed as a [[PoetryPython|Poetry]] plugin, it replaces Makefile / Invoke / shell scripts for project automation.

## In LLM Engineer's Handbook
Ch. 2 ([[leh-ch02-tooling-and-installation]]) installs Poe the Poet (`poetry self add 'poethepoet[poetry_plugin]'`) and uses it for every dev command — e.g. `poetry poe local-infrastructure-up`, `poetry poe run-digital-data-etl-maxime`. Ch. 3 ([[leh-ch03-data-engineering]]) registers per-author ETL run commands, and Ch. 11 ([[leh-ch11-mlops-and-llmops]]) wires CI/CD jobs (`gitleaks-check`, `lint-check`, `format-check`, `test`, `export-settings-to-zenml`, `run-end-to-end-data-pipeline`) into Poe tasks for both local invocation and GitHub Actions.

## Connections
- [[PoetryPython]] — Poe is a Poetry plugin.
- [[Python]] — language.
- [[CLI]] — Poe is the project's CLI surface.
- [[GitHubActions]] — Poe tasks run from CI/CD workflows.
