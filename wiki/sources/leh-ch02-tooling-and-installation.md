---
title: "LLM Engineer's Handbook — Ch 2: Tooling and Installation"
type: source
tags: [book, llm-engineering, llm-engineers-handbook, mlops, llmops, tooling]
date: 2024-10-22
source_file: raw/books/llm-engineers-handbook/ch02-tooling-and-installation.md
---

## Summary
Chapter 2 of the LLM Engineer's Handbook is a tour of the tech stack used to build the `LLM Twin` project across the rest of the book. It walks through the Python ecosystem (pyenv for Python version management, Poetry for dependency/virtualenv management, and Poe the Poet as a task runner), the MLOps/LLMOps tooling (Hugging Face as a model registry, ZenML as an orchestrator with pipelines/steps/artifacts/metadata and a "stack" abstraction, Comet ML for experiment tracking, and Opik for prompt monitoring), the storage layer (MongoDB as a NoSQL store for raw scraped data and Qdrant as the vector database), and the AWS setup (root account, IAM admin user, access keys, AWS CLI, and SageMaker for training and inference compute). The chapter justifies each choice against alternatives (uv, Pipenv, Conda, W&B, MLflow, Neptune, Airflow, Prefect, Dagster, Metaflow, Kubeflow, Argo, Milvus, Pinecone, Weaviate, Chroma, pgvector, Langfuse, LangSmith, Galileo, Bedrock, EKS, ECS) and gives the exact Docker-based local recipe (`poetry poe local-infrastructure-up`) to bring up ZenML, MongoDB, and Qdrant on a developer's laptop.

## Key Claims
- All book code is pinned to Python 3.11.8, installed via `pyenv install 3.11.8` and selected per-repo by a checked-in `.python-version` file produced with `pyenv local 3.11.8`.
- Poetry (version 1.8.3 in the book) is used for both dependency specification (`pyproject.toml`) and virtualenv creation, and crucially writes a `poetry.lock` that pins exact transitive versions to eliminate "works on my machine" drift.
- `uv` (Rust-based) is flagged as a faster potential successor to Poetry worth testing; Venv/Conda lack dependency management and rely on the weaker `requirements.txt`; Pipenv is comparable to Poetry but slower.
- Poe the Poet is installed as a Poetry plugin (`poetry self add 'poethepoet[poetry_plugin]'`) and centralizes all CLI commands in `pyproject.toml` under `[tool.poe.tasks]`, replacing Makefile/Invoke/shell scripts and acting as living documentation.
- Local infra is brought up with three steps: Docker 27.1.1+ installed, `.env` filled with credentials, then `poetry poe local-infrastructure-up`, which exposes ZenML at `http://127.0.0.1:8237/` plus MongoDB and Qdrant containers.
- Hugging Face is chosen as the model registry purely for ecosystem reach — ZenML, Comet, and SageMaker each offer their own registries — and hosts the book's fine-tuned models `mlabonne/TwinLlama-3.1-8B` and `mlabonne/TwinLlama-3.1-8B-DPO` plus Hugging Face Spaces demos.
- ZenML is positioned as the bridge between ML research and MLOps; its primitives are `@pipeline` and `@step` decorators, and its differentiator vs Airflow/Prefect/Metaflow/Dagster/Argo/Kubeflow is the "stack" abstraction that lets the same Python code target local, AWS, GCP, or Azure infrastructure without vendor lock-in.
- The book's deployed ZenML stack pairs SageMaker (orchestrator + compute), S3 (artifact storage), and ECR (container registry); the application logic is encapsulated in an `llm_engineering` Python module so ZenML can be swapped out cleanly.
- ZenML auto-versions every step output as an `artifact` and supports user-attached metadata; the book demonstrates this by attaching dataset categories, train/test split size, and per-category sample counts to an `instruct_datasets` artifact via `step_context.add_output_metadata`.
- Pipelines are configured at runtime via YAML files in `configs/` (e.g. `digital_data_etl_maxime_labonne.yaml`) injected through `digital_data_etl.with_options()`, decoupling code from per-run inputs like user name and crawl link lists.
- ZenML's default materializer cannot serialize UUID return types out of the box — the authors had to extend it, and reported the issue upstream for inclusion in future versions.
- Comet ML is chosen as the experiment tracker over W&B, MLflow, and Neptune on UX grounds; the book's TwinLlama training runs are publicly viewable at `comet.com/mlabonne/llm-twin-training`. Comet logs training/eval loss, gradient norm, hyperparameters, and system metrics (GPU/CPU/memory) automatically.
- Opik (open source by Comet) is used for prompt monitoring because standard logging tools cannot capture chained, unstructured prompt traces; alternatives Langfuse (OSS), Galileo, and LangSmith are dismissed as more cumbersome.
- MongoDB stores raw scraped (unstructured) data before processing; Qdrant stores the processed, embedded data for GenAI retrieval. Qdrant is selected over Milvus/Redis/Weaviate/Pinecone/Chroma/pgvector for its RPS/latency/index-time trade-off, citing the Superlinked Vector DB Comparison.
- AWS is chosen as cloud provider; the book recommends an IAM user with `AdministratorAccess` for tutorial simplicity (explicitly noting this violates least-privilege for production), an access key pair, and `aws configure` with region `eu-central-1`.
- Estimated AWS spend for running the book end-to-end is $50–$100, almost entirely SageMaker training and inference; readers are told to set CloudWatch billing alarms.
- SageMaker is chosen over Bedrock because Bedrock is a serverless API over a limited model set (Mistral, Flan, Llama 2, Llama 3 at writing) and hides the engineering the book intends to teach; SageMaker exposes pay-as-you-go training and real-time inference endpoints with full customization, requiring autoscaling to manage idle cost.
- For maximum control beyond SageMaker, the authors point to AWS EKS (managed Kubernetes) or ECS, noting both are cheaper but require more engineering.

