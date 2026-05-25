---
title: "LLM Engineer's Handbook — Ch 10: Inference Pipeline Deployment"
type: source
tags: [book, llm-engineering, llm-engineers-handbook, deployment, mlops, sagemaker, microservices, autoscaling, rag, fastapi]
date: 2024-10-22
source_file: raw/books/llm-engineers-handbook/ch10-inference-pipeline-deployment.md
---

## Summary
Chapter 10 of the LLM Engineer's Handbook walks through the design and concrete implementation of the LLM Twin's **inference pipeline deployment**. It first establishes a four-criterion framework (throughput, latency, data, infrastructure) for choosing among three deployment archetypes — **online real-time inference**, **asynchronous inference**, and **offline batch transform** — and then weighs **monolithic** vs **microservices** architectures for ML serving. The authors then justify their concrete choice for the LLM Twin: an online real-time microservice split, where a **FastAPI business service** handles RAG retrieval/augmentation and a separate **AWS SageMaker** LLM microservice runs the fine-tuned model inside a **Hugging Face Deep Learning Container** (DLC) powered by the **Text Generation Inference (TGI)** engine. The chapter then provides an end-to-end SageMaker deployment automation (IAM roles, `ResourceManager`, `DeploymentService`, `SagemakerHuggingfaceStrategy`, `HuggingFaceModel`, `ResourceRequirements`, plus a thin `LLMInferenceSagemakerEndpoint` + `InferenceExecutor` client wrapper) and a FastAPI `/rag` endpoint that glues retrieval to LLM invocation. It closes with an **Application Auto Scaling** primer — registering a scalable target, defining a `TargetTrackingScaling` policy (e.g., `SageMakerInferenceComponentInvocationsPerCopy`), min/max replica bounds, and cooldown periods — plus warnings about over-scaling cost and under-scaling user experience.

