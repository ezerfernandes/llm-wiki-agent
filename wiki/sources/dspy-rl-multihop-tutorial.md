---
title: "DSPy Tutorial — Online RL for Multi-Hop Research (GRPO over HoVer)"
type: source
tags: [dspy, tutorial, rl, grpo, multi-hop, hover, bm25, arbor, qwen, lora, online-rl, dapo]
date: 2026-05-24
source_file: raw/dspy-rl-multihop-tutorial.md
---

## Summary

Official [[DSPy]] tutorial at `https://dspy.ai/tutorials/rl_multihop/` — labeled **"extremely EXPERIMENTAL ... pure proof of concept"** — that runs [[grpo|GRPO]] (via [[ArborGRPO|`dspy.ArborGRPO`]]) against a 2-hop [[chainofthought|`dspy.ChainOfThought`]] retrieval program over [[HoVer]] three-hop claims with a [[BM25|BM25]] retriever over the 2017 Wikipedia abstracts corpus. **Second wiki receipt of [[ArborGRPO]] / [[Arbor]] / [[DAPO]]** after [[dspy-tutorial-rl-papillon]] (which trained [[PAPILLON]] on [[PUPA]] for privacy-preserving delegation). This tutorial moves the RL surface from a **2-module privacy-delegation chain** to a **2-hop retrieval program**, swapping an [[LLMJudge|LLM-as-judge composite reward]] for a **deterministic title-recall metric**. **First wiki receipts within this tutorial**: `ResearchHop` as the 2-hop generate-query / append-notes program shape; **`program.set_lm(...)`** as the per-program LM-binding API distinct from global `dspy.configure(lm=...)`; `ArborProvider()` + `arbor:` model-name prefix as the explicit [[DSPyLM|`dspy.LM(...)`]] binding form for Arbor-backed RL training; [[HoVer]] as a *weight-space RL* optimization target (prior HoVer DSPy receipt was [[dspy-tutorial-rag-as-agent|MIPROv2 over a `dspy.ReAct` agent]]); the `bm25s` + `PyStemmer` in-process [[BM25|BM25]] retriever as the indexing path (prior wiki BM25 receipts used `rank_bm25.BM25Okapi` ([[hands-on-llm-ch08-semantic-search-and-rag|Hands-On LLMs Ch 8]]) or [[ColBERTv2]] ([[dspy-custom-module]] / [[dspy-tutorial-rag-as-agent]])); the `wiki.abstracts.2017.tar.gz` Hugging Face artifact (5M Wikipedia abstracts) as the indexed corpus; `Qwen/Qwen2.5-1.5B-Instruct` named explicitly as the student model. **Twelfth wiki-corpus DSPy tutorial** and **second tutorial with a weight-space optimizer** (after [[dspy-tutorial-rl-papillon|the PAPILLON tutorial]]) — the wiki now has **two parallel ArborGRPO receipts** on two different task families. **Headline number**: ~18 hours on 4 GPUs (3 training + 1 inference) lifts devset recall from **61.8% → 66.2%** (+4.4 pts, ~7% relative). The tutorial itself frames this honestly as worse on cost/quality than the prompt optimizers — **first DSPy tutorial whose own conclusion documents that the demonstrated technique is dominated by prior tutorials on the same benchmark family**.

## Key Claims

- **`dspy.ArborGRPO(...)` is a [[DSPyOptimizers|DSPy compiler]] in the optimizer slot, not a parallel training script.** The signature mirrors the prompt-optimizer compilers — `compiler.compile(student=program, trainset=trainset, valset=devset)` returns an `optimized_program` with the same module shape and call interface. This is the **structural lift**: GRPO weight updates are wrapped in a DSPy [[DSPyOptimization|optimizer]] so they compose with the rest of the framework (the [[DSPyModules|Module]] surface, the metric protocol, the [[DSPyEvaluate|Evaluate]] surface). The wiki's first instance of *"RL training as a compiler step over a `dspy.Module`"*.

