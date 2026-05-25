---
title: "LLM Engineer's Handbook — Ch 3: Data Engineering"
type: source
tags: [book, llm-engineering, llm-engineers-handbook, data-engineering]
date: 2024-10-22
source_file: raw/books/llm-engineers-handbook/ch03-data-engineering.md
---

## Summary
Chapter 3 of the LLM Engineer's Handbook walks through designing and implementing the LLM Twin project's data collection pipeline as an end-to-end ETL: it crawls Medium, Substack, GitHub, and LinkedIn for raw text and code authored by a target "user" and loads the standardized documents into a MongoDB NoSQL "data warehouse." The architecture reduces every source to three data categories — `ArticleDocument`, `PostDocument`, and `RepositoryDocument` — so that new sources can be added by writing one more crawler without touching downstream layers. The implementation is orchestrated by ZenML pipelines and steps, uses a `CrawlerDispatcher` (built with the Builder design pattern) to map URL domains to the right crawler subclass, and exposes data through a custom hand-rolled Object-Document Mapper (`NoSQLBaseDocument`) on top of `pymongo` with Pydantic for typed fields. Specific crawlers leverage Selenium + BeautifulSoup (Medium, LinkedIn), `git clone` in a subprocess (GitHub), and LangChain's `AsyncHtmlLoader` / `Html2TextTransformer` (generic article fallback for Substack and blogs). The chapter closes with running the pipeline via `poe` commands, inspecting ZenML artifacts (`user`, `crawled_links`), and querying MongoDB through the ODM (`ArticleDocument.bulk_find(author_id=...)`).

## Key Claims
- The LLM Twin data collection pipeline is structured as a classic ETL: **extract** (crawl Medium / Substack / GitHub / LinkedIn), **transform** (clean and standardize HTML into normalized text), **load** (write to MongoDB).
- MongoDB is used as the "data warehouse" despite being a transactional NoSQL database; the authors justify it for small-scale, unstructured text data and recommend Snowflake or BigQuery for production at millions-of-documents scale.
- All crawled content is reduced to three domain entities — article, repository, post — keeping downstream pipelines source-agnostic and making the system trivially extensible (adding X / Twitter requires only a new crawler that emits a `PostDocument`).
- A `CrawlerDispatcher` class implements the **Builder pattern** (`CrawlerDispatcher.build().register_linkedin().register_medium().register_github()`) and uses regex-normalized URL netlocs to dispatch links to the correct crawler subclass; unknown domains fall back to `CustomArticleCrawler`.
- The crawler hierarchy uses an abstract `BaseCrawler` (ABC + `extract()` method + `model: type[NoSQLBaseDocument]` class attribute) so the dispatcher can call `crawler.extract(link, user=user)` polymorphically without knowing the concrete class.
- `BaseSeleniumCrawler` extends `BaseCrawler` with reusable Selenium-driven browser automation (headless Chrome via `chromedriver_autoinstaller`, configured options for sandbox/GPU/notifications, `scroll_page()` for infinite-feed scraping, `login()` and `set_extra_driver_options()` hooks for subclasses).
- The `GithubCrawler` shells out to `git clone` in a `tempfile.mkdtemp()` directory, walks the file tree, skips files matching ignore patterns (`.git`, `.toml`, `.lock`, `.png`), reads contents (with `errors="ignore"`), and stores a `{file_path: contents}` dict on a `RepositoryDocument`.
- The `CustomArticleCrawler` uses LangChain's `AsyncHtmlLoader` + `Html2TextTransformer` as a fast-but-uncustomizable fallback for Substack and personal blogs — the authors note this is why "many developers avoid using LangChain in production use cases."
- The `MediumCrawler` (inherits `BaseSeleniumCrawler`) drives a headless Chrome session, scrolls the article, then parses with `BeautifulSoup`, selecting elements by class (`h1.pw-post-title`, `h2.pw-subtitle-paragraph`).
- The `LinkedInCrawler` (referenced but not shown) follows the same Selenium pattern: log in, navigate to feed, scroll until a limit, extract posts.
- A custom Object-Document Mapper (ODM) — `NoSQLBaseDocument` — is implemented from scratch on top of `pymongo` and Pydantic, giving every domain document `save()`, `find()`, `bulk_find()`, `bulk_insert()`, `get_or_create()`, plus MongoDB `_id` / UUID conversion via `from_mongo()` / `to_mongo()`.
- The ODM uses Python generics (`T = TypeVar("T", bound="NoSQLBaseDocument")`) and a nested `Settings` class on each subclass to declare the MongoDB collection name; misconfiguration raises `ImproperlyConfigured`.
- ORM vs ODM: ORM (e.g., SQLAlchemy, SQLModel) maps Python classes to SQL tables; ODM (e.g., `mongoengine`) maps them to NoSQL JSON-like documents. The chapter implements a lightweight ODM by hand for pedagogical reasons.
- A `DataCategory` `StrEnum` (`ARTICLES`, `POSTS`, `REPOSITORIES`, `PROMPT`, `QUERIES`, `INSTRUCT_DATASET`, `PREFERENCE_DATASET`, …) centralizes collection names and ties this chapter to later fine-tuning chapters that consume the same enum.
- ZenML orchestrates the pipeline through two steps — `get_or_create_user(user_full_name)` and `crawl_links(user, links)` — exposing `user` and `crawled_links` as inspectable output artifacts with attached metadata (query parameters, per-domain success/total counts).
- Pipelines are configured per-author via YAML files (`configs/digital_data_etl_paul_iusztin.yaml`, `configs/digital_data_etl_maxime_labonne.yaml`) and invoked through `poetry poe run-digital-data-etl-paul` / `…-maxime` / `…` (all authors).
- The ETL pipeline is decoupled from the downstream feature pipeline (covered in Ch. 4) — they communicate only through the MongoDB warehouse and can run on independent schedules.
- The chapter recommends modern alternatives for production crawling: **Scrapy** for general structured-data scraping and **Crawl4AI** for LLM-targeted crawling.
- Troubleshooting tips: (a) comment out Medium URLs in the YAML configs to skip Selenium if ChromeDriver fails, leaving Substack / blog URLs handled by the LangChain-based `CustomArticleCrawler`; (b) `poetry poe run-import-data-warehouse-from-json` restores a backed-up dataset (88 articles, 3 users) from `data/data_warehouse_raw_data`.
- VSCode's MongoDB plugin is recommended for inspecting the local database (URI `mongodb://llm_engineering:llm_engineering@127.0.0.1:27017`).

