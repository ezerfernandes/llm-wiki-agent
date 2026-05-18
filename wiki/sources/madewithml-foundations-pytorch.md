---
title: "Made With ML — PyTorch Fundamentals"
type: source
tags: [foundations, made-with-ml, pytorch, tensors, autograd, course]
date: 2026-05-15
source_file: raw/madewithml/foundations-pytorch.md
---

## Summary
Bridge lesson from [[NumPy]] to [[PyTorch]]. Introduces `torch.Tensor` as a NumPy-array-like object with two additional capabilities: GPU placement (via `.to(device)` and CUDA) and automatic differentiation (via `requires_grad=True` and `.backward()`). Covers tensor creation (`torch.randn`, `torch.zeros`, `torch.ones`, conversion from Python lists and NumPy arrays), type changes (`.long()`, `.float()`), arithmetic, matrix multiplication (`torch.mm`), indexing and slicing (mirrors NumPy), `torch.cat` joining, and the gradient mechanics: build a computation graph with `requires_grad=True` leaves, run `.backward()` on a scalar output, and read accumulated gradients from `.grad`. Closes with the CUDA section showing how `torch.cuda.is_available()` + `device = torch.device("cuda" if ... else "cpu")` is the portable cross-hardware idiom every subsequent deep-learning lesson uses.

## Key Claims
- `torch.Tensor` is intentionally NumPy-API-shaped so practitioners can transfer mental models — the two real additions are device placement and autograd.
- Reproducibility requires seeding both NumPy (`np.random.seed`) *and* PyTorch (`torch.manual_seed`); seeding only one leaves stochastic ops in the other library uncontrolled.
- Autograd records a dynamic computation graph as ops execute; `.backward()` on a scalar populates `.grad` on every leaf with `requires_grad=True` via the chain rule. This is the entire mechanism behind every deep-learning optimization step in the course.
- The `device = torch.device("cuda" if torch.cuda.is_available() else "cpu")` pattern + `.to(device)` calls is the canonical write-once-run-anywhere recipe for code that should work on both laptops and GPU clusters.
- Default tensor dtype is `float32` (`torch.FloatTensor`); converting to `long` is required for index tensors (e.g. classification labels) consumed by losses like `CrossEntropyLoss`.
- `torch.mm(a, b)` is the explicit matrix-multiply primitive; in higher-level code the `@` operator and `nn.Linear` wrap this, but the gradient flow is the same.

## Key Quotes
> "PyTorch is a popular ML framework that allows us to perform tensor calculations and create models for machine learning."

> "We can set a seed for reproducibility."

## Connections
- [[GokuMohandas]] — author.
- [[MadeWithML]] — parent course.
- [[PyTorch]] — the library itself.
- [[Tensor]] — central data structure.
- [[Autograd]] — automatic differentiation engine.
- [[CUDA]] — NVIDIA GPU compute backend.
- [[NumPy]] — prerequisite; tensor API is intentionally NumPy-shaped.
- [[Python]] — prerequisite language.
- [[pandas]] — sibling foundations lesson; DataFrames frequently feed tensors.
- [[Gradient]] — the computational quantity autograd produces.
- [[BackPropagation]] — algorithm autograd implements.
- [[NeuralNetwork]] — downstream construct built on tensors + autograd.

## Contradictions
None — fundamentals lesson; the rest of the deep-learning track (linear regression, neural networks, CNNs, RNNs, attention, transformers) builds directly on the device + autograd primitives introduced here.
