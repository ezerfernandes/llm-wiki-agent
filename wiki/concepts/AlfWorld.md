---
title: "AlfWorld"
type: concept
tags: [benchmark, agent, interactive-fiction, household-tasks, embodied-ai, react, dataset, simulator]
sources: [dspy-tutorial-games]
last_updated: 2026-05-24
---

# AlfWorld

**AlfWorld** is an aligned text-and-embodied benchmark that re-implements the **ALFRED** household-task suite ([Shridhar et al. 2020](https://arxiv.org/abs/2010.03768)) inside a **TextWorld** interactive-fiction environment ([Côté et al. 2018](https://arxiv.org/abs/1806.11532)) — turning ALFRED's vision-and-language pick-and-place tasks into **text-only command-issuing tasks** at the same task-spec level. The canonical paper is [Shridhar et al. 2021](https://arxiv.org/abs/2010.03768) (*"ALFWorld: Aligning Text and Embodied Environments for Interactive Learning"*).

In the LLM-agent literature, AlfWorld is the **default text-only household-task benchmark** for evaluating goal-directed agents that compose multi-step plans (navigate → pick up → process → place) — most notably as the testbed for [[react|ReAct (Yao et al. 2022)]], which is where DSPy's framing inherits from.

## Task shape

Each task instantiates a [[TextWorld]] room containing a fixed inventory of receptacles (drawers, countertops, sinkbasins, garbagecans, dressers, sidetables, etc.) and a high-level natural-language goal — e.g., *"put a clean soapbar in garbagecan"* or *"put some box on dresser"*.

The agent interacts via two channels:

- **Admissible commands** — environment-supplied list per turn (`info["admissible_commands"]`): `go to <receptacle>`, `take <obj> from <receptacle>`, `move <obj> to <receptacle>`, `examine <receptacle>`, `look`, `clean <obj> with <appliance>`, `heat <obj> with <appliance>`, `cool <obj> with <appliance>`, etc.
- **Observations** — environment text after each command (`obs[0]`).

A task ends when the agent satisfies the goal (`done=True, reward=1`) or hits the iteration cap (`done=False, reward=0`). The canonical iteration cap is **50 steps**, matching [[react|Yao et al. 2022]].

## Standard task types

Six canonical types (from the ALFRED parent paper):

1. **Pick & Place** — put X on Y
2. **Examine in Light** — look at X with desklamp
3. **Clean & Place** — clean X (at sinkbasin), put on Y
4. **Heat & Place** — heat X (at microwave), put on Y
5. **Cool & Place** — cool X (at fridge), put on Y
6. **Pick Two & Place** — put two of X on Y

Goal text is uniformly formatted but the **required sub-plan length** varies — pick-and-place is ~5-8 steps; cool-and-place is ~10-15 steps with mandatory appliance-mediated transformations.

## Wiki-corpus receipts

| Receipt | Setup | Headline |
|---|---|---|
| **[[dspy-tutorial-games\|DSPy Tutorial — Fine-tuning Agents]]** | Hand-rolled [[react\|ReAct]]-pattern `dspy.Module` (one `dspy.Predict("task, trajectory, possible_actions: list[str] -> action")`, `max_iters=50`, `"think:"` pseudo-action), 200 train + 200 dev, [[MIPROv2\|`MIPROv2(auto="light")`]] + [[BootstrapFinetune]] | **GPT-4o-mini 15.0% → 71.5%** devset (+56.5 pts, ~4.8×); fine-tuned 4o-mini beats GPT-4o teacher (57.5%) by +14 pts |

This is the **first wiki-corpus DSPy receipt on AlfWorld** and the **first wiki receipt where AlfWorld is the SFT target of a [[BootstrapFinetune|weight-tuning]] optimizer**.

## DSPy-native loader

`dspy.datasets.alfworld.AlfWorld()` returns a hybrid **dataset + simulator handle** — exposes `.trainset` / `.devset` as lists of `dspy.Example` records (with `.inputs()` returning the task `idx`) and a `POOL` attribute (a context-managed worker pool for the underlying TextWorld subprocesses). Pattern:

```python
from dspy.datasets.alfworld import AlfWorld
alfworld = AlfWorld()
trainset, devset = alfworld.trainset[:200], alfworld.devset[-200:]

with alfworld.POOL.session() as env:
    task, info = env.init(**example.inputs())
    obs, reward, done, info = env.step(action)
```

Sibling in the DSPy in-framework dataset family: [[dspy-tutorial-math|`dspy.datasets.MATH(subset='algebra')`]] — but AlfWorld goes further by also shipping **executable environment infrastructure**, not just data records.

## Installation

```bash
pip install -U alfworld==0.3.5 multiprocess
alfworld-download   # downloads the TextWorld game files
```

DSPy ≥ 2.6.0 required for the loader.

## Connections

- [[react|ReAct]] — the canonical agent pattern AlfWorld is the **default benchmark for** ([[react|Yao et al. 2022]] use AlfWorld as the long-horizon embodied task showcase)
- [[TextWorld]] — the underlying interactive-fiction engine AlfWorld is implemented on top of
- [[dspy-tutorial-games]] — the wiki's only AlfWorld receipt
- [[DSPy]] — the framework with an in-tree `dspy.datasets.alfworld.AlfWorld` loader
- [[BootstrapFinetune]] — the optimizer that turns AlfWorld trajectories into supervised fine-tuning data via teacher rollouts
- [[MIPROv2]] — the prompt-optimizer used to seed the teacher in the BFT pipeline
- [[FineTuning]] — the weight-tuning regime AlfWorld is the SFT target of in the wiki's only receipt
- [[GPT]] — the model family used as both teacher (GPT-4o) and student (GPT-4o-mini)
- [[OpenAI]] — the fine-tuning provider
- [[KnowledgeDistillation]] — the pattern AlfWorld's teacher-student pipeline realizes
- [[Agent]] — the broader concept; AlfWorld is the wiki's first **long-horizon (50-step) embodied-style agent benchmark**

## Open questions / wiki gaps

- **No multi-task-type breakdown.** [[dspy-tutorial-games]] reports one aggregate 71.5% — whether the fine-tune generalizes uniformly across the six task types is unknown. The original [[react|ReAct paper]] reports per-type numbers.
- **No GRPO / online-RL receipt.** AlfWorld's binary `won` reward is a natural [[grpo|GRPO]] target via [[ArborGRPO]] — would complete the wiki's prompt-vs-SFT-vs-online-RL triplet on the same task family.
- **No baseline ReAct paper numbers cross-referenced.** [[react|Yao et al. 2022]] report AlfWorld success rates on the original benchmark; cross-tutorial alignment with this wiki's 71.5% has not been computed.
- **No ALFRED (vision-and-language) sibling receipt.** AlfWorld's text-only framing is one side of the alignment pair; the vision-and-language ALFRED benchmark sits in a different model regime and is not yet a wiki receipt.
