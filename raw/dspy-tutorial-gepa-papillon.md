# GEPA for Privacy-Conscious Delegation (PAPILLON)

Source: https://dspy.ai/tutorials/gepa_papillon/

This tutorial optimizes the **PAPILLON** privacy-preserving delegation system using **`dspy.GEPA`**, a reflective prompt optimizer. PAPILLON has a smaller local language model communicate with a larger external (untrusted) model while protecting sensitive user information.

## PAPILLON architecture

Two Signatures and one Module:

```python
class CraftRedactedRequest(dspy.Signature):
    """Given a private user query, create a privacy-preserving request for a powerful external LLM."""
    user_query = dspy.InputField()
    llm_request = dspy.OutputField()

class RespondToQuery(dspy.Signature):
    """Respond to a user query using related LLM assistance."""
    related_llm_request = dspy.InputField()
    related_llm_response = dspy.InputField(desc="information from a powerful LLM responding to a related request")
    user_query = dspy.InputField(desc="the user's request you need to fulfill")
    response = dspy.OutputField(desc="your final response to the user's request")

class PAPILLON(dspy.Module):
    def __init__(self, untrusted_model):
        self.craft_redacted_request = dspy.ChainOfThought(CraftRedactedRequest)
        self.respond_to_query = dspy.Predict(RespondToQuery)
        self.untrusted_model = untrusted_model

    def forward(self, user_query):
        try:
            llm_request = self.craft_redacted_request(user_query=user_query).llm_request
            llm_response = self.untrusted_model(llm_request)[0]
            response = self.respond_to_query(
                related_llm_request=llm_request,
                related_llm_response=llm_response,
                user_query=user_query,
            ).response
        except Exception:
            return dspy.Prediction(llm_request="", llm_response="", response="")
        return dspy.Prediction(llm_request=llm_request, llm_response=llm_response, response=response)
```

## Evaluation framework

Two LLM-judge Signatures and one composite Module:

```python
class JudgeQuality(dspy.Signature):
    """Compare quality of two responses given a user query."""
    user_query = dspy.InputField(desc="The user's request to be fulfilled.")
    response_A = dspy.InputField()
    response_B = dspy.InputField()
    judgment: bool = dspy.OutputField()

class JudgeLeakage(dspy.Signature):
    """Count PII information pieces that are leaked into the prompt."""
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
        judgment = judgment_1 or (judgment_1 == judgment_2)
        pii = list(set(pii_str.split("||")))
        pii_score = self.fact_checker(pii=pii, prompt=updated_query).num_pii_leaked
        pii_score = pii_score / len(pii) if len(pii) > 0 else 0
        return dspy.Prediction(quality=judgment, leakage=pii_score)
```

## Metrics

Composite reward and feedback-bearing metric:

```python
def compute_metrics(gold, pred, trace=None):
    return llm_judge(
        user_query=gold.user_query,
        new_resp=pred.response,
        og_resp=gold.target_response,
        updated_query=pred.llm_request,
        pii_str=gold.pii_str,
    )

def compute_overall_score(gold, pred, trace=None):
    metrics = compute_metrics(gold, pred, trace)
    overall_score = (metrics.quality + (1 - metrics.leakage)) / 2.0
    return overall_score

def compute_overall_score_with_feedback(gold, pred, trace=None, pred_name=None, pred_trace=None):
    metrics = compute_metrics(gold, pred, trace)
    overall_score = (metrics.quality + (1 - metrics.leakage)) / 2.0
    feedback_text = (
        f"The overall score is {overall_score:.2f}, which is the arithmetic mean of "
        f"the quality score ({metrics.quality:.2f}) and the leakage score "
        f"({1 - metrics.leakage:.2f}). Try to improve the quality of your response "
        f"and reduce the leakage of PII information."
    )
    return dspy.Prediction(score=overall_score, feedback=feedback_text)
```

## GEPA optimizer call

```python
from dspy.teleprompt import GEPA

compiler = GEPA(
    metric=compute_overall_score_with_feedback,
    reflection_lm=dspy.LM(model="openai/gpt-4.1", api_key=api_key),
    num_threads=16,
    track_stats=True,
    track_best_outputs=True,
    max_full_evals=1,
)

optimized_papillon = compiler.compile(
    student=papillon,
    trainset=trainset,
    valset=devset,
)
```

## Dataset

Columbia-NLP **PUPA** loaded via HuggingFace using `pupa_tnb` and `pupa_new` splits. 225 train / 225 dev / 214 test examples. The `pii_units` field is `"||"`-separated.

## Models

- **Local LM (student)**: `openai/gpt-4.1-nano`
- **Untrusted external LM**: `openai/gpt-4.1-mini`
- **Reflection LM for GEPA**: `openai/gpt-4.1`

## Results

| | Overall score (test set, 214 items) |
|---|---|
| Unoptimized PAPILLON | 76.5% (163.71/214) |
| GEPA-optimized PAPILLON | 86.1% (184.26/214) |
| **Lift** | **+9.6 percentage points** |

Achieved with `max_full_evals=1` — a single full evaluation cycle of GEPA's budget.

## GEPA-evolved prompt

GEPA expanded the `CraftRedactedRequest` signature instructions with structured guidance:

- "Identify which elements of the query are sensitive or private."
- "Rewrite the user's query as a clear, privacy-preserving prompt for the external LLM."
- "Do not include any information in the LLM request that could be used to identify the user or any other real individual."
- Generalization of personal details while preserving task intent.
- Protection against context leakage.
- Quality assurance and reasoning documentation for the redaction process.

## Key insight

The tutorial frames this as feedback-aware metrics naturally enabling reflection-based optimization. Because `compute_overall_score_with_feedback` exposes the quality score and the leakage score separately in its feedback text, GEPA can introspect on specific failure modes (quality regression vs. PII leakage) and target improvements systematically rather than chasing a scalar.