## Key Claims
- Every ML deployment trades off four requirements: **throughput** (RPS), **latency** (ms per request), **data** (size/type/format of inputs and outputs), and **infrastructure** (CPU/GPU/network/storage); the four interact non-trivially and define user experience.
- **Lower per-request latency translates to higher throughput only when requests are parallelized**; with batching, latency and throughput are coupled in the opposite direction (a 200 ms batch of 60 requests is 300 RPS even though latency is 2× a 100 ms batch of 20 at 200 RPS).
- Google's 2016 mobile-site study (cited) — **53% of visits are abandoned if a mobile site takes longer than 3 s to load** — is used to argue that user-experience latency budgets dominate deployment design.
- **Three fundamental ML serving archetypes**: (1) online real-time (HTTP/REST or gRPC, synchronous, low latency); (2) asynchronous (queue-mediated, polling or push notification, decouples spikes); (3) offline batch transform (pull data → process in bulk → store results in object store / warehouse, optimized for throughput).
- **REST is more accessible but slower** (JSON serialization); **gRPC with protobuf** is faster on the wire and preferred for internal services within the same ML system, at the cost of schema-coupling between client and server.
- LLM-style services such as **ChatGPT** and **Claude** often use **WebSockets** to stream individual tokens (Server-Sent Events / SSE), improving perceived responsiveness in real-time inference.
- Asynchronous inference excels when (a) jobs take more than ~5 minutes, (b) traffic spikes can be smoothed by a queue rather than by scaling GPU VMs 10×, or (c) cost optimization beats latency (e.g., document summarization, deepfake processing, keyword extraction).
- Offline batch transform is appropriate when *predictions can be stale* (e.g., daily movie recommendations) but is unacceptable for high-freshness use cases (e.g., a social-media feed where 1-hour-old predictions look broken).
- **Monolithic ML serving** is simple to start but cannot scale GPU and CPU paths independently — the GPU sits idle during business-logic execution, wasting expensive A100/V100/A10G time; teams also can't split work cleanly.
- **Microservices architecture** decouples the LLM service (GPU-bound) from business logic (CPU/I-O-bound), enabling independent horizontal scaling, heterogeneous tech stacks (e.g., LLM in Rust/C++/ONNX/TensorRT, business logic in Python), and cheaper overall compute — at the cost of operational complexity and network-hop latency.
- A pragmatic migration path: **start monolithic, design for modularity (separate Python modules or even packages), then split into services later** — failing to design modularly forces a rewrite during the transition.
- The LLM Twin's concrete deployment choice: **online real-time + microservices**, with the LLM microservice on **AWS SageMaker** (Hugging Face DLC + TGI) and a **FastAPI business microservice** doing all RAG retrieval/augmentation.
- **SageMaker inference is composed of four artifacts**: **endpoint** (the HTTPS API SageMaker hosts), **model** (the trained-artifact wrapper with weights + compute logic), **endpoint configuration** (hardware/software setup), and **inference component** (binds model + config to the endpoint and is what `InvokeEndpoint` API targets).
- **Hugging Face DLCs** are pre-built Docker images bundling `transformers`, `datasets`, `tokenizers`, plus the **TGI** engine; TGI provides tensor parallelism, flash-attention-optimized transformers, `bitsandbytes` quantization, continuous batching, `safetensors` fast loading, and SSE token streaming.
- **Two IAM steps gate SageMaker deployment**: a narrow **SageMaker IAM user** (created via `poetry poe create-sagemaker-role`) that scopes credentials to SageMaker/ECR/S3 only, and a **SageMaker execution role** (`create-sagemaker-execution-role`) attached to the deployed endpoint so it can read S3, write CloudWatch, and pull ECR images on the user's behalf.
- The deployment workflow uses three Python classes implementing a strategy pattern: **`ResourceManager`** (boto3 wrapper that checks endpoint/config existence), **`DeploymentService`** (calls `HuggingFaceModel(...).deploy(...)` and orchestrates configuration), and **`SagemakerHuggingfaceStrategy`** (the high-level entry point that aggregates them).
- **`ResourceRequirements`** lets multi-replica endpoints declare `copies`, `num_accelerators` (GPUs), `num_cpus`, and `memory` (MB) — these directly drive cost and latency tradeoffs and should be tuned empirically.
- The TGI engine is configured via `HF_MODEL_ID`, `SM_NUM_GPUS`, `MAX_INPUT_LENGTH`, `MAX_TOTAL_TOKENS`, `MAX_BATCH_TOTAL_TOKENS`, `MAX_BATCH_PREFILL_TOKENS`, `HUGGING_FACE_HUB_TOKEN`, and `HF_MODEL_QUANTIZE` (e.g., `bitsandbytes`) — set via the SageMaker model `env` dict.
- The default deployment uses a single `ml.g5.xlarge` GPU instance; tweaking `GPUS`, `SM_NUM_GPUS`, and `GPU_INSTANCE_TYPE` in `.env` selects the hardware envelope; SageMaker deployments typically take 15–30 minutes.
- The published LLM Twin model is `mlabonne/TwinLlama-3.1-8B-13` — a fine-tuned **Llama 3.1 8B** stored in Hugging Face's hub used here as the model registry, deliberately sharable so readers don't have to spend ~$100 retraining.
- The client side uses an `Inference` interface implemented by **`LLMInferenceSagemakerEndpoint`** (boto3 `sagemaker-runtime` wrapper exposing `set_payload` / `inference`) plus an **`InferenceExecutor`** wrapper that injects a prompt template, sets `max_new_tokens` / `repetition_penalty` / `temperature`, and calls `invoke_endpoint`. Decoupling via an interface allows future swap-outs (e.g., to local inference) without touching call sites.
- The **business microservice** is a FastAPI app exposing `POST /rag` with Pydantic `QueryRequest` / `QueryResponse` schemas; the `rag()` function builds a `ContextRetriever`, fetches `k=3*3=9` documents from Qdrant, builds context via `EmbeddedChunk.to_context`, and delegates LLM generation to the SageMaker microservice via `call_llm_service`.
- The FastAPI server runs locally under `uvicorn ... --host 0.0.0.0 --port 8000 --reload`; productionization is left to AWS EKS or ECS (Dockerize → push to ECR → deploy), explicitly punted to Chapter 11 because it's not LLM-specific.
- **Always delete SageMaker resources after testing** (`poetry poe delete-inference-endpoint`) — pay-as-you-go GPU costs grow exponentially over idle days.
- **Training vs inference pipelines differ** in data access (offline batch with lineage vs online low-latency RAG), output (model weights vs predictions), and compute profile (high-VRAM GPU + gradients + optimizer state vs single-sample, no optimization); but **preprocessing/post-processing must be shared** between both to prevent training-serving skew.
- The training-serving skew problem is named explicitly as the failure mode of inconsistent preprocessing/post-processing across training and inference.
- **Autoscaling** is essential because static replica counts either burn money in idle periods or fail users during spikes; the SageMaker primitive is **Application Auto Scaling**, configured in two steps: (1) **register a scalable target** (resource ID, service namespace, scalable dimension, MinCapacity/MaxCapacity), then (2) **create a scaling policy** (e.g., `TargetTrackingScaling`) with a chosen metric.
- A canonical target metric is **`SageMakerInferenceComponentInvocationsPerCopy`**; alternative tracking can target GPU utilization (e.g., maintain ~70 % to leave headroom for spikes while limiting idle cost).
- An **Application Load Balancer (ALB)** sits between client and replicas, typically using round-robin routing, so adding/removing replicas does not change the client-facing endpoint.
- The **cooldown period** is the most important stability lever in autoscaling: it prevents rapid oscillation by delaying both scale-out (creating replicas) and scale-in (removing replicas) actions after a previous adjustment.
- **Two opposite autoscaling failure modes**: **over-scaling** (too aggressive policy / too short cooldown → idle replicas → cost blowup) and **under-scaling** (too conservative policy → user-experience degradation under load).
- Tuning autoscaling is analogous to **hyperparameter tuning**: stress-test in dev/test until the sweet spot between cost, latency, and throughput is found for both average and outlier traffic profiles.

