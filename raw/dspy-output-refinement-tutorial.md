# Output Refinement: BestOfN and Refine Tutorial

Source: https://dspy.ai/tutorials/output_refinement/best-of-n-and-refine/

## Overview

Both `BestOfN` and `Refine` are DSPy modules that "improve the reliability and quality of predictions by making multiple LM calls with different rollout IDs to bypass caching."

## BestOfN Module

### Purpose
`BestOfN` executes a module repeatedly (up to N times) with different rollout IDs, returning either the first prediction exceeding a threshold or the highest-scoring result.

### Basic Usage Example
```python
import dspy

def one_word_answer(args, pred: dspy.Prediction) -> float:
    return 1.0 if len(pred.answer.split()) == 1 else 0.0

best_of_3 = dspy.BestOfN(
    module=dspy.ChainOfThought("question -> answer"),
    N=3,
    reward_fn=one_word_answer,
    threshold=1.0
)

result = best_of_3(question="What is the capital of Belgium?")
print(result.answer)  # Brussels
```

### Error Handling
The `fail_count` parameter controls error tolerance:
```python
best_of_3 = dspy.BestOfN(
    module=qa,
    N=3,
    reward_fn=one_word_answer,
    threshold=1.0,
    fail_count=1  # raises error after first failure
)
```

## Refine Module

### Purpose
`Refine` extends `BestOfN` by adding "an automatic feedback loop" where unsuccessful attempts generate detailed performance feedback used as hints for subsequent runs.

### Basic Usage Example
```python
import dspy

def one_word_answer(args, pred: dspy.Prediction) -> float:
    return 1.0 if len(pred.answer.split()) == 1 else 0.0

refine = dspy.Refine(
    module=dspy.ChainOfThought("question -> answer"),
    N=3,
    reward_fn=one_word_answer,
    threshold=1.0
)

result = refine(question="What is the capital of Belgium?")
print(result.answer)  # Brussels
```

### Error Handling
```python
refine = dspy.Refine(
    module=qa,
    N=3,
    reward_fn=one_word_answer,
    threshold=1.0,
    fail_count=1
)
```

## Key Differences

- **BestOfN**: Tries different rollouts and selects the best result per the reward function
- **Refine**: Adds feedback generation, where the LM analyzes performance and uses insights to improve subsequent attempts

## Practical Examples

### Factual Correctness Validation
```python
import dspy

class FactualityJudge(dspy.Signature):
    """Determine if a statement is factually accurate."""
    statement: str = dspy.InputField()
    is_factual: bool = dspy.OutputField()

factuality_judge = dspy.ChainOfThought(FactualityJudge)

def factuality_reward(args, pred: dspy.Prediction) -> float:
    statement = pred.answer
    result = factuality_judge(statement)
    return 1.0 if result.is_factual else 0.0

refined_qa = dspy.Refine(
    module=dspy.ChainOfThought("question -> answer"),
    N=3,
    reward_fn=factuality_reward,
    threshold=1.0
)

result = refined_qa(question="Tell me about Belgium's capital city.")
print(result.answer)
```

### Length-Controlled Summarization
```python
import dspy

def ideal_length_reward(args, pred: dspy.Prediction) -> float:
    """Reward summaries near 75 words with tapering for longer text."""
    word_count = len(pred.summary.split())
    distance = abs(word_count - 75)
    return max(0.0, 1.0 - (distance / 125))

optimized_summarizer = dspy.BestOfN(
    module=dspy.ChainOfThought("text -> summary"),
    N=50,
    reward_fn=ideal_length_reward,
    threshold=0.9
)

result = optimized_summarizer(text="[Long text to summarize...]")
print(result.summary)
```

## Migration Note

As of DSPy 2.6, these modules replace `dspy.Suggest` and `dspy.Assert`.
