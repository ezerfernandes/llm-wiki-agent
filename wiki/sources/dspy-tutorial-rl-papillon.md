---
title: "DSPy Tutorial — Online RL over a Multi-Module DSPy Program (PAPILLON + ArborGRPO)"
type: source
tags: [dspy, tutorial, rl, grpo, papillon, privacy, delegation, lora, arbor, pupa, experimental]
date: 2026-05-24
source_file: raw/dspy-tutorial-rl-papillon.md
---

## Summary

Official [[DSPy]] tutorial at `https://dspy.ai/tutorials/rl_papillon/` — **the wiki's first receipt of [[GRPO|GRPO]]-style online [[reinforcementlearning|reinforcement learning]] applied to a *multi-module* [[CompoundAISystem|compound AI system]]** via DSPy's `dspy.GRPO` / `ArborGRPO` compiler. Trains a tiny 1.5B-parameter local LM inside the two-module [[PAPILLON]] privacy-preserving delegation program (`dspy.ChainOfThought(CraftRedactedRequest)` → external untrusted LLM → `dspy.Predict(RespondToQuery)`) on the [[PUPA]] benchmark, optimizing a composite `(quality + (1 − leakage)) / 2` reward via an [[LLMJudge|`LLMJudge`]] of dual `JudgeQuality` + `JudgeLeakage` modules. **Devset composite lifts 54.6 → 60.0 in ~3 h on 4× [[H100]] using [[LoRA]] (rank-8, α=16, dropout 0.05, all attention + MLP projections), [[DAPO|`loss_type="dapo"`]], `beta=0.0` (no [[KLPenalty|KL]]), bf16, `lr=1e-6`, batch 8 × grad-accum 4, 500 train steps with 8 samples per input × 4 examples per GRPO step.** Authors are explicit that this is *"new and extremely EXPERIMENTAL"*, *"in pure proof of concept and development mode"*, and *"typically worse on cost/quality basis than"* conventional [[DSPyOptimizers|prompt optimization]] — but a *"solid start for online RL over arbitrary LM programs for tiny LMs."* **Bookends the wiki's [[grpo|GRPO]] coverage**: contrast with [[hf-llm-course-ch12-reasoning-models|HF LLM Course Ch 12]]'s single-module `GRPOTrainer` on [[GSM8K]] math and [[2507.19457-gepa|GEPA paper]]'s argument that on PUPA itself GEPA reaches **91.85** vs GRPO's **86.66** with up to 35× fewer rollouts — i.e. this very same program / benchmark / RL-vs-prompt pairing the GEPA paper used to argue *against* GRPO for compound systems.

## Key Claims

