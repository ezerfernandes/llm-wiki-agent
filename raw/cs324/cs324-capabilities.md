# Stanford CS324 (Winter 2022) — Capabilities
Source: https://stanford-cs324.github.io/winter2022/lectures/capabilities/
Fetched for wiki ingest.

## Overview

This lecture examines what **GPT-3** (175 billion parameters) can accomplish across various NLP tasks, following the benchmarks reported in the original [GPT-3 paper](https://arxiv.org/pdf/2005.14165.pdf) (Brown et al., 2020).

The central framing: "GPT-3 was **not trained on these tasks** explicitly; it was just trained as a language model to predict the next word." Despite this, the model achieves passable-to-strong performance across diverse NLP benchmarks — the key insight motivating the entire analysis.

### Key Insight

GPT-3 was trained solely as a language model to predict the next word, yet performs reasonably across diverse tasks without explicit training on them. Results are mixed:
- **Exceeds SOTA significantly** on language modeling tasks.
- **Lags behind** on tasks requiring large labeled datasets.

The fact that GPT-3 does not dominate every benchmark suggests it hasn't overfit to specific benchmarks, which is taken as evidence of promise for transfer to novel tasks.

A fundamental mystery persists: "Why does this work? No one knows."

## Adaptation Methods

Two primary approaches convert a language model into a task model:

1. **Training**: Supervised learning via probing, fine-tuning, or lightweight fine-tuning.
2. **Prompting** (in-context learning):
   - **Zero-shot** (0 examples)
   - **One-shot** (1 example)
   - **Few-shot** (multiple examples)

Prompting/in-context learning is constrained by the **2048-token** Transformer context limit.

## Task Categories

The lecture organizes evaluations into six domains:
1. Language modeling
2. Question answering
3. Translation
4. Arithmetic
5. News article generation
6. Novel tasks

---

## Language Modeling

### Penn Tree Bank (PTB)

**Adaptation**: Feed the entire text as the prompt; evaluate perplexity.

| Model | Perplexity |
|-------|-----------|
| GPT-3 | **20.5** |
| BERT-Large-CAs | 31.3 |

GPT-3 vastly outperforms existing approaches.

**Contamination caveat**: "The authors did not evaluate on some datasets such as WikiText-103 because GPT-3 was trained on Wikipedia." Penn Treebank was advantageous because it "predated the Internet, and is only available through a paid license," reducing train/test contamination risk. This highlights broader tensions in large-scale model evaluation.

PTB language modeling benchmark history is noted via **Emami & Jelinek (2004)** and **Mikolov & Zweig (2012)**; a preprocessing note is attributed to **John Hewitt** (Stanford NLP).

### LAMBADA (Paperno et al. 2016)

**Task**: Predict the final word of a sentence requiring "long-range dependencies."

**Adaptation**: Frame as an explicit input-output mapping with in-context examples.

| Model | Perplexity |
|-------|-----------|
| GPT-3 (few-shot) | **1.92** |
| SOTA | 8.63 |

### HellaSwag (Zellers et al. 2019)

**Task**: Multiple-choice sentence completion for commonsense reasoning.

**Adaptation**: Score each candidate; predict the best-scoring option using heuristics:
- Unnormalized probability (biased toward short answers)
- Length-normalized probability
- Frequency-normalized probability

| Model | Accuracy |
|-------|----------|
| SOTA | **85.6%** |
| GPT-3 | 79.3% |

---

## Question Answering

Closed-book QA requires models to "know" answers without access to an external database/retrieval.

### TriviaQA (Joshi et al. 2017)

**Task**: Generate answers to trivia questions.

**Adaptation**: Define a prompt from training instances plus the question; use the completion as the answer.

| Model | Accuracy |
|-------|----------|
| RAG | 68.0% |
| GPT-3 (zero-shot) | 64.3% |
| GPT-3 (few-shot) | **71.2%** |

Both model size and the number of in-context examples improve performance.

### WebQuestions (Berant et al. 2013)

**Task**: Answer questions drawn from Google search queries.

| Model | Accuracy |
|-------|----------|
| RAG | **45.5%** |
| GPT-3 (zero-shot) | 14.4% |
| GPT-3 (few-shot) | 41.5% |

### NaturalQuestions

**Task**: Answer questions with long-form responses.

| Model | Accuracy |
|-------|----------|
| RAG | **44.5%** |
| GPT-3 (zero-shot) | 14.6% |
| GPT-3 (few-shot) | 29.9% |

---

## Translation

**Task**: Translate sentences between languages.

**Context**: Machine translation dates to the 1960s; neural approaches emerged in the mid-2010s.

**Standard datasets**: WMT'14 and WMT'16.

**Metric**: BLEU (n-gram overlap).

### German to English

**Adaptation**: Construct a prompt with input-output training instances plus the source text.

| Model | BLEU |
|-------|------|
| SOTA (supervised) | 40.2 |
| GPT-3 (zero-shot) | 27.2 |
| GPT-3 (few-shot) | **40.6** |

GPT-3 matches supervised SOTA without task-specific training data. French and Romanian show similar patterns. English-to-foreign-language performance is significantly weaker (translating *into* a foreign language is harder than *out of* it).

---

## Arithmetic

**Task**: Perform 2–5 digit addition, subtraction, and multiplication (used as a diagnostic / probing task for emergent capability, not a practical application).

**Adaptation**: Pose as question-answering.

GPT-3 performs surprisingly well but imperfectly, hardly demonstrating full arithmetic understanding.

---

## News Article Generation

**Task**: Generate news articles from a title and subtitle.

**Dataset**: titles/subtitles from newser.com.

**Evaluation**: Humans rated the likelihood that an article was machine- vs. human-authored.

**Adaptation**: In-context learning demonstrates the prompt format.

**Results**: Humans correctly identified articles as "machine"-generated only **52% of the time** (barely above the 50% random baseline). For one particular sample article, correct identification dropped to **12%**.

---

## Novel Tasks

### Using New Words

**Task**: Generate sentences using made-up words given their definitions.

**Adaptation**: Describe the task in the prompt.

Example: "To 'screeg' something is to swing a sword at it."

### Correcting English Grammar

**Task**: Convert ungrammatical sentences into correct versions.

**Adaptation**: Provide input-output example pairs.

---

## Other Benchmarks

- **SWORDS**: Lexical substitution.
- **Massive Multitask Language Understanding (MMLU)**: 57 multiple-choice problem sets spanning mathematics, US history, computer science, law, and more.
- **TruthfulQA**: Answers questions that humans themselves typically answer incorrectly (tests imitation of human falsehoods).

Performance remains mediocre on these, though the few-shot in-context learning behavior is notable.

---

## Perplexity: Mathematical Foundation

**Definition**: The geometric average of per-token (inverse) probabilities — the average "branching factor" per token. The joint sequence probability is decomposed via the chain rule, then geometric averaging is applied to avoid the length bias that plagues arithmetic means.

$$\text{perplexity}_p(x_{1:L}) = \exp\left(\frac{1}{L} \sum_{i=1}^L \log \frac{1}{p(x_i \mid x_{1:i-1})}\right)$$

Interpreted as the average "branching factor" per token.

### Two Error Types (asymmetric penalties)

- **Recall error**: The model fails to assign probability to the correct token → perplexity blows up toward infinity. "Perplexity has no mercy": if `p(ate | the, mouse) → 0`, perplexity → ∞. This is the catastrophic, asymmetric penalty.
- **Precision error**: The model assigns extra probability mass to incorrect sequences → only a modest penalty. Mixing in ~5% "garbage" increases perplexity by only ~5%, even though this can severely degrade generation quality.

---

## Key Findings / Summary

1. Model size matters: larger models show improved performance.
2. In-context examples matter: few-shot consistently outperforms zero-shot. "Both increasing the size of the model and the number of examples helps performance."
3. Task adaptation is heuristic-driven (scoring methods such as length-/frequency-normalized probabilities lack a principled basis).
4. Performance spans from massively exceeding SOTA to significantly lagging it.
5. Transfer potential exists despite the lack of task-specific training.
6. "Why does this work? No one knows."

## Notable Contributors / References

- **Brown et al. (2020)** — GPT-3 paper authors: Tom B. Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, J. Kaplan, Prafulla Dhariwal, Arvind Neelakantan, Pranav Shyam, Girish Sastry, Amanda Askell, Sandhini Agarwal, Ariel Herbert-Voss, Gretchen Krueger, T. Henighan, R. Child, A. Ramesh, Daniel M. Ziegler, Jeff Wu, Clemens Winter, Christopher Hesse, Mark Chen, Eric Sigler, Mateusz Litwin, Scott Gray, Benjamin Chess, Jack Clark, Christopher Berner, Sam McCandlish, Alec Radford, Ilya Sutskever, Dario Amodei.
- **John Hewitt** (Stanford NLP) — Penn Tree Bank preprocessing note.
- **Emami & Jelinek (2004)** — PTB language modeling benchmark pioneers.
- **Mikolov & Zweig (2012)** — PTB language modeling continuation.
- Dataset/benchmark citations: Paperno et al. 2016 (LAMBADA); Zellers et al. 2019 (HellaSwag); Joshi et al. 2017 (TriviaQA); Berant et al. 2013 (WebQuestions).
