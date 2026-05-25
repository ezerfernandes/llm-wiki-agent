---
title: "System 1 vs System 2"
type: concept
tags: [cognitive-science, reasoning, framing]
sources: [2402.01817-llm-modulo, hands-on-llm-ch06-prompt-engineering]
last_updated: 2026-05-23
---

# System 1 vs System 2

Kahneman's dual-process taxonomy (*Thinking, Fast and Slow*, 2011):
- **System 1** — fast, intuitive, associative, parallel, automatic, constant-time response.
- **System 2** — slow, deliberate, sequential, search-based, principled, effortful.

## Use in this wiki
[[2402.01817-llm-modulo]] hangs its central argument on this taxonomy:

> *Even from a pure engineering perspective, a system that takes constant time to produce the next token cannot possibly be doing principled reasoning on its own.*

LLMs are framed as a **giant pseudo-System 1** — an "approximate knowledge source gleaned either from the environment or compiled from System 2" — whose strength is making/finding analogies across vast prior text, not deliberation. Multi-modality (GPT-4V) **extends System 1 imagination** but does not bestow System 2 competence.

The [[LLMModuloFramework]] is, in this framing, an explicit **System 1 (LLM) + System 2 (sound external critic loop)** composition, with soundness inherited from the System 2 side.

## Connections
- [[Planning]], [[SelfVerification]] — examples of System-2 tasks LLMs alone cannot perform
- [[LLMModuloFramework]] — proposed System-1/System-2 composition
- [[ChainOfThought]], [[TreeOfThoughts]], [[Reflexion]] — critiqued as System-1 priming variations, not true System 2
- [[2402.01817-llm-modulo]] — source critiquing the System-2-resemblance claim
- [[hands-on-llm-ch06-prompt-engineering]] — source taking the constructive position

## From [[hands-on-llm-ch06-prompt-engineering|Hands-On LLMs Ch 6]]

Ch 6 cites Kahneman's *Thinking, Fast and Slow* (2011) directly and takes the **constructive position** on operationalizing System 2 via prompting:

> *"System 1 thinking represents an automatic, intuitive, and near-instantaneous process. It shares similarities with generative models that automatically generate tokens without any self-reflective behavior. In contrast, system 2 thinking is a conscious, slow, and logical process, akin to brainstorming and self-reflection. If we could give a generative model the ability to mimic a form of self-reflection, we would essentially be emulating the system 2 way of thinking, which tends to produce more thoughtful responses than system 1 thinking."* — Ch 6

This frames [[chainofthought|chain-of-thought]], [[selfconsistency|self-consistency]], and [[TreeOfThoughts|tree-of-thought]] as **constructive operationalizations of System 2** — the LLM doesn't *become* System 2, but *resembles* it sufficiently to produce more thoughtful outputs.

### The constructive-vs-critical live tension

Ch 6's constructive stance sits in soft tension with [[2402.01817-llm-modulo|Kambhampati et al.'s critique]] that *"a system that takes constant time to produce the next token cannot possibly be doing principled reasoning on its own"*. Both positions are now documented on this page:

| Position | Source | Claim |
|---|---|---|
| **Constructive** | Ch 6 | CoT / self-consistency / ToT *resemble* System 2 well enough to improve outputs in practice. |
| **Critical** | [[2402.01817-llm-modulo]] | The resemblance is empty without an external verifier; apparent gains come from problem-specific verifiers (e.g., 24-puzzle arithmetic checker). |

The wiki position: **both positions hold simultaneously** — the resemblance is real *and* operationally useful (Ch 6), *and* the resemblance is not principled reasoning and breaks where the verifier is absent (Kambhampati et al.). The disagreement is on *interpretation* of the operational fact, not on the fact itself. Ch 6 is the only wiki source that explicitly cites Kahneman's primary 2011 framing; [[2402.01817-llm-modulo]] uses Kahneman to anchor the critique.

The [[TreeOfThoughts]] page is the most direct intersection point — both ToT framings are documented there (Yao et al. 2023's multi-call architecture, Ch 6's single-prompt three-experts approximation, and Kambhampati et al.'s critique).
