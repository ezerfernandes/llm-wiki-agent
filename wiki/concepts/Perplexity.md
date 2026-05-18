---
title: "Perplexity"
type: concept
tags: [nlp, language-models, evaluation, information-theory]
sources: [d2l-recurrent-neural-networks]
last_updated: 2026-05-16
---

# Perplexity

The NLP-standard **language-model quality metric**: the exponentiated average per-token cross-entropy of a sequence under the model

$$\textrm{PPL} = \exp\!\left(-\frac{1}{n}\sum_{t=1}^n \log P(x_t \mid x_{t-1}, \ldots, x_1)\right)$$

([[d2l-recurrent-neural-networks]] §perplexity). Adopted "for historical reasons" — equivalent information-theoretically to averaged [[CrossEntropyLoss|cross-entropy]].

## Interpretation

> "Perplexity can be best understood as the reciprocal of the geometric mean of the number of real choices that we have when deciding which token to pick next." — [[d2l-recurrent-neural-networks]]

## Bounds

- **Perfect predictor:** model always assigns probability 1 to the true next token → $\textrm{PPL} = 1$.
- **Worst predictor:** model assigns probability 0 → $\textrm{PPL} = +\infty$.
- **Uniform baseline:** model predicts uniform over vocabulary → $\textrm{PPL} = |\mathcal{V}|$ (the trivial upper bound any useful model must beat).

## Why exp(avg-CE), not raw likelihood

Per-document likelihood is not length-comparable: longer sequences are exponentially less likely. Average cross-entropy is length-comparable. Exponentiating just gives an intuitive interpretation (effective vocabulary size).

## Use in training

D2L tracks per-batch perplexity during training of the from-scratch character-level [[RNN]] LM on *The Time Machine*. Cross-entropy + softmax outputs feed directly into both the gradient computation and the perplexity metric.

## Connections

- [[d2l-recurrent-neural-networks]] — definitional source.
- [[LanguageModel]] — what perplexity evaluates.
- [[CrossEntropyLoss]] — perplexity = exp(avg-CE).
- [[NGram]] / [[RNN]] / [[Transformer]] — LM architectures evaluated by perplexity.
- [[informationtheory|Information Theory]] — entropy / surprisal / KL underpinnings.
