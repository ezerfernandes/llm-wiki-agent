---
title: "AlphaCode 2"
type: entity
tags: [agent, coding, google, deepmind]
sources: [2312.11805-gemini]
last_updated: 2026-05-10
---

# AlphaCode 2

[[GoogleDeepMind]]'s competitive-programming agent (Leblond et al., 2023), built on a [[Gemini]] Pro model fine-tuned on competitive-programming data. Performs massive search over the program space, then filtering / clustering / reranking using Gemini Pro as both proposal generator and reward model.

## Headline result (per [[2312.11805-gemini]])

- **43% solve rate on 77 Codeforces div-1/2 problems** drawn from 12 contests — a 1.7× improvement over the original AlphaCode (25%).
- Roughly **85th percentile** among Codeforces entrants. The original AlphaCode ranked around the 50th percentile.

## Position in the wiki

AlphaCode 2 is the canonical concrete example in the Gemini paper of *"compose a strong pre-trained model with search and tool use to obtain a more general agent."* The pattern recurs in the 2026 agentic-coding corpus — see [[2604.25067-frontier-coding-agents-c4]], [[2604.25850-agentic-harness-engineering]], [[2605.02396-heavyskill]] — where the bespoke search machinery of AlphaCode 2 is partially supplanted by general-purpose agentic harnesses around frontier base models.
