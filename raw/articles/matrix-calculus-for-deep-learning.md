# The Matrix Calculus You Need For Deep Learning

> Source URL: https://explained.ai/matrix-calculus/
> Authors: Terence Parr (University of San Francisco; later Google) and Jeremy Howard (fast.ai)
> Captured: 2026-06-04 via web fetch (structured extraction of the HTML article)

## Purpose

Explains the matrix calculus needed to understand the training of deep neural networks,
assuming only Calculus 1 background. Understanding matrix calculus is not strictly required
to *practice* deep learning, but it is essential for reading academic papers and for
grasping/optimizing what training does. The authors rederive the key rules "in an effort to
explain them," with the thesis that "matrix calculus is really not that hard!"

## Section structure

### 1. Review: Scalar Derivative Rules
- Constant rule, multiplication-by-constant, power rule.
- Sum, difference, product, and (single-variable) chain rules.
- Foundation built from familiar Calculus 1.

### 2. Introduction to Vector Calculus and Partial Derivatives
- Partial derivatives (∂/∂x notation).
- Gradient = vector of partial derivatives, organized as a horizontal (row) vector.
- Functions of multiple parameters.

### 3. Matrix Calculus
- **The Jacobian matrix**: stacked gradients organizing partial derivatives into a matrix.
  Authors note there are multiple conventions: **numerator layout** vs **denominator layout**.
  They deliberately adopt the *numerator layout* (functions vary down rows, variables across
  columns) and flag the alternative so readers can navigate other papers.
- **Generalization of the Jacobian**: m scalar-valued functions stacked into vector **f** of
  n parameters → Jacobian is m rows × n columns.
- **Derivatives of element-wise binary operators**: element-wise operations produce *diagonal*
  Jacobians when the "element-wise diagonal condition" holds (each output element depends only
  on the correspondingly-indexed input element). Examples:
  - Vector addition: ∂(**w** + **x**)/∂**w** = I (identity).
  - Element-wise (Hadamard) multiplication: diagonal matrix of corresponding elements.
  - Element-wise division: diagonal structure.
- **Scalar expansion**: adding/multiplying a scalar broadcasts it across the vector
  (x + z → x + z·**1**; z·**x** → z ⊙ **x**), yielding diagonal Jacobians.
- **Vector sum reduction**: ∂(Σᵢ fᵢ)/∂**x** is a horizontal (transposed) vector.

### 4. The Chain Rules (three variants)
- **Single-variable chain rule** — for nested functions like y = sin(x²): introduce
  intermediate variables, differentiate each stage, multiply the results ("chain").
- **Single-variable total-derivative chain rule** — for functions where a variable appears
  along multiple dataflow paths (e.g. y = x² + x). The total derivative *sums* the
  contributions of all paths: ∂f/∂x = Σⱼ (∂f/∂uⱼ)(∂uⱼ/∂x). The crucial fix over the naive
  chain rule: **summation**, not multiplication alone, accounts for every path from parameter
  to output.
- **Vector chain rule** — most general: ∂**f**(g(**x**))/∂**x** = (∂**f**/∂**g**)(∂**g**/∂**x**),
  a product of Jacobian matrices. It "automatically takes into consideration the total
  derivative while maintaining notational simplicity." When intermediate functions are
  element-wise and satisfy the diagonal condition, it simplifies to
  ∂y/∂**x** = diag(∂fᵢ/∂gᵢ) · (∂**g**/∂**x**).

### 5. The Gradient of Neuron Activation
For activation u = max(0, **w**·**x** + b):
- Dot-product derivative: ∂(**w**·**x**)/∂**w** = **x**ᵀ.
- ReLU derivative: ∂max(0,z)/∂z = 0 if z ≤ 0, else 1.
- Combined: ∂u/∂**w** = **0**ᵀ if z ≤ 0, else **x**ᵀ.

### 6. The Gradient of the Neural Network Loss Function
Using MSE loss C = (1/N) Σᵢ vᵢ² with vᵢ = yᵢ − uᵢ:
- **Gradient w.r.t. weights**: ∂C/∂**w** ∝ (1/N) Σᵢ (error termᵢ) · **xᵢ**ᵀ — an error-weighted
  average of input vectors; large errors emphasize their inputs.
- **Gradient w.r.t. bias**: ∂C/∂b = (2/N) Σᵢ {0 if z ≤ 0; **w**·**xᵢ** + b − yᵢ if z > 0}.
- **Gradient-descent update**: **w** ← **w** − α(∂C/∂**w**), b ← b − α(∂C/∂b); learning rate α
  scales the step; subtracting the gradient moves toward lower cost.

## Key notation
| Symbol | Meaning |
|--------|---------|
| ∂f/∂x | partial derivative |
| ∇f | gradient (vector of partials) |
| ∂**f**/∂**x** | Jacobian matrix |
| **x**ᵀ | vector transpose |
| diag(**x**) | diagonal matrix from a vector |
| ⊙ | Hadamard (element-wise) product |
| **x** vs x | bold = vector, plain = scalar |

## Major takeaways
1. Decompose complex expressions into simple subexpressions, differentiate each, recombine via
   the chain rule.
2. The Jacobian organizes all partial derivatives; its frequently-diagonal structure simplifies
   computation drastically.
3. Total derivatives matter: when a variable has multiple dependency paths, *sum* all path
   contributions.
4. In neural nets, weight gradients point in the error-weighted input direction; bias updates
   average the errors.
5. Autodiff libraries handle this in practice, but manual derivation reveals what happens under
   the hood.
