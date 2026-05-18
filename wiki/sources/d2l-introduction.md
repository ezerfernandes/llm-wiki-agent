---
title: "Dive into Deep Learning — Introduction"
type: source
tags: [textbook, d2l, introduction, deep-learning, machine-learning, history]
date: 2026-05-16
source_file: raw/d2l-en/chapter_introduction/
---

# Dive into Deep Learning — Introduction

## Summary

First substantive chapter of [[d2l-preface|*Dive into Deep Learning*]] ([[AstonZhang]], [[ZacharyLipton]], [[MuLi]] & [[AlexanderSmola]]). Defines [[MachineLearning|machine learning]] as "the study of algorithms that can learn from experience" and motivates it as the right tool when human ingenuity cannot enumerate rules — wake-word recognition is the running example. The chapter then catalogs the **four core components** of any ML system (data, model, objective function, optimization algorithm), surveys the **landscape of ML problem types** ([[SupervisedLearning|supervised]] — [[Regression|regression]], [[Classification|classification]], tagging, search, recommendation, sequence learning; [[UnsupervisedLearning|unsupervised]] and [[SelfSupervisedLearning|self-supervised]]; [[reinforcementlearning|reinforcement learning]] with [[MarkovDecisionProcess|MDP]] / contextual-bandit / [[MultiArmedBandits|multi-armed-bandit]] special cases), and walks the **historical and intellectual roots** from Bernoulli / Gauss / Fisher / Shannon / Turing / Hebb / Rosenblatt through the 1995–2005 neural-network winter to the [[DeepLearning|deep-learning]] revival driven by **data + compute + algorithms** ([[ImageNet]], cheap [[GPUMemoryHierarchy|GPUs]], [[Dropout]] / [[Attention]] / [[transformer|Transformers]] / large [[languagemodel|language models]] / [[generativeadversarialnetwork|GANs]] / [[DiffusionModel|diffusion models]] / [[DistributedTraining|parallel training]] / open-source frameworks). Closes by defining deep learning as multi-level [[RepresentationLearning|representation learning]] with [[EndToEndTraining|end-to-end training]] that replaces feature engineering.

## Key Claims