## Key Quotes

> "Once deployed, an application can make HTTP requests to the endpoint to receive real-time predictions." — defining the SageMaker endpoint role

> "The Hugging Face Inference DLC ... includes a fully integrated serving stack, significantly simplifying the deployment process and reducing the technical expertise needed to serve deep learning models in production."

> "Continuous batching of incoming requests, thus improving throughput by dynamically batching requests as they arrive." — TGI's headline performance feature

> "If you start with a monolith and down the line you want to move to a microservices architecture, it's essential to design your software with modularity in mind. Otherwise, if the logic is mixed, you will probably have to rewrite everything from scratch."

> "Training-serving skew, where the model's performance during inference deviates from its performance during training." — the canonical bug avoided by sharing preprocessing logic

> "Adding or removing new replicas doesn't affect the server and client communication protocol." — why the ALB abstraction is load-bearing for autoscaling

> "Tweak and experiment with the autoscaling parameters in a dev or test environment until you find the sweet spot (similar to hyperparameter tuning when training models)."

## Deployment Components

### Serving stack
- **AWS SageMaker Inference endpoint** — the HTTPS-fronted SageMaker resource hosting the LLM microservice. Four sub-artifacts: endpoint, model, endpoint configuration, inference component.
- **Hugging Face Deep Learning Container (DLC)** — pre-built Docker image with `transformers` + `datasets` + `tokenizers` + TGI; specified via `get_huggingface_llm_image_uri("huggingface", version=None)`.
- **Text Generation Inference (TGI)** — Hugging Face's open-source LLM serving engine; tensor parallelism, flash-attention, `bitsandbytes` quantization, continuous batching, `safetensors` fast load, SSE token streaming. Repo: `huggingface/text-generation-inference`.
- **FastAPI** — Python web framework for the **business microservice**; exposes `POST /rag` and orchestrates RAG retrieval + LLM-microservice invocation.
- **uvicorn** — ASGI server used to run the FastAPI app locally on port 8000.
- **boto3** — AWS SDK for Python; used both for SageMaker control plane (`sagemaker` client) and inference (`sagemaker-runtime` client).
- **Qdrant** — online vector DB powering RAG retrieval in the business microservice.
- **Hugging Face Hub** — used as the **model registry**, holding `mlabonne/TwinLlama-3.1-8B-13`; chosen because it's free, sharable, and publicly accessible.
- **Comet** — prompt monitoring pipeline destination (detail deferred to Chapter 11).
- **AWS CloudWatch** — endpoint logs and CPU/GPU/memory/disk metrics; also hosts the alarms backing `TargetTrackingScaling`.
- **AWS ECR** — Docker image registry for SageMaker DLC images.
- **AWS S3** — model-artifact and configuration storage referenced by the SageMaker execution role.
- **AWS IAM** — narrow user (CLI-deploys SageMaker resources) and execution role (attached to SageMaker so it can reach S3/CloudWatch/ECR).
- **AWS Application Load Balancer (ALB)** — abstracts the multi-replica endpoint behind a single client-facing URL via round-robin routing.
- **AWS EKS / ECS** — future deployment target for the FastAPI service (left to Chapter 11).
- **AWS Application Auto Scaling** — the autoscaling control plane for SageMaker inference components.
- **`ml.g5.xlarge`** — default GPU instance type for the LLM Twin endpoint.

