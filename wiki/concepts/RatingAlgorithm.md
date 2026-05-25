---
title: "Rating Algorithm"
type: concept
tags: [evaluation, ranking, methodology]
sources: [ai-engineering-ch03-evaluation-methodology]
last_updated: 2024-12-04
---

# Rating Algorithm

A **rating algorithm** converts pairwise match outcomes into a global ranking of competitors. Per [[ai-engineering-ch03-evaluation-methodology|*AI Engineering* Ch 3]]:

> "Comparative evaluation is new in AI but has been around for almost a century in other industries. It's especially popular in sports and video games. Many rating algorithms developed for these other domains can be adapted to evaluating AI models, such as Elo, Bradley–Terry, and TrueSkill."

## Three named algorithms

| Algorithm | Origin | Used by |
|---|---|---|
| [[EloRating\|Elo]] | Chess (Arpad Elo, 1960s) | [[ChatbotArena]] (originally) |
| [[BradleyTerry\|Bradley-Terry]] | Pairwise comparison statistics (1952) | [[ChatbotArena]] (after switching from Elo) |
| [[TrueSkill]] | Microsoft (Xbox Live, 2007) | Multi-team / multi-player games |

## How they work (Ch 3 framing)

> "Typically, this algorithm first computes a score for each model from the comparative signals and then ranks models by their scores."

The score-to-rank mapping is straightforward; the hard part is **inferring stable scores from limited and noisy pairwise outcomes**. Different algorithms have different assumptions:
- Elo: simple update-on-each-match rule, sensitive to evaluation order.
- Bradley-Terry: maximum-likelihood global fit, less order-sensitive.
- TrueSkill: Bayesian, supports multi-player and uncertainty estimates.

## The LMSYS switch

[[ChatbotArena|LMSYS Chatbot Arena]] originally used Elo. They switched to Bradley-Terry because *"they found Elo sensitive to the order of evaluators and prompts."* Even after switching, they cosmetically rescale Bradley-Terry scores (×400 + 1000, normalized so Llama-13b=800) to *"make them look like Elo scores."*

## Common assumption: transitivity

All three algorithms typically assume **[[TransitivityAssumption|transitivity]]** (A>B ∧ B>C ⇒ A>C) to avoid needing every pairwise comparison. *"However, it's unclear if this transitivity assumption holds for AI models"* (Ch 3, citing Boubdir et al.; Balduzzi et al.; Munos et al.).

## Connections

- [[ai-engineering-ch03-evaluation-methodology]] — primary source.
- [[EloRating]] / [[BradleyTerry]] / [[TrueSkill]] — the three named algorithms.
- [[ComparativeEvaluation]] — the parent paradigm.
- [[WinRate]] — the input signal.
- [[TransitivityAssumption]] — the shared simplification.
