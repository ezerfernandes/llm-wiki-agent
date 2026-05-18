---
title: "Dive into Deep Learning — Installation"
type: source
tags: [textbook, d2l, installation, setup]
date: 2026-05-16
source_file: raw/d2l-en/chapter_installation/
---

# Dive into Deep Learning — Installation

## Summary

The Installation chapter of [[d2l-preface|*Dive into Deep Learning*]] (D2L) gives the minimum runbook for setting up a local environment to execute every notebook in the book: install [[Miniconda]] (Python 3.9 tested), create and activate a `conda` environment named `d2l`, install one of four deep-learning frameworks ([[MXNet]] / [[PyTorch]] / [[TensorFlow]] / [[JAX]]) at pinned versions — with optional [[CUDA]] support if [[CUDA|NVIDIA GPUs]] are present — install the `d2l==1.0.3` Python helper package ([[D2LPackage]]), download the per-framework notebooks zip from `d2l.ai`, and launch them with `jupyter notebook` ([[Jupyter]]) at `http://localhost:8888`. The chapter is the operational counterpart to the [[d2l-preface|preface]]'s "executable textbook" thesis: every later D2L chapter assumes this exact environment.

## Key Claims

- **Recommended package manager: [[Miniconda]].** "Your simplest option is to install Miniconda." Python 3.x is required; chapter tested with Python 3.9. Miniconda is preferred over full Anaconda — minimal distribution, fewer pre-installed libraries, smaller install footprint.
- **Conda environment name is `d2l`.** Created via `conda create --name d2l python=3.9 -y` and activated with `conda activate d2l`. Every later D2L chapter assumes you are inside this environment; reactivate `conda activate d2l` whenever opening a new shell. Exit with `conda deactivate`.
- **GPU is optional for the first few chapters.** "Your CPU provides more than enough horsepower to get you through the first few chapters." But: "you will want to access GPUs before running larger models." The check for GPU-readiness is *NVIDIA GPU + CUDA installed* — laptop integrated/display GPUs do not count.
- **CUDA version check.** Use `nvcc --version` or `cat /usr/local/cuda/version.txt` to identify your installed [[CUDA]] toolkit version. The framework `pip` install command is then tagged with that version (e.g., `mxnet-cu112` for CUDA 11.2, `cu101` for 10.1, `cu90` for 9.0).
- **Pinned framework versions** at time of publication (D2L 1.0.3):
  - [[MXNet]]: `mxnet-cu112==1.9.1` (GPU, CUDA 11.2) or `mxnet==1.9.1` (CPU). Windows users append `-f https://dist.mxnet.io/python`.
  - [[PyTorch]]: `pip install torch==2.0.0 torchvision==0.15.1` (single command for CPU or GPU support).
  - [[TensorFlow]]: `pip install tensorflow==2.12.0 tensorflow-probability==0.20.0`.
  - [[JAX]]: `pip install "jax[cuda11_pip]==0.4.13" -f https://storage.googleapis.com/jax-releases/jax_cuda_releases.html flax==0.7.0` (GPU) or `pip install "jax[cpu]==0.4.13" flax==0.7.0` (CPU). Always paired with Flax 0.7.0.
- **`d2l` helper package: `pip install d2l==1.0.3`.** Installed *after* the chosen deep-learning framework. Provides the `#@save`-marked utilities from previous chapters as importable Python ([[D2LPackage]]).
- **Notebook bundle.** Notebooks are downloadable from the "Notebooks" tab on `d2l.ai`, or via `curl https://d2l.ai/d2l-en-1.0.3.zip -o d2l-en.zip && unzip d2l-en.zip`. Inside the unzipped tree, framework-specific notebooks live in per-framework directories (`d2l-en/mxnet/`, `d2l-en/pytorch/`, `d2l-en/tensorflow/`, `d2l-en/jax/`). Requires `unzip` (`sudo apt-get install unzip` on Linux if missing).
- **Runtime: `jupyter notebook` → `http://localhost:8888`.** Classic Jupyter Notebook server, not [[JupyterLab]]. Browser may auto-open.
- **Workflow rule.** Whenever you open a new terminal: `conda activate d2l` before running notebooks *or* upgrading either the framework or the `d2l` package.
- **Per-framework discussion forums.** Each framework variant has its own Discourse thread on `discuss.d2l.ai` (mxnet → t/23, pytorch → t/24, tensorflow → t/436, jax → t/17964) — the "Discourse forum" component of the GitHub + Jupyter + Sphinx + Discourse stack named in the [[d2l-preface|preface]].

## Key Quotes

> "Your simplest option is to install Miniconda. Note that the Python 3.x version is required." — recommended setup baseline

> "Before installing any deep learning framework, please first check whether or not you have proper GPUs on your machine (the GPUs that power the display on a standard laptop are not relevant for our purposes)." — operational definition of a usable GPU

> "Your CPU provides more than enough horsepower to get you through the first few chapters. Just remember that you will want to access GPUs before running larger models." — when GPUs start mattering

> "Whenever you open a new command line window, you will need to execute `conda activate d2l` to activate the runtime environment before running the D2L notebooks, or updating your packages (either the deep learning framework or the `d2l` package)." — the conda activation rule

## Connections

- [[d2l-preface]] — preceding chapter; this chapter operationalizes the executable-textbook thesis.
- [[Miniconda]] — recommended Python distribution and package manager. **New concept page.**
- [[CUDA]] — required NVIDIA toolkit if installing GPU-enabled framework builds; existing concept page.
- [[Jupyter]] — notebook runtime (`jupyter notebook` → `http://localhost:8888`); existing concept page.
- [[VirtualEnvironment]] — the `conda create --name d2l` step is a [[VirtualEnvironment]] instance (conda flavor).
- [[PyTorch]] — primary framework since the 2021 D2L redesign; existing entity page.
- [[MXNet]] — original D2L framework; existing entity page.
- [[TensorFlow]] — supported framework; existing entity page.
- [[JAX]] — supported framework (paired with Flax 0.7.0); existing entity page.
- [[D2LPackage]] — `d2l==1.0.3` helper package installed last; existing concept page.

## Contradictions

- None against existing wiki content. The chapter is purely operational and consistent with the [[d2l-preface|preface]]'s multi-framework framing.
