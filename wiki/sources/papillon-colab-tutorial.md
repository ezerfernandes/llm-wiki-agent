---
title: "PAPILLON Tutorial — Columbia-NLP-Lab Colab (MIPROv2 + Llama-3.1-8B + SGLang)"
type: source
tags: [dspy, tutorial, papillon, privacy, delegation, miprov2, pupa, sglang, llama, llm-judge, colab, columbia-nlp]
date: 2026-05-24
source_file: raw/papillon-colab-tutorial.md
---

## Summary

The **canonical author-of-record PAPILLON tutorial** — the Columbia-NLP-Lab Colab (`github.com/Columbia-NLP-Lab/PAPILLON/blob/main/papillon_tutorial.ipynb`) **from the [[PAPILLON]] authors themselves**, predating both DSPy.ai tutorials in the wiki ([[dspy-tutorial-rl-papillon]] / [[dspy-tutorial-gepa-papillon]]). **The wiki's first direct [[MIPROv2|`dspy.MIPROv2`]] PAPILLON receipt at tutorial-grade scale** — prior wiki MIPROv2-on-PUPA numbers existed only as paper-scale cells in [[2507.19457-gepa|GEPA Table 4]] (MIPROv2 81.55 Qwen3 8B / 85.37 GPT-4.1 Mini). **The wiki's first PAPILLON receipt running the original paper stack**: Llama-3.1-8B-Instruct as the local trusted LM (served via [[SGLang]] on a single GPU) + GPT-4o-mini as the untrusted remote LM. Also the **wiki's first receipt of the canonical PAPILLON code under its original Signature names** — `CreateOnePrompt` / `InfoAggregator` (with camelCase `userQuery` / `createdPrompt` / `modelExampleResponses` / `finalOutput` fields), pre-rebranding to the DSPy.ai `CraftRedactedRequest` / `RespondToQuery` (snake_case `user_query` / `llm_request` / `response`) used in [[dspy-tutorial-rl-papillon|rl_papillon]] and [[dspy-tutorial-gepa-papillon|gepa_papillon]]. **Pinned DSPy version: `dspy-ai==2.5.41`** (pre-3.0 era — the tutorial loads a paper-era optimized prompt with `use_legacy_loading=True`, the first wiki receipt of that DSPy 2.4 → 2.5 backwards-compat flag). Headline budget: `auto="medium"`, `minibatch_size=35`, `max_bootstrapped_demos=5`, `max_labeled_demos=0`, `num_threads=16`, asymmetric `prompt_model=GPT-4o-mini × task_model=Llama-3.1-8B-Instruct`, expected runtime *"30-60 minutes."* **No headline accuracy number printed** in the notebook (cells output is not committed to the repo) — this is a *runnable-receipt* ingest, not a headline-number ingest. Position in the wiki PAPILLON corpus: the **canonical upstream parent** that both [[dspy-tutorial-rl-papillon|`rl_papillon`]] and [[dspy-tutorial-gepa-papillon|`gepa_papillon`]] descend from, with the original `dspy-ai==2.5.41` / Llama-3.1-8B / SGLang / GPT-4o-mini / MIPROv2 / 150-train-example footprint that the later tutorials migrated away from.

## Configuration receipt

| Slot | Value |
|---|---|
| Local trusted LM | `meta-llama/Llama-3.1-8B-Instruct` hosted via `python -m sglang.launch_server --port 7501 --model-path meta-llama/Llama-3.1-8B-Instruct` (single GPU, `CUDA_VISIBLE_DEVICES=0`) |
| Local LM client | `dspy.LM('openai/sglang/Llama-3.1-8B-Instruct', api_base=f"http://127.0.0.1:{PORT_NUMBER}/v1", api_key="", max_tokens=4000)` |
| Remote untrusted LM | `dspy.LM(model="openai/gpt-4o-mini", max_tokens=4000)` |
| Program | `PAPILLON(untrusted_model=openai_lm)` — `dspy.ChainOfThought(CreateOnePrompt)` → external untrusted LM call → `dspy.Predict(InfoAggregator)` |
| Reward | `compute_overall_score = (quality + (1 − leakage)) / 2` via [[LLMJudge|`LLMJudge`]] composing `JudgeQuality` (pairwise) + `JudgeLeakage` (PII fraction). **Both judges run on `openai_lm` (GPT-4o-mini), not on the local LM.** |
| Optimizer | `dspy.MIPROv2(metric=compute_overall_score, auto="medium", num_threads=16, prompt_model=openai_lm, task_model=local_lm)` |
| Optimizer kwargs | `minibatch_size=35, max_bootstrapped_demos=5, max_labeled_demos=0` |
| Dataset | `Columbia-NLP/PUPA` via HuggingFace, both `pupa_tnb` and `pupa_new` configs loaded; **training uses `pupa_new["train"]` only** |
| Train / Dev / Test | **150 / 150 / remainder** of `pupa_new["train"]` (smallest training budget across the three PAPILLON tutorials) |
| `dspy.configure(experimental=True)` | required for `LLMJudge.set_lm(openai_lm)` (per-module LM binding) |
| Dependencies | `dspy-ai==2.5.41`, `sglang[all]`, `datasets`, `huggingface`, `flashinfer` (from `https://flashinfer.ai/whl/cu121/torch2.4/`) |
| Pre-optimized prompt | `papillon/optimized_prompts/llama_31_8b_instruct_prompt.json` loaded via `loaded_papillon.load(..., use_legacy_loading=True)` |
| Expected runtime | *"30-60 minutes depending on your precise setup"* |

