---
title: "Ruff"
type: entity
tags: [tool]
sources: [leh-ch11-mlops-and-llmops]
last_updated: 2026-05-22
---

## What it is
Rust-implemented Python linter and formatter.

## In LLM Engineer's Handbook
Ruff (Astral) is a Python linter and formatter written in Rust. The LLM Twin's CI pipeline ([[leh-ch11-mlops-and-llmops]]) uses Ruff for both `lint-check` (PEP 8 + dead-code/unused-import checks) and `format-check` (indentation, line length, spacing) — fast enough for large codebases.
