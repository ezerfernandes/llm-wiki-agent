# Pipelines & Prompt Optimization with DSPy

**Author:** Drew Breunig (dbreunig.com)
**Date:** December 12, 2024
**URL:** https://www.dbreunig.com/2024/12/12/pipelines-prompt-optimization-with-dspy.html
**Tags:** AI, LLM, DSPy, Prompting, Machine Learning

---

## Introduction

The author discovered DSPy while seeking a framework for building a small agent to enhance their weather forecasting website. DSPy positions itself as "the framework for programming—rather than prompting—language models," significantly reducing time spent on manual prompt engineering by letting the framework handle prompt generation automatically.

---

## How DSPy Works: A Quick Overview

### Signatures

DSPy uses **signatures** to express desired tasks by defining inputs and outputs. Signatures can be simple string-based declarations:

```
'question -> answer'
'sentence -> sentiment: bool'
'document -> summary'
```

Or more complex class-based definitions that allow additional specifications for intricate tasks.

### Modules

**Modules** are runners that apply specific prompting techniques to generate and execute prompts against language models. The foundational module is `Predict`, which frames signatures with boilerplate instructions.

For example, given the signature `question -> answer` and input "What is the capital of France?", the `Predict` module generates structured system and user prompts that guide the LLM response.

---

## Practical Example: Categorizing Historic Events

### Setup

The author demonstrates DSPy's capabilities using a historic event categorization task, gathering descriptions from Wikipedia date pages like the Battle of Nineveh.

Installation and configuration:

```python
import dspy

lm = dspy.LM('ollama_chat/llama3.2:1b', api_base='http://localhost:11434')
dspy.configure(lm=lm)
```

They use a local Llama 3.2 1b model via Ollama for faster iteration.

### Class-Based Signature Definition

```python
from typing import Literal

class Categorize(dspy.Signature):
    """Classify historic events."""

    event: str = dspy.InputField()
    category: Literal[
        "Wars and Conflicts",
        "Politics and Governance",
        "Science and Innovation",
        "Cultural and Artistic Movements",
        "Exploration and Discovery",
        "Economic Events",
        "Social Movements",
        "Man-Made Disasters and Accidents",
        "Natural Disasters and Climate",
        "Sports and Entertainment",
        "Famous Personalities and Achievements"
    ] = dspy.OutputField()
    confidence: float = dspy.OutputField()

classify = dspy.Predict(Categorize)
```

The `Predict` module automatically generates detailed system prompts specifying input/output fields and formatting requirements.

### Initial Results

Using the small Llama 3.2 1b model achieved approximately 51.9% accuracy. The larger Llama 3.3 70b model reached higher accuracy but ran approximately 10 times slower. The performance gap reflected the smaller model's limited contextual knowledge rather than prompting deficiencies.

---

## Prompt Optimization with DSPy

### Defining Metrics and Training Data

To optimize prompts, DSPy requires a metric function and training dataset:

```python
def validate_category(example, prediction, trace=None):
    return prediction.category == example.category
```

The author generated a 300-example training set using Llama 3.3, which provided high-quality categorizations as ground truth.

### Using MIPROv2 Optimizer

DSPy's optimizer generates alternative prompting strategies using rephrasing, in-context examples, and other techniques:

```python
from dspy.teleprompt import *

tp = dspy.MIPROv2(metric=validate_category, auto="light")
optimized_classify = tp.compile(classify, trainset=trainset,
                                max_labeled_demos=0,
                                max_bootstrapped_demos=0)
```

Initial optimization improved the small model's accuracy from 51.9% to 63.0% by adding task-specific context to the prompt, though some overfitting occurred.

### Leveraging Separate Models for Prompt Generation

A more effective approach uses a larger model for generating prompting strategies while evaluating against the smaller model:

```python
lm = dspy.LM('ollama_chat/llama3.2:1b', api_base='http://localhost:11434')
prompt_gen_lm = dspy.LM('ollama_chat/llama3.3', api_base='http://localhost:11434')

tp = dspy.MIPROv2(metric=validate_category, auto="light",
                   prompt_model=prompt_gen_lm, task_model=lm)
optimized_classify = tp.compile(classify, trainset=trainset,
                                max_labeled_demos=0,
                                max_bootstrapped_demos=0)
```

This approach reduced overfitting while generating more generalizable prompting instructions, producing qualitatively better results despite slightly lower numerical accuracy (62%).

### Saving Optimized Configurations

Optimized systems can be persisted for reuse:

```python
optimized_classify.save("optimized_event_classifier.json")
```

---

## Key Takeaways

The author emphasizes that "there's something really clean and freeing about ceding the details and nuance of the prompt back to an LLM." DSPy abstracts away prompt engineering complexity, making systems more maintainable and easier to iterate on. This pattern becomes increasingly valuable as pipelines grow more complex with multiple modules and tool integrations.

The optimization process demonstrates that combining smaller, faster models with larger ones strategically—using the larger model for prompt generation while evaluating on the smaller model—yields better results than relying solely on either approach alone.
