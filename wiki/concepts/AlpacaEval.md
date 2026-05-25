---
title: "AlpacaEval"
type: concept
tags: [benchmark, evaluation, llm-as-judge, leaderboard]
sources: [ai-engineering-ch03-evaluation-methodology]
last_updated: 2024-12-04
---

# AlpacaEval

**AlpacaEval** (Dubois et al. 2023) is an [[LLMAsAJudge|AI-as-judge]]-based leaderboard for instruction-following LLMs that achieves remarkable correlation with human preferences. Per [[ai-engineering-ch03-evaluation-methodology|*AI Engineering* Ch 3]]:

> "AlpacaEval authors (Dubois et al., 2023) also found that their AI judges have a near perfect (0.98) correlation with LMSYS's Chat Arena leaderboard, which is evaluated by humans."

## The 0.98 correlation result

This is one of the strongest empirical data points in Ch 3 for AI-as-judge credibility:
- [[ChatbotArena|Chatbot Arena]] is human-evaluated.
- AlpacaEval is AI-judge-evaluated.
- Their rankings correlate at **0.98** — nearly identical.

If you trust Chatbot Arena, the correlation says you can trust AlpacaEval at a fraction of the cost and turnaround time.

## Position

Sibling to [[MTBench]] (Zheng et al. 2023, fixed 80 questions, 8 categories) and [[ChatbotArena]] (open prompts, crowdsourced). AlpacaEval offers an automated AI-judge alternative that can be re-run on new models without waiting for crowdsourced votes — making it the **fast-iteration leaderboard** of the three.

## Caveats

- The 0.98 correlation is over the ranked set of models tested at the time of Dubois et al. 2023. New models, new prompt distributions, or new judge models can shift this.
- AlpacaEval inherits all [[LLMAsAJudge|AI-as-judge]] biases ([[SelfBiasJudge]], [[FirstPositionBias]], [[VerbosityBias]]) — though apparently in a way that aggregates back to a Chatbot-Arena-like ordering.

## Connections

- [[ai-engineering-ch03-evaluation-methodology]] — primary source.
- [[LLMAsAJudge]] — the methodology.
- [[ChatbotArena]] / [[MTBench]] — sibling leaderboards.
- [[ComparativeEvaluation]] — parent paradigm.
- [[SelfBiasJudge]] / [[FirstPositionBias]] / [[VerbosityBias]] — inherited biases.