- *Machine learning is the study of algorithms that can learn from experience.* Distinct from deterministic rule-based software because performance improves with accumulated observational data or environment interactions, without explicit reprogramming.
- *Every ML system has four core components:* (i) **data**, (ii) a **model** transforming data, (iii) an **objective function** ([[loss function]] — squared error for regression, [[CrossEntropyLoss|cross-entropy]] for classification, sometimes a *surrogate* when the natural metric is non-differentiable), (iv) an **optimization algorithm** ([[GradientDescent|gradient descent]] family). Training optimizes the loss on the **training set**; the **test set** measures whether the model **generalizes** (failure to do so is [[Overfitting|overfitting]]).
- *Data quality matters as much as data volume.* "Garbage in, garbage out"; underrepresented groups in training data cause failures (skin-cancer detection that has never seen black skin); past prejudices encoded in historical labels can be automated by ML — fairness/bias is intrinsic to the data, not a downstream concern.
- *[[SupervisedLearning|Supervised learning]] dominates industrial ML* and decomposes into a rich taxonomy: [[Regression|regression]] (continuous "how much?" outputs, Gaussian-noise / squared-error loss), [[Classification|classification]] (discrete "which one?" outputs, soft-probability outputs + cross-entropy; binary / multiclass / **hierarchical** / **multi-label** / *tagging* variants, exemplified by Linnaean taxonomy and PubMed's 28k-tag MeSH ontology), **search and ranking** (PageRank as the original example; now query-dependent ML), **[[RecommenderSystems|recommender systems]]** (with their pathologies: censored feedback, feedback loops, exposure bias), and **sequence learning** (variable-length inputs and/or outputs — [[PartOfSpeechTagging|PoS tagging]] / NER as aligned cases; [[SpeechRecognition|speech recognition]], TTS, and [[machinetranslation|machine translation]] as sequence-to-sequence).
- *[[UnsupervisedLearning|Unsupervised learning]] asks open-ended questions of unlabeled data:* clustering, subspace estimation ([[PrincipalComponentAnalysis|PCA]] when the dependence is linear), [[WordEmbedding|word embeddings]] with semantic algebra ("Rome − Italy + France = Paris"), causal / [[ProbabilisticGraphicalModel|graphical-model]] discovery, and **deep generative models** ([[VariationalAutoencoder|VAEs]] 2014, [[generativeadversarialnetwork|GANs]] 2014, [[NormalizingFlow|normalizing flows]] 2014/2017, [[DiffusionModel|diffusion models]] 2015/2020).
- *[[SelfSupervisedLearning|Self-supervised learning]]* leverages structure within unlabeled data to fabricate supervision — fill-in-the-blank masked words ([[bert|BERT]]-style), predicting relative positions of image patches, predicting occluded image regions, contrastive perturbation pairs. The learned representations are then fine-tuned on downstream tasks.
- *[[reinforcementlearning|Reinforcement learning]] formalizes agent-environment interaction* over time steps: observations → actions → rewards. Distinguished from supervised learning by the **credit assignment** problem (which past action caused the eventual reward?), **partial observability**, and the **explore/exploit** tradeoff. Special cases: [[MarkovDecisionProcess|MDP]] (fully observed), contextual bandit (state independent of past actions), [[MultiArmedBandits|multi-armed bandit]] (no state). [[DeepReinforcementLearning|Deep RL]] examples: DQN beating humans at Atari (Mnih et al. 2015) and AlphaGo dethroning the Go world champion (Silver et al. 2016).
- *Roots predate computing.* The Bernoulli distribution (Jacob Bernoulli, 1655–1705), the Gaussian distribution and least-squares (Carl Friedrich Gauss, 1777–1855), Ohm's law as the first linear model, Jacob Köbel's 1535 trimmed-mean foot estimation, Ronald Fisher's Iris dataset (1936) and linear discriminant analysis, Claude Shannon's information theory, and Alan Turing's 1950 *Computing Machinery and Intelligence* defining the [[TuringTest|Turing test]] all feed into modern ML. **Fisher was a eugenicist** — "the morally dubious use of data science has as long and enduring a history as its productive use."
- *Neural networks have biological roots and a winter.* Donald Hebb's 1949 *Organization of Behavior* posited that "neurons learn by positive reinforcement" — the **Hebbian learning rule**, inspiring Rosenblatt's perceptron and modern SGD. After early progress, neural-network research **languished from ~1995 to ~2005** because (a) training was computationally prohibitive (RAM plentiful, compute scarce) and (b) datasets were tiny (Iris from 1936 was still popular; MNIST's 60,000 digits was "considered huge"). [[KernelMethods|Kernel methods]], decision trees, and graphical models dominated empirically and had stronger theory.
- *Three forces revived deep learning: data, compute, algorithms.* The Web + low-cost sensors + Kryder's-law cheap storage + Moore's-law cheap compute (especially **GPUs originally engineered for gaming**) made decade-old algorithms (1943 [[MultilayerPerceptron|MLPs]], 1997 [[lstm|LSTM]], 1992 [[QLearning|Q-Learning]], 1998 [[CNN|CNNs]]) suddenly viable. The 1970→2020 table goes from 100 Iris examples on 100 KF Intel 8080 to 1T social-network examples on 1 PF NVIDIA DGX-2 — datasets grew faster than RAM, compute grew faster than data; the sweet spot shifted from linear models / kernels to deep nets.
- *Algorithmic innovations beyond raw scale:* [[Dropout|dropout]] (Srivastava/Hinton/Krizhevsky 2014) for capacity control via noise injection; **[[Attention|attention mechanisms]]** (Bahdanau/Cho/Bengio 2014) — a "learnable pointer structure" that increased memory without increasing parameters; the **[[transformer|Transformer]]** (Vaswani et al. 2017, [[AttentionIsAllYouNeed]]) built solely on attention, exhibiting superior *scaling* in dataset / model / compute (Kaplan et al. [[scalinglaws]]); [[languagemodel|language models]] scaled to GPT-3 / PaLM / LLaMA / OpenAI's **ChatGPT**; multi-stage memory networks / neural programmer-interpreters; [[generativeadversarialnetwork|GANs]] replacing fixed samplers with differentiable ones (zebras, fake faces, sketch-to-photo); diffusion models replacing GANs (DALL-E 2, Imagen); large-batch distributed SGD pushing ResNet-50 / ImageNet training from days to **< 7 minutes** on 1,024 GPUs; deep-learning frameworks evolving across three generations ([[Caffe]] / [[Torch]] / [[Theano]] → [[TensorFlow]] + [[Keras]] / CNTK / Caffe 2 / [[MXNet]] → [[Chainer]] / [[PyTorch]] / Gluon / [[JAX]]).
- *Success stories.* OCR-based mail sorting (since 1990s, source of the famous [[MNIST]] dataset), automated check reading, credit scoring, fraud detection (PayPal/Stripe/AliPay/WeChat/Visa/MasterCard), search and recommendation. Recent consumer-visible advances: **Siri / Alexa / Google Assistant** with near-human speech recognition; ImageNet top-5 error dropped 28% (2010) → 2.25% (2017); **chess** (DeepBlue beat Kasparov 1997), **Go** (AlphaGo achieved parity 2015, combining DL with Monte Carlo tree search), **Poker** (Libratus exceeded humans despite partial observability); partial-autonomy self-driving from **[[Tesla]] / NVIDIA / Waymo**.
- *Deep learning's essence is end-to-end training of multi-layer representations.* Instead of feature engineering ([[CannyEdgeDetector|Canny]] 1987, [[SIFT|Lowe's SIFT]] 2004 dominated CV for a decade), deep nets *jointly* learn all transformations from raw input to output. This **end-to-end** philosophy unifies CV / speech / NLP / medical informatics under a shared toolset. Concurrent trends: parametric → nonparametric models as data grows; acceptance of non-convex optimization and suboptimal solutions; tool-sharing across academic-corporate boundaries (open-source libraries, trained networks, executable notebooks).
- *Caveat on AGI.* "There are simply no tools for [[ArtificialGeneralIntelligence|artificial general intelligence]] that are able to improve themselves, reason about themselves, [and] modify, extend, and improve their own architecture while trying to solve general tasks." The authors argue the *pressing* concern is mundane automation displacing menial jobs and bias-amplifying statistical models — not malevolent superintelligence.

