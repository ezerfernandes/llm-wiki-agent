---
title: "IIR Ch. 20: Web Crawling and Indexes"
type: source
tags: [iir, information-retrieval, textbook, web-crawler, url-frontier, distributed-index]
date: 2026-05-23
source_file: "https://nlp.stanford.edu/IR-book/html/htmledition/web-crawling-and-indexes-1.html"
---

## Summary

Chapter 20 of *Introduction to Information Retrieval* (Manning, Raghavan, Schütze 2008) turns from how to score and rank documents to the systems problem of *acquiring* the web corpus in the first place and then *distributing* the resulting index over many machines. It treats web crawling as a graph traversal that must be **polite, robust, distributed, scalable, efficient, extensible, and quality-biased**, then drills into the [[Mercator]]-style crawler architecture — a pipeline of fetcher, parser, URL filter, content-seen test, duplicate-URL elim, and a [[URLFrontier]] split into prioritization *front queues* and politeness *back queues*. It identifies [[DNSResolution]] as a hidden bottleneck that forces crawlers to ship their own asynchronous resolver with exponential backoff. It explains how the [[RobotsExclusionProtocol]] and [[Sitemap]]s govern what a crawler may and should fetch. Finally it contrasts [[TermPartitioning]] (global) vs. [[DocumentPartitioning]] (local) indexes for web-scale serving, and introduces the [[ConnectivityServer]], which uses gap encoding plus row-similarity and locality tricks to fit the entire web graph (a few billion nodes, tens of billions of edges) in RAM at roughly 3 bits per link.

## Key Claims

- Web crawling is graph traversal from a *seed set*: fetch page, parse out text and links, hand text to indexer, push new URLs onto the [[URLFrontier]]. ([[InformationRetrieval]])
- A practical [[WebCrawler]] must be **robust** (resilient to spider traps) and **polite** (respect server policies); it *should* also be distributed, scalable, efficient, quality-biased, fresh, and extensible.
- Politeness has three operational rules: (1) at most one open connection per host at a time, (2) several-second gap between successive requests to the same host, (3) honor the [[RobotsExclusionProtocol]] (`robots.txt`).
- Fetching ~1 billion pages/month means several *hundred pages per second*, achievable only with a multi-threaded design and asynchronous I/O.
- Crawler architecture has five core modules: URL Frontier, [[DNSResolution]], Fetch (HTTP), Parse, Duplicate Elimination — plus a *Content Seen?* stage using fingerprints/shingles to skip pages whose content was already indexed under a different URL.
- `robots.txt` must be re-checked *immediately before fetching*, not at link-extraction time, because a URL may sit in the frontier for a long time and the host's policy could change.
- DNS lookups can take seconds and the standard libc resolver is *synchronous*, blocking all threads in a process; crawlers therefore implement custom asynchronous DNS resolvers with retry and exponential backoff (Mercator: ~5 retries from 1s to ~90s).
- The [[URLFrontier]] is the heart of the crawler. It must simultaneously prioritize (high-quality, fast-changing pages first) *and* enforce politeness (per-host pacing). Mercator's solution is a two-tier queue system: F **front queues** (priority) feeding B **back queues** (one queue per host), with a min-heap of next-allowed-fetch times.
- For scale, most of the URL frontier lives on disk; only a working set stays in RAM.
- Content-seen deduplication is hard to distribute: fingerprints have no host locality, so they must be partitioned by hash of the fingerprint, requiring RPCs per check; no caching benefit because the fingerprint stream has no temporal locality.
- A distributed crawler uses a **host splitter** after the URL filter to route URLs to the node responsible for that host. Geographic locality of nodes is *not* a reliable way to assign hosts.
- Two index distribution strategies: **term-partitioned** (global index, each node owns a dictionary subset) vs. **document-partitioned** (local index, each node holds a full inverted index over its document shard). Document partitioning is preferred in practice — queries fan out to all nodes, results merge, and load balances naturally; term partitioning suffers from long postings shipped across the network and skewed term-frequency load. ([[InvertedIndex]])
- Document partitioning forces global statistics like `idf` to be computed and refreshed by a separate background pass across the whole collection.
- A **[[ConnectivityServer]]** answers "what links into / out of URL X?" queries used by link analysis, sibling-page detection, and crawl scheduling. A naive store would need ~320 GB for 4B pages × 10 links; three compression tricks bring this to ~3 bits per link: (a) row similarity (encode an adjacency row as a delta from a recent prototype row), (b) link locality (most outlinks are on the same host, so destinations are nearby integers), (c) **gap encoding** of sorted destination lists.
- Historical context: the first crawler was Matthew Gray's *Wanderer* (1993); [[Mercator]] (Najork & Heydon) is the reference design; Boldi & Vigna (2004) gave the 3-bits-per-link connectivity scheme; Google's web-scale distribution is documented in Barroso et al. (2003).

