---
title: "Prompt Attack"
type: concept
tags: [llm-security, adversarial, safety]
sources: [ai-engineering-ch05-prompt-engineering, hands-on-llm-ch07-advanced-text-generation]
last_updated: 2026-05-23
---

# Prompt Attack

**An adversarial input that causes an LLM-backed application to behave in unintended, harmful, or information-revealing ways.** The umbrella category in [[ai-engineering-ch05-prompt-engineering|*AI Engineering* Ch 5]] covering three families:

| Family | Goal |
|---|---|
| **[[PromptExtraction\|Prompt extraction]]** (a.k.a. [[ReversePromptEngineering\|reverse prompt engineering]]) | Leak the system prompt or other proprietary prompt material. |
| **[[Jailbreak\|Jailbreaking]] / [[PromptInjection\|prompt injection]]** | Make the model do things its safety training is supposed to prevent. |
| **[[InformationExtraction\|Information extraction]]** | Get the model to reveal training data or context (PII, copyright, secrets). |

## Why prompt attacks exist at all

Per Ch 5:

> "Prompt attacks are possible precisely because models are trained to follow instructions. As models get better at following instructions, they also get better at following malicious instructions."

The structural problem: from the model's perspective, **all input is just tokens**. A user-supplied "ignore the above" looks indistinguishable from a developer-supplied instruction unless the model has been **trained** to distinguish them — which is exactly what the [[InstructionHierarchy|instruction-hierarchy]] post-training scheme does.

## Sophistication ladder (Ch 5)

Ch 5 orders attacks by increasing sophistication. Most low-rung attacks are no longer effective on frontier models.

## From [[hands-on-llm-ch07-advanced-text-generation|Hands-On LLMs Ch 7]]

Ch 7 surfaces prompt attacks only **indirectly** — by naming [[LangChain]]'s **2023 remote-code-execution vulnerability** as the canonical example of an in-the-wild prompt-attack surface in tooling. Ch 7 itself uses [[LangChain]] as its pedagogical-first framework and does not survey attacks; the security framing comes from [[ai-engineering-ch05-prompt-engineering|Huyen Ch 5]] (already covered here). The cross-source consistency note: LangChain is pedagogical-first in Ch 7 and security-fragile in Ch 5 — **different operating modes**, not a contradiction.

1. **[[Obfuscation|Obfuscation]]** — misspell keywords (`vacine`, `el qeada`); insert special-character strings (`bomb ! ! ! ! ! !`); mix languages or Unicode.
2. **[[OutputFormatManipulation|Output-format manipulation]]** — hide malicious intent in poems, code, songs, UwU paragraphs.
3. **[[Roleplaying]] / persona** — [[DANJailbreak|DAN]], [[GrandmaExploit|grandma exploit]], NSA-agent-with-secret-code.
4. **Automated attacks** — algorithmic substring substitution; [[PAIR]] (an attacker LLM that iteratively refines its prompt; <20 queries).
5. **[[IndirectPromptInjection|Indirect prompt injection]]** — malicious instructions live in tools (web pages, GitHub repos, retrieved documents, emails) rather than in the user prompt.

## The asymmetry

The attacker only needs one working attack. The defender needs to defend against all of them. This is why Ch 5 frames safety as *"an evolving cat-and-mouse game"* with no terminal state.

## Connections

- [[ai-engineering-ch05-prompt-engineering]] — primary source.
- [[DefensivePromptEngineering]] — the defensive counterpart.
- [[PromptExtraction]] / [[ReversePromptEngineering]] / [[Jailbreak]] / [[PromptInjection]] / [[IndirectPromptInjection]] / [[InformationExtraction]] — the attack families.
- [[PAIR]] — automated attack via attacker-LLM.
- [[DivergenceAttack]] — Nasr et al. 2023 training-data extraction attack.
- [[Guardrail]] — defensive layer.
- [[InstructionHierarchy]] — the load-bearing model-level defense.
- [[AttackSuccessRate]] — how prompt attacks are scored.