- **`dspy.GRPO` exists as a first-class [[DSPyOptimizers|DSPy optimizer]]** alongside [[MIPROv2]] / [[GEPA]] / [[BootstrapFinetune]], surfaced via the experimental **[[ArborGRPO|`ArborGRPO`]] compiler** that wraps the [[Arbor|`arbor-ai`]] distributed-RL framework. Same `compiler.compile(student=program, trainset=..., valset=...)` interface as every other DSPy optimizer.
- **The optimizer targets [[CompoundAISystem|compound AI systems]], not single signatures** — `multitask=True`, `num_dspy_examples_per_grpo_step=4`, `num_samples_per_input=8`. One scalar reward propagates back to *all* trainable modules in the program simultaneously.
- **Reward is a [[LLMJudge|LLM-as-Judge]]**: `compute_overall_score = (quality + (1 − leakage)) / 2`, where `quality` is a [[chainofthought|`dspy.ChainOfThought`]] pairwise judgment vs. a target large-LM response and `leakage` is `num_pii_leaked / |pii|` extracted from the redacted prompt. Both judges run on a stronger external LM (e.g. GPT-4o), the *trained* LM is the local 1.5B model.
- **The local model is a single weight set serving both [[PAPILLON]] modules** — `CraftRedactedRequest` (privacy-preserving query crafter) and `RespondToQuery` (final responder using untrusted-LLM response). Both are routed through the same fine-tuned LM; `exclude_demos=True` keeps few-shot exemplars out of the RL rollouts so the gradient operates on the model's own zero-shot policy.
- **[[LoRA]] is the only thing that moves**: rank-8, α=16, dropout 0.05, targets `["q_proj","k_proj","v_proj","o_proj","up_proj","down_proj","gate_proj"]`. Base weights frozen. `gradient_checkpointing=True`, `bf16=True`, `lr=1e-6`, `lr_scheduler_type="constant_with_warmup"`.
- **`loss_type="dapo"`** (DAPO — Decoupled clip and dynamic sampling Policy Optimization, the GRPO variant that decouples clip ratio + token-level loss; the tutorial uses DAPO not vanilla GRPO).
- **`beta=0.00` — no [[KLPenalty|KL penalty]] to the reference policy.** Pure reward maximization on this run; the tutorial does not justify why beta is zero.
- **`per_device_train_batch_size=8 × gradient_accumulation_steps=4 = 32 effective batch`** × 8 rollouts per prompt × 4 prompts per step = 256 rollout-traces per gradient update. `max_steps=1000` (but `num_train_steps=500` in the ArborGRPO call — the smaller of the two governs).
- **Training infra: [[Arbor]] (`pip install -U arbor-ai`) + DSPy main branch (`pip install -U git+https://github.com/stanfordnlp/dspy.git@main`).** Demonstrated on 4× [[H100]].
- **Dataset split is 225 / 225 / 450** from the [[PUPA]] `pupa_new` HuggingFace dataset — train / dev / test. `pii_units` field comes ||-separated and is `.split("||")` into the PII list the leakage judge counts against.
- **Headline result: 54.6 → 60.0 composite (+5.4 pts absolute, ~9.9% relative) on dev after ~3 h training.** The tutorial reports no test-set number, no variance across seeds, no comparison to [[MIPROv2]] or [[GEPA]] on the same setup.
- **Authors self-disqualify the approach on cost/quality grounds**: *"typically worse on cost/quality basis than"* prompt optimization. The value proposition is *"online RL over arbitrary LM programs for tiny LMs"* — i.e. when prompt-only optimization hits a capability ceiling because the underlying LM is too small for prompt-engineering alone to close the gap.

## Key Quotes

> "new and extremely EXPERIMENTAL"

> "in pure proof of concept and development mode"

> "typically worse on cost/quality basis than" [conventional prompt optimization]

> "a solid start for online RL over arbitrary LM programs for tiny LMs"

> "responses of the local model should be as good as (or better than) the target_response from a large LM" (quality judge directive)

> "training three hours boosts the composite score (devset) from 54.6% to 60.0%"

## Code Receipt

```python
import dspy
from dspy.teleprompt import ArborGRPO

class CraftRedactedRequest(dspy.Signature):
    """Given a private user query, create a privacy-preserving request for a powerful external LLM."""
    user_query = dspy.InputField()
    llm_request = dspy.OutputField()

class RespondToQuery(dspy.Signature):
    """Respond to a user query with inspiration from related LLM request/response."""
    related_llm_request = dspy.InputField()
    related_llm_response = dspy.InputField(desc="information from powerful LLM")
    user_query = dspy.InputField(desc="user's request to fulfill")
    response = dspy.OutputField(desc="final response to user's request")

class PAPILLON(dspy.Module):
    def __init__(self, untrusted_model):
        self.craft_redacted_request = dspy.ChainOfThought(CraftRedactedRequest)
        self.respond_to_query = dspy.Predict(RespondToQuery)
        self.untrusted_model = untrusted_model

    def forward(self, user_query):
        llm_request = self.craft_redacted_request(user_query=user_query).llm_request
        llm_response = self.untrusted_model(llm_request)[0]
        response = self.respond_to_query(
            related_llm_request=llm_request,
            related_llm_response=llm_response,
            user_query=user_query,
        ).response
        return dspy.Prediction(llm_request=llm_request, llm_response=llm_response, response=response)

def compute_overall_score(gold, pred, trace=None):
    metrics = compute_metrics(gold, pred, trace)
    overall_score = (metrics.quality + (1 - metrics.leakage)) / 2.0
    return overall_score >= 1.0 if trace is not None else overall_score

train_kwargs = {
    "per_device_train_batch_size": 8,
    "gradient_accumulation_steps": 4,
    "temperature": 1.0, "top_k": -1, "top_p": 1.0, "repetition_penalty": 1.0,
    "beta": 0.00,                              # no KL to reference policy
    "learning_rate": 1e-6,
    "gradient_checkpointing": True, "bf16": True,
    "lr_scheduler_type": "constant_with_warmup",
    "loss_type": "dapo",                       # DAPO variant of GRPO
    "max_steps": 1000,
    "lora_config": {
        "lora_alpha": 16, "lora_dropout": 0.05, "r": 8,
        "target_modules": ["q_proj","k_proj","v_proj","o_proj",
                           "up_proj","down_proj","gate_proj"],
    },
}

compiler = ArborGRPO(
    metric=compute_overall_score,
    multitask=True,
    num_dspy_examples_per_grpo_step=4,
    num_samples_per_input=8,
    exclude_demos=True,
    num_train_steps=500,
    num_threads=24,
)

optimized_papillon = compiler.compile(student=papillon, trainset=trainset, valset=devset)
```

