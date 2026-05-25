---
title: "Isolation"
type: concept
tags: [llm-security, defense, system-design, sandboxing]
sources: [ai-engineering-ch05-prompt-engineering]
last_updated: 2024-12-04
---

# Isolation

**A system-level defense in which model-generated code or tool invocations are executed in an environment separated from the user's main machine** — typically a virtual machine or container. Named in [[ai-engineering-ch05-prompt-engineering|*AI Engineering* Ch 5]] as one of the most important practical defenses for any LLM application that executes generated code.

> "If your system involves executing generated code, execute this code only in a virtual machine separated from the user's main machine. This isolation helps protect against untrusted code. For example, if the generated code contains instructions to install malware, the malware would be limited to the virtual machine." — Ch 5

## Why it matters

Code-execution attack surfaces compound: a successful [[PromptInjection|prompt injection]] or [[IndirectPromptInjection|indirect prompt injection]] that flows into a code-execution tool can run arbitrary commands. Without isolation, the attacker effectively gains the privilege level of the process running the LLM application — which on a developer's machine is often *the developer's full user account*.

Ch 5's [[Jailbreak]] / [[PromptAttack|prompt-attack]] risk-class enumeration explicitly names **remote code or tool execution** as a top-tier impact category; isolation is the structural mitigation.

## Implementation patterns

- **Containerized execution** — Docker, Firecracker, gVisor.
- **Per-session VMs** — fresh VM per user session, destroyed after use.
- **Network egress restrictions** — block outbound calls from the sandbox.
- **Filesystem restrictions** — read-only root, scratch workspace only.
- **No shared secrets** — credentials never present in the sandbox.

## Beyond code execution

Isolation generalizes to any **side-effectful tool** the model can call: database connections (use read-only credentials in the model's tool layer), email-send tools (gate behind [[HumanInTheLoopApproval|human approval]] for impactful actions), API keys (scoped credentials per session).

## Connections

- [[ai-engineering-ch05-prompt-engineering]] — primary source.
- [[DefensivePromptEngineering]] — parent discipline.
- [[HumanInTheLoopApproval]] — complementary system-level defense for non-isolated side-effectful tools.
- [[PromptInjection]] / [[IndirectPromptInjection]] — the attacks isolation contains.
- [[Agent]] — agentic systems with code-execution tools are the primary deployment pattern that needs this.
- [[CodeAttack]] — adversarial-code-generation attack family that isolation contains.
