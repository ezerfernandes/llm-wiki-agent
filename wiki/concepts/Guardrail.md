---
title: "Guardrail"
type: concept
tags: [llm-security, safety, defense]
sources: [dspy-guardrails, ai-engineering-ch05-prompt-engineering, ai-engineering-ch10-architecture-feedback]
last_updated: 2024-12-04
---

# Guardrail

A **guardrail** is a defensive layer around an LLM that detects, blocks, or rewrites inputs and outputs to prevent unsafe behavior. Guardrails sit between the user and the model (input-side) and between the model and the user (output-side), filtering for harmful content, [[Jailbreak|jailbreaks]], PII leakage, format violations, hallucinated facts, and policy violations.

## Taxonomy of guardrails

| Layer | Approach | Examples |
|---|---|---|
| **Trained classifier** | Supervised model judges safety | [[LlamaGuard]] (Inan et al. 2023, [[meta|Meta]]) |
| **Rule-based dialog flow** | Hand-written conversational state machine | [[NeMoGuardrails]] ([[Colang]] DSL, [[NVIDIA]]) |
| **Output validator** | Pydantic-style schema + correctness checks | [[GuardrailsAI]] (Rajpal 2023) |
| **Optimized prompt program** | Auto-tuned [[DSPy]] program | [[DSPyGuardrails]] (Yu & He 2024) |
| **External sound critic** | Separate verifier outside the LLM | [[LLMModuloFramework|LLM-Modulo]] (Kambhampati et al. 2024) |

## Key design tension

The [[dspy-guardrails|DSPy Guardrails paper]] frames the central tension explicitly: **manually-written guardrails do not generalize to evolving [[Jailbreak|jailbreaks]]**. The three pre-2024 baselines ([[LlamaGuard]], [[NeMoGuardrails]], [[GuardrailsAI]]) all rely on human authoring (a taxonomy, a [[Colang]] flow, a set of validators); the paper's contribution is to replace the human-authoring layer with [[DSPyOptimizers|automatic optimization]] over an annotated dataset.

## See also

- [[Jailbreak]] — adversarial-input problem class guardrails defend against
- [[AttackSuccessRate]] — how guardrails are scored
- [[DSPyGuardrails]] — auto-optimized [[DSPy]] guardrail
- [[LlamaGuard]] / [[NeMoGuardrails]] / [[GuardrailsAI]] — pre-2024 baselines

## From [[ai-engineering-ch05-prompt-engineering|AI Engineering Ch 5]]

Ch 5 implicitly positions [[Guardrail|guardrails]] as the **wrapper-layer + external-layer defense** in the [[DefensivePromptEngineering|defensive-prompt-engineering]] stack, complementing:

- **Model-level** defenses — [[InstructionHierarchy|instruction hierarchy]] training ([[WallaceEtAl2024]], [[openai|OpenAI]]).
- **Prompt-level** defenses — *"write your system prompt assuming it will be public."*
- **Tool-boundary** defenses — sanitize tool outputs before re-insertion (especially for [[IndirectPromptInjection|indirect prompt injection]]).

Ch 5 also references the [[anthropic|Claude]] fill-in-the-blank blocker (Figure 5-15) as an example of a coarse but effective guardrail — even though it false-positives on benign requests, it cuts off the cleanest [[FactualProbing|factual-probing]] / [[TrainingDataExtraction|training-data extraction]] pattern.

The chapter is consistent with the broader wiki framing: guardrails are the **practitioner-grade defense** for production applications, sitting alongside (not in place of) model-level safety training.

The Ch 5 **defenses-supplemental section** further partitions wrapper-layer guardrails into:

- **[[InputGuardrail|Input guardrails]]** — block-lists, known-attack-pattern matching, model-based suspicious-request detection.
- **[[OutputGuardrail|Output guardrails]]** — PII detection, toxicity detection. Non-optional because *"inputs that appear harmless can produce harmful outputs."*
- **[[UsagePatternMonitoring|Usage-pattern monitoring]]** — behavior-over-time anomaly detection that catches what per-request filters miss.

These are paired with system-level [[Isolation|isolation]] and [[HumanInTheLoopApproval|human-in-the-loop approval]] for impactful actions.

## From [[ai-engineering-ch10-architecture-feedback|AI Engineering Ch 10]]

Ch 10 promotes guardrails from a *Ch 5 defensive technique* to **Step 2 of the production AI-app reference architecture**, sitting between context construction and model gateway/router. The chapter adds four operational tradeoffs Ch 5 did not surface:

### Reliability vs latency

> *"Some teams told me that latency is more important. The teams decided not to implement guardrails because they can significantly increase the application's latency."* — Ch 10

Each guardrail adds an inference (often AI-powered itself) to the critical path. Real teams skip guardrails entirely to preserve TTFT, a stance Huyen flags as nightmare-inducing but real. The architect's job is to push detectors off the critical path (parallel calls, async scoring) where possible.

### The stream-completion blind spot

> *"Output guardrails might not work well in the stream completion mode. By default, the whole response is generated before being shown to the user, which can take a long time. In the stream completion mode, new tokens are streamed to the user as they are generated, reducing the time the user has to wait to see the response. The downside is that it's hard to evaluate partial responses, so unsafe responses might be streamed to users before the system guardrails can determine that they should be blocked."* — Ch 10

Streaming and post-hoc output filtering are partially incompatible. Mitigations: chunk-level scoring, optimistic streaming with claw-back UI affordances, or accepting longer TTFT for streamed responses.

### Self-host vs API split

> *"While you can implement guardrails on top of both, third-party APIs can reduce the guardrails you need to implement since API providers typically provide many guardrails out of the box for you. At the same time, self-hosting means that you don't need to send requests externally, which reduces the need for many types of input guardrails."* — Ch 10

The total-guardrail-budget depends on which side of the API line your data sits on. Self-hosting removes the egress-PII concern; third-party APIs ship some output filters but require defensive input masking ([[PIIReverseDictionary]]).

### Named off-the-shelf solutions

Ch 10's canonical list:

- **[[PurpleLlama|Meta Purple Llama]]** — Meta's safety umbrella (Llama Guard etc.).
- **[[NeMoGuardrails|NVIDIA NeMo Guardrails]]** — [[Colang]] dialog-flow guardrails.
- **[[AzurePyRIT|Azure PyRIT]]** + Azure AI content filters — Microsoft's safety stack.
- **[[PerspectiveAPI|Perspective API]]** — Google/Jigsaw toxicity-scoring API.
- **[[openai|OpenAI]]'s content moderation API**.

### Failure-handling policies

Beyond detect/block, Ch 10 names three policy patterns for handling failures the guardrails catch:

1. **Retry** — incurs latency cost.
2. **Parallel calls** — N copies of the same request, pick the best; incurs redundant cost.
3. **Human fallback** — route on anger sentiment, on stuck-loop detection, on sentinel phrases.

### Where guardrails live in the architecture

Ch 10 notes that guardrail responsibility is *fluid*: it can sit in the [[InferenceService]], in the [[ModelGateway]], or as a standalone component. *"While it's necessary to separate components to keep your system modular and maintainable, this separation is fluid."* The same goes for [[ExactCache|caching]] — it can be in the gateway or as a standalone layer.
