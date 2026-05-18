---
title: "PyTorch"
type: entity
tags: [tool, deep-learning, framework]
sources: [madewithml-mlops-training, madewithml-foundations-pytorch, d2l-preliminaries, d2l-builders-guide]
last_updated: 2026-05-16
---

# PyTorch

Deep-learning framework underlying every foundations DL lesson and the training pipeline in [[madewithml-mlops-training]]. Bridges from [[NumPy]] semantics to GPU-accelerated [[Tensor]] ops with [[Autograd]]; wrapped by [[RayTrain]] for distributed training.

[[d2l-builders-guide]] is the chapter that explains *how* PyTorch is structured: every layer / sub-network / model is a `nn.Module` subclass exposing a `forward` method; [[StateDict|`state_dict()`]] saves parameters (not architecture); `nn.LazyLinear` defers shape inference; `nn.Parameter` wraps a tensor as a tracked weight; `net.to(device)` migrates the model across CPU/[[GPU]] boundaries with explicit operand-locality rules.
