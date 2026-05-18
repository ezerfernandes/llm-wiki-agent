---
title: "Co-adaptation"
type: concept
tags: [deep-learning, regularization, theory]
sources: [d2l-multilayer-perceptrons]
last_updated: 2026-05-16
---

# Co-adaptation

In [[NeuralNetwork|neural-network]] training, the phenomenon where hidden units in a layer rely on *specific patterns of activations* in the previous layer rather than learning robust independent features. [[NitishSrivastava|Srivastava]], [[GeoffreyHinton|Hinton]], [[AlexKrizhevsky|Krizhevsky]] et al. (2014) argued that overfitting in deep networks is *characterized* by co-adaptation, and proposed [[Dropout|dropout]] as a remedy — by analogy to sexual reproduction breaking up co-adapted genes ([[d2l-multilayer-perceptrons]] §Dropout).

## Why it matters

Co-adapted units are fragile: their useful behaviour depends on the precise pattern of upstream activations, which may be a memorized training-set artifact. [[Dropout]] forces each unit to be *individually useful* by randomly zeroing its peers, breaking dependencies and pushing the network toward more redundant, robust representations.

## Relation to other ideas

- **[[Dropout]]** is the canonical intervention.
- **Bishop (1995) noise-injection ≡ Tikhonov regularization** is the formal cousin — adding noise to inputs forces the function to be smooth.
- **Batch normalization** independently shifts activations and partly compensates for co-adaptation downstream.
- **Permutation symmetry** at initialization is the *extreme* case of co-adaptation — all units identical.

## Caveat

[[d2l-multilayer-perceptrons]] flags that the co-adaptation justification for dropout is debatable ("such a justification of this theory is certainly up for debate"), even though the technique itself works robustly. The Tikhonov / unbiased-noise framing is the more formally defensible motivation.

## Connections

- [[d2l-multilayer-perceptrons]] — §Dropout (origin of the term in deep learning).
- [[Dropout]] — the remedy.
- [[Regularization]] — the broader class.
- [[NitishSrivastava]] / [[GeoffreyHinton]] / [[AlexKrizhevsky]] — dropout / co-adaptation authors.
- [[Overfitting]] — what co-adaptation is a putative mechanism of.
