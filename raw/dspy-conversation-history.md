# Managing Conversation History — DSPy Tutorial

**Source:** https://dspy.ai/tutorials/conversation_history/

## Overview

DSPy provides the `dspy.History` utility to manage conversation history in AI applications like chatbots, though automatic management isn't built into `dspy.Module`.

## Using dspy.History to Manage Conversation History

The `dspy.History` class functions as an input field type containing a `messages: list[dict[str, Any]]` attribute that tracks conversational exchanges.

### Implementation Steps

Two essential procedures apply when managing conversation history:

1. **Include a `dspy.History` field in your Signature**
2. **Maintain a history instance at runtime**, appending each conversation turn with all relevant input and output field data

### Code Example

```python
import dspy
import os

os.environ["OPENAI_API_KEY"] = "{your_openai_api_key}"

dspy.configure(lm=dspy.LM("openai/gpt-4o-mini"))

class QA(dspy.Signature):
    question: str = dspy.InputField()
    history: dspy.History = dspy.InputField()
    answer: str = dspy.OutputField()

predict = dspy.Predict(QA)
history = dspy.History(messages=[])

while True:
    question = input("Type your question, end conversation by typing 'finish': ")
    if question == "finish":
        break
    outputs = predict(question=question, history=history)
    print(f"\n{outputs.answer}\n")
    history.messages.append({"question": question, **outputs})

dspy.inspect_history()
```

## History in Few-Shot Examples

When including conversation history in few-shot demonstrations, DSPy maintains "compatibility with the OpenAI standard format" by representing each example as a single turn rather than expanding the history into multiple turns.

### Few-Shot Example Code

```python
import dspy

dspy.configure(lm=dspy.LM("openai/gpt-4o-mini"))

class QA(dspy.Signature):
    question: str = dspy.InputField()
    history: dspy.History = dspy.InputField()
    answer: str = dspy.OutputField()

predict = dspy.Predict(QA)
history = dspy.History(messages=[])

predict.demos.append(
    dspy.Example(
        question="What is the capital of France?",
        history=dspy.History(
            messages=[{"question": "What is the capital of Germany?", "answer": "The capital of Germany is Berlin."}]
        ),
        answer="The capital of France is Paris.",
    )
)

predict(question="What is the capital of America?", history=dspy.History(messages=[]))
dspy.inspect_history()
```

### Key Distinction

History data in few-shot examples appears as JSON within the history section rather than as expanded conversation turns, preserving standard prompt compatibility.
