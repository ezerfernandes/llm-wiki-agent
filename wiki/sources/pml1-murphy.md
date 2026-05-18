---
title: "Probabilistic Machine Learning: An Introduction"
type: source
tags: [textbook, machine-learning, probabilistic-modeling, foundations, canonical-reference]
date: 2022-03-01
source_file: raw/book1.pdf
---

## Summary

Kevin P. Murphy's *Probabilistic Machine Learning: An Introduction* ([[MITPress]], 2022; CC-BY-NC-ND; 860 pages; third printing January 2025) is the canonical undergraduate-to-early-graduate ML reference framed through the **[[ProbabilisticPerspective]]** — *every* unknown quantity (predictions, parameters, latent factors) is treated as a random variable endowed with a probability distribution. Twenty-three chapters across five parts cover the foundations (probability, statistics, decision theory, information theory, linear algebra, optimization), linear models (LDA, logistic / linear / generalized linear regression), deep neural networks (tabular / image / sequence), nonparametric methods (KNN, kernels, trees + boosting), and unsupervised learning (semi-/self-supervised, dimensionality reduction, clustering, recommender systems, graph embeddings). The book is a sibling to [[scikitlearn]]-style practical references and a prerequisite to its sequel — *Probabilistic Machine Learning: Advanced Topics* ([Mur23], a.k.a. "PML2") — which covers RL, probabilistic graphical models, and generative modeling.

## Key Claims

- **Probabilistic perspective is the unifying lens** (§1.1). Quoting [[ShakirMohamed|Shakir Mohamed]] (DeepMind): "almost all of machine learning can be viewed in probabilistic terms... mastery of probabilistic thinking is essential." Two justifications: (i) optimal **[[DecisionMakingUnderUncertainty|decision-making under uncertainty]]** requires probability; (ii) probability is the lingua franca of every neighboring computational science (control, OR, econometrics, information theory, statistical physics, biostatistics).
- **Three ML regimes, one math** (§1.2–§1.4). Supervised learning fits $p(y|\mathbf{x};\boldsymbol\theta)$; unsupervised learning fits $p(\mathbf{x};\boldsymbol\theta)$; reinforcement learning learns a policy $a=\pi(\mathbf{x})$ from sparse reward. The LeCun "chocolate cake" analogy (§1.4, Fig. 1.11) ranks information density: unsupervised/predictive learning is the cake (millions of bits/sample), supervised is the icing (10–10000 bits/sample), RL is the cherry (a few bits per *some* samples).
- **[[EmpiricalRiskMinimization|Empirical risk minimization]]** (§1.2.1.4): $\hat\boldsymbol\theta=\arg\min_\boldsymbol\theta \frac{1}{N}\sum_n \ell(y_n, f(\mathbf{x}_n;\boldsymbol\theta))$. With **zero-one loss** ERM recovers misclassification rate; with **quadratic loss** it recovers MSE; with **negative log-likelihood** it recovers [[MaximumLikelihoodEstimation|MLE]].
- **NLL = MLE = (often) ERM with a probabilistic loss** (§1.2.1.6). For Gaussian regression, $\text{NLL}(\boldsymbol\theta) = \frac{1}{2\sigma^2}\text{MSE}(\boldsymbol\theta) + \text{const}$, so least squares is MLE under fixed-variance Gaussian noise.
- **Two kinds of uncertainty** (§1.2.1.5). **Epistemic / model uncertainty** (ignorance about the input-output mapping; reducible by more data) vs **aleatoric / data uncertainty** (intrinsic stochasticity; irreducible). The probabilistic framing prevents "false confidence bred from an ignorance of the probabilistic nature of the world" (Kant via Konnikova).
- **Overfitting is the [[GeneralizationGap]]** (§1.2.3): $\mathcal{L}(\boldsymbol\theta;p^*) - \mathcal{L}(\boldsymbol\theta;\mathcal{D}_{\text{train}})$. Approximated by train/test partition; model selection uses a third **validation set**. Test-error vs model-complexity curves are U-shaped (Fig. 1.7d).
- **[[NoFreeLunchTheorem|No Free Lunch theorem]]** (§1.2.4, Wolpert 1996): averaged over *all* problem instances, no learner outperforms any other. Every meaningful generalization result therefore prices in an **inductive bias**. Murphy's prescription: keep many models and selection techniques (cross-validation, Bayesian model selection) in one's toolbox.
- **Probability extends logic** (§2.1.3). Murphy follows the Jaynes/Cox view: probability is the unique calculus of plausible reasoning under degree of belief. Bayes' rule is the inference engine: $p(H|E) = p(E|H)p(H)/p(E)$.
- **Softmax + logits as the universal classification head** (§1.2.1.5, §2.5.2). $\text{softmax}(\mathbf{a})_c = e^{a_c}/\sum_{c'} e^{a_{c'}}$; classifier output is $p(y=c|\mathbf{x};\boldsymbol\theta) = \text{softmax}_c(f(\mathbf{x};\boldsymbol\theta))$. The pre-softmax values $\mathbf{a}$ are **logits**.
- **DNNs as compositions of feature extractors** (§1.2.2.3). $f(\mathbf{x};\boldsymbol\theta) = f_L(f_{L-1}(\cdots f_1(\mathbf{x})\cdots))$ — automatic, parameterized feature learning replacing hand-engineered polynomial expansion. [[CNN]]s for images, [[RNN]]s for sequences (Part III).
- **Reward hacking, alignment, and Intelligence Augmentation** (§1.6.3). Misspecified loss → **reward hacking** → general **alignment problem**. Two paradigms: AGI (autonomous decisions) vs **Intelligence Augmentation / IA** (human-in-the-loop tools — adaptive cruise, autocomplete). Russell's **inverse reinforcement learning** / "assistance game" framing is offered as a constructive remedy.
- **Five-part structure (chapters 1–23 + Appendix A on notation):**
  - **Part I — Foundations** (Ch 2–8): Probability (univariate + multivariate), Statistics, Decision Theory, Information Theory, Linear Algebra, Optimization.
  - **Part II — Linear Models** (Ch 9–12): LDA, Logistic Regression, Linear Regression, Generalized Linear Models.
  - **Part III — Deep Neural Networks** (Ch 13–15): NNs for tabular data, for images ([[CNN]]s), for sequences ([[RNN]]s incl. [[LSTM]] / [[Transformer]] preliminaries).
  - **Part IV — Nonparametric Models** (Ch 16–18): Exemplar-based methods (KNN), kernel methods, Trees / Forests / Bagging / Boosting.
  - **Part V — Beyond Supervised Learning** (Ch 19–23): Learning with fewer labeled examples (semi-/self-/transfer), Dimensionality Reduction (PCA, factor analysis, autoencoders), Clustering, Recommender Systems, Graph Embeddings.