### Hardware mentioned for sizing
- **Nvidia A10G** — sufficient for an 8B-parameter quantized model (one machine).
- **Nvidia A100** — recommended upgrade for a 30B model.
- **Nvidia V100** — listed alongside A100/A10G as a typical LLM-serving GPU.

### Alternate tools the chapter calls out
- **Hopsworks**, **Modal**, **Google Vertex AI**, **Azure ML**, **Azure OpenAI**, **AWS Bedrock**, **Seldon**, **BentoML**, **NVIDIA Triton** — mentioned as alternative ML deployment platforms; choice depends on use case.

## Code & Concrete Examples

### Top-level deployment entry point
```python
def create_endpoint(endpoint_type=EndpointType.INFERENCE_COMPONENT_BASED):
    llm_image = get_huggingface_llm_image_uri("huggingface", version=None)
    resource_manager = ResourceManager()
    deployment_service = DeploymentService(resource_manager=resource_manager)
    SagemakerHuggingfaceStrategy(deployment_service).deploy(
        role_arn=settings.ARN_ROLE,
        llm_image=llm_image,
        config=hugging_face_deploy_config,
        endpoint_name=settings.SAGEMAKER_ENDPOINT_INFERENCE,
        endpoint_config_name=settings.SAGEMAKER_ENDPOINT_CONFIG_INFERENCE,
        gpu_instance_type=settings.GPU_INSTANCE_TYPE,
        resources=model_resource_config,
        endpoint_type=endpoint_type,
    )
```
Three-class strategy pattern: `ResourceManager` (existence checks via boto3), `DeploymentService` (orchestrates `HuggingFaceModel(...).deploy(...)`), `SagemakerHuggingfaceStrategy` (top-level facade).

### HuggingFaceModel instantiation (the SageMaker SDK call)
```python
huggingface_model = HuggingFaceModel(
    role=role_arn,
    image_uri=llm_image,
    env=config,
    transformers_version="4.6",
    pytorch_version="1.13",
    py_version="py310",
)
huggingface_model.deploy(
    instance_type=gpu_instance_type,
    initial_instance_count=1,
    endpoint_name=endpoint_name,
    update_endpoint=update_endpoint,
    resources=resources,
    tags=[{"Key": "task", "Value": "model_task"}],
    endpoint_type=endpoint_type,
)
```

### Multi-replica resource declaration
```python
from sagemaker.compute_resource_requirements.resource_requirements import ResourceRequirements
model_resource_config = ResourceRequirements(
    requests={
        "copies": settings.COPIES,
        "num_accelerators": settings.GPUS,
        "num_cpus": settings.CPUS,
        "memory": 5 * 1024,
    },
)
```

### TGI / HF engine configuration (passed as SageMaker model `env`)
```python
hugging_face_deploy_config = {
    "HF_MODEL_ID": settings.HF_MODEL_ID,                # e.g. mlabonne/TwinLlama-3.1-8B-13
    "SM_NUM_GPUS": json.dumps(settings.SM_NUM_GPUS),
    "MAX_INPUT_LENGTH": json.dumps(settings.MAX_INPUT_LENGTH),
    "MAX_TOTAL_TOKENS": json.dumps(settings.MAX_TOTAL_TOKENS),
    "MAX_BATCH_TOTAL_TOKENS": json.dumps(settings.MAX_BATCH_TOTAL_TOKENS),
    "HUGGING_FACE_HUB_TOKEN": settings.HUGGINGFACE_ACCESS_TOKEN,
    "MAX_BATCH_PREFILL_TOKENS": "10000",
    "HF_MODEL_QUANTIZE": "bitsandbytes",
}
```

