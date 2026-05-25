---
title: "LLM Red Teaming"
type: concept
tags: [llm-security, defense, evaluation, red-team]
sources: [ai-engineering-ch05-prompt-engineering]
last_updated: 2024-12-04
---

# LLM Red Teaming

**The application of security-red-team discipline — adversarial probing and attack invention — to LLM applications.** Named in [[ai-engineering-ch05-prompt-engineering|*AI Engineering* Ch 5]] as the source of the empirical data that informs every layer of [[DefensivePromptEngineering|defensive prompt engineering]].

> "Many organizations have a security red team that comes up with new attacks so that they can make their systems safe against them. Microsoft has a great write-up on how to plan red teaming for LLMs." — Ch 5

The [[microsoft|Microsoft]] red-teaming write-up Ch 5 cites is the canonical practitioner reference for planning and running LLM red-team exercises.

## What it produces

> "Learnings from red teaming will help devise the right defense mechanisms." — Ch 5

Red-teaming outputs feed into:

- **Model-level defenses** — new attack categories added to instruction-hierarchy training data ([[InstructionHierarchy]] / [[WallaceEtAl2024]]).
- **Prompt-level defenses** — system prompts updated to preempt newly-discovered attack modes by name.
- **System-level defenses** — new patterns added to [[InputGuardrail|input guardrail]] and [[OutputGuardrail|output guardrail]] catalogs; [[UsagePatternMonitoring|usage-pattern monitoring]] rules updated.
- **Benchmarks** — newly-discovered attacks added to [[AdvBench]], [[PromptRobustnessBenchmark|PromptRobust]], [[JailbreakBench]] for future regression testing.

## Manual vs automated red teaming

Ch 5 distinguishes manual red-teaming (humans inventing attacks) from automated red-teaming tools:

| Tool | What it does |
|---|---|
| [[AzurePyRIT]] | Microsoft's Python Risk Identification Toolkit for LLMs. |
| [[GarakLLMScanner]] | `leondz/garak` — open-source LLM vulnerability scanner. |
| [[GreshakeLLMSecurity]] | `greshake/llm-security` — security tooling from the Indirect Prompt Injection author. |
| [[CHATSPersuasiveJailbreaker]] | `CHATS-lab/persuasive_jailbreaker` — automated jailbreaking via persuasive-rhetoric attacks. |

These tools maintain templates of known attacks and run them against target models automatically, surfacing regressions and quantifying [[ViolationRate|violation rate]] / [[AttackSuccessRate|ASR]].

## The cat-and-mouse framing

> "AI safety, like any area of cybersecurity, is an evolving cat-and-mouse game where developers continuously work to neutralize known threats while attackers devise new ones." — Ch 5

Red teaming is the structural answer to that game on the defender side — institutionalizing the invention of new attacks so that the defender, not the attacker, is the one who finds them first.

## Connections

- [[ai-engineering-ch05-prompt-engineering]] — primary source.
- [[DefensivePromptEngineering]] — parent discipline.
- [[microsoft|Microsoft]] — author of the canonical LLM red-teaming write-up.
- [[AzurePyRIT]] / [[GarakLLMScanner]] / [[GreshakeLLMSecurity]] / [[CHATSPersuasiveJailbreaker]] — automated red-team tooling.
- [[AdvBench]] / [[PromptRobustnessBenchmark]] / [[JailbreakBench]] — benchmarks downstream of red-team learnings.
- [[ViolationRate]] / [[AttackSuccessRate]] / [[FalseRefusalRate]] — metrics quantifying red-team output.
- [[InstructionHierarchy]] — the model-level defense whose training data is shaped by red-team findings.
