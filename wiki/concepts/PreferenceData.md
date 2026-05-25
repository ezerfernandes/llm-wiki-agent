---
title: "Preference Data"
type: concept
tags: [data, preference-alignment, rlhf, dpo, training-data, hands-on-llm]
sources: [hands-on-llm-ch12-fine-tuning-generation-models]
last_updated: 2026-05-23
---

# Preference Data

**Preference data** is the dataset shape used to train a [[RewardModel|reward model]] (for [[rlhf|RLHF]] / [[PPO|PPO]]) or to directly fine-tune an LLM via [[DPO]] / [[ORPO]] / similar reference-free methods. Each example is a tuple of (prompt, chosen completion, rejected completion) — the model is trained to **prefer chosen over rejected**.

## Ch 12's framing

[[hands-on-llm-ch12-fine-tuning-generation-models|Ch 12]] introduces preference data via Figure 12-27:

> *"One common shape for preference datasets is for a training example to have a prompt, with one accepted generation and one rejected generation."* — Ch 12

And the important nuance:

> *"It's not always a good versus bad generation; it can be that the two generations are both good, but one is better than the other."* — Ch 12

## How it's collected (Ch 12)

> *"One way to generate preference data is to present a prompt to the LLM and have it generate two different generations ... we can ask human labelers which of the two they prefer."* — Ch 12

Alternative collection paths discussed elsewhere in the wiki:
- **LLM-as-judge synthesis** — have a strong model (e.g., GPT-4) produce both completions and score them. The chapter's worked DPO dataset (`argilla/distilabel-intel-orca-dpo-pairs`) was generated this way *"in part by ChatGPT with scores on which output should be accepted and which rejected."*
- **Pairwise human comparison via [[ChatbotArena]]** — the same Elo-style pairwise voting that powers the Chatbot Arena leaderboard can yield (chosen, rejected) pairs over many prompts.

## Schema in Ch 12's DPO run

The chapter's `format_prompt` function normalizes preference data into the exact schema [[DPOTrainer]] expects:

```python
return {
    "prompt": system + prompt,    # <|system|>...<|user|>...<|assistant|>
    "chosen": chosen + "</s>\n",
    "rejected": rejected + "</s>\n",
}
```

A filter on the worked dataset reduces ~13,000 raw examples to ~6,000 by dropping ties, requiring `chosen_score >= 8`, and excluding GSM8k-train overlap.

## Connections

- [[ComparisonData]] — the wiki's canonical name for the (prompt, winning, losing) triplet shape; preference data and comparison data are often used interchangeably.
- [[RewardModel]] — the model trained on preference data for RLHF.
- [[DPO]] / [[ORPO]] — algorithms that consume preference data without training a separate reward model.
- [[PreferenceFinetuning]] — the regime that uses this data.
- [[DistilabelIntelOrcaDPOPairs]] — Ch 12's worked DPO dataset.
- [[UltraChat]] — Ch 12's SFT dataset (instruction data — not preference data).
- [[hands-on-llm-ch12-fine-tuning-generation-models]] — primary source.
- [[ai-engineering-ch02-foundation-models]] — Huyen's comparison-data deep-dive (cost figures, labeler-agreement numbers).
