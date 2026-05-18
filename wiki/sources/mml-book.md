---
title: "Mathematics for Machine Learning"
type: source
tags: [textbook, mathematics, foundations, linear-algebra, calculus, probability, optimization, regression, dimensionality-reduction, density-estimation, classification]
date: 2020-01-01
source_file: raw/mml-book.pdf
---

## Summary

[[MarcDeisenroth]], [[AAldoFaisal]] & [[ChengSoonOng]]'s 417-page [[CambridgeUniversityPress]] textbook (2020 first ed., draft revision 2024-01-15; freely available at <https://mml-book.com>) packages the **mathematical pre-requisites needed to read a modern machine-learning textbook** into a single self-contained volume. The book is split into two parts: **Part I — Mathematical Foundations** ([[LinearAlgebra]], [[AnalyticGeometry]], [[MatrixDecomposition]], [[VectorCalculus]], [[ProbabilityAndDistributions]], [[ContinuousOptimization]]) — and **Part II — Central Machine Learning Problems** ([[LinearRegression]], [[PrincipalComponentAnalysis|PCA]], [[GaussianMixtureModel|Gaussian Mixture Models]], [[SupportVectorMachine|SVM]]). The four pillars (regression, dimensionality reduction, density estimation, classification) are deliberately framed as *applications* of the six mathematical foundations, with the explicit goal of closing the "high-school-math → ML-textbook" gap. It positions itself between [[pml1-murphy|Murphy's *Probabilistic ML*]] (broader ML methods, assumes the math) and Bishop / MacKay (covers some background but only a chapter or two).

## Key Claims