## Section Notes

### 20.1 Overview
Web crawling = "the process by which we gather pages from the Web, in order to index them and support a search engine." Scope ranges from a student-project crawler to web-scale operations such as those of [[CommonCrawl]] or commercial engines.

### 20.1.1 Features a crawler MUST provide
Two non-negotiables:
1. **Robustness** — survive *spider traps*, both malicious and accidental, that generate infinite pages within a domain.
2. **Politeness** — honor each server's implicit (load) and explicit (`robots.txt`) policies; violators get IP-banned and harm the whole crawling community.

### 20.1.2 Features a crawler SHOULD provide
Six "shoulds": distributed, scalable, efficient (CPU/disk/network), biased toward *quality* (because most web pages are low utility), *fresh* (re-fetch frequency tracks observed page change rate), and *extensible* (modular for new MIME types and protocols).

### 20.2 Crawling
Standard loop: pop URL from frontier → DNS resolve → HTTP fetch → parse → emit text to indexer → emit links back into frontier. Continuous crawling re-adds fetched URLs to the frontier with future timestamps.

### 20.2.1 Crawler architecture
The five modules — URL Frontier, DNS Resolver, Fetch, Parse, Dup Elim — are connected by a pipeline:

```
[Frontier] -> [DNS] -> [Fetch] -> [Parse] -> [Content Seen?] -> [URL Filter] -> [Robots Filter] -> [Dup URL Elim] -> [Frontier]
```

A separate **housekeeping thread** snapshots state for failure recovery (checkpointing) and tracks crawl statistics. The *Content Seen?* test uses fingerprints (e.g. 64-bit Rabin) or shingles to detect duplicate or near-duplicate page content even if the URLs differ.

### 20.2.2 DNS resolution
Standard resolvers are synchronous and slow. Mitigations: (a) in-process DNS cache, though politeness blunts its effectiveness; (b) custom asynchronous resolver thread that sends UDP queries and reaps replies; (c) exponential backoff retries because some legitimate hosts genuinely take a long time to resolve.

### 20.2.3 The URL frontier
Mercator-style two-tier design:

- **F front queues** (numbered 1..F by priority). On extraction, a URL's priority is computed from page quality (e.g., PageRank-ish signals) and observed change rate; the URL is appended to its priority queue.
- **B back queues** (one per host, B chosen so B ≥ number of crawl threads). Each back queue holds URLs from exactly one host.
- A **min-heap** keyed by *earliest next fetch time per back queue* governs which thread fetches next.
- Fetch loop: pull root of heap (host h, time t) → wait until t → fetch → re-heap with t' = t + k·(last fetch latency) where k ≈ 10. If the back queue empties after the pull, refill it by popping URLs from the front queues (biased toward higher-priority queues) until a URL whose host is not yet mapped to a back queue appears.
- Most of the frontier lives on disk; in-memory portion is a working set that is paged.

### 20.2.4 Distributing the crawler
Add a **host splitter** stage right after URL filtering: hash the host to one of N crawler nodes. Each node runs the full local pipeline. Geographic placement (crawl "near" hosts) is unreliable because routing and TLDs don't track physical location.

*Content Seen?* in a distributed setting:
- Fingerprints partitioned by `hash(fingerprint) mod N`, *not* by host, since identical content can appear on different hosts.
- Each check usually requires an RPC to a remote node.
- The fingerprint stream has no temporal locality, so caching does not help.
- Pages change, so old fingerprints must be evictable.

### 20.3 Distributing indexes
Two schemes:

- **Term partitioning (global index)**: dictionary split across nodes; node *k* owns postings for some subset of terms. Allows query-level concurrency but multi-term queries ship long postings across the network and load skews with term frequency.
- **Document partitioning (local index)**: each node holds a complete [[InvertedIndex]] over its document shard. Queries broadcast to all nodes; partial results merge. Trades extra disk seeks for less network traffic, balances load naturally, and is what most large web search engines use.

