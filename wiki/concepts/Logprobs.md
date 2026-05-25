---
title: "Logprobs"
type: concept
tags: [sampling, inference, llm, debugging]
sources: [ai-engineering-ch02-foundation-models, ai-engineering-ch04-evaluate-ai-systems]
last_updated: 2024-12-04
---

# Logprobs

**Log-scale probabilities** — the natural log of token probabilities, exposed (sparingly) by model providers. Per [[ai-engineering-ch02-foundation-models|*AI Engineering* Ch 2]]:

> "Logprobs, short for log probabilities, are probabilities in the log scale. Log scale is preferred when working with a neural network's probabilities because it helps reduce the underflow problem."

## Why log scale

A language model with a vocabulary of ≈100K tokens distributes probability across all of them. **The probabilities for many tokens can be too small to be represented as floats** — they get rounded to 0 (the **underflow problem**). Log scale moves these very small numbers into a representable range.

A sequence's log-probability is the **sum of token logprobs** rather than the product of token probabilities:

$$\log P(s) = \sum_t \log P(s_t \mid s_{<t})$$

— much more numerically stable than multiplying many small floats.

## What logprobs are used for

Three categories per Ch 2:
1. **Building applications, especially classification** — read the logprob of each class label and compare.
2. **Evaluating applications** — sequence likelihood as a quality signal.
3. **Understanding how models work under the hood** — debugging, calibration analysis.

## Why providers expose logprobs sparingly

> "Many model providers don't expose their models' logprobs, or if they do, the logprobs API is limited. The limited logprobs API is likely due to security reasons as a model's exposed logprobs make it easier for others to replicate the model."

Ch 2's specific data point: **OpenAI API exposes logprobs of up to the 20 most likely tokens**; the ability to get logprobs for arbitrary user-provided text was discontinued in September 2023. **[[anthropic|Anthropic]] doesn't expose logprobs at all.**

## In test-time-compute

[[bestofn|Best-of-N]] candidate selection by likelihood uses **average logprob per token** — summing the logprobs over the sequence and dividing by length. This avoids the bias toward shorter sequences that summed logprobs alone would create.

> "After sampling multiple outputs, you pick the one with the highest average logprob. As of this writing, this is what the OpenAI API uses [for `best_of`]." — Ch 2

## Debugging heuristic

> "A common debugging technique when working with an AI model is to look at the probabilities this model computes for given inputs. For example, if the probabilities look random, the model hasn't learned much."

## Connections
- [[Softmax]] — the transformation that produces probabilities from logits.
- [[bestofn]] — sequence-selection strategy that depends on logprobs.
- [[Temperature]] / [[Topk]] / [[Topp]] — sampling controls that operate on logprobs.
- [[Perplexity]] — exp of (negative) average logprob — the standard LM evaluation metric.
- [[ai-engineering-ch02-foundation-models]] — primary source.

## From [[ai-engineering-ch04-evaluate-ai-systems|AI Engineering Ch 4]]

Ch 4 names logprobs as a **primary evaluation-pipeline input** with two practical uses:

1. **Classification confidence.** If you ask a model to output one of three classes and the logprobs for those three classes are all 30-40%, the model isn't confident. If one class is 95%, it is. Use logprobs to threshold uncertainty before acting on a classification output.
2. **Sequence perplexity.** Logprobs let you compute [[Perplexity|perplexity]] on generated text — useful for fluency, factual-consistency proxies, and [[DataContamination|contamination detection]].

> "When logprobs are available, use them."

Ch 4 also names logprobs as a **functionality dimension of [[ModelBuildVsBuy|model build-vs-buy]]**: *"A functionality that many use cases need is logprobs, which are very useful for classification tasks, evaluation, and interpretability. However, commercial model providers might be hesitant to expose logprobs for fear of others using logprobs to replicate their models. In fact, many model APIs don't expose logprobs or expose only limited logprobs."* This is one of the reasons evaluation-heavy teams sometimes self-host.
