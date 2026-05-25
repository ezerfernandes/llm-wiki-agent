---
title: "Chatbot Arena"
type: concept
tags: [benchmark, leaderboard, evaluation, comparative-evaluation]
sources: [ai-engineering-ch03-evaluation-methodology, ai-engineering-ch04-evaluate-ai-systems, hands-on-llm-ch12-fine-tuning-generation-models]
last_updated: 2026-05-24
---

# Chatbot Arena

**Chatbot Arena** is [[LMSYS]]'s crowdsourced LLM-comparison leaderboard — the dominant public ranking of frontier LLMs by [[ComparativeEvaluation|pairwise human preference]]. Per [[ai-engineering-ch03-evaluation-methodology|*AI Engineering* Ch 3]]:

> "Anyone can go to the website, enter a prompt, get back two responses from two anonymous models, and vote for the better one. Only after voting is done are the model names revealed."

## The pipeline

1. User submits a prompt.
2. Two anonymous models respond.
3. User votes (Model A wins / Model B wins / Tie / Both bad).
4. Vote contributes to the [[WinRate|win-rate]] estimate between the two models.
5. A [[RatingAlgorithm|rating algorithm]] converts win rates into a global ranking.

## The Elo→Bradley-Terry switch

Originally used [[EloRating|Elo]]; switched to [[BradleyTerry|Bradley-Terry]] because *"they found Elo sensitive to the order of evaluators and prompts."* For a while, Bradley-Terry scores were cosmetically scaled to "look like Elo scores" — multiply by 400, add 1000, normalize so Llama-13b = 800. **What Chatbot Arena currently displays as an "Elo score" is actually a rescaled Bradley-Terry strength.**

## Scale

- **57 models** (Jan 2024) ranked using **244,000 comparisons** — averaging ≈153 comparisons per pair across 1,596 pairs.
- Built on the [[TransitivityAssumption|transitivity assumption]] to infer rankings without exhaustive pairwise comparison.

## Quality-control issues

Ch 3 flags substantial signal-quality problems with crowdsourced prompts:
- **Trivially easy prompts dominate** — 180 of 33,000 LMSYS prompts in 2023 were "hello"/"hi" variants (0.55%); the brainteaser *"X has 3 sisters, each has a brother. How many brothers does X have?"* was asked 44 times.
- **No fact-checking** — voters might prefer responses that sound better but are factually wrong.
- **Malicious votes** — some users intentionally prefer toxic responses.
- **No real-world grounding** — prompts don't reflect production usage; users default to whatever comes to mind first.

LMSYS mitigates by filtering out easy prompts and ranking only on hard prompts. Some teams ([[ScaleAI|Scale]]) prefer a **trained-evaluator** private leaderboard despite the much smaller comparison count.

## Position in the wiki

The wiki's first concept-page anchor for Chatbot Arena. Where the [[LMSYS]] entity page surfaces LMSYS's role across the FM ecosystem (comparison-data labor cost, etc.), this page anchors *the specific leaderboard product*.

## Strong agreement with AI judges

Ch 3 cites Dubois et al. (2023): [[AlpacaEval]] has **0.98 correlation** with Chatbot Arena's ranking. This is one of the chapter's strongest data points for [[LLMAsAJudge|AI-as-judge]] credibility.

## Connections

- [[ai-engineering-ch03-evaluation-methodology]] — primary source.
- [[LMSYS]] — host organization.
- [[ComparativeEvaluation]] — methodology.
- [[EloRating]] / [[BradleyTerry]] — rating algorithms (history + present).
- [[WinRate]] — the input signal.
- [[TransitivityAssumption]] — load-bearing assumption.
- [[AlpacaEval]] / [[MTBench]] — AI-judged siblings with strong correlation to Arena.
- [[ChipHuyen]] — author who flags the quality-control issues.

## From [[ai-engineering-ch04-evaluate-ai-systems|AI Engineering Ch 4]]

Ch 4 names Chatbot Arena as a **soft model-selection signal**. The example evaluation criteria table (Table 4-3) uses Elo > 1200 as the hard requirement for overall model quality, > 1250 as the ideal:

| Criterion | Metric | Benchmark | Hard | Ideal |
|---|---|---|---|---|
| Overall model quality | Elo score | Chatbot Arena ranking | > 1200 | > 1250 |

This is the canonical example of how to **use a public leaderboard as one input to a [[CustomLeaderboard|custom leaderboard]]** without taking it as the whole answer.

## From [[hands-on-llm-ch12-fine-tuning-generation-models|Hands-On LLMs Ch 12]]

Ch 12 of *Hands-On LLMs* names Chatbot Arena (Chiang et al. 2024, arXiv:2403.04132) as the **canonical crowdsourced-human-evaluation leaderboard** for generative LLMs — the human-eval tier above LLM-as-judge in the chapter's evaluation taxonomy. Headline scale Ch 12 surfaces: **800,000+ votes** used to compute the leaderboard via the [[EloRating|Elo rating]] system (chess analogy: low-ranked beats high-ranked → big ranking change).

### Position in the eval taxonomy

Ch 12 places Chatbot Arena at the **top of its evaluation tier hierarchy**:

1. Word-level metrics ([[Perplexity]] / [[ROUGE]] / [[bleu|BLEU]] / [[BERTScore]]) — fastest, weakest signal.
2. Public benchmarks ([[MMLU]] / [[GSM8K]] / [[HellaSwag]] / [[TruthfulQA]] / [[HumanEval]] / [[GLUE]]) — broader coverage, leaderboard-overfit risk.
3. Leaderboards ([[OpenLLMLeaderboard]]) — multi-benchmark aggregation.
4. **LLM-as-a-judge** ([[LLMAsAJudge]]) — automated proxy for human eval.
5. **Human evaluation via Chatbot Arena** — *"the gold standard"*.

> *"Even if an LLM scores well on broad benchmarks, it still might not score well on domain-specific tasks. Moreover, benchmarks do not fully capture human preference and all methods discussed before are merely proxies for that."* — Ch 12

The author-personal-evaluation framing Ch 12 codifies: Jay Alammar tests new models with Arabic prompts; Maarten Grootendorst tests with Dutch — *"you are the best evaluator."*