Practical refinement: assign documents to shards via *hash of URL* (uniform load) rather than by host (which would cluster topically and bias rankings). A tiered architecture splits high-scoring from low-scoring docs and consults lower tiers only if upper tiers don't yield enough results. Global `idf` must be computed by a periodic background pass across the whole corpus.

### 20.4 Connectivity servers
A [[ConnectivityServer]] stores the *web graph* and answers in/out-neighbor queries used by link analysis, crawl scheduling, near-duplicate / mirror detection, and finding sibling pages. Goal isn't merely "fit in memory" but "fit in memory while still supporting fast random-access queries." Bharat et al. (1998) introduced the idea; Boldi & Vigna (2004) achieved ~3 bits per link using:

1. **Row similarity** — adjacency rows of nearby URLs are nearly identical (shared nav, footer, copyright links). Encode row *i* as deltas from a prototype row chosen from the previous ~7 rows.
2. **Locality** — most outlinks point within the same host; sort URLs lexicographically so destination IDs of intra-host links are small.
3. **Gap encoding** — store sorted destination lists as gaps (variable-length codes), not absolute IDs.

### 20.5 References and further reading
Wanderer (Gray 1993, first crawler); [[Mercator]] (Najork & Heydon); WebBase (Hirai et al. 2000); Cho & Garcia-Molina (2002) on distributed-crawler taxonomies; Boldi et al. (2002), Shkapenyuk & Suel (2002) on large-scale crawlers; Barroso et al. (2003) on Google's index distribution; Tomasic & Garcia-Molina (1993) and Jeong & Omiecinski (1995) on term-vs-doc partitioning; Sornil (2001) on hybrid partitioning. Robots Exclusion Protocol: `robotstxt.org/wc/exclusion.html`.

## Algorithms & Formulas

### URL frontier — Mercator front/back queue design

```
Front queues F[1..F]            # F priority levels
Back queues  B[1..B]            # B ≥ #threads, one per active host
Map host -> back-queue index
Heap H keyed by (next_fetch_time_for_host)

# Enqueue side
on receiving URL u with priority p in {1..F}:
    F[p].append(u)

# Crawler thread loop
loop:
    (h, t) = H.pop_min()
    sleep until t
    u = B[idx_of(h)].pop_head()
    page = HTTP_fetch(u)
    delta = max(min_gap, 10 * last_fetch_latency(h))
    if B[idx_of(h)].empty:
        # refill: pull from front queues biased to higher priority
        while true:
            v = pick_front_queue_biased().pop_head()
            if host(v) not in map:
                map[host(v)] = idx_of(h)
                B[idx_of(h)].append(v)
                H.push((host(v), now + delta))
                break
            else:
                B[map[host(v)]].append(v)   # routed elsewhere; keep refilling
    else:
        H.push((h, now + delta))
```

Politeness emerges because (1) at most one back queue per host means at most one URL of host *h* is in flight, and (2) the heap re-insertion enforces the time gap.

### Duplicate elimination (content-seen test)

```
def content_seen(page_bytes):
    fp = fingerprint64(page_bytes)          # e.g. Rabin fingerprint
    node = fp % N                           # owning node in distributed case
    return rpc(node, "lookup_and_add", fp)  # set membership over the web

def url_seen(u):
    return BloomOrHash.contains_or_add(canonicalize(u))
```

URL-level dedup keeps the frontier free of revisits; content-level dedup keeps the indexer from re-indexing mirrors.

### Robots Exclusion Protocol — minimal parse

```
# /robots.txt, fetched and cached per host with TTL
User-agent: *
Disallow: /tmp/
Disallow: /private
Crawl-delay: 5
Sitemap: https://example.com/sitemap.xml

def allowed(url, ua="MyBot"):
    rules = cache.get(host(url)) or fetch_robots(host(url))
    block = rules.most_specific_block_for(ua)
    for pat in block.disallow:
        if path(url).startswith(pat):
            for pat2 in block.allow:               # later RFC 9309 extension
                if path(url).startswith(pat2):
                    return True
            return False
    return True
```

Must be re-checked *just before* fetch — `robots.txt` is mutable and the URL may have been in the frontier for days.

### Term-partitioned vs. document-partitioned query

```
# Document partitioned (local index)
def query_doc_partitioned(q):
    partial = parallel_call(all_nodes, node.search, q, k)
    return merge_topk(partial, k)

# Term partitioned (global index)
def query_term_partitioned(q):
    posting_lists = []
    for t in q.terms:
        posting_lists.append(rpc(node_for_term(t), "get_postings", t))
    # intersect/merge on coordinator -> heavy traffic for rare-common term mixes
    return score_and_topk(intersect(posting_lists), k)
```

