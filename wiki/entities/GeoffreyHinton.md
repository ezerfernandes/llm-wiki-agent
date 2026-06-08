---
title: "Geoffrey Hinton"
type: entity
tags: [person, researcher, deep-learning, turing-award]
sources: [d2l-convolutional-modern, d2l-multilayer-perceptrons, d2l-optimization, mlsysbook-ch05-neural-computation, mlsysbook-ch09-data-selection, mlsysbook-ch10-model-compression]
last_updated: 2026-06-05
---

# Geoffrey Hinton

British-Canadian cognitive psychologist and computer scientist; long-time University of Toronto professor; former Google Brain researcher; 2018 [[TuringAward]] co-recipient (with [[YannLeCun]] and [[YoshuaBengio]]) for foundational deep-learning work. PhD advisor to [[AlexKrizhevsky]] and [[IlyaSutskever]] (the AlexNet team) and to many other major deep-learning figures.

## Why he matters here

- **AlexNet (2012).** Senior author of [[AlexKrizhevsky|Krizhevsky]], [[IlyaSutskever|Sutskever]] & **Hinton** (2012) — the [[AlexNet]] paper that broke [[ImageNet]] and ignited the modern deep-learning revival ([[d2l-convolutional-modern]] §alexnet).
- **Dropout (2014).** Senior author of [[NitishSrivastava|Srivastava]], **Hinton**, [[AlexKrizhevsky|Krizhevsky]] et al. (2014) — the [[Dropout]] paper ([[d2l-multilayer-perceptrons]] §dropout).
- **Layer normalization (2016).** Co-author of [[LayerNormalization|layer normalization]] ([[Ba|Ba]], [[JamieKiros|Kiros]] & **Hinton** 2016) — the BN variant that became default in [[transformer|Transformers]] ([[d2l-convolutional-modern]] §batch-norm).
- **Pre-2012 era.** Co-inventor of [[Backpropagation]] practice in neural networks (Rumelhart, **Hinton**, Williams 1986); contrastive divergence for Boltzmann machines; deep belief nets (2006). Often called a co-founder of the field of deep learning.
- **RMSProp (2012).** Co-introduced [[RMSProp]] with Tijmen Tieleman in Coursera lecture notes — never formally published as a paper but became one of the most-cited optimizers ([[d2l-optimization]] §rmsprop).

## Affiliations

- [[universityoftoronto|University of Toronto]] — emeritus.
- [[google]] — 2013–2023 (Google Brain).
- Vector Institute (Toronto) — founding scientific advisor.

## Connections

- [[d2l-convolutional-modern]] / [[d2l-multilayer-perceptrons]] — chapters that cite him directly.
- [[AlexNet]] / [[Dropout]] / [[LayerNormalization]] / [[RMSProp]] — co-authored / co-introduced.
- [[AlexKrizhevsky]] / [[IlyaSutskever]] — PhD students who became AlexNet co-authors.
- [[YannLeCun]] / [[YoshuaBengio]] — 2018 Turing Award co-recipients.
- [[Backpropagation]] — co-introduced backprop into NN practice.
- [[CNN]] / [[ImageNet]] — the architectures and benchmark his AlexNet broke through on.
- [[ReLU]] / [[mlsysbook-ch05-neural-computation]] — Reddi's Ch 5 credits Nair & Hinton (2010) with demonstrating ReLU's effective deep-net training, and names Hinton (with [[YannLeCun|LeCun]]/[[YoshuaBengio|Bengio]]) as the 2018 Turing trio whose contributions (backprop, conv nets, sequence models) shaped the three dominant accelerator workloads.
- [[KnowledgeDistillation]] / [[mlsysbook-ch09-data-selection]] — coined "dark knowledge" (Hinton et al. 2015); Ch 9 frames distillation's soft labels as a [[DataSelection|data-selection]] technique that raises information density per sample.
- [[KnowledgeDistillation]] / [[mlsysbook-ch10-model-compression]] — Ch 10's distillation math (temperature-scaled softmax, $T^2$ KL loss) is the Hinton et al. (2015) formulation; the [[AlexKrizhevsky|AlexNet]] two-GPU split he co-authored anchors the chapter's "memory shaped deep learning since 2012" war story.
