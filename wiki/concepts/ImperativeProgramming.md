---
title: "Imperative Programming"
type: concept
tags: [programming-models, deep-learning, performance]
sources: [d2l-computational-performance]
last_updated: 2026-05-16
---

# Imperative Programming

A programming model where statements (`print`, `+`, `if`) are executed *in sequence*, each changing the program's state. Python is an *interpreted language* in this style: when evaluating `e = add(a, b); f = add(c, d); g = add(e, f)`, Python evaluates each call individually and stores the intermediate variables ([[d2l-computational-performance]] §`hybridize`).

## In deep learning

[[PyTorch]] and Chainer adopted imperative-by-default with [[Autograd|dynamic computation graphs]]; [[TensorFlow]] 2.0 added imperative mode (*eager execution*) by default. Imperative code is **easier to write and debug** — you can `print(x)` any intermediate, attach `pdb`, and use Python control flow naturally.

## Cost

- **Python-interpreter overhead** — every line crosses the Python ↔ C++ boundary. On a single CPU this is negligible; on an 8-GPU server it can stall all GPUs because the single-threaded Python interpreter cannot dispatch work fast enough.
- **Memory pressure** — intermediates (`e`, `f`) must be kept live because the system cannot know whether downstream Python code will use them.

The fix is hybrid programming — see [[SymbolicProgramming]], [[TorchScript]], `tf.function`, [[XLA]], and MXNet's `hybridize()`.

## See also
- [[SymbolicProgramming]] — the contrasting "define then compile" model.
- [[TorchScript]] / `tf.function` — bridges from imperative to symbolic.
- [[d2l-computational-performance]] §`hybridize`.