- **A practitioner who only uses ML libraries risks not knowing the *design decisions and limits* of the algorithms** (Foreword, p. 1). The book is written to surface those decisions through their mathematical content.
- **Three audience types** (Foreword, pp. 2–3) — *Astute Listener* (informed consumer; needs background for ethics/fairness/risk-management of ML), *Experienced Artist* (practitioner extending favorite methods), *Fledgling Composer* (researcher developing new methods). Same book, different reading modes (top-down vs bottom-up; §1.2).
- **Three core ML concepts** (§1, p. 11): *data*, *model*, *learning*. Data → vectors; models → simplified data-generating processes (probabilistic or as functions); learning → optimization of model parameters against a utility / loss function over training data, with the goal of generalizing to unseen data.
- **Four pillars × six foundations** (§1.2 / Fig. 1.1): regression / dim-reduction / density-estimation / classification sit on top of linear algebra, analytic geometry, matrix decomposition, vector calculus, probability & distributions, and continuous optimization.
- **Linear algebra is the substrate** (Ch 2): vectors are anything closed under addition and scalar multiplication — geometric vectors, polynomials, audio signals, $\mathbb{R}^n$ tuples. ML largely lives in $\mathbb{R}^n$. The chapter's mind map (Fig. 2.2): Vector → Vector Space (closure) → Linear Independence → Basis; Matrix → System of Linear Equations → Gaussian Elimination; Linear Mapping connects them.
- **Analytic geometry adds geometry to linear algebra** (Ch 3): [[InnerProduct]]s induce [[Norm]]s induce metrics. [[CauchySchwarzInequality]] defines [[Angle]]. [[OrthogonalProjection]] is *the* operation behind least-squares regression (Ch 9), PCA (Ch 10), and SVM margin (Ch 12). [[SymmetricPositiveDefiniteMatrix|Symmetric positive definite matrices]] characterize all valid inner products in $\mathbb{R}^n$ (Thm 3.5).
- **Matrix decomposition = matrix factoring** (Ch 4, p. 98): "An analogy for matrix decomposition is the factoring of numbers, such as the factoring of 21 into prime numbers 7·3." Determinant + trace summarize a matrix in numbers; Cholesky, Eigendecomposition, SVD factor it into interpretable factors. **The determinant is the signed volume of the parallelepiped spanned by columns** (§4.1, Example 4.2) — the geometric reading that justifies its later appearance in change-of-variables (§6.7) and Gaussian densities (§6.5).
- **Vector calculus = the gradient machinery for optimization** (Ch 5). Partial derivatives collected in a [[Jacobian]] (§5.2 — the row-vector convention is a deliberate choice). [[TaylorSeries]] extends to multivariate Taylor (§5.8) for [[Linearization]]; [[Backpropagation]] is automatic differentiation via the chain rule (§5.6) and is the mathematical content of neural-net training.
- **Probability is a generalization of Boolean logic** (Ch 6, §6.1.1 — citing Jaynes 2003). [[CoxJaynesTheorem]] proves that any internally consistent assignment of plausibilities must obey the rules of probability. The book is *agnostic* between Bayesian and frequentist interpretations (§6.1, Remark) but routinely uses both. A [[ProbabilitySpace]] = (sample space $\Omega$, event space $\mathcal{A}$, probability $P$); a [[RandomVariable]] is a function $X:\Omega\to\mathcal{T}$, not a variable. *"The name 'random variable' is a great source of misunderstanding as it is neither random nor it is a variable. It is a function."* (§6.1.2, marginal note, p. 175).
- **Optimization splits two ways** (Ch 7): unconstrained ([[GradientDescent]] + [[Momentum]] + [[StochasticGradientDescent|SGD]], §7.1) vs constrained ([[LagrangeMultipliers]], §7.2) plus the special case of [[ConvexOptimization]] (§7.3) where *every local minimum is global* and duality theory applies. The [[ConditionNumber]] $\kappa = \sigma_{\max}/\sigma_{\min}$ (§7.1.1) — the ratio of largest to smallest singular value — controls gradient-descent convergence speed.
- **Empirical Risk Minimization is the framing of supervised learning** (§8.2, p. 258). [[MaximumLikelihoodEstimation|MLE]] (§8.3) is its probabilistic counterpart; full Bayesian inference (§8.4) integrates over the parameter uncertainty rather than picking a point estimate. **Model selection happens at a higher level** (§8.6) via [[NestedCrossValidation|nested cross-validation]] — and philosophically is *[[Abduction|abduction]]*, not induction or deduction (§8.2 marginal).
- **Linear regression is "linear in the parameters, not in the inputs"** (Ch 9, §9.2 remark, p. 295). A polynomial regression is a *linear* model because $\boldsymbol\theta$ enters linearly through a [[FeatureMap]] $\phi(\mathbf{x})$. The MLE closed form $\boldsymbol\theta_{\text{ML}} = (\mathbf{X}^\top\mathbf{X})^{-1}\mathbf{X}^\top\mathbf{y}$ is derived as both an [[OrthogonalProjection]] (§9.4) and the gradient-zero solution to squared-error NLL (§9.2.1). [[BayesianLinearRegression]] (§9.3) integrates parameters out instead.
- **PCA is the [[KarhunenLoeveTransform]]** (Ch 10, p. 318). Three equivalent derivations (§10.2 maximum variance, §10.3 minimum reconstruction error, §10.7 latent-variable / probabilistic PCA) all yield the same answer: project onto the $M$ eigenvectors of the [[DataCovarianceMatrix]] $\mathbf{S}=\frac{1}{N}\sum \mathbf{x}_n\mathbf{x}_n^\top$ with the largest eigenvalues. The variance retained by an $M$-dim projection equals $\sum_{m=1}^M \lambda_m$ (Eq. 10.23). PCA is "compression like JPEG or MP3" without losing the dominant signal.
- **The EM algorithm is the workaround for the no-closed-form GMM MLE** (Ch 11, §11.2–11.3). The log-likelihood $\sum_n \log \sum_k \pi_k \mathcal{N}(\mathbf{x}_n|\boldsymbol\mu_k, \boldsymbol\Sigma_k)$ cannot be optimized in closed form (the log can't enter the sum over $k$, p. 351). The fix is to introduce [[Responsibility|responsibilities]] $r_{nk}$ (soft cluster assignments, §11.2.1) and alternate: E-step recomputes $r_{nk}$ given parameters; M-step recomputes $(\boldsymbol\mu_k, \boldsymbol\Sigma_k, \pi_k)$ given $r_{nk}$. The mean update $\boldsymbol\mu_k^{\text{new}} = \frac{\sum r_{nk}\mathbf{x}_n}{\sum r_{nk}}$ is an importance-weighted Monte Carlo estimate.
- **The SVM is the geometric counterpart to MLE-driven linear regression** (Ch 12, p. 371). Where Ch 9 starts from a probabilistic model and derives an optimization problem, the SVM *starts from the loss function* (maximize the [[Margin]] $r$, geometrically) and arrives at a [[ConvexOptimization]] problem (quadratic programming) with no analytic solution. Hard-margin: $\min \frac{1}{2}\|\mathbf{w}\|^2$ s.t. $y_n(\langle\mathbf{w},\mathbf{x}_n\rangle+b)\geq 1$. The dual (Ch 12.3) exposes support vectors; the kernel trick (Ch 12.4) lifts the SVM to nonlinear classifiers without ever computing $\phi(\mathbf{x})$ explicitly.
- **The book intentionally provides only four representative ML algorithms** (Foreword, p. 2): linear regression, PCA, GMM, SVM. These are *worked examples* of the foundations, not a survey — for that, the book defers to Bishop / MacKay / Murphy / Shalev-Shwartz–Ben-David.

## Key Quotes

> "Machine learning is the latest in a long line of attempts to distill human knowledge and reasoning into a form that is suitable for constructing machines and engineering automated systems." — Foreword, p. 1
> 
> Framing for why mathematical foundations matter: ML libraries hide the math, but the *design decisions* sit in the math.

> "We have found many people who want to delve into the foundations of basic machine learning methods who struggle with the mathematical knowledge required to read a machine learning textbook. Having taught undergraduate and graduate courses at universities, we find that the gap between high school mathematics and the mathematics level required to read a standard machine learning textbook is too big for many people. This book brings the mathematical foundations of basic machine learning concepts to the fore..." — Foreword, p. 1
> 
> The mission statement. This book exists to close the gap that Murphy/Bishop/MacKay assume away.

> "Math is linked in the popular mind with phobia and anxiety. You'd think we're discussing spiders." — Strogatz 2014, quoted in Foreword margin, p. 2

> "We provide only four representative examples of machine learning algorithms. Instead, we focus on the mathematical concepts behind the models themselves." — Foreword, p. 2
> 
> Frames the book's scope: this is a *math* book applied to ML, not an ML survey.

> "The name 'random variable' is a great source of misunderstanding as it is neither random nor it is a variable. It is a function." — §6.1.2 marginal, p. 175
> 
> Cuts through the standard naming confusion at the foundation of probability.

> "Linear regression refers to models that are linear in the parameters, but the inputs can undergo any nonlinear transformation." — §9.2 marginal, p. 295
> 
> The distinction that lets [[PolynomialRegression]] / [[KernelRegression]] all sit under the "linear regression" framework.

> "Working directly with high-dimensional data, such as images, comes with some difficulties: It is hard to analyze, interpretation is difficult, visualization is nearly impossible, and (from a practical point of view) storage of the data vectors can be expensive." — §10, p. 317
> 
> The motivation for dimensionality reduction — and implicitly for the [[CurseOfDimensionality]] discussed in Corpus II / VI.

> "The SVM view of machine learning is subtly different from the maximum likelihood view of Chapter 9. The maximum likelihood view proposes a model based on a probabilistic view of the data distribution, from which an optimization problem is derived. In contrast, the SVM view starts by designing a particular function that is to be optimized during training, based on geometric intuitions." — §12, p. 371
> 
> The book's clearest statement that two equally valid framings of supervised ML exist: probabilistic (Ch 9, 11) and geometric (Ch 10, 12).

## Connections

### Authors and publisher
- [[MarcDeisenroth]] — Imperial College London / [[AmazonResearch]] (DeepMind Chair of AI at UCL). Lead author.
- [[AAldoFaisal]] — Imperial College London. Co-author.
- [[ChengSoonOng]] — [[CSIROsData61]] + Australian National University. Co-author.
- [[CambridgeUniversityPress]] — publisher.

### To Corpus I — algebrica.org mathematics
- **Ch 2 (Linear Algebra)** is the wiki-level integration point for [[vectors]] / [[matrices]] / [[determinant-of-a-square-matrix]] / [[rank-of-a-matrix]] / [[inverse-matrix]] / [[eigenvalues-and-eigenvectors]] / [[matrix-diagonalization]] / [[linear-combinations]] from algebrica.org. Where algebrica.org gives the *operations*, MML gives the *mappings-and-bases* view that ML uses.
- **Ch 3 (Analytic Geometry)** lifts the [[unit-circle]] / [[pythagorean-theorem]] / [[absolute-value]] block into general [[InnerProduct]] spaces; [[CauchySchwarzInequality]] is the bridge.
- **Ch 4 (Matrix Decomposition)** = the missing capstone of the algebrica.org [[matrices]] block — algebrica.org has [[matrix-diagonalization]] but not Cholesky / SVD / matrix-approximation.
- **Ch 5 (Vector Calculus)** rests on [[remarkable-limits]] / [[indefinite-integrals]] / [[derivatives]] (algebrica.org stubs); generalizes them to multivariate.
- **Ch 6 (Probability)** is downstream of [[sets]] / [[real-numbers]] / [[intervals]] / [[absolute-value]]; introduces $\sigma$-algebras informally.
- **Ch 7 (Optimization)** uses [[polynomials]] for examples ("Abel-Ruffini: in general no algebraic solution for polynomials of degree 5+", p. 227) and connects to algebrica.org's [[roots-of-a-polynomial]] / [[polynomial-equations]].

### To Corpus II — LLM research
- **Ch 5.6 (Backpropagation)** is the mathematical core of training the Transformers in [[1706.03762-attention-is-all-you-need]] / [[1810.04805-bert]] / [[1910.10683-t5]] and every later LLM. Combined with [[ChainRule]] and [[Jacobian]], it explains how gradients flow through arbitrarily deep computational graphs.
- **Ch 7.1 (Gradient Descent / Momentum / SGD)** + **Ch 8.3 (Maximum Likelihood)** = the optimization regime [[2001.08361-scaling-laws]] characterizes empirically. Scaling laws fit a power law to pretraining cross-entropy — the cross-entropy is NLL of a softmax classifier (§9.2 + Ch 11 substrate).
- **Ch 8.6 (Model Selection)** + **Ch 8.2 (ERM)** + the [[NoFreeLunchTheorem]] (§8.2.1) supply the learning-theoretic vocabulary that [[2605.12966-agentic-ai-to-agi]] uses to argue for the [[StructuredRealWorldDistribution]] and the [[AverageTrap]].
- **Ch 10 (PCA)** is the prototype of the *low-dimensional structure* assumption [[2605.12966-agentic-ai-to-agi]] formalizes as a union of low-dim Riemannian manifolds.
- **Ch 6.5 (Gaussian Distribution)** + **Ch 11 (GMM)** are the substrate for Gaussian-noise assumptions throughout Corpus II (e.g., [[BayesianLinearRegression]] / [[RLHF]] reward modeling / [[GaussianProcess]]es).

### To Corpus III — Molnar interpretability
- **Ch 4.5 (SVD)** + **Ch 5 (Vector Calculus)** supply the math behind [[imlbook-shap]] / [[imlbook-shapley]]'s game-theoretic substrate, [[imlbook-ale]] / [[imlbook-pdp]] (which require partial derivatives), and [[imlbook-counterfactual]] (which requires gradient-based perturbations).

### To Corpus IV — McKinney PDA
- **Ch 2 + Ch 3** are the *theory* layer for [[pydata-numpy-basics]] (the [[NDArray]] / [[Broadcasting]] tooling). Where McKinney shows *how to compute* $\mathbf{X}^\top\mathbf{X}$, MML shows *what it geometrically means* (Gram matrix of column inner products).
- **Ch 9 (Linear Regression)** is the theoretical complement to [[pydata-modeling]]'s [[statsmodels]] / [[scikitlearn]] OLS — same closed-form $\boldsymbol\theta = (\mathbf{X}^\top\mathbf{X})^{-1}\mathbf{X}^\top\mathbf{y}$.

### To Corpus V — Made With ML
- **Ch 5 (Vector Calculus) + Ch 7 (Optimization)** is the prerequisite for [[madewithml-foundations-pytorch]]'s [[Autograd]] / [[Backpropagation]] section and [[madewithml-foundations-linear-regression]]'s forward/loss/backward/update training-loop template.
- **Ch 11 (GMM / EM)** is the unsupervised-clustering counterpart to [[madewithml-foundations-utilities]]'s supervised-training scaffolding.

### To Corpus VI — Murphy PML1
- **Identical scope on overlapping chapters** but different framing: where [[pml1-murphy]] is encyclopedic and probabilistic-first, MML is *math-first, four-ML-examples-deep*. Pairing:
  - Murphy Ch 2–3 (Probability) ↔ MML Ch 6.
  - Murphy Ch 7 (Linear Algebra) ↔ MML Ch 2 + Ch 4.
  - Murphy Ch 8 (Optimization) ↔ MML Ch 5 + Ch 7.
  - Murphy Ch 10 (Logistic Regression) — MML omits, only covers linear regression in Ch 9.
  - Murphy Ch 11 (Linear Regression) ↔ MML Ch 9.
  - Murphy Ch 12.1 (Mahalanobis Distance) ↔ MML Ch 3 (Inner Products + SPD matrices).
  - Murphy Ch 20 (PCA) ↔ MML Ch 10.
  - Murphy Ch 17.3 (Kernels) ↔ MML Ch 12.4.
- **Where MML is *more* compact**: explicit *mind maps* opening each chapter (Figs. 2.2, 3.1, 4.1, 5.2, 6.1, 7.1) showing internal concept dependencies — a feature Murphy lacks.
- **Where Murphy is more comprehensive**: deep learning (MML doesn't cover NNs as a topic; only as a backdrop for Ch 5 backprop), generalized linear models, graphical models, nonparametric methods, RL.

## Concepts introduced or canonicalized here

### Linear algebra & geometry (Ch 2–4)
[[VectorSpace]], [[LinearIndependence]], [[Basis]], [[Rank]], [[LinearMapping]], [[AffineSpace]], [[Norm]], [[InnerProduct]], [[CauchySchwarzInequality]], [[OrthogonalProjection]], [[OrthonormalBasis]], [[OrthogonalComplement]], [[Rotation]], [[Determinant]], [[Trace]], [[CharacteristicPolynomial]], [[Eigendecomposition]], [[CholeskyDecomposition]], [[SingularValueDecomposition]], [[MatrixDecomposition]], [[SymmetricPositiveDefiniteMatrix]].

### Calculus (Ch 5)
[[PartialDerivative]], [[Gradient]] (the row-vector convention), [[Jacobian]], [[Hessian]], [[ChainRule]], [[Backpropagation]], [[AutomaticDifferentiation]], [[TaylorSeries]] (multivariate), [[Linearization]].

### Probability (Ch 6)
[[ProbabilitySpace]], [[RandomVariable]], [[ProbabilityMassFunction]], [[ProbabilityDensityFunction]], [[CumulativeDistributionFunction]], [[BayesTheorem]], [[GaussianDistribution]], [[ExponentialFamily]], [[ConjugatePrior]], [[ChangeOfVariables]], [[CoxJaynesTheorem]].

### Optimization (Ch 7)
[[GradientDescent]], [[Momentum]], [[StochasticGradientDescent]], [[ConditionNumber]], [[Preconditioner]], [[LagrangeMultipliers]], [[ConvexOptimization]], [[Duality]], [[LinearProgramming]], [[QuadraticProgramming]].

### ML methodology (Ch 8)
[[EmpiricalRiskMinimization]], [[MaximumLikelihoodEstimation]], [[MAPEstimation]], [[BayesianInference]], [[Hyperparameter]], [[ModelSelection]], [[NestedCrossValidation]], [[Abduction]], [[ProbabilisticGraphicalModel]], [[GeneralizationGap]], [[NoFreeLunchTheorem]].

### Four pillars (Ch 9–12)
[[LinearRegression]], [[FeatureMap]], [[DesignMatrix]], [[BayesianLinearRegression]], [[PrincipalComponentAnalysis]], [[DataCovarianceMatrix]], [[KarhunenLoeveTransform]], [[ProbabilisticPCA]], [[MixtureModel]], [[GaussianMixtureModel]], [[EMAlgorithm]], [[Responsibility]], [[SupportVectorMachine]], [[SeparatingHyperplane]], [[Margin]], [[HardMarginSVM]], [[SoftMarginSVM]], [[KernelTrick]].

## Contradictions

- **Murphy's "self-supervised learning as a recently popular approach"** (Murphy 2022) reads as already dated against Corpus II — pretraining-then-finetune is the default in 2026. MML doesn't take a position on self-supervision at all (the book predates the BERT-era explosion as the conceptual core of ML), making it *consistent with* the assumption-free Murphy reading but *silently behind* Corpus II.
- **MML's Ch 5 row-vector gradient convention** (Eq. 5.40, p. 146): "the row vector in (5.40) is called the gradient of $f$ or the Jacobian." This differs from Murphy / most deep learning texts where the gradient is a column vector. Same math, different transpose conventions — a known source of confusion when reading multiple references.
- **MML defines linear regression as $f(\mathbf{x}) = \boldsymbol\theta^\top\mathbf{x}$ (no bias)** (Eq. 9.4, p. 291) — adding the bias requires the $x^{(0)}=1$ augmentation trick (Example 8.1, p. 259). This contrasts with the [[madewithml-foundations-linear-regression]] convention of carrying $\theta_0$ separately. Both are correct, but cross-referencing the formulas requires noting the augmentation.

## Operational notes

- The book is **freely available** at <https://mml-book.com>; Cambridge UP supports the open distribution.
- The current copy in `raw/` is the **2024-01-15 draft** revision of the **2020 first edition**. Page numbering follows the printed-book numbering, not PDF page count (PDF page = printed page + ~6 due to front matter).
- The book is split into Part I (Foundations, ~225 pages) and Part II (ML problems, ~145 pages). Each chapter opens with an explicit **mind map** of internal concepts and arrows to where they're used downstream.
- Pen-and-paper exercises in Part I; Jupyter notebooks for Part II (linked at mml-book.com).