## Key Quotes

> "Machine learning is the study of algorithms that can learn from experience. As a machine learning algorithm accumulates more experience, typically in the form of observational data or interactions with an environment, its performance improves." — the chapter's working definition

> "Often, even when we do not know how to tell a computer explicitly how to map from inputs to outputs, we are nonetheless capable of performing the cognitive feat ourselves. … Armed with this ability, we can collect a huge *dataset* …" — the central trick that makes supervised ML work; the wake-word motivating example

> "The recent progress in statistical models, applications, and algorithms has sometimes been likened to the Cambrian explosion: a moment of rapid progress in the evolution of species." — the post-2010 deep-learning surge

> "Built solely on attention mechanisms, the *Transformer* architecture has demonstrated superior *scaling* behavior: it performs better with an increase in dataset size, model size, and amount of training compute." — corpus-anchor framing of [[AttentionIsAllYouNeed]] + [[scalinglaws]]

> "What differentiates deep learning is that the operations learned at each of the many layers of representations are learned jointly from data." — the canonical definition of deep learning's *essential* property (end-to-end joint optimization of multi-level representations)

> "Fisher was also a proponent of eugenics, which should remind us that the morally dubious use of data science has as long and enduring a history as its productive use in industry and the natural sciences." — historical ethical caveat applied to the discipline's founders

## Connections

### Co-authors and publisher (already on the wiki)
- [[AstonZhang]], [[ZacharyLipton]], [[MuLi]], [[AlexanderSmola]] — D2L co-authors.
- [[Amazon|AWS]] — funder of the book authoring effort.
- [[CambridgeUniversityPress]] — print publisher.
- [[d2l-preface]] — front-matter; this chapter's parent.
- [[d2l-notation]], [[d2l-installation]] — sibling preliminary chapters.
- [[D2LPackage]] — utility library that wraps shared imports/helpers.
- [[JustInTimeTeaching]] — D2L's pedagogical principle this chapter exemplifies (introduce supervised learning via wake-word recognition *before* defining loss functions formally).

### Core ML components and paradigms (deeply cross-linked to existing pages)
- [[MachineLearning]] — the field this chapter defines.
- [[DeepLearning]] — subset of ML the book focuses on.
- [[Dataset]], [[FeatureEngineering]], [[Generalization]], [[Overfitting]], [[DataSplitting]], [[TrainValTestSplit]], [[HoldoutDataset]] — the four-components framing.
- [[Gradient]], [[GradientDescent]], [[StochasticGradientDescent]] — the optimization spine.
- [[CrossEntropyLoss]], [[MeanSquaredError]] — the two canonical losses the chapter names.
- [[SupervisedLearning]] — dominant paradigm, surveyed in depth.
- [[Regression]], [[LinearRegression]] — the simplest supervised case ("how much?" — the contractor pricing example).
- [[Classification]], [[LogisticRegression]], [[Softmax]] — the categorical case ("which one?").
- [[UnsupervisedLearning]], [[PrincipalComponentAnalysis]], [[HierarchicalClustering]], [[KMeansClustering]] — open-ended discovery on unlabeled data.
- [[SelfSupervisedLearning]] — fill-in-the-blank supervision from structure.
- [[reinforcementlearning]] — agent / environment / action / reward framework.
- [[MultiArmedBandits]] — RL special case the chapter names.
- [[bert]], [[maskedlanguagemodel]] — concrete instance of the chapter's "fill in the blanks" self-supervision example.
- [[FewShotLearning]], [[ZeroShotLearning]], [[TransferLearning]], [[FineTuning]] — downstream-task usage of self-supervised representations.

