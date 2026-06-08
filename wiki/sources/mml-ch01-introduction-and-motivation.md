---
title: "MML Ch 1 — Introduction and Motivation"
type: source
tags: [textbook, mathematics, foundations, machine-learning, motivation, mml]
date: 2020-01-01
source_file: raw/mml-book.pdf
---

## Summary

Chapter 1 of *[[mml-book|Mathematics for Machine Learning]]* (book pages 11–16) is a short, motivational opening that frames the entire book. It establishes the three concepts the authors place "at the core of machine learning" — **data**, a **model**, and **learning** — and argues that, even though usable [[MachineLearning|machine-learning]] software is now readily available, the **mathematical foundations** matter because they expose the design decisions, assumptions, and limitations of the methods. It then introduces the book's two-part structure (Part I: mathematical foundations; Part II: four central ML problems), the **[[FourPillarsOfMachineLearning|four pillars × six foundations]]** organizing metaphor of Figure 1.1, and two complementary reading strategies (bottom-up vs. top-down). The chapter is written by [[MarcDeisenroth]], [[AAldoFaisal]] & [[ChengSoonOng]] and published by [[CambridgeUniversityPress]].

The chapter has three sections: **§1.1 Finding Words for Intuitions** (the deliberate ambiguity of ML vocabulary, and the working definitions of data / model / learning the book will use), **§1.2 Two Ways to Read This Book** (bottom-up vs. top-down; the Part I / Part II split; a chapter-by-chapter tour of both parts), and **§1.3 Exercises and Feedback** (pen-and-paper exercises in Part I, Jupyter-notebook tutorials in Part II, open access via mml-book.com).

## Key Claims

### Opening framing (§1, p. 11)

- **Machine learning is about designing algorithms that automatically extract valuable information from data**, with the emphasis on *"automatic"* — i.e., ML is concerned with general-purpose methodologies that can be applied to many datasets while still producing something meaningful (p. 11).
- **Three concepts are at the core of machine learning: data, a model, and learning** (p. 11). This trichotomy is the spine of the whole book and is revisited mathematically in Chapter 8.
- **Data is at the core because machine learning is inherently data driven** (margin note "data", p. 11). The goal of ML is to design general-purpose methodologies to extract valuable patterns from data, *ideally without much domain-specific expertise*. Worked example: given a large corpus of documents (e.g., books in many libraries), ML methods can automatically find shared relevant topics — citing Hoffman et al. (2010) (latent Dirichlet allocation / online variational inference).
- **A model is typically related to the process that generates data, similar to the dataset we are given** (margin note "model", p. 11). Example: in a [[Regression|regression]] setting the model describes a *function* that maps inputs to real-valued outputs. The authors paraphrase Mitchell (1997): *a model is said to learn from data if its performance on a given task improves after the data is taken into account.* The goal is to find good models that **[[Generalization|generalize]]** well to yet-unseen data, which "we may care about in the future."
- **Learning can be understood as a way to automatically find patterns and structure in data by optimizing the parameters of the model** (margin note "learning", p. 11). This binds learning to [[ContinuousOptimization|optimization]] and to model [[Parameter|parameters]].
- **Mathematical foundations matter even though ML software is readily available** (p. 11). Understanding the foundations can (1) facilitate creating new ML solutions, (2) help understand and debug existing approaches, and (3) reveal the inherent assumptions and limitations of the methodologies in use.

### §1.1 Finding Words for Intuitions (pp. 12–13)

- **ML concepts and words are "slippery"**: a single component of an ML system can be abstracted to different mathematical concepts, so the same word can carry multiple meanings (p. 12).
- **The word "algorithm" is used in (at least) two distinct senses** (p. 12) — a central disambiguation introduced here:
  1. **A [[Predictor|predictor]]**: "machine learning algorithm" meaning a *system that makes predictions based on input data*.
  2. **A training procedure**: the same phrase meaning a system that *adapts some internal parameters of the predictor* so it performs well on future unseen input data. This adaptation is called **[[Training|training]]** a system.
- **The book will not resolve this ambiguity** but flags it up front and attempts to make context clear enough to reduce it (p. 12).
- **Part I's job is to introduce the mathematical concepts/foundations needed to talk about the three components** (data, models, learning), which are briefly outlined in Ch 1 and revisited in Chapter 8 once the math is in place (p. 12).
- **Data as vectors** (margin note "data as vectors", p. 12): although not all data is numerical, the book assumes data has *already been appropriately converted into a numerical representation* suitable for reading into a computer program, so **data is thought of as vectors**. The authors note three ways to think about a vector — illustrating how subtle even basic words are:
  - a vector as an **array of numbers** (a computer-science view);
  - a vector as an **arrow with direction and magnitude** (a physics view);
  - a vector as an **object that obeys addition and scaling** (a mathematical view).