## Key Quotes
> "An ETL pipeline involves three fundamental steps: We **extract** data from various sources… **transform** this data by cleaning and standardizing it… **load** the transformed data into a data warehouse or database." — definition the chapter operationalizes for LLM Twin.

> "By reducing all the collected data to three data categories and not creating a new data category for every new data source, we can easily extend this architecture to multiple data sources with minimal effort." — the core extensibility argument for the article/post/repository taxonomy.

> "Using a transactional database, such as MongoDB, as a data warehouse is uncommon. However, in our use case, we are working with small amounts of data, which MongoDB can handle… when working with big data (millions of documents or more), using a dedicated data warehouse such as Snowflake or BigQuery will be ideal." — justifying the unusual choice.

> "These two classes follow the LangChain paradigm, which provides high-level functionality that works decently in most scenarios. It is fast to implement but hard to customize. That is one of the reasons why many developers avoid using LangChain in production use cases." — the authors' explicit reservation about LangChain.

> "The ODM pattern is extremely similar to ORM, but instead of working with SQL databases and tables, it works with NoSQL databases (such as MongoDB) and unstructured collections." — the ORM→ODM analogy that frames `NoSQLBaseDocument`.

> "By leveraging Python packages such as Pydantic, we have out-of-the-box type validation, which ensures consistency in our datasets." — the role of Pydantic in the domain model.

## Architecture & Components

**ETL pipeline (ZenML `digital_data_etl`)**
- `pipelines/digital_data_etl.py` — `@pipeline` function: `get_or_create_user → crawl_links`.
- `steps/etl/get_or_create_user.py` — looks up or creates a `UserDocument`, attaches `query` / `retrieved` metadata to the ZenML `user` artifact.
- `steps/etl/crawl_links.py` — iterates links with `tqdm`, builds a `CrawlerDispatcher`, accumulates per-domain `{successful, total}` metadata for the `crawled_links` artifact.