### Client-side inference wrapper
```python
class LLMInferenceSagemakerEndpoint(Inference):
    def __init__(self, endpoint_name, default_payload=None, inference_component_name=None):
        super().__init__()
        self.client = boto3.client("sagemaker-runtime", ...)
        self.endpoint_name = endpoint_name
        self.payload = default_payload if default_payload else self._default_payload()
        self.inference_component_name = inference_component_name

    def _default_payload(self):
        return {
            "inputs": "",
            "parameters": {
                "max_new_tokens": settings.MAX_NEW_TOKENS_INFERENCE,
                "top_p": settings.TOP_P_INFERENCE,
                "temperature": settings.TEMPERATURE_INFERENCE,
                "return_full_text": False,
            },
        }

    def inference(self):
        invoke_args = {
            "EndpointName": self.endpoint_name,
            "ContentType": "application/json",
            "Body": json.dumps(self.payload),
        }
        if self.inference_component_name not in ["None", None]:
            invoke_args["InferenceComponentName"] = self.inference_component_name
        response = self.client.invoke_endpoint(**invoke_args)
        return json.loads(response["Body"].read().decode("utf8"))
```

### Inference executor (prompt templating + repetition penalty)
```python
class InferenceExecutor:
    def __init__(self, llm, query, context=None, prompt=None):
        self.llm = llm
        self.query = query
        self.context = context if context else ""
        self.prompt = prompt or """
You are a content creator. Write what the user asked you to while using the provided context as the primary source of information for the content.
User query: {query}
Context: {context}
        """

    def execute(self):
        self.llm.set_payload(
            inputs=self.prompt.format(query=self.query, context=self.context),
            parameters={
                "max_new_tokens": settings.MAX_NEW_TOKENS_INFERENCE,
                "repetition_penalty": 1.1,
                "temperature": settings.TEMPERATURE_INFERENCE,
            },
        )
        return self.llm.inference()[0]["generated_text"]
```

### FastAPI business microservice
```python
app = FastAPI()

class QueryRequest(BaseModel):
    query: str

class QueryResponse(BaseModel):
    answer: str

def call_llm_service(query, context):
    llm = LLMInferenceSagemakerEndpoint(
        endpoint_name=settings.SAGEMAKER_ENDPOINT_INFERENCE,
        inference_component_name=None,
    )
    return InferenceExecutor(llm, query, context).execute()

def rag(query):
    retriever = ContextRetriever(mock=False)
    documents = retriever.search(query, k=3 * 3)
    context = EmbeddedChunk.to_context(documents)
    return call_llm_service(query, context)

@app.post("/rag", response_model=QueryResponse)
async def rag_endpoint(request: QueryRequest):
    try:
        return {"answer": rag(query=request.query)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) from e
```

### Useful poe commands referenced
- `poetry poe create-sagemaker-role` — creates narrow IAM user.
- `poetry poe create-sagemaker-execution-role` — creates execution role for SageMaker.
- `poetry poe deploy-inference-endpoint` — runs `create_endpoint()`.
- `poetry poe test-sagemaker-endpoint` — runs an inference smoke test.
- `poetry poe run-inference-ml-service` — `uvicorn tools.ml_service:app --host 0.0.0.0 --port 8000 --reload`.
- `poetry poe call-inference-ml-service` — fires a POST to `/rag` with a sample query.
- `poetry poe delete-inference-endpoint` — tears down the SageMaker resources (do this every time to avoid runaway cost).

### Curl smoke test
```bash
curl -X POST 'http://127.0.0.1:8000/rag' \
  -H 'Content-Type: application/json' \
  -d '{"query": "your_query"}'
```

### Autoscaling worked example (from the chapter narrative)
- Idle: 1 replica (or scale-to-zero if latency permits).
- ~10 RPS: 2 replicas online.
- Spike to 100 RPS: scale to 20 replicas via `TargetTrackingScaling`, cooldown gates oscillation.
- Suggested target tracking metric: `SageMakerInferenceComponentInvocationsPerCopy` or GPU utilization ~70 %.

