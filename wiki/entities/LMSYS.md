---
title: "LMSYS"
type: entity
tags: [organization, research, evaluation]
sources: [ai-engineering-ch02-foundation-models, ai-engineering-ch04-evaluate-ai-systems]
last_updated: 2024-12-04
---

# LMSYS

**Large Model Systems Organization** — an open research organization focused on large-language-model evaluation and serving infrastructure. Best known publicly for **Chatbot Arena** (the crowdsourced LLM-comparison platform).

## In [[ai-engineering-ch02-foundation-models|AI Engineering Ch 2]]

Ch 2 cites LMSYS (Chiang et al. 2024) for a specific data point on the human-labor cost of [[ComparisonData|comparison data]]:

> "LMSYS (the Large Model Systems Organization), an open research organization, found that manually comparing two responses took on average **three to five minutes**, as the process requires fact-checking each response."

## Why this matters

The 3–5 minute/comparison figure (with fact-checking) is the **floor cost on human-evaluated preference data**. It compounds with [[ThomasScialom|Thomas Scialom's]] ≈$3.50/comparison figure to give a concrete sense of why [[rlhf|RLHF]] is expensive at scale and why companies like [[meta|Meta]] have migrated to [[DPO|DPO]] (Llama 3) and others to AI-graded approaches like [[RLAIF]].

## Connections
- [[ComparisonData]] — the data format LMSYS measured the cost of.
- [[rlhf]] / [[PreferenceFinetuning]] — what the comparison data feeds.
- [[ai-engineering-ch02-foundation-models]] — primary source.
- [[ThomasScialom]] — peer cost data point.

## From [[ai-engineering-ch04-evaluate-ai-systems|AI Engineering Ch 4]]

Ch 4 surfaces two LMSYS data points beyond [[ChatbotArena]] itself:

1. **Million-conversation analysis** (Zheng et al. 2023) — analyzed 1M conversations from Vicuna demo and Chatbot Arena. Identifies **[[Roleplaying|roleplaying]] as the 8th most common use case**. Figure 4-4 in Ch 4.
2. **Chatbot Arena as a model-selection criterion** — used in the example evaluation criteria table (Table 4-3) where overall model quality is measured by Chatbot Arena Elo (> 1200 hard, > 1250 ideal). This is the canonical pattern for using a public leaderboard as one input to your own [[CustomLeaderboard|custom leaderboard]].