**Crawler dispatcher**
- `llm_engineering/application/crawlers/dispatcher.py` — `CrawlerDispatcher`: `build()` classmethod + chainable `register_medium()` / `register_linkedin()` / `register_github()` methods (Builder pattern); `register(domain, crawler_cls)` normalizes via `urlparse` and stores as regex key `r"https://(www\.)?{netloc}/*"`; `get_crawler(url)` regex-matches and falls back to `CustomArticleCrawler`.

**Crawler hierarchy** (`llm_engineering/application/crawlers/`)
- `BaseCrawler(ABC)` — `model: type[NoSQLBaseDocument]`, abstract `extract(link, **kwargs)`.
- `BaseSeleniumCrawler(BaseCrawler, ABC)` — sets headless Chrome options, runs `chromedriver_autoinstaller.install()`, exposes `set_extra_driver_options`, `login`, `scroll_page` hooks; uses `scroll_limit` to bound infinite feeds.
- `GithubCrawler(BaseCrawler)` — model = `RepositoryDocument`; uses `subprocess.run(["git", "clone", link])` inside `tempfile.mkdtemp()`; ignores `.git`, `.toml`, `.lock`, `.png`.
- `CustomArticleCrawler(BaseCrawler)` — model = `ArticleDocument`; uses `langchain_community.document_loaders.AsyncHtmlLoader` + `Html2TextTransformer`.
- `MediumCrawler(BaseSeleniumCrawler)` — model = `ArticleDocument`; parses with `BeautifulSoup` (`pw-post-title`, `pw-subtitle-paragraph`).
- `LinkedInCrawler(BaseSeleniumCrawler)` — login + feed scroll; emits `PostDocument` instances.

**Domain documents / ODM** (`llm_engineering/domain/`)
- `domain/base/nosql.py` — `NoSQLBaseDocument(BaseModel, Generic[T], ABC)`: UUID4 `id`, `__eq__`/`__hash__`, `from_mongo`/`to_mongo`, `save`, `get_or_create`, `bulk_insert`, `find`, `bulk_find`, `get_collection_name` (reads `cls.Settings.name`).
- `domain/types.py` — `DataCategory(StrEnum)` with values used as MongoDB collection names.
- `domain/documents.py` — `Document(NoSQLBaseDocument, ABC)` (`content`, `platform`, `author_id`, `author_full_name`), then `ArticleDocument`, `PostDocument`, `RepositoryDocument`, `UserDocument`.

**Storage**
- MongoDB local container (`mongodb://llm_engineering:llm_engineering@127.0.0.1:27017`, default database `twin`); cloud freemium tier supported.
- Collections: `articles`, `posts`, `repositories`, `users`.

**Configuration / execution**
- Per-author YAML configs under `configs/` (`digital_data_etl_paul_iusztin.yaml`, `digital_data_etl_maxime_labonne.yaml`).
- Poe-the-poet entry points: `poetry poe run-digital-data-etl-paul`, `…-maxime`, `…` (all), plus `poetry poe run-import-data-warehouse-from-json` for the seeded dataset.

## Code & Concrete Examples

**Builder-pattern dispatcher wiring (chainable):**
```python
dispatcher = (CrawlerDispatcher
              .build()
              .register_linkedin()
              .register_medium()
              .register_github())
crawler = dispatcher.get_crawler(link)
crawler.extract(link=link, user=user)
```

**Regex-keyed domain registration:**
```python
def register(self, domain: str, crawler: type[BaseCrawler]) -> None:
    parsed_domain = urlparse(domain)
    domain = parsed_domain.netloc
    self._crawlers[r"https://(www\.)?{}/*".format(re.escape(domain))] = crawler
```

**GitHub crawler — `git clone` in a temp dir, walk + ignore patterns:**
```python
class GithubCrawler(BaseCrawler):
    model = RepositoryDocument
    def __init__(self, ignore=(".git", ".toml", ".lock", ".png")) -> None:
        super().__init__()
        self._ignore = ignore
    def extract(self, link, **kwargs):
        # …skip if already in DB; mkdtemp; subprocess git clone; os.walk; build {path: content}; RepositoryDocument(...).save()
```