- **The student program is structurally identical to a prompt-optimization program.** `ResearchHop(num_docs=4, num_hops=2)` composes **two [[chainofthought|`dspy.ChainOfThought`]] sub-modules** (`generate_query` and `append_notes`) inside a single `dspy.Module` subclass with a hop-loop `forward(...)`. No RL-specific code in the program itself — the RL is purely in the compiler. **First receipt that prompt-optimization-shaped and RL-optimization-shaped DSPy programs are structurally indistinguishable** — the optimizer is the only difference.

- **The metric protocol survives unchanged.** `recall(example, pred, trace=None)` returns a float in `[0, 1]` — same protocol as every prior DSPy tutorial. **GRPO consumes this metric as a scalar reward signal.** No need for a separate reward function — the [[DSPyMetrics|DSPy metric]] IS the GRPO reward. This is the [[2507.19457-gepa|GEPA paper's]] information-bandwidth contrast in operational form: prompt optimizers extract kilobytes of natural-language feedback from the same metric call's trace; GRPO extracts ~1 bit per rollout.

- **`Qwen/Qwen2.5-1.5B-Instruct` is the wiki's smallest open-weights DSPy student.** Prior DSPy tutorials used [[Llama|Llama-3.2-3B-Instruct]] ([[dspy-tutorial-rag-as-agent]]), `gpt-4o-mini` ([[dspy-yahoo-finance-react-tutorial]] and most others), or [[Llama|Llama-3-8B]] ([[2406.11695-mipro|MIPRO paper]]). 1.5B is the **bottom of the open-weights size band** where GRPO weight updates can fit on consumer-tier multi-GPU rigs while still leaving headroom for the (frozen) BM25 index to live in process memory.

- **LoRA configuration is GRPO-paper-canonical, not [[2407.10930-better-together|BetterTogether]]-canonical.** `r=8, lora_alpha=16, lora_dropout=0.05, target_modules=["q_proj","k_proj","v_proj","o_proj","up_proj","down_proj","gate_proj"]` — **seven target modules** spanning **all four self-attention projections plus all three feedforward layers**. Contrast: [[2407.10930-better-together|BetterTogether]] uses `r=32, alpha=64, no dropout` and targets **only q_proj + k_proj**. The tutorial's wider target set ↔ smaller rank ↔ nonzero dropout combination is the configuration the [[GRPO|DeepSeek / GRPO-paper line]] favors for **on-policy RL on small models**, where exploration variance matters more than the absolute parameter budget.

- **The training pipeline is dual-rank GPU: 3 training + 1 inference.** `num_training_gpus=3, num_inference_gpus=1` — first wiki receipt of explicit **train-inference GPU partitioning** for an online-RL run. The inference GPU holds the rollout-generation copy of the policy; the three training GPUs do gradient computation on collected trajectories. The split is necessary because GRPO is **on-policy** — every gradient step requires fresh rollouts from the current policy, which would block training compute if served from the same GPUs.

- **`loss_type="dapo"` selects [[DAPO|DAPO]] as the GRPO variant.** First wiki receipt of [[DAPO]] (Decoupled Clip and Dynamic Sampling Policy Optimization, Yu et al. 2025) as a configured loss. DAPO is the GRPO descendant that **decouples the clipping ratios for positive and negative advantage tokens** — addressing a known GRPO failure where the symmetric PPO-style clip suppresses exploration on the positive-advantage side. The [[grpo|GRPO concept page]] names DAPO / GSPO / CISPO as the descendant family; this tutorial is the **first wiki-corpus receipt where DAPO is the operational choice rather than a citation**.

- **`beta=0.00` disables the KL penalty against the reference policy.** Standard GRPO papers use `beta=0.04` or similar to anchor the policy near the SFT reference. The tutorial zero's it — letting the policy drift freely. Combined with `loss_type="dapo"` (which has its own clipping discipline) and `learning_rate=1e-6` (very small), the resulting setup is **maximum-exploration, KL-unconstrained, low-step-size** — appropriate for a 1000-step run on a 1.5B student where the cold start is far from a good policy.

- **`scale_rewards=False` keeps the recall metric on its native [0, 1] scale.** Reward scaling would normalize across batches (mean-zero, unit-variance); leaving it off means every example contributes its raw recall fraction to the advantage computation. This is consistent with the **[[grpo|GRPO group-baseline]] formulation** — the per-example advantage is `recall - mean(group_recalls)`, and rescaling would distort the relative ordering inside the group.

- **`num_dspy_examples_per_grpo_step=6, num_rollouts_per_grpo_step=24`** → **4 rollouts per example per step**. The group size for the GRPO advantage estimate is 4. The `gradient_accumulation_steps=24/6=4` matches (one micro-batch per rollout group). **The 24-rollout step × 1000 steps = 24,000 total rollouts** — **same total rollout budget the [[2507.19457-gepa|GEPA paper]] gave its GRPO baseline** that GEPA beat by 6% average and up to 20% on the same HoVer benchmark.

- **`checkpoint="single-best"`** keeps only the highest-val-score checkpoint across the 1000 training steps (validated every 50 steps, `num_steps_for_val=50`). Twenty validation events; the best one's weights survive. This is the **early-stopping discipline** for online RL where the loss-curve doesn't monotonically translate to held-out metric improvement.

- **Initial recall is already 61.8% on the 2-hop ResearchHop program, not 8%.** The [[dspy-tutorial-rag-as-agent|RAG-as-agent tutorial]] reports 8% baseline → 41.67% optimized for a `dspy.ReAct` agent with `max_iters=20` and `Llama-3.2-3B`. This tutorial's baseline is **already higher than the optimized ReAct number on the same HoVer dataset family** — because (a) the program is a fixed 2-hop loop with cleaner control flow than a free-ranging ReAct agent, (b) the [[BM25|BM25]] retriever index is tightly matched to the title-recall metric (titles appear in the indexed text), (c) the metric is **per-page recall** (3 gold titles) rather than `top5_recall` (binary at depth 5). The two numbers are not directly comparable — different program shapes, different metric definitions.

- **The +4.4 point lift over 18 hours is the tutorial's honest data point, not a marketing number.** The tutorial states explicitly: *"This is typically worse on cost/quality basis than you'd get from running prompt optimizers `dspy.MIPROv2` or `dspy.SIMBA`."* No prior DSPy tutorial in the wiki has self-disclosed inferiority to other tutorials on the same task. The framing is **invitation-to-improve**, not benchmark posturing.

## Key Quotes

> *"This feature is new and extremely EXPERIMENTAL. Unlike almost everything else in DSPy, it's currently in pure proof of concept and development mode, but we release it to encourage community involvement."*

> *"In our preliminary experiments, training about 18 hours boosts the recall (devset) from 61.8% to 66.2%."*

> *"This is typically worse on cost/quality basis than you'd get from running prompt optimizers `dspy.MIPROv2` or `dspy.SIMBA`, but it's still a very solid start for online RL over arbitrary LM programs for small LMs."*

> *"This is 500MB compressed, so the download and decompression may take 2-3 minutes."* — on the wiki.abstracts.2017 corpus.

> *"Given a claim and some key facts, generate a follow-up search query to find the next most essential clue towards verifying or refuting the claim. The goal ultimately is to find all documents implicated by the claim."* — `instr1`, the first sub-Signature's natural-language instruction.

> *"Given a claim, some key facts, and new search results, identify any new learnings from the new search results, which will extend the key facts known so far about the whether the claim is true or false. The goal is to ultimately collect all facts that would help us find all documents implicated by the claim."* — `instr2`, the second sub-Signature's instruction.

## Code Receipt — minimum reproducible program

```python
import dspy
import arbor
from arbor import ArborGRPO, ArborProvider
import orjson, bm25s, Stemmer, random
from dspy.utils import download
from dspy.datasets import DataLoader

arbor_server_info = arbor.init()
local_lm = dspy.LM(
    model="openai/arbor:Qwen/Qwen2.5-1.5B-Instruct",
    provider=ArborProvider(),
    api_base=arbor_server_info["base_url"],
    temperature=1.0, top_p=1.0, top_k=-1,
    repetition_penalty=1.0, max_tokens=2048,
)
dspy.configure(lm=local_lm)

# corpus: 5M Wikipedia abstracts (2017) indexed under BM25 (k1=0.9, b=0.4)
corpus = []
with open("wiki.abstracts.2017.jsonl") as f:
    for line in f:
        line = orjson.loads(line)
        corpus.append(f"{line['title']} | {' '.join(line['text'])}")
stemmer = Stemmer.Stemmer("english")
corpus_tokens = bm25s.tokenize(corpus, stopwords="en", stemmer=stemmer)
retriever = bm25s.BM25(k1=0.9, b=0.4)
retriever.index(corpus_tokens)

def search(query: str, k: int) -> list[str]:
    tokens = bm25s.tokenize(query, stopwords="en", stemmer=stemmer, show_progress=False)
    results, scores = retriever.retrieve(tokens, k=k, n_threads=1, show_progress=False)
    return list({corpus[doc]: float(score) for doc, score in zip(results[0], scores[0])}.keys())

instr1 = "Given a claim and some key facts, generate a follow-up search query..."
instr2 = "Given a claim, some key facts, and new search results, identify any new learnings..."

class ResearchHop(dspy.Module):
    def __init__(self, num_docs, num_hops):
        self.num_docs, self.num_hops = num_docs, num_hops
        self.generate_query = dspy.ChainOfThought(
            dspy.Signature("claim, key_facts -> followup_search_query", instr1))
        self.append_notes = dspy.ChainOfThought(
            dspy.Signature("claim, key_facts, new_search_results -> new_key_facts", instr2))

    def forward(self, claim: str):
        key_facts, retrieved_docs = [], []
        for hop_idx in range(self.num_hops):
            query = (self.generate_query(claim=claim, key_facts=key_facts).followup_search_query
                     if hop_idx else claim)
            search_results = search(query, k=self.num_docs)
            retrieved_docs.extend(search_results)
            if hop_idx == self.num_hops - 1:
                break
            prediction = self.append_notes(claim=claim, key_facts=key_facts,
                                           new_search_results=search_results)
            key_facts.append(prediction.new_key_facts)
        return dspy.Prediction(key_facts=key_facts, retrieved_docs=retrieved_docs)

def recall(example, pred, trace=None):
    gold_titles = example.titles
    retrieved_titles = [doc.split(" | ")[0] for doc in pred.retrieved_docs]
    return sum(x in retrieved_titles for x in set(gold_titles)) / len(gold_titles)

program = ResearchHop(num_docs=4, num_hops=2)
program.set_lm(local_lm)

compiler = ArborGRPO(
    metric=recall,
    num_dspy_examples_per_grpo_step=6,
    num_rollouts_per_grpo_step=24,
    exclude_demos=True,
    num_train_steps=1000,
    num_threads=16,
    use_train_as_val=False,
    num_steps_for_val=50,
    train_kwargs={
        "per_device_train_batch_size": 2,
        "gradient_accumulation_steps": 24/6,
        "learning_rate": 1e-6, "beta": 0.00,
        "loss_type": "dapo", "max_steps": 1000,
        "bf16": True, "gradient_checkpointing": True,
        "lr_scheduler_type": "constant_with_warmup",
        "scale_rewards": False, "max_grad_norm": 1.0,
        "lora_config": {
            "lora_alpha": 16, "lora_dropout": 0.05, "r": 8,
            "target_modules": ["q_proj","k_proj","v_proj","o_proj",
                               "up_proj","down_proj","gate_proj"],
        },
        "num_training_gpus": 3, "num_inference_gpus": 1,
        "weight_decay": 0.001,
    },
    checkpoint="single-best",
)

optimized_program = compiler.compile(student=program, trainset=trainset, valset=devset)
```

## Position in the DSPy Tutorial Corpus

**Twelfth wiki-corpus DSPy tutorial.** Coverage along the **optimizer / training-regime axis**:

| Tutorial | Optimizer | Regime | Student | Task | Lift |
|---|---|---|---|---|---|
| [[dspy-tutorial-math]] | [[MIPROv2]] `auto="medium"` | prompt-space | gpt-4o-mini | MATH-algebra | 74.0 → 88.57 |
| [[dspy-rag-tutorial]] | [[MIPROv2]] `auto="medium"` | prompt-space | gpt-4o-mini | StackExchange RAG | 42 → 61.1 |
| [[dspy-entity-extraction-tutorial]] | [[MIPROv2]] `auto="medium"` | prompt-space | gpt-4o-mini | CoNLL-2003 NER | 86 → 93 |
| [[dspy-tutorial-rag-as-agent]] | [[MIPROv2]] `auto="medium"` + teacher | prompt-space | Llama-3.2-3B | HoVer ReAct | 8 → 41.67 |
| [[dspy-tutorial-rl-papillon]] | [[ArborGRPO]] (DAPO, LoRA r=8) | weight-space (RL) | 1.5B local | PUPA / [[PAPILLON]] privacy | 54.6 → 60.0 (composite) |
| **dspy-rl-multihop-tutorial** *(this page)* | **[[ArborGRPO]] (DAPO, LoRA r=8)** | **weight-space (RL)** | **Qwen2.5-1.5B-Instruct** | **HoVer 3-hop retrieval** | **61.8 → 66.2** |
| (programming-stage-only tutorials) | — | — | various | — | — |

**What this tutorial uniquely contributes** to the DSPy tutorial corpus:

1. **Second [[ArborGRPO]] receipt in the wiki**, paired structurally with [[dspy-tutorial-rl-papillon|the PAPILLON tutorial]]. Together the two receipts cover **two distinct task families** under one optimizer: privacy-preserving delegation with an [[LLMJudge|LLM-judge composite reward]] (PAPILLON / PUPA) and multi-hop retrieval with a **deterministic title-recall reward** (HoVer). Establishes that the ArborGRPO compiler accepts *any* DSPy metric function as the reward signal — LM-judge composites and deterministic numerics flow through the same `metric=` kwarg.
2. **Second [[HoVer]] receipt under a DSPy optimizer**, paired structurally with [[dspy-tutorial-rag-as-agent|the RAG-as-agent tutorial]]. Together: **MIPROv2 over `dspy.ReAct` agent** (prompt-space, 8 → 41.67 on top5_recall) ↔ **ArborGRPO over 2-hop `ResearchHop`** (weight-space, 61.8 → 66.2 on title-recall). HoVer is now the wiki's first **two-tutorial benchmark with both a prompt-optimizer and a weight-optimizer receipt** — the operational form of the [[2507.19457-gepa|GEPA paper's]] central contrast.
3. **First DSPy receipt of `program.set_lm(...)`** — the per-program LM binding API distinct from the global `dspy.configure(lm=...)`. [[dspy-tutorial-rl-papillon|The PAPILLON tutorial]] used global `dspy.configure(...)` for the trained LM and a separate `untrusted_model` kwarg passed into the program; this tutorial uses **explicit per-program binding** for the LM that will receive the GRPO gradient updates.
4. **First DSPy receipt of `ArborProvider()` + `"openai/arbor:Qwen/..."` model prefix** as the explicit [[DSPyLM|`dspy.LM(...)`]] binding form (also `api_base=arbor_server_info["base_url"]`). [[dspy-tutorial-rl-papillon|The PAPILLON tutorial]] only shows the optimizer call, not the `dspy.LM(...)` construction.
5. **First DSPy receipt where `Qwen/Qwen2.5-1.5B-Instruct` is named explicitly** as the student model — pins the **1.5B-parameter open-weights floor** in the DSPy tutorial corpus. (PAPILLON tutorial generically said *"tiny 1.5B-parameter local LM"* without naming the model.)
6. **First DSPy receipt of `bm25s.BM25(k1=0.9, b=0.4)` + `Stemmer` (PyStemmer)** as the in-process Python BM25 retriever. Prior BM25 receipts in the wiki used `rank_bm25.BM25Okapi` ([[hands-on-llm-ch08-semantic-search-and-rag|Hands-On LLMs Ch 8]]); prior DSPy retrieval receipts used [[ColBERTv2]] ([[dspy-custom-module]], [[dspy-tutorial-rag-as-agent]]).
7. **First DSPy receipt of the `wiki.abstracts.2017.tar.gz` Hugging Face artifact** (500MB compressed, 5M Wikipedia page abstracts) as a directly-downloadable indexed corpus. Closes a long-standing forward reference: every prior DSPy retrieval receipt in the wiki used a hosted [[ColBERTv2]] index; this tutorial demonstrates **the BYO-corpus path** with `dspy.utils.download(...)` + `bm25s` indexing in process memory.
8. **First DSPy ArborGRPO receipt to disclose the GPU-partitioning kwargs explicitly**: `num_training_gpus=3, num_inference_gpus=1` — the on-policy RL pattern where the inference GPU holds a rollout-generation copy of the policy while the three training GPUs do gradient computation on collected trajectories. [[dspy-tutorial-rl-papillon|The PAPILLON tutorial]] mentioned 4× H100s but did not surface the partition.
9. **First DSPy ArborGRPO receipt to disclose `scale_rewards=False, max_grad_norm=1.0, weight_decay=0.001, lr_scheduler_type="constant_with_warmup", report_to="wandb", log_completions=True, logging_steps=1, max_prompt_length=None, max_completion_length=None`** as configured kwargs — the broader Hugging Face TRL surface that flows through `train_kwargs`.
10. **First DSPy ArborGRPO receipt of the `checkpoint="single-best"` + `num_steps_for_val=50, use_train_as_val=False`** combination — the early-stopping discipline (20 validation events across 1000 steps; only the highest-val-score checkpoint survives).
11. **First DSPy receipt where the tutorial's own conclusion documents that the demonstrated technique is dominated** by a prior tutorial on the same benchmark family ([[dspy-tutorial-rag-as-agent|HoVer]] via [[MIPROv2]]).
12. **Operational form of the [[2507.19457-gepa|GEPA paper's]] central contrast** on the *retrieval* benchmark axis (PAPILLON tutorial covers the *judge-reward* axis; this tutorial covers the *deterministic-metric* axis). Same 24,000-rollout total budget the [[2507.19457-gepa|GEPA paper]] gave its GRPO baseline that GEPA beat by 6% average and up to 20% on HoVer.

## DSPy Optimizer Catalog — wiki state after this ingest

| Family | Optimizer | Wiki status |
|---|---|---|
| **Prompt-space** | `dspy.MIPROv2` | Primary; 5 tutorial receipts ([[MIPROv2]]). |
| **Prompt-space** | `dspy.SIMBA` | Primary ([[SIMBA]]); adversarial-search receipt. |
| **Prompt-space** | `dspy.COPRO` | Forward reference. |
| **Prompt-space (evolutionary)** | `dspy.GEPA` | Primary ([[2507.19457-gepa]] / [[GEPA]]). |
| **Prompt-space (stochastic)** | `dspy.BootstrapFewShotWithRandomSearch` | Primary ([[BootstrapFewShotWithRandomSearch]]). |
| **Weight-space (SFT)** | `dspy.BootstrapFinetune` | Primary ([[BootstrapFinetune]] / [[2407.10930-better-together]]). |
| **Weight-space (RL)** | `dspy.ArborGRPO` | Two tutorial receipts: [[dspy-tutorial-rl-papillon|PAPILLON / PUPA]] and **this tutorial (HoVer)**. |
| Meta-optimizer | [[BetterTogether]] | Primary ([[2407.10930-better-together]]). |

The DSPy optimizer surface is documented across **two regimes** (prompt-space, weight-space) and **two weight-space sub-regimes** (SFT via [[BootstrapFinetune]], on-policy RL via [[ArborGRPO]]). The framework's coverage of the optimizer-design space is complete at the catalog level; the empirical ordering on any specific task remains task-dependent ([[2507.19457-gepa|GEPA paper]] data: prompt-space wins on 5/6 of its benchmarks; tutorial-internal data here: [[MIPROv2]] beats [[ArborGRPO]] on HoVer-family cost/quality).

## Connections

- [[DSPy]] — the framework being demonstrated.
- [[chainofthought|`dspy.ChainOfThought`]] — the sub-module used twice inside `ResearchHop`.
- [[DSPyModules]] — `ResearchHop` is a `dspy.Module` subclass; `set_lm(...)` is a new API surface receipt.
- [[DSPySignatures]] — inline string-form `dspy.Signature("claim, key_facts -> followup_search_query", instr1)` with a natural-language instruction as the second positional argument.
- [[DSPyLM]] — `dspy.LM(model="openai/arbor:Qwen/...", provider=ArborProvider(), api_base=...)` is the new local-RL binding form.
- [[DSPyOptimizers]] / [[DSPyOptimization]] — the catalog this tutorial extends with a weight-space RL entry.
- [[ArborGRPO]] — the DSPy compiler wrapping Arbor's GRPO trainer; this tutorial is the **second receipt** after [[dspy-tutorial-rl-papillon]].
- [[Arbor]] — the open-source RL training framework (`arbor-ai`, `arbor.init()`, `ArborProvider`); second receipt.
- [[grpo|GRPO]] — the RL algorithm.
- [[DAPO]] — the GRPO loss variant (`loss_type="dapo"`); second receipt.
- [[Qwen|Qwen2.5-1.5B-Instruct]] — the student model. First DSPy tutorial receipt to name the exact `Qwen/Qwen2.5-1.5B-Instruct` checkpoint.
- [[HoVer]] — the benchmark; this tutorial uses the same 3-hop subset as [[dspy-tutorial-rag-as-agent]] but with a different filtering / split (600/300/300 vs 100/100/remainder).
- [[BM25]] — the retriever family.
- [[bm25s]] — **new entity page.** The Python BM25 implementation (`bm25s.BM25(k1=0.9, b=0.4)`).
- [[PyStemmer]] — **new entity page.** The C-backed snowball stemmer used by `bm25s.tokenize(stemmer=Stemmer.Stemmer("english"))`.
- [[ResearchHop]] — **new concept page.** The 2-hop generate-query / append-notes program shape introduced by this tutorial.
- [[lora|LoRA]] — the PEFT method used (`r=8, alpha=16, dropout=0.05`, seven target modules).
- [[MIPROv2]] / [[SIMBA]] — explicitly named as the **dominant** prompt-space alternatives the tutorial concedes outperform GRPO on cost/quality here.
- [[2507.19457-gepa]] / [[GEPA]] — the paper-side argument that prompt-space outperforms GRPO on sample-constrained compound-AI-system optimization; this tutorial is the operational instance of that comparison's GRPO side.
- [[dspy-tutorial-rag-as-agent]] — sibling HoVer tutorial; uses [[MIPROv2]] over a `dspy.ReAct` agent. The two tutorials are the **prompt-vs-weight pair** on the HoVer task family.
- [[MultiHopQA]] — task type; HoVer-3-hop is the multi-hop variant.
- [[MultiHopRAG]] — the architectural pattern `ResearchHop` instantiates.
- [[dspy-data]] — the [[DSPy]] data API page; `dspy.Example(...).with_inputs("claim")` and `DataLoader().from_huggingface(...)` are documented there.
- [[DSPyEvaluate]] — the `dspy.Evaluate(devset=..., metric=recall, ...)` evaluation harness.
- [[DSPyMetrics]] — the metric protocol; `recall(example, pred, trace=None)` returns a float in `[0, 1]`, consumed by both `dspy.Evaluate` and `ArborGRPO` as the reward signal.
- [[HuggingFace]] — host of the `wiki.abstracts.2017.tar.gz` corpus and the `hover-nlp/hover` dataset.
- [[2406.11695-mipro]] — the MIPRO paper that established HoVer as the deepest-pipeline benchmark in the [[DSPyOptimizerBenchmark]]; this tutorial uses the same dataset family on the weight-space side.

## Contradictions

None with the existing wiki — the tutorial's own framing **explicitly aligns** with the [[2507.19457-gepa|GEPA paper's]] ordering (prompt-space optimizers beat GRPO on cost/quality for sample-constrained compound-AI-system tasks). The tutorial extends rather than contradicts:

