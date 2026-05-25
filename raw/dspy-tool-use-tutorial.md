# Advanced Tool Use — DSPy Tutorial

Source: https://dspy.ai/tutorials/tool_use/

## Overview

Demonstrates building and optimizing a DSPy agent for the ToolHop task, achieving a **71% relative performance improvement** through prompt optimization (35.0% → 60.7% dev accuracy).

## Installation

```python
pip install -U dspy
pip install func_timeout datasets
pip install dspy[numpy]
pip install mlflow>=2.20
```

## LM Configuration

```python
import dspy

gpt4o = dspy.LM("openai/gpt-4o", temperature=0.7)
dspy.configure(lm=gpt4o)
```

## Dataset Loading

```python
from dspy.utils import download
import orjson
import random

download("https://huggingface.co/datasets/bytedance-research/ToolHop/resolve/main/data/ToolHop.json")

data = orjson.loads(open("ToolHop.json").read())
random.Random(0).shuffle(data)
```

## Data Preparation and Splitting

```python
import re
import inspect

examples = []
fns2code = {}

def finish(answer: str):
    """Conclude the trajectory and return the final answer."""
    return answer

for datapoint in data:
    func_dict = {}
    for func_code in datapoint["functions"]:
        cleaned_code = func_code.rsplit("\n\n# Example usage", 1)[0]
        fn_name = re.search(r"^\s*def\s+([a-zA-Z0-9_]+)\s*\(", cleaned_code)
        fn_name = fn_name.group(1) if fn_name else None

        if not fn_name:
            continue

        local_vars = {}
        exec(cleaned_code, {}, local_vars)
        fn_obj = local_vars.get(fn_name)

        if callable(fn_obj):
            func_dict[fn_name] = fn_obj
            fns2code[fn_obj] = (fn_name, cleaned_code)

    func_dict["finish"] = finish
    example = dspy.Example(
        question=datapoint["question"],
        answer=datapoint["answer"],
        functions=func_dict
    )
    examples.append(example.with_inputs("question", "functions"))

trainset = examples[:100]
devset = examples[100:400]
testset = examples[400:]
```

## Function Wrapping (Timeout Sandbox)

```python
from func_timeout import func_set_timeout

def wrap_function_with_timeout(fn):
    @func_set_timeout(10)
    def wrapper(*args, **kwargs):
        try:
            return {"return_value": fn(*args, **kwargs), "errors": None}
        except Exception as e:
            return {"return_value": None, "errors": str(e)}
    return wrapper

def fn_metadata(func):
    signature = inspect.signature(func)
    docstring = inspect.getdoc(func) or "No docstring."
    return dict(
        function_name=func.__name__,
        arguments=str(signature),
        docstring=docstring
    )
```

## Metric

```python
def metric(example, pred, trace=None):
    gold = str(example.answer).rstrip(".0").replace(",", "").lower()
    pred = str(pred.answer).rstrip(".0").replace(",", "").lower()
    return pred == gold
```

Normalization rules applied:
- Strip trailing ".0" from numbers
- Remove commas
- Lowercase
- Exact match

## Evaluator

```python
evaluate = dspy.Evaluate(
    devset=devset,
    metric=metric,
    num_threads=24,
    display_progress=True,
    display_table=0,
    max_errors=999
)
```

## Agent (Hand-Rolled ReAct)

```python
class Agent(dspy.Module):
    def __init__(self, max_steps=5):
        self.max_steps = max_steps
        instructions = (
            "For the final answer, produce short (not full sentence) answers "
            "in which you format dates as YYYY-MM-DD, names as Firstname "
            "Lastname, and numbers without leading 0s."
        )
        signature = dspy.Signature(
            'question, trajectory, functions -> next_selected_fn, args: dict[str, Any]',
            instructions
        )
        self.react = dspy.ChainOfThought(signature)

    def forward(self, question, functions):
        tools = {fn_name: fn_metadata(fn) for fn_name, fn in functions.items()}
        trajectory = []

        for _ in range(self.max_steps):
            pred = self.react(
                question=question,
                trajectory=trajectory,
                functions=tools
            )
            selected_fn = pred.next_selected_fn.strip('"').strip("'")
            fn_output = wrap_function_with_timeout(functions[selected_fn])(**pred.args)
            trajectory.append(dict(
                reasoning=pred.reasoning,
                selected_fn=selected_fn,
                args=pred.args,
                **fn_output
            ))

            if selected_fn == "finish":
                break

        return dspy.Prediction(answer=fn_output.get("return_value", ''), trajectory=trajectory)
```

## SIMBA Optimization

```python
simba = dspy.SIMBA(metric=metric, max_steps=12, max_demos=10)
optimized_agent = simba.compile(agent, trainset=trainset, seed=6793115)
```

## MLflow (Optional)

```python
import mlflow

mlflow.set_tracking_uri("http://localhost:5000")
mlflow.set_experiment("DSPy")
mlflow.dspy.autolog()
```

## Key Numbers

| Item | Value |
|---|---|
| LM | `openai/gpt-4o`, temperature 0.7 |
| Train / Dev / Test | 100 / 300 / 595 |
| Max agent steps | 5 |
| Tool timeout | 10 seconds (`func_set_timeout(10)`) |
| SIMBA `max_steps` | 12 |
| SIMBA `max_demos` | 10 |
| Optimizer seed | `6793115` |
| Eval threads | 24 |
| Baseline dev accuracy | **35.0%** |
| Optimized dev accuracy | **60.7%** |
| Relative improvement | **~71%** (+25.7 absolute pts) |

## Key Insight

> "For the final answer, produce short (not full sentence) answers in which you format dates as YYYY-MM-DD, names as Firstname Lastname, and numbers without leading 0s."

— the explicit instruction the optimizer refined (baseline Signature instruction). The post-optimization instruction text is not explicitly shown in the rendered tutorial.

## Dataset

[ByteDance ToolHop](https://huggingface.co/datasets/bytedance-research/ToolHop) — multi-hop QA benchmark where each datapoint ships its own bundle of Python tool source-code strings, an answer requiring multi-hop tool composition, and a `# Example usage` suffix that must be stripped before `exec()`.
