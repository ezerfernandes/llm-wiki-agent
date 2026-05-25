---
title: "PAPILLON"
type: concept
tags: [dspy, privacy, delegation, compound-ai, llm-systems, papillon]
sources: [papillon-colab-tutorial, dspy-tutorial-rl-papillon, dspy-tutorial-gepa-papillon, 2507.19457-gepa]
last_updated: 2026-05-24
---

# PAPILLON

**Privacy-preserving LLM delegation** program. A trusted (often smaller) local LM constructs a *redacted* request to a powerful external (potentially untrusted) LLM, then composes the external response with the original private query to produce a final answer — the goal is to extract the external LLM's capability *without* exposing the user's PII.

The **canonical author-of-record receipt** is the [[papillon-colab-tutorial|Columbia-NLP-Lab Colab tutorial]] — written by the [[PAPILLON]] authors themselves on the paper's `dspy-ai==2.5.41` / Llama-3.1-8B-Instruct / [[SGLang]] / GPT-4o-mini / [[MIPROv2|`dspy.MIPROv2`]] stack, with the original Signature names `CreateOnePrompt(userQuery → createdPrompt)` and `InfoAggregator(userQuery, modelExampleResponses → finalOutput)` (camelCase). The DSPy.ai variants ([[dspy-tutorial-rl-papillon|`rl_papillon`]] / [[dspy-tutorial-gepa-papillon|`gepa_papillon`]]) are **downstream re-implementations** that rename the Signatures to `CraftRedactedRequest(user_query → llm_request)` and `RespondToQuery(...)` (snake_case), substitute the optimizer ([[MIPROv2]] → [[ArborGRPO]] / [[GEPA]]), and change the student LM (Llama-3.1-8B → Qwen2.5-1.5B / GPT-4.1-Nano). **Cross-tutorial Signature-fingerprinting requires the field-name dictionary documented on [[papillon-colab-tutorial]].**

The two-module [[CompoundAISystem|compound AI program]] expressed in the DSPy.ai naming convention:

```python
class PAPILLON(dspy.Module):
    def __init__(self, untrusted_model):
        self.craft_redacted_request = dspy.ChainOfThought(CraftRedactedRequest)
        self.respond_to_query       = dspy.Predict(RespondToQuery)
        self.untrusted_model        = untrusted_model

    def forward(self, user_query):
        llm_request  = self.craft_redacted_request(user_query=user_query).llm_request
        llm_response = self.untrusted_model(llm_request)[0]
        response     = self.respond_to_query(
            related_llm_request=llm_request,
            related_llm_response=llm_response,
            user_query=user_query,
        ).response
        return dspy.Prediction(llm_request=llm_request, llm_response=llm_response, response=response)
```

Two trainable [[DSPyModules|modules]] (`CraftRedactedRequest`, `RespondToQuery`) share a single local LM; one untrusted external LM call sits between them. The corresponding benchmark is **[[PUPA]]** (Privacy-Utility Pareto, Li et al. 2025a) — same authors as PAPILLON.

## Two evaluation axes

PAPILLON is judged on both axes simultaneously via an [[LLMJudge]]:

1. **Quality** — pairwise judgment that the local model's response is "as good as (or better than) the target_response from a large LM"
2. **Privacy leakage** — fraction `num_pii_leaked / |pii|` of PII units that appear in the redacted external request

Composite reward: $\text{score} = (\text{quality} + (1 - \text{leakage})) / 2$.

## Training surfaces

| Surface | Receipt | Headline number |
|---|---|---|
| [[grpo|GRPO]] online RL via [[ArborGRPO]] / `dspy.GRPO` | [[dspy-tutorial-rl-papillon]] | Composite **54.6 → 60.0** on devset (Qwen2.5-1.5B-Instruct), ~3 h on 4× [[NVIDIA|H100]] |
| [[GEPA]] reflective prompt optimization (DSPy tutorial) | [[dspy-tutorial-gepa-papillon]] | Composite **76.5 → 86.1** on testset (GPT-4.1 Nano student × GPT-4.1 reflection), `max_full_evals=1` |
| [[GEPA]] reflective prompt optimization (paper) | [[2507.19457-gepa]] (Table 4) | PUPA **80.82 → 91.85** on Qwen3 8B; **74.18 → 96.46** on GPT-4.1 Mini (with [[SystemAwareMerge|Merge]]) |
| [[MIPROv2]] reference-optimizer (paper) | [[2507.19457-gepa]] (Table 4) | **81.55** (Qwen3 8B) / **85.37** (GPT-4.1 Mini) |
| [[MIPROv2]] (Colab tutorial — authors-of-record) | [[papillon-colab-tutorial]] | **not printed** — runnable receipt only; `auto="medium"`, `minibatch_size=35`, `max_bootstrapped_demos=5, max_labeled_demos=0`, 150 train, ~30–60 min on one GPU |
| Vanilla GRPO (24,000 rollouts) | [[2507.19457-gepa]] (Table 4) | **86.66** (Qwen3 8B) |