- The [[grpo|GRPO page's]] framing of GRPO as the *"default weight-space RL baseline"* is operationalized here: same 24,000-rollout budget the [[2507.19457-gepa|GEPA paper]] used against GRPO, same HoVer benchmark family, same broad conclusion (prompt-space dominates).
- The [[DSPyOptimizers|Optimizer page's]] catalog of compilers is extended with `dspy.ArborGRPO` as the weight-space RL slot.

## Scope-Limit Gaps

- **No comparison run with [[MIPROv2]] or [[SIMBA]] on the same `ResearchHop` program.** The tutorial asserts GRPO is dominated but does not run the dominators on the same program for a side-by-side number. The reader must cross-reference [[dspy-tutorial-rag-as-agent]] (different program shape) or [[2507.19457-gepa]] (different model) for the contrast.
- **No test-set number.** The 61.8% → 66.2% lift is **devset**; testset is allocated (300 examples) but never evaluated in the tutorial. The single-best checkpoint is selected on devset, so the dev number has selection bias.
- **No cost characterization.** *"Training about 18 hours"* on 4 GPUs (3 training + 1 inference) — no GPU-type disclosure, no wall-clock-per-rollout, no comparison to the few-dollar [[MIPROv2|MIPROv2 `auto="medium"`]] run on the same task.
- **No ablation across the GRPO hyperparameters.** `loss_type="dapo"`, `beta=0.00`, `r=8`, `target_modules=` (seven modules), `learning_rate=1e-6` — each is a chosen point in a high-dimensional space; no sensitivity analysis.
- **No reward-shaping discussion.** The metric is raw fractional recall; no curriculum, no shaping toward partial credit on close-but-wrong titles, no penalty for redundant search queries.
- **No exploration / collapse diagnostics.** With `beta=0.00` and `temperature=1.0`, mode collapse is a real risk; the tutorial doesn't show entropy / KL-from-reference plots over training.
- **No alternative loss / framework comparison.** `loss_type` is a configurable kwarg with [[DAPO]] selected; GSPO, CISPO, vanilla GRPO are not exercised. No comparison to the [[2407.10930-better-together|BetterTogether]] SFT-LoRA path.
- **No deployment recipe.** The optimized program is called once on `devset[0]`; no `program.save(...)` / `dspy.load(...)` round-trip ([[DSPySaving]]), no MLflow logging ([[MLflow]]), no serving recipe ([[dspy-deployment-tutorial]]).
- **No data-leakage / contamination check.** Qwen2.5-1.5B-Instruct's pretraining data plausibly includes the [[HoVer]] dataset and the 2017 Wikipedia dump; the 61.8% baseline could include memorized title recall. No disclosure of contamination analysis.
- **No discussion of the [[grpo|GRPO]]-vs-[[DAPO]] difference at the loss-function level.** [[DAPO]] is selected by string kwarg; the tutorial doesn't motivate the choice or surface what DAPO changes relative to vanilla GRPO.
- **`gradient_accumulation_steps=24/6`** is a non-integer-looking expression that evaluates to `4.0` (float). This works in PyTorch but is **brittle stylistically** — first wiki-corpus DSPy tutorial with a non-integer kwarg that happens to be integer-valued.
- **`arbor.init()` and `ArborProvider()` are presented without surface documentation.** Port `7453` is named but never explained; the inference server lifecycle is implicit.
- **No streaming / observability integration.** [[DSPyStreaming]] and [[DSPyObservability]] composing over an RL-optimized program is not exercised.