- **A model is typically used to describe a process for generating data, similar to the dataset at hand** (margin note "model", p. 12). Good models can therefore be thought of as *simplified versions* of the real (unknown) data-generating process, capturing the aspects relevant for modeling the data and extracting hidden patterns. A good model can then be used to **predict what would happen in the real world without performing real-world experiments**.
- **Learning is "the crux of the matter"** (margin note "learning", p. 12). Given a dataset and a suitable model, **training the model means using the available data to optimize the parameters of the model with respect to a utility function that evaluates how well the model predicts the training data**. Most training methods can be thought of as **hill-climbing to reach the peak**, where the peak corresponds to a maximum of some desired performance measure (pp. 12–13).
- **Generalization, not memorization, is the goal** (p. 13): in practice we want the model to perform well on *unseen* data. Performing well on training data alone may only mean we found a good way to *memorize* the data, which may not generalize. Hence "we often need to expose our machine learning system to situations that it has not encountered before."
- **Three-bullet summary of the main concepts the book covers** (p. 13):
  1. We **represent data as vectors**.
  2. We **choose an appropriate model**, either using the **probabilistic** view or the **optimization** view.
  3. We **learn from available data using numerical optimization methods**, with the aim that the model performs well on data not used for training.

### §1.2 Two Ways to Read This Book (pp. 13–16)

- **Two strategies for understanding the mathematics for ML** (p. 13):
  - **Bottom-up**: build concepts from foundational to advanced (the preferred approach in technical fields like mathematics). Advantage: the reader can always rely on previously learned concepts. Disadvantage: many foundational concepts aren't interesting by themselves, so the lack of motivation means most foundational definitions are quickly forgotten.
  - **Top-down**: drill down from practical needs to basic requirements. Advantage: this goal-driven approach means readers always know *why* they need a particular concept, and there is a clear path of required knowledge. Disadvantage: the knowledge is built on potentially shaky foundations, and readers must remember words they have no real way of understanding.
- **The book is deliberately modular** to support *both* reading orders (p. 13): foundational (mathematical) concepts are separated from applications. The book is split into **Part I** (mathematical foundations) and **Part II** (applies Part I to fundamental ML problems = the four pillars of Figure 1.1).
- **Chapter coupling** (pp. 13–14): chapters in Part I mostly build on previous ones, but a chapter can be skipped and worked backward if needed; chapters in Part II are only loosely coupled and can be read in any order. There are many forward/backward pointers between the two parts linking math concepts to ML algorithms.
- **"Of course there are more than two ways to read this book"** (p. 14): most readers use a *combination* of top-down and bottom-up — building basic math skills before attempting more complex concepts, but also choosing topics by ML application.
- **Figure 1.1 — the foundations and four pillars of machine learning** (p. 14): a temple/Parthenon diagram where a pediment labeled **Machine Learning** rests on **four pillars** (left to right: **Regression**, **Dimensionality Reduction**, **Density Estimation**, **Classification**) standing on a two-tier foundation of **six mathematical disciplines**:
  - Upper foundation row: **Vector Calculus**, **Probability & Distributions**, **Optimization**.
  - Lower foundation row: **Linear Algebra**, **Analytic Geometry**, **Matrix Decomposition**.

- **Part I Is about Mathematics** (pp. 14–15) — chapter-by-chapter map of the six foundations:
  - **Ch 2 — [[LinearAlgebra|Linear algebra]]**: we represent numerical data as vectors and a table of such data as a matrix; the study of vectors and matrices is linear algebra. Collecting vectors into a matrix is also covered here.
  - **Ch 3 — [[AnalyticGeometry|Analytic geometry]]**: given two vectors representing two real-world objects, we want statements about their *similarity* (similar vectors should be predicted to have similar outputs by the predictor). Formalizing similarity requires operations that take two vectors and return a numerical similarity value — the construction of similarity and distances is central to analytic geometry.
  - **Ch 4 — [[MatrixDecomposition|Matrix decomposition]]**: fundamental concepts about matrices and their decompositions; some matrix operations are extremely useful in ML and enable intuitive interpretation of the data and more efficient learning.
  - **Noise and uncertainty motivate probability** (p. 14): we often consider data to be *noisy observations* of some true underlying signal, and hope ML can identify the signal from the noise. This requires a language for quantifying "noise," and predictors that can express *uncertainty* (e.g., confidence about a prediction at a particular test point).
  - **Ch 6 — [[ProbabilityAndDistributions|Probability theory]]** (margin note "probability theory", p. 15): quantification of uncertainty is the realm of probability theory.
  - **Ch 5 — [[VectorCalculus|Vector calculus]]** (margin note, p. 15): many optimization techniques require the concept of a **gradient**, which tells us the direction in which to search for a solution; Ch 5 details gradients.
  - **Ch 7 — [[ContinuousOptimization|Optimization]]** (margin note, p. 15): uses the gradients from Ch 5 to find maxima/minima of functions; to train ML models we typically find parameters that maximize some performance measure.

