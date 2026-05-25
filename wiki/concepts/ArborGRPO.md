---
title: "ArborGRPO"
type: concept
tags: [dspy, optimizer, rl, grpo, dapo, lora, multi-module, experimental]
sources: [dspy-tutorial-rl-papillon, dspy-rl-multihop-tutorial]
last_updated: 2026-05-24
---

# ArborGRPO

**Multi-module online-RL [[DSPyOptimizers|DSPy optimizer]]** that extends [[grpo|GRPO]] to compound AI systems. Surfaced as the `dspy.GRPO` / `ArborGRPO` compiler over the [[Arbor]] (`arbor-ai`) distributed-RL framework; takes a [[DSPyModules|`dspy.Module`]] program and trains its underlying LM's [[lora|LoRA]] weights so that *one scalar reward propagates back across all modules* in the program simultaneously.

Two wiki receipts, both labeled **"new and extremely EXPERIMENTAL"** and **"in pure proof of concept and development mode"**:
- [[dspy-tutorial-rl-papillon|DSPy `rl_papillon` tutorial]] — trains [[PAPILLON]] on [[PUPA]] with an [[LLMJudge|LLM-as-judge composite reward]]; 1.5B local LM, 4× H100, ~3 h, 54.6 → 60.0 composite.
- [[dspy-rl-multihop-tutorial|DSPy `rl_multihop` tutorial]] — trains [[ResearchHop]] on [[HoVer]] 3-hop claims with a **deterministic title-recall reward**; `Qwen/Qwen2.5-1.5B-Instruct`, 4 GPUs (3 training + 1 inference), ~18 h, 61.8 → 66.2 recall.

## Compiler interface

```python
compiler = ArborGRPO(
    metric=compute_overall_score,           # scalar reward function (LLM judge OK)
    multitask=True,                         # one model, many program modules
    num_dspy_examples_per_grpo_step=4,      # prompts per gradient update
    num_samples_per_input=8,                # rollouts per prompt
    exclude_demos=True,                     # zero-shot rollouts (no bootstrapped demos)
    num_train_steps=500,
    num_threads=24,
)

optimized_program = compiler.compile(
    student=program, trainset=trainset, valset=devset
)
```

Same `optimizer.compile(student=..., trainset=..., valset=...)` contract as every other DSPy optimizer ([[MIPROv2]], [[GEPA]], [[BootstrapFinetune]], [[BootstrapFewShot]] …) — see [[DSPyOptimizers]] for the catalog.

## Training-time hyperparameters

Configured via a `train_kwargs` dict passed through to Arbor / Hugging Face TRL:

| Key | Value (PAPILLON tutorial) | Note |
|---|---|---|
| `per_device_train_batch_size` | 8 | × `gradient_accumulation_steps` → effective batch 32 |
| `gradient_accumulation_steps` | 4 | |
| `temperature` | 1.0 | rollout sampling temp |
| `top_k` / `top_p` | -1 / 1.0 | unrestricted sampling |
| `beta` | **0.00** | **no [[KLPenalty|KL]] anchor to reference policy** (unjustified in tutorial) |
| `learning_rate` | 1e-6 | |
| `lr_scheduler_type` | `constant_with_warmup` | |
| `gradient_checkpointing` | `True` | memory trade-off |
| `bf16` | `True` | mixed precision |
| `loss_type` | `"dapo"` | **uses [[DAPO]], not vanilla GRPO** |
| `max_steps` | 1000 | hard cap |
| `lora_config` | r=8, α=16, dropout=0.05; targets q/k/v/o/up/down/gate `_proj` | rank-8 [[lora|LoRA]] adapters |

## Position in the DSPy optimizer catalog

[[DSPyOptimizers]] organizes optimizers by **what they tune** along three orthogonal axes — *demonstrations*, *instructions*, *LM weights*. ArborGRPO joins [[BootstrapFinetune]] on the **LM-weights** axis but with a fundamentally different mechanism:

| Optimizer | Mechanism | Reward signal | Data budget |
|---|---|---|---|
| [[BootstrapFinetune]] | Distill prompt-based program into fine-tuned LM via metric-validated bootstrapped traces | Pass/fail on metric | Bootstrap pass — finite |
| **ArborGRPO** | Online RL: rollouts → reward → policy gradient → [[lora|LoRA]] update | Scalar metric / [[LLMJudge|LLM judge]] | Online — bounded only by `num_train_steps × num_dspy_examples_per_grpo_step × num_samples_per_input` |

## Authors' own caveats

> "typically worse on cost/quality basis than" [conventional prompt optimization]

> "a solid start for online RL over arbitrary LM programs for tiny LMs"

