---
title: "The Fuzzing Book Ch 01 — Tours through the Book"
type: source
tags: [book, fuzzingbook, fuzzing, testing, security, navigation, orientation, table-of-contents]
date: 2026-06-06
source_file: raw/books/fuzzingbook/fuzzingbook-01-tours.md
book: "The Fuzzing Book"
book_authors: ["Andreas Zeller", "Rahul Gopinath", "Marcel Böhme", "Gordon Fraser", "Christian Holler"]
book_publisher: "CISPA Helmholtz Center for Information Security"
book_year: 2024
book_url: "https://www.fuzzingbook.org/"
---

# Tours through the Book

## Summary
This is the opening orientation chapter of *The Fuzzing Book* — a navigational "meta" chapter that maps the book's overall structure rather than teaching a fuzzing technique. The book is large (>20,000 lines of code and >150,000 words, ~1,200 printed pages), so the chapter argues against linear reading and instead offers a **chapter dependency sitemap** (a prerequisite graph where $A \rightarrow B$ means chapter $A$ is a prerequisite for chapter $B$) plus several role-based **tours** (reading paths) tailored to programmers, students, and researchers. It establishes the six-part arc of the book: orientation, lexical fuzzing, syntactic fuzzing, semantic fuzzing, domain-specific fuzzing, and managing fuzzing. As the table-of-contents/front-matter source, its primary value is linking the 30 sibling content chapters; the canonical entry point for the basics is [[fuzzingbook-02-intro-testing|Ch 2]].

## Key Concepts
- **Chapter dependency sitemap** — a directed prerequisite graph (rendered as an interactive SVG, `PICS/Sitemap.svg`) over all chapters; readers pick any path to reach topics of interest.
- **Role-based tours** — curated reading paths that subset the sitemap:
  - **Pragmatic Programmer Tour** — usage-first path: [[fuzzingbook-02-intro-testing|Ch 2]] → simple [[Fuzzing|fuzzers]] ([[fuzzingbook-03-fuzzer|Ch 3]]) → [[Coverage|coverage]] ([[fuzzingbook-04-coverage|Ch 4]]) and greybox guidance ([[fuzzingbook-06-greybox-fuzzer|Ch 6]]) → grammars ([[fuzzingbook-09-grammars|Ch 9]]) and grammar-coverage fuzzing ([[fuzzingbook-11-grammar-coverage-fuzzer|Ch 11]]) → probabilistic ([[fuzzingbook-13-probabilistic-grammar-fuzzer|Ch 13]]) and generator-based fuzzing ([[fuzzingbook-14-generator-grammar-fuzzer|Ch 14]]) → managing fuzzers at scale ([[fuzzingbook-29-fuzzing-in-the-large|Ch 29]]). Advises reading each chapter's **Synopsis** section first.
  - **Page-by-Page / Part Tours** — the book's own organization: lexical (Part II), syntactical (Part III), semantic (Part IV), application/domain-specific (Part V), management (Part VI).
  - **Undergraduate Tour** — algorithm/implementation depth: testing + [[Coverage|coverage]] basics → simple fuzzers → mutation-based fuzzing ([[fuzzingbook-05-mutation-fuzzer|Ch 5]]) → grammars and grammar mining ([[fuzzingbook-18-grammar-miner|Ch 18]]) → API ([[fuzzingbook-24-api-fuzzer|Ch 24]]) and GUI fuzzing ([[fuzzingbook-28-gui-fuzzer|Ch 28]]) → input reduction ([[fuzzingbook-16-reducer|Ch 16]]).
  - **Graduate Tour** — adds search-based testing ([[fuzzingbook-07-search-based-fuzzer|Ch 7]]), configuration testing ([[fuzzingbook-23-configuration-fuzzer|Ch 23]]), mutation analysis ([[fuzzingbook-08-mutation-analysis|Ch 8]]), parsing ([[fuzzingbook-12-parser|Ch 12]]), concolic ([[fuzzingbook-20-concolic-fuzzer|Ch 20]]) and symbolic fuzzing ([[fuzzingbook-21-symbolic-fuzzer|Ch 21]]), and stopping criteria ([[fuzzingbook-30-when-to-stop-fuzzing|Ch 30]]).
  - **Black-Box Tour** — techniques needing no program feedback: basic fuzzing, syntactical fuzzing, semantic fuzzing with constraints ([[fuzzingbook-17-fuzzing-with-constraints|Ch 17]]), domain-specific fuzzing, large-scale management.
  - **White-Box Tour** — feedback-driven techniques: [[Coverage|coverage]], mutation-based fuzzing, greybox/AFL-style fuzzing, information flow ([[fuzzingbook-19-information-flow|Ch 19]]) + concolic, and symbolic fuzzing.
  - **Researcher Tour** — open research topics: mining function specifications ([[fuzzingbook-22-dynamic-invariants|Ch 22]]), mining input grammars ([[fuzzingbook-18-grammar-miner|Ch 18]]), probabilistic and generator/constraint-based fuzzing, carving unit tests ([[fuzzingbook-25-carver|Ch 25]]), web ([[fuzzingbook-27-web-fuzzer|Ch 27]]) and GUI testing, and statistical estimators in greybox fuzzing ([[fuzzingbook-15-greybox-grammar-fuzzer|Ch 15]]).
  - **Author Tour** — for contributors: the Guide for Authors and a Template chapter (non-content appendices).
