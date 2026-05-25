---
title: "Convai"
type: entity
tags: [company, startup, npc, conversational-ai, gaming]
sources: [ai-engineering-ch01-intro, ai-engineering-ch04-evaluate-ai-systems]
last_updated: 2024-12-04
---

# Convai

Startup building AI-powered 3D conversational characters (smart NPCs — non-player characters) for games and immersive experiences. [[ChipHuyen|Chip Huyen]] discloses in [[ai-engineering-ch01-intro|*AI Engineering* Ch 1]] that she is an advisor to Convai. Highlighted alongside [[Inworld]] (the peer in the same category) as the canonical examples of [[AIInterface|3D/embodied AI interfaces]] — a third category beyond text chat and voice assistants.

## In Ch 1

- **3D-conversational use case**: 3D NPCs are essential to advancing storylines in many games; classical NPCs are scripted with limited dialogue. Convai/Inworld-style smart NPCs change the dynamics of games like *The Sims* and *Skyrim* and enable new game genres.
- **NVIDIA demos**: Huyen cites NVIDIA's public demos of Inworld and Convai as the canonical industry surfacing of the 3D-NPC pattern.

## Connections

- [[ChipHuyen]] — advisor (disclosed).
- [[Inworld]] — peer in the 3D-NPC category.
- [[NVIDIA]] — demo partner.
- [[AIInterface]] — 3D/embodied interface category.
- [[FoundationModelUseCases]] — conversational bots use case.
- [[ai-engineering-ch01-intro]] — Ch 1 source.

## From [[ai-engineering-ch04-evaluate-ai-systems|AI Engineering Ch 4]]

Ch 4 returns to Convai as a **build-vs-buy case study for over-censoring**:

> "A company I advise, Convai, builds 3D AI characters that can interact in 3D environments, including picking up objects. When working with commercial models, they ran into an issue where the models kept responding: 'As an AI model, I don't have physical abilities'. Convai ended up finetuning open source models."

This is one of Ch 4's clearest examples of **commercial-model safety guardrails being the deal-breaker** that drives a company to open-source alternatives. It's also a worked example of [[Roleplaying|roleplaying]] capability needs — NPCs need to *be* the character, not lecture about being an AI.
