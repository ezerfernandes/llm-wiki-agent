---
title: "HuggingFace LLM Course — Ch 12: Build Reasoning Models like DeepSeek R1"
type: source
tags: [hf-llm-course, course, reasoning, rlhf, grpo, deepseek, r1, rl]
date: 2026-05-23
source_file: raw/hf-llm-course/ch12-reasoning-models.md
---

## Summary

Chapter 12 of the HuggingFace LLM Course (also known as "Open R1 for Students") teaches how reinforcement learning can be used to develop reasoning capabilities in LLMs, centered on the DeepSeek R1 paper and the Group Relative Policy Optimization (GRPO) algorithm. It progresses from RL fundamentals (agent, environment, action, reward, policy) and RLHF, to a detailed walkthrough of the DeepSeek R1 training pipeline (Cold Start → Reasoning RL → Rejection Sampling → Diverse RL) and the emergent "Aha Moment" phenomenon observed in R1-Zero. A dedicated mathematical deep-dive (Section 3b, by Shirin Yamani) covers GRPO's three-step objective: group sampling, advantage standardization, and clipped policy update with KL penalty. The chapter ends with two hands-on practical exercises that fine-tune SmolLM2-135M and Gemma-3-1B with [[GRPO]] via the [[TRL]] `GRPOTrainer`, the second using [[Unsloth]] + vLLM for accelerated training on [[GSM8K]] with XML-formatted chain-of-thought rewards.

## Key Claims

- Pure reinforcement learning (no supervised fine-tuning) is sufficient to elicit reasoning capabilities in LLMs — proven by DeepSeek-R1-Zero (71.0% AIME 2024).
- DeepSeek-R1 builds on R1-Zero by adding SFT phases (Cold Start, Rejection Sampling), reaching 79.8% on AIME 2024 and 97.3% on MATH-500.
- GRPO eliminates the separate value/critic model used by PPO, replacing per-step value estimation with **group-relative advantage** — comparing G (typically 4–16) completions for the same prompt.
- Advantage is standardized within each group: `A_i = (r_i - mean(rewards)) / std(rewards)` — "grading on a curve".
- GRPO uses any reward function, not preference pairs (unlike DPO) and not a learned reward model (unlike PPO) — rule-based rewards (math solvers, format checks, length penalties) are sufficient for verifiable tasks.
- The "Aha Moment" — emergent self-correction (initial attempt → recognition of error → correction → explanation) — appeared naturally during R1-Zero's RL training without being explicitly programmed.
- DeepSeek-R1's training proceeds in four phases: Cold Start (SFT on high-quality R1-Zero samples), Reasoning RL (rule-based rewards on verifiable tasks), Rejection Sampling (DeepSeek-V3 as quality judge), Diverse RL (hybrid rule + LLM feedback).
- The GRPO objective combines a clipped probability ratio (PPO-style, ε ≈ 0.2) with a KL divergence penalty against the reference policy (β = 0.04 in DeepSeekMath).
- Loss in GRPO **increases** during training — counter-intuitively expected — because it is proportional to KL from the original policy, which grows as the model adapts.
- GRPO can be distilled across model sizes (1.5B–70B); 7B reaches 55.5% on AIME 2024, 70B distilled hits 94.5% MATH-500 (near o1-mini).
- TRL's `GRPOTrainer` exposes `num_generation` (group size), `use_vllm` for fast generation, and accepts a list of reward functions whose scores are summed.
- Unsloth + 4-bit quantization + LoRA (r=32) makes GRPO training of Gemma-3-1B feasible on a free Google Colab T4 GPU.
- GSM8K + an XML chain-of-thought format (`<reasoning>…</reasoning><answer>…</answer>`) is the standard recipe — multiple shaped rewards (correctness, integer-answer, strict format, soft format, XML tag count) are combined.
- Rewards may not improve for the first 150–200 training steps — patience required.
- Generation cost is GRPO's main drawback: G completions per prompt multiplies forward-pass cost vs. PPO/DPO.
- Reward function design is the single biggest lever — poor rewards lead to reward hacking; β tuning balances exploration vs. stability.

## Key Quotes

> "GRPO directly evaluates the model-generated responses by comparing them within groups of generation to optimize policy model, instead of training a separate value model (Critic). This approach leads to significant reduction in computational cost!"
> — Section 3b, Shirin Yamani

> "Advantage = (reward - mean(group_rewards)) / std(group_rewards)"
> — GRPO advantage formula (Section 3)

> "One of the most remarkable discoveries in R1-Zero's training was the emergence of a phenomenon known as the 'Aha Moment.' [...] This ability emerged naturally from RL training, without being explicitly programmed, demonstrating learning rather than mere memorization of a process from the training data."
> — Section 3 (the Aha Moment)

> "GRPO's key innovations are: Learning directly from any function or model, eliminating the reliance on a separate reward model. Group-based learning, which is more stable and efficient than traditional methods like pairwise comparisons."
> — Section 3

> "The loss in GRPO is proportional to the KL divergence (the cap relative to original policy). As training progresses, the model learns to generate text that better matches the reward function, causing it to diverge more from its initial policy. This increasing divergence is reflected in the rising loss value, which actually indicates that the model is successfully adapting."
> — Section 5

## Code & Patterns

