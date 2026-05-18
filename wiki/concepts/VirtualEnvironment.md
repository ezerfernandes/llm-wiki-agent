---
title: "Virtual Environment"
type: concept
tags: [python, packaging, devex]
sources: [madewithml-packaging, d2l-installation]
last_updated: 2026-05-16
---

# Virtual Environment

An isolated [[Python]] interpreter and dependency tree ([[Miniconda|venv / conda / uv]]) per project. Prevents cross-project conflicts and supports [[Reproducibility]] when paired with [[PyprojectToml]] lockfiles. [[d2l-installation]] uses the conda flavor — a named env (`d2l`) created with `conda create --name d2l python=3.9 -y` and activated per shell.