- **Part II Is about Machine Learning** (pp. 15–16) — chapter-by-chapter map of the four pillars (broadly ordered by ascending difficulty):
  - **Ch 8**: restates the three components of ML — *data, models, and parameter estimation* — in a mathematical fashion, and provides guidelines for building experimental set-ups that guard against overly optimistic evaluations of ML systems. Reiterates that the goal is a predictor that performs well on *unseen* data.
  - **Ch 9 — [[LinearRegression|Linear regression]]**: find functions that map inputs $\boldsymbol{x} \in \mathbb{R}^D$ to corresponding observed function values $y \in \mathbb{R}$, interpreted as labels. Covers classical model fitting (parameter estimation) via [[MaximumLikelihoodEstimation|maximum likelihood]], and [[BayesianLinearRegression|Bayesian linear regression]] where parameters are *integrated out* instead of optimized.
  - **Ch 10 — [[DimensionalityReduction|Dimensionality reduction]]** (the second pillar), using [[PrincipalComponentAnalysis|principal component analysis]]: find a compact, lower-dimensional representation of high-dimensional data $\boldsymbol{x} \in \mathbb{R}^D$ that is often easier to analyze. Unlike regression, dimensionality reduction is *only* concerned with modeling the data — there are **no labels** associated with a data point $\boldsymbol{x}$.
  - **Ch 11 — Density estimation** (the third pillar): find a probability distribution that describes a given dataset; the book focuses on [[GaussianMixtureModel|Gaussian mixture models]] and an iterative scheme to find the parameters. As in dimensionality reduction there are *no labels*; however, unlike dimensionality reduction we do **not** seek a low-dimensional representation — instead we want a *density model* that describes the data.
  - **Ch 12 — [[Classification|Classification]]** (the fourth pillar), in the context of [[SupportVectorMachine|support vector machines]]. Similar to regression (Ch 9) we have inputs $\boldsymbol{x}$ and corresponding labels $y$; but unlike regression where labels are real-valued, in classification the labels are **integers**, which requires special care.

### §1.3 Exercises and Feedback (p. 16)

- **Part I provides pen-and-paper exercises**; **Part II provides programming tutorials (Jupyter notebooks)** to explore properties of the ML algorithms discussed (p. 16).
- **The authors appreciate that [[CambridgeUniversityPress]] strongly supports their aim to democratize education and learning** by making the book freely available for download at <https://mml-book.com> (p. 16).
- **mml-book.com hosts tutorials, errata, and additional materials**; mistakes can be reported and feedback provided via the same URL (p. 16).

## Key Quotes

> "Machine learning is about designing algorithms that automatically extract valuable information from data. The emphasis here is on 'automatic', i.e., machine learning is concerned about general-purpose methodologies that can be applied to many datasets, while producing something that is meaningful." — §1, p. 11 (opening sentence of the book body)

> "There are three concepts that are at the core of machine learning: data, a model, and learning." — §1, p. 11

> "Learning can be understood as a way to automatically find patterns and structure in data by optimizing the parameters of the model." — §1, p. 11 (working definition of learning)

