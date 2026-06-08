---
title: "Static Computation Graph"
type: concept
tags: [frameworks, execution-model, compilation, deep-learning]
sources: [mlsysbook-ch07-ml-frameworks]
last_updated: 2026-06-05
---

# Static Computation Graph

A **static graph** ("define-then-run") defines the complete [[ComputationalGraph|computational graph]] as a symbolic representation *first*, then executes it separately. Because the framework sees the entire computation before any arithmetic occurs, it can analyze, transform, and optimize globally — a visibility impossible when operations run one at a time in [[EagerExecution|eager mode]]. [[TensorFlow]] 1.x exemplified this with `tf.placeholder` + `sess.run()`; modern frameworks reach the same point via [[JITCompilation|JIT]] graph capture.

## Ahead-of-time optimizations enabled

- **[[KernelFusion|Kernel fusion]]** — `y = x*2; z = y+1` fuses to `z = x*2+1`, eliminating the intermediate and halving memory traffic.
- **Exact memory preallocation + buffer reuse** — the compiler computes all tensor lifetimes in advance.
- **Global layout transforms** — NCHW↔NHWC without runtime copies.
- **[[DeadCodeElimination|Dead code elimination]]** (5–15% of nodes in large transformers) and **[[ConstantFolding|constant folding]]**.

Together DCE + constant folding can cut total FLOPs 5–10% "before the first batch arrives." [[XLA]] compiles the graph to hardware-specific machine code for ~1.5–2× on a transformer encoder block.

## Cost

Reduced flexibility: standard Python `if`/`for` cannot depend on computed tensor values (`tf.cond`/`tf.while_loop` required); debugging points at symbolic node names rather than the line that failed.

## Connections

- [[mlsysbook-ch07-ml-frameworks]] — static graph as one of three execution strategies.
- [[EagerExecution]] / [[JITCompilation]] — the other points on the continuum.
- [[ComputationalGraph]] — the DAG made fully visible before execution.
- [[XLA]] / [[KernelFusion]] / [[DeadCodeElimination]] / [[ConstantFolding]] — the AOT optimizations it unlocks.
- [[TensorFlow]] — graph-first framework; [[CompilationContinuum]] — when AOT wins.
