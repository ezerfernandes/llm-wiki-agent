---
title: "Neural Network"
type: concept
tags: [neural-networks, architecture]
sources: [madewithml-baselines, d2l-multilayer-perceptrons, mlsysbook-ch05-neural-computation]
last_updated: 2026-06-05
---

# Neural Network

A composition of differentiable layers with learnable parameters, trained end-to-end by [[GradientDescent|gradient descent]] + [[Backpropagation|backprop]] on a [[ComputationalGraph]]. Foundation for [[MultilayerPerceptron]], [[RNN]], [[CNN]], [[Transformer]], and modern deep learning. [[d2l-multilayer-perceptrons]] is the canonical pedagogical entry: hidden layers + [[ActivationFunction|nonlinear activation]] + [[ForwardPropagation|forward]] / [[Backpropagation|backward]] propagation + [[XavierInitialization|Xavier]] / [[HeInitialization|He]] init + [[Dropout]] is the minimum viable mental model.

## Systems view (mlsysbook Ch 5)

[[mlsysbook-ch05-neural-computation|mlsysbook Vol 1 Ch 5]] treats the network as a *computational workload*: every net reduces to [[MatrixMultiplication|matrix multiplications]] ([[GEMM]] = >90% of FLOPs) interleaved with [[ActivationFunction|activations]], built up from the [[ArtificialNeuron|artificial neuron]] (N [[MultiplyAccumulate|MACs]] + 2N+2 memory accesses each). Four emergent properties drive its infrastructure demands — adaptive parameterization, parallel integration, hierarchical representation ([[Compositionality|compositionality]]), and resource economy (data reuse against the [[MemoryWall|memory wall]]). The model's parameter count, precision, and operations set the terms of the [[IronLawOfMLSystems|silicon contract]] (see [[ModelSize]]).

## Connections

- [[ArtificialNeuron]] / [[MultilayerPerceptron]] / [[WeightMatrix]] — the building blocks.
- [[ForwardPropagation]] / [[Backpropagation]] / [[GradientDescent]] — the train/infer cycle.
- [[ActivationFunction]] / [[MatrixMultiplication]] / [[GEMM]] — the dominant primitives.
- [[Compositionality]] / [[ModelSize]] / [[DAMTaxonomy]] — why depth and scale matter, and how Data·Algorithm·Machine align.
- [[mlsysbook-ch05-neural-computation]] — systems-level treatment.
