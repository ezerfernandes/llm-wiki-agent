---
title: "Neural Network"
type: concept
tags: [neural-networks, architecture]
sources: [madewithml-baselines, d2l-multilayer-perceptrons]
last_updated: 2026-05-16
---

# Neural Network

A composition of differentiable layers with learnable parameters, trained end-to-end by [[GradientDescent|gradient descent]] + [[Backpropagation|backprop]] on a [[ComputationalGraph]]. Foundation for [[MultilayerPerceptron]], [[RNN]], [[CNN]], [[Transformer]], and modern deep learning. [[d2l-multilayer-perceptrons]] is the canonical pedagogical entry: hidden layers + [[ActivationFunction|nonlinear activation]] + [[ForwardPropagation|forward]] / [[Backpropagation|backward]] propagation + [[XavierInitialization|Xavier]] / [[HeInitialization|He]] init + [[Dropout]] is the minimum viable mental model.