## Key Quotes
> "Because we defined a `.python-version` file within the repository, `pyenv` will know to pick up the version from that file and use it locally whenever you are working within that folder." — on per-repo Python pinning.

> "By locking all the dependencies and sub-dependencies to specific versions, the `poetry.lock` file ensures that all project installations use the same versions of each package." — on reproducibility through Poetry's lockfile.

> "ZenML acts as the bridge between ML and MLOps." — framing of ZenML's role in the stack.

> "The beauty of this is that ZenML doesn't vendor-lock you into any cloud platform. It completely abstracts away the implementation of your Python code from the infrastructure it runs on." — on the ZenML "stack" abstraction.

> "In MLOps, an artifact is any file(s) produced during the machine learning lifecycle, such as datasets, trained models, checkpoints, or logs." — working definition used in the chapter.

> "You cannot use standard logging tools as prompts are complex and unstructured chains." — motivating Opik vs traditional logs.

> "Bedrock would have been an excellent solution for quickly prototyping something, but this is a book on LLM engineering, and our goal is to dig into all the engineering aspects that Bedrock tries to mask away." — justifying SageMaker over Bedrock.

> "Based on our tests, the AWS costs can vary between $50 and $100 using the specifications provided in this book and repository." — explicit cost guidance.

## Tools & Services Covered
- **Python 3.11.8** — interpreter version pinned for the whole book.
- **pyenv** — installs and switches between Python versions per directory via `.python-version`.
- **Poetry 1.8.3** — declares dependencies in `pyproject.toml`, creates a virtualenv, and locks transitive versions in `poetry.lock`.
- **Poe the Poet** — task runner installed as a Poetry plugin; centralizes CLI commands as aliases in `pyproject.toml`.
- **uv** — Rust-based, faster alternative to Poetry the authors flag as worth testing.
- **Venv / Conda / Pipenv** — alternative virtualenv tools mentioned and contrasted.
- **Docker 27.1.1+** — used to spin up MongoDB, Qdrant, and ZenML locally with one Poe command.
- **Hugging Face Hub** — model registry hosting `TwinLlama-3.1-8B` and `TwinLlama-3.1-8B-DPO`.
- **Hugging Face Spaces** — hosts public demo apps for the TwinLlama models.
- **ZenML** — orchestrator with `@pipeline` / `@step` decorators, artifact/metadata system, and a `stack` abstraction for portable infrastructure.
- **Airflow / Prefect / Metaflow / Dagster / Argo Workflows / Kubeflow** — alternative orchestrators evaluated and rejected vs ZenML.
- **Comet ML** — experiment tracker for training/eval loss, gradient norm, hyperparameters, and system metrics.
- **Weights & Biases / MLflow / Neptune** — alternative experiment trackers compared.
- **Opik** — Comet's open-source prompt-monitoring tool for grouping prompt chains into traces.
- **Langfuse / Galileo / LangSmith** — alternative prompt-monitoring tools evaluated.
- **MongoDB** — NoSQL database for raw, unstructured scraped text.
- **Qdrant** — vector database for processed embeddings.
- **Milvus / Redis / Weaviate / Pinecone / Chroma / pgvector** — vector-DB alternatives compared; reader pointed to Superlinked's Vector DB Comparison.
- **AWS** — cloud provider for production deployment.
- **AWS IAM** — used to create the admin user that owns the access keys.
- **AWS CLI** — installed and configured via `aws configure` to talk to AWS programmatically.
- **AWS SageMaker** — training/inference compute and ZenML orchestrator backend.
- **AWS S3** — remote artifact storage in the production ZenML stack.
- **AWS ECR** — container registry in the production ZenML stack.
- **AWS Bedrock** — serverless LLM API rejected in favor of SageMaker.
- **AWS EKS / ECS** — alternatives to SageMaker for fuller infrastructure control.
- **AWS CloudWatch** — recommended for billing alarms while running book exercises.
- **Unsloth** — mentioned as the fine-tuning framework integrated via the Hugging Face registry.
- **GitHub (PacktPublishing/LLM-Engineers-Handbook)** — companion repo cloned in step one.

