---
title: "Dive into Deep Learning — Multilayer Perceptrons"
type: source
tags: [textbook, d2l, mlp, deep-learning, activation-functions, backpropagation, dropout, regularization]
date: 2026-05-16
source_file: raw/d2l-en/chapter_multilayer-perceptrons/
---

## Summary

[[AstonZhang|Zhang]], [[ZacharyLipton|Lipton]], [[MuLi|Li]] & [[AlexanderSmola|Smola]]'s seven-section chapter introducing the first genuinely *deep* network in [[d2l-preface|D2L]]: the **[[MultilayerPerceptron|multilayer perceptron (MLP)]]**. Builds from the limitations of linear models through [[HiddenLayer|hidden layers]] + nonlinear [[ActivationFunction|activations]] ([[ReLU]], [[Sigmoid]], [[Tanh]]), the [[UniversalApproximationTheorem|universal-approximation]] result, [[ForwardPropagation|forward]] / [[Backpropagation|backward]] propagation on the [[ComputationalGraph|computational graph]], numerical-stability pathologies ([[VanishingGradient|vanishing]] / [[ExplodingGradient|exploding]] gradients, permutation symmetry) and their initialization remedies ([[XavierInitialization|Xavier]] / [[HeInitialization|He]]), the modern [[Generalization|generalization]] story (over-parametrization, [[InterpolationRegime|interpolation regime]], [[DoubleDescent|double descent]], [[NeuralTangentKernel|NTK]], [[EarlyStopping|early stopping]]), [[Dropout|dropout]] regularization, and a complete [[Kaggle]] house-price prediction case study as the chapter capstone. Marks D2L's transition from linear models to genuine deep networks.

## Key Claims

