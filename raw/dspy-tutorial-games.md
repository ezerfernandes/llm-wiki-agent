# DSPy Tutorial: Fine-tuning Agents

**Source URL:** https://dspy.ai/tutorials/games/
**Notebook source:** https://github.com/stanfordnlp/dspy/blob/main/docs/docs/tutorials/games/index.ipynb
**Ingested:** 2026-05-24

---

Let's walk through a quick example of optimizing the _language model weights_ (i.e., fine-tuning) inside a DSPy module that represents a ReAct agent playing a game with 50-step tasks.

### Install dependencies and download data

Install the latest DSPy via `pip install -U dspy` and follow along. This tutorial uses the AlfWorld dataset, which depends on DSPy 2.6.0.

You will also need the following dependencies:

```shell
> pip install -U alfworld==0.3.5 multiprocess
> alfworld-download
```

### Recommended: Setup MLflow Tracing

MLflow is an LLMOps tool that natively integrates with DSPy and offers explainability and experiment tracking.

```bash
%pip install mlflow>=2.20
mlflow ui --port 5000
```

```python
import mlflow
mlflow.set_tracking_uri("http://localhost:5000")
mlflow.set_experiment("DSPy")
mlflow.dspy.autolog()
```

### Set up the language models

Our goal is to allow `gpt-4o-mini` to play the AlfWorld household game proficiently, without tinkering with string prompts or example trajectories by hand. Though it's not strictly necessary, we'll make our job a little easier by using the larger `gpt-4o` for prompt optimization and fine-tuning, building our small `gpt-4o-mini` agent.

```python
import dspy

gpt4o_mini = dspy.LM('gpt-4o-mini-2024-07-18')
gpt4o = dspy.LM('openai/gpt-4o')
dspy.configure(experimental=True)
```

Let's load 200 training and 200 development tasks from AlfWorld. The dataset is much larger, but a small number of examples will help keep this tutorial run in 1-2 hours, including fine-tuning.

With just 100 training tasks, we'll teach 4o-mini to go from 19% (can barely play the game) to 72%. If you use 500 tasks and retain the demonstrations during fine-tuning, you can push that easily to 82%.

```python
from dspy.datasets.alfworld import AlfWorld

alfworld = AlfWorld()
trainset, devset = alfworld.trainset[:200], alfworld.devset[-200:]
len(trainset), len(devset)
# (200, 200)
```

Example task:

```
-= Welcome to TextWorld, ALFRED! =-

You are in the middle of a room. Looking quickly around you, you see a countertop 1, a drawer 8, a drawer 7, a drawer 6, a drawer 5, a drawer 4, a drawer 3, a drawer 2, a drawer 1, a garbagecan 1, a handtowelholder 1, a sinkbasin 2, a sinkbasin 1, a toilet 1, a toiletpaperhanger 1, and a towelholder 1.

Your task is to: put a clean soapbar in garbagecan.
```

### Defining the Agent program

The agent is a pretty simple `dspy.Module` with one sub-module called `self.react`.

This sub-module consumes a definition of a specific `task`, sees its previous `trajectory`, and sees a list of `possible_actions` it can take. It responds simply with the next action.

In the `forward` method, we just initialize an environment for the given task `idx`. And we loop up to `self.max_iters`, repeatedly invoking the `self.react` module to take the next action.

```python
class Agent(dspy.Module):
    def __init__(self, max_iters=50, verbose=False):
        self.max_iters = max_iters
        self.verbose = verbose
        self.react = dspy.Predict("task, trajectory, possible_actions: list[str] -> action")

    def forward(self, idx):
        with alfworld.POOL.session() as env:
            trajectory = []
            task, info = env.init(idx)
            if self.verbose:
                print(f"Task: {task}")

            for _ in range(self.max_iters):
                trajectory_ = "\n".join(trajectory)
                possible_actions = info["admissible_commands"][0] + ["think: ${...thoughts...}"]
                prediction = self.react(task=task, trajectory=trajectory_, possible_actions=possible_actions)
                trajectory.append(f"> {prediction.action}")

                if prediction.action.startswith("think:"):
                    trajectory.append("OK.")
                    continue

                obs, reward, done, info = env.step(prediction.action)
                obs, reward, done = obs[0], reward[0], done[0]
                trajectory.append(obs)

                if self.verbose:
                    print("\n".join(trajectory[-2:]))

                if done:
                    break

        assert reward == int(info["won"][0]), (reward, info["won"][0])
        return dspy.Prediction(trajectory=trajectory, success=reward)
```