The [[2507.19457-gepa|GEPA paper]] reports that on the same [[PUPA]] benchmark, GEPA reaches 91.85 vs GRPO's 86.66 (Qwen3 8B, both within +1% of each other only on baseline) with **up to 35× fewer rollouts** — concrete evidence that *reflective prompt mutation > online weight-RL* in the compound-AI-system regime when the underlying LM is capable enough that prompts can move the needle.

## When ArborGRPO is worth reaching for

The tutorial's own positioning: **when the local LM is small enough that prompt-only optimization hits a capability ceiling**. The receipt is a 1.5B model where 3 h of GRPO+LoRA on 4× [[NVIDIA|H100]] lifts a composite reward from 54.6 → 60.0 — a regime where MIPROv2 / GEPA prompts almost certainly do *not* close the gap because the underlying LM cannot follow the optimized instruction.

## Cross-tutorial config diff

| Kwarg | [[dspy-tutorial-rl-papillon|PAPILLON tutorial]] | [[dspy-rl-multihop-tutorial|rl_multihop tutorial]] |
|---|---|---|
| Task | Privacy-preserving delegation ([[PAPILLON]] / [[PUPA]]) | Multi-hop retrieval ([[ResearchHop]] / [[HoVer]]) |
| Reward | [[LLMJudge|LLM-judge composite]] `(quality + (1-leakage))/2` | Deterministic title-recall (gold ∩ retrieved) / |gold| |
| `num_dspy_examples_per_grpo_step` | 4 | 6 |
| `num_samples_per_input` / `num_rollouts_per_grpo_step` | 8 (`num_samples_per_input`) | 24 (`num_rollouts_per_grpo_step`) |
| Group size (advantage estimate) | 8 | 4 |
| `multitask` | `True` | (not shown — single-LM both sub-modules implied) |
| `num_train_steps` | 500 | 1000 |
| `num_threads` | 24 | 16 |
| `num_steps_for_val` / `use_train_as_val` / `checkpoint` | not shown | `50` / `False` / `"single-best"` |
| `per_device_train_batch_size` | 8 | 2 |
| `gradient_accumulation_steps` | 4 | 24/6 = 4 |
| `beta` (KL anchor) | 0.00 | 0.00 |
| `loss_type` | `"dapo"` | `"dapo"` |
| `learning_rate` | 1e-6 | 1e-6 |
| `lora_config` | r=8, α=16, dropout=0.05, q/k/v/o/up/down/gate `_proj` | identical |
| `num_training_gpus` / `num_inference_gpus` | not surfaced | 3 / 1 |
| `scale_rewards` / `max_grad_norm` / `weight_decay` | not surfaced | `False` / `1.0` / `0.001` |
| Wall-clock | ~3 h on 4× H100 | ~18 h on 4 GPUs |
| Lift | 54.6 → 60.0 (composite) | 61.8 → 66.2 (recall) |

The **LoRA config and `loss_type="dapo"` + `beta=0.00`** combination is identical across both receipts — strong evidence this is the **default DAPO+LoRA recipe** for ArborGRPO. The differences are task-shape kwargs (rollout budget, validation cadence, GPU partition) and hardware envelope (PAPILLON ran shorter on bigger compute; rl_multihop runs longer on smaller compute).

## Connections

- [[grpo|GRPO]] — the base RL algorithm; ArborGRPO is its multi-module compound-AI-system extension.
- [[DAPO]] — the GRPO variant ArborGRPO uses by default (`loss_type="dapo"`).
- [[DSPy]] / [[DSPyOptimizers]] / [[DSPyModules]] — the framework + optimizer-catalog context.
- [[Arbor]] — the `arbor-ai` distributed-RL framework that does the actual training work.
- [[PAPILLON]] — privacy-delegation program ArborGRPO has been demonstrated on.
- [[ResearchHop]] — multi-hop retrieval program ArborGRPO has been demonstrated on (second receipt).
- [[PUPA]] / [[HoVer]] — the corresponding benchmarks.
- [[LLMJudge]] — the reward-function pattern paired with ArborGRPO in the PAPILLON receipt.
- [[lora|LoRA]] — the parameter-efficient fine-tuning surface ArborGRPO writes into.
- [[BootstrapFinetune]] — the other LM-weights-axis DSPy optimizer; mechanism contrast (distillation vs. online RL).
- [[GEPA]] / [[2507.19457-gepa]] — the prompt-space alternative that empirically dominates ArborGRPO on both PUPA and HoVer.
- [[dspy-tutorial-rl-papillon]] — first canonical tutorial.
- [[dspy-rl-multihop-tutorial]] — second canonical tutorial.
