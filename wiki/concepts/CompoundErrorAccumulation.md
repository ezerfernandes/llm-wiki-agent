---
title: "Compound Error Accumulation"
type: concept
tags: [agents, reliability, evaluation]
sources: [ai-engineering-ch06-rag-agents, hands-on-llm-ch07-advanced-text-generation]
last_updated: 2026-05-23
---

# Compound Error Accumulation

**Compound error accumulation** is the agent-reliability phenomenon that **multi-step agent accuracy decays geometrically** as the step count grows. Named in [[ai-engineering-ch06-rag-agents|*AI Engineering* Ch 6]] as one of the two structural reasons agents need more powerful models than non-agent applications.

## The math

If per-step accuracy is `p`, then the probability of reaching the goal after `n` steps is `p^n`:

| Per-step accuracy | After 10 steps | After 100 steps |
|---|---|---|
| 95% | 60% | 0.6% |
| 99% | 90% | 37% |
| 99.9% | 99% | 90.5% |

Per Huyen: *"If the model's accuracy is 95% per step, over 10 steps, the accuracy will drop to 60%, and over 100 steps, the accuracy will be only 0.6%."*

## Why this matters

- **Per-step accuracy is the *only* thing that scales the system**. A linear increase in per-step accuracy is an exponential increase in end-to-end accuracy.
- **Long-horizon agents need frontier models**. 95%/step models work for 1–3-step pipelines but fall off cliffs at horizon 10+.
- **Step-count compression is a force multiplier**. Reducing a 20-step plan to a 5-step plan can be a more leveraged optimization than improving the model.
- **Reflection helps because it catches per-step errors before they propagate** — see [[react|ReAct]] and [[reflexion|Reflexion]].

## The complementary risk

Compound mistakes are one of two reasons Huyen names for agents needing more powerful models. The other is **higher stakes**: *"with access to tools, agents are capable of performing more impactful tasks, but any failure could have more severe consequences."* (see [[WriteAction]]).

## Connections

- [[Agent]] — the system whose accuracy decays this way.
- [[Planning]] — the subsystem whose plan length directly drives n.
- [[react|ReAct]] / [[reflexion|Reflexion]] — reflection-based mitigations.
- [[longhorizontasks]] — the task family most affected.
- [[WriteAction]] — the "higher stakes" sibling risk.
- [[AgentEfficiency]] — the evaluation axis that measures step count.
- [[ai-engineering-ch06-rag-agents]] — primary source.
- [[hands-on-llm-ch07-advanced-text-generation]] — Ch 7's worked agent illustrates the capability cliff (Phi-3-mini insufficient; GPT-3.5 required).

## From [[hands-on-llm-ch07-advanced-text-generation|Hands-On LLMs Ch 7]]

Ch 7 doesn't name *"compound error accumulation"* explicitly but **operationalizes the failure mode** it describes. The chapter switches from local [[Phi3Mini|Phi-3-mini]] (used for chains and memory) to [[ChatGPT|GPT-3.5-turbo]] for the [[LangChainAgent|ReAct agent]] example, with the candid framing:

> *"These autonomous processes generally require an LLM that is powerful enough to properly follow complex instructions. The LLM that we used thus far is relatively small and not sufficient to run these examples."* — Ch 7

This is the **agent-capability cliff** the math on this page predicts: per-step accuracy that's adequate for a single classification or generation call (say 90%) becomes catastrophically inadequate for a 2-cycle ReAct trajectory (0.9² = 81%) — and the chapter's worked example *requires* a 2-cycle trajectory (search → calculate). The chapter's parting safety caveat — *"there is no [[humanintheloop|human in the loop]] to judge the quality of the output or reasoning process. This double-edged sword requires a careful system design to improve its reliability"* — is the same risk argument this page makes, surfaced as deployment caution rather than capability math.