## Code & Concrete Examples
- Install and pin Python: `pyenv install 3.11.8`, `pyenv local 3.11.8`, then verify with `python --version`.
- Bootstrap repo: `git clone https://github.com/PacktPublishing/LLM-Engineers-Handbook.git && cd LLM-Engineers-Handbook && poetry install --without aws && poetry self add 'poethepoet[poetry_plugin]'`.
- Example `pyproject.toml` snippet for Poetry dependencies (`python = "^3.11"`, `requests = "^2.25.1"`, `numpy = "^1.19.5"`).
- Example `[tool.poe.tasks]` block defining `test = "pytest"`, `format = "black ."`, `start = "python main.py"`.
- Activate Poetry env: `poetry shell` or prefix each command with `poetry run`.
- Spin up local infra: `poetry poe local-infrastructure-up` (ZenML at `127.0.0.1:8237`, plus MongoDB + Qdrant Docker containers).
- ZenML pipeline definition: `@pipeline def digital_data_etl(user_full_name, links): user = get_or_create_user(user_full_name); crawl_links(user=user, links=links)`.
- ZenML step definition with typed return: `@step def get_or_create_user(user_full_name) -> Annotated[UserDocument, "user"]: ...`.
- Artifact metadata attachment with `ArtifactConfig(name="instruct_datasets", tags=["dataset", "instruct", "cleaned"])` and `step_context.add_output_metadata(...)`.
- Loading a specific artifact version: `Client().get_artifact_version('8bba35c4-8ff9-4d8f-a039-08046efc9fdc').load()`.
- Runtime pipeline configuration: `digital_data_etl.with_options(config_path=..., run_name=...)(**run_args_etl)`, with YAML configs like `configs/digital_data_etl_maxime_labonne.yaml` carrying `parameters.user_full_name` and `parameters.links`.
- Poe-wrapped run commands: `poetry poe run-digital-data-etl-maxime`, `poetry poe run-digital-data-etl-paul`.
- AWS CLI configuration sample with `aws_access_key_id`, `aws_secret_access_key`, `region = eu-central-1`, `output = json`.
- `.env` block for project AWS credentials: `AWS_REGION`, `AWS_ACCESS_KEY`, `AWS_SECRET_KEY`.

