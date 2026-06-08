---
title: "Yann LeCun"
type: entity
tags: [person, researcher, cnn, deep-learning]
sources: [d2l-convolutional-neural-networks, ai-engineering-ch06-rag-agents, mlsysbook-ch05-neural-computation]
last_updated: 2026-06-05
---

# Yann LeCun

French-American computer scientist; chief AI scientist at Meta (formerly Facebook); New York University professor; 2018 [[TuringAward]] co-recipient (with [[GeoffreyHinton]] and [[YoshuaBengio]]) for foundational deep-learning work. Best known as the inventor of [[LeNet]] — the first successfully-deployed [[CNN|convolutional neural network]] — and for the first paper to train CNNs via [[Backpropagation]] (LeCun, Boser, Denker et al. 1989).

## Why he matters here

- **CNN pioneer.** Introduced the [[ConvolutionalLayer|convolutional layer]] as a practical architecture; named in [[d2l-convolutional-neural-networks]] as the LeNet author. His 1989 paper was "the first study to successfully train CNNs via backpropagation" ([[d2l-convolutional-neural-networks]] §lenet).
- **LeNet-5.** Developed at AT&T [[BellLabs]] in the 1990s for handwritten-digit recognition ([[MNIST]]). Matched SVM accuracy (<1% per-digit error) when SVMs were the dominant supervised-learning approach. Adopted commercially for ATM check-deposit OCR; *some ATMs still run his and [[LeonBottou|Leon Bottou]]'s 1990s code* ([[d2l-convolutional-neural-networks]]).
- **Cited LeNet references.** `LeCun.Jackel.Bottou.ea.1995` (the CNN-tutorial paper D2L cites when introducing CNNs); `LeCun.Bottou.Bengio.ea.1998` ("Gradient-based learning applied to document recognition", *Proceedings of the IEEE* — the canonical LeNet-5 reference); `LeCun.Boser.Denker.ea.1989` (first backprop-trained CNN); `LeCun.Bengio.ea.1995` (CNNs for time-series).

## Affiliations

- [[BellLabs]] (AT&T) — where LeNet was developed and deployed.
- Meta / [[Facebook]] — chief AI scientist.
- [[NewYorkUniversity]] — professor (Courant Institute / CDS).

## Connections

- [[d2l-convolutional-neural-networks]] — chapter that walks through LeNet line by line.
- [[LeNet]] — the architecture; one-to-one cited to LeCun.
- [[CNN]] — the broader family; LeCun's invention.
- [[Backpropagation]] — LeCun's 1989 paper first applied backprop to CNNs.
- [[LeonBottou]] — long-running collaborator; co-author on the deployed LeNet code.
- [[MNIST]] — the dataset LeCun curated and on which LeNet established CNN credibility.
- [[madewithml-foundations-cnn]] — Mohandas' applied take; LeCun's foundational work is the historical anchor.
- [[USPSDigitRecognition]] / [[mlsysbook-ch05-neural-computation]] — Reddi's Ch 5 case study credits LeCun et al. (1989, 1998) with the USPS ZIP-code recognizer (1% error, ~10K params, Sun-4/260), and names LeCun (with [[YoshuaBengio|Bengio]]/[[GeoffreyHinton|Hinton]]) as the 2018 Turing trio whose contributions shaped the three dominant accelerator workloads (convolution, attention, gradient computation).

## From [[ai-engineering-ch06-rag-agents|AI Engineering Ch 6]]

[[ChipHuyen|Huyen]] cites LeCun (as Meta's Chief AI Scientist) for his **unequivocal 2023 position that autoregressive LLMs cannot plan**. In Ch 6's planning section:

> *"Meta's Chief AI Scientist Yann LeCun states unequivocally that autoregressive LLMs can't plan (2023)."*

This is one of the two skeptic positions Huyen records (the other is [[SubbaraoKambhampati|Kambhampati]]'s); both are countered with [[ReasoningWithLanguageModelIsPlanningWithWorldModel|Hao et al. 2023]]'s *"LLMs contain a world model"* argument. Huyen does not adjudicate — the chapter's agnostic position is that *"it's unclear whether it's because we don't know how to use LLMs the right way or because LLMs, fundamentally, can't plan."*

LeCun's broader research agenda — energy-based models, world models, JEPA (Joint Embedding Predictive Architecture) — is the AI-architectural alternative he proposes to autoregressive LLMs. His Ch 6 citation is the most-prominent wiki anchor for this position.