## Connections

### Existing wiki pages
- [[leh-ch01-understanding-llm-twin-concept]] — first chapter framing the FTI architecture this inference pipeline instantiates.
- [[AmazonSageMaker]] — the chapter's primary deployment target; this source significantly extends the wiki's SageMaker coverage from notebooks into managed inference endpoints, IAM roles, and autoscaling.
- [[Amazon]] — parent of AWS / SageMaker; the chapter relies on Amazon's whole inference stack (SageMaker, ECR, S3, CloudWatch, IAM, ALB, ECS/EKS).
- [[AmazonS3]] — referenced for model artifacts and the execution role's S3 access.
- [[HuggingFace]] — provides the DLC, TGI, model registry, and `safetensors` infrastructure; this chapter materially expands HF's wiki role beyond the `transformers` library.
- [[FastAPI]] — the business microservice framework; this chapter is the canonical example of FastAPI wrapping an LLM RAG endpoint.
- [[ModelServing]] — the chapter is the wiki's most complete walk through LLM model-serving design tradeoffs.
- [[OnlineInference]] — the chosen archetype for LLM Twin; chapter expands the wiki definition with batching/throughput nuances and SSE token streaming.
- [[BatchInference]] — contrasted as the offline batch transform archetype.
- [[Autoscaling]] — the wiki's autoscaling page is currently a stub; this chapter is the deepest treatment available (Application Auto Scaling, target tracking, cooldown, ALB).
- [[ModelRegistry]] — the chapter uses Hugging Face Hub as the registry rather than MLflow / SageMaker Model Registry.
- [[rag]] — RAG retrieval and augmentation live in the business microservice; chapter describes the split with the LLM microservice.
- [[MLOps]] — model-serving and autoscaling are core MLOps capabilities materialized here.
- [[FineTuning]] / [[LLMFineTuning]] — the deployed model is the fine-tuned LLM Twin from earlier chapters.
- [[Latency]] — the chapter defines latency vs throughput tradeoffs and ties them to user experience.
- [[lora]] / [[knowledgedistillation]] — quantization (`bitsandbytes`) mentioned as an inference-time optimization (Chapter 8 forward reference).
- [[flashattention]] — TGI uses flash-attention-optimized transformer kernels; this is one of the few practical deployment-side references to the technique in the wiki.
- [[FeatureStore]] — referenced as the data interface to the inference pipeline (Qdrant + versioned artifacts as a "logical feature store").
- [[CICD]] — adjacent MLOps capability the chapter explicitly defers to Chapter 11.
- [[CometML]] — destination of the prompt monitoring pipeline (Chapter 11 deep-dive).
- [[NVIDIA]] — A10G / A100 / V100 are the GPU envelopes the chapter sizes against.
- [[BentoML]] / [[NvidiaTriton]] / [[Ray]] / [[RayServe]] — listed as alternative serving stacks alongside SageMaker.

