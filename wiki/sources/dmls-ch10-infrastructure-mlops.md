---
title: "Designing ML Systems — Ch 10: Infrastructure and Tooling for MLOps"
type: source
tags: [book, dmls, mlops, infrastructure, tooling, chip-huyen, oreilly, kubernetes, docker, feature-store, model-store, cloud, orchestration]
date: 2022-05-17
sources: []
source_file: raw/books/designing-ml-systems/dmls-ch10-infrastructure-mlops.txt
last_updated: 2026-05-23
---

## Summary
Chapter 10 of [[ChipHuyen|Chip Huyen]]'s *Designing Machine Learning Systems* ([[OReilly|O'Reilly]], 2022) argues that bringing ML to production is fundamentally an infrastructure problem and lays out a four-layer model of ML infrastructure: storage & compute, resource management, ML platform, and development environment. The chapter explicitly scopes itself to "reasonable scale" companies — those working with gigabytes-to-terabytes of data per day rather than the petabyte-scale FAAAM (Facebook, Apple, Amazon, Alphabet, Microsoft) regime — and surveys the tooling ecosystem layer by layer. Huyen traces the evolution from [[Cron|cron]] → schedulers → orchestrators → data-science workflow managers ([[Airflow]], [[ArgoWorkflows|Argo]], [[Prefect]], [[Kubeflow]], [[Metaflow]]), then dissects the three least-mature ML-platform components: [[ModelDeployment|model deployment]], [[ModelStore|model store]], and [[FeatureStore|feature store]]. The chapter closes with a build-versus-buy framework driven by company stage, competitive focus, and tool maturity — and warns that "while getting started with the cloud is easy, moving away from the cloud is hard."