**LangChain fallback for arbitrary sites:**
```python
loader = AsyncHtmlLoader([link])
docs = loader.load()
docs_transformed = Html2TextTransformer().transform_documents(docs)
content = {
    "Title": docs_transformed[0].metadata.get("title"),
    "Subtitle": docs_transformed[0].metadata.get("description"),
    "Content": docs_transformed[0].page_content,
    "language": docs_transformed[0].metadata.get("language"),
}
```

**Selenium scroll for infinite feeds:**
```python
def scroll_page(self):
    last_height = self.driver.execute_script("return document.body.scrollHeight")
    while True:
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)
        new_height = self.driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height or (self.scroll_limit and current_scroll >= self.scroll_limit):
            break
        last_height = new_height
        current_scroll += 1
```

**Medium parsing via BeautifulSoup:**
```python
soup = BeautifulSoup(self.driver.page_source, "html.parser")
title = soup.find_all("h1", class_="pw-post-title")
subtitle = soup.find_all("h2", class_="pw-subtitle-paragraph")
```

**Custom ODM CRUD primitives:**
```python
class NoSQLBaseDocument(BaseModel, Generic[T], ABC):
    id: UUID4 = Field(default_factory=uuid.uuid4)
    @classmethod
    def from_mongo(cls, data): ...
    def to_mongo(self, **kw): ...
    def save(self, **kw): ...
    @classmethod
    def get_or_create(cls, **filter_options): ...
    @classmethod
    def bulk_insert(cls, docs, **kw): ...
    @classmethod
    def find(cls, **filter_options): ...
    @classmethod
    def bulk_find(cls, **filter_options): ...
    @classmethod
    def get_collection_name(cls): return cls.Settings.name
```

**Data category enum + concrete documents:**
```python
class DataCategory(StrEnum):
    POSTS = "posts"; ARTICLES = "articles"; REPOSITORIES = "repositories"
    PROMPT = "prompt"; QUERIES = "queries"
    INSTRUCT_DATASET_SAMPLES = "instruct_dataset_samples"
    INSTRUCT_DATASET = "instruct_dataset"
    PREFERENCE_DATASET_SAMPLES = "preference_dataset_samples"
    PREFERENCE_DATASET = "preference_dataset"

class ArticleDocument(Document):
    link: str
    class Settings: name = DataCategory.ARTICLES
```

**Querying the warehouse through the ODM:**
```python
user = UserDocument.get_or_create(first_name="Paul", last_name="Iusztin")
articles = ArticleDocument.bulk_find(author_id=str(user.id))
# → Number of articles: 50
```

**Inspecting a ZenML artifact downstream:**
```python
from zenml.client import Client
artifact = Client().get_artifact_version('8349ce09-0693-4e28-8fa2-20f82c76ddec')
loaded_artifact = artifact.load()
```