Dataset:

```python
examples = [
    dspy.Example(
        {"target_response": x["target_response"],
         "user_query":      x["user_query"],
         "pii_str":         x["pii_units"]}
    ).with_inputs("user_query")
    for x in pupa_new["train"]
]
trainset, devset, testset = examples[:225], examples[225:450], examples[450:]
```

## Connections

- [[DSPy]] — host framework; `dspy.GRPO` / `ArborGRPO` exposed alongside [[MIPROv2]] / [[GEPA]] / [[BootstrapFinetune]] under the same `compile(...)` contract.
- [[PAPILLON]] — the privacy-preserving delegation **program** trained here (newly minted concept page).
- [[ArborGRPO]] — the **optimizer** itself (newly minted concept page).
- [[Arbor]] — the underlying `arbor-ai` distributed-RL framework (newly minted entity page).
- [[grpo|GRPO]] — base RL algorithm; this tutorial extends it to multi-module DSPy programs.
- [[DAPO]] — the actual GRPO variant used (`loss_type="dapo"`); newly minted concept page.
- [[PUPA]] — the benchmark used for training and evaluation.
- [[CompoundAISystem]] — the formalism `Φ = (M, C, X, Y)` with learnable `Π_Φ` (prompts) + `Θ_Φ` (weights); this tutorial updates `Θ_Φ` while leaving `Π_Φ` fixed.
- [[DSPyOptimizers]] — adds `dspy.GRPO` / `ArborGRPO` to the catalog under the **LM weights** axis alongside [[BootstrapFinetune]].
- [[chainofthought|ChainOfThought]] / [[DSPyPredict|Predict]] / [[DSPySignatures|Signatures]] / [[DSPyModules|Modules]] — the four DSPy primitives composed into the PAPILLON program.
- [[LoRA]] — the only weight set that moves (rank 8, α 16, all attention + MLP projections).
- [[NVIDIA|H100]] — 4× demonstrated hardware.
- [[LLMJudge]] — pairwise quality + PII-leakage assessment; complementary to verifiable-reward rewards from [[hf-llm-course-ch12-reasoning-models|HF LLM Course Ch 12]].
- [[KLPenalty]] — set to zero (`beta=0.00`) here; contrast with vanilla GRPO / RLHF / [[hf-llm-course-ch12-reasoning-models|HF Ch 12]] which keep a KL term to the reference policy.
- [[hf-llm-course-ch12-reasoning-models|HF LLM Course Ch 12]] — single-module GRPO on [[GSM8K]] with [[VerifiableReward|verifiable rewards]]; this tutorial is the *multi-module + LLM-judge-reward* counterpart.
- [[dspy-rl-multihop-tutorial|DSPy `rl_multihop` tutorial]] — sibling **second** [[ArborGRPO]] receipt in the wiki: trains a 2-module `ResearchHop` (`generate_query` + `append_notes`) on [[HoVer]] 3-hop claims with a **deterministic title-recall reward** instead of an LLM-judge reward; same [[lora|LoRA]] / [[DAPO]] / `beta=0.0` configuration. Same disclaimer: *"typically worse on cost/quality basis than"* prompt optimization.
- [[2507.19457-gepa|GEPA paper (Agrawal et al. 2026)]] — runs **on the same PUPA benchmark** and reports GEPA 91.85 vs [[grpo|GRPO]] 86.66 / [[MIPROv2]] 81.55 / baseline 80.82 (Qwen3 8B), arguing the same RL-on-compound-systems setup demonstrated here is *empirically dominated* by reflective prompt optimization at up to 35× fewer rollouts.
- [[2604.14585-prompt-optimization-coin-flip|Zhang et al. 2026]] — the *"prompt optimization is a coin flip"* paper; orthogonal critique that prompt optimization itself often underperforms zero-shot, so the prompt-vs-RL frontier is genuinely contested.