## Connections
- [[Python]] — chapter pins Python 3.11.8 as the runtime for every example.
- [[PythonLanguage]] — language used throughout the book.
- [[VirtualEnvironment]] — Poetry's role is to manage these per project to avoid global package clashes.
- [[Reproducibility]] — `poetry.lock` and YAML pipeline configs are presented as reproducibility levers.
- [[ReproducibilityInML]] — ZenML pipelines, artifacts, and metadata are framed as reproducibility infrastructure.
- [[MLOps]] — chapter is the MLOps tour for the rest of the book.
- [[ModelRegistry]] — Hugging Face Hub is the chosen model registry.
- [[ExperimentTracking]] — Comet ML fills this role.
- [[CICD]] — model registry is described as a key piece of CI/CD pipelines.
- [[DataPipeline]] — ZenML pipelines like `digital_data_etl` are the concrete data pipelines.
- [[ETL]] — `digital_data_etl` is an ETL crawling user web content.
- [[CLI]] — Poe the Poet plus `python -m tools.run` form the book's CLI surface.
- [[HuggingFace]] — model registry of record; hosts TwinLlama-3.1-8B.
- [[CometML]] — experiment tracker; also publisher of Opik.
- [[MLflow]] — listed as a comparable experiment tracker.
- [[WeightsAndBiases]] — listed as a comparable experiment tracker.
- [[Neptune]] — listed as a comparable experiment tracker.
- [[AmazonSageMaker]] — chosen training/inference compute and ZenML orchestrator backend.
- [[AmazonS3]] — remote artifact storage in the production stack.
- [[AWSIAM]] — used to create the admin user backing the AWS CLI access keys.
- [[Amazon]] — parent of the AWS services used.
- [[Kubeflow]] — orchestrator alternative compared to ZenML.
- [[Prefect]] — orchestrator alternative compared to ZenML.
- [[GitHub]] — hosts the companion repo `PacktPublishing/LLM-Engineers-Handbook`.
- [[Llama3_8BInstruct]] — base model family fine-tuned into TwinLlama 3.1 8B.
- [[FineTuning]] — downstream activity for which the registry, tracker, and SageMaker compute exist.
- [[Llama2_7BChat]] — mentioned as one of the Bedrock-hosted foundation models.
- [[ZenML]] — central orchestrator described in depth (new page).
- [[PoetryPython]] — Python dependency/virtualenv manager used throughout (new page).
- [[PoeThePoet]] — task runner plugin (new page).
- [[Pyenv]] — Python version manager (new page).
- [[MongoDB]] — NoSQL store for raw scraped data (new page).
- [[Qdrant]] — vector database for processed embeddings (new page).
- [[Opik]] — prompt-monitoring tool (new page).
- [[AmazonBedrock]] — serverless LLM API explicitly rejected for the book (new page).
- [[AmazonECR]] — container registry in the production ZenML stack (new page).
- [[AmazonEKS]] — Kubernetes alternative for full control (new page).
- [[AmazonECS]] — container orchestration alternative (new page).
- [[AmazonCloudWatch]] — used for AWS billing alarms (new page).
- [[AWSCLI]] — installed and configured via `aws configure` (new page).
- [[PacktPublishing]] — publisher and GitHub org hosting the companion repo (new page).
- [[PaulIusztin]] — co-author (new page).
- [[MaximeLabonne]] — co-author; owns the TwinLlama HF models (new page).
- [[AlexVesa]] — co-author (new page).
- [[TwinLlama]] — the fine-tuned model artifact the book produces (new concept).
- [[LLMTwin]] — the umbrella project being built across all chapters (new concept).
- [[DirectPreferenceOptimization]] — the technique behind `TwinLlama-3.1-8B-DPO` (new concept).
- [[Unsloth]] — fine-tuning framework integrated through the HF registry (new entity).
- [[UV]] — Rust-based Poetry alternative the authors recommend trying (new entity/tool).
- [[Conda]] — virtualenv alternative mentioned (new entity).
- [[Pipenv]] — virtualenv/dependency alternative mentioned (new entity).
- [[Airflow]] — orchestrator alternative (new entity).
- [[Dagster]] — orchestrator alternative (new entity).
- [[Metaflow]] — orchestrator alternative (new entity).
- [[ArgoWorkflows]] — orchestrator alternative (new entity).
- [[Kubernetes]] — substrate underneath Argo/Kubeflow/EKS (new concept).
- [[Docker]] — used to run local infra (new entity/concept).
- [[Pinecone]] — vector DB alternative (new entity).
- [[Milvus]] — vector DB alternative (new entity).
- [[Weaviate]] — vector DB alternative (new entity).
- [[ChromaDB]] — vector DB alternative (new entity).
- [[Pgvector]] — vector DB alternative (new entity).
- [[RedisVectorSearch]] — vector DB alternative (new entity).
- [[Langfuse]] — prompt-monitoring alternative (new entity).
- [[LangSmith]] — prompt-monitoring alternative (new entity).
- [[Galileo]] — prompt-monitoring alternative (new entity).
- [[Superlinked]] — publisher of the Vector DB Comparison (new entity).
- [[Pipeline]] — ZenML's `@pipeline` concept (new concept; or link to existing pipeline-themed page).
- [[Step]] — ZenML's `@step` concept (new concept).
- [[Artifact]] — central ZenML/MLOps unit defined in this chapter (new concept).
- [[Stack]] — ZenML stack abstraction (new concept).
- [[Orchestrator]] — defined here as the system that schedules and coordinates ML pipelines (new concept).
- [[PromptMonitoring]] — defined here as a non-standard logging discipline for chained prompts (new concept).
- [[DirectedAcyclicGraph]] — ZenML pipeline runs are visualized as DAGs (new concept).
- [[Serverless]] — used to describe Bedrock and ZenML Cloud (new concept).
- [[Materializer]] — ZenML's serializer extension point (new concept).

## Contradictions
- None observed. The chapter is a tooling tour and does not directly contest claims in other wiki pages. The recommendation to grant an IAM user `AdministratorAccess` for the tutorial is explicitly flagged as inappropriate for production (a self-noted deviation from least-privilege rather than a contradiction with prior wiki content).