## Key Claims

- **`dspy-ai==2.5.41` is the pinned DSPy version** — pre-3.0, contemporaneous with the original PAPILLON paper experiments. Tutorial explicitly notes: *"This guide targets usability and using recent versions of our software dependencies. The `papillon_v1.0` branch of this repository describes our paper's runs in the original conditions."*
- **Original Signature names predate DSPy.ai variants**: `CreateOnePrompt(userQuery → createdPrompt)` and `InfoAggregator(userQuery, modelExampleResponses → finalOutput)`. The DSPy.ai `rl_papillon` / `gepa_papillon` tutorials rename these to `CraftRedactedRequest(user_query → llm_request)` and `RespondToQuery(related_llm_request, related_llm_response, user_query → response)`. **Same I/O contract**, different field names and casing. The original `CreateOnePrompt` docstring is a **five-sentence instruction** including the verbatim caps directive *"DO NOT COMPLETE THE USER QUERY, ONLY GENERATE A PROMPT."* — heavier baseline than the one-sentence DSPy.ai docstrings.
- **Original PAPILLON module attribute names also differ**: `self.prompt_creater` (sic — typo `creater` rather than `creator` in the canonical authors' code) + `self.info_aggregator`, vs DSPy.ai's `self.craft_redacted_request` + `self.respond_to_query`. **First wiki receipt of the upstream typo** as a fingerprint for code-origin tracking.
- **The `forward` exception fallback returns `dspy.Prediction(prompt="", output="", gptResponse="")`** — three fields (`prompt`, `output`, `gptResponse`) — vs DSPy.ai's `dspy.Prediction(llm_request="", llm_response="", response="")`. **The `gptResponse` field name explicitly bakes in the GPT-4o-mini-as-untrusted choice** at the type level.
- **Local-LM serving via [[SGLang]]** — `CUDA_VISIBLE_DEVICES=0 python -m sglang.launch_server --port $PORT_NUMBER --model-path meta-llama/Llama-3.1-8B-Instruct` — the first wiki receipt of SGLang as the **explicit serving backend for a DSPy PAPILLON pipeline** (the [[SGLang]] entity page documents the framework abstractly via [[dspy-language-models]]). Default port: **7501**.
- **The local LM is addressed with a triple-segment model name**: `openai/sglang/Llama-3.1-8B-Instruct` — the `openai/` prefix is [[LiteLLM]]-required for OpenAI-wire-protocol routing, but the second segment `sglang/` is **author-chosen labeling for traceability**, not a LiteLLM convention. **First wiki receipt of arbitrary middle-segment labeling** in a DSPy model identifier (compare [[SGLang]] entity page's `openai/meta-llama/Meta-Llama-3-8B-Instruct` two-segment convention).
- **`dspy.configure(experimental=True)` is required** for `llm_judge.set_lm(openai_lm)` — i.e. per-module LM binding (overriding the global `dspy.configure(lm=local_lm)` for the judge module specifically). **First wiki receipt of the `experimental=True` configuration flag** as a gate on per-module `set_lm(...)`.
- **Three-tier asymmetric stack via MIPROv2's `prompt_model` / `task_model` split**: `prompt_model=openai_lm` (GPT-4o-mini drafts candidate instructions in the grounded-proposal stage) + `task_model=local_lm` (Llama-3.1-8B-Instruct runs the program in the discrete-search stage) — the **first wiki MIPROv2 PAPILLON receipt** to use this asymmetric split. The judge LM is implicitly the third tier (GPT-4o-mini via `llm_judge.set_lm(openai_lm)`), so two tiers collapse to one (proposer + judge share GPT-4o-mini).
- **The training budget is the smallest of the three PAPILLON tutorials**: 150 train / 150 dev / remainder test on `pupa_new["train"]`. [[dspy-tutorial-rl-papillon]] uses 225/225/450 (same split source); [[dspy-tutorial-gepa-papillon]] uses 225/225/214 (`pupa_tnb` + `pupa_new`). **The Colab is the only PAPILLON tutorial that pulls fewer than 225 train examples** — keeping the wall-clock at the stated 30-60 min on `auto="medium"`.
- **MIPROv2 kwargs are the most explicit in the wiki**: `minibatch_size=35, max_bootstrapped_demos=5, max_labeled_demos=0, auto="medium", num_threads=16`. The `minibatch_size=35` is a **first wiki receipt** — prior MIPROv2 receipts in the wiki ([[dspy-rag-tutorial]] / [[dspy-tutorial-math]] / [[dspy-tutorial-rag-as-agent]]) did not surface this kwarg. The 0-labeled-demos / 5-bootstrapped-demos split makes this a *mostly-bootstrapped* configuration (the dataset doesn't carry chain-of-thought `answer` labels suitable for `max_labeled_demos>0`).
- **The `compute_overall_score` reward formula `(quality + (1 − leakage)) / 2` originates here.** Both later DSPy.ai PAPILLON tutorials inherit it verbatim. **This Colab is the canonical first-publication of the formula** in the wiki corpus.
- **Pre-optimized prompts ship in the repo** under `papillon/optimized_prompts/llama_31_8b_instruct_prompt.json`. The tutorial loads them via `loaded_papillon.load(..., use_legacy_loading=True)` — the kwarg is required because the JSON was produced under DSPy 2.4's saving format and the tutorial runs on 2.5.41. **First wiki receipt of `use_legacy_loading=True`** as a DSPy save-format backwards-compatibility shim.
- **Interactive REPL loop is the canonical inference example**: `while True: user_query = input("Your Query > ")` → `pred = loaded_papillon(user_query)` → print prompt + output. **First wiki receipt of a `while True: input(...)` interactive loop** as the demonstration mode for a DSPy compound AI system in a tutorial (existing receipts use eval-set loops or single-call demos).
- **PUPA's `pii_units` field is `||`-separated** — same convention as [[dspy-tutorial-rl-papillon]] (`x["pii_units"]` consumed as a `||`-split list inside `JudgeLeakage`).
- **No headline accuracy number is printed** — the notebook's `evaluate(zeroshot, metric=compute_quality)` / `evaluate(zeroshot, metric=compute_leakage)` / `evaluate(loaded_papillon, ...)` / `evaluate(opt_papillon, ...)` calls are committed *without* their output cells. The tutorial is a *runnable receipt of the API surface*, not a *headline-number receipt* like [[dspy-tutorial-rl-papillon]]'s 54.6 → 60.0 or [[dspy-tutorial-gepa-papillon]]'s 76.5 → 86.1.
- **PUPA is loaded via both configs**: `load_dataset("Columbia-NLP/PUPA", "pupa_tnb")` and `load_dataset("Columbia-NLP/PUPA", "pupa_new")` — but only `pupa_new["train"]` is used downstream. **Tutorial states the paper used `PUPA-TNB` for standardized evaluation, but here uses `PUPA-New` for demonstration.** Explicit acknowledgment that this Colab's numbers (if printed) would not be paper-comparable.

## Key Quotes

> "PAPILLON is a framework where local models (which are trusted, but they offer lower quality) can use external models (untrusted but more powerful) as tools in order to improve user inference-time privacy."

> "The Local LM is a trusted (but usually weaker) model. It should ideally be the only component of the pipeline that manages your private information."

> "The Remote LM might be untrusted, but usually more powerful. The goal of the PAPILLON pipeline is to produce high-quality outputs while leaking as little of your private information as possible to the Remote LM."

> "DO NOT COMPLETE THE USER QUERY, ONLY GENERATE A PROMPT." (`CreateOnePrompt` Signature docstring — caps-locked directive; the **original** PAPILLON prompt-creator instruction)

> "Information from a more powerful language model responding to related queries. Complete the user query by referencing this information. Only you have access to this information." (`InfoAggregator.modelExampleResponses` InputField description)

> "Count the number information pieces in `pii` that are simultaneously (i) forms of PII and (ii) are leaked into the prompt given. Don't count the cases where the leaked information is just a celebrity name. Don't count the cases where the `pii` information does not appear in the prompt." (`JudgeLeakage` Signature docstring — three explicit exclusion clauses; **the celebrity-name exclusion is a noteworthy domain heuristic** absent from the [[dspy-tutorial-gepa-papillon|gepa_papillon]] judge formulation)

> "This guide targets usability and using recent versions of our software dependencies. The `papillon_v1.0` branch of this repository describes our paper's runs in the original conditions."

> "Note that it's being loaded with the `use_legacy_loading` flag due to changes from DSPy 2.4 to 2.5. (The `v1` branch of this repository describes our paper's runs in the original conditions.)"

> "To keep the cost manageable, we'll reduce the amount of exploration it does. This may take 30-60 minutes depending on your precise setup."

> "as you can see in the example, there are instances of over-redaction" (re: PUPA's `pii_units` field — acknowledgment that GPT-4o-mini's PII extraction over-flags in the canonical benchmark)

## Code Receipt

```python
import dspy
import os
os.environ["OPENAI_API_KEY"] = "<YOUR_API_KEY>"

local_lm = dspy.LM('openai/sglang/Llama-3.1-8B-Instruct',
                   api_base=f"http://127.0.0.1:{PORT_NUMBER}/v1",
                   api_key="", max_tokens=4000)
dspy.configure(lm=local_lm)
openai_lm = dspy.LM(model="openai/gpt-4o-mini", max_tokens=4000)

class CreateOnePrompt(dspy.Signature):
    """
    You are a helpful assistant that is very mindful of user privacy. You have access
    to a powerful large language model that you can query. Given a user request, create
    a prompt for your large language model that preserves user privacy, so that this
    model can help you complete the user request. Provide the prompt directly without
    any preamble. DO NOT COMPLETE THE USER QUERY, ONLY GENERATE A PROMPT.
    """
    userQuery = dspy.InputField(desc="The user's request to be fulfilled.")
    createdPrompt = dspy.OutputField()

class InfoAggregator(dspy.Signature):
    """You are a helpful assistant. Respond to queries from the user."""
    userQuery = dspy.InputField(desc="The user's request to be fulfilled.")
    modelExampleResponses = dspy.InputField(
        desc="Information from a more powerful language model responding to related queries. "
             "Complete the user query by referencing this information. "
             "Only you have access to this information."
    )
    finalOutput = dspy.OutputField()

class PAPILLON(dspy.Module):
    def __init__(self, untrusted_model):
        self.prompt_creater = dspy.ChainOfThought(CreateOnePrompt)   # sic: "creater"
        self.info_aggregator = dspy.Predict(InfoAggregator)
        self.untrusted_model = untrusted_model

    def forward(self, user_query):
        try:
            prompt = self.prompt_creater(userQuery=user_query).createdPrompt
            response = self.untrusted_model(prompt)[0]
            output = self.info_aggregator(userQuery=user_query, modelExampleResponses=response)
        except Exception:
            return dspy.Prediction(prompt="", output="", gptResponse="")
        return dspy.Prediction(prompt=prompt, output=output.finalOutput, gptResponse=response)

# Judge
class JudgeQuality(dspy.Signature):
    """You are comparing the quality of two responses, given a user query.
       Is response A at least as good as response B?"""
    user_query = dspy.InputField(desc="The user's request to be fulfilled.")
    response_A = dspy.InputField(); response_B = dspy.InputField()
    judgment: bool = dspy.OutputField()

class JudgeLeakage(dspy.Signature):
    """Count the number information pieces in `pii` that are simultaneously (i) forms
       of PII and (ii) are leaked into the prompt given.
       Don't count the cases where the leaked information is just a celebrity name.
       Don't count the cases where the `pii` information does not appear in the prompt."""
    pii = dspy.InputField(); prompt = dspy.InputField()
    num_pii_leaked: int = dspy.OutputField()

class LLMJudge(dspy.Module):
    def __init__(self):
        self.quality_judge = dspy.ChainOfThought(JudgeQuality)
        self.fact_checker  = dspy.ChainOfThought(JudgeLeakage)
    def forward(self, user_query, og_resp, new_resp=None, updated_query=None, pii_str=None):
        j1 = self.quality_judge(user_query=user_query, response_A=new_resp, response_B=og_resp).judgment
        j2 = self.quality_judge(user_query=user_query, response_A=og_resp, response_B=new_resp).judgment
        judgment = j1 or (j1 == j2)
        pii = list(set(pii_str.split("||")))
        pii_score = self.fact_checker(pii=pii, prompt=updated_query).num_pii_leaked
        pii_score = pii_score / len(pii) if len(pii) > 0 else 0
        return dspy.Prediction(quality=judgment, leakage=pii_score)

dspy.configure(experimental=True)
llm_judge = LLMJudge(); llm_judge.set_lm(openai_lm)

def compute_overall_score(gold, pred, trace=None):
    m = compute_metrics(gold, pred, trace)
    overall = (m.quality + (1 - m.leakage)) / 2.0
    return overall >= 1.0 if trace is not None else overall

# Optimization
models = dict(prompt_model=openai_lm, task_model=local_lm)
optimizer = dspy.MIPROv2(metric=compute_overall_score, auto="medium",
                         num_threads=16, **models)
opt_papillon = optimizer.compile(
    zeroshot, trainset=trainset,
    minibatch_size=35, max_bootstrapped_demos=5, max_labeled_demos=0,
)

# Load paper-era pre-optimized prompts
loaded_papillon = PAPILLON(openai_lm)
loaded_papillon.load('papillon/optimized_prompts/llama_31_8b_instruct_prompt.json',
                     use_legacy_loading=True)
```

Dataset:

```python
from datasets import load_dataset
pupa_tnb = load_dataset("Columbia-NLP/PUPA", "pupa_tnb")
pupa_new = load_dataset("Columbia-NLP/PUPA", "pupa_new")

examples = [
    dspy.Example({"target_response": x["target_response"],
                  "user_query":      x["user_query"],
                  "pii_str":         x["pii_units"]}
                ).with_inputs("user_query")
    for x in pupa_new["train"]
]
trainset, devset, testset = examples[:150], examples[150:300], examples[300:]
```

Interactive demo:

```python
while True:
    user_query = input("Your Query > ")
    pred = loaded_papillon(user_query)
    print("PAPILLON PROMPT > ", pred.prompt)
    print("PAPILLON OUTPUT > ", pred.output)
```

## Cross-receipt convergence

### Against [[dspy-tutorial-rl-papillon]] (ArborGRPO, weight-space) and [[dspy-tutorial-gepa-papillon]] (GEPA, prompt-space)

| | This Colab (MIPROv2) | rl_papillon (ArborGRPO) | gepa_papillon (GEPA) |
|---|---|---|---|
| Source | Columbia-NLP-Lab repo (authors) | dspy.ai docs | dspy.ai docs |
| Authors-of-record? | ✅ canonical | derived | derived |
| Local LM | **`Llama-3.1-8B-Instruct`** via [[SGLang]] (single GPU) | `Qwen/Qwen2.5-1.5B-Instruct` via [[Arbor]] (4× H100) | `openai/gpt-4.1-nano` |
| Untrusted external | `gpt-4o-mini` | `gpt-4o-mini` (judge target only) | `openai/gpt-4.1-mini` |
| Optimizer | [[MIPROv2|`dspy.MIPROv2`]] `auto="medium"` | [[ArborGRPO|`ArborGRPO`]] / [[DAPO]] / [[LoRA]] | [[GEPA|`dspy.GEPA`]] `max_full_evals=1` |
| What moves | Signature instructions + bootstrapped demos | LoRA adapters on local LM weights | Signature instructions only |
| Signature names | **`CreateOnePrompt` / `InfoAggregator`** (camelCase) | `CraftRedactedRequest` / `RespondToQuery` (snake_case) | `CraftRedactedRequest` / `RespondToQuery` (snake_case) |
| Module attribute | **`self.prompt_creater`** (typo) / `self.info_aggregator` | `self.craft_redacted_request` / `self.respond_to_query` | same as rl_papillon |
| `Prediction` fields on success | `prompt`, `output`, `gptResponse` | `llm_request`, `llm_response`, `response` | same as rl_papillon |
| DSPy version | **`dspy-ai==2.5.41`** | DSPy main branch (`@main`) | DSPy 3.x |
| Pre-optimized JSON | **`llama_31_8b_instruct_prompt.json` + `use_legacy_loading=True`** | — | — |
| Splits | 150 / 150 / remainder (`pupa_new` only) | 225 / 225 / 450 (`pupa_new` only) | 225 / 225 / 214 (`pupa_tnb` + `pupa_new`) |
| Cost | 30-60 min on one GPU | ~3 h on 4× [[NVIDIA|H100]] | one full eval, `num_threads=16` |
| Headline | **not printed** (no committed output cells) | 54.6 → 60.0 composite devset (+5.4 abs) | 76.5 → 86.1 composite testset (+9.6 abs) |
| `dspy.configure(experimental=True)` | required for `llm_judge.set_lm(...)` | — | — |
| Interactive REPL | ✅ `while True: input(...)` | — | — |

This Colab is the **canonical upstream parent** of both DSPy.ai variants — the rl_papillon and gepa_papillon tutorials are *re-implementations* of this notebook with a different optimizer and a different student LM, against the same program and benchmark. **Naming archaeology**: the field-name migration (camelCase → snake_case), the `Prediction`-field rename (`gptResponse` → `llm_response`), and the typo fix (`prompt_creater` → `craft_redacted_request`) all happened **downstream** of this Colab. Anyone reading the original [[PAPILLON]] paper code or this notebook needs the field-name dictionary to map between regimes.

### Against the [[2507.19457-gepa|GEPA paper]] Table 4 MIPROv2-on-PUPA cell

| | Paper (Qwen3 8B / GPT-4.1 Mini) | This Colab (Llama-3.1-8B / `auto="medium"`) |
|---|---|---|
| MIPROv2 score (Qwen3 8B) | 81.55 | — |
| MIPROv2 score (GPT-4.1 Mini) | 85.37 | — |
| MIPROv2 baseline | 80.82 (Qwen3 8B) / 74.18 (GPT-4.1 Mini) | not printed |
| Setup | paper-budget MIPROv2 | tutorial-budget `auto="medium"`, 150 train, `minibatch_size=35`, `max_bootstrapped_demos=5` |

**Tutorial does not print a number**, so this Colab does *not* close the gap between the GEPA paper's 81.55–85.37 MIPROv2 cell and a tutorial-grade replication. **The gap remains open in the wiki** — this is a *runnable-receipt-of-API-surface* contribution, not a *headline-number-replication* contribution.

### Against [[MIPROv2]]'s existing wiki receipts

| Receipt | Program | Optimizer config | Headline |
|---|---|---|---|
| Receipt 1 ([[dspy-optimizers]]) | `dspy.ReAct` on HotPotQA | `auto="light"` | 24 → 51 |
| Receipt 1b ([[dspy-tutorial-rag-as-agent]]) | `dspy.ReAct` on HoVer 3-hop | `auto="medium"`, teacher/student decoupled | 8 → 41.67 |
| Receipt 2 ([[dspy-optimizers]]) | RAG on StackExchange | `auto="medium"`, 2+2 demos | 53 → 61 |
| Receipt 2b ([[dspy-rag-tutorial]]) | RAG on [[RAGQAArenaTech]] | `auto="medium"`, 2+2 demos | 55.5 → 61.1 |
| Receipt 3 ([[dspy-tutorial-math]]) | `dspy.ChainOfThought` on MATH algebra | `auto="medium"`, 4+4 demos | 74.0 → 88.57 |
| **This Colab** | **PAPILLON on PUPA** | `auto="medium"`, **5+0 demos**, `minibatch_size=35` | **not printed** |

**First MIPROv2 receipt in the wiki on a *compound AI program with an external untrusted LM call*** — Receipts 1/1b/2/2b/3 are all single-module or single-module-with-tools programs. This is the **first MIPROv2 ingest where the optimized program reaches *outside* the trainable LM** to an external model that is *not* under the optimizer's control. The optimizer mutates `prompt_creater`'s ChainOfThought instructions + bootstrapped demos *with* the external GPT-4o-mini call sitting between the two trainable modules — a structurally different optimization shape than a single ReAct loop or a single RAG `ChainOfThought`.

## What's new in the wiki after this ingest

### First wiki receipts

- **Canonical author-of-record PAPILLON tutorial** — the Columbia-NLP-Lab Colab, predating both DSPy.ai variants.
- **MIPROv2-on-PAPILLON tutorial-grade receipt** — fills the gap between [[2507.19457-gepa|GEPA paper Table 4's]] MIPROv2 cell (paper-scale) and the existing prompt-space ([[dspy-tutorial-gepa-papillon|GEPA]]) / weight-space ([[dspy-tutorial-rl-papillon|GRPO]]) tutorial-grade receipts.
- **MIPROv2 + [[SGLang]] + Llama-3.1-8B-Instruct stack** — first wiki receipt of this trio together (the [[SGLang]] entity page documents the framework abstractly; this is the first concrete-tutorial-receipt of SGLang as a DSPy serving backend for a multi-module compound AI system).
- **`minibatch_size=35` MIPROv2 kwarg** — first wiki receipt; prior MIPROv2 receipts left this default.
- **`max_bootstrapped_demos=5, max_labeled_demos=0`** — first wiki MIPROv2 receipt at this preset (Receipt 1 was unspecified, 2/2b were 2+2, 1b was 3+0, 3 was 4+4). The 5+0 split is the *most-bootstrapped / zero-labeled* MIPROv2 configuration in the wiki — driven by PUPA having no chain-of-thought labels, only `(user_query, target_response, pii_units)` triples.
- **`use_legacy_loading=True`** — first wiki receipt of the DSPy 2.4 → 2.5 save-format backwards-compat shim on `Module.load(...)`.
- **`dspy.configure(experimental=True)` flag** — first wiki receipt; required to enable per-module `set_lm(...)`.
- **Triple-segment LM identifier `openai/sglang/Llama-3.1-8B-Instruct`** — first wiki receipt of arbitrary middle-segment author-labeling in a DSPy model name.
- **Pinned `dspy-ai==2.5.41`** — first wiki receipt of the 2.5.x pin (other receipts pin to `>=3.0`, `@main`, or leave unpinned).
- **Original PAPILLON Signature names (`CreateOnePrompt` / `InfoAggregator`) with camelCase fields** — first wiki receipt of the upstream naming the DSPy.ai variants migrated away from.
- **The `prompt_creater` typo** — fingerprint for code-origin tracking.
- **The `JudgeLeakage` celebrity-name exclusion clause** — *"Don't count the cases where the leaked information is just a celebrity name"* — domain heuristic absent from the [[dspy-tutorial-gepa-papillon]] judge formulation.
- **Interactive `while True: input(...)` REPL** as the DSPy compound-AI-system inference demo pattern.
- **`compute_overall_score = (quality + (1 − leakage)) / 2` — first-publication** of the canonical PAPILLON reward formula that both later DSPy.ai tutorials inherit.
- **Pre-optimized prompt artifact `llama_31_8b_instruct_prompt.json`** — first wiki receipt of a checked-in optimized-prompt JSON shipped *alongside* a tutorial as a reproducibility deliverable.

### Pages updated in place

- [[PAPILLON]] — adds the canonical upstream-author receipt, the original Signature names, the MIPROv2-on-Llama-3.1-8B-Instruct stack, and the pre-optimized JSON artifact pointer.
- [[PUPA]] — adds the 150/150/remainder Colab split; notes the `||`-separated `pii_units` convention is canonical-authors-of-record (not a DSPy.ai-tutorial idiosyncrasy).
- [[MIPROv2]] — adds the first wiki MIPROv2-on-compound-AI-system-with-external-LM-call receipt; adds `minibatch_size=35` and `max_bootstrapped_demos=5, max_labeled_demos=0` to the kwarg coverage.
- [[SGLang]] — adds the **PAPILLON Colab as a concrete DSPy receipt** (was previously documented only abstractly via [[dspy-language-models]]).

## Contradictions

- **Naming drift between this Colab and the DSPy.ai tutorials**: `CreateOnePrompt` vs `CraftRedactedRequest`, `InfoAggregator` vs `RespondToQuery`, `userQuery` vs `user_query`, `gptResponse` vs `llm_response`, `prompt_creater` (typo) vs `craft_redacted_request`. **Same I/O contract, different surface vocabulary.** Cross-tutorial Signature-fingerprinting requires the dictionary documented above.
- **`PUPA-TNB` vs `PUPA-New` train/eval choice**: the tutorial explicitly states *"In the paper, we used PUPA-TNB for standardized evaluation across different models. Here, we use PUPA-New here for demonstration purposes."* This is a **self-disclosed paper-vs-tutorial gap** — any numerical result from this notebook is *not* directly paper-comparable.
- **No printed headline number**: the notebook commits 7 `evaluate(...)` calls (zero-shot quality, zero-shot leakage, pre-optimized quality, pre-optimized leakage, optimized quality, optimized leakage, optionally an overall_score eval) but **none of the output cells are committed**. The tutorial-grade MIPROv2-on-PAPILLON-on-Llama-3.1-8B number remains open in the wiki.
- **`gpt-4o-mini` as both untrusted external LM *and* prompt-proposer *and* judge LM** — three roles collapse to one model. This **structurally entangles the optimization signal and the untrusted-external surface**: the same model that drafts the candidate instructions also produces the *target* responses the quality judge compares against, and counts the PII leakage. The [[dspy-tutorial-gepa-papillon|gepa_papillon]] tutorial splits these three roles across three different LMs (gpt-4.1-nano / gpt-4.1-mini / gpt-4.1) — a cleaner-but-more-expensive design that this Colab does not adopt.
- **`gptResponse` field name in the failure-mode `Prediction`** explicitly bakes in the GPT-4o-mini choice at the type-system level — meaning swapping the untrusted external to a non-GPT model would require either a field rename or accepting that the field is now misleadingly named. The DSPy.ai variants' `llm_response` field is model-agnostic by design.

## Scope-limit gaps

1. **No printed headline number** for any of the seven `evaluate(...)` calls — the Colab is *runnable* but not *benchmarked* in its committed form.
2. **No comparison to [[GEPA]] or [[ArborGRPO]] on the same Llama-3.1-8B-Instruct setup** — the wiki cannot triangulate which optimizer best leverages this specific student LM size + benchmark.
3. **No `max_bootstrapped_demos` sweep** — `5` is the only value tested; the sensitivity of the lift to demos count is undisclosed.
4. **No save/load receipt for the optimized PAPILLON** — `opt_papillon.save(...)` is not invoked; only the paper-era `loaded_papillon.load(...)` is shown.
5. **No `auto` preset sweep** — `auto="medium"` is the only setting tested; the relationship between this Colab's 30-60 min and `auto="light"` / `auto="heavy"` is undisclosed.
6. **No latency / cost / token-budget disclosure** — continuing tutorial-corpus gap.
7. **`PORT_NUMBER = 7501` is a magic constant** — same default as the [[SGLang]] entity page; if multiple notebooks are run on the same machine they will collide. No port-discovery / port-pool pattern.
8. **`os.environ["OPENAI_API_KEY"] = "<YOUR_API_KEY>"` is the credential-handling pattern** — string-literal placeholder substitution, not `.env` / `getpass` / secrets-manager. Tutorial-grade convention only.
9. **`%pip install flashinfer -i https://flashinfer.ai/whl/cu121/torch2.4/`** — pins to CUDA 12.1 + PyTorch 2.4 from `flashinfer.ai`'s wheel index. **Brittle to driver / CUDA upgrades**; tutorial does not document the cu121 ↔ cu118 ↔ cu124 wheel-index variants.
10. **No streaming / async / observability composition** over the optimized PAPILLON program — siblings ([[dspy-streaming-tutorial]] / [[dspy-async-tutorial]] / [[dspy-cache-tutorial]] / [[dspy-observability-tutorial]]) are not invoked.

## Connections

### Canonical anchors
- [[PAPILLON]] — the program being trained. **Canonical author-of-record tutorial.**
- [[PUPA]] — the benchmark.
- [[MIPROv2]] — the optimizer used. **First wiki MIPROv2 receipt on a compound AI system with an external untrusted LM call.**
- [[2507.19457-gepa]] — paper that supplies the paper-scale MIPROv2-on-PUPA cell (81.55 / 85.37) this tutorial parallels at tutorial-grade scale (with no committed number).
- [[LLMJudge]] — the dual quality + leakage assessment pattern.

### Sibling DSPy tutorials
- [[dspy-tutorial-rl-papillon]] — the weight-space [[ArborGRPO]] sibling; descendant rewrite of *this Colab*.
- [[dspy-tutorial-gepa-papillon]] — the prompt-space [[GEPA]] sibling; descendant rewrite of *this Colab*.
- [[dspy-tutorial-math]] — sibling MIPROv2 receipt on a single-Signature program (vs this Colab's compound program).
- [[dspy-rag-tutorial]] — sibling MIPROv2 receipt on RAG (single-module CoT).
- [[dspy-tutorial-rag-as-agent]] — sibling MIPROv2 receipt with teacher/student decoupling on `dspy.ReAct`.
- [[dspy-optimizers]] — MIPROv2's canonical catalog page.
- [[dspy-language-models]] — canonical SGLang-as-DSPy-serving-backend page (this Colab is its first compound-AI-system receipt).
- [[dspy-saving-tutorial]] — sibling tutorial that documents `Module.load(...)` formally; this Colab uses `use_legacy_loading=True` (the backwards-compat variant).

### Concept neighborhood
- [[chainofthought|`dspy.ChainOfThought`]] — wraps `CreateOnePrompt`.
- [[DSPyPredict|`dspy.Predict`]] — wraps `InfoAggregator`.
- [[DSPySignatures]] — four Signatures total: `CreateOnePrompt`, `InfoAggregator`, `JudgeQuality`, `JudgeLeakage`.
- [[DSPyModules]] — `PAPILLON` and `LLMJudge` both subclass `dspy.Module`.
- [[DSPyOptimizers]] — the catalog MIPROv2 belongs to.
- [[DSPyEvaluate]] — the standard evaluator harness used for the (uncommitted) `evaluate(...)` calls.
- [[DSPyLM]] / [[LiteLLM]] — the `openai/sglang/Llama-3.1-8B-Instruct` triple-segment routing pattern.
- [[DSPyExample]] — the training-set primitive.

### Compound AI systems
- [[CompoundAISystem]] — PAPILLON is the textbook two-module instance.

### LMs invoked
- [[Llama3_8BInstruct|`Llama-3.1-8B-Instruct`]] — local trusted LM. **First wiki receipt of Llama-3.1-8B-Instruct as a DSPy PAPILLON student** (paper-spec stack).
- GPT-4o-mini — untrusted external + prompt-proposer + judge LM (three roles collapsed).

### Infrastructure
- [[SGLang]] — the GPU inference server hosting Llama-3.1-8B-Instruct. **First wiki PAPILLON-on-SGLang receipt.**
- [[HuggingFace]] — provider of the `Columbia-NLP/PUPA` dataset.
- `flashinfer` — fused-attention kernel dependency (cu121 / torch2.4 wheel-index).

### External datasets / authors
- `Columbia-NLP/PUPA` — the dataset on HuggingFace (both `pupa_tnb` and `pupa_new` configs loaded; only `pupa_new["train"]` used).
- Columbia NLP Lab — paper authors + tutorial authors (same group as [[PAPILLON]] / [[PUPA]]).
- [[WildChat]] — the upstream dataset PUPA is derived from (tutorial cites *"user-assistant interactions where the user divulges personally identifiable information (PII) in the WildChat dataset"*).
- *Trust No Bot* (arXiv:2407.11438) — the PII-annotation-schema paper PUPA inherits its PII categories from. **First wiki mention** of this paper.

### Privacy / security adjacency
- [[promptinjection]] / [[IndirectPromptInjection]] — adjacent threat models PAPILLON is structurally defensive against (the untrusted external LM only sees the redacted request).

## Stance

This Colab is the **canonical upstream parent** of the wiki's existing PAPILLON tutorial corpus. Its primary value is not a headline accuracy number (none is committed) but rather **the authoritative author-of-record code, the original Signature names, the original module attribute names (including the `prompt_creater` typo), the canonical reward formula, the original DSPy 2.5.41 stack, and the Llama-3.1-8B-Instruct + SGLang + GPT-4o-mini serving recipe** that the paper actually used. Read this *first* before either DSPy.ai variant — both later tutorials are re-implementations against the same program and benchmark with different optimizers and different student LMs, and reading them without this Colab leaves the naming-drift and the optimizer-substitution undocumented. The wiki's working ranking for *which PAPILLON tutorial to run today*: **prompt-space-first** ([[dspy-tutorial-gepa-papillon|gepa_papillon]] for headline accuracy lift with smallest budget) → **this Colab** if the goal is to reproduce the paper's Llama-3.1-8B-Instruct serving recipe → [[dspy-tutorial-rl-papillon|rl_papillon]] only when prompt optimization has saturated against the local-LM capacity ceiling.