## Key Claims
- **ML infrastructure has four layers, and the right amount depends on scale.** Huyen segments the world into (1) ad-hoc analytics shops needing only Jupyter/Pandas, (2) "reasonable scale" companies in the GB–TB/day range (10–hundreds of engineers) that benefit from increasingly standardized generalized ML infrastructure, and (3) FAAAM-scale operations (Facebook generated 4 PB/day in 2014, [[GoogleSearch|Google Search]] does 63K queries/sec) that build their own. The book targets the middle band.
- **Storage is commoditized; compute is the live battleground.** The storage layer has been "mostly commoditized and moved to the cloud" — data is now stored "without the cost." The chapter therefore focuses on the [[ComputeLayer|compute layer]], characterized by two metrics: how much memory a [[ComputeUnit|compute unit]] holds and how fast it runs operations.
- **A compute unit's identity varies by framework.** Threads/cores on bare CPU, "job" in Spark and Ray, "[[KubernetesPod|pod]]" (a container wrapper) in Kubernetes. AWS counts in vCPUs (≈ half a physical core). Short-lived units like AWS Step Functions or GCP Cloud Run die with the job; "instances" (VMs) are more permanent.
- **[[FLOPs|FLOPS]] is a contentious compute-speed metric.** Vendors disagree on what counts as one operation (operation fusion ambiguity), and theoretical FLOPS rarely match achieved FLOPS. The achieved/theoretical ratio is [[GPUUtilization|utilization]]; 50% might be considered good or bad depending on workload and hardware. I/O bandwidth bounds how fast data can be loaded into memory between operations, which gates utilization. [[MLPerf|MLPerf]] (training ResNet-50 on ImageNet, BERT-large on SQuAD) is the canonical benchmark.
- **Cloud's economics invert past a growth threshold — driving "[[CloudRepatriation|cloud repatriation]]."** Synergy Research: 2020 cloud spend grew 35% to ~$130B while data-center spend dropped 6% to <$90B. But [[A16Z|a16z]] estimates cloud accounts for ~50% of cost-of-revenue for public software companies, costing ~$100B of market value across 50 firms. [[Dropbox|Dropbox]] saved $75M in two years pre-IPO by moving workloads off public cloud. The dominant pattern is hybrid: keep most workloads on cloud, slowly invest in private data centers.
- **[[MultiCloud|Multicloud]] is rarely chosen on purpose.** A 2019 Gartner study found 81% of orgs use ≥2 public clouds, but Huyen quotes reviewer Josh Wills: "Nobody in their right mind intends to use multicloud." Multicloud usually arises from independent business units, acquisitions, or strategic investments by Microsoft/Google. A common ML pattern is training on GCP/Azure and serving on AWS.
- **The dev environment is the single highest-leverage place to invest.** Quoting Ville Tuulos: "If you have time to set up only one piece of infrastructure well, make it the development environment for data scientists." Huyen reports that outside a handful of tech companies, the dev environment is "severely underrated and underinvested in."
- **ML versioning sprawls across tools.** Code → Git, data → [[DVC]], experiments → [[WeightsAndBiases|Weights & Biases]] / [[CometML|Comet.ml]], deployment artifacts → [[MLflow]]; Huyen's startup [[ClaypotAI|Claypot AI]] is building a unified successor. Versioning is more important for ML than for SWE because more things change (code, parameters, data) and reproducing prior runs is mandatory.
- **[[JupyterNotebook|Notebooks]] are stateful — a double-edged sword.** Statefulness lets you resume from a failed step without reloading data, which is huge for large datasets, but it also lets you run cells out of order, making reproducibility hard ("Chris Albon joke"). [[Netflix|Netflix]]'s 2018 "Beyond Interactive" post catalogs notebook-amplifying tools: [[Papermill|Papermill]] (parameterized notebooks), [[Commuter|Commuter]] (notebook hub), [[nbdev|nbdev]] (tests + docs alongside code).
- **Standardize the dev environment, then move it to the cloud.** Huyen's startup hit three escalating standardization failures (unpinned package versions, mismatched [[Python|Python]] minor versions, then an M1-MacBook Docker incompatibility) before moving to cloud dev environments — they chose [[GitHubCodespaces|GitHub Codespaces]]. Cloud dev environments reduce IT burden, enable remote work, improve security (revocation on lost laptops), and — crucially — narrow the gap between dev and prod when prod is also in the cloud.
- **Containers solve the "re-create environment on any new instance" problem.** A [[Dockerfile|Dockerfile]] is the recipe → a [[DockerImage|image]] is the mold → a [[DockerContainer|container]] is a running instance. Multi-container designs are common when stages have different resource profiles (featurizing on CPU, training on GPU) or conflicting dependencies (NumPy 0.8 vs 1.0). [[DockerCompose|Docker Compose]] orchestrates containers on a single host; [[Kubernetes|Kubernetes (K8s)]] orchestrates them across hosts and was "one of the fastest-growing technologies in the 2010s."
- **Resource management's problem statement has inverted from utilization to cost-effectiveness.** Pre-cloud, finite resources forced complex utilization-maximization logic. In the elastic cloud, the question is whether the marginal cost of more resources is justified by saved engineering time — and since engineer time is more valuable than compute, the bias is to throw compute at problems.
- **ML workflows differ from generic jobs along two axes: repetitiveness and dependencies.** Repetitiveness invites [[Cron|cron]]-style scheduling (run weekly retraining, generate predictions every 4 hours). Complex dependencies — including conditional ones like "deploy A if A beats B, else deploy B" — are best expressed as [[DirectedAcyclicGraph|DAGs]]. Almost every workflow tool requires you to express the workflow as a DAG.
- **Schedulers ≠ orchestrators, but they overlap.** Schedulers (Slurm, Borg) answer *when* a job runs and *what resources it needs*, handling DAGs, priority queues, and per-user quotas. Orchestrators (K8s, HashiCorp Nomad) answer *where* to get those resources — instances, clusters, replication. Borg estimates real resource use and reclaims over-allocations. Schedulers usually run on top of orchestrators (Spark scheduler on K8s; AWS Batch on EKS).
- **The five workflow-management tools each fix the previous generation's deficiencies.** [[Airflow]] (2014, Airbnb): "configuration as code" in Python, huge operator library — but monolithic (one container for the whole DAG), non-parameterized, static DAGs. [[Prefect]]: parameterized + dynamic DAGs in Python, but containerized steps remain second-class. [[ArgoWorkflows|Argo]]: every step in its own container, but YAML-defined and K8s-only (needs minikube locally). [[Kubeflow]] + [[Metaflow]]: bridge dev and prod environments; Metaflow's `@conda` and `@batch` Python decorators (e.g. `@batch(gpu=2, memory=16000)`) let one workflow run partly locally and partly on AWS Batch with no Dockerfile/YAML boilerplate.
- **An ML platform is a recently-emerged shared-tooling team — usually born from a recommender-system group.** Huyen recounts a major streaming company's [[MLPlatform|ML platform]] team origin story: tools built first for recommender systems (feature management, model management, monitoring) became the shared substrate. She focuses on three components — model deployment, model store, feature store — and explicitly skips monitoring (covered in Ch 8).
- **Model deployment is the most mature ML-platform component; model store is the least.** All major clouds offer deployment ([[AmazonSageMaker|SageMaker]], [[GoogleCloudVertexAI|Vertex AI]], [[AzureML|Azure ML]], Alibaba Machine Learning Studio); startups offer [[MLflow]] Models, [[Seldon]], Cortex, [[RayServe|Ray Serve]]. But model stores are "due for a makeover" — three of the top-six [[MLflow]] Stack Overflow questions are about storing/accessing artifacts. Stitch Fix and others build their own.
- **A model store should hold eight artifact classes — almost nobody stores all of them.** (1) model definition, (2) model parameters, (3) featurize/predict functions, (4) dependencies (usually a container), (5) data (pointer or DVC commit), (6) model generation code (notebook commit, hyperparam ranges, splits), (7) experiment artifacts (loss curves, test metrics), (8) tags (owner, task). Companies typically scatter these across S3, ECS, Snowflake, W&B, and Lambda — with locations tracked in a fragile README.
- **A [[FeatureStore|feature store]] addresses three orthogonal problems.** (1) **Feature management** — share/discover features across teams, manage access (Uber had ~10K features across teams by 2017); tools: [[Amundsen]] (Lyft), [[DataHub]] (LinkedIn). (2) **Feature computation** — compute expensive features once and store the results; in this capacity a feature store acts like a data warehouse. (3) **Feature consistency** — unify batch (training) and streaming (inference) feature logic to eliminate [[TrainingServingSkew|training-serving skew]] when prod is written in Java/C while dev is in Python.
- **Feature stores are still immature.** As of January 2022, [[Feast]] is the most popular open-source feature store but is weak at streaming features; [[Tecton]] is fully managed but requires deep integration that slows adoption. In a 95-company survey, only ~40% used a feature store, and half of those built their own.
- **Build versus buy is dominated by three factors.** (1) Company stage — buy early, build as scale makes vendor costs exorbitant. (2) Competitive focus — Stefan Krawczyk (Stitch Fix): "If it's something we want to be really good at, we'll manage that in-house. If not, we'll use a vendor." Tech companies bias toward build; retail/banking/manufacturing bias toward buy. (3) Tool maturity — early adopters build because nothing's mature; later vendors struggle to sell to those same early adopters because of "integration hell."