### Architectures the chapter previews (existing concept pages)
- [[NeuralNetwork]], [[MultilayerPerceptron]], [[Backpropagation]], [[ActivationFunction]], [[ReLU]], [[WeightInitialization]] — the biological-inspiration backbone.
- [[CNN]], [[Convolution]], [[Filter]], [[Pooling]] — the LeCun-Bottou-Bengio-Haffner 1998 CV stack.
- [[RNN]], [[lstm|LSTM]], [[GRU]] — the 1997 sequence stack (Hochreiter & Schmidhuber).
- [[Attention]], [[AttentionIsAllYouNeed]], [[transformer]], [[selfattention]], [[multiheadattention]], [[scaleddotproductattention]] — the post-2017 stack.
- [[Dropout]], [[BatchNormalization]] — regularization techniques the chapter cites.
- [[Autoencoder]] — generative-model preliminary.
- [[scalinglaws]], [[chinchillascalinglaws]], [[computeefficienttraining]], [[powerlaw]] — Kaplan-et-al. scaling story the chapter cites.
- [[pretraining]] — the training-recipe layer the language-model success story rests on.

### Application domains
- [[ComputerVision]] — the chapter's pre-eminent deep-learning success case (ImageNet 28%→2.25%).
- [[NLP]] — sentiment, translation, dialogue; Transformers displaced RNNs here.
- [[SpeechRecognition]] — Siri / Alexa / Google Assistant near-human performance.
- [[machinetranslation]] — German-verb-at-the-end example; the original seq2seq motivation.

### Frameworks and infrastructure
- [[PyTorch]] — D2L's current primary framework.
- [[MXNet]] — D2L's original framework.
- [[TensorFlow]] — Google's framework + [[Keras|Keras]] high-level API.
- [[JAX]] — Google's composable-transformations framework.
- [[CUDA]], [[GPUMemoryHierarchy]] — the GPU substrate that made DL practical.
- [[DistributedTraining]], [[DistributedComputing]] — the parallel-SGD wins of large-batch ResNet-50.

### Historical figures and intellectual lineage (existing or implicitly required)
- [[Amazon]], [[google|Google]] (via [[googledeepmind|DeepMind]]'s AlphaGo and Google Assistant), [[meta]], [[openai]] (chapter cites ChatGPT, GPT-4) — the institutional landscape.
- [[Tesla]] — partial-autonomy self-driving example.
- [[2001.08361-scaling-laws]] — Kaplan et al. scaling-law paper the chapter cites for Transformer scaling.
- [[1706.03762-attention-is-all-you-need]] — Vaswani et al. Transformer paper the chapter cites.
- [[1810.04805-bert]] — BERT, the masked-language-model instance cited for self-supervised text learning.

### Open-research-question pages
- [[CapabilityVsAlignment]], [[Hallucination]], [[ClassImbalance]], [[ConceptDrift]], [[DataDrift]] — touched implicitly by the chapter's fairness / feedback-loop / distribution-shift cautions.

## Contradictions

- *None against existing wiki content.* The chapter's positions on (a) attention having displaced RNNs in NLP, (b) deep learning revival driven by data + compute + algorithms, (c) Transformer's scaling advantage, and (d) AGI being "far away" are all consistent with the existing [[d2l-preface]] / [[2001.08361-scaling-laws]] / [[1706.03762-attention-is-all-you-need]] / [[2605.12966-agentic-ai-to-agi]] coverage.
- *Mild framing tension* with [[2605.12966-agentic-ai-to-agi]]'s [[AverageTrap]] argument: the chapter assumes monolithic supervised learning generalizes fine when given enough data, which is exactly what Liao et al. argue is *structurally* bottlenecked under heterogeneous task manifolds. D2L Ch 1 is silent on the agentic-AI critique — this is a textbook-vs-frontier-paper gap, not an internal contradiction.
- *Notational/historical scope:* the chapter dates Hebbian learning to 1949 and biologically-inspired NNs to Alexander Bain (1873) and James Sherrington (1890) — these antedate the post-1956 "AI" framing but are presented as continuous with modern NN history. No conflict; just a wider historical lens than most ML textbooks.
