---
title: "Self-Play"
type: concept
tags: [reinforcement-learning, simulation, training, game-bots]
sources: [ai-engineering-ch08-dataset-engineering]
last_updated: 2024-12-04
---

# Self-Play

**A training technique where an agent learns by playing against itself or other versions of itself.** Per [[ai-engineering-ch08-dataset-engineering|*AI Engineering* Ch 8]], self-play is a form of [[Simulation|simulation]]-driven data generation that lets AI agents generate their own training data at enormous scale.

## Canonical examples (Ch 8)

- **[[OpenAIDota2|OpenAI Dota 2]]** (2019) — the bot played approximately **180 years' worth of games every day** in simulation, learning to refine strategies by playing against itself.
- **AlphaGo / AlphaZero** ([[googledeepmind|DeepMind]]) — simulated millions of Go games to train [[alphazero|AlphaZero]] / AlphaGo. Self-play is the foundation of the AlphaGo family's training pipeline.

## Beyond games

Per Ch 8, self-play extends to general agents:

> "You can have AIs negotiate against each other using different strategies to see which one works better. You can have one version of the model play the role of a customer with issues and another play the customer support agent."

Use cases:

- **Tool-use training** — one agent plays the user; one plays the assistant; data is the assistant's tool calls and responses.
- **Adversarial training** — one agent plays the attacker; one plays the defender.
- **Negotiation training** — different strategies played head-to-head; the winning strategy's behavior becomes training data.

## Why self-play works

- **Scales infinitely** — no human data ceiling.
- **Discovers actions humans overlook** — AI can find efficient strategies that aren't intuitive to humans.
- **Adversarial co-evolution** — each version of the agent is challenged by a slightly better opponent (itself).

## Connections

- [[Simulation]] — parent technique.
- [[OpenAIDota2]] — the canonical large-scale example.
- [[alphazero|AlphaZero]] — DeepMind's self-play family.
- [[ReinforcementLearning]] — the learning paradigm self-play typically pairs with.
- [[DataSynthesis]] — self-play is one approach.
- [[ai-engineering-ch08-dataset-engineering]] — primary source.
