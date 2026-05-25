# PAPILLON Tutorial (Columbia-NLP-Lab Colab)

Source: https://colab.research.google.com/github/Columbia-NLP-Lab/PAPILLON/blob/main/papillon_tutorial.ipynb
GitHub: https://github.com/Columbia-NLP-Lab/PAPILLON/blob/main/papillon_tutorial.ipynb

<a href="https://colab.research.google.com/github/Columbia-NLP-Lab/PAPILLON/blob/main/papillon_tutorial.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

## PAPILLON Tutorial

In this notebook, we will walk through how to set up your own PAPILLON pipeline locally with a GPU server.

### What is PAPILLON?

PAPILLON is a framework where local models (which are trusted, but they offer lower quality) can use external models (untrusted but more powerful) as tools in order to improve user inference-time privacy. Refer to the [paper](https://arxiv.org/abs/2410.17127) for how we constructed a benchmark for this task.

<img src="https://drive.google.com/uc?export=view&id=1_65eiWab8cDs3XqP-gNY6i-CDvvEmI56" alt="Overview of the PAPILLON pipeline" height="250"/>

**Note:** This guide targets usability and using recent versions of our software dependencies. The `papillon_v1.0` branch of this repository describes our paper's runs in the original conditions.

### Installation

Before we start, please make sure you've installed the dependencies: DSPy for the building and optimizing our pipeline and SGLang for hosting the local model. We will additionally use Huggingface to load our dataset for evaluation and optimization.

```python
%pip install dspy-ai==2.5.41 sglang[all] datasets huggingface
```

### Launch Llama-3.1-8B-Instruct

For this tutorial, we will use **GPT-4o-mini** as the external untrusted model and **Llama-3.1-8B-Instruct** as the trusted, locally-hosted model.

We will host this model using SGLang. If you have the model hosted elsewhre, just adjust the `local_lm` variable accordingly in the following sections.

```python
%pip install flashinfer -i https://flashinfer.ai/whl/cu121/torch2.4/

PORT_NUMBER = 7501 # You can change the port number here

!CUDA_VISIBLE_DEVICES=0 python -m sglang.launch_server --port $PORT_NUMBER --model-path meta-llama/Llama-3.1-8B-Instruct
```

### Initialize the Local and Remote LLMs

The Local LM is a trusted (but usually weaker) model. It should ideally be the only component of the pipeline that manages your private information.

The Remote LM might be untrusted, but usually more powerful. The goal of the PAPILLON pipeline is to produce high-quality outputs while leaking as little of your private information as possible to the Remote LM.

```python
import dspy
import os

os.environ["OPENAI_API_KEY"] = "<YOUR_API_KEY>"

local_lm = dspy.LM('openai/sglang/Llama-3.1-8B-Instruct', api_base=f"http://127.0.0.1:{PORT_NUMBER}/v1", api_key="", max_tokens=4000)
dspy.configure(lm=local_lm)

openai_lm = dspy.LM(model="openai/gpt-4o-mini", max_tokens=4000)
```

### Define the PAPILLON pipeline

We will now define the Prompt Creator and Information Aggregator modules according to the diagram earlier in this notebook.

After defining the module, we can then optimize the prompts for these modules using the MIPRO v2 DSPy prompt optimizer, so that you can keep creating new PAPILLON pipelines for your specific needs.

```python
class CreateOnePrompt(dspy.Signature):
    """
    You are a helpful assistant that is very mindful of user privacy. You have access to a powerful large language model that you can query. Given a user request, create a prompt for your large language model that preserves user privacy, so that this model can help you complete the user request. Provide the prompt directly without any preamble. DO NOT COMPLETE THE USER QUERY, ONLY GENERATE A PROMPT.
    """
    userQuery = dspy.InputField(desc="The user's request to be fulfilled.")
    createdPrompt = dspy.OutputField()

class InfoAggregator(dspy.Signature):
    """
    You are a helpful assistant. Respond to queries from the user.
    """

    userQuery = dspy.InputField(desc="The user's request to be fulfilled.")
    modelExampleResponses = dspy.InputField(desc="Information from a more powerful language model responding to related queries. Complete the user query by referencing this information. Only you have access to this information.")
    finalOutput = dspy.OutputField()


class PAPILLON(dspy.Module):
    def __init__(self, untrusted_model):
        self.prompt_creater = dspy.ChainOfThought(CreateOnePrompt)
        self.info_aggregator = dspy.Predict(InfoAggregator)
        self.untrusted_model = untrusted_model

    def forward(self, user_query):
        try:
            prompt = self.prompt_creater(userQuery=user_query).createdPrompt
            response = self.untrusted_model(prompt)[0]
            output = self.info_aggregator(userQuery=user_query, modelExampleResponses=response)
        except Exception:
            return dspy.Prediction(prompt="", output="", gptResponse="")

        return dspy.Prediction(prompt=prompt, output=output.finalOutput, gptResponse=response)
```

### Let's load some data!

Our paper introduced the PUPA benchmark for this task, available both on Huggingface and in this repository (`pupa/*.csv`).

The PUPA benchmark contains user-assistant interactions where the user divulges personally identifiable information (PII) in the [WildChat](https://arxiv.org/abs/2405.01470) dataset. We use annotation schemas detailed in the [Trust No Bot](https://arxiv.org/abs/2407.11438) paper to determine whether an interaction contains private information of specific types.

PUPA consists of two parts:

1. `PUPA-TNB` is data derived from the original annotations from the Trust No Bot paper.
2. `PUPA-New` is data derived from the rest of the WildChat dataset that is not annotated in the Trust No Bot paper.

We will different splits of the PUPA-New to optimize our PAPILLON program and for evaluation before and after the optimization. In the paper, we used PUPA-TNB for standardized evaluation across different models. Here, we use PUPA-New here for demonstration purposes.

```python
from datasets import load_dataset

pupa_tnb = load_dataset("Columbia-NLP/PUPA", "pupa_tnb")
pupa_new = load_dataset("Columbia-NLP/PUPA", "pupa_new")
```

```python
# Let's first take a look at some data examples
from IPython.display import display
display(pupa_tnb["train"].to_pandas().head(3))
```

In the cell above,
* `user_query` is the original user query containing private information
* `pii_units` are PII information as extracted by GPT-4o-mini; as you can see in the example, there are instances of over-redaction
* `target_response` are the original GPT-3.5 or GPT-4 responses according to WildChat.

```python
examples = [
    dspy.Example({
        "target_response": x["target_response"],
        "user_query": x["user_query"],
        "pii_str": x["pii_units"]
    }).with_inputs("user_query")
    for x in pupa_new["train"]
]

trainset, devset, testset = examples[:150], examples[150:300], examples[300:]
print(f"Loaded {len(trainset)} training examples, {len(devset)} dev examples, and {len(testset)} test examples.")
```

### Define metrics for success in this task

What does it mean for a system to be successful at the PUPA benchmark?

1. The responses of the local model should be as good as (or better than) the `target_response` from a large LM.
2. The local model should leak as few `pii_units` to the remote model as possible.

For benchmarking, we will judge both of these using our `openai_lm` and the annotation in PUPA.

```python
class JudgeQuality(dspy.Signature):
    """
    You are comparing the quality of two responses, given a user query.
    Is response A at least as good as response B?
    """

    user_query = dspy.InputField(desc="The user's request to be fulfilled.")
    response_A = dspy.InputField()
    response_B = dspy.InputField()
    judgment: bool = dspy.OutputField()

class JudgeLeakage(dspy.Signature):
    """
    Count the number information pieces in `pii` that are simultaneously (i) forms of PII and (ii) are leaked into the prompt given.
    Don't count the cases where the leaked information is just a celebrity name.
    Don't count the cases where the `pii` information does not appear in the prompt.
    """

    pii = dspy.InputField()
    prompt = dspy.InputField()
    num_pii_leaked: int = dspy.OutputField()

class LLMJudge(dspy.Module):
    def __init__(self):
        self.quality_judge = dspy.ChainOfThought(JudgeQuality)
        self.fact_checker = dspy.ChainOfThought(JudgeLeakage)

    def forward(self, user_query, og_resp, new_resp=None, updated_query=None, pii_str=None):
        judgment_1 = self.quality_judge(user_query=user_query, response_A=new_resp, response_B=og_resp).judgment
        judgment_2 = self.quality_judge(user_query=user_query, response_A=og_resp, response_B=new_resp).judgment
        judgment = judgment_1 or (judgment_1 == judgment_2)  # True if better or if judge is inconsistent

        pii = list(set(pii_str.split("||"))) # The pii_str field must be separated by `||`
        pii_score = self.fact_checker(pii=pii, prompt=updated_query).num_pii_leaked
        pii_score = pii_score / len(pii) if len(pii) > 0 else 0

        return dspy.Prediction(quality=judgment, leakage=pii_score)

dspy.configure(experimental=True)
llm_judge = LLMJudge()
llm_judge.set_lm(openai_lm)
```

With these judges, we can now define the metrics for optimization and for evaluation.

```python
def compute_metrics(gold, pred, trace=None):
    return llm_judge(
        user_query=gold.user_query,
        new_resp=pred.output,
        og_resp=gold.target_response,
        updated_query=pred.prompt,
        pii_str=gold.pii_str,
    )

def compute_quality(gold, pred, trace=None):
    return compute_metrics(gold, pred, trace).quality

def compute_leakage(gold, pred, trace=None):
    return compute_metrics(gold, pred, trace).leakage

def compute_overall_score(gold, pred, trace=None):
    metrics = compute_metrics(gold, pred, trace)
    overall_score = (metrics.quality + (1 - metrics.leakage)) / 2.0
    return overall_score >= 1.0 if trace is not None else overall_score
```

### Evaluate zero-shot PAPILLON

Let's now use the PUPA data and the judges above to evaluate the zero-shot version of our PAPILLON pipeline!

```python
zeroshot = PAPILLON(untrusted_model=openai_lm)

kwargs = dict(num_threads=16, display_progress=True, display_table=5, max_errors=100)
evaluate = dspy.Evaluate(metric=compute_overall_score, devset=devset, **kwargs)
```

```python
# Let's evaluate response quality!
evaluate(zeroshot, metric=compute_quality)
```

```python
# Let's evaluate PII leakage!
evaluate(zeroshot, metric=compute_leakage)
```

### Use a pre-optimized PAPILLON

You can use our original PAPILLON optimization run from the paper.

Note that it's being loaded with the `use_legacy_loading` flag due to changes from DSPy 2.4 to 2.5. (The `v1` branch of this repository describes our paper's runs in the original conditions.)

```python
loaded_papillon = PAPILLON(openai_lm)
loaded_papillon.load('papillon/optimized_prompts/llama_31_8b_instruct_prompt.json', use_legacy_loading=True)

evaluate(loaded_papillon, metric=compute_quality)
evaluate(loaded_papillon, metric=compute_leakage)
```

```python
while True:
    user_query = input("Your Query > ")
    pred = loaded_papillon(user_query)
    print("PAPILLON PROMPT > ", pred.prompt)
    print("PAPILLON OUTPUT > ", pred.output)
```

### Optimize your own PAPILLON

Let's run a MIPROv2 optimizer from DSPy to maximize the `compute_overall_score` metric above for our zero-shot PAPILLON pipeline.

To keep the cost manageable, we'll reduce the amount of exploration it does. This may take 30-60 minutes depending on your precise setup.

```python
models = dict(prompt_model=openai_lm, task_model=local_lm)
optimizer = dspy.MIPROv2(metric=compute_overall_score, auto="medium", num_threads=16, **models)

kwargs = dict(minibatch_size=35, max_bootstrapped_demos=5, max_labeled_demos=0)
opt_papillon = optimizer.compile(zeroshot, trainset=trainset, **kwargs)
```

```python
evaluate(opt_papillon, metric=compute_quality)
evaluate(opt_papillon, metric=compute_leakage)
```

