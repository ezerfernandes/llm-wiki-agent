---
title: "OpenAI Dota 2"
type: entity
tags: [project, openai, self-play, reinforcement-learning]
sources: [ai-engineering-ch08-dataset-engineering]
last_updated: 2024-12-04
---

# OpenAI Dota 2

[[openai|OpenAI]]'s 2019 project that trained a bot to play Dota 2 at top-human level — using **self-play in a simulator that enabled the bot to play approximately 180 years' worth of games every day**. Per [[ai-engineering-ch08-dataset-engineering|*AI Engineering* Ch 8]], this is the chapter's canonical example of [[SelfPlay|self-play]]-based data generation for [[ReinforcementLearning|reinforcement learning]].

## The headline numbers

- **180 game-years per day** of simulated training.
- Reached **top professional human level** in 5v5 Dota 2.
- Demonstrated that **AI can develop and refine strategies over time** through self-play alone.

## Why it's in Ch 8

The Dota 2 result is Huyen's evidence that **simulation can generate effectively unlimited training data** when the environment is well-defined. The same principle extends beyond games:

- Two AIs negotiating against each other with different strategies.
- One AI playing a frustrated customer; another playing the support agent.
- Adversarial pair training.

## Connections

- [[openai|OpenAI]] — the project's lab.
- [[SelfPlay]] — the technique exemplified.
- [[Simulation]] — parent technique.
- [[alphazero|AlphaZero]] — sibling self-play project (DeepMind, board games).
- [[ai-engineering-ch08-dataset-engineering]] — primary source.
