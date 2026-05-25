---
title: "Few-Shot Learning"
type: concept
tags: [llm, learning-paradigms, prompt-engineering]
sources: [ai-engineering-ch05-prompt-engineering, hands-on-llm-ch06-prompt-engineering, hands-on-llm-ch11-fine-tuning-representation-models]
last_updated: 2026-05-23
---

# Few-Shot Learning

Adapting a model to a new task from only a handful of labeled examples, typically by providing them in the prompt ([[InContextLearning|in-context learning]]) for an LLM or via meta-learning for smaller models. Hallmark capability of [[transformer]] LMs; complements [[FineTuning]] when data is scarce.

## From [[ai-engineering-ch05-prompt-engineering|AI Engineering Ch 5]]

Ch 5 sharpens the terminology and positions few-shot inside the [[InContextLearning|in-context learning]] framework introduced by [[GPT3|GPT-3]] (Brown et al. 2020).

**Shot terminology**:
- **n-shot** = n examples provided.
- **5-shot learning** = five examples.
- **Few-shot** = small number (1-10ish).
- **0-shot** = no examples ([[ZeroShotLearning|zero-shot learning]]).

**How many shots?**

> "In general, the more examples you show a model, the better it can learn. The number of examples is limited by the model's maximum context length. The more examples there are, the longer your prompt will be, increasing the inference cost." — Ch 5

**Diminishing returns with stronger models.** Microsoft 2023 analysis: *"For GPT-3, few-shot learning showed significant improvement compared to zero-shot learning. However, for the use cases in Microsoft's 2023 analysis, few-shot learning led to only limited improvement compared to zero-shot learning on GPT-4 and a few other models."*

Domain-specific use cases (Ch 5's [[IbisDataframeAPI|Ibis dataframe API]] example) remain a strong few-shot use case because the model has seen relatively few examples during pretraining.

**Token economics matter.** Ch 5's Table 5-2 shows that more compact example formats use fewer tokens:

| Format | Tokens (GPT-4) |
|---|---|
| `Input: chickpea / Output: edible` | 38 |
| `chickpea --> edible` | 27 |

Prefer the more compact format if both perform equally.

## Connections

- [[ai-engineering-ch05-prompt-engineering]] — primary source.
- [[InContextLearning]] — parent paradigm.
- [[ZeroShotLearning]] — special case (n=0).
- [[GPT3]] — the model that first demonstrated dramatic few-shot improvement.
- [[PromptEngineering]] — discipline.
- [[ContextLength]] — bound on the number of shots.

## From [[hands-on-llm-ch06-prompt-engineering|Hands-On LLMs Ch 6]]

Ch 6 codifies the three-point spectrum:

> *"Zero-shot prompting does not leverage examples, one-shot prompts use a single example, and few-shot prompts use two or more examples."* — Ch 6

The Ch 6 framing of [[OneShotPrompting|one-shot]] (`n=1`) as a **named distinct case** between zero-shot and few-shot is a useful subdivision Huyen Ch 5's coverage left implicit.

### Few-shot for output-format control

Ch 6's [[OutputVerification|output-verification]] discussion identifies few-shot prompting as the **first of three output-control methods** (alongside grammar-constrained decoding and fine-tuning). The RPG character-profile worked example shows that providing a one-shot JSON template:

```json
{
  "description": "A SHORT DESCRIPTION",
  "name": "THE CHARACTER'S NAME",
  "armor": "ONE PIECE OF ARMOR",
  "weapon": "ONE OR MORE WEAPONS"
}
```

produces conforming output (`Lysandra Shadowstep / Leather Cloak of the Night / Dagger of Whispers`), whereas the zero-shot prompt produces verbose, truncated JSON with unwanted fields. *"This also demonstrates the importance of leveraging few-shot learning to improve the structure of the output and not only its content."*

But: *"It is still up to the model whether it will adhere to your suggested format or not. Some models are better than others at following instructions."* The stronger guarantee comes from [[GrammarConstrainedDecoding|grammar-constrained decoding]].

## From [[hands-on-llm-ch11-fine-tuning-representation-models|*Hands-On LLMs* Ch 11]]

Ch 11 introduces an **embedding-based** alternative to in-context-learning few-shot: **[[SetFit]]** ([[LewisTunstall|Tunstall]] et al. 2022, arXiv:2209.11055). Instead of providing labeled examples to a generative LLM at inference time, SetFit **fine-tunes a [[SentenceTransformers|SentenceTransformer]]** on contrastively-generated sentence pairs from the few labeled examples, then trains a downstream classifier (default: scikit-learn [[LogisticRegression|logistic regression]]) on the resulting embeddings.

Per Ch 11:

> *"Few-shot classification is a technique within supervised classification where you have a classifier learn target labels based on only a few labeled examples. This technique is great when you have a classification task but do not have many labeled data points readily available."*

The Ch 11 framing positions **few-shot classification** as a **labeled-data-scarcity regime** distinct from few-shot prompting (which is a labeled-data-included-in-prompt regime). Both share the *"a few labels per class"* surface, but few-shot prompting needs an LLM at inference time; few-shot classification trains a small encoder + classifier you can deploy without an LLM in the loop.

**Headline Ch 11 result**: 32 labeled examples (16 per class on Rotten Tomatoes) → F1 = 0.85, **matching** the F1 from a logistic regression trained on the embeddings of the **full** 8,500-example dataset (Ch 2). The combinatorial pair-expansion (32 sentences → 1,280 contrastive pairs) is what makes this efficient.

SetFit also supports **zero-shot** by **synthesizing examples from label names** (e.g., labels *happy / sad* → synthetic data *"The example is happy"* / *"This example is sad"*).
