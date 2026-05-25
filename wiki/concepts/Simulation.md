---
title: "Simulation"
type: concept
tags: [dataset-engineering, synthetic-data, robotics, self-driving]
sources: [ai-engineering-ch08-dataset-engineering]
last_updated: 2024-12-04
---

# Simulation

**Running virtual experiments to produce training data** — the traditional [[DataSynthesis|synthesis]] technique used when real-world data collection is expensive, dangerous, or impossible. Per [[ai-engineering-ch08-dataset-engineering|*AI Engineering* Ch 8]], simulation is one of the three traditional synthesis approaches, alongside [[RuleBasedDataSynthesis|rule-based]] and the modern [[AIPoweredDataSynthesis|AI-powered]].

## Canonical use cases

| Domain | Example |
|---|---|
| Self-driving | [[CARLA]], Waymo SimulationCity, [[Tesla|Tesla]] SF simulation |
| Robotics | Joint-movement simulation for tasks like pouring coffee |
| Game-bot training | [[OpenAIDota2\|OpenAI Dota 2]] (180 game-years/day); AlphaGo |
| Finance | Bankruptcy / IPO scenarios for market-impact training |
| Manufacturing | Defect / assembly-error simulation for anomaly detection |
| Climate science | Temperature / precipitation / extreme-weather variation |
| **Tool use** | Action-sequence simulation for AI agents (Ch 8) |

## Why simulations work for AI

> "Simulations allow you to run multiple experiments with minimal costs while avoiding accidents and physical damage."

For AI agents specifically, **simulations may uncover actions that humans overlook** — since AI's optimal tool-use patterns differ from human patterns (humans use UIs; AI uses APIs).

## Limitations

- Simulations are always **simplifications** of the real world.
- A robot that fails in simulation likely fails in the real world.
- A robot that succeeds in simulation may still fail in the real world.

## Sim2Real

A subfield specifically focused on **adapting algorithms trained in simulation to real-world deployment**. The wider the sim2real gap, the more transfer learning, domain randomization, and additional real-world fine-tuning are required.

## Self-play

A special form of simulation where **the AI generates its own data by playing against itself**:

- **[[OpenAIDota2|OpenAI Dota 2]]** — bot played ~180 years' worth of games per day.
- **AlphaGo / AlphaZero** — DeepMind simulated millions of Go games.

Self-play extends beyond games: have one agent simulate a customer with issues; another play the support agent. Have AIs negotiate against each other with different strategies. The output is training data for general agents.

## Connections

- [[DataSynthesis]] — parent concept.
- [[RuleBasedDataSynthesis]] / [[AIPoweredDataSynthesis]] — the other two traditional + modern synthesis approaches.
- [[Sim2Real]] — the subfield bridging simulation and reality.
- [[SelfPlay]] — a class of simulation where AI generates its own opponent.
- [[CARLA]] / [[OpenAIDota2]] — canonical examples.
- [[MonteCarloSimulation]] — adjacent simulation technique.
- [[ai-engineering-ch08-dataset-engineering]] — primary source.