The [[2507.19457-gepa|GEPA paper]] uses PAPILLON+PUPA as one of its strongest *reflective-prompt-mutation > weight-RL* demonstrations: with **up to 35× fewer rollouts** GEPA reaches +5.19 over GRPO on Qwen3 8B; on GPT-4.1 Mini the comparison is prompt-only (no GRPO). [[dspy-tutorial-gepa-papillon|The official `gepa_papillon` tutorial]] supplies the **tutorial-grade GEPA receipt** at the GPT-4.1 Nano student level (one tier smaller than the paper's GPT-4.1 Mini cell) — the **wiki's first direct DSPy `dspy.GEPA` receipt on PAPILLON**, complementing the paper-scale numbers above.

### Prompt-space vs weight-space, same program

[[dspy-tutorial-gepa-papillon]] and [[dspy-tutorial-rl-papillon]] form the **wiki's first side-by-side prompt-space vs weight-space pair** on the same compound AI program + benchmark family. The two are **not directly head-to-head comparable** — different student models (GPT-4.1 Nano vs Qwen2.5-1.5B), different test sets ([[PUPA]] `pupa_tnb`+`pupa_new` 214-item vs `pupa_new`-only 450-item), and different baselines (76.5 vs 54.6) — but the **directional ordering** (prompt-space lift larger, cheaper, and structurally simpler at this program shape) matches the GEPA paper's central thesis. Tutorial-grade scale, paper-scale corroboration.

## Connections

- [[papillon-colab-tutorial]] — **the canonical author-of-record Colab tutorial** from the Columbia-NLP-Lab repo; the upstream parent of both DSPy.ai variants. Original `CreateOnePrompt` / `InfoAggregator` Signature names; `dspy-ai==2.5.41` + Llama-3.1-8B-Instruct via [[SGLang]] + GPT-4o-mini stack; [[MIPROv2|`dspy.MIPROv2`]] `auto="medium"`, `minibatch_size=35`, `max_bootstrapped_demos=5, max_labeled_demos=0`; loads `papillon/optimized_prompts/llama_31_8b_instruct_prompt.json` via `use_legacy_loading=True`. **The wiki's first MIPROv2-on-PAPILLON tutorial-grade receipt** — paper-scale numbers from the [[2507.19457-gepa|GEPA paper]] (MIPROv2 81.55 Qwen3 8B / 85.37 GPT-4.1 Mini) parallel the Colab's `auto="medium"` setup but the Colab does not commit a headline number.
- [[dspy-tutorial-rl-papillon]] — the DSPy `rl_papillon` tutorial; the [[ArborGRPO]] weight-space receipt.
- [[dspy-tutorial-gepa-papillon]] — the DSPy `gepa_papillon` tutorial; the [[GEPA]] prompt-space receipt. **Sibling** to the rl_papillon tutorial on the same program + benchmark family, different optimizer; 76.5 → 86.1 at `max_full_evals=1`.
- [[dspy-rl-multihop-tutorial]] — sibling second [[ArborGRPO]] receipt; trains a 2-module `ResearchHop` on [[HoVer]] 3-hop claims with a deterministic title-recall reward instead of an [[LLMJudge|LLM-judge composite]].
- [[PUPA]] — the benchmark PAPILLON is trained / evaluated on.
- [[ArborGRPO]] — the multi-module GRPO optimizer used in the tutorial.
- [[grpo|GRPO]] — the underlying RL algorithm.
- [[GEPA]] / [[2507.19457-gepa]] — the prompt-optimization alternative that empirically dominates GRPO on PUPA.
- [[LLMJudge]] — the dual quality + leakage assessment pattern PAPILLON uses for its reward.
- [[CompoundAISystem]] — PAPILLON is a textbook two-module compound AI system.
- [[chainofthought|ChainOfThought]] — the [[DSPyModules|module]] type wrapping `CraftRedactedRequest`.
- [[DSPyPredict|dspy.Predict]] — the module type wrapping `RespondToQuery`.
- [[DSPySignatures]] — `CraftRedactedRequest` + `RespondToQuery` are the two signatures defining the program's input/output contract.