### Connectivity server compression

```
# Pre-process
URLs sorted lexicographically -> integer IDs (induces link locality)

# For each row i (outlinks of URL i)
prototype_j = argmin_{j in [i-7, i-1]} dist(row_i, row_j)
delta_i     = row_i XOR row_j     # encoded as add/remove sets

# Encode delta destination list using gaps
sorted_dsts = sort(delta_i.adds)
gaps        = [sorted_dsts[0]] + [sorted_dsts[k]-sorted_dsts[k-1] for k>=1]
bits        = concat(gamma_or_delta_code(g) for g in gaps)
```

End result: ~3 bits/edge → the entire web graph fits in RAM.

## Key Quotes

> "Crawling the web…is the first step in any web search engine." — §20.1

> "Web crawlers are also known as spiders, robots, web robots, etc." — §20.1

> "[Crawlers] must be robust [to] spider traps, which are generators of web pages that mislead crawlers into getting stuck fetching an infinite number of pages in a particular domain." — §20.1.1

> "Web servers have both implicit and explicit policies regulating the rate at which a crawler can visit them." — §20.1.1 (introducing the [[RobotsExclusionProtocol]])

> "Only one connection should be open to any given host at a time… [and] a waiting time of a few seconds should occur between successive requests to a host." — §20.2

> "DNS resolution is a well-known bottleneck in web crawling." — §20.2.2

> "High-quality pages that change frequently should be prioritized for frequent crawling." — §20.2.3

> "Our goal is not to simply compress the web graph to fit into memory; we must do so in a way that efficiently supports connectivity queries." — §20.4

> "As few as 3 bits per link, on average — a dramatic reduction from the 64 required in the naive representation." — §20.4 (on Boldi & Vigna's [[ConnectivityServer]])

## Connections

- [[InformationRetrieval]] — Chapter 20 is the systems counterpart to the algorithmic IR core: it explains how the corpus that earlier chapters assume actually shows up on disk.
- [[InvertedIndex]] — directly extends the single-machine index of earlier chapters to distributed term- and document-partitioned variants.
- [[CommonCrawl]] — a present-day, open implementation of the architecture this chapter describes; the [[URLFrontier]] / politeness / `robots.txt` discipline of CC matches §20.2 almost verbatim.
- [[WebCrawler]] — new concept page: general-purpose definition + the seven desiderata (robust, polite, distributed, scalable, efficient, quality-biased, extensible).
- [[URLFrontier]] — new concept page: the prioritized + per-host queueing data structure that is the heart of any production crawler.
- [[RobotsExclusionProtocol]] — new concept page: `robots.txt` semantics, *Crawl-delay*, *Sitemap* directives, and why it is re-checked just before fetch.
- [[Sitemap]] — new concept page: XML sitemap mechanism for sites to advertise high-priority URLs and last-modified dates to crawlers.
- [[Mercator]] — new concept page: the canonical academic crawler (Najork & Heydon, Compaq SRC, 1999), reference architecture for §20.2.
- [[ConnectivityServer]] — new concept page: in-memory web-graph store using row similarity + locality + gap encoding.
- [[TermPartitioning]] — new concept page: global-index distribution scheme.
- [[DocumentPartitioning]] — new concept page: local-index distribution scheme, dominant in practice.
- [[DNSResolution]] — new concept page: why DNS is a crawler bottleneck and how custom async resolvers fix it.
- [[Politeness]] — new concept page: per-host rate-limiting and connection-cap discipline for crawlers and other automated clients.
- [[Heritrix]] — new entity page: Internet Archive's open-source production crawler, modeled closely on [[Mercator]] (referenced in the IIR further-reading lineage).
- [[InternetArchive]] — new entity page: operator of [[Heritrix]] and the Wayback Machine; consumes the architecture of this chapter at the largest open scale.

## Contradictions

- None with existing wiki content. The chapter slightly tightens the politeness picture compared to popular folklore: it is *not* the case that one "Crawl-delay" in `robots.txt` is sufficient — IIR also requires the one-connection-per-host invariant and a time-gap proportional to last fetch latency. If a later page on [[CommonCrawl]] or [[Politeness]] suggests fixed delays alone are enough, it should be reconciled with §20.2.
