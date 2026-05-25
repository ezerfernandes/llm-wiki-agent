---
title: "Claude Haiku 4.5"
type: entity
tags: [model, anthropic, claude, mid-tier]
sources: [2604.14585-prompt-optimization-coin-flip]
last_updated: 2026-05-22
---

# Claude Haiku 4.5

[[anthropic|Anthropic]]'s **mid-tier** model in the Claude 4 family. The primary executor model in [[2604.14585-prompt-optimization-coin-flip]]'s controlled study of prompt optimization.

## Wiki role

Used as the **mid-tier executor** across both studies in the canonical compound-AI-optimization audit:

- **Study 1 (agent coupling)**: 3 tasks × $10 \times 10$ prompt grid × $n=30$ samples → ANOVA decomposition. Interaction non-significant in all conditions ($F < 1$, $p > 0.52$).
- **Study 2 (single-agent optimization)**: 4 tasks × 6 optimizers × 3 repeats = 72 runs. **49% score below zero-shot** — the canonical coin-flip statistic.

The companion budget-tier executor in the study is [[AmazonNovaLite]]; the judge model is [[ClaudeSonnet46|Claude Sonnet 4.6]].

## Headline behavior

- **HotpotQA** (Study 1): Agent B dominates ($p < 0.001$); interaction 0.18% (smallest of all 6 conditions).
- **HelpSteer2** (Study 2): all 6 methods beat zero-shot (best $+6.8$ from [[EvoPrompt]]) — the only task where this happens. Demonstrates the [[CanButDoesntPattern|"can but doesn't" pattern]] for JSON-rubric output.
- **3 of 4 free-form tasks**: average optimizer gain is negative.

## Connections
- [[anthropic]] — developer.
- [[claudeopus47|Claude Opus 4.7]] / [[claudeopus46|Claude Opus 4.6]] — flagship siblings.
- [[ClaudeSonnet46]] — judge model used in the same study.
- [[AmazonNovaLite]] — budget-tier executor compared against.
- [[2604.14585-prompt-optimization-coin-flip]] — canonical wiki anchor.
