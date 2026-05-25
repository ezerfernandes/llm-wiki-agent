---
title: "LLM Engineer's Handbook — Ch 11: MLOps and LLMOps"
type: source
tags: [book, llm-engineering, llm-engineers-handbook, mlops, llmops, cicd, continuous-training, monitoring, aws, zenml]
date: 2024-10-22
source_file: raw/books/llm-engineers-handbook/ch11-mlops-and-llmops.md
---

## Summary
Chapter 11 — the longest in the book — closes the LLM Twin project by giving it production-grade operational maturity. The authors first build the theoretical scaffolding (**DevOps → MLOps → LLMOps**), arguing that LLMOps inherits the six MLOps principles (automation, versioning, experiment tracking, testing, monitoring, reproducibility) and adds LLM-specific concerns: prompt monitoring with full traces, input/output guardrails, RLHF/DPO feedback loops, and the realization that very few organizations train foundation models from scratch (~$100M for GPT-4) so most LLMOps work centers on fine-tuning, prompt engineering, and RAG. The second half is a hands-on deployment: provisioning serverless MongoDB and Qdrant, spinning up an AWS stack (S3, ECR, SageMaker, IAM, CloudFormation) through ZenML Cloud's in-browser experience, Dockerizing the codebase with a multi-stage `Dockerfile`, pushing to ECR, and switching ZenML to the `aws-stack` to run pipelines as SageMaker processing jobs. Finally, the chapter implements the LLMOps layer itself: a GitHub Actions **CI** pipeline (gitleaks → Ruff lint → Ruff format → pytest) and **CD** pipeline (build Docker image and push to ECR), a **CT** pipeline that chains ZenML pipelines end-to-end (`end_to_end_data` master pipeline), prompt and RAG tracing via Opik's `@track` decorator (logging model IDs, temperature, token counts, latency per step), and ZenML alerters that post pipeline success/failure to Slack/Discord/email. An appendix expands the six MLOps principles, including a deep dive on drift detection (data/target/concept) using KS tests for univariate features and MMD for embeddings, plus behavioral testing of NLP models (invariance, directional, minimum-functionality) following the CheckList paper.