## Key Quotes
> "While getting started with the cloud is easy, moving away from the cloud is hard. Cloud repatriation requires nontrivial up-front investment in both commodities and engineering effort." — Huyen, on why hybrid (mostly-cloud with a growing data-center footprint) has become the dominant production pattern.

> "Nobody in their right mind intends to use multicloud." — Josh Wills (early reviewer), quoted in the chapter; multicloud usually accrues through independent business decisions, acquisitions, or investor pressure rather than deliberate architecture.

> "If you have time to set up only one piece of infrastructure well, make it the development environment for data scientists." — Ville Tuulos (*Effective Data Science Infrastructure*, Manning 2022), Huyen's argument for why dev-env investment dominates other infrastructure spend in ROI.

> "An ML workload typically requires between 4 GB and 8 GB of memory; 16 GB of memory is enough to handle most ML workloads." — Huyen's rule of thumb for compute-unit sizing at reasonable scale (Footnote 10).

> "If it's something we want to be really good at, we'll manage that in-house. If not, we'll use a vendor." — Stefan Krawczyk, manager of Stitch Fix's ML platform team, articulating the competitive-focus heuristic for build-versus-buy.

> "One of the most important jobs of a CTO is vendor/product selection and the importance of this keeps going up rapidly every year since the infrastructure space grows so fast." — Erik Bernhardsson (ex-CTO, Better.com), quoted on the build-versus-buy decision.