#### Aside: If you wanted to include instructions for your agent

Above, we opted to keep the agent super simple, without even providing short instructions that describe the task. In principle, you can copy a short definition of the AlfWorld task (based on Yao et al., 2022) and use that as the instruction for your agent.

```python
INSTRUCTIONS = """
Interact with a simulated household to achieve a high-level goal. Make sure to plan, track subgoals,
determine likely locations for common household items (e.g. desklamps will likely be on desks, shelfs, or dressers),
and explore systematically (e.g. check all desks one by one for desklamp).
""".strip()

self.react = dspy.Predict(dspy.Signature("task, trajectory, possible_actions: list[str] -> action", INSTRUCTIONS))
```

### Zero-shot evaluation

```python
agent_4o = Agent()
agent_4o.set_lm(gpt4o)
agent_4o.verbose = True
agent_4o(**example.inputs())
```

The zero-shot GPT-4o agent fails the example task — picks up the soapbar but never satisfies the *clean* precondition, then thrashes between `examine garbagecan 1` and `look` until iteration cap.

```python
metric = lambda x, y, trace=None: y.success
evaluate = dspy.Evaluate(devset=devset, metric=metric, display_progress=True, num_threads=16)

evaluate(agent_4o)
# Average Metric: 115.00 / 200 (57.5%)

agent_4o_mini = Agent()
agent_4o_mini.set_lm(gpt4o_mini)
evaluate(agent_4o_mini)
# Average Metric: 30.00 / 200 (15.0%)
```

Out of the box, on this task, 4o is decent (58% success rate) while 4o-mini struggles (15% success rate).

Let's apply the following strategy:

1. We'll optimize the _prompts_ for gpt-4o in a lightweight way.
2. We'll then use this prompt-optimized agent as a teacher to fine-tune gpt-4o-mini on the task. This will increase its quality from 19% to 72% (or 82% if you use 500 trainset examples).

### Prompt-optimizing GPT-4o

```python
optimizer = dspy.MIPROv2(metric=metric, auto="light", num_threads=16, prompt_model=gpt4o)
config = dict(max_bootstrapped_demos=1, max_labeled_demos=0, minibatch_size=40)
optimized_4o = optimizer.compile(agent_4o, trainset=trainset, **config)
```

### Fine-tuning GPT-4o-mini

For fine-tuning, we'll need a teacher program (`optimized_4o` above) and a student program derived from it (`student_4om` below).

```python
student_4o_mini = optimized_4o.deepcopy()
student_4o_mini.set_lm(gpt4o_mini)
# student_4o_mini.react.demos = []  # you can optionally reset the demos

optimizer = dspy.BootstrapFinetune(metric=metric, num_threads=16)
finetuned_4o_mini = optimizer.compile(student_4o_mini, teacher=optimized_4o, trainset=trainset)
```

### Evaluate the finetuned GPT-4o-mini agent

```python
evaluate(finetuned_4o_mini)
# Average Metric: 143.00 / 200 (71.5%)
```

Save:

```python
finetuned_4o_mini.save('finetuned_4o_mini_001.pkl')
```

> **⚠️ Security Warning:** Loading `.pkl` files can execute arbitrary code and may be dangerous. Only save and load pickle files from trusted sources in secure environments. Consider using JSON format when possible for safer serialization.

Load:

```python
loaded = Agent()
loaded.load('finetuned_4o_mini_001.pkl', allow_pickle=True)
```

### Headline results

| Configuration | Devset success | Δ vs 4o-mini zero-shot |
|---|---|---|
| GPT-4o zero-shot | 57.5% (115/200) | +42.5 pts |
| GPT-4o-mini zero-shot | 15.0% (30/200) | baseline |
| GPT-4o-mini after MIPROv2-teacher + BootstrapFinetune | **71.5%** (143/200) | **+56.5 pts (~4.8×)** |

The fine-tuned 4o-mini **exceeds the GPT-4o teacher's zero-shot score by +14 pts** while running on a smaller, cheaper model.
