---
title: "GRPO"
type: concept
tags: [ml-method, rl-algorithm]
sources: [2512.04388-conductor, 2605.02572-long-horizon-llm-training]
last_updated: 2026-05-10
---

# GRPO

Group Relative Policy Optimization (Shao et al., 2024). Critic-free policy-gradient method that uses Monte-Carlo advantages within grouped completions; reduces memory/compute relative to PPO and is the default RL backbone in modern reasoning LLM training (DeepSeek R1, the Conductor, and the long-horizon study all build on GRPO or its descendants like DAPO / GSPO / CISPO).

## Connections
- [[reinforcementlearning|ReinforcementLearning]]
- [[deepseekr1|DeepSeekR1]]
- [[2512.04388-conductor]]
- [[2605.02572-long-horizon-llm-training]]