- **Stacking affine layers without nonlinearity collapses to a single affine map.** A two-layer model $\mathbf{O} = (\mathbf{X}\mathbf{W}^{(1)} + \mathbf{b}^{(1)})\mathbf{W}^{(2)} + \mathbf{b}^{(2)}$ rewrites exactly as $\mathbf{X}\mathbf{W} + \mathbf{b}$ with $\mathbf{W} = \mathbf{W}^{(1)}\mathbf{W}^{(2)}$, so **a nonlinear [[ActivationFunction|activation]] is *necessary* for depth to add expressive power**.
- **[[ReLU|ReLU]] $\sigma(x) = \max(0, x)$ is the default hidden-layer activation** ([[Nair-Hinton-2010|Nair & Hinton 2010]]). Its piecewise-linear derivative (0 or 1) avoids the saturating-region [[VanishingGradient|vanishing gradients]] of [[Sigmoid|sigmoid]] / [[Tanh|tanh]] and is "significantly more amenable to optimization … arguably one of the key innovations that helped the resurgence of deep learning."
- **[[Sigmoid|Sigmoid]] and [[Tanh|tanh]] are squashing activations whose gradients vanish in the saturated tails** (sigmoid maxes its derivative at 0.25 at $x=0$; tanh maxes at 1 at $x=0$). They survive only at output units (probability interpretation) and inside gated units (LSTM / GRU); ReLU has displaced them in hidden layers.
- **[[UniversalApproximationTheorem|Universal approximation]]** ([[GeorgeCybenko|Cybenko 1989]]): even a *single-hidden-layer* MLP with enough units can approximate any function — but "actually learning that function is the hard part" and deeper-rather-than-wider networks tend to be more compact ([[KarenSimonyan|Simonyan]] & [[AndrewZisserman|Zisserman]] 2014).
- **[[ForwardPropagation|Forward propagation]] sequentially evaluates and *caches* intermediate variables**; [[Backpropagation|backpropagation]] then traverses the [[ComputationalGraph|computational graph]] in *reverse* applying the [[ChainRule|chain rule]] to compute parameter gradients. Forward and backward are *interdependent* — backward reuses cached forward activations, which is why training requires significantly more memory than prediction (roughly proportional to depth × batch size).
- **The gradient through $L$ layers is a product of $L$ Jacobian matrices.** Initial matrices can have arbitrary eigenvalues, so the product *either explodes or vanishes exponentially* — manifesting as the **[[ExplodingGradient|exploding]]** and **[[VanishingGradient|vanishing]] gradient** problems. Multiplying 100 random Gaussian $4\times 4$ matrices is shown to blow up numerically.
- **Permutation symmetry must be broken at initialization.** Initializing all weights to the same constant makes every hidden unit compute the same activation and receive the same gradient — the hidden layer behaves as if it had one unit. **Random initialization breaks the symmetry**; dropout regularization also breaks it, but minibatch SGD alone does not.
- **[[XavierInitialization|Xavier (Glorot) initialization]]** ([[XavierGlorot|Glorot]] & [[YoshuaBengio|Bengio]] 2010) variance $\sigma^2 = \tfrac{2}{n_\text{in} + n_\text{out}}$ approximately preserves activation variance forward *and* gradient variance backward. Even with the nonlinearity-free assumption violated, Xavier works well in practice; ReLU networks typically use the [[HeInitialization|He / Kaiming]] variant ([[KaimingHe|He et al. 2015]]) with $\sigma^2 = \tfrac{2}{n_\text{in}}$.
- **Deep networks are over-parametrized**: they can fit even random labels on millions of examples ([[ChiyuanZhang|Zhang]] et al. 2021). All architectures under consideration achieve ~zero training error, so *the only remaining axis for improvement is reducing the generalization gap* — yet this gap can be reduced by *adding* capacity, producing the non-monotonic **[[DoubleDescent|double-descent]]** curve ([[PreetumNakkiran|Nakkiran]] et al. 2021).
- **Classical complexity-based bounds ([[VCDimension|VC dimension]], [[RademacherComplexity|Rademacher complexity]]) are vacuous for deep networks** that can fit arbitrary labels yet still generalize. Deep networks behave more like *nonparametric* models in the [[InterpolationRegime|interpolation regime]]; the [[NeuralTangentKernel|neural tangent kernel]] ([[ArthurJacot|Jacot]] et al. 2018) makes the infinite-width-MLP-↔-kernel connection precise.
- **[[Dropout|Dropout]]** ([[NitishSrivastava|Srivastava]], [[GeoffreyHinton|Hinton]], [[AlexKrizhevsky|Krizhevsky]] et al. 2014) injects unbiased multiplicative noise — each activation is zeroed with probability $p$ and surviving activations are scaled by $1/(1-p)$, preserving expectations. Connects to [[ChrisBishop|Bishop's]] 1995 result that input noise ≈ Tikhonov regularization, and to the [[Coadaptation|co-adaptation]] story: dropout breaks dependencies among hidden units. Typically *disabled at test time*.
- **[[EarlyStopping|Early stopping]] is the classical-regularization technique that survives best for deep networks.** Networks fit cleanly-labeled examples *before* memorizing label noise, so stopping at the inflection point ("patience criterion") gives both generalization and substantial wall-clock + GPU-cost savings.
- **[[WeightDecay|Weight decay]] / $\ell_2$ regularization remains popular** in deep-learning implementations despite the theoretical caveat that "typical strengths of $\ell_2$ regularization are insufficient to prevent the networks from interpolating the data" — its real role is to encode *inductive biases* compatible with data, not to bound complexity in the classical sense.
- **The [[Kaggle]] House Prices competition** (Ames, Iowa 2006–2010; [[Cock-2011|De Cock 2011]]) is the chapter's capstone: a hands-on regression case study covering Pandas-driven preprocessing, log-price loss, and an MLP-with-dropout pipeline. Marks D2L's first end-to-end real-data project.

## Key Quotes

> "An affine function of an affine function is itself an affine function. Moreover, our linear model was already capable of representing any affine function." — `mlp.md` §From Linear to Nonlinear

> "Even with a single-hidden-layer network, given enough nodes (possibly absurdly many), and the right set of weights, we can model any function. Actually learning that function is the hard part, though." — `mlp.md` §Universal Approximators

> "Forward propagation sequentially calculates and stores intermediate variables within the computational graph defined by the neural network. … Backpropagation sequentially calculates and stores the gradients of intermediate variables and parameters within the neural network in the reversed order." — `backprop.md` §Summary

> "Vanishing and exploding gradients are common issues in deep networks. Great care in parameter initialization is required … Random initialization is key to ensuring that symmetry is broken before optimization." — `numerical-stability-and-init.md` §Summary

> "Strangely, for many deep learning tasks … we are typically choosing among model architectures, all of which can achieve arbitrarily low training loss (and zero training error). Because all models under consideration achieve zero training error, *the only avenue for further gains is to reduce overfitting*." — `generalization-deep.md` §Revisiting Overfitting and Regularization

> "Throughout training, on each iteration, standard dropout consists of zeroing out some fraction of the nodes in each layer before calculating the subsequent layer. … By design, the expectation remains unchanged, i.e., $E[h']=h$." — `dropout.md` §Dropout

## Connections

- [[d2l-preface]] — pedagogical thesis (concepts / context / code, just-in-time).
- [[d2l-introduction]] — broad ML/DL survey context.
- [[d2l-preliminaries]] — tensors, calculus, autograd, computational graph background.
- [[d2l-linear-regression]] — linear-model baseline that MLP extends.
- [[d2l-linear-classification]] — [[Softmax|softmax regression]] is the *output layer* an MLP composes with.
- [[MultilayerPerceptron]] — the architecture introduced.
- [[HiddenLayer]] — the central new building block.
- [[ActivationFunction]] — nonlinearity that unlocks depth's expressive power.
- [[ReLU]] / [[Sigmoid]] / [[Tanh]] — the three core hidden-layer activations.
- [[UniversalApproximationTheorem]] — single-hidden-layer expressivity result.
- [[ForwardPropagation]] / [[Backpropagation]] — the training-loop primitives, on the [[ComputationalGraph]].
- [[ChainRule]] — calculus behind backprop.
- [[VanishingGradient]] / [[ExplodingGradient]] — the gradient-product pathologies.
- [[XavierInitialization]] / [[HeInitialization]] — initialization remedies.
- [[WeightInitialization]] — parent concept (now expanded with Xavier derivation).
- [[Dropout]] — the chapter's regularization centrepiece.
- [[EarlyStopping]] — companion regularization technique.
- [[WeightDecay]] / [[Regularization]] — classical regularizers in deep-learning context.
- [[Generalization]] / [[GeneralizationGap]] / [[Overfitting]] — modern generalization story (over-parametrization, interpolation, double descent).
- [[DoubleDescent]] — non-monotonic complexity–error curve.
- [[InterpolationRegime]] — "fit training perfectly" zero-training-loss regime.
- [[NeuralTangentKernel]] — infinite-width MLP ↔ kernel-method connection.
- [[Coadaptation]] — the phenomenon dropout breaks.
- [[Kaggle]] — platform hosting the chapter's capstone competition.
- [[NeuralNetwork]] — supercategory of MLPs.
- [[StochasticGradientDescent]] / [[MinibatchSGD]] — optimizer paired with backprop.
- [[FashionMNIST]] — Fashion-MNIST is the running benchmark for the MLP-from-scratch + dropout-from-scratch implementations.
- [[NitishSrivastava]] / [[GeoffreyHinton]] / [[AlexKrizhevsky]] — dropout authors (entities exist or stubs).

## Contradictions

- **None direct.** Reaffirms the [[d2l-linear-classification]] / [[GeneralizationGap]] caveat that classical [[VCDimension|VC]] / [[RademacherComplexity|Rademacher]] bounds are vacuous for modern over-parametrized networks. Reaffirms the [[Overfitting]] page's "best predictive models often perform far better on training data than holdout" framing in the [[DoubleDescent|double-descent]] direction. No tension with prior D2L chapters or with [[mml-book|MML]] / [[pml1-murphy|Murphy]] / [[islr-seventh-printing|ISLR]] / [[madewithml-baselines|MWML]] coverage.