### New pages worth creating
- [[AWSSageMakerInferenceEndpoint]] — the specific managed-inference resource on SageMaker (vs the notebook surface currently covered in `AmazonSageMaker`).
- [[HuggingFaceDLC]] — Hugging Face Deep Learning Containers; pre-built serving Docker images for SageMaker.
- [[TextGenerationInference]] — Hugging Face's TGI engine (tensor parallelism, flash-attention, continuous batching, `safetensors`, SSE).
- [[ContinuousBatching]] — TGI's dynamic batching strategy that improves throughput by merging in-flight requests.
- [[TensorParallelism]] — the model-sharding strategy TGI uses to fit larger LLMs across GPUs.
- [[Safetensors]] — Hugging Face's fast/safe tensor serialization format used for accelerated weight loading.
- [[Bitsandbytes]] — the k-bit quantization library TGI integrates for `HF_MODEL_QUANTIZE`.
- [[ServerSentEvents]] — the SSE protocol TGI uses to stream tokens.
- [[WebSockets]] — alternative streaming protocol used by ChatGPT/Claude; mentioned for real-time LLM UX.
- [[gRPC]] — the binary RPC protocol contrasted with REST as a faster internal alternative.
- [[REST]] / [[RESTAPI]] — the dominant LLM API protocol; uses JSON.
- [[Protobuf]] — gRPC's compiled schema format.
- [[JSON]] — REST's wire format.
- [[OnlineRealTimeInference]] — distinct from the generic `OnlineInference` page; the chapter's specific archetype with synchronous client wait.
- [[AsynchronousInference]] — queue-mediated archetype with polling or push notifications; intermediate between online and offline.
- [[OfflineBatchTransform]] — the batch-from-storage-to-storage archetype.
- [[MicroservicesArchitecture]] — the chosen LLM Twin pattern; LLM microservice + business microservice.
- [[MonolithicArchitecture]] — the rejected single-process pattern.
- [[ApplicationAutoScaling]] — the AWS-specific autoscaling product; resource ID, service namespace, scalable dimension, min/max, cooldown.
- [[TargetTrackingScaling]] — the autoscaling policy type used in the chapter; metric + target value with auto-managed CloudWatch alarms.
- [[ScalableTarget]] — registered scaling boundary for a SageMaker inference component.
- [[ScalingPolicy]] — defines when scaling actions occur given a registered scalable target.
- [[CooldownPeriod]] — the autoscaling stability lever that delays both scale-in and scale-out adjustments.
- [[ApplicationLoadBalancer]] — AWS ALB; round-robin routing in front of multi-replica endpoints.
- [[RoundRobinRouting]] — the simplest load-balancer routing strategy.
- [[AmazonCloudWatch]] — host of endpoint logs and the alarms backing target tracking.
- [[AmazonECR]] — the Docker registry used for DLC images.
- [[AmazonEKS]] — Elastic Kubernetes Service; future home for the FastAPI service.
- [[AmazonECS]] — Elastic Container Service; alternative future home for the FastAPI service.
- [[AWSIAM]] — Identity and Access Management; the chapter creates a narrow user + execution role pair (note: a thin stub already exists).
- [[IAMUser]] — distinct from a role; used to authenticate the developer's CLI.
- [[IAMRole]] — attached to SageMaker so it can act on AWS services on the developer's behalf.
- [[ARN]] — Amazon Resource Name; identifies AWS resources globally.
- [[Boto3]] — the AWS Python SDK driving all deployment automation here.
- [[Qdrant]] — vector DB used for RAG retrieval in the business microservice.
- [[ZenML]] — pipeline orchestrator used elsewhere in the book; named here for training-pipeline data lineage.
- [[Uvicorn]] — ASGI server running the FastAPI app.
- [[Pydantic]] — used for FastAPI request/response schemas.
- [[TrainingServingSkew]] — failure mode the chapter calls out (preprocessing must match between training and inference).
- [[InferenceOptimization]] — generalizing the chapter's emphasis on quantization, flash attention, continuous batching, and tensor parallelism at serving time.
- [[GPUUtilization]] — a candidate scaling metric (~70 % target) suggested in the autoscaling section.
- [[InvokeEndpoint]] — SageMaker's runtime API used by `boto3.client("sagemaker-runtime").invoke_endpoint(...)`.
- [[InferenceComponent]] — the SageMaker artifact that binds model + config to an endpoint and can be scaled independently.
- [[GoogleCloudVertexAI]] / [[AzureML]] / [[AzureOpenAI]] / [[AmazonBedrock]] / [[Modal]] / [[Hopsworks]] / [[Seldon]] — alternative deployment platforms the chapter enumerates.
- [[TwinLlama]] — the published fine-tuned LLM Twin model (`mlabonne/TwinLlama-3.1-8B-13`) used as the canonical SageMaker deployment artifact.
- [[PaulIusztin]] / [[MaximeLabonne]] / [[AlexVesa]] — book co-authors.

## Contradictions
- None observed within the wiki. The chapter's claim that "Hugging Face Hub serves as a model registry" is a pragmatic redefinition of [[ModelRegistry]] (which the existing concept page describes more abstractly as "a versioned store of trained model artifacts"), but it doesn't contradict that definition — it instantiates it.
- The chapter notes that latency-throughput coupling reverses when batching is in play; this is consistent with the wiki's existing [[Latency]] / [[BatchInference]] / [[OnlineInference]] pages, just sharper.
