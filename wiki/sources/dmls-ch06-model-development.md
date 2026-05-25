---
title: "Designing ML Systems — Ch 6: Model Development and Offline Evaluation"
type: source
tags: [book, dmls, designing-ml-systems, model-development, offline-evaluation, ensembles, distributed-training, automl, calibration, slice-evaluation, oreilly]
date: 2022-05-17
sources: []
source_file: raw/books/designing-ml-systems/dmls-ch06-model-development.txt
last_updated: 2026-05-23
---

# Designing ML Systems Ch 6 — Model Development and Offline Evaluation

## Summary

Chapter 6 of [[ChipHuyen|Chip Huyen]]'s *Designing Machine Learning Systems* ([[OReilly|O'Reilly]], 2022) is the **ML-algorithm chapter** of the book — the moment when data engineering (Ch 4) and feature engineering (Ch 5) become a model whose predictions you can evaluate. The chapter is organized in two halves: (1) **model development and training** — how to select an ML model, how to build [[ModelEnsemble|ensembles]] ([[Bagging|bagging]], [[Boosting|boosting]], stacking), [[ExperimentTracking|experiment tracking]] and [[Versioning|versioning]], [[DistributedTraining|distributed training]] ([[DataParallelism|data parallelism]], [[ModelParallelism|model parallelism]], [[PipelineParallelism|pipeline parallelism]]), and [[AutoML]] (hyperparameter tuning, [[NeuralArchitectureSearch|neural architecture search]], learned optimizers); and (2) **offline evaluation** — baselines, perturbation tests, invariance tests, directional expectation tests, [[ModelCalibration|model calibration]], confidence measurement, and [[DataSlicing|slice-based evaluation]] including [[SimpsonsParadox|Simpson's paradox]].

The chapter's thesis is that picking a model is **not** about chasing state-of-the-art benchmarks; it is about navigating a multi-axis trade-off (accuracy vs latency, compute, interpretability, data needs, future-improvement headroom) under hard practical constraints, then validating the result with evaluation methods that go beyond a single aggregate metric. Huyen offers six tips for model selection (avoid the SOTA trap, start with simplest, watch for human biases, evaluate now-vs-later, evaluate trade-offs, understand model assumptions), names four phases of ML adoption (before-ML → simplest ML → optimized simple ML → complex models), and argues that **evaluation metrics are meaningless without baselines** — naming five baseline classes (random, simple heuristic, zero rule, human, existing solutions). The offline-evaluation half then introduces five complementary evaluation techniques that probe robustness, fairness, calibration, per-sample confidence, and subgroup performance — designed to catch failures that aggregate accuracy hides.

The chapter also embeds two extended sidebars: **Debugging ML Models** (why ML debugging is uniquely painful — silent failures, slow validation, cross-functional complexity — with three debugging techniques: start-simple-and-grow, overfit a single batch, set a random seed) and **Four Phases of ML Model Development** (each phase's solution becomes the baseline for the next).

## Key Claims

- **Deep learning is not replacing classical ML.** Many recommender systems still use [[CollaborativeFiltering|collaborative filtering]] and [[MatrixFactorization|matrix factorization]]; tree-based models including gradient-boosted trees still power latency-sensitive classification. Neural and classical models often coexist in ensembles or pipelines (e.g., a pretrained [[bert|BERT]] or [[GPT3|GPT-3]] generates embeddings that feed a [[LogisticRegression|logistic regression]] head).
- **Avoid the state-of-the-art trap.** A model being SOTA on a static academic dataset means it beats existing models on that dataset — not that it will be fast, cheap, or even most accurate on *your* data. *"If there's a solution that can solve your problem that is much cheaper and simpler than state-of-the-art models, use the simpler solution."*
- **Start with the simplest model** for three reasons: (1) early deploy validates that the training pipeline matches the prediction pipeline; (2) simple models are easier to debug and to incrementally extend; (3) they form the **baseline** for more complex follow-ons. *"Simplest models are not always the same as models with the least effort"* — a pretrained BERT via [[HuggingFace|Hugging Face]] Transformers is complex but low-effort to start with.
- **Human bias contaminates model comparisons.** If an engineer runs 100 experiments on architecture A and only 5 on architecture B, A will appear to win. Comparing architectures requires comparable experimental budgets per architecture, and any "X beats Y" claim is context-dependent on task, data, hyperparameters, and feature set.
- **Best model now is not best model two months from now.** A learning curve (performance vs training-set size) is a cheap diagnostic for whether more data will help. Huyen recounts a case where a [[CollaborativeFiltering|collaborative filtering]] recommender beat a small neural net offline, but the neural net — trained online with each incoming example — overtook it in two weeks of production.
- **Every model carries assumptions** — *"all models are wrong, but some are useful"* (George Box, 1976). Examples: the **prediction assumption** (Y is predictable from X); **IID** (neural networks assume independent, identically distributed examples); **smoothness** (similar inputs → similar outputs); **tractability** (generative models assume P(Z\|X) is tractable); **boundaries** (linear classifiers assume linear decision boundaries); **conditional independence** ([[NaiveBayes|naive Bayes]]); **normality** (many statistical methods).
- **Ensembles consistently boost performance** — *20 of 22 winning Kaggle solutions in 2021 were ensembles*; as of January 2022, the **top 20 SQuAD 2.0 leaderboard entries were all ensembles**. Yet ensembles are unfavored in production because they are harder to deploy and maintain; they remain common in high-stakes tasks (e.g., ad click-through-rate prediction) where small gains move large dollars.
- **Ensembles work best when base learners are uncorrelated.** A worked example: three independent 70%-accurate classifiers voting by majority reach 78.4% (0.343 + 0.441). Perfectly correlated learners give no gain. Hence the heuristic of mixing very different model families (e.g., a [[transformer|transformer]] + an [[RNN]] + a gradient-boosted tree).
- **Three ensembling families**: (1) **[[Bagging|bagging]]** — bootstrap aggregating; sample-with-replacement to build N bootstraps, train one model per bootstrap, vote/average. Reduces variance, helps with overfitting, helps with class imbalance. [[RandomForests|Random forests]] = bagging + per-tree feature subsampling. Helps unstable methods (NN, trees, subset selection in LR); can *degrade* stable methods like [[KNearestNeighbors|k-NN]] (Breiman 1996). (2) **[[Boosting|boosting]]** — iteratively reweight samples toward misclassified ones; combine weak learners into a strong learner. **GBM** generalizes by allowing arbitrary differentiable loss; **XGBoost** was the long-time Kaggle champion (used for Higgs boson discovery); **LightGBM** is now often preferred for parallel learning on large datasets. (3) **Stacking** — train base learners, then train a meta-learner (heuristic vote, average, or another model like logistic/linear regression) that combines their outputs.
- **Experiment tracking and versioning are inseparable.** Many tools that began as one have grown into both — [[MLflow]] and [[WeightsAndBiases|Weights & Biases]] added versioning; [[DVC]] added experiment tracking. Track at minimum: loss curves per split, performance metrics (accuracy, F1, perplexity), sample/prediction/label logs, training speed (steps/sec or tokens/sec), system metrics (memory, CPU/GPU utilization), and any parameter/hyperparameter that can shift performance (learning rate schedule, gradient norms — globally and per-layer, weight norms when using weight decay).
- **Data versioning is "like flossing — everyone agrees it's good, few do it."** It is hard because: data is too large for line-by-line diffs and full duplication; what constitutes a diff is unclear ([[DVC]] as of 2021 registers a diff only when checksums of the directory change or files are added/removed); merge conflicts have no model-coherent resolution; and regulations like GDPR may legally forbid keeping older versions if users request deletion. Aggressive tracking improves [[Reproducibility|reproducibility]] but cannot guarantee it — nondeterminism in CUDA atomic operations and floating-point rounding can still vary between runs.
- **Debugging ML models is uniquely painful**: (1) **silent failures** — the code compiles, loss decreases, predictions are made and are wrong, and nobody notices; (2) **slow validation** — fixing a bug requires retraining and waiting hours for convergence to know if the fix worked; (3) **cross-functional complexity** — data, labels, features, algorithms, code, and infrastructure are owned by different teams. Three debugging recipes (echoing [[AndrejKarpathy|Andrej Karpathy]]'s *"A Recipe for Training Neural Networks"*): **start simple and gradually add components**, **overfit a single batch** (10 images to 100% acc, or 100 sentence pairs to ~100 BLEU), and **set a random seed** to make runs comparable and bugs reproducible.
- **Distributed training: three parallelism axes.** **Data parallelism** splits data across machines, accumulates gradients — but suffers from stragglers under synchronous SGD and from gradient staleness under asynchronous SGD (Hogwild! showed staleness is mild when gradient updates are sparse, which they typically are for large models). Scaling to many machines also balloons effective batch size (OpenAI's GPT-3 175B used a **3.2M batch size** in 2020); increasing the learning rate is the first lever but has diminishing returns. **Model parallelism** splits the model itself across machines but is "misleadingly named" — sequential layer dependencies often serialize execution. **Pipeline parallelism** (e.g., GPipe) breaks each machine's work into micro-batches so machines can process different micro-batches simultaneously. The three approaches are not mutually exclusive.
- **AutoML has soft and hard flavors.** **Soft AutoML = [[HyperparameterTuning|hyperparameter tuning]]** — popular methods are [[RandomSearch|random search]], [[GridSearch|grid search]], and [[BayesianOptimization|Bayesian optimization]]; tools include auto-sklearn, Keras Tuner, [[RayTune|Ray Tune]]. The most common technique remains "graduate student descent." Melis et al. 2018 showed *weaker models with well-tuned hyperparameters can outperform stronger fancier models*. **Never tune hyperparameters on the test split.** **Hard AutoML = [[NeuralArchitectureSearch|neural architecture search]] and learned optimizers** — NAS has three components (search space, performance estimation strategy, search strategy — RL or evolution); learned optimizers replace the gradient update rule with a neural network, can be meta-trained across thousands of tasks (Metz et al.), and can generalize to new datasets and architectures. EfficientNets (Google) achieved SOTA accuracy with up to 10× better efficiency than hand-designed nets.
- **Four phases of ML model development**: (1) before-ML — start with heuristics; *"if you think ML will give a 100% boost, a heuristic will get you 50% there"* (Zinkevich, *Rules of ML*). Facebook newsfeed shipped in 2006 with reverse-chronological order; ranking arrived in 2011. (2) Simplest ML — [[LogisticRegression|logistic regression]], gradient-boosted trees, [[KNearestNeighbors|k-NN]]. (3) Optimize the simple model — feature engineering, hyperparameter search, more data, ensembles. (4) Complex models — and now also plan for retraining cadence as the model decays in production.
- **Evaluation metrics are meaningless without baselines.** Five baselines: **random** (uniform, or label-distribution-matched — on a 90/10 imbalanced binary task, label-matched random gets 0.82 accuracy and 0.10 F1), **simple heuristic** (e.g., reverse-chronological newsfeed), **zero-rule** (always predict the most common class), **human** (essential for self-driving, medical, and any system that must replace expert judgment), and **existing solutions** (the if/else business rules or third-party tools you would replace). *"A good system isn't necessarily useful, and a bad system isn't necessarily useless"* — an ML system can be inferior in raw accuracy yet useful if it is cheaper or simpler than the existing solution.
- **Perturbation tests** — small noise injected into the test split (background sound, clipping, lighting changes, typos like *"loooooong"*) reveals robustness gaps; the model best on clean data may not be the model best on the noisy data your users will actually produce. Sensitivity to input perturbations also signals susceptibility to adversarial attack.
- **Invariance tests** — *"certain changes to the inputs shouldn't lead to changes in the output."* The 2008–2015 Berkeley mortgage study found 1.3M creditworthy Black and Latino applicants were rejected; removing race-identifying features led to acceptance. The remedy: exclude sensitive attributes from training features in the first place, and probe with hold-everything-else-constant perturbations.
- **Directional expectation tests** — *"certain changes to the inputs should cause predictable changes in outputs."* A housing-price model that *decreases* its prediction when lot size grows or *increases* it when square footage shrinks is learning the wrong thing.
- **[[ModelCalibration|Model calibration]] is one of the most important and most overlooked properties.** Nate Silver in *The Signal and the Noise*: calibration is *"the single most important test of a forecast."* A 70%-probability prediction is calibrated iff the predicted outcome occurs 70% of the time. Two motivating examples: a recommender that always plays a user's most-likely genre (100% romance) is uncalibrated against the 80/20 romance/comedy actual preference; an ad-click model can rank A above B correctly while being miscalibrated, breaking downstream click-count estimates. **Platt scaling** (`sklearn.calibration.CalibratedClassifierCV`) is the standard fix; calibration curves are produced via `sklearn.calibration.calibration_curve`.
- **Confidence measurement is per-sample, not per-system.** Aggregate metrics tell you average performance; confidence tells you whether to show *this* prediction. Below threshold, you can discard, escalate to a human, or ask for more input — a precondition for selective prediction and human-in-the-loop deployment.
- **[[DataSlicing|Slice-based evaluation]] is essential.** Two failure modes: (a) model should perform equally across slices but doesn't (Model A: 98% on majority / 80% on minority / 96.2% overall vs Model B: 95% / 95% / 95% — naive aggregation hides Model A's minority failure); (b) model should perform *differently* on critical slices (e.g., paid users in a churn model) but is tuned only for overall. **[[SimpsonsParadox|Simpson's paradox]]** can flip the choice: Model A beat Model B in both groups of the 1986 kidney-stone study (93% > 87% in group A, 73% > 69% in group B) but lost overall (78% < 83%). The 1973 Berkeley admissions case is the classic real-world instance: aggregate showed bias against women, but four of six departments admitted women at higher rates than men. Three approaches to discovering slices: **heuristics-based** (domain knowledge — mobile vs desktop, geography, browser), **error analysis** (manually inspect misclassifications for patterns), and **slice finders** (Chung et al. 2019 — automated candidate generation via beam search/clustering, then pruning and ranking).

## Key Quotes

> "All models are wrong, but some are useful." — George Box (1976), framing why understanding a model's assumptions is more useful than ranking models in the abstract.

> "If you think that machine learning will give you a 100% boost, then a heuristic will get you 50% of the way there." — Martin Zinkevich, *Rules of Machine Learning*, quoted in the Four-Phases-of-ML sidebar.

> "Data versioning is like flossing. Everyone agrees it's a good thing to do, but few do it." — Huyen on why ML systems' code-plus-data nature defeats traditional version control.

> "Aggressive experiment tracking and versioning helps with reproducibility, but it doesn't ensure reproducibility." — On the limits of bookkeeping in the face of CUDA nondeterminism and framework-level randomness.

> "It's crucial to never use your test split to tune hyperparameters." — The single hardest rule in the AutoML section; tuning on test overfits the test set and inflates reported performance.

> "Calibration is one of the most important tests of a forecast — I would argue that it is the single most important one." — Nate Silver, *The Signal and the Noise*, quoted in the Model Calibration section.

> "A good system isn't necessarily useful, and a bad system isn't necessarily useless." — On evaluating ML systems against the *useful* threshold (human baselines, existing solutions) rather than against an abstract benchmark.

> "Evaluation metrics, by themselves, mean little. When evaluating your model, it's essential to know the baseline you're evaluating it against." — The chapter's organizing argument for the five baselines and the suite of beyond-aggregate evaluation methods.

## Connections

### Book / author / publisher
- [[ChipHuyen]] — author of the book; this chapter is one of ten in *Designing Machine Learning Systems*.
- [[OReilly]] — publisher.
- [[ai-engineering-chip-huyen]] — Huyen's 2024 follow-up book; *AI Engineering* is the foundation-model-era successor and shares the model-selection / evaluation / baselines / slicing scaffolding (see esp. [[ai-engineering-ch04-evaluate-ai-systems|Ch 4]]).

### Model-selection and trade-offs
- [[ModelSelection]] — this chapter is one of the canonical applied treatments of the topic; six tips, four phases, multi-axis trade-offs.
- [[LogisticRegression]], [[NaiveBayes]], [[KNearestNeighbors]], [[DecisionTrees]], [[RandomForests]], [[LSTM|LSTM]]/[[RNN]], [[transformer]], [[bert|BERT]] — the model families Huyen names as candidate sets for common tasks (text classification, fraud detection, recommendation).
- [[TransferLearning]], [[pretraining]] — pretrained BERT/GPT-3 as feature extractors and as low-effort high-complexity starting points.
- [[Overfitting]], [[Underfitting]], [[BiasVarianceTradeoff]] — the underlying tensions any model-selection decision must trade off.
- [[F1Score]], [[Accuracy]], [[CrossEntropy]] — the metric vocabulary used in the chapter's worked examples (esp. the imbalanced F1 = accuracy ≈ 0.82 / 0.10 baseline table).

### Ensembles
- [[ModelEnsemble]] — direct topic.
- [[Bagging]], [[Boosting]] — two of the three ensembling families.
- [[RandomForests]] — bagging + feature randomness; called out as the canonical bagging example.
- [[GradientBoosting]] / GBM, [[XGBoost]], [[LightGBM]] — boosting realizations; XGBoost cited for Higgs boson discovery (Chen and He 2015); LightGBM as the parallel-friendly successor.
- [[Kaggle]] — Huyen's data point that 20/22 winning 2021 solutions used ensembles; the *MLWave* ensemble guide is referenced.
- [[NeuralNetwork]] — bagging stabilizes unstable methods including neural nets.

### Experiment tracking & versioning
- [[ExperimentTracking]], [[Versioning]], [[Reproducibility]] — the three intertwined concepts.
- [[MLflow]], [[WeightsAndBiases]], [[DVC]] — named tooling that has converged on tracking + versioning + (partial) data versioning.
- [[observability]] — Huyen's framing that experiment tracking is *observability for training*; the deeper monitoring story lives in DMLS Ch 8.

### Debugging
- [[Debugger]] — adjacent general-debugging concept.
- [[AndrejKarpathy]] — Karpathy's *"A Recipe for Training Neural Networks"* is the explicit reference for the three debugging recipes.
- [[Overfitting]] — overfit-a-single-batch is the diagnostic that proves the implementation can learn at all.
- [[maskedlanguagemodel|Masked Language Model]] / [[nextsentenceprediction|Next Sentence Prediction]] — used as a concrete example: build BERT-like model with MLM loss first, add NSP only after the simpler version trains.

### Distributed training
- [[DistributedTraining]] — direct topic.
- [[DataParallelism]], [[ModelParallelism]], [[PipelineParallelism]] — the three named axes.
- [[GradientDescent]], [[MinibatchSGD]] — synchronous vs asynchronous SGD as the data-parallel design choice.
- [[GradientCheckpointing]] — used when samples are too large to fit in memory; 10× larger feedforward models for 20% compute overhead.
- [[NVIDIA]], [[google|Google]], [[openai|OpenAI]], [[Cohere]] — companies Huyen names for large-scale language-model training. [[openai|OpenAI]]'s GPT-3 175B 3.2M batch is the chapter's concrete scale data point.

### AutoML
- [[AutoML]] — direct topic.
- [[HyperparameterTuning]], [[HyperparameterOptimization]] — soft AutoML.
- [[RandomSearch]], [[GridSearch]], [[BayesianOptimization]] — the three hyperparameter-search strategies named.
- [[sklearn|scikit-learn]], [[TensorFlow]], [[RayTune]] — auto-sklearn, Keras Tuner, Ray Tune as tooling.
- [[Quantization]] — Huyen frames quantization (32/16/8-bit) as a hyperparameter to tune.
- [[NeuralArchitectureSearch]] — hard AutoML; three components (search space, performance estimation strategy, search strategy).
- [[reinforcementlearning]] — one of the two search strategies for NAS.
- [[Adam]], [[Momentum]] — the hand-designed optimizers that learned optimizers aspire to replace.

### Offline evaluation
- [[OfflineEvaluation]], [[ModelEvaluation]] — direct topic pages.
- [[Perturbation]] — the test family for measuring robustness to input noise.
- [[ModelCalibration]] — Platt scaling, calibration curves, calibrated recommendations (Steck 2018, Netflix).
- [[DataSlicing]] — slice-based evaluation as the third pillar of the offline-evaluation suite.
- [[SimpsonsParadox]] — kidney-stone and Berkeley admissions worked examples.
- [[BusinessMetric]] — Huyen recommends partnering with the business team to develop evaluation metrics that map to business value.
- [[F1Score]], [[Accuracy]] — the imbalanced-class baselines table (90/10 split → label-matched random gets 0.82 acc / 0.10 F1).
- [[DataLeakage]] — implicit in the "never tune hyperparameters on test split" warning.
- [[TestSetReuse]] — adjacent concept on what *test* means once a split has been touched.
- [[TrainValTestSplit]], [[ValidationSetApproach]] — the splits the chapter assumes.

### Cross-references in the wiki corpus
- [[ai-engineering-ch04-evaluate-ai-systems]] — the 2024 evolution of the same evaluation framework for foundation models; **[[DataSlicing|slicing]]**, **[[SimpsonsParadox|Simpson's paradox]]**, **baselines**, and the **never-tune-on-test** rule are recapitulated almost verbatim.
- [[GradientCheckpointing]] — already covered as an inference-memory technique; this chapter is one of its earliest training-side justifications in the wiki.

## Contradictions

- **None with the existing wiki corpus.** This chapter pre-dates the foundation-model wave covered in [[ai-engineering-chip-huyen|Huyen's 2024 book]] and the wiki's heavier paper-level coverage of LLMs, so the framings on ensembles, hyperparameter tuning, and slice-based evaluation are upstream of — and consistent with — what later sources elaborate. Two soft tensions worth noting (but not contradictions):
  - The 2022 advice *"deep learning is not replacing classical ML"* is more strongly true in the recommender/tabular world than in NLP, where the wiki's later sources document near-total transformer dominance for general-purpose text tasks.
  - The 2022 framing of "graduate student descent" as the dominant hyperparameter-tuning approach has shifted by 2024 toward more automated pipelines ([[RayTune]], [[BayesianOptimization]]) — Huyen herself updates this in *AI Engineering*.
