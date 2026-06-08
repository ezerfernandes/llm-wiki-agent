---
title: "TensorFlow"
type: entity
tags: [tool, deep-learning, framework]
sources: [d2l-preface, d2l-preliminaries, d2l-builders-guide, mlsysbook-ch07-ml-frameworks, mlsysbook-ch14-ml-operations]
last_updated: 2026-06-05
---

# TensorFlow

Open-source deep-learning framework originally developed by [[google|Google]]; widely adopted in industry. One of four frameworks supported by *Dive into Deep Learning* ([[d2l-preface]]) — TensorFlow implementations were adapted from the PyTorch port by Yuan Tang.

## From [[mlsysbook-ch07-ml-frameworks|mlsysbook Vol 1 Ch 7]]

Ch 7 casts TensorFlow as the **graph-first production machine** — Google's answer to the *abstraction problem*. Its static "Define-and-Run" design enables ahead-of-time ([[StaticGraph|static-graph]]) compilation and per-target optimization across the full deployment spectrum: TPU pods, Android via [[TensorFlowLite|TF Lite]], browser via TensorFlow.js, plus SavedModel→TF Serving. Differentiation is reverse-mode (symbolic in 1.x); 2.x added [[EagerExecution|eager]] by default with `tf.function` for graph compilation. The TF variant ladder (full ~1,400 ops → [[TensorFlowLite|TF Lite]] ~130 → TF Lite Micro ~50, binary MB → ~10 KB) illustrates progressive constraint enabling progressive optimization.

## Connections
- [[google|Google]] — original developer.
- [[Keras]] — its high-level layer API (`tf.keras`); [[XLA]] — its compiler backend.
- [[TensorFlowLite]] — its edge/TinyML runtimes.
- [[PyTorch]] — D2L primary framework; sibling implementation. [[JAX]] — Google's functional sibling.
- [[MXNet]] — other D2L-supported framework.
- [[d2l-preface]] — references TensorFlow as one of D2L's four framework targets.
- [[mlsysbook-ch07-ml-frameworks]] — analyzes TensorFlow as the abstraction-first platform.
- [[mlsysbook-ch14-ml-operations]] — Ch 14 uses TensorFlow (with TFX, TF Serving, TFLite) as a production training/serving framework across the pipeline.

