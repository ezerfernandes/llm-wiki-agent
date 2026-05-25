---
title: "MT-Bench"
type: concept
tags: [benchmark, evaluation, llm-as-judge]
sources: [ai-engineering-ch03-evaluation-methodology]
last_updated: 2024-12-04
---

# MT-Bench

**MT-Bench** (Zheng et al. 2023, *"Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena"*) is a multi-turn benchmark for evaluating LLMs that pioneered the **AI-as-judge agreement-with-humans** measurement. Per [[ai-engineering-ch03-evaluation-methodology|*AI Engineering* Ch 3]]:

> "In 2023, Zheng et al. found that on their evaluation benchmark, MT-Bench, the agreement between GPT-4 and humans reached 85%, which is even higher than the agreement among humans (81%)."

## Why MT-Bench matters

MT-Bench is the **load-bearing empirical citation** for [[LLMAsAJudge|AI-as-judge]] credibility in Ch 3:
- GPT-4's 85% agreement with humans is **higher than human-human agreement (81%)**.
- This suggests AI judges can be at least as reliable as human judges — at least on the MT-Bench distribution.

## What MT-Bench tests

80 multi-turn questions spanning 8 categories: writing, roleplay, extraction, reasoning, math, coding, STEM knowledge, and humanities/social-science knowledge. Each model produces multi-turn responses; the AI judge scores them on a 10-point rubric.

## Caveat from the same paper

Ch 3 notes that *"including evaluation examples in the prompt can increase the consistency of GPT-4 from 65% to 77.5%. However, they acknowledged that high consistency may not imply high accuracy — the judge might consistently make the same mistakes."* The high agreement number must be read as **agreement with the human distribution**, not as ground-truth correctness.

## Position

Sibling benchmark to [[AlpacaEval]] (which has 0.98 correlation with [[ChatbotArena]]) and [[ChatbotArena]] itself. MT-Bench differs from Arena in being **fixed-prompt** (80 questions) rather than open-prompt, making it more reproducible at the cost of less prompt diversity.

## Connections

- [[ai-engineering-ch03-evaluation-methodology]] — primary source.
- [[LLMAsAJudge]] — what MT-Bench evaluates (and is evaluated by).
- [[ChatbotArena]] / [[AlpacaEval]] — sibling leaderboards.
- [[Evaluation]] — parent discipline.
- [[ComparativeEvaluation]] — methodological framing.
