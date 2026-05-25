---
title: "Designing ML Systems — Ch 5: Feature Engineering"
type: source
tags: [book, dmls, designing-ml-systems, feature-engineering, data-leakage, oreilly, chip-huyen]
date: 2022-05-17
sources: []
source_file: raw/books/designing-ml-systems/dmls-ch05-feature-engineering.txt
last_updated: 2026-05-23
---

# Designing ML Systems Ch 5 — Feature Engineering

## Summary

Chapter 5 of [[ChipHuyen|Chip Huyen]]'s *Designing Machine Learning Systems* ([[OReilly|O'Reilly Media]], 2022) argues that — even in the deep-learning era — features remain the single biggest lever on production ML performance, citing the [[Facebook]] ads team's 2014 "Practical Lessons from Predicting Clicks on Ads at Facebook" finding that *"having the right features is the most important thing in developing their ML models."* The chapter is split into three movements: (1) a tour of the **common feature-engineering operations** — handling missing values, [[FeatureScaling|scaling]], [[Discretization|discretization]], encoding [[CategoricalData|categorical features]] (including the [[HashingTrick|hashing trick]]), [[FeatureCrossing|feature crossing]], and discrete/continuous positional embeddings; (2) a deep dive on **[[DataLeakage|data leakage]]** — what it is, six common causes (random-splitting time-correlated data, scaling before splitting, imputing with global statistics, data duplication, group leakage, leakage from the data-generation process), and how to detect it; and (3) the question of **what makes a feature good** — [[FeatureImportance|feature importance]] (via [[XGBoost]] built-ins, [[SHAP]], [[InterpretML|InterpretML]]) and [[FeatureGeneralization|feature generalization]] (coverage + value-distribution overlap between train and test). The chapter closes with a nine-item best-practices checklist (split by time, scale after splitting, use train-split statistics only, track [[DataLineage|data lineage]], involve domain experts, prune useless features) that doubles as Huyen's operational creed for feature work in production.

## Key Claims

