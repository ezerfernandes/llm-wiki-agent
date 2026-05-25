---
title: "Modeling and Training"
type: concept
tags: [training, modeling, ml-engineering, foundation-models]
sources: [ai-engineering-ch01-intro]
last_updated: 2024-12-04
---

# Modeling and Training

**The process of coming up with a model architecture, training it, and finetuning it.** A model-development-layer responsibility in the [[AIEngineeringStack|AI engineering stack]]. Per [[ai-engineering-ch01-intro|*AI Engineering* Ch 1]], this is the layer that has historically required deep ML expertise — but in the [[AIEngineering|AI engineering]] era, it's *"a nice-to-have, not a must-have"* for application teams using API-served foundation models.

## What ML knowledge entails (classical view)

- **ML algorithms**: clustering, logistic regression, decision trees, collaborative filtering.
- **Neural network architectures**: feedforward, recurrent, convolutional, [[transformer|transformer]].
- **Training mechanics**: gradient descent, loss functions, regularization.

Tools: [[google|Google's]] [[TensorFlow]], [[HuggingFace|Hugging Face's]] [[transformer|Transformers]], [[meta|Meta's]] [[PyTorch]].

## Huyen's framing

> *"With the availability of foundation models, ML knowledge is no longer a must-have for building AI applications. I've met many wonderful and successful AI application builders who aren't at all interested in learning about gradient descent. However, ML knowledge is still extremely valuable, as it expands the set of tools that you can use and helps troubleshooting when a model doesn't work as expected."*

This claim is one of the chapter's most-contested — Huyen flags in a footnote that *"many people would dispute this claim, saying that ML knowledge is a must-have."*

## Training phase taxonomy

Ch 1 makes explicit distinctions among related but-distinct training phases:

| Phase | Definition | Who does it |
|---|---|---|
| **[[Pretraining\|Pre-training]]** | Train from scratch (random weights). For LLMs, usually text completion. **98% of [[openai\|OpenAI's]] InstructGPT compute went here.** | Model developers (frontier labs). |
| **[[FineTuning\|Finetuning]]** | Continue training a previously-trained model. Less data/compute than pre-training. | Anyone — application developers commonly. |
| **[[posttraining\|Post-training]]** | Conceptually same as finetuning, but **done by model developers** before release (e.g., OpenAI post-trains to improve instruction-following). | Model developers. |

Ch 1's footnote: *"If you find the terms 'pre-training' and 'post-training' lacking in imagination, you're not alone. The AI research community is great at many things, but naming isn't one of them."*

## What is NOT training

- **[[Quantization]]** — changes weight values but not via gradient updates.
- **[[PromptEngineering|Prompt engineering]]** — teaches the model what to do via context input. Ch 1 explicitly calls out people who use "training" colloquially when they mean prompt engineering.

## Comparison table

| Category | Traditional ML | Foundation models |
|---|---|---|
| Modeling and training | ML knowledge required | Nice-to-have |

## Connections

- [[AIEngineeringStack]] — model-development-layer home.
- [[pretraining]] / [[FineTuning]] / [[posttraining|PostTraining]] — the three training phases.
- [[Quantization]] / [[PromptEngineering]] — confused-with-training operations.
- [[TensorFlow]] / [[PyTorch]] / [[HuggingFace]] — canonical tools.
- [[AIEngineeringVsMLEngineering]] — comparison taxonomy.
- [[ai-engineering-ch01-intro]] — primary source.