## Key Quotes

> "Almost all of machine learning can be viewed in probabilistic terms, making probabilistic thinking fundamental. ... mastery of probabilistic thinking is essential." — Shakir Mohamed (DeepMind), §1.1

> "[We must avoid] false confidence bred from an ignorance of the probabilistic nature of the world, from a desire to see black and white where we should rightly see gray." — Kant, paraphrased by Konnikova; §1.2.1.5 epigraph

> "All models are wrong, but some models are useful." — George Box, §1.2.4 epigraph

> "If intelligence was a cake, unsupervised learning would be the chocolate sponge, supervised learning would be the icing, and reinforcement learning would be the cherry." — Yann LeCun, NIPS 2016 (quoted §1.4)

> "When we're learning to see, nobody's telling us what the right answers are — we just look. Every so often, your mother says 'that's a dog' ... that's very little information. ... You need more like O(10^5) bits per second. And there's only one place you can get that much information: from the input itself." — Geoffrey Hinton, 1996 (quoted §1.3)

> "[If the statistics field had] incorporated computing methodology from its inception as a fundamental tool ... many of the other data related fields [such as ML] would not have needed to exist — they would have been part of statistics." — Jerry Friedman (quoted §1.6.1)

## Connections

- [[KevinMurphy]] — author; researcher at [[google|Google]] (Doug Eck acknowledged as manager); wrote the predecessor *Machine Learning: A Probabilistic Perspective* (MIT Press, 2012) and the sequel *PML: Advanced Topics* (2023).
- [[MITPress]] — publisher; CC-BY-NC-ND license; *Adaptive Computation and Machine Learning* series (Dietterich ed.; Bishop, Heckerman, Jordan, Kearns assoc. eds.). Other titles in the series include Sutton & Barto's *Reinforcement Learning: An Introduction*, Rasmussen & Williams' *Gaussian Processes for ML*, Koller & Friedman's *Probabilistic Graphical Models*, and Goodfellow/Bengio/Courville's *Deep Learning*.
- [[ProbabilisticPerspective]] — the book's unifying frame.
- [[EmpiricalRiskMinimization]] — §1.2.1.4; the engine of all supervised fitting in the book.
- [[MaximumLikelihoodEstimation]] — §1.2.1.6; ERM with NLL loss; the bridge between probabilistic modeling and optimization.
- [[GeneralizationGap]] — §1.2.3; defines overfitting operationally.
- [[NoFreeLunchTheorem]] — §1.2.4; the inductive-bias entry point.
- [[ReinforcementLearning]] — §1.4; treated lightly here, in depth in the sequel.
- [[CurseOfDimensionality]] — appears throughout high-dimensional discussions; load-bearing in Ch 16 (exemplar methods) and Ch 20 (dimensionality reduction).
- [[Transformer]] — Ch 15 (NNs for sequences); the book predates the post-2022 LLM scaleup but covers self-attention and sequence-to-sequence framings.
- [[CNN]] — Ch 14 (NNs for images).
- [[LSTM]] — Ch 15 (NNs for sequences); the recurrent baseline the [[Transformer]] displaced (see [[1409.3215-seq2seq]] for the historical seq2seq predecessor).
- [[MaskedLanguageModel]] / [[selfattention]] / [[multiheadattention]] — covered in Ch 15; canonical references for these are [[1810.04805-bert]] and [[1706.03762-attention-is-all-you-need]].
- [[scikitlearn]] — the de facto Python implementation of the linear-models / nonparametric chapters; the book's companion Python notebooks (`probml.github.io/book1`) use it and JAX.
- [[pandas]] / [[NumPy]] — operational substrate; cf. [[pydata-numpy-basics]], [[pydata-modeling]] for the McKinney-side treatment of the same APIs.
- [[scikitlearn]] estimator API + the Iris dataset (§1.2.1.1) are the same teaching scaffold used in [[imlbook-data]] / [[imlbook-tree]] / [[imlbook-shap]] (Molnar's *Interpretable ML*).
- [[InterpretableMachineLearning]] / [[imlbook-overview]] — Murphy's tree / kernel / linear-model chapters give the *fitted* models that Corpus III's interpretability methods analyze.

## Cross-corpus role

This is the **foundations-layer textbook** the wiki has been missing. Where Corpus II (2026 LLM research) tacitly assumes its readers know Bayes' rule, NLL/MLE equivalence, GLMs, SGD, and PCA, this book is the canonical reference for those prerequisites. Concretely:

- The [[ScalingLaws|scaling-laws]] curve (Kaplan et al., [[2001.08361-scaling-laws]]) is a power-law fit to pretraining cross-entropy — Murphy Ch 6 (Information Theory) is the cross-entropy reference; Ch 8 (Optimization) covers the SGD / Adam / momentum machinery the scaling experiments use.
- The **[[ProbabilisticPerspective|probabilistic framing of LLM outputs]]** $p(\mathbf{x}_t | \mathbf{x}_{<t})$ in [[1706.03762-attention-is-all-you-need]] and [[1810.04805-bert]] is exactly the conditional density Murphy formalizes in §1.2.1.5.
- The **[[AverageTrap]] / [[CompositionalCapacity]]** analysis in [[2605.12966-agentic-ai-to-agi]] is built on quadratic-loss / weighted-average decompositions whose linear-algebraic and decision-theoretic primitives are Murphy Ch 5 + Ch 7.
- The **[[NoFreeLunchTheorem]]** that [[2605.12966-agentic-ai-to-agi]] uses as its argument's entry point is §1.2.4 here.
- Corpus III ([[imlbook-overview|Molnar IML]]) interprets fitted models; **Murphy provides the fitted models**. Logistic regression (Ch 10) → [[imlbook-logistic]]; decision trees (Ch 18) → [[imlbook-tree]]; kernels (Ch 17) → [[imlbook-shap]]'s game-theoretic substrate; linear models (Ch 11) → [[imlbook-limo]]; CNN feature visualization (Ch 14) → [[imlbook-cnn-features]] / [[imlbook-pixel-attribution]].
- Corpus IV ([[pydata-modeling|McKinney PDA]]) is the *tooling* layer (pandas/numpy/sklearn API). Murphy is the *theory* layer for the same API surface.

## Contradictions

- **Pure-scaling vs. structural-bottleneck readings of AGI.** Murphy's Ch 1 framing ("In this book, we take one particular path through this interconnected landscape, using probability theory as our unifying lens" — §1.6.2) and the LeCun-cake hierarchy (§1.4) is *agnostic* on the AGI path question. By contrast, [[2605.12966-agentic-ai-to-agi]] (Liao et al., ICML 2026) argues monolithic scaling is *structurally* bottlenecked by the [[AverageTrap]] and the [[CurseOfDimensionality]] applied to ambient $D$. The two are compatible (Murphy doesn't take a position) but Murphy's choice to defer RL and generative modeling to the sequel and to organize Part III around monolithic-DNN supervised learning could read as implicit acceptance of the scaling story Liao et al. contest.
- **MAR assumption** (§1.5.5). Murphy declares the book "will always make the MAR assumption" for missing data. This is standard but bites in causal-inference / NMAR settings that some of Corpus II's RLHF / preference-data papers tacitly inhabit.
- **"Reward hacking → IRL/assistance games"** (§1.6.3) reads cleanly in 2022 but is somewhat eclipsed by 2026's empirical [[BystanderEffect|bystander-effect]] / [[AlignmentHallucination]] findings ([[2605.10698-bystander-effect-mas]]) showing that even sound external critics admit *anticipatory* alignment failures — the [[SovereigntyGap]] regime is invisible to the IRL formalization Murphy cites.
- **Self-supervised learning as a "recently popular approach"** (§1.3.3) is dated by the post-2022 LLM scaleup; pretraining-then-finetuning is now the default not the curiosity.

## Provenance and printings

- First printing March 2022; second April 2023; third January 2025 (changelog: github.com/probml/pml-book/issues).
- Online PDF dated "April 18, 2025" (verbatim from page footers).
- Companion notebooks: `probml.github.io/book1` (JAX + TF).
- License: Creative Commons Attribution-NonCommercial-NoDerivatives (CC-BY-NC-ND).
- Cover illustration: a hand-written digit being classified by a CNN — the canonical $p(y|\mathbf{x})$ figure.

## Dedication

"This book is dedicated to my mother, Brigid Murphy, who introduced me to the joy of learning and teaching."