### Minimal GRPO loop (pseudocode)
```
For each iteration:
  reference_policy = current_policy (snapshot)
  For each prompt:
    Generate G outputs ~ π_old
    rewards = reward_function(outputs)
    A_i = (r_i - mean(rewards)) / std(rewards)
    Loss = -min(ratio * A, clip(ratio, 1-ε, 1+ε) * A) + β * KL(π || π_ref)
```

### TRL minimal training
```python
from trl import GRPOTrainer, GRPOConfig

training_args = GRPOConfig(
    output_dir="output",
    num_generation=4,        # group size G
    per_device_train_batch_size=4,
    use_vllm=True,
)

trainer = GRPOTrainer(
    model="Qwen/Qwen2-0.5B-Instruct",
    args=training_args,
    train_dataset=dataset,
    reward_funcs=reward_func,
)
trainer.train()
```

### Rule-based reward stack (GSM8K + XML CoT, Unsloth exercise)
- `correctness_reward_func` — +2.0 if extracted `<answer>` matches ground truth
- `int_reward_func` — +0.5 if answer is digit
- `strict_format_reward_func` — +0.5 for exact XML pattern
- `soft_format_reward_func` — +0.5 for relaxed pattern
- `xmlcount_reward_func` — fractional credit per tag, penalizes content after `</answer>`

### Advantage calculation (PyTorch)
```python
rewards_grouped = rewards.view(-1, num_generations)
mean = rewards_grouped.mean(dim=1).repeat_interleave(num_generations)
std = rewards_grouped.std(dim=1).repeat_interleave(num_generations)
advantages = (rewards - mean) / (std + 1e-8)
```

### GRPO loss with KL
```python
ratio = torch.exp(new_per_token_logps - per_token_logps)
pg1 = -advantages * ratio
pg2 = -advantages * torch.clamp(ratio, 1.0 - eps, 1.0 + eps)
per_token_loss = torch.max(pg1, pg2) + beta * per_token_kl
```

### Unsloth + Gemma-3-1B setup (4-bit + LoRA r=32, T4-friendly)
```python
model, tokenizer = FastLanguageModel.from_pretrained(
    model_name="google/gemma-3-1b-it",
    load_in_4bit=True,
    fast_inference=True,
    max_lora_rank=32,
    gpu_memory_utilization=0.6,
)
```

### Typical hyperparameters
- `num_generations`: 4–16 (8 common; 6 on T4)
- `ε` (clip range): 0.2
- `β` (KL coef): 0.04 (DeepSeekMath default)
- `learning_rate`: 5e-6 to 2e-5
- `max_grad_norm`: 0.1

### Standard dataset format
- Prompt-only (no chosen/rejected pairs as in DPO).
- For verifiable tasks: prompt + ground-truth answer column (`answers`).
- GSM8K answer extraction: split on `####`; XML CoT answer extraction: split on `<answer>`/`</answer>`.

## Connections

- [[GRPO]] — central algorithm; this source provides the deepest treatment in the wiki (algorithm, math, pseudocode, PyTorch impl).
- [[DeepSeekR1]] — the paper that motivates the entire chapter; covers R1 vs R1-Zero and the four training phases.
- [[DeepSeekMath]] — original GRPO paper (arXiv 2402.03300); source for β = 0.04 default.
- [[PPO]] — baseline RL algorithm; GRPO contrasts by removing the critic and clipping group-relative advantage.
- [[DPO]] — alternative preference-optimization technique; contrasted as preference-pair-based vs GRPO's group-relative.
- [[RLHF]] / [[ReinforcementLearning]] — broader framing; GRPO is positioned as a successor RLHF algorithm.
- [[RewardModel]] / [[RewardFunction]] — GRPO replaces learned reward models with arbitrary reward functions (math solver, length, format).
- [[KullbackLeiblerDivergence]] — the KL penalty term anchoring the policy to π_ref.
- [[GSM8K]] — primary benchmark/training dataset for the Unsloth exercise.
- [[ChainOfThought]] — XML `<reasoning>…</reasoning>` format used to elicit reasoning traces.
- [[TRL]] / [[DPOTrainer]] / [[DPOConfig]] — TRL library family; `GRPOTrainer` and `GRPOConfig` parallel the DPO equivalents.
- [[Unsloth]] — acceleration library enabling GRPO on free Colab T4 GPUs.
- [[HuggingFace]] — publisher of the course; hosts Open R1 project and TRL.
- [[LoRA]] / [[LoraConfig]] / [[QLoRA]] — parameter-efficient fine-tuning used in both practical exercises.
- [[AgenticReinforcementLearning]] — adjacent application of RL to LLM agents.
- [[ReasoningWithLanguageModelIsPlanningWithWorldModel]] — related reasoning-as-search line of work.

## Contradictions

- None identified with existing wiki content. The existing [[GRPO]] page is brief; this source materially expands it (clipping, β, group-size guidance, PyTorch reference impl). The existing [[DeepSeekR1]] page is a stub (297 B); this source supplies the canonical training-phase breakdown and benchmarks. No conflicting claims about PPO vs DPO vs GRPO were found.
- Minor terminological note: TRL `GRPOConfig` field appears as both `num_generation` (singular, Section 4) and `num_generations` (plural, Sections 5–6) — the plural form is the current TRL API; the singular is likely a course typo.