- **Features still beat algorithms in production.** *"Once they have a workable model, having the right features tends to give them the biggest performance boost compared to clever algorithmic techniques such as [[Hyperparameter|hyperparameter]] tuning."* Even SOTA architectures perform poorly without good features.
- **Deep learning is sometimes called "feature learning" but does NOT replace feature engineering.** For text and images, raw inputs can be fed in directly, but real ML systems also need tabular signals (comment upvotes, account age, thread popularity) that still must be hand-engineered. TikTok's next-video recommender uses on the order of millions of features.
- **Three types of missing values, often confused.** **MNAR** (missing not at random — high earners hide income), **MAR** (missing at random — gender A skips age), **MCAR** (missing completely at random — rare in practice). The mechanism determines which remediation is safe.
- **Deletion is easy but lossy.** *Column deletion* discards a variable when its missing-rate is high (e.g., >50%) but can drop signal correlated with the label (married → homeowner). *Row deletion* is only safe when data is MCAR and the missing-rate is small (<0.1%); deleting MAR rows introduces bias (removing all gender-A respondents).
- **Imputation choices can silently break models.** A real incident: the frontend stopped collecting age, so the missing-age imputation defaulted to 0 — *"the model never saw the age value of 0 during training, so it couldn't make reasonable predictions."* Avoid filling with values that overlap legitimate values (e.g., filling missing children-count with 0).
- **There is no perfect way to handle missing values.** *"With deletion, you risk losing important information or accentuating biases. With imputation, you risk injecting your own bias into and adding noise to your data, or worse, [[DataLeakage|data leakage]]."*
- **Always [[FeatureScaling|scale]] features before training classical models.** Without scaling, `Annual Income ∈ [10K, 150K]` dwarfs `Age ∈ [20, 40]` numerically. Min-max rescaling to `[0, 1]` (or `[-1, 1]` — Huyen finds the latter empirically better), or [[Standardization|standardization]] (zero-mean / unit-variance) when a normal distribution is plausible. *"Feature scaling once boosted my model's performance by almost 10%."* Especially critical for [[LogisticRegression|logistic regression]] and gradient-boosted trees.
- **Log-transformation mitigates skew.** For heavily skewed distributions, applying `log` often improves model performance — though it doesn't always work and analyses on log-transformed data must be interpreted carefully.
- **Scaling requires global statistics — and this is a data-leakage trap.** During inference, you reuse the training-time mean/min/max/variance; if the data has drifted, those statistics are stale, so models must be retrained often.
- **[[Discretization|Discretization]] (a.k.a. [[Quantization]] / binning) trades resolution for sample efficiency** but introduces sharp boundaries (\$34,999 ≠ \$35,000 = \$100,000). Histograms, quantiles, and subject-matter expertise help choose cut-points. Huyen reports it "rarely" helps in her experience.
- **Categorical features in production are dynamic.** Amazon already had over 2 million brands in 2019, and new brands appear continuously. Naïve integer encoding crashes on unseen categories; an `UNKNOWN` bucket starves new brands of recommendations; encoding only the top 99% by popularity still treats new luxury and knockoff brands identically. The same trap arises for new accounts, IPs, domains, restaurants, products.
- **The [[HashingTrick|hashing trick]] (popularized by [[VowpalWabbit|Vowpal Wabbit]] at [[microsoft|Microsoft]]) fixes the vocabulary size in advance** — 18 bits ⇒ 262,144 indices that cover every present and future category. [[Booking|Booking.com]] (Bernardi) found *"even for 50% colliding features, the performance loss is less than 0.5%."* It's shipped in [[scikitlearn|scikit-learn]], [[TensorFlow]], and [[Gensim|gensim]]; especially useful in [[continuallearning|continual learning]].
- **Locality-sensitive hashing** can be used as the hash function so that similar categories hash to nearby indices.
- **[[FeatureCrossing|Feature crossing]] models nonlinear interactions explicitly** — e.g., `marriage × children`. Essential for [[LinearRegression|linear]] / [[LogisticRegression|logistic]] regression and tree-based models that struggle with nonlinearities; less critical for neural networks but still useful. [[DeepFM]] and xDeepFM are the canonical families that exploit explicit feature interactions for [[RecommenderSystems|recommender systems]] and [[CTRPrediction|click-through-rate prediction]]. Caveats: feature-space blow-up (100×100 → 10,000 values) and increased [[Overfitting|overfitting]] risk.
- **Positional embeddings became data-engineering staples after "[[1706.03762-attention-is-all-you-need|Attention Is All You Need]]" (Vaswani et al. 2017).** [[RNN|RNNs]] consume tokens sequentially so position is implicit; [[transformer|transformers]] process tokens in parallel and must be told position explicitly. Absolute integer positions break unit-variance assumptions; rescaled `[0,1]` positions are too close together to differentiate.
- **Two positional-embedding regimes.** *Learned* (a column-per-position matrix summed with [[WordEmbedding|word embeddings]] — how Hugging Face's BERT did it as of August 2021); *fixed* (sine/cosine alternating by index — a special case of **Fourier features**). For continuous coordinates (e.g., 3D points on a teapot surface) a learned matrix can't have continuous columns, but Fourier features still work — Tancik et al. 2020 "Fourier Features Let Networks Learn High Frequency Functions in Low Dimensional Domains."
- **[[DataLeakage|Data leakage]] is when label information leaks into features and is unavailable at inference.** MIT Technology Review (July 2021): hundreds of COVID-detection models failed because they had learned patient-position (scans of seriously-ill patients were taken lying down) or hospital-specific scan-label fonts as proxies for severity.
- **Six common causes of data leakage.** (1) Randomly splitting time-correlated data — stock-price example, song-recommendation-on-day-an-artist-dies example. (2) Scaling before splitting (test-set mean/variance leaks into the training process). (3) Imputing missing values with statistics computed over the full dataset. (4) Failing to dedupe before splitting — Barz & Denzler 2019 showed CIFAR-10 has 3.3% and CIFAR-100 has 10% test-train duplicates released in 2009. (5) **Group leakage** — two CT scans of the same patient one week apart land in different splits. (6) Leakage from the data-generation process — hospital A routes suspected cancer patients to a different scanner, and the scanner becomes the predictor.
- **Always split by time, then scale, then handle missing values — using only train-split statistics.** *"Always check for duplicates before splitting and also after splitting just to make sure. If you oversample your data, do it after splitting."*
- **Detect leakage by measuring per-feature predictive power, running [[Ablation|ablation studies]], scrutinizing suspiciously-helpful new features, and never using the test split for anything except final reporting.** A feature pair can leak (start-date + end-date → tenure) when neither feature leaks alone.
- **More features is not always better.** Costs of feature bloat: more leakage surface, [[Overfitting|overfitting]], higher memory at serving time, higher [[Latency|inference latency]] for [[OnlineInference|online prediction]], and technical debt (every pipeline change cascades through every dependent feature). [[Regularization|L1 regularization]] should in theory zero out useless features but in practice explicit pruning helps models learn faster.
- **[[FeatureImportance|Feature importance]] is heavy-tailed.** [[Facebook]]'s ads team (He et al.): the top 10 features account for ~50% of total feature importance; the bottom 300 features contribute <1%. Measure importance with [[XGBoost]]'s `get_score`, with [[SHAP]] (Lundberg — also gives per-prediction attribution), or with [[InterpretML|InterpretML]]. These methods double as [[Interpretability|interpretability]] tools.
- **[[FeatureGeneralization|Feature generalization]] has two axes: coverage and value-distribution overlap.** Low coverage (e.g., a feature present in 1% of data) usually means low generalization — except when missing-ness itself is informative (the 1% with the feature is 99% positive). Train/test coverage divergence is itself a signal of bad splitting or leakage.
- **Generalization-vs-specificity trade-off.** `DAY_OF_THE_WEEK` (values Mon–Sat in train but only Sun in test) generalizes poorly; `HOUR_OF_THE_DAY` has 100% overlap and helps; `IS_RUSH_HOUR` is more generalizable but discards information vs. `HOUR_OF_THE_DAY` — often you want both.
- **Subject-matter expertise is part of feature engineering.** Domain experts are often nonengineers; design workflows so they can contribute. Reading Kaggle-competition write-ups is recommended for learning feature-engineering tricks.

## Key Quotes

> "Having the right features is the most important thing in developing their ML models." — quoting [[Facebook]]'s 2014 *Practical Lessons from Predicting Clicks on Ads at Facebook*; framing the chapter's thesis.

> "State-of-the-art model architectures can still perform poorly if they don't use a good set of features." — opening claim that features dominate algorithmic cleverness.

> "Feature scaling once boosted my model's performance by almost 10%." — Huyen's footnote-4 anecdote on the underappreciated impact of [[FeatureScaling|scaling]].

> "Because patients scanned while lying down were more likely to be seriously ill, the model learned to predict serious covid risk from a person's position." — paraphrasing MIT Technology Review on the canonical COVID-imaging [[DataLeakage|leakage]] failure.

> "A 50% collision rate only causes the log loss to increase less than 0.5%." — [[Booking|Booking.com]] (Bernardi) finding that the [[HashingTrick|hashing trick]] is robust under heavy collision.

> "There is no perfect way to handle missing values. With deletion, you risk losing important information or accentuating biases. With imputation, you risk injecting your own bias into and adding noise to your data, or worse, data leakage." — Huyen's honest summary on imputation/deletion trade-offs.

> "A benchmark stops being useful as soon as it becomes public." — the *Ion Switching* / Kaggle cautionary tale: synthesized test data was reverse-engineered and the two winning teams exploited the leak.

> "We are never done with data and features. In most real-world ML projects, the process of collecting data and feature engineering goes on as long as your models are in production." — closing reminder that feature engineering is continuous, tying the chapter to [[continuallearning|continual learning]].

## Connections

- [[ChipHuyen]] — author of *Designing Machine Learning Systems*; this is Ch 5 of her [[OReilly]] book.
- [[OReilly]] — publisher of the book.
- [[FeatureEngineering]] — primary concept of the chapter; this source materially expands the stub page.
- [[DataLeakage]] — the chapter's centerpiece deep-dive; six causes enumerated.
- [[FeatureScaling]] — chapter section; min-max, `[a,b]`, and standardization formulas given.
- [[Standardization]] — zero-mean unit-variance scaling discussed alongside min-max.
- [[CategoricalData]] — production-categorical-features problem and remedies.
- [[OneHotEncoding]] — the naïve encoding the chapter compares against.
- [[LabelEncoding]] — the integer-index baseline that breaks on unseen categories.
- [[HashingTrick]] *(to create)* — the chapter introduces it explicitly, attributing to [[VowpalWabbit]] / [[microsoft|Microsoft]].
- [[FeatureCrossing]] *(to create)* — combining features to model nonlinearities; canonical for [[DeepFM]].
- [[DeepFM]] — named as exploiting explicit feature interactions for [[CTRPrediction]].
- [[CTRPrediction]] — click-through-rate prediction; the canonical application of feature crossing + hashing.
- [[RecommenderSystems]] — the broader system class where these techniques matter most.
- [[Discretization]] *(to create)* — binning continuous features; aka quantization.
- [[Quantization]] — alternate name; the existing page is mostly about model quantization but the chapter uses the term for feature binning.
- [[Imputation]] *(to create)* — filling missing values; mean/median/mode/default discussed.
- [[MissingValues]] *(to create)* — taxonomy MNAR/MAR/MCAR.
- [[FeatureImportance]] *(to create)* — measuring per-feature contribution to model performance.
- [[FeatureGeneralization]] *(to create)* — coverage + value-distribution overlap.
- [[Coverage]] — Huyen uses this term for the percentage of samples carrying a feature.
- [[SHAP]] — model-agnostic feature-attribution method (Lundberg); the chapter promotes it.
- [[XGBoost]] *(to create or verify)* — gradient-boosted trees with built-in `get_score` importance.
- [[InterpretML]] *(to create)* — open-source feature-importance/interpretability package.
- [[Interpretability]] — feature-importance methods double as interpretability tools.
- [[FourierFeatures]] *(to create)* — generalization of fixed sinusoidal positional embeddings to continuous inputs.
- [[positionalencoding]] — sinusoidal vs learned position embeddings; the chapter introduces both via the [[transformer]] paper.
- [[transformer]] — parallel token processing motivates explicit position embeddings.
- [[1706.03762-attention-is-all-you-need]] — origin of positional embeddings; chapter cites Vaswani et al. 2017 directly.
- [[Embedding]] — the chapter's sidebar defines embeddings and embedding spaces.
- [[WordEmbedding]] — position embeddings are summed with word embeddings in BERT.
- [[bert|BERT]] — Hugging Face's BERT learned-position-embedding implementation cited as of Aug 2021.
- [[HuggingFace]] — the implementation reference for learned positional embeddings.
- [[RNN]] — implicit-position baseline contrasted with [[transformer]]'s explicit positions.
- [[LogisticRegression]] — example of a classical model that benefits from feature scaling and crossing.
- [[LinearRegression]] — same — benefits from explicit feature crosses.
- [[Overfitting]] — risk of feature crossing and feature bloat.
- [[Regularization]] — L1 can in theory prune useless features but explicit pruning is still recommended.
- [[Latency]] / [[CostAndLatency]] — too many features increase serving latency.
- [[OnlineInference]] — online prediction is where feature-extraction latency bites hardest.
- [[DataLineage]] — Huyen's explicit best-practice: track lineage of every feature.
- [[continuallearning]] — hashing trick is especially valuable in continual-learning settings (cross-reference to Ch 9).
- [[FeatureStore]] — Ch 5 defers feature stores to Ch 10 but mentions them as the infrastructure for feature management.
- [[DataAugmentation]] — oversampling is mentioned as a duplication trap; do it after splitting.
- [[CrossValidation]] / [[TrainValTestSplit]] / [[DataSplitting]] — split-by-time guidance updates the basic ML-101 random-split recipe.
- [[TrainingServingSkew]] — stale training-time scaling statistics in production are a form of training-serving skew.
- [[SentimentAnalysis]] — spam-comment classifier is the running NLP example.
- [[NGram]] — n-gram vocabularies are the pre-deep-learning baseline for text features.
- [[Tokenization]] — deep learning replaces n-grams + lemmatization with tokenization + learned embeddings.
- [[StopWord]] — classical text-processing technique now subsumed by tokenization + embeddings in DL.
- [[VocabularySize]] — hash-space size is the analog for hashed categorical features.
- [[CIFAR10]] — used as the canonical "released-with-duplicates" cautionary example (Barz & Denzler 2019: 3.3% test-train duplicates).
- [[Generalization]] — feature generalization is a specific instance of the broader concept.
- [[Kaggle]] — Ion Switching competition cited as a leakage cautionary tale; reading Kaggle winners recommended for learning feature engineering.
- [[universityofliverpool]] — launched the Ion Switching Kaggle competition (2020) referenced in the leakage section.
- [[Amazon]] — 2 million brands as of 2019 — running example for categorical-cardinality explosion.
- [[Facebook]] *(to create or verify)* — author of 2014 "Practical Lessons from Predicting Clicks on Ads at Facebook"; ads-team data on heavy-tailed feature importance.
- [[VowpalWabbit]] *(to create)* — the [[microsoft|Microsoft]] package that popularized the hashing trick.
- [[microsoft|Microsoft]] — origin of Vowpal Wabbit.
- [[Booking]] *(to create or skip)* — Booking.com's empirical result on hashing-collision tolerance (Bernardi 2018).
- [[InterpretML]] *(to create)* — Microsoft's interpretability package leveraging feature importance.
- [[scikitlearn]] / [[TensorFlow]] / [[Gensim]] — ship the hashing trick; recommended for production use.
- [[ai-engineering-ch08-dataset-engineering]] — companion chapter in Huyen's later [[ai-engineering-chip-huyen|AI Engineering]] book that revisits dataset/feature topics for LLMs.

## Contradictions

- None directly contradicted in the existing wiki. Minor terminology overlap to note: [[Quantization]] in the existing wiki primarily describes **model-weight quantization** (numerical precision reduction for compression/inference), whereas this chapter uses *quantization* as a synonym for **feature discretization (binning)**. The two senses should be disambiguated when [[Discretization]] is created — Huyen's usage is the older statistical sense; the existing [[Quantization]] page covers the newer model-compression sense.
