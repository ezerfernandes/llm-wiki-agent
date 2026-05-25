---
title: "Actor-Critic Agent"
type: concept
tags: [reinforcement-learning, agents, reflection]
sources: [ai-engineering-ch06-rag-agents]
last_updated: 2024-12-04
---

# Actor-Critic Agent

**Actor-critic** (Konda & Tsitsiklis 1999) is the reinforcement-learning agent architecture in which **one component proposes actions (the actor)** and **another component evaluates them (the critic)**. Named in [[ai-engineering-ch06-rag-agents|*AI Engineering* Ch 6]] as the RL ancestor of the modern LLM **actor-evaluator reflection pattern** that powers [[react|ReAct]] and [[reflexion|Reflexion]].

## Why Huyen mentions it

In a footnote to the multi-agent reflection discussion:

> *"This reminds me of the actor-critic (AC) agent method (Konda and Tsitsiklis, 1999) in reinforcement learning."*

The structural correspondence is exact:

| Component | RL actor-critic | LLM reflection |
|---|---|---|
| **Actor** | Policy network — proposes next action | LLM — proposes next action / tool call |
| **Critic** | Value network — estimates state value | LLM judge / scorer — evaluates outcome |

In RL, the critic's value estimate is the gradient signal used to train the actor. In LLM agents, the critic's verbal evaluation is the *prompt-time* signal used to revise the actor's next action ([[reflexion|Reflexion]]'s *"verbal reinforcement learning"*).

## Position in the FM vs RL agents debate

Huyen contrasts FM-agent and RL-agent planning in a Ch 6 sidebar:

- **RL agent**: planner trained by an RL algorithm — high training cost, expensive to retrain.
- **FM agent**: model *is* the planner — promptable or finetunable; cheaper.

But she predicts convergence:

> *"There's nothing to prevent an FM agent from incorporating RL algorithms to improve its performance. I suspect that in the long run, FM agents and RL agents will merge."*

Actor-critic is the *structural* substrate that already enables this merge: prompted LLMs can play either role, and RL training can be added on top of the same architectural skeleton.

## Connections

- [[Agent]] — the parent abstraction.
- [[react|ReAct]] / [[reflexion|Reflexion]] — modern LLM realizations of the actor-evaluator pattern.
- [[ReinforcementLearning]] — the parent RL field.
- [[SelfCritique]] — the LLM-side mechanism.
- [[Planning]] — the agent subsystem the actor populates.
- [[ai-engineering-ch06-rag-agents]] — primary source.
