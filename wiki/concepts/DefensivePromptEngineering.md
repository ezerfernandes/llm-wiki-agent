---
title: "Defensive Prompt Engineering"
type: concept
tags: [prompt-engineering, llm-security, safety, defense]
sources: [ai-engineering-ch05-prompt-engineering]
last_updated: 2024-12-04
---

# Defensive Prompt Engineering

**The discipline of designing prompts and surrounding-system controls to resist [[PromptAttack|prompt attacks]] from malicious users and from poisoned tool outputs.** The second half of [[ai-engineering-ch05-prompt-engineering|*AI Engineering* Ch 5]].

> "Once your application is made available, it can be used by both intended users and malicious attackers who may try to exploit it." — Ch 5

## The three attack families

Ch 5 names three:

| Family | What it does |
|---|---|
| **[[PromptExtraction\|Prompt extraction]]** | Extract the application's prompts (including system prompt) to replicate or exploit the application. |
| **[[Jailbreak\|Jailbreaking]] and [[PromptInjection\|prompt injection]]** | Get the model to do bad things. |
| **[[InformationExtraction\|Information extraction]]** | Get the model to reveal training data or context. |

## Risk classes

The chapter enumerates concrete impact categories:

- **Remote code or tool execution** — attacker invokes unauthorized SQL queries, unauthorized emails, or arbitrary code via the model's tool use. Cited 2023 LangChain remote-code-execution vulnerability.
- **Data leaks** — extraction of private user/system data.
- **Social harms** — attackers extract knowledge about dangerous or criminal activities (weapon-making, tax evasion, exfiltration techniques).
- **Misinformation** — attackers manipulate the model to support an agenda.
- **Service interruption** — attackers cause the model to reject all queries (or accept queries it should reject).
- **Brand risk** — politically incorrect or offensive output (Google AI's "eat rocks" 2024; Microsoft Tay's racist comments 2016).

## Why the problem doesn't go away

Ch 5's core insight:

> "Prompt attacks are possible precisely because models are trained to follow instructions. As models get better at following instructions, they also get better at following malicious instructions."

And:

> "AI safety, like any area of cybersecurity, is an evolving cat-and-mouse game where developers continuously work to neutralize known threats while attackers devise new ones."

## Defense layers

| Layer | Where the work happens | Examples |
|---|---|---|
| **Model** | Post-training | [[InstructionHierarchy]] ([[WallaceEtAl2024]]) |
| **Prompt** | System-prompt authoring | "Write your system prompt assuming it will be public" |
| **Wrapper** | Application code | Input/output filters (PII, suspicious characters, fill-in-the-blank patterns) |
| **External** | Separate model/system | [[Guardrail\|Guardrails]] ([[LlamaGuard]], [[NeMoGuardrails]], [[GuardrailsAI]]) |
| **Tool boundary** | Tool layer | Sanitize tool outputs before returning to model |

## Paired robustness metrics

Ch 5 names **two metrics** for evaluating a system's robustness against prompt attacks — both must be tracked jointly:

- **[[ViolationRate|Violation rate]]** — percentage of successful attacks out of all attack attempts.
- **[[FalseRefusalRate|False refusal rate]]** — how often the model refuses safe queries.

A system that refuses every request has a violation rate of zero but is useless. The joint Pareto frontier defines a deployable safety posture.

## Practitioner-grade defense layers (expanded)

The Ch 5 defenses-supplemental section expands the layer table with concrete patterns at each level:

| Layer | Defenses (expanded) |
|---|---|
| **Model** | [[InstructionHierarchy]] (4-level: system > user > model output > tool output); [[BorderlineRequest|borderline-request]] safe-helpful training |
| **Prompt** | Explicit don't-do rules; [[PromptSandwich|prompt sandwich]]; pre-name known attack modes (DAN, grandma); inspect framework default templates |
| **System** | [[Isolation]] (VM sandbox for code execution); [[HumanInTheLoopApproval]] for impactful tool calls; [[OutOfScopeTopics]] filtering; [[InputGuardrail]] + [[OutputGuardrail]] paired; [[UsagePatternMonitoring]] for behavior-over-time anomaly detection |
| **Red-team tooling** | [[AzurePyRIT]] / [[GarakLLMScanner]] / [[GreshakeLLMSecurity]] / [[CHATSPersuasiveJailbreaker]]; benchmarks [[AdvBench]] / [[PromptRobustnessBenchmark]] |

## Connections

- [[ai-engineering-ch05-prompt-engineering]] — primary source.
- [[PromptAttack]] — the umbrella category.
- [[PromptExtraction]] / [[Jailbreak]] / [[PromptInjection]] / [[IndirectPromptInjection]] / [[InformationExtraction]] — the attack families.
- [[InstructionHierarchy]] — the load-bearing model-level defense.
- [[Guardrail]] / [[LlamaGuard]] / [[NeMoGuardrails]] / [[GuardrailsAI]] — wrapper / external defenses.
- [[InputGuardrail]] / [[OutputGuardrail]] / [[OutOfScopeTopics]] / [[Isolation]] / [[HumanInTheLoopApproval]] / [[UsagePatternMonitoring]] / [[PromptSandwich]] / [[BorderlineRequest]] — practitioner-grade defenses.
- [[ViolationRate]] / [[FalseRefusalRate]] / [[AttackSuccessRate]] — evaluation metrics.
- [[LLMRedTeaming]] / [[AzurePyRIT]] / [[GarakLLMScanner]] / [[GreshakeLLMSecurity]] / [[CHATSPersuasiveJailbreaker]] — red-team discipline and tooling.
- [[AdvBench]] / [[PromptRobustnessBenchmark]] — adversarial-robustness benchmarks.
- [[PromptEngineering]] — parent discipline.
