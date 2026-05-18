---
title: "d2l Package"
type: concept
tags: [tool, python, deep-learning]
sources: [d2l-preface, d2l-installation, d2l-appendix-tools]
last_updated: 2026-05-16
---

# d2l Package

Lightweight Python utility package shipped with *Dive into Deep Learning* ([[d2l-preface]]). Captures the most-frequently-imported helpers (functions, classes, common import statements) so chapters don't repeat boilerplate. Code blocks marked `#@save` in the textbook are persisted into the package and become importable from later chapters as `from d2l import …`.

Installed via `pip install d2l==1.0.3` inside the activated [[Miniconda|conda]] `d2l` environment, *after* the chosen deep-learning framework is installed (see [[d2l-installation]]).

Dependencies the preface lists: `inspect`, `collections`, [[NumPy]], [[matplotlib]], `pandas`, `requests`, `IPython`, plus framework-specific imports for [[MXNet]] / [[PyTorch]] / [[TensorFlow]] / [[JAX]].

## Connections
- [[d2l-preface]] — defines the package convention.
- [[d2l-installation]] — pins `d2l==1.0.3` and orders the install steps.
- [[Miniconda]] — install inside the activated `d2l` conda environment.
- [[Jupyter]] — host environment for `#@save` blocks.
- [[NumPy]], [[matplotlib]] — required dependencies.
- [[d2l-appendix-tools]] — §`d2l` provides the alphabetical `autoclass` / `autofunction` API documentation for every reusable class and helper shipped in the package: [[Module]] / [[DataModule]] / [[Trainer]] / [[HyperParameters]] / [[ProgressBoard]] OO scaffold; [[LinearRegression]] / [[Classifier]] / [[LeNet]]; [[RNN]] / [[GRU]] / [[Seq2Seq]] / [[EncoderDecoder]] / [[AttentionDecoder]]; [[AdditiveAttention]] / [[DotProductAttention]] / [[MultiHeadAttention]] / [[TransformerEncoder]]; helpers `try_gpu` / `try_all_gpus` / `corr2d` / `bleu` / `masked_softmax` / `plot` / `add_to_class`.
