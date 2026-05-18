# DSPy Learn — Signatures

Source URL: https://dspy.ai/learn/programming/signatures/
Retrieved: 2026-05-17
Page 4 of 13 in the DSPy *Learn* documentation.

---

## Signatures

When assigning tasks to language models in DSPy, behavior is specified through a Signature.

**A signature is a declarative specification of input/output behavior of a DSPy module.** Signatures enable you to communicate *what* needs to happen rather than *how* to prompt the model.

Unlike traditional function signatures that merely describe arguments, DSPy Signatures both declare and initialize module behavior. Field names carry semantic weight — a `question` differs fundamentally from an `answer`.

### Why Use DSPy Signatures?

For modular, maintainable code where LM calls compile into optimized prompts or automatic finetunings. Rather than crafting lengthy, fragile prompts or collecting training data, signatures provide a cleaner, more reproducible approach.

> "The DSPy compiler will figure out how to build a highly-optimized prompt for your LM (or finetune your small LM) for your signature, on your data, and within your pipeline."

---

## Inline DSPy Signatures

Signatures defined as short strings with argument names and optional types establishing semantic roles:

1. **Question Answering:** `"question -> answer"` (equivalent to `"question: str -> answer: str"`)
2. **Sentiment Classification:** `"sentence -> sentiment: bool"`
3. **Summarization:** `"document -> summary"`

Multiple input/output fields with types:

1. **RAG QA:** `"context: list[str], question: str -> answer: str"`
2. **Multiple-Choice with Reasoning:** `"question, choices: list[str] -> reasoning: str, selection: int"`

Field names should be semantically meaningful but kept simple initially. Add instructions using the `instructions` keyword argument:

```python
toxicity = dspy.Predict(
    dspy.Signature(
        "comment -> toxic: bool",
        instructions="Mark as 'toxic' if the comment includes insults, harassment, or sarcastic derogatory remarks.",
    )
)
comment = "you are beautiful."
toxicity(comment=comment).toxic
```

**Output:** `False`

### Example A: Sentiment Classification

```python
sentence = "it's a charming and often affecting journey."

classify = dspy.Predict('sentence -> sentiment: bool')
classify(sentence=sentence).sentiment
```

**Output:** `True`

### Example B: Summarization

```python
document = """The 21-year-old made seven appearances for the Hammers and netted his only goal for them in a Europa League qualification round match against Andorran side FC Lustrains last season. Lee had two loan spells in League One last term, with Blackpool and then Colchester United. He scored twice for the U's but was unable to save them from relegation. The length of Lee's contract with the promoted Tykes has not been revealed. Find all the latest football transfers on our dedicated page."""

summarize = dspy.ChainOfThought('document -> summary')
response = summarize(document=document)

print(response.summary)
```

**Possible Output:**

```
The 21-year-old Lee made seven appearances and scored one goal for West Ham last season. He had loan spells in League One with Blackpool and Colchester United, scoring twice for the latter. He has now signed a contract with Barnsley, but the length of the contract has not been revealed.
```

Many DSPy modules expand signatures under the hood. For example, `dspy.ChainOfThought` adds a `reasoning` field:

```python
print("Reasoning:", response.reasoning)
```

**Possible Output:**

```
Reasoning: We need to highlight Lee's performance for West Ham, his loan spells in League One, and his new contract with Barnsley. We also need to mention that his contract length has not been disclosed.
```

---

## Class-based DSPy Signatures

For advanced tasks requiring verbosity, use class-based signatures to:

1. Clarify task nature via docstring
2. Supply input field hints using `desc` parameter in `dspy.InputField`
3. Supply output field constraints using `desc` parameter in `dspy.OutputField`

### Example C: Classification

```python
from typing import Literal

class Emotion(dspy.Signature):
    """Classify emotion."""

    sentence: str = dspy.InputField()
    sentiment: Literal['sadness', 'joy', 'love', 'anger', 'fear', 'surprise'] = dspy.OutputField()

sentence = "i started feeling a little vulnerable when the giant spotlight started blinding me"

classify = dspy.Predict(Emotion)
classify(sentence=sentence)
```

**Possible Output:**

```python
Prediction(
    sentiment='fear'
)
```

### Example D: Citation Faithfulness Metric

```python
class CheckCitationFaithfulness(dspy.Signature):
    """Verify that the text is based on the provided context."""

    context: str = dspy.InputField(desc="facts here are assumed to be true")
    text: str = dspy.InputField()
    faithfulness: bool = dspy.OutputField()
    evidence: dict[str, list[str]] = dspy.OutputField(desc="Supporting evidence for claims")

context = "The 21-year-old made seven appearances for the Hammers and netted his only goal for them in a Europa League qualification round match against Andorran side FC Lustrains last season. Lee had two loan spells in League One last term, with Blackpool and then Colchester United. He scored twice for the U's but was unable to save them from relegation. The length of Lee's contract with the promoted Tykes has not been revealed. Find all the latest football transfers on our dedicated page."

text = "Lee scored 3 goals for Colchester United."

faithfulness = dspy.ChainOfThought(CheckCitationFaithfulness)
faithfulness(context=context, text=text)
```

**Possible Output:**

```python
Prediction(
    reasoning="Let's check the claims against the context. The text states Lee scored 3 goals for Colchester United, but the context clearly states 'He scored twice for the U's'. This is a direct contradiction.",
    faithfulness=False,
    evidence={'goal_count': ["scored twice for the U's"]}
)
```

### Example E: Multi-modal Image Classification

```python
class DogPictureSignature(dspy.Signature):
    """Output the dog breed of the dog in the image."""
    image_1: dspy.Image = dspy.InputField(desc="An image of a dog")
    answer: str = dspy.OutputField(desc="The dog breed of the dog in the image")

image_url = "https://picsum.photos/id/237/200/300"
classify = dspy.Predict(DogPictureSignature)
classify(image_1=dspy.Image.from_url(image_url))
```

**Possible Output:**

```python
Prediction(
    answer='Labrador Retriever'
)
```

---

## Type Resolution in Signatures

DSPy signatures support:

1. **Basic types:** `str`, `int`, `bool`
2. **Typing module types:** `list[str]`, `dict[str, int]`, `Optional[float]`, `Union[str, int]`
3. **Custom types** defined in your code
4. **Dot notation** for nested types with proper configuration
5. **Special data types:** `dspy.Image`, `dspy.History`

### Working with Custom Types

```python
class QueryResult(pydantic.BaseModel):
    text: str
    score: float

signature = dspy.Signature("query: str -> result: QueryResult")

class MyContainer:
    class Query(pydantic.BaseModel):
        text: str
    class Score(pydantic.BaseModel):
        score: float

signature = dspy.Signature("query: MyContainer.Query -> score: MyContainer.Score")
```

### Type Checking for Input Fields

DSPy automatically validates input field values match specified types. Type mismatches trigger warnings:

```python
class MathSignature(dspy.Signature):
    """Perform a mathematical operation."""
    number: int = dspy.InputField()
    result: str = dspy.OutputField()

predictor = dspy.Predict(MathSignature)

# This triggers a warning
predictor(number="42")  # Warning: Type mismatch for field 'number'
```

**Disabling Type Checking:**

```python
dspy.configure(warn_on_type_mismatch=False)

predictor = dspy.Predict("number: int -> result: str")
predictor(number="42")  # No warning
```

---

## Using Signatures to Build and Compile Modules

While signatures streamline prototyping with structured inputs/outputs, their primary value emerges when composing multiple signatures into larger DSPy modules and compiling these into optimized prompts and finetunings.