- **Synopsis-first reading** — every content chapter opens with a "Synopsis" giving a usage-level overview; readers can stop there for a "usage" view or read on for "understanding."

## Key Claims
- The book contains >20,000 lines of code and >150,000 words; a printed edition would exceed 1,200 pages — motivating non-linear, tour-based reading.
- The chapters form a prerequisite DAG, not a strict linear sequence; multiple valid reading orders exist.
- The simple fuzzers introduced early ([[fuzzingbook-03-fuzzer|Ch 3]]) reflect techniques that "took down 30% of UNIX utilities in the 90s."
- Mutation-based fuzzing ([[fuzzingbook-05-mutation-fuzzer|Ch 5]]) is described as "pretty much the standard in fuzzing today."
- The book deliberately separates a *usage* perspective (read only the Synopsis) from an *understanding* perspective (read the full chapter and experiment with the Python implementations).
- Having runnable Python implementations in notebooks is framed as the book's key asset for both learners and researchers (who can extend and evaluate ideas, then port stable approaches to languages like C).

## Key Quotes
> "This book is _massive_. With more than 20,000 lines of code and 150,000 words of text, a printed version would cover more than 1,200 pages of text." — opening motivation for the tours.

> "an arrow $A \rightarrow B$ means that chapter $A$ is a prerequisite for chapter $B$. You can pick arbitrary paths in this graph to get to the topics that interest you most." — describing the dependency sitemap.

> "[Mutation-based fuzzing] is pretty much the standard in fuzzing today: Take a set of seeds, and mutate them until we find a bug." — Undergraduate/White-Box tours.

## Connections
- [[Fuzzing]] — the book's central subject; this chapter orients the reader across all fuzzing techniques it covers.
- [[Testing]] / [[Coverage]] — recurring foundations that every tour starts from.
- [[AndreasZeller]] — lead author; the chapter is the authors' framing of how to navigate their book.
- [[fuzzingbook-02-intro-testing|Ch 2]] — the universal starting point every tour points to first.
- [[fuzzingbook-03-fuzzer|Ch 3]], [[fuzzingbook-05-mutation-fuzzer|Ch 5]], [[fuzzingbook-06-greybox-fuzzer|Ch 6]] — the lexical-fuzzing core the programmer/undergraduate tours route through.
- [[fuzzingbook-09-grammars|Ch 9]] through [[fuzzingbook-16-reducer|Ch 16]] — the syntactic-fuzzing part reachable via the syntactical tour.
- [[fuzzingbook-17-fuzzing-with-constraints|Ch 17]] through [[fuzzingbook-22-dynamic-invariants|Ch 22]] — semantic fuzzing emphasized in the graduate/researcher tours.
- [[fuzzingbook-23-configuration-fuzzer|Ch 23]] through [[fuzzingbook-28-gui-fuzzer|Ch 28]] — domain-specific applications.
- [[fuzzingbook-29-fuzzing-in-the-large|Ch 29]], [[fuzzingbook-30-when-to-stop-fuzzing|Ch 30]] — the management part the programmer and graduate tours close with.

## Contradictions
- None identified.
