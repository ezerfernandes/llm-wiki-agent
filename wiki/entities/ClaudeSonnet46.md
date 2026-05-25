---
title: "Claude Sonnet 4.6"
type: entity
tags: [model, anthropic, claude, judge]
sources: [2604.14585-prompt-optimization-coin-flip]
last_updated: 2026-05-22
---

# Claude Sonnet 4.6

[[anthropic|Anthropic]]'s mid-flagship-tier model in the Claude 4 family. Used as the **judge model** for free-form output scoring in [[2604.14585-prompt-optimization-coin-flip]].

The choice of a higher-tier model (Sonnet 4.6) to evaluate outputs from mid-tier ([[ClaudeHaiku45|Haiku 4.5]]) and budget-tier ([[AmazonNovaLite|Nova Lite]]) executors follows the standard LLM-as-a-judge protocol — using a stronger model to score outputs of weaker ones to minimize bias toward the executor's own writing style.

Surfaces elsewhere in the wiki via [[2605.10698-bystander-effect-mas|Shehata & Li 2026]]'s "Fortified Mind" finding — Claude Sonnet 4.6 was the lone model in that audit to resist the bystander-effect / cognitive-loafing collapse under simulated peer consensus.

## Connections
- [[anthropic]] — developer.
- [[claudeopus47|Claude Opus 4.7]] / [[claudeopus46|Claude Opus 4.6]] — flagship siblings.
- [[ClaudeHaiku45]] — mid-tier sibling; the executor model in the coin-flip study.
- [[2604.14585-prompt-optimization-coin-flip]] — judge model use.
- [[2605.10698-bystander-effect-mas]] — "Fortified Mind" — resists multi-agent cognitive loafing.
