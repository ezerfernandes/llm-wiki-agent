# Tutorial: Online RL over a Multi-Module DSPy Program

Source: https://dspy.ai/tutorials/rl_papillon/
Fetched: 2026-05-24

## Overview

This experimental tutorial demonstrates optimizing language model weights in
PAPILLON — a privacy-preserving delegation system — using ArborGRPO, which
extends the GRPO online reinforcement learning algorithm to sophisticated
multi-module LM programs.

## Status

Explicitly marked as "new and extremely EXPERIMENTAL" proof-of-concept
requiring community feedback; "in pure proof of concept and development mode."

## Purpose

Teach users to balance response quality with privacy protection by training a
compact 1.5B-parameter model to strategically delegate tasks to more powerful
but potentially untrustworthy external LLMs.

## PAPILLON system architecture

- Craft redacted requests that preserve privacy
- Query external LLM with obfuscated prompts
- Generate responses using contextual information without exposing sensitive
  details

## Evaluation metrics

The system optimizes dual objectives through custom judges:

1. *Quality assessment*: "responses of the local model should be as good as (or
   better than) the target_response from a large LM"
2. *Privacy leakage measurement*: Quantifies how many personally identifiable
   information elements appear in delegated prompts

## Setup requirements

- Arbor framework for distributed RL training
- DSPy for modular LM program composition
- OpenAI API access for judging and untrusted delegation
- Multiple GPUs (demonstrated on 4×H100)

```
pip install -U arbor-ai
pip install -U git+https://github.com/stanfordnlp/dspy.git@main
```

## Key modules

- `CraftRedactedRequest`: ChainOfThought module for privacy-preserving queries
- `RespondToQuery`: Predict module combining external and local knowledge
- `LLMJudge`: Dual assessment for quality and information leakage

### CraftRedactedRequest signature

```python
class CraftRedactedRequest(dspy.Signature):
    """Given a private user query, create a privacy-preserving request for a powerful external LLM."""
    user_query = dspy.InputField()
    llm_request = dspy.OutputField()
```

### RespondToQuery signature

```python
class RespondToQuery(dspy.Signature):
    """Respond to a user query with inspiration from related LLM request/response."""
    related_llm_request = dspy.InputField()
    related_llm_response = dspy.InputField(desc="information from powerful LLM")
    user_query = dspy.InputField(desc="user's request to fulfill")
    response = dspy.OutputField(desc="final response to user's request")
```

### PAPILLON module

```python
class PAPILLON(dspy.Module):
    def __init__(self, untrusted_model):
        self.craft_redacted_request = dspy.ChainOfThought(CraftRedactedRequest)
        self.respond_to_query = dspy.Predict(RespondToQuery)
        self.untrusted_model = untrusted_model

    def forward(self, user_query):
        llm_request = self.craft_redacted_request(user_query=user_query).llm_request
        llm_response = self.untrusted_model(llm_request)[0]
        response = self.respond_to_query(
            related_llm_request=llm_request, related_llm_response=llm_response, user_query=user_query
        ).response
        return dspy.Prediction(llm_request=llm_request, llm_response=llm_response, response=response)
```

### LLMJudge module

```python
class LLMJudge(dspy.Module):
    def __init__(self):
        self.quality_judge = dspy.ChainOfThought(JudgeQuality)
        self.fact_checker = dspy.ChainOfThought(JudgeLeakage)

    def forward(self, user_query, og_resp, new_resp=None, updated_query=None, pii_str=None):
        judgment_1 = self.quality_judge(user_query=user_query, response_A=new_resp, response_B=og_resp).judgment
        judgment_2 = self.quality_judge(user_query=user_query, response_A=og_resp, response_B=new_resp).judgment
        judgment = judgment_1 or (judgment_1 == judgment_2)
        pii = list(set(pii_str.split("||")))
        pii_score = self.fact_checker(pii=pii, prompt=updated_query).num_pii_leaked
        pii_score = pii_score / len(pii) if len(pii) > 0 else 0
        return dspy.Prediction(quality=judgment, leakage=pii_score)
```

## Reward function

```python
def compute_overall_score(gold, pred, trace=None):
    metrics = compute_metrics(gold, pred, trace)
    overall_score = (metrics.quality + (1 - metrics.leakage)) / 2.0
    return overall_score >= 1.0 if trace is not None else overall_score
```

## ArborGRPO configuration

```python
train_kwargs = {
    "per_device_train_batch_size": 8,
    "gradient_accumulation_steps": 4,
    "temperature": 1.0,
    "top_k": -1,
    "top_p": 1.0,
    "repetition_penalty": 1.0,
    "beta": 0.00,
    "learning_rate": 1e-6,
    "gradient_checkpointing": True,
    "bf16": True,
    "lr_scheduler_type": "constant_with_warmup",
    "loss_type": "dapo",
    "max_steps": 1000,
    "lora_config": {
        "lora_alpha": 16,
        "lora_dropout": 0.05,
        "r": 8,
        "target_modules": ["q_proj", "k_proj", "v_proj", "o_proj", "up_proj", "down_proj", "gate_proj"]
    },
}

compiler = ArborGRPO(
    metric=compute_overall_score,
    multitask=True,
    num_dspy_examples_per_grpo_step=4,
    num_samples_per_input=8,
    exclude_demos=True,
    num_train_steps=500,
    num_threads=24,
)

optimized_papillon = compiler.compile(student=papillon, trainset=trainset, valset=devset)
```

## Dataset loading

```python
examples = [
    dspy.Example(
        {"target_response": x["target_response"], "user_query": x["user_query"], "pii_str": x["pii_units"]}
    ).with_inputs("user_query")
    for x in pupa_new["train"]
]
trainset, devset, testset = examples[:225], examples[225:450], examples[450:]
```

## Results

Training three hours boosts the composite score (devset) from 54.6% to 60.0%.
Authors note the approach is "typically worse on cost/quality basis than"
conventional prompt optimization methods, yet represents "a solid start for
online RL over arbitrary LM programs for tiny LMs."
