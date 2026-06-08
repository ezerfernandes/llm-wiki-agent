---
title: "Transistor Tax"
type: concept
tags: [hardware, activation-functions, ml-systems, efficiency]
sources: [mlsysbook-ch05-neural-computation]
last_updated: 2026-06-05
---

# Transistor Tax

The silicon-area and energy cost difference between [[ActivationFunction|activation functions]], framed as a **Logic Unit Cost** (transistor count + energy per operation). Coined in [[mlsysbook-ch05-neural-computation|mlsysbook Vol 1 Ch 5]] to explain why the deep-learning era abandoned the "biologically plausible" [[Sigmoid|sigmoid]] for the "silicon-efficient" [[ReLU]].

## The numbers

- **[[ReLU]]** = a single comparator + multiplexer ≈ **50 transistors, 1 cycle**.
- **[[Sigmoid]] / [[Tanh]]** = a floating-point exponential approximated via lookup tables or iterative Taylor expansion ≈ **2,500 transistors, 20–40 cycles**.
- Net: selecting sigmoid over ReLU raises the silicon "price" of an activation by **~50×**, and this penalty scales with *every neuron in every layer*.

ReLU is therefore a **density optimization**: it lets hardware architects pack orders of magnitude more neurons into the same power and area budget. The activation choice is thus *both* a gradient-stability decision (avoiding the [[VanishingGradient|vanishing gradient]]) *and* a hardware decision.

## Connections

- [[ActivationFunction]] / [[ReLU]] / [[Sigmoid]] / [[Tanh]] — the functions being priced.
- [[ArithmeticIntensity]] / [[ComputeBound]] — related per-operation cost framing.
- [[VanishingGradient]] — the other reason ReLU won.
- [[mlsysbook-ch05-neural-computation]] — source of the term and the ~50× figure.