## Contradictions

- **Headline result vs. GEPA's PUPA numbers** — this tutorial reports 54.6 → 60.0 *composite* on a 1.5B local model after 3 h of GRPO+LoRA. The [[2507.19457-gepa|GEPA paper]] reports GRPO **86.66** on PUPA (Qwen3 8B, 24,000 rollouts) vs GEPA **91.85** and baseline **80.82** — using a different metric scale and a different (larger) underlying model. **The tutorial does not report PUPA's standard GEPA-paper metric**, so the two numbers are not directly comparable; readers should not conflate "60.0 composite" with "60.0 PUPA score". This is a documentation gap, not a contradiction in claim, but warrants explicit flagging.
- **`beta=0.00` (no KL penalty)** contradicts the standard [[grpo|GRPO]] / [[rlhf|RLHF]] / [[hf-llm-course-ch12-reasoning-models|HF Ch 12]] formulation where a non-zero KL anchors the trained policy to the reference. The tutorial offers no justification; one reading is that DAPO's clipping makes the KL term redundant for short LoRA training horizons, another is that the authors are still tuning and `beta=0.00` is provisional.
- **Authors' own cost/quality disclaimer** — the page openly states this approach is *"typically worse on cost/quality basis than"* conventional [[DSPyOptimizers|prompt optimization]], which contradicts the implicit promise of a *tutorial demonstrating online RL for compound AI systems*. The value proposition the page settles on — *"online RL over arbitrary LM programs for tiny LMs"* — is narrower than the headline framing.

## What's new in the wiki after this ingest

- **Mints**: [[PAPILLON]] (program / system), [[ArborGRPO]] (DSPy optimizer), [[Arbor]] (entity — the `arbor-ai` framework), [[DAPO]] (RL algorithm variant), [[LLMJudge]] (DSPy pattern), [[H100]] (entity — NVIDIA accelerator) — *only if not already present; the agent should check before creating each.*
- **Updates**: [[PUPA]] (back-link from PAPILLON tutorial), [[grpo|GRPO]] (mention of `dspy.GRPO` / ArborGRPO multi-module extension + DAPO loss + 4×H100 / 3 h / 225-example training receipt), [[DSPyOptimizers]] (adds `dspy.GRPO`/`ArborGRPO` under the LM-weights axis), [[DSPy]] (RL optimizer surface).

## Stance

This is a *receipt-of-existence* ingest: the tutorial proves `dspy.GRPO` ships and runs end-to-end, with concrete hyperparameters and a measurable lift on a real benchmark. It is **not** a proof of the technique's superiority — the authors themselves disclaim that. Read alongside [[2507.19457-gepa|GEPA]] and [[2604.14585-prompt-optimization-coin-flip|Zhang et al.]] to triangulate when the RL-on-compound-AI-system frontier *is* worth crossing; for now, the wiki's working hypothesis is *prompt-optimization-first, RL only when prompt optimization saturates against an underlying capability ceiling.*