## Key Claims
- **LLMOps is built on top of MLOps, which is built on top of DevOps**; LLMOps does not replace MLOps — it adds LLM-specific concerns (prompt monitoring/versioning, guardrails, human-feedback loops, scale of data and models) on top of the same six MLOps principles.
- **DevOps lifecycle** has eight stages: plan, code, build, test, release, deploy, operate, monitor; its core practices are deployment environments (dev/staging/prod), version control, **CI** (build + test on every change), and **CD** (automated infra provisioning + deployment).
- In DevOps the build is triggered by **code** changes; in MLOps the build can be triggered by changes in **code, data, or model** — three first-class citizens — and a change in one usually cascades to the others.
- A formal definition the chapter adopts: **"MLOps is the extension of the DevOps field that makes data and models their first-class citizen while preserving the DevOps methodology."**
- The four core **MLOps components** are: **model registry** (Comet ML, W&B, MLflow, ZenML), **feature store** (Hopsworks, Tecton, Featureform), **ML metadata store** (Comet ML, W&B, MLflow), and **ML pipeline orchestrator** (ZenML, Airflow, Prefect, Dagster) — most platforms unify several of these.
- The **six MLOps principles** are: automation/operationalization, versioning, experiment tracking, testing, monitoring, and reproducibility — all tool-agnostic.
- The three **automation tiers** are manual (Jupyter notebooks, DS-driven), **CT** (orchestrator-triggered retraining on schedule/event/drift), and full **CI/CD** that builds, tests, and deploys data + model + training pipelines.
- ML/MLOps role boundary: data scientists build models, ML engineers wrap them in modular code with DB/API access, and MLOps engineers deploy them onto generic infrastructure — at small/medium teams one person wears all three hats.
- **LLMOps is "MLOps at scale"**: GPT-4 was trained on ~13 trillion tokens at an estimated ~$100M cost, only a handful of organizations can afford to train foundation models from scratch, so most teams adopt foundation models and focus operationally on fine-tuning, prompt engineering, and RAG.
- **Human feedback loops** (thumbs-up/thumbs-down) collect preference data for alignment via [[rlhf]] and [[DPO]] (Direct Preference Optimization).
- **Guardrails** divide into **input guardrails** (private-data leak prevention, model-jailbreak/prompt-injection defense, blocking unethical/violent prompts) and **output guardrails** (catch empty/malformed/JSON-broken/toxic/hallucinated responses, sensitive-info leakage); tools cited include **Galileo Protect**, **OpenAI's Moderation API**.
- Guardrails add latency; to keep response time low, run **multiple generations in parallel and pick the best one** rather than sequential retries.
- **Prompt monitoring** is the distinctive LLMOps practice — log user input, prompt templates, input variables, generated answer, token counts, and latency; tools cited: **Opik** (Comet ML), **W&B**, **Langfuse**.
- LLM latency has multiple facets, not one metric: **Time to First Token (TTFT)**, **Time Between Tokens (TBT)**, **Tokens Per Second (TPS)**, **Time Per Output Token (TPOT)**, and **Total Latency** — all matter to UX because tokens stream.
- Always log the **full trace** (query rewrite → retrieval → final prompt → answer), with per-step latency, tokens, and costs — without traces you cannot localize failures in multi-step LLM systems.
- The LLM Twin AWS infrastructure stack is: **MongoDB serverless (M0 free) + Qdrant cloud (GCP free) + ZenML cloud trial + AWS (ECR + S3 + SageMaker + IAM + CloudFormation)** — all pinned to `eu-central-1` (Frankfurt) for low cross-service latency.
- A ZenML **stack** is a set of components (orchestrator, object store, container registry) that defines an infrastructure target; switching from local development to AWS execution is a single `zenml stack set aws-stack` command.
- **CloudFormation** is the IaC tool ZenML uses to provision the AWS resources (S3 bucket, ECR repo, SageMaker orchestrator, IAM roles) via an in-browser experience; **Terraform** is offered as a more flexible alternative.
- The **Dockerfile** uses `python:3.11-slim-bullseye`, installs Google Chrome (needed by the crawler ETLs), Poetry 1.8.3, and copies the project last — **layer caching** keeps rebuilds fast since system + Python deps change rarely.
- Docker image must be built with `--platform linux/amd64` because the Google Chrome Linux installer is incompatible with macOS/Windows native targets.
- **Pipelines run asynchronously** on SageMaker via `zenml orchestrator update aws-stack --synchronous=False` to avoid CLI timeouts.
- Free-tier SageMaker uses `ml.t3.medium`; some AWS accounts ship with a zero quota for this instance type and must file a **Service Quotas** increase request before running pipelines.
- The LLM Twin **CI pipeline** (`.github/workflows/ci.yaml`) runs two jobs: a **QA** job (gitleaks → Ruff lint → Ruff format) and a **Test** job (pytest); static checks run first because they are faster — order matters.
- **Ruff** is preferred for both linting and formatting because it is written in Rust and is fast on large codebases; it incorporates PEP 8, common formatting checks, and deeper linting checks in a single tool.
- The **CD pipeline** (`.github/workflows/cd.yaml`) is triggered on push to `main`, uses `docker/setup-buildx-action`, configures AWS credentials from GitHub Actions secrets (`AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `AWS_REGION`, `AWS_ECR_NAME`), logs in via `aws-actions/amazon-ecr-login`, and pushes images tagged with both `latest` and the commit SHA.
- The **CT pipeline** is enabled by two prior design choices: the **FTI architecture** (modular pipelines with clear interfaces) and **starting with an orchestrator on day 0** (ZenML used locally from the very beginning, which forced inter-pipeline communication through versioned storage rather than ad-hoc CLI flags).
- CT triggers fall into three categories: **manual** (CLI/dashboard), **REST API** (HTTP-triggered, e.g., a watcher service), and **scheduled** (cron expressions); the LLM Twin uses manual triggers because its data sources are static link lists.
- The reference solution chains all data pipelines into one `end_to_end_data` master pipeline as a **workaround for ZenML free-tier's 3-pipeline limit**; the authors note this is an anti-pattern — ideally each pipeline stays isolated and uses `Client().trigger_pipeline(...)` to fire downstream.
- Prompt monitoring is implemented at the **business microservice**, not the LLM microservice — the business service has the end-to-end view (RAG retrieval, query rewriting, postprocessing) needed for a meaningful trace.
- Use Opik's `@track` decorator on `rag()`, `call_llm_service()`, `ContextRetriever.search()`, and `SelfQuery.generate()`; granularity is a developer judgment call — too much tracing produces noise that makes traces hard to debug.
- Three things to always log on a trace: **model configuration** (model IDs, temperature for both the LLM and the embedding model), **total tokens** (impacts serving cost), **per-step duration** (locates bottlenecks).
- **Alerting** via ZenML uses the active stack's alerter component (`Client().active_stack.alerter`) with `on_failure` callbacks and explicit `notify_on_success()` steps — the same code can fan out to Slack, Discord, or email.
- **Versioning the three dimensions** uses different mechanisms: **code → Git** (commits + Semantic Versioning major.minor.patch releases); **models → model registry** (also SemVer with alpha/beta); **data → DVC or artifact systems** for unstructured, SQL version columns for structured.
- **Testing across six layers**: unit, integration, system, acceptance, regression (cross-cutting), stress; ML adds explicit **data tests** (validity at ETL/feature ingestion) and **model tests** (input/output tensor shapes, loss decreases on a batch, overfits on a small batch, CPU+GPU parity, early-stopping/checkpoint logic).
- **Behavioral model testing** (per the CheckList paper) treats the model as a black box and probes **invariance** (synonym swaps should not change output), **directional** (sentiment flips should change output), and **minimum functionality** (trivial inputs the model must always get right).
- **Drift** is decomposed into three types: **data drift / covariate shift** (input distribution shifts), **target drift** (label distribution shifts), and **concept drift** (the input→output mapping itself shifts — gradually, suddenly, or periodically).
- Drift detection uses two windows — a **reference window** (from training data) and a **test window** (production data) — and a hypothesis test: **Kolmogorov–Smirnov (KS)** for univariate continuous features, **chi-squared** for categorical, and **Maximum Mean Discrepancy (MMD)** on dimensionality-reduced embeddings for text; `alibi_detect.cd.KSDrift` and `alibi_detect.cd.MMDDrift` are the cited implementations.
- **Monitoring vs. observability**: monitoring collects + visualizes pre-defined metrics; observability surfaces *internal state* so root causes can be diagnosed — a system can be monitored without being observable.
- **Reproducibility** requires both (a) tracking the inputs (dataset version, hyperparameters, seeds) and (b) fighting ML's inherent non-determinism by setting seeds before any pseudo-random operation (weight init, data sampling, augmentation, value imputation).
- An ML system **can complete training successfully and silently produce wrong results** — unlike traditional software, no exceptions are thrown; this is why monitoring + behavioral tests + drift detection are non-negotiable.

## Key Quotes

> "LLMOps is built on top of MLOps, which is built on top of development operations (DevOps)."

> "MLOps is the extension of the DevOps field that makes data and models their first-class citizen while preserving the DevOps methodology."

> "At its core, LLMOps is MLOps at scale."

> "The estimated training cost for GPT-4 is around $100 million, as stated by Sam Altman, the CEO of OpenAI."

> "Unfortunately, LLM systems are not reliable, as they often hallucinate."

> "There is a trade-off between the safety of your input/output and latency."

> "Monitoring is not new to LLMOps, but in the LLM world, we have a new entity to manage: the prompt."

> "We are not interested only in the input prompt and generated answer... We want to log the entire trace from the user's input until the final result is available."

> "Starting with an orchestrator since day 0... forced us to decouple each pipeline and transfer the communication between them solely through various types of data storage."

> "Once you can manually trigger all your ML pipelines through a single command, you can quickly adapt it to more advanced and complex scenarios."

> "Even in a fully automated ML system, it is recommended to have a manual step before accepting a new production model."

> "ML systems can successfully complete without throwing any errors. However, the real issue is that they produce incorrect results that can only be observed during evaluations or tests."

> "Data is the new oil, remember?" — closing remark of the book

## MLOps vs LLMOps

The chapter draws an explicit hierarchy:

| Layer | What it operationalizes | What it adds over the layer below |
|---|---|---|
| **DevOps** | Code | Plan/code/build/test/release/deploy/operate/monitor lifecycle; CI/CD; version control; multiple environments. Single first-class citizen: code. |
| **MLOps** | Code + Data + Model | Model registry, feature store, metadata store, orchestrator; six principles (automation, versioning, experiment tracking, testing, monitoring, reproducibility); **CT** in addition to CI/CD; drift detection; behavioral testing. Three first-class citizens. |
| **LLMOps** | Code + Data + Model + **Prompt** | Prompt monitoring with full traces and per-step latency/tokens/cost; **input + output guardrails**; **human feedback loops** (RLHF/DPO); awareness that training from scratch is economically out of reach for most teams, so focus shifts to fine-tuning + prompt engineering + RAG. Four first-class citizens. |

Key asymmetries:
- DevOps builds trigger on **code** changes only. MLOps builds trigger on code OR data OR model changes — a code-frozen build can still be needed when only data changes.
- MLOps adds the **CT pipeline** as a peer of CI/CD; LLMOps inherits CT but the most common LLMOps "retraining" is a fine-tune of an existing foundation model, not a from-scratch training run.
- LLMOps requires monitoring latency at **five different granularities** (TTFT, TBT, TPS, TPOT, total latency) because tokens stream — a coarse "request time" metric is misleading.
- LLMOps must defend against **prompt-injection / jailbreak** attacks, sensitive-data exfiltration, and toxic output — risks largely absent in classical ML monitoring.

## Tools / Platforms Covered

**Cloud and infra**
- **AWS SageMaker** (orchestrator + processing jobs + training/inference endpoints); pipelines map to SageMaker processing jobs on EC2 `ml.t3.medium` by default
- **AWS S3** as artifact and model object storage
- **AWS ECR** as the Docker container registry (image tagged `latest` + commit SHA)
- **AWS IAM** roles for cross-service permissions
- **AWS CloudFormation** as the IaC tool ZenML uses to provision the entire AWS stack
- **AWS EC2** (`ml.t3.medium` for SageMaker jobs; quota-gated)
- **Terraform** mentioned as an alternative IaC path for full control
- **MongoDB Atlas** (M0 free tier, AWS Frankfurt region) — `DATABASE_HOST` env var
- **Qdrant Cloud** (free tier on GCP) — `USE_QDRANT_CLOUD`, `QDRANT_CLOUD_URL`, `QDRANT_APIKEY`

**Orchestrators**
- **ZenML** (cloud trial; stacks; pipelines; secrets; alerter; `zenml connect`, `zenml stack set`, `zenml orchestrator update`)
- Alternatives surveyed: **Airflow**, **Prefect**, **Dagster**, **Metaflow**, **Kubeflow**

**MLOps platforms / model registries / experiment tracking**
- **Comet ML** (also provider of Opik)
- **MLflow**
- **Weights & Biases (W&B)**
- **Neptune**

**Feature stores**
- **Hopsworks**
- **Tecton**
- **Featureform**

**Data versioning**
- **DVC** (Data Version Control) — Git-like for datasets
- Artifact systems in Comet ML, W&B, ZenML

**Prompt monitoring / observability**
- **Opik** (Comet ML's prompt-tracing tool, used in the LLM Twin) — `@track` decorator, `opik_context.update_current_trace(...)`
- **Langfuse**
- **W&B** prompt logging

**Guardrails**
- **Galileo Protect** (prompt-injection, toxicity, privacy, hallucination detection)
- **OpenAI Moderation API** (input/output harm detection)

**CI/CD**
- **GitHub Actions** (used; `pull_request` and `push` triggers, `concurrency` cancel-in-progress, hosted Ubuntu runners)
- **GitHub** (version control), **GitLab** (cited as alternative)
- Alternatives surveyed: **GitLab CI/CD**, **CircleCI**, **Jenkins** (self-hosted)

**Python tooling**
- **Poetry 1.8.3** with `poethepoet` plugin (task runner — `poetry poe ...`)
- **Ruff** (linter + formatter, written in Rust, replaces Black/isort/Flake8/pylint)
- **Pytest** (test runner)
- **gitleaks** (secret scanner in CI)

**Drift detection**
- **alibi-detect** — `KSDrift`, `MMDDrift`

**Containers**
- **Docker** with `python:3.11-slim-bullseye` base; `docker buildx build --platform linux/amd64`
- Google Chrome installed inside the container for crawler ETLs

## Pipelines & Architecture

### Infrastructure deployment flow (Figure 11.5)

1. Build a Docker image with system deps + Python deps + LLM Twin code.
2. Push image to **AWS ECR**.
3. Trigger a ZenML pipeline from the local CLI or the ZenML cloud dashboard.
4. Each ZenML step is mapped to a **SageMaker processing job** on an EC2 VM; DAG dependencies determine which steps run in parallel vs. sequentially.
5. SageMaker pulls the image from ECR and runs the step inside a container.
6. The job reads/writes the **S3 artifact store**, **MongoDB**, and **Qdrant vector DB**; ZenML dashboard surfaces real-time pipeline state.

### LLM Twin CI/CD/CT topology (Figure 11.14, 11.19)

- **Feature branches → PR → staging** triggers **CI** (gitleaks → Ruff lint → Ruff format → pytest); merging triggers **CD** which builds + tags + pushes the Docker image to ECR.
- **Staging → PR → production** repeats the CI check, then CD pushes the production image.
- **CT** uses ZenML to chain (sequentially in the simplified version, or via `trigger_pipeline()` in the production version): data collection ETL → feature engineering → instruct-dataset generation → training → deploy.
- **Prompt monitoring** (Opik) and **alerting** (ZenML alerter) cut across all runtime pipelines.

### CT trigger types
- **Manual** — used by the LLM Twin because data sources are static.
- **REST API** — `Client().trigger_pipeline(...)` invoked by an external watcher service.
- **Scheduled** — cron expressions, e.g., `Schedule(cron_expression="* * 1 * *")`.

## Code & Concrete Examples

**Dockerfile highlights**

```dockerfile
FROM python:3.11-slim-bullseye AS release
ENV WORKSPACE_ROOT=/app/
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV POETRY_VERSION=1.8.3
ENV DEBIAN_FRONTEND=noninteractive
ENV POETRY_NO_INTERACTION=1

# Google Chrome installation (for crawler ETLs)
RUN apt-get update -y && \
    apt-get install -y gnupg wget curl --no-install-recommends && \
    wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | gpg --dearmor -o /usr/share/keyrings/google-linux-signing-key.gpg && \
    echo "deb [signed-by=/usr/share/keyrings/google-linux-signing-key.gpg] https://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list && \
    apt-get update -y && apt-get install -y google-chrome-stable && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir "poetry==$POETRY_VERSION"
RUN poetry config installer.max-workers 20

WORKDIR $WORKSPACE_ROOT
COPY pyproject.toml poetry.lock $WORKSPACE_ROOT
RUN poetry config virtualenvs.create false && \
    poetry install --no-root --no-interaction --no-cache --without dev && \
    poetry self add 'poethepoet[poetry_plugin]'

COPY . $WORKSPACE_ROOT   # last so unrelated code changes don't bust the deps layer
```

**Build + push to ECR**

```bash
docker buildx build --platform linux/amd64 -t llmtwin -f Dockerfile .

aws ecr get-login-password --region ${AWS_REGION} \
  | docker login --username AWS --password-stdin ${AWS_ECR_URL}

docker tag llmtwin ${AWS_ECR_URL}:latest
docker push ${AWS_ECR_URL}:latest
```

**Switch ZenML to the AWS stack and run a pipeline**

```bash
zenml stack set aws-stack
poetry poe export-settings-to-zenml
zenml orchestrator update aws-stack --synchronous=False
poetry poe run-end-to-end-data-pipeline
```

**Pipeline `parent_image` config (`configs/end_to_end_data.yaml`)**

```yaml
settings:
  docker:
    parent_image: <ECR URL>   # e.g. 992382797823.dkr.ecr.eu-central-1.amazonaws.com/zenml-rlwlcs:latest
    skip_build: True
```

**CI workflow excerpt (`.github/workflows/ci.yaml`)**

```yaml
name: CI
on:
  pull_request:

concurrency:
  group: ${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: true

jobs:
  qa:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v3
        with: { python-version: "3.11" }
      - uses: abatilo/actions-poetry@v2
        with: { poetry-version: 1.8.3 }
      - run: |
          poetry install --only dev
          poetry self add 'poethepoet[poetry_plugin]'
      - run: poetry poe gitleaks-check
      - run: poetry poe lint-check
      - run: poetry poe format-check
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      # ... setup ...
      - run: poetry poe test
```

**CD workflow excerpt (`.github/workflows/cd.yaml`)**

```yaml
name: CD
on:
  push:
    branches: [main]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: docker/setup-buildx-action@v3
      - uses: aws-actions/configure-aws-credentials@v1
        with:
          aws-access-key-id:     ${{ secrets.AWS_ACCESS_KEY_ID }}
          aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          aws-region:            ${{ secrets.AWS_REGION }}
      - id: login-ecr
        uses: aws-actions/amazon-ecr-login@v1
      - uses: docker/build-push-action@v6
        with:
          context: .
          file: ./Dockerfile
          tags: |
            ${{ steps.login-ecr.outputs.registry }}/${{ secrets.AWS_ECR_NAME }}:${{ github.sha }}
            ${{ steps.login-ecr.outputs.registry }}/${{ secrets.AWS_ECR_NAME }}:latest
          push: true
```

**CT master pipeline (chained `end_to_end_data`)**

```python
@pipeline
def end_to_end_data(author_links: list[dict[str, str | list[str]]], ...) -> None:
    wait_for_ids = []
    for author_data in author_links:
        last_step_invocation_id = digital_data_etl(
            user_full_name=author_data["user_full_name"], links=author_data["links"]
        )
        wait_for_ids.append(last_step_invocation_id)
    author_full_names = [a["user_full_name"] for a in author_links]
    wait_for_ids = feature_engineering(author_full_names=author_full_names, wait_for=wait_for_ids)
    generate_instruct_datasets(...)
    training(...)
    deploy(...)
```

**Pipeline-to-pipeline trigger (the recommended pattern, blocked by the free-tier 3-pipeline limit)**

```python
@step
def trigger_feature_engineering_pipeline(user):
    run_config = PipelineRunConfiguration(...)
    Client().trigger_pipeline("feature_engineering", run_configuration=run_config)

@pipeline
def digital_data_etl(user_full_name: str, links: list[str]) -> str:
    user = get_or_create_user(user_full_name)
    crawl_links(user=user, links=links)
    trigger_feature_engineering_pipeline(user)
```

**Opik tracing of a RAG flow**

```python
from opik import track
from opik import opik_context

@track
def call_llm_service(query: str, context: str | None) -> str:
    llm = LLMInferenceSagemakerEndpoint(...)
    return InferenceExecutor(llm, query, context).execute()

@track
def rag(query: str) -> str:
    retriever = ContextRetriever()
    documents = retriever.search(query, k=3 * 3)
    context = EmbeddedChunk.to_context(documents)
    answer, prompt = call_llm_service(query, context)
    trace = get_current_trace()
    trace.update(
        tags=["rag"],
        metadata={
            "model_id": settings.HF_MODEL_ID,
            "embedding_model_id": settings.TEXT_EMBEDDING_MODEL_ID,
            "temperature": settings.TEMPERATURE_INFERENCE,
            "prompt_tokens": compute_num_tokens(prompt),
            "total_tokens": compute_num_tokens(answer),
        },
    )
    return answer
```

**ZenML alerter callback**

```python
from zenml import pipeline
from zenml.client import Client

alerter = Client().active_stack.alerter

def notify_on_failure() -> None:
    alerter.post(message=build_message(status="failed"))

@step(enable_cache=False)
def notify_on_success() -> None:
    alerter.post(message=build_message(status="succeeded"))

@pipeline(on_failure=notify_on_failure)
def training_pipeline(...):
    ...
    notify_on_success()
```

**Drift detection examples (Appendix)**

```python
# Univariate KS test on a single continuous feature
from alibi_detect.cd import KSDrift
cd = KSDrift(X_ref, p_val=.05, preprocess_fn=preprocess_fn, input_shape=(max_len,))

# Multivariate MMD on text embeddings
from alibi_detect.cd import MMDDrift
cd = MMDDrift(x_ref, backend='pytorch', p_val=.05)
preds = cd.predict(x)
```

## LLM Latency Metrics

| Metric | Definition |
|---|---|
| **TTFT** (Time to First Token) | Time from request to the first generated token |
| **TBT** (Time Between Tokens) | Interval between successive tokens during streaming |
| **TPS** (Tokens Per Second) | Rate of token generation |
| **TPOT** (Time Per Output Token) | Per-token time cost in the streamed response |
| **Total Latency** | End-to-end time to complete the response |

Plus **total input + output tokens** to track serving costs.

## Drift Taxonomy (Appendix)

| Drift type | What changes | Typical fix |
|---|---|---|
| **Data drift / covariate shift** | Distribution of input features | Retrain on fresh data once degradation is confirmed |
| **Target drift** | Distribution of labels / output classes | Adapt head + post-processing, optionally retrain |
| **Concept drift** | Mapping between input and output (gradual, sudden, periodic) | Retrain — old patterns are obsolete |

Detection requires a **reference window** (training data) vs. a **test window** (production data) and a hypothesis test (**KS** for univariate continuous, **chi-squared** for categorical, **MMD** on reduced embeddings for text).

## Connections

- [[leh-ch01-understanding-llm-twin-concept]] — the FTI architecture introduced in Ch 1 is what makes the CT pipeline of Ch 11 tractable; the prompt monitoring requirement listed there is implemented here.
- [[MLOps]] — this chapter is the definitive in-wiki source on what MLOps means as a discipline (components + six principles).
- [[CICD]] — concrete GitHub Actions implementation of CI (gitleaks/Ruff/pytest) and CD (Docker build + push to ECR).
- [[Monitoring]] / [[ModelMonitoring]] — extends to prompt-trace monitoring and per-token latency metrics in the LLM context.
- [[ModelRegistry]] / [[FeatureStore]] / [[FeatureEngineering]] — components recapped as MLOps building blocks.
- [[DataDrift]] / [[TargetDrift]] / [[ConceptDrift]] / [[LabelShift]] — full drift taxonomy and detection recipes covered in the appendix.
- [[Reproducibility]] / [[ReproducibilityInML]] — codified as one of the six MLOps principles with seed-setting guidance.
- [[Hallucination]] — primary risk that motivates LLMOps guardrails.
- [[Guardrail]] / [[GuardrailsAI]] / [[NeMoGuardrails]] — chapter discusses input/output guardrails (Galileo Protect, OpenAI Moderation) at the LLM layer.
- [[Jailbreak]] / [[promptinjection]] — explicitly the targets of input guardrails.
- [[rlhf]] / [[DPO]] — the techniques the human-feedback loop feeds.
- [[rag]] — the runtime architecture being instrumented with Opik tracing.
- [[CometML]] — vendor of Opik (prompt monitoring) and the experiment-tracking platform behind the LLM Twin.
- [[MLflow]] / [[WeightsAndBiases]] / [[Neptune]] — alternative experiment-tracking + model-registry platforms.
- [[AmazonSageMaker]] — the orchestrator runtime used; ZenML pipeline steps materialize as SageMaker processing jobs.
- [[GitHub]] / [[GitHubActions]] — version control + CI/CD platform.
- [[FastAPI]] — the business microservice (from Ch 10) is where Opik tracing is wired in.
- [[ChipHuyen]] — Chip Huyen's "Building a generative AI platform" essay is one of the chapter's primary external references.
- [[SecretsScanning]] — implemented in the CI pipeline via gitleaks.
- [[CanaryDeployment]] / [[ShadowDeployment]] — the chapter's "manual red button" guidance complements these progressive-rollout patterns.
- [[DVC]] / [[GitLFS]] — the data-versioning tools cited as code-equivalent for datasets.
- [[Reproducibility]] / [[Versioning]] — codified as MLOps principles.
- [[Testing]] / [[UnitTesting]] / [[IntegrationTesting]] / [[RegressionTesting]] / [[BehavioralTesting]] / [[CheckList]] — the six-tier testing taxonomy plus behavioral NLP testing per the CheckList paper.
- [[madewithml-mlops-monitoring]] / [[madewithml-mlops-cicd]] / [[madewithml-mlops-testing]] / [[madewithml-mlops-experiment-tracking]] / [[madewithml-mlops-versioning]] — Goku Mohandas' Made-With-ML course is cited as a primary reference.

## Contradictions

- None observed against existing wiki pages. The chapter's framing of [[MLOps]] components (model registry, feature store, metadata store, orchestrator) is consistent with how those concepts are described elsewhere in the wiki, and its drift taxonomy aligns with [[DataDrift]], [[TargetDrift]], [[ConceptDrift]], and [[LabelShift]]. The "compress all steps into a master pipeline" pattern in the LLM Twin code is *explicitly self-flagged* by the authors as an anti-pattern adopted only because ZenML's free trial caps tenants at three pipelines — not a contradiction with best practice but a documented workaround.
