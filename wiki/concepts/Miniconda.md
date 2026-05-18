---
title: "Miniconda"
type: concept
tags: [tool, python, packaging, devex]
sources: [d2l-installation, pydata-preliminaries]
last_updated: 2026-05-16
---

# Miniconda

Minimal installer for the **conda** Python package and environment manager. Ships only Python, `conda`, and a few core dependencies — strict subset of the larger Anaconda distribution. Recommended baseline for [[d2l-installation|*Dive into Deep Learning*]]: install Miniconda (Python 3.x; D2L tested on 3.9), initialize the shell (`~/miniconda3/bin/conda init`), create a project environment (`conda create --name d2l python=3.9 -y`), activate it (`conda activate d2l`), and `pip install` the chosen [[DeepLearning|deep-learning]] framework + [[D2LPackage|`d2l`]] helpers inside it.

Each project should get its own conda env — Miniconda is the [[VirtualEnvironment]] flavor D2L assumes.

## Key commands (from [[d2l-installation]])

- `sh Miniconda3-py39_4.12.0-MacOSX-x86_64.sh -b` — install on macOS (Intel) in batch mode
- `sh Miniconda3-py39_4.12.0-Linux-x86_64.sh -b` — install on Linux
- `~/miniconda3/bin/conda init` — wire `conda` into the shell
- `conda create --name <env> python=3.9 -y` — make a new env
- `conda activate <env>` / `conda deactivate` — enter / leave the env

## Connections

- [[d2l-installation]] — recommends Miniconda as the simplest setup path.
- [[VirtualEnvironment]] — Miniconda is one implementation alongside `venv` and `uv`.
- [[Jupyter]] — the `jupyter notebook` server runs inside the activated conda env.
- [[CUDA]] — when installing GPU framework builds, the CUDA version determines which framework wheel to `pip install` inside the env.
