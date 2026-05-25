---
title: "Arbor"
type: entity
tags: [framework, rl, distributed-training, dspy]
sources: [dspy-tutorial-rl-papillon, dspy-rl-multihop-tutorial]
last_updated: 2026-05-24
---

# Arbor

`arbor-ai` — distributed reinforcement-learning framework that backs [[DSPy]]'s online-RL optimizer [[ArborGRPO]] (`dspy.GRPO`). Installation: `pip install -U arbor-ai`. Two wiki receipts:

- [[dspy-tutorial-rl-papillon|DSPy `rl_papillon` tutorial]] — drives [[grpo|GRPO]] / [[DAPO]] training of a 1.5B-parameter local LM on 4× [[NVIDIA|H100]] for the [[PAPILLON]] privacy-delegation program.
- [[dspy-rl-multihop-tutorial|DSPy `rl_multihop` tutorial]] — drives [[grpo|GRPO]] / [[DAPO]] training of `Qwen/Qwen2.5-1.5B-Instruct` on 4 GPUs (3 training + 1 inference) for the [[ResearchHop]] multi-hop retrieval program over [[HoVer]].

## Explicit API surface (from the rl_multihop tutorial)

```python
import arbor
from arbor import ArborGRPO, ArborProvider

arbor_server_info = arbor.init()
local_lm = dspy.LM(
    model="openai/arbor:Qwen/Qwen2.5-1.5B-Instruct",
    provider=ArborProvider(),
    api_base=arbor_server_info["base_url"],
    ...
)
```

- **`arbor.init()`** spins up the Arbor inference server and returns connection metadata (`base_url`, port).
- **`ArborProvider`** is the [[DSPyLM|`dspy.LM(provider=...)`]] adapter that routes DSPy LM calls through the Arbor server.
- **`"openai/arbor:Qwen/..."`** is the model-name convention: `openai/` prefix selects the OpenAI-compatible API surface; `arbor:` sub-prefix tells DSPy to route via the Arbor backend; the remainder is the local model identifier.

## Role inside the [[ArborGRPO]] compiler

- Spawns RL rollouts in parallel (`num_threads=` in `ArborGRPO(...)`).
- Applies the configured loss (`loss_type="dapo"`) over those rollouts.
- Writes [[lora|LoRA]] adapter updates back into the local LM.
- Exposes the standard Hugging Face TRL-style `train_kwargs` surface for batch / lr / LoRA / GPU-partition hyperparameters (`num_training_gpus` / `num_inference_gpus`, the rl_multihop tutorial reveals).

## Connections

- [[ArborGRPO]] — the DSPy optimizer that wraps Arbor.
- [[DSPy]] / [[DSPyLM]] — the host framework Arbor is exposed through; `provider=ArborProvider()` is the binding form.
- [[grpo|GRPO]] / [[DAPO]] — the RL algorithms Arbor implements.
- [[dspy-tutorial-rl-papillon]] — the wiki's first DSPy tutorial built on Arbor (PAPILLON + PUPA).
- [[dspy-rl-multihop-tutorial]] — the wiki's second Arbor receipt (`ResearchHop` + HoVer).
- [[PAPILLON]] / [[PUPA]] / [[ResearchHop]] / [[HoVer]] — the programs + benchmarks the tutorials train.
