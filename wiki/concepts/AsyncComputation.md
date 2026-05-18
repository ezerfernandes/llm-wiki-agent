---
title: "Asynchronous Computation"
type: concept
tags: [deep-learning, performance, parallelism, frameworks]
sources: [d2l-computational-performance]
last_updated: 2026-05-16
---

# Asynchronous Computation

Decoupling a deep-learning framework's Python **frontend** (where user code lives) from a C++ **backend** (where ops actually run) via a task queue. The frontend returns immediately after enqueuing each op; the backend executes ops in topological order on a [[ComputationalGraph|dependency graph]] ([[d2l-computational-performance]] §`async-computation`).

## Why

Python is single-threaded. On a multi-GPU server the GIL cannot dispatch work fast enough to keep all devices busy. **Async dispatch turns 10,000 sequential `y=x+1` ops from $10000(t_1+t_2+t_3)$ into $t_1 + 10000\,t_2 + t_3$** because the frontend doesn't wait for backend results.

## Defaults across frameworks

- **PyTorch** — *GPU operations are asynchronous by default*. CPU operations are sync. `torch.cuda.synchronize(device)` forces completion.
- **MXNet** — fully asynchronous. `npx.waitall()` or `tensor.wait_to_read()` forces completion.
- **TensorFlow 2** — async under `tf.function`; eager mode is mostly sync.

## Implicit blockers

Calls that force the frontend to wait for the backend — *most* performance bugs come from these:

- Printing a tensor (must materialize the value).
- `.item()` (scalar conversion).
- `.asnumpy()` / `.numpy()` / `.cpu()` (NumPy or host conversion).
- `wait_to_read()` / `synchronize()` (explicit barrier).
- Inserting into a Python list / dict if you then read it.

> *"Copying small amounts of data frequently from MXNet's scope to NumPy and back can destroy performance of an otherwise efficient code, since each such operation requires the computational graph to evaluate all intermediate results."* — [[d2l-computational-performance]]

D2L's recommendation: **synchronize at most once per minibatch**, keep logging tensors on the GPU.

## See also
- [[AutoParallelism]] — what the dep-graph scheduler does with the async queue.
- [[ComputationalGraph]] — the dependency structure that lets the backend decide what can run in parallel.
- [[GPU]] — `print(gpu_tensor)` is one of the canonical "transfers are slow" sins.
- [[d2l-computational-performance]] §`async-computation`.
