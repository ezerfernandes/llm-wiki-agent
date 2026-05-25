---
title: "Amazon Nova Lite"
type: entity
tags: [model, amazon, nova, budget-tier]
sources: [2604.14585-prompt-optimization-coin-flip]
last_updated: 2026-05-22
---

# Amazon Nova Lite

[[Amazon]]'s **budget-tier** LM in the Nova model family. The companion executor to [[ClaudeHaiku45|Claude Haiku 4.5]] in [[2604.14585-prompt-optimization-coin-flip]]'s cross-model study of prompt optimization.

## Wiki role

The cross-vendor budget-tier executor in [[2604.14585-prompt-optimization-coin-flip]]:

- **Study 1**: 3 tasks × $10 \times 10$ prompt grid. Interaction non-significant in all conditions — replicates the Haiku finding on a different vendor's model.
- **Study 2**: 4 tasks × 6 optimizers. **14 of 24 method×task means fall below zero-shot** (worse than Haiku's 49%).

## Model-specificity reversals (Section 5 of the paper)

The Nova / Haiku comparison is the canonical wiki anchor for [[ModelSpecificityShelfLife|model-specific optimization headroom]]:

- [[HelpSteer2]] is highly optimizable on Haiku (6/6 methods beat zero-shot) but barely on Nova (1/6) — a near-complete reversal.
- [[FeedbackBench]] goes from 1/6 on Haiku to 4/6 on Nova — also a reversal in the opposite direction.
- On [[XSum]], Agent A (extractor) matters on Nova ($p < 0.001$) but not on Haiku.

The reversals illustrate the paper's claim that **neither coupling structure nor optimization headroom can be determined a priori** — both are empirical properties of the specific model–task combination.

## Connections
- [[Amazon]] — developer.
- [[ClaudeHaiku45]] — mid-tier executor compared against.
- [[ClaudeSonnet46]] — judge model in the same study.
- [[AWSGenerativeAIInnovationCenter]] — paper's lead institution; cross-vendor evaluation includes Amazon's own Nova.
- [[2604.14585-prompt-optimization-coin-flip]] — canonical wiki anchor.
- [[ModelSpecificityShelfLife]] — meta-finding the Nova / Haiku reversals support.
