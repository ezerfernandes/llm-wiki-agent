---
title: "First-Position Bias"
type: concept
tags: [evaluation, bias, llm-as-judge]
sources: [ai-engineering-ch03-evaluation-methodology, ai-engineering-ch08-dataset-engineering]
last_updated: 2024-12-04
---

# First-Position Bias

The AI-judge bias toward the **first option** in a pairwise comparison or list. Per [[ai-engineering-ch03-evaluation-methodology|*AI Engineering* Ch 3]]:

> "Many AI models have first-position bias. An AI judge may favor the first answer in a pairwise comparison or the first in a list of options."

## Inverse of humans

A striking framing in Ch 3:

> "The position bias of AI is the opposite of that of humans. Humans tend to favor the answer they see last, which is called [[RecencyBias|recency bias]]."

AI judges anchor on the **first** option; human judges anchor on the **last**. This means an AI-judge result and a human-judge result on the same pairwise comparison can systematically disagree just because of where each places its anchor.

## Mitigation

> "This can be mitigated by repeating the same test multiple times with different orderings or with carefully crafted prompts."

The standard practice: for each pair (A, B), evaluate both `(A, B)` and `(B, A)`. If the judge gives the same winner in both orderings, you have a stable preference. If it flips, the result is dominated by position bias and should be discarded or marked as a tie.

## Practical implications

- Comparative-evaluation systems that don't randomize order and don't double-check produce biased rankings.
- Pairwise [[PreferenceModel|preference models]] should be trained with augmented data that swaps order.
- The cost: doubles the comparison count if double-evaluation is done for every pair.

## Connections

- [[ai-engineering-ch03-evaluation-methodology]] — primary source.
- [[LLMAsAJudge]] — the parent paradigm.
- [[SelfBiasJudge]] / [[VerbosityBias]] — sibling AI-judge biases.
- [[RecencyBias]] — the human counterpart (inverse direction).
- [[ComparativeEvaluation]] — the methodology most affected.
- [[ComparisonData]] — preference data labeled with order randomization.

## From [[ai-engineering-ch08-dataset-engineering|AI Engineering Ch 8]]

Ch 8 applies the first-position-bias mitigation explicitly to **synthetic preference-data curation** — not just to evaluation.

### NVIDIA's Nemotron-4 trick

Per Ch 8:

> "[[Nemotron4|Nemotron-4]] researchers asked the AI judge twice, once with the response order swapped. They picked a valid (prompt, winning, losing) triplet only when the AI judge picked the same winner both times."

This **filters out** synthetic preference triples whose label flips with order — leaving only stable preference signals in the training data. It's the same swap-and-check mitigation Ch 3 named for evaluation, repurposed for **data curation**.

### Why it matters for synthetic data

AI-generated preference data inherits the AI judge's first-position bias. Without explicit mitigation, the synthetic preference dataset will systematically encode the bias rather than the true preference signal. The swap-and-keep-only-consistent-verdicts trick is the canonical defense.
