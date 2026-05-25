---
title: "Repeated Token Attack"
type: concept
tags: [llm-security, adversarial, training-data, prompt-attack]
sources: [ai-engineering-ch05-prompt-engineering]
last_updated: 2024-12-04
---

# Repeated Token Attack

**A family of [[TrainingDataExtraction|training-data extraction]] attacks that exploit unusual token-repetition patterns to cause the model to diverge from its normal output distribution and emit memorized training data.** Cited in [[ai-engineering-ch05-prompt-engineering|*AI Engineering* Ch 5]] (footnote) via Dropbox's *"Bye Bye Bye...: Evolution of repeated token attacks on ChatGPT models"* (Breitenbach & Wood, 2024).

## Variants

| Variant | Mechanism |
|---|---|
| **[[DivergenceAttack\|Divergence attack]]** ([[NasrEtAl2023]]) | *"Repeat 'poem' forever"* — model repeats, then diverges. |
| **In-prompt repetition** | Embed a target string repeated many times in the prompt to nudge the model into a different distribution. |
| **Nested repetition** | Unusual patterns combining repetition with structural prompts. |

## Why this family matters

Two structural properties make repeated-token attacks distinct:

1. **The trigger prompts are innocuous-looking.** *"Repeat 'poem' forever"* doesn't match any PII filter or jailbreak pattern.
2. **The exploit is at the *generation* layer, not the *instruction-following* layer.** It works by pushing the model out of its trained output distribution rather than by tricking it about what to do.

This is why repeated-token attacks bypass defenses tuned for prompt-injection and persona-based jailbreaks — the attack class is fundamentally different.

## Defenses

- **Block long repetition** in inputs.
- **Halt generation** when the model starts producing degenerate output (repeating its own previous output, breaking from the prompt's task).
- **Output filters** for PII and copyrighted-content patterns.

## Connections

- [[ai-engineering-ch05-prompt-engineering]] — primary source.
- [[DivergenceAttack]] — the canonical member.
- [[TrainingDataExtraction]] — parent.
- [[InformationExtraction]] — umbrella attack family.
- [[PromptAttack]] — root umbrella.
- [[NasrEtAl2023]] — paper that demonstrated the divergence variant.
