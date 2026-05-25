# DSPy Math Reasoning Tutorial

Source: https://dspy.ai/tutorials/math/

## Overview

Tutorial demonstrating how to optimize a DSPy module for algebra problem-solving on the MATH benchmark. Workflow: setup, baseline evaluation, prompt optimization with MIPROv2.

## Setup

```python
import dspy

gpt4o_mini = dspy.LM('openai/gpt-4o-mini', max_tokens=2000)
gpt4o = dspy.LM('openai/gpt-4o', max_tokens=2000)
dspy.configure(lm=gpt4o_mini)
```

- **Student LM**: GPT-4o-mini (default LM)
- **Teacher LM**: GPT-4o (used by optimizer for bootstrapped reasoning)

## Dataset

```python
from dspy.datasets import MATH

dataset = MATH(subset='algebra')
print(len(dataset.train), len(dataset.dev))
```

Output: `350 350`

- MATH benchmark, algebra subset
- 350 training examples, 350 dev examples
- Built-in `dataset.metric` for correctness scoring

### Example

```python
example = dataset.train[0]
print("Question:", example.question)
print("Answer:", example.answer)
```

Sample question: "The doctor has told Cal O'Ree that during his ten weeks of working out at the gym, he can expect each week's weight loss to be 1% of his weight at the end of the previous week. His weight at the beginning of the workouts is 244 pounds."

## Module

```python
module = dspy.ChainOfThought("question -> answer")
module(question=example.question)
```

Simple `ChainOfThought` module with signature `question -> answer`. No custom prompt engineering — DSPy generates the prompt from the signature.

## Baseline Evaluation

```python
THREADS = 24
kwargs = dict(num_threads=THREADS, display_progress=True, display_table=5)
evaluate = dspy.Evaluate(devset=dataset.dev, metric=dataset.metric, **kwargs)

evaluate(module)
```

Output: `74.0` (259/350 correct on dev set)

## Optimization with MIPROv2

```python
kwargs = dict(num_threads=THREADS, teacher_settings=dict(lm=gpt4o), prompt_model=gpt4o_mini)
optimizer = dspy.MIPROv2(metric=dataset.metric, auto="medium", **kwargs)

kwargs = dict(max_bootstrapped_demos=4, max_labeled_demos=4)
optimized_module = optimizer.compile(module, trainset=dataset.train, **kwargs)
```

Configuration:
- `teacher_settings`: GPT-4o generates bootstrapped reasoning traces
- `prompt_model`: GPT-4o-mini proposes new instructions
- `auto="medium"`: medium-budget optimization preset
- `max_bootstrapped_demos=4`: up to 4 LM-generated demonstrations in final prompt
- `max_labeled_demos=4`: up to 4 ground-truth labeled demonstrations

## Results

```python
evaluate(optimized_module)
```

Output: `88.57` (310/350 correct)

**Lift: 74.0% → 88.6%** (+14.6 percentage points absolute, ~20% relative improvement)

## Inspection

```python
dspy.inspect_history()
```

Inspects the optimized prompt and recent LM calls. Optimized prompt incorporates mathematical reasoning patterns from successful bootstrapped examples, providing structured guidance for systematic algebra problem solving.

## Notes

- MLflow tracing recommended for visualization and explainability during optimization.
- Workflow generalizes: any task expressible as a DSPy signature can follow the same pattern (baseline → MIPROv2 → re-evaluate).
