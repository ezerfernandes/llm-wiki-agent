---
title: "Theano"
type: entity
tags: [framework, deep-learning, history, computational-graph]
sources: [mlsysbook-ch07-ml-frameworks]
last_updated: 2026-06-05
---

# Theano

**Theano** was an early and influential Python deep-learning framework, developed at the Montreal Institute for Learning Algorithms (MILA) under Yoshua Bengio starting in **2007**. Its key insight — that a Python-defined symbolic [[ComputationalGraph|computational graph]] could be compiled to optimized CPU/GPU (CUDA) code without the researcher writing GPU code — became the architectural template for [[TensorFlow]] (2015) and influenced [[PyTorch]]'s autograd design. Theano is the rung on the [[LadderOfAbstraction|Ladder of Abstraction]] that "solved differentiation," turning the chain rule into a software primitive via the computational graph. It was retired in 2017, but every modern framework inherits its core abstraction.

## Connections

- [[mlsysbook-ch07-ml-frameworks]] — the 2007 origin of graph-based deep learning in Python.
- [[ComputationalGraph]] — the abstraction Theano popularized.
- [[LadderOfAbstraction]] — Theano's rung; [[TensorFlow]] / [[PyTorch]] — its successors.
