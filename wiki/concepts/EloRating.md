---
title: "Elo Rating"
type: concept
tags: [evaluation, ranking, rating-algorithm]
sources: [ai-engineering-ch03-evaluation-methodology, hands-on-llm-ch12-fine-tuning-generation-models]
last_updated: 2026-05-24
---

# Elo Rating

The **Elo rating system** (Arpad Elo, 1960s, originally for chess) is the most widely-recognized [[RatingAlgorithm|rating algorithm]] for pairwise competition. Per [[ai-engineering-ch03-evaluation-methodology|*AI Engineering* Ch 3]], Elo was the first algorithm used by [[ChatbotArena|LMSYS Chatbot Arena]] to rank LLMs.

## How it works (informal)

Each player has a numeric rating. After a match:
- The winner gains points; the loser loses points.
- The size of the swing depends on the **expected** outcome — beating a higher-rated opponent yields a bigger swing than beating a lower-rated one.
- A K-factor parameter controls the maximum per-match swing.

The chess convention starts new players at 1000 or 1200.

## Why LMSYS switched away

Ch 3: *"LMSYS's Chatbot Arena originally used Elo to compute models' ranking but later switched to the [[BradleyTerry|Bradley–Terry algorithm]] because they found Elo sensitive to the order of evaluators and prompts."*

This is a known property of Elo — the per-match update rule means **the order in which matches happen affects the final ratings**. In a fairly-mixed evaluation stream this is fine; in a streaming-leaderboard with model bursts and prompt clustering, it produces order-of-evaluation artifacts.

## The cosmetic re-scaling

Even after switching to Bradley-Terry, LMSYS continued *"referring to their model ratings 'Elo scores'"* for a while because users were familiar with the Elo scale. Per Ch 3 footnote: *"They scaled the resulting Bradley-Terry scores to make them look like Elo scores. The scaling is fairly complicated. Each score is multiplied by 400 (the scale used in Elo) and added to 1,000 (the initial Elo score). Then this score is rescaled so that the model Llama-13b has a score of 800."*

**Takeaway:** what is publicly displayed as an "Elo score" on Chatbot Arena since the switch is *not* a true Elo score — it's a Bradley-Terry score in Elo-style clothing. This is a wiki-flagged contradiction in nomenclature.

## Connections

- [[ai-engineering-ch03-evaluation-methodology]] — primary source.
- [[RatingAlgorithm]] — parent concept.
- [[BradleyTerry]] — the algorithm LMSYS switched to.
- [[TrueSkill]] — sibling rating algorithm (Microsoft / Xbox Live).
- [[ChatbotArena]] — the LLM leaderboard that originally used Elo.
- [[ComparativeEvaluation]] — parent paradigm.
- [[TransitivityAssumption]] — Elo assumes it like its siblings do.

## From [[hands-on-llm-ch12-fine-tuning-generation-models|Hands-On LLMs Ch 12]]

Ch 12 of *Hands-On LLMs* names Elo as the **rating system underneath [[ChatbotArena|Chatbot Arena]]'s 800,000+-vote leaderboard** and surfaces the chess analogy explicitly: *"if you have a low ranking but beat someone with a high ranking, then you would also receive a higher rank as a result."* The chapter elides the Elo → Bradley-Terry transition Ch 3 documents and refers throughout to "the Elo rating system" — matching how the leaderboard publicly presents its scores.