## Connections
- [[ETL]] — chapter is a worked example of an extract / transform / load pipeline ending in a NoSQL warehouse.
- [[ELT]] — implicit contrast: the chapter loads cleaned text but defers feature transformation to the next pipeline.
- [[DataEngineering]] — the chapter sits squarely in this discipline as applied to LLM training-data collection.
- [[DataPipeline]] — concrete instantiation of a multi-stage data pipeline orchestrated by ZenML.
- [[DataWarehouse]] — the chapter uses MongoDB as one, with caveats about scale.
- [[DataLake]] — referenced implicitly as an alternative to the chosen warehouse approach.
- [[BuilderPattern]] — `CrawlerDispatcher.build().register_*()` chain is a canonical builder.
- [[DSPy]] — unrelated; this chapter does not touch DSPy but its data is the upstream input for any later DSPy-based LLM pipeline.
- [[rag]] — feature pipeline in Ch. 4 ingests this chapter's MongoDB data into Qdrant for retrieval.
- [[FineTuning]] — same raw corpus feeds fine-tuning pipelines later in the book.
- [[GitHub]] — one of the four crawled sources; cloned via `git clone` in a subprocess.
- [[FastAPI]] — referenced as motivating SQLModel (FastAPI's ORM wrapper over SQLAlchemy).
- [[NLP]] — text crawling pipeline produces the corpus consumed by downstream NLP/LLM stages.
- [[CustomerServiceAgent]] — sibling DSPy example; both illustrate end-to-end LLM application engineering.
- [[Pydantic]] *(new)* — Pydantic `BaseModel` and `Field` underpin every domain document and provide type validation.
- [[MongoDB]] *(new)* — primary NoSQL data warehouse; chapter uses `pymongo` directly.
- [[ZenML]] *(new)* — orchestrates the `digital_data_etl` pipeline and exposes its artifacts.
- [[Qdrant]] *(new)* — vector DB target of the downstream feature pipeline (mentioned).
- [[Selenium]] *(new)* — drives headless Chrome for Medium / LinkedIn crawlers.
- [[BeautifulSoup]] *(new)* — parses HTML extracted by Selenium into title / subtitle / content fields.
- [[LangChain]] *(new)* — `AsyncHtmlLoader` + `Html2TextTransformer` power the `CustomArticleCrawler` fallback.
- [[Scrapy]] *(new)* — recommended for production-grade general web scraping.
- [[Crawl4AI]] *(new)* — recommended for LLM-targeted crawling.
- [[SQLAlchemy]] *(new)* — used to explain the ORM pattern that motivates the chapter's ODM.
- [[SQLModel]] *(new)* — FastAPI's SQLAlchemy wrapper, mentioned alongside SQLAlchemy.
- [[ORM]] *(new)* — Object-Relational Mapping pattern; basis of the analogy with ODM.
- [[ODM]] *(new)* — Object-Document Mapping pattern; the chapter implements one from scratch.
- [[CRUD]] *(new)* — operations that ORMs/ODMs encapsulate.
- [[WebCrawling]] *(new)* — the umbrella technique for the four crawler implementations.
- [[Polymorphism]] *(new)* — the dispatcher relies on this OOP concept to call `extract()` uniformly.
- [[LLMTwin]] *(new)* — book-spanning project this chapter feeds.
- [[Snowflake]] — recommended large-scale data warehouse alternative.
- [[GoogleBigQuery]] — recommended large-scale data warehouse alternative.
- [[Loguru]] *(new)* — logging library used throughout the codebase.
- [[Pulumi]] *(new)* — referenced as the IaC tool used in Ch. 4 to provision infrastructure.
- [[Packt]] *(new)* — publisher of the LLM Engineer's Handbook.
- [[PaulIusztin]] *(new)* — co-author; one of the two configured "users" whose links seed the pipeline.
- [[MaximeLabonne]] *(new)* — co-author; the other configured user.
- [[AlexVesa]] *(new)* — co-author.
- [[Medium]] *(new)* — one of the four crawled platforms.
- [[Substack]] *(new)* — crawled via the `CustomArticleCrawler` fallback.
- [[LinkedIn]] *(new)* — crawled via Selenium-driven `LinkedInCrawler`.
- [[ChromeDriver]] *(new)* — installed automatically via `chromedriver_autoinstaller`; the Selenium-vs-driver mismatch is a documented failure mode.
- [[PoeThePoet]] *(new)* — task runner used to invoke pipeline configurations.
- [[Mongoengine]] *(new)* — production ODM that the chapter compares its custom implementation against.

## Contradictions
- The chapter labels MongoDB a "data warehouse" while simultaneously acknowledging this is an unconventional use of a transactional NoSQL DB; this differs from the orthodox separation between transactional stores and warehouses found on the existing [[DataWarehouse]] and [[DataLake]] pages and on data-engineering chapters from other books in the wiki (e.g., madewithml-mlops-data-engineering). Not a factual contradiction — the authors flag the trade-off explicitly and recommend Snowflake / BigQuery for scale — but worth noting when synthesizing the wiki's overall stance on warehouse architecture.
- The chapter is mildly skeptical of LangChain ("fast to implement but hard to customize… many developers avoid using LangChain in production use cases"), which contrasts with more enthusiastic LangChain treatments elsewhere in the source set (e.g., DSPy materials position LangChain as a reasonable baseline). This is opinion, not contradiction.
