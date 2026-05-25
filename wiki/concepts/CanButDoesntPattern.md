---
title: "Can But Doesn't Pattern"
type: concept
tags: [prompt-optimization, output-structure, capability-gap, compound-ai-system]
sources: [2604.14585-prompt-optimization-coin-flip]
last_updated: 2026-05-22
---

# Can But Doesn't Pattern

The **"can but doesn't" pattern** — coined by [[2604.14585-prompt-optimization-coin-flip|Zhang et al. (2026)]] — names the property of a task where [[PromptOptimization|prompt optimization]] can deliver real gains: **the model has the latent capability to produce the required output format, but does not default to it in zero-shot**.

A well-chosen prompt unlocks the latent capability. A poorly chosen prompt (or zero-shot) does not.

## The canonical example: HelpSteer2

[[HelpSteer2]] requires **structured rubric-based evaluation with JSON-formatted output**. [[ClaudeHaiku45|Claude Haiku 4.5]] can produce this format — when prompted correctly, scores jump from **68.0 → 74.8** ($+6.8$ pts, the largest gain in the paper's Study 2). But its zero-shot default is **unstructured prose**.

This is the **sole task** in [[2604.14585-prompt-optimization-coin-flip|Zhang et al.]] where all six optimizers beat zero-shot on Haiku. All methods that reach $\geq 74$ pts **independently discover the same JSON-rubric structure** — strong evidence that the optimization landscape has a clear feature to exploit.

## Why other tasks fail

[[FeedbackBench]], [[WildBench]], and [[XSum]] all accept **free-form natural-language output**. The model's zero-shot behavior is already near-optimal for the format these tasks require — there is **no latent capability gap** for optimization to unlock. Gains over zero-shot confirm this:

| Task | Required format | Best gain ([[ClaudeHaiku45\|Haiku]]) |
|---|---|---|
| [[HelpSteer2]] | **JSON rubric** | **+6.8** |
| [[FeedbackBench]] | Free-form prose | +1.1 |
| [[WildBench]] | Free-form prose | +0.7 |
| [[XSum]] | Free-form prose | +0.6 |

The bottom three are within the noise floor of 20-question evaluation. Only the JSON-rubric task crosses the 2-pt [[HeadroomTest|headroom threshold]].

## Generalization hypothesis

The paper hypothesizes the pattern generalizes to:

- Tasks requiring **specific output schemas** (JSON, XML).
- **Domain-specific formatting conventions** (citation styles, code blocks, structured tables).
- **Structured reasoning templates** (chain-of-thought scaffolds, plan-then-execute).
- Any setting where the model has latent capability that a **well-chosen prompt can unlock**.

The opposite — tasks where the model's free-form default is already format-appropriate — predicts a coin-flip outcome under any prompt optimization budget.

## Why this matters

The pattern reframes the [[PromptOptimization|prompt-optimization]] research program:

- **Optimization methods are not universally useful tools.** They are **format-unlocking probes** — they help when the model has a latent capability gated behind a specific output structure.
- The aggregate **49% below-zero-shot failure rate** in [[2604.14585-prompt-optimization-coin-flip|Zhang et al.]] is the price paid for running optimization on the wrong kind of task.
- The [[HeadroomTest|headroom test]] (~$5, 10 min) is the cheap pre-test that predicts which kind of task you have.

## Connections to wiki precedents

The pattern explains why **certain prior wiki successes worked**:

- [[2025-bionlp-archehr-qa-neural|Neural at ArchEHR-QA 2025]] beats zero-shot by **20 points** with [[MIPROv2]]. The task imposes a strict ≤75-word + citation-format constraint + a six-metric composite reward — **exploitable output structure** by Zhang et al.'s framing.
- [[2312.13382-dspy-assertions|DSPy Assertions]] lifts [[QuizGen]] valid-JSON output from 37.6% → 100%. The valid-JSON gate is the **canonical** [[CanButDoesntPattern|"can but doesn't"]] gap.
- [[2406.11695-mipro|MIPRO]] wins biggest on [[HotPotQAConditional]] (6 → 23.3 — answer-format depends on entity type). Conditional output format = exploitable structure.

And why **other wiki results were limited**:

- [[OPRO]] / [[APE]] / [[EvoPrompt]] on free-form QA show modest gains. Free-form ≠ exploitable structure.

## Connections

- [[2604.14585-prompt-optimization-coin-flip]] — canonical source; coins the pattern.
- [[HeadroomTest]] — the cheap pre-test for the pattern's presence.
- [[CompoundAIDiagnostic]] — the framework that gates on this pattern.
- [[PromptOptimization]] — parent task the pattern qualifies.
- [[HelpSteer2]] — the canonical positive example.
- [[FeedbackBench]] / [[WildBench]] / [[XSum]] — canonical negative examples.
- [[CoinFlipOptimization]] — the failure phenomenon this pattern explains the *exceptions* to.
- [[2025-bionlp-archehr-qa-neural]] — clinical-QA case consistent with the pattern.
- [[QuizGen]] — JSON-format unlock case consistent with the pattern.
