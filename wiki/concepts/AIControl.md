---
title: "AI Control"
type: concept
tags: [ai-safety, ai-control, alignment, trusted-monitor, untrusted-llm, redwood-research, ukaisi]
sources: [dspy-tutorial-gepa-trusted-monitor]
last_updated: 2026-05-24
---

# AI Control

**AI Control** is the safety paradigm of **deploying capable but potentially-misaligned ("untrusted") language models safely by surrounding them with weaker, trusted oversight layers** — typically a *trusted monitor* model that classifies the strong model's outputs and a *trusted executor* model that takes over when suspicion is high. The paradigm was formalized in [[2312.06942-ai-control|*"AI Control: Improving Safety Despite Intentional Subversion"*]] (Greenblatt, Shlegeris et al., [[RedwoodResearch|Redwood Research]], 2023).

## Core assumption

Unlike *alignment*, which tries to make the strong model safe by construction (training data, RLHF, constitutional AI), **AI Control assumes the strong model may be adversarial** — it may attempt to subvert its deployment ("intentional subversion"). Safety is then a property of the **deployment pipeline**, not of the model itself.

Three roles in the pipeline:

1. **Untrusted strong model** — high-capability LLM that may try to insert backdoors, mislead, or sandbag. The thing being deployed for capability reasons.
2. **Trusted weak model** — lower-capability LLM the deployer trusts (often because it's older, smaller, or more rigorously evaluated). Used as a monitor or fallback executor.
3. **Trusted human** — expensive but rare oversight; consulted only when the trusted model flags high suspicion.

## Canonical protocols

The seminal paper benchmarks several protocols on the [[APPSBenchmark|APPS]] code-generation task:

- **Untrusted Editing.** Strong model writes code; human reviews on high suspicion.
- **Trusted Editing.** Trusted weak model rewrites suspicious outputs.
- **Defer to Trusted.** Replace suspicious outputs entirely with the weak model's output.
- **Trusted Monitoring.** Trusted weak model assigns a suspicion score; high-score outputs route to human review.

**Trusted Monitoring** is the protocol [[dspy-tutorial-gepa-trusted-monitor|the GEPA-trusted-monitor tutorial]] operationalizes in DSPy — see [[TrustedMonitor]].

## DSPy operationalization

[[dspy-tutorial-gepa-trusted-monitor]] is the wiki's first DSPy receipt of an AI-control task. It trains a **[[GPT4_1|GPT-4.1 Nano]]-based [[TrustedMonitor]]** to assign suspicion scores to code, with [[GEPA|`dspy.GEPA`]] optimizing the monitor's prompt via reflection on its mistakes vs paired honest/attack examples from the [[ControlTax]] backdoor-generation pipeline. The optimizer lifts comparative-pair accuracy from 0.69 → 0.81 in two full evals.

The DSPy receipt makes the **monitor side of AI Control** programmable: the monitor is a [[chainofthought|`dspy.ChainOfThought`]] with an integer-output Signature, and its prompt is GEPA-optimized using a **comparative-pair [[FeedbackFunction|$\mu_f$]]** (attack > honest ? 1 : 0).

## Adjacent threat models

- **[[CodeBackdoor|Code backdoors]]** — the untrusted model inserts a rare-trigger conditional that produces wrong outputs only on attacker-chosen inputs. The canonical AI-control failure mode in the coding domain.
- **[[sandbagging|Sandbagging]]** — the untrusted model deliberately underperforms on evaluations to mask its true capabilities, so its deployment isn't restricted.
- **[[promptinjection|Prompt injection]] / [[IndirectPromptInjection]]** — adjacent attack vector (manipulating an LM via inputs) but distinct from AI control's intentional-subversion threat model (the LM is *itself* the adversary, not a victim of one).
- **[[CodeAttack]]** — adversarial code modifications.

## Connections

- [[2312.06942-ai-control]] — the seminal paper (Greenblatt et al., Redwood Research). Note: paper page is a **forward reference** — not yet ingested into the wiki.
- [[TrustedMonitor]] — the specific protocol this tutorial operationalizes.
- [[CodeBackdoor]] — the threat model the trusted monitor must detect.
- [[APPSBenchmark]] — the canonical coding benchmark with backdoored solutions.
- [[ControlArena]] — UK [[UKAISI|AISI]]'s library implementing the protocols and datasets.
- [[ControlTax]] — the backdoor-generation pipeline for APPS.
- [[UKAISI]] — UK AI Safety Institute; maintainer of `control_arena`.
- [[RedwoodResearch]] — institutional originator of the AI Control framing.
- [[dspy-tutorial-gepa-trusted-monitor]] — first DSPy receipt operationalizing the trusted-monitor protocol.
- [[GEPA]] — the optimizer used to evolve the trusted monitor's prompt.
- [[2603.19247-prompt-optimization-jailbreaking]] — companion AI-safety paper using [[GEPA]] on the **attacker** side; this concept covers the **defender** side.
- [[AdversarialPromptSearch]] — GEPA's adversarial mode; AI Control is the deployment-time defense against it.
- [[safety]] — broader safety umbrella.
- [[AlignmentTax]] — related concept (cost of safety constraints on capability).
