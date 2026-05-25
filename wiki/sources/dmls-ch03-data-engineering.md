---
title: "Designing ML Systems — Ch 3: Data Engineering Fundamentals"
type: source
tags: [book, designing-ml-systems, data-engineering, oreilly, dmls, chip-huyen, etl, elt, oltp, olap, streaming, batch, data-models, data-formats, dataflow]
date: 2022-05-17
sources: []
source_file: raw/books/designing-ml-systems/dmls-ch03-data-engineering.txt
last_updated: 2026-05-23
---

## Summary

Chapter 3 of [[ChipHuyen|Chip Huyen]]'s *Designing Machine Learning Systems* ([[OReilly]], 2022) is a survey of the data-engineering substrate that every production ML system rests on. It walks five concentric layers: where data comes from (user input, system-generated logs, internal databases, third-party data), how to serialize it ([[JSON]], [[CSVFormat|CSV]], [[Parquet]], [[Avro]], [[Protobuf]], [[Pickle]] — with the [[RowMajorOrder|row-major]] vs [[ColumnMajorOrder|column-major]] and text-vs-binary trade-offs), how to model it ([[RelationalModel|relational]], [[DocumentModel|document]], [[GraphModel|graph]]; structured vs unstructured), how to store and process it ([[OLTP]] vs [[OLAP]]; [[ACID]] vs [[BASE]]; [[ETL]] vs [[ELT]]; the decoupling of storage from compute), and how to move it between processes ([[Database|database-mediated]], request-driven [[REST]]/[[RPC]] services, and event-driven [[RealTimeTransport|real-time transports]] like [[ApacheKafka|Kafka]] and [[Kinesis|Kinesis]]). It closes with the [[BatchProcessing]] vs [[StreamProcessing]] dichotomy and how batch and streaming features ("static" and "dynamic" features) flow into ML models. The chapter is heavily inspired by Martin Kleppmann's *Designing Data-Intensive Applications*, which Huyen explicitly recommends as a deeper companion text.

## Key Claims