> "Kubeflow helps you abstract away other tools' boilerplate by making you write Kubeflow boilerplate." — Huyen's critique that Kubeflow demands per-component Dockerfiles + YAML in addition to Python workflow code, in contrast to Metaflow's `@conda`/`@batch` decorators.

> "Bringing ML models to production is an infrastructural problem." — the chapter's thesis from the closing summary.

## Connections
- [[ChipHuyen]] — author; this is Chapter 10 of her 2022 [[OReilly|O'Reilly]] book *Designing Machine Learning Systems*, building on Chs 7–9 (deployment, monitoring, continual learning).
- [[OReilly]] — publisher.
- [[dmls-ch01-overview]] — opening chapter; established that ML systems include infrastructure as a first-class component, a thesis Ch 10 operationalizes.
- [[ai-engineering-chip-huyen]] — Huyen's 2024 successor book; same infrastructure-aware systems lens applied to foundation-model applications.
- [[MLOps]] — chapter's domain; Ch 10 is the most concrete tooling survey in the book.
- [[MLPlatform]] — central concept of the chapter's third major section; defined as the shared tooling team/layer.
- [[ModelDeployment]] — first of three ML-platform components surveyed.
- [[ModelStore]] — second ML-platform component; least mature, eight-artifact taxonomy.
- [[FeatureStore]] — third ML-platform component; three problems (management, computation, consistency).
- [[TrainingServingSkew]] — the bug class that feature consistency in a feature store is designed to prevent.
- [[FeatureEngineering]] — what feature stores manage and compute.
- [[ModelRegistry]] — closely related to (and sometimes synonymous with) model store.
- [[ModelServing]] — operationalization of model deployment; deployment service exposes models as endpoints.
- [[OnlineInference]] — one of two prediction modes a deployment service must support.
- [[BatchInference]] — the other prediction mode; Huyen notes it is "usually trickier" to set up than online.
- [[ABTesting]] / [[ShadowDeployment]] / [[CanaryDeployment]] — production-test techniques (Ch 9) that a good deployment service should make easy.
- [[ModelBuildVsBuy]] — chapter's closing section; this page captures the three deciding factors (stage, focus, maturity).
- [[ExperimentTracking]] — the model-development sub-area whose artifacts (loss curves, metrics) are class #7 of the model-store taxonomy.
- [[Reproducibility]] — versioning + experiment tracking + dependency capture are the reproducibility substrate Huyen argues for.
- [[Versioning]] — code/data/experiment/artifact versioning all need separate tools today.
- [[DataVersioning]] — DVC (one of Huyen's named versioning tools); data is class #5 of the model-store taxonomy.
- [[Reproducibility]] / [[ReproducibilityInML]] — notebook out-of-order execution is the chapter's signature reproducibility hazard.
- [[ComputeLayer]] — abstraction Huyen uses; the engine that executes jobs.
- [[ComputeUnit]] — characterized by memory + operation speed; varies by framework (thread/core, job, pod).
- [[FLOPs]] — contested compute-speed metric; Huyen warns achieved ≠ theoretical.
- [[GPUUtilization]] — the achieved/theoretical FLOPS ratio.
- [[MLPerf]] — Huyen's recommended hardware benchmark (ResNet-50 on ImageNet, BERT-large on SQuAD).
- [[CloudComputing]] — the substrate the chapter assumes by default.
- [[CloudRepatriation]] — Huyen's term for moving back to private data centers; Dropbox's $75M case study.
- [[MultiCloud]] — the 81% reality, but rarely chosen on purpose.
- [[SpotInstance]] — cost-saving instance type Huyen flags as "not always easy to use."
- [[DataCenter]] — on-prem alternative to cloud compute; chapter's repatriation discussion centers on these.
- [[DataWarehouse]] — feature store with computed features behaves like one.
- [[DataLake]] — referenced via the Uber/Zillow scale discussion.
- [[DirectedAcyclicGraph]] — the canonical workflow representation; every workflow manager surveyed uses DAGs.
- [[Cron]] — the scheduling baseline Huyen compares schedulers against.
- [[Scheduler]] — disambiguation: this chapter discusses the *workflow scheduler* (Slurm, Borg) sense, distinct from the OS-kernel scheduler on the existing wiki page.
- [[Orchestrator]] — chapter's distinction between schedulers and orchestrators; K8s is the canonical orchestrator.
- [[Airflow]] — 2014 Airbnb scheduler; "configuration as code" champion; monolithic, non-parameterized, static-DAG limitations.
- [[Prefect]] — next-gen workflow tool fixing Airflow's parameterization and dynamism.
- [[ArgoWorkflows]] — container-per-step workflow tool; YAML-defined, K8s-only.
- [[Kubeflow]] — K8s-native ML workflow tool; built on Argo; criticized for Dockerfile + YAML boilerplate.
- [[Metaflow]] — Netflix's workflow tool; Python decorators (`@conda`, `@batch`) bridge dev and prod environments.
- [[Dagster]] — listed alongside the above orchestrators in the wiki's existing orchestrator catalog.
- [[Kubernetes]] — the dominant container orchestrator; Huyen links to her "Why Data Scientists Shouldn't Need to Know Kubernetes" post.
- [[Docker]] — container engine; chapter explains image vs container, build-from-scratch vs base-image.
- [[DockerImage]] — the artifact a Dockerfile builds.
- [[DockerContainer]] — a running instance of a Docker image.
- [[Dockerfile]] — the recipe; chapter includes a PyTorch+apex+transformers example.
- [[DockerCompose]] — single-host orchestrator.
- [[DockerHub]] — public container registry.
- [[AmazonECR]] — AWS's container registry.
- [[Conda]] — virtual-environment tool Huyen's startup used.
- [[VirtualEnvironment]] — the Python-dependency isolation primitive.
- [[Python]] — primary workflow-definition language for Airflow/Prefect/Metaflow/Kubeflow.
- [[VSCode]] — Huyen's recommended local IDE for cloud dev environments.
- [[JupyterNotebook|Jupyter]] — primary data-science IDE; stateful semantics analyzed in depth.
- [[GoogleColab]] — hosted notebook environment; offers free GPUs.
- [[GitHubCodespaces]] — Huyen's startup's chosen cloud dev environment; auto-shuts down after 30 min of inactivity.
- [[CICD]] — referenced as part of the dev environment; chapter declines to cover in depth.
- [[GitHubActions]] — example CI/CD tool.
- [[DVC]] — data-versioning tool in Huyen's recommended ML-workflow versioning stack.
- [[WeightsAndBiases]] — experiment-tracking tool.
- [[CometML]] — alternative experiment-tracking tool.
- [[MLflow]] — most popular non-cloud-bundled model store; also offers MLflow Models for deployment.
- [[Seldon]] — model deployment startup.
- [[RayServe]] — Ray-based model serving framework.
- [[AmazonSageMaker]] — AWS's ML platform; SageMaker Studio comes with hosted JupyterLab.
- [[AmazonEC2]] — canonical IaaS compute; X1e is the largest instance (128 vCPUs, ~4 TB RAM).
- [[AmazonS3]] — canonical object storage; common model-binary store.
- [[AmazonECS]] — Elastic Container Service; common container dependency host.
- [[AmazonECR]] — Elastic Container Registry; companion to ECS.
- [[AmazonEKS]] — managed K8s on AWS; common orchestrator-as-a-service.
- [[AmazonRedshift]] — referenced as one side of a multi-warehouse data scatter example.
- [[GoogleCloudVertexAI]] — GCP's deployment platform.
- [[GoogleBigQuery]] — referenced opposite Redshift in the same scatter example.
- [[GoogleCloudStorage]] — GCP storage layer.
- [[AzureML]] — Microsoft's deployment platform.
- [[AlibabaDAMOAcademy|Alibaba]] — referenced via Alibaba's Machine Learning Studio.
- [[Databricks]] — referenced for batch prediction and managed-cluster build-vs-buy example.
- [[Snowflake]] — managed data warehouse example.
- [[NVIDIA]] — provider of GPU-optimized base Docker images (TensorFlow on GPUs).
- [[TensorFlow]] — runtime example in the Dockerfile NVIDIA-image pattern.
- [[PyTorch]] — base image in the chapter's Dockerfile example.
- [[HuggingFace]] — `transformers` repo cloned in the chapter's Dockerfile example.
- [[ApacheSpark|Spark]] — uses "job" as its compute unit; common scheduler on K8s.
- [[Ray]] — alongside Spark as a non-thread compute abstraction.
- [[Tecton]] — fully managed feature store; weak adoption due to deep-integration requirement.
- [[Feast]] — most popular open-source feature store; weak on streaming features.
- [[Amundsen]] — Lyft's feature/metadata catalog.
- [[DataHub]] — LinkedIn's feature/metadata catalog.
- [[Papermill]] — Netflix's parameterized-notebook tool.
- [[Commuter]] — Netflix's notebook hub.
- [[nbdev]] — fast.ai's docs+tests-in-notebook library.
- [[Borg]] — Google's cluster manager; reclaims unused resources from over-allocations.
- [[Slurm]] — example scheduler with `#SBATCH` job spec syntax.
- [[HashiCorpNomad]] — orchestrator with built-in scheduling capacity.
- [[ClaypotAI]] — Huyen's startup (at time of writing) building unified ML workflow versioning.
- [[StitchFix]] — case study for both feature stores and model stores; builds its own.
- [[StefanKrawczyk]] — Stitch Fix ML platform manager; quoted on build-vs-buy and on the eight-artifact model-store taxonomy (CS 329S slide).
- [[VilleTuulos]] — author of *Effective Data Science Infrastructure* (Manning 2022); Metaflow creator at Netflix; quoted on dev-environment investment priority.
- [[ErikBernhardsson]] — ex-CTO of Better.com; quoted on vendor selection.
- [[JoshWills]] — early reviewer quoted on multicloud.
- [[Netflix]] — origin of Metaflow and the "Beyond Interactive" notebook-tooling post.
- [[Uber]] — 2017 had ~10K features across teams (Michelangelo platform reference); +tens of TB/day to data lake in 2018.
- [[Airbnb]] — origin of Airflow (2014).
- [[Lyft]] — origin of Amundsen.
- [[LinkedIn]] — origin of DataHub.
- [[Dropbox]] — flagship cloud-repatriation case study ($75M saved over 2 years pre-IPO).
- [[Zillow]] — reasonable-scale data-volume reference (2 TB/day uncompressed in 2018).
- [[Tesla]] / [[Waymo]] — self-driving examples of specialized in-house infrastructure.
- [[A16Z]] — venture firm whose "The Cost of Cloud, a Trillion Dollar Paradox" estimate (50% of cost-of-revenue, $100B lost market value) frames the repatriation argument.
- [[Gartner]] — source of the 81% multicloud statistic (2019).
- [[CS329S]] — Huyen's Stanford ML systems design course; Stefan Krawczyk slide is the source of the model-store artifact figure.
- [[MichelangeloPlatform|Michelangelo]] — Uber's internal ML platform; cited via the 10K-features figure.

## Contradictions
- None observed against existing wiki content. The chapter's definition of an [[Orchestrator]] (cluster-level resource provisioning; K8s as canonical) is consistent with — and complementary to — the existing [[Orchestrator]] page's MLOps-pipeline framing, and aligns with [[AIPipelineOrchestration]]'s distinction between batch-DAG orchestrators and request-shaped inference orchestrators.
- The chapter's [[Scheduler]] usage (workflow-level: Slurm, Borg, job queues, DAGs) overlaps with but does not contradict the existing [[Scheduler]] page's OS-kernel-process-scheduler scope; the two are distinct senses of the same word and should be cross-referenced rather than reconciled.
