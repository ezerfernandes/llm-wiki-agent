---
title: "Dive into Deep Learning — Preface"
type: source
tags: [textbook, d2l, preface]
date: 2026-05-16
source_file: raw/d2l-en/chapter_preface/
---

# Dive into Deep Learning — Preface

## Summary

Front-matter chapter of *Dive into Deep Learning* (D2L) by [[AstonZhang]], [[ZacharyLipton]], [[MuLi]] & [[AlexanderSmola]] — a free, open-source, multi-framework ([[MXNet]] / [[PyTorch]] / [[TensorFlow]] / [[JAX]]) deep-learning textbook built as executable [[Jupyter]] notebooks and published online plus in print via [[CambridgeUniversityPress]]. The preface lays out the book's pedagogical thesis — teach [[DeepLearning]] *just-in-time* by interleaving *concepts*, *context*, and *code* — and the authoring infrastructure that makes it possible: GitHub source, Jupyter notebooks for prose-plus-code, Sphinx for rendering, and a Discourse forum. The chapter situates D2L against alternatives ([[Bishop2006|Bishop's PRML]], [[Goodfellow.Bengio.Courville.2016|Goodfellow-Bengio-Courville]], scattered blog/Distill posts) and credits hundreds of named GitHub contributors plus [[Amazon|AWS]] support.

## Key Claims

- Deep learning has transitioned from an obscure academic subfield into a general-purpose technology driving [[ComputerVision]], [[NLP|natural language processing]], [[SpeechRecognition|automatic speech recognition]], [[reinforcementlearning|reinforcement learning]], and biomedical informatics — and is now reshaping movies, medicine, and basic sciences (astrophysics, climate, weather, biomedicine).
- Practising deep learning requires *simultaneously* mastering five disciplines: (i) problem framing, (ii) the model's mathematics, (iii) optimization for fitting, (iv) statistical principles of generalization, and (v) engineering for efficient training on real hardware. No prior resource integrated all five with both depth and runnable code.
- Goals of the book: free and open, technically deep enough for an applied ML scientist starting point, runnable code, rapidly updatable by the community, and complemented by a discussion forum.
- D2L claims to be "the first book published using such an integrated workflow" — GitHub for source, Jupyter notebooks for code + equations + text, Sphinx as renderer, Discourse for discussion.
- *Pedagogical principle — "Learning by Doing":* teach concepts *just-in-time*. Reverses the [[Bishop2006|Bishop-style]] exhaustive-foundations-first order so beginners "taste the satisfaction of training your first model before worrying about more esoteric concepts."
- *One working example, one notebook:* keeps copy-and-modify workflow viable. Each example is presented in two forms — from-scratch (only NumPy-like ops + [[Autograd|automatic differentiation]]) *and* high-level-API — and afterwards relies on the high-level API.
- The `d2l` Python package captures frequently-imported helpers; blocks marked `#@save` are persisted into it.
- Three-part structure: **Part 1** preliminaries + linear models + [[MultilayerPerceptron|MLPs]] + [[regularization]]; **Part 2** modern techniques ([[CNN|CNNs]], [[RNN|RNNs]], [[Attention|attention]] + [[transformer|transformers]] — explicitly noting attention has "displaced RNNs as the dominant architecture for most natural language processing tasks"); **Part 3** (online only) scalability/efficiency + [[ComputerVision]] + [[NLP]] applications + language-model pretraining.
- Audience: students, engineers, researchers; no prior ML required but assumes "modest amounts of linear algebra, calculus, probability, and Python programming." Prioritizes intuition over rigour. Recommends [[Bollobas.1999|*Linear Analysis*]], [[Wasserman.2013|*All of Statistics*]], and [[JoeBlitzstein|Blitzstein]]'s probability books/courses for supplementary depth.
- Originally MXNet-first; redesigned and reimplemented since July 2021 with [[PyTorch]] as primary framework; PyTorch → JAX adaptation by Anirudh Dagar; PyTorch → PaddlePaddle adaptation (Chinese draft) by Baidu team.
- Acknowledges [[Amazon|Amazon Web Services]] (Wen-Ming Ye, George Karypis, Swami Sivasubramanian, Peter DeSantis, Adam Selipsky, Andy Jassy) for "generous support in writing this book" and [[CambridgeUniversityPress]] (commissioning editor David Tranah) for publication support.
- Lists ~250+ named GitHub contributors to the English draft.

## Key Quotes

> "This book represents our attempt to make deep learning approachable, teaching you the *concepts*, the *context*, and the *code*." — thesis statement

> "In this book, we teach most concepts *just in time*. In other words, you will learn concepts at the very moment that they are needed to accomplish some practical end." — pedagogical method

> "We believe that *Dive into Deep Learning* might be the first book published using such an integrated workflow." — on the GitHub + Jupyter + Sphinx + Discourse stack

> "In :numref:`chap_attention-and-transformers`, we describe a relatively new class of models, based on so-called *attention mechanisms*, that has displaced RNNs as the dominant architecture for most natural language processing tasks." — corpus-anchor framing of [[Attention]] / [[transformer]]

> "We are hopeful that as the theory of deep learning progresses, each future edition of this book will provide insights that eclipse those presently available." — epistemic stance: theory is incomplete, the book will track it

## Connections

- [[AstonZhang]] — first author; lead maintainer.
- [[ZacharyLipton]] — co-author; CMU.
- [[MuLi]] — co-author; AWS principal scientist.
- [[AlexanderSmola]] — co-author; AWS VP / distinguished scientist.
- [[Amazon|AWS]] — funder of book authoring; original MXNet framework backer.
- [[CambridgeUniversityPress]] — publisher of the print edition; commissioning editor David Tranah.
- [[PyTorch]] — primary framework since the July 2021 redesign.
- [[MXNet]] — original primary framework.
- [[TensorFlow]] — secondary framework (Yuan Tang adaptation).
- [[JAX]] — fourth supported framework (Anirudh Dagar adaptation).
- [[Jupyter]] — notebook format used for every chapter.
- [[NumPy]] — substrate for from-scratch implementations.
- [[Autograd|automatic differentiation]] — the other half of the from-scratch substrate.
- [[DeepLearning]] — subject of the book.
- [[NeuralNetwork]] — basic primitive.
- [[CNN]] / [[RNN]] / [[Attention]] / [[transformer]] — Part 2 architectures.
- [[reinforcementlearning]] — listed as a deep-learning application area.
- [[ComputerVision]] / [[NLP]] / [[SpeechRecognition]] — three application domains the preface highlights as having been transformed.
- [[D2LPackage|the `d2l` package]] — utility library packaging shared imports / helpers.
- [[JustInTimeTeaching]] — pedagogical principle the book operationalizes.

## Contradictions

- None against existing wiki content. The preface's MXNet-vs-PyTorch-vs-TensorFlow-vs-JAX neutrality is consistent with [[PyTorch]]'s existing description and does not conflict with any framework claim in the corpus.