- ML systems consume four major **data-source archetypes** — user input (untrusted, requires heavy validation and low-latency processing), system-generated logs and model predictions (less malformed but high-volume), internal databases (CRM, inventory, user tables — directly consumable by models), and third-party data (first-party = your own; second-party = a partner's; third-party = aggregated from the public; usage of third-party data has shrunk since Apple's 2021 IDFA opt-in change).
- **Choice of [[DataSerialization|serialization format]]** is a function of human-readability, text-vs-binary size, and access pattern: [[JSON]] is ubiquitous and schema-flexible but bulky; [[CSVFormat|CSV]] is [[RowMajorOrder|row-major]] and write-friendly but poor at non-text values; [[Parquet]] is [[ColumnMajorOrder|column-major]], binary, and dominant in [[Hadoop]]/[[AmazonRedshift|Redshift]] analytics — AWS reports Parquet is up to 2× faster to unload and uses up to 6× less S3 storage than text formats. Converting a 14 MB CSV (17,654 rows × 10 cols) to Parquet shrank it to 6 MB in Huyen's example.
- **Row-major formats are better for write-heavy or example-wise workloads; column-major formats are better for column-wise reads** (selecting 4 of 1,000 features). This subtlety routinely trips up users who treat [[pandas]] DataFrames like row-major [[NumPy]] [[NDArray|ndarrays]] — iterating a DataFrame by row took 2.41 s vs 0.07 s by column in Huyen's benchmark (and dropped back to row-fast after `.values`/`.to_numpy()` conversion).
- The **[[RelationalModel|relational model]]** (Edgar F. Codd, 1970) organizes data into relations of unordered tuples, encourages [[DataNormalization|normalization]] to reduce redundancy and improve integrity, but pays a join-cost penalty as data spreads across tables.
- **[[SQL]] is a declarative query language**: callers specify the desired result, not the steps; query optimizers (themselves a research target — ML-augmented optimizers like Neo exist) plan the actual execution. With minor extensions SQL is Turing-complete.
- **[[DocumentModel|Document databases]] are not truly schemaless** — they shift the burden of structure assumption from the writer to the reader. Documents have better locality than normalized relations (a whole book in one JSON), but cross-document joins are harder than relational joins.
- **[[GraphModel|Graph databases]] make relationship-traversal queries first-class** (e.g., "everyone born in the USA, allowing arbitrary hops through within/born_in edges") that are awkward in both SQL and document models — picking the right data model can make some problems trivial that others find intractable.
- **Structured vs unstructured is a fluid boundary**: structured data forces the writer to commit to a schema and bears schema-migration pain (a colleague's bug: nulls replaced with 0 → ML model treated transactions as made by 0-year-olds); unstructured data shifts the burden to the reader and is stored in [[DataLake|data lakes]] rather than [[DataWarehouse|data warehouses]]. Hybrid [[Lakehouse|lakehouses]] from [[Databricks]] and [[Snowflake]] combine the two.
- **Transactional ([[OLTP]]) databases optimize for low latency, high availability, and ACID guarantees** (atomicity, consistency, isolation, durability); analytical ([[OLAP]]) systems optimize for aggregation across many rows. The terms are becoming outdated: storage and compute are decoupling ([[GoogleBigQuery|BigQuery]], [[Snowflake]], IBM, Teradata), and convergent systems handle both workloads (CockroachDB on the OLTP side, Apache Iceberg / DuckDB on the OLAP side).
- **[[ACID]] is not mandatory** for transactional databases; the looser [[BASE]] alternative (Basically Available, Soft state, Eventual consistency) is common in NoSQL.
- **[[ETL]] vs [[ELT]]**: classical ETL transforms-then-loads into a warehouse and is still the dominant data-layer pattern; ELT loads raw data into a [[DataLake|lake]] and transforms on demand, trading fast arrival for slow scans on raw data. Hybrid lakehouse vendors are blurring the line.
- **Three modes of [[Dataflow]] between processes**: (1) through a shared database — simple but requires both processes to access it and is too slow for strict latency; (2) through services — request-driven [[REST]] or [[RPC]] APIs, the basis of [[MicroservicesArchitecture|microservice architectures]] like Lyft's hundreds of services; (3) through [[RealTimeTransport|real-time transports]] like [[ApacheKafka|Kafka]] and [[Kinesis]] — an event-driven broker that decouples producers from consumers.
- **Request-driven architecture suits logic-heavy systems; event-driven architecture suits data-heavy systems.** With ≥3 services that all need each other's outputs, pairwise request-driven traffic becomes a synchronous, fault-coupled mesh; a broker (pubsub or message queue) collapses N² coupling to N.
- The **two main real-time transport models** are pubsub (any service publishes to a topic, retention policy controls staleness; examples: Kafka, Kinesis) and message queue (events have intended consumers, examples: Apache RocketMQ, RabbitMQ).
- **[[BatchProcessing]] vs [[StreamProcessing]]**: data in storage = historical, processed periodically (MapReduce, Spark) → produces **static features** (e.g., a driver's rating); data in real-time transports = streaming, processed continuously ([[ApacheFlink|Flink]], KSQL, Spark Streaming) → produces **dynamic features** (e.g., available drivers right now). Production ML systems typically need both kinds joined together — fraud detection and credit-scoring stream-feature counts often run in the hundreds or thousands.
- **Stream processing is harder than batch** because data is unbounded and arrives at variable rates; but stateful streaming can avoid the redundancy of recomputing the last 30 days every day for a 30-day-window batch job. Apache Flink's maintainers argue that batch is a special case of streaming, motivating unified pipelines.

## Key Quotes

> "There are three main modes of dataflow: data passing through databases, data passing through services using requests such as the requests provided by REST and RPC APIs, [and] data passing through a real-time transport like Apache Kafka and Amazon Kinesis." — Modes of Dataflow (Huyen's tri-partite taxonomy)

> "Request-driven architecture works well for systems that rely more on logic than on data. Event-driven architecture works better for systems that are data-heavy." — Real-Time Transport section, on choosing between REST/RPC and pubsub

> "The Parquet format is up to 2x faster to unload and consumes up to 6x less storage in Amazon S3, compared to text formats." — Huyen quoting AWS in the Text-Versus-Binary section, arguing for [[Parquet]] adoption

> "Because the document model doesn't enforce a schema, it's often referred to as schemaless. This is misleading… Document databases just shift the responsibility of assuming structures from the application that writes the data to the application that reads the data." — NoSQL/Document Model, dismantling the "schemaless" myth

> "Stream processing is more difficult because the data amount is unbounded and the data comes in at variable rates and speeds. It's easier to make a stream processor do batch processing than to make a batch processor do stream processing." — Batch vs Stream, echoing Flink's "batch is a special case of streaming" position (Kostas Tzoumas, Ververica 2015)

> "In the imperative paradigm, you specify the steps needed for an action and the computer executes these steps to return the outputs. In the declarative paradigm, you specify the outputs you want, and the computer figures out the steps needed to get you the queried outputs." — on SQL as a declarative language and the inspiration for declarative ML (Ludwig, H2O AutoML)

> "While declarative ML can be useful in many cases, it leaves unanswered the biggest challenges with ML in production… model development is often the easier part. The hard part lies in feature engineering, data processing, model evaluation, data shift detection, continual learning, and so on." — Huyen's critique of declarative ML systems

## Connections

- [[ChipHuyen]] — author; this chapter is the data-engineering foundation under all subsequent DMLS chapters.
- [[OReilly]] — publisher of *Designing Machine Learning Systems* (2022) and the predecessor to [[ai-engineering-chip-huyen|*AI Engineering*]] (2024).
- [[ai-engineering-chip-huyen]] — the spiritual successor book; both share Huyen's voice and many design-trade-off framings.
- [[DataEngineering]] — umbrella concept the chapter inhabits.
- [[madewithml-mlops-data-engineering]] — a parallel modern-data-stack walkthrough that operationalizes ELT into BigQuery + dbt; complements this chapter's conceptual treatment.
- [[JSON]] — ubiquitous text-based serialization format, discussed for its schema-rigidity and verbosity.
- [[CSVFormat]] — row-major text format, the "everywhere" comparator.
- [[Parquet]] — column-major binary format championed by AWS/Hadoop for analytics.
- [[Avro]] — binary-primary format common in Hadoop (new concept to mint).
- [[Protobuf]] — Google/TensorFlow TFRecord format; already in wiki.
- [[Pickle]] — Python/PyTorch binary serialization (new concept to mint).
- [[RowMajorOrder]] — existing row-major page (currently C-language-centric); this chapter adds the data-format / pandas / CSV usage.
- [[ColumnMajorOrder]] — new concept; Parquet, pandas DataFrame, dbt warehouse columnar internals.
- [[DataSerialization]] — new umbrella concept covering JSON/CSV/Parquet/Avro/Protobuf/Pickle.
- [[RelationalModel]] — new concept; Codd 1970, tuples-in-relations, normalization.
- [[DocumentModel]] — new concept; JSON/BSON-encoded documents, locality, schema-on-read.
- [[GraphModel]] — new concept; nodes + edges, relationship-first queries.
- [[NoSQL]] — new umbrella concept covering document + graph; "Not Only SQL" reinterpretation.
- [[SQL]] — new concept (existing pages are SQL-benchmark-specific); declarative query language for relational databases.
- [[DeclarativeProgramming]] — new concept; the paradigm SQL exemplifies.
- [[ImperativeProgramming]] — existing concept; SQL contrasted with Python.
- [[DeclarativeML]] — new concept; Ludwig (Uber) and H2O AutoML as exemplars.
- [[DataNormalization]] — new concept; 1NF/2NF/3NF, splitting Book/Publisher tables.
- [[QueryOptimizer]] — new concept; the engine that turns declarative SQL into execution plans; ML-augmented optimizers like Neo (Marcus et al. 2019).
- [[StructuredData]] — new concept; schema-on-write.
- [[UnstructuredData]] — new concept; schema-on-read.
- [[DataLake]] — existing concept; chapter's canonical home for unstructured/raw data.
- [[DataWarehouse]] — existing concept; chapter's canonical home for structured/processed data.
- [[Lakehouse]] — new concept; Databricks/Snowflake hybrid.
- [[OLTP]] — existing concept; row-major, low-latency, ACID-friendly.
- [[OLAP]] — existing concept; column-major aggregation.
- [[ACID]] — new concept; atomicity, consistency, isolation, durability — the transactional contract.
- [[BASE]] — new concept; Basically Available, Soft state, Eventual consistency — the looser NoSQL contract.
- [[ETL]] — existing concept; transform-then-load classical pipeline.
- [[ELT]] — existing concept; load-then-transform modern pipeline.
- [[StorageComputeSeparation]] — new concept; the decoupling pattern adopted by BigQuery, Snowflake, IBM, Teradata.
- [[Dataflow]] — new umbrella concept (distinct from existing [[DataflowVariable]]); the three modes Huyen enumerates.
- [[MicroservicesArchitecture]] — existing concept; expanded here with the Lyft three-services pricing example.
- [[REST]] — existing concept; HTTP-style request-driven inter-service communication.
- [[RPC]] — new concept; remote procedure call style, faster intra-org alternative to REST.
- [[RealTimeTransport]] — new concept; in-memory event-passing substrate.
- [[EventDrivenArchitecture]] — new concept; data-heavy alternative to request-driven.
- [[PubSub]] — new concept; topic-based publish-subscribe model.
- [[MessageQueue]] — new concept; intended-consumer message-passing model.
- [[ApacheKafka]] — existing entity; canonical pubsub real-time transport.
- [[Kinesis]] — existing entity; AWS pubsub real-time transport.
- [[RabbitMQ]] — new entity; canonical message-queue platform.
- [[ApacheRocketMQ]] — new entity; alternative message-queue platform.
- [[BatchProcessing]] — new concept; periodic compute on historical data.
- [[StreamProcessing]] — new concept; continuous compute on streaming data; Flink/KSQL/Spark Streaming.
- [[StaticFeature]] — new concept; batch-computed feature (driver rating).
- [[DynamicFeature]] — new concept; stream-computed feature (drivers available now).
- [[MapReduce]] — existing concept; classical batch-processing distributed framework.
- [[ApacheSpark]] — existing entity; modern batch + micro-batch processing engine.
- [[ApacheFlink]] — existing entity; the stream-processing champion ("batch is a special case of streaming").
- [[KSQL]] — new entity; SQL-on-Kafka stream-processing engine.
- [[SparkStreaming]] — new entity; Spark's streaming module.
- [[Hadoop]] — existing entity; the Parquet/Avro ecosystem origin.
- [[AmazonRedshift]] — existing entity; Parquet-friendly cloud data warehouse.
- [[GoogleBigQuery]] — existing entity; storage-compute decoupling exemplar.
- [[Snowflake]] — existing entity; lakehouse / storage-compute decoupling vendor.
- [[Databricks]] — existing entity; lakehouse vendor.
- [[PostgreSQL]] — existing entity; relational DB that also supports document features.
- [[MySQL]] — new entity; relational DB that also supports document features.
- [[CockroachDB]] — new entity; transactional DB that also handles analytical queries.
- [[ApacheIceberg]] — new entity; analytical table format that also handles transactional queries.
- [[DuckDB]] — new entity; in-process OLAP database that handles transactional queries too.
- [[AmazonS3]] — existing entity; canonical cheap object store; Standard vs Glacier tier example.
- [[MartinKleppmann]] — new entity; author of *Designing Data-Intensive Applications* (O'Reilly 2017), the foundational reference Huyen recommends and quotes throughout.
- [[DesigningDataIntensiveApplications]] — new concept/source-stub; Kleppmann's book.
- [[EdgarFCodd]] — new entity; inventor of the relational model (1970).
- [[Ludwig]] — new entity; Uber's declarative ML framework.
- [[H2OAutoML]] — new entity; H2O's declarative-ML system.
- [[Uber]] — new entity; creator of Ludwig.
- [[Lyft]] — new entity; the ride-sharing microservice example.
- [[Apple]] — existing entity; expanded here with IDFA opt-in (2021) and the impact on third-party data.
- [[IDFA]] — new concept; Apple's Identifier for Advertisers.
- [[AAID]] — new concept; Android Advertising ID.
- [[CAID]] — new concept; China Advertising Association's device-fingerprinting workaround.
- [[TikTok]] — new entity; cited as user of CAID workaround.
- [[Tencent]] — new entity; cited as user of CAID workaround.
- [[Datadog]] — existing entity; log-processing service example.
- [[Logstash]] — new entity; log-processing service example.
- [[NumPy]] — existing concept; row-major default ndarray.
- [[pandas]] — existing concept; column-major DataFrame, the row-iteration pitfall.
- [[NDArray]] — existing concept; the row-major comparator.
- [[FeatureEngineering]] — existing concept; downstream consumer of batch + stream features.
- [[FeatureStore]] — existing concept; the production home for static + dynamic features.
- [[FraudDetection]] — new concept; canonical use case for stream features at the hundreds-of-features scale.
- [[CreditScoring]] — new concept; canonical use case for stream features.
- [[RecommenderSystems]] — existing concept; cited as a third-party-data consumer.
- [[gRPC]] — existing concept; the RPC framework Huyen alludes to in the REST vs RPC discussion.

## Contradictions

- **None of substance.** The chapter sits cleanly upstream of the rest of the wiki's data-engineering corpus ([[madewithml-mlops-data-engineering]], [[leh-ch10-inference-pipeline-deployment]], [[ai-engineering-chip-huyen]]). Minor framing differences:
  - [[madewithml-mlops-data-engineering]] adopts a sharp "ELT > ETL" position; this chapter is more balanced, noting that ELT loses efficiency as data lakes grow ("inefficient to search through a massive amount of raw data") and that hybrid lakehouses are the convergent direction.
  - [[ai-engineering-chip-huyen]] (Huyen's 2024 follow-up) generalizes the relational/document/graph + batch/stream lattice to *context construction for foundation models* rather than feature pipelines for classical ML; the substrate is identical.
  - The chapter's footnote that storage cost "is rarely a problem" in 2022 is now slightly dated given the surge in multimodal data volumes — but it does not contradict any existing wiki claim.