> "While machine learning has seen many success stories, and software is readily available to design and train rich and flexible machine learning systems, we believe that the mathematical foundations of machine learning are important in order to understand fundamental principles upon which more complicated machine learning systems are built." — §1, p. 11 (the book's mission statement)

> "In the first sense, we use the phrase 'machine learning algorithm' to mean a system that makes predictions based on input data. We refer to these algorithms as predictors. In the second sense, we use the exact same phrase 'machine learning algorithm' to mean a system that adapts some internal parameters of the predictor so that it performs well on future unseen input data. Here we refer to this adaptation as training a system." — §1.1, p. 12 (the predictor-vs-training disambiguation)

> "there are (at least) three different ways to think about vectors: a vector as an array of numbers (a computer science view), a vector as an arrow with a direction and magnitude (a physics view), and a vector as an object that obeys addition and scaling (a mathematical view)." — §1.1, p. 12

> "Training the model means to use the data available to optimize some parameters of the model with respect to a utility function that evaluates how well the model predicts the training data. Most training methods can be thought of as an approach analogous to climbing a hill to reach its peak. In this analogy, the peak of the hill corresponds to a maximum of some desired performance measure." — §1.1, pp. 12–13 (the hill-climbing metaphor for training)

> "Performing well on data that we have already seen (training data) may only mean that we found a good way to memorize the data. However, this may not generalize well to unseen data, and, in practical applications, we often need to expose our machine learning system to situations that it has not encountered before." — §1.1, p. 13

> "Bottom-up: Building up the concepts from foundational to more advanced. … Unfortunately, for a practitioner many of the foundational concepts are not particularly interesting by themselves, and the lack of motivation means that most foundational definitions are quickly forgotten." — §1.2, p. 13

> "Top-down: Drilling down from practical needs to more basic requirements. … The downside of this strategy is that the knowledge is built on potentially shaky foundations, and the readers have to remember a set of words that they do not have any way of understanding." — §1.2, p. 13

> "Of course there are more than two ways to read this book. Most readers learn using a combination of top-down and bottom-up approaches…" — §1.2, p. 14

> "We appreciate that Cambridge University Press strongly supports our aim to democratize education and learning by making this book freely available for download at https://mml-book.com" — §1.3, p. 16

## Connections

- [[mml-book]] — this is the per-chapter deep dive of Chapter 1 of the umbrella book page.
- [[MarcDeisenroth]], [[AAldoFaisal]], [[ChengSoonOng]] — the three authors.
- [[CambridgeUniversityPress]] — publisher; explicitly credited for supporting open distribution.
- [[MachineLearning]] — Ch 1 gives the book's canonical definition (automatic extraction of valuable information from data) and the data/model/learning trichotomy.
- [[Predictor]] — Ch 1 introduces the predictor sense of "ML algorithm" (a system that makes predictions).
- [[Training]] — Ch 1 introduces the training sense (a system that adapts the predictor's parameters) and the hill-climbing metaphor.
- [[Generalization]] — Ch 1 states the goal of learning is to perform well on unseen data, not to memorize the training set.
- [[FourPillarsOfMachineLearning]] — Figure 1.1's organizing metaphor (four pillars on six foundations).
- [[Parameter]] (model parameters) / [[ContinuousOptimization]] — learning = optimizing model parameters against a utility function.
- [[VectorSpace]] / [[LinearAlgebra]] — data is represented as vectors; the three views of a vector are introduced here.
- [[Regression]], [[DimensionalityReduction]], [[PrincipalComponentAnalysis]], [[GaussianMixtureModel]], [[Classification]], [[SupportVectorMachine]] — the four-pillar applications previewed in §1.2.
- [[AnalyticGeometry]], [[MatrixDecomposition]], [[VectorCalculus]], [[ProbabilityAndDistributions]] — the remaining foundations previewed in §1.2.
- [[LinearRegression]] / [[BayesianLinearRegression]] / [[MaximumLikelihoodEstimation]] — Ch 9 preview (parameter estimation vs. integrating parameters out).

## Concepts introduced or canonicalized here

- **Data / model / learning trichotomy** — the book's organizing definition of ML ([[MachineLearning]]).
- **Predictor vs. training** — the two senses of "machine learning algorithm" ([[Predictor]], [[Training]]).
- **Model as a simplified data-generating process** — probabilistic view vs. function/optimization view ([[MachineLearning]], previews [[BayesianLinearRegression]]).
- **Data as vectors** + the three views of a vector (CS / physics / mathematical) ([[VectorSpace]], [[LinearAlgebra]]).
- **Learning as parameter optimization against a utility function** + hill-climbing metaphor ([[Training]], [[ContinuousOptimization]]).
- **Generalization to unseen data as the goal** ([[Generalization]]).
- **Four pillars × six foundations** (Figure 1.1) ([[FourPillarsOfMachineLearning]]).
- **Bottom-up vs. top-down reading strategies** (a pedagogical framing, captured in [[FourPillarsOfMachineLearning]] and this source page rather than its own concept page).

## Contradictions / notational quirks

- **"Utility function" terminology** (§1.1, pp. 12–13): Ch 1 frames training as *maximizing* a *utility function* / performance measure (hill-climbing to a peak). Most of the rest of the wiki — and indeed MML's own later chapters — frames training as *minimizing* a **loss / cost** function (e.g., [[Generalization]]'s $R_\text{emp}$, [[EmpiricalRiskMinimization]]). These are the same idea up to a sign (maximize utility ≡ minimize negative-loss); the Ch 1 "hill-climbing to a maximum" wording is a motivational simplification, not a contradiction.
- **Density estimation has no standalone wiki concept page yet** — only [[KernelDensityEstimation]] and [[GaussianMixtureModel]] exist. Ch 11 (the density-estimation pillar) is the proper home for that page; Ch 1 only previews it. Not created here to avoid a thin stub.
- **No contradictions** with the existing [[mml-book]] umbrella page or other corpora — Ch 1 is purely the motivational front matter that the umbrella page already summarizes at a higher level. This page expands that summary with section/page-level granularity.

## Forward references (resolved in later chapters)

- The three components are *restated mathematically* in **Chapter 8** (§1.1, p. 12; §1.2 Ch 8 entry).
- Gradients (Ch 5) feed optimization (Ch 7); probability/uncertainty (Ch 6) underpins the probabilistic model view.
- The four pillars are each developed in Chapters 9–12.
