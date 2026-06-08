---
title: "TorchDynamo"
type: concept
tags: [frameworks, pytorch, compilation, graph-capture]
sources: [mlsysbook-ch07-ml-frameworks]
last_updated: 2026-06-05
---

# TorchDynamo

**TorchDynamo** is the graph-capture stage of PyTorch 2.0's [[TorchCompile|torch.compile]] pipeline. It intercepts Python bytecode execution using CPython's **PEP 523 frame-evaluation API** to extract a [[ComputationalGraph|computational graph]] from unmodified eager code. Unlike `torch.jit.trace` — which records a single execution path and silently ignores alternative branches — TorchDynamo inserts **graph breaks** when it encounters unsupported code (`print`, arbitrary Python, non-PyTorch calls), finalizing the current graph for compilation, executing the unsupported code eagerly, then beginning a new graph after. This ensures *correctness* rather than silent failure.

The captured operations are converted to an [[FXGraph|FX Graph]] and handed to a backend (default [[TorchInductor]]). Graph breaks are performance-critical: each forces a return to eager dispatch, resetting the [[JITCompilation|JIT]] overhead amortization. Diagnose with `TORCH_LOGS="graph_breaks"`.

## Connections

- [[mlsysbook-ch07-ml-frameworks]] — torch.compile's three-stage pipeline.
- [[TorchCompile]] — the user-facing API; [[FXGraph]] — its output; [[TorchInductor]] — the downstream backend.
- [[JITCompilation]] / [[TorchScript]] — TorchDynamo improves on tracing's silent-failure mode.
- [[PyTorch]] — the framework.
