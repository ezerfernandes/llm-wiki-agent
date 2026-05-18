---
title: "ParProcBook Appendix C: R Quick Start"
type: source
tags: [textbook, parallel-computing, r-language, programming-primer]
date: 2026-05-17
source_file: raw/parproc-matloff.pdf
---

## Summary

Appendix C of [[NormMatloff|Matloff]]'s *Programming on Parallel Machines* (pp. 321–338) is a self-contained R primer written for readers coming from C/C++. It introduces [[Rlanguage|R]]'s core data model — everything is a vector, scalars are one-element vectors, column-major 2-D storage — and motivates [[RVectorization|R vectorization]] as the primary technique for writing fast R code: replacing interpreted loops with calls to compiled built-in functions reduces runtimes by orders of magnitude. The appendix also covers the [[RList|R list type]], [[S3Classes|S3 object-oriented classes]], data frames, graphics, packages, debugging, complex numbers, and pointers to further learning.

## Key Claims

- **C/R correspondence**: assignment is `<-` (not `=`), subscripts start at 1 (not 0), 2-D arrays use column-major order, modules are loaded with `library()`, the comment character is `#`.
- **Vectorization is a performance imperative**: `sum(x)` on a million-element vector runs in ~0.006 s; an equivalent scalar `for` loop takes ~2.859 s — a ~476× difference. This shift from interpreted R to C-level built-ins is the single most important optimization strategy available in R, and the parallel chapters build on it (Snow, Rdsm, CUDA R bindings all assume vectorized worker functions).
- **Recycling**: R scalars do not exist — `2.5 * m3` recycles `2.5` to a conforming matrix before element-wise multiplication. `ifelse()` is the vectorized conditional: `ifelse(bool_vec, yes_vec, no_vec)` processes all elements in one compiled call.
- **The list type** is the workhorse mixed container: components accessed by `$name` or `[[i]]`, returned from functions to yield multiple values. `Reduce()` applies a function cumulatively across list elements; `lapply()` and `sapply()` map a function over a list.
- **S3 classes** are lists with a class attribute. Generic functions dispatch on the class: defining `print.employee()` causes `print(j)` to call that method when `class(j) == "employee"`.
- **Data frames** are lists of equal-length column vectors supporting mixed types — R's native tabular data structure. Filtering (`df[df$col == val,]`), column addition, `write.table()` / `read.table()` I/O, and `rbind()` / `cbind()` all apply.
- **Packages**: the CRAN repository hosts thousands of contributed packages. `install.packages()` downloads; `library()` attaches. The `parallel` package (shown via `ls(package:parallel)`) provides `makeCluster`, `clusterApply`, `parLapply`, `parSapply`, `mclapply`, `mcparallel`, and related functions — the functional parallel API that the book's Ch1 and Ch9 use with [[Snow]].
- **Debugging**: R's built-in `debug()` is primitive; Matloff recommends RStudio's integrated debugger, `ess-tracebug` for Emacs, StatET for Eclipse, or his own `debugR` tool (Linux/Mac only).
- **Complex numbers**: native support via `complex(real=..., imaginary=...)`, arithmetic operators, `Re()`, `Im()`, `abs()`, `exp()`, `cos()`, `sin()`. Complex-valued vectors and matrices work without special functions.

## Key Quotes

> "Vectorization means taking advantage of the vector-based, functional language nature of R, exploiting R's built-in functions instead of loops. This changes the venue from interpreted R to C level, with a potentially large increase in speed." — §C.4

> "In R, scalars don't really exist; they are just one-element vectors." — §C.6

> "R is an object-oriented (and functional) language. It features two types of classes, S3 and S4." — §C.10.3

## Section Outline

| Section | Topic |
|---|---|
| C.1 | Correspondences: R vs C/C++ (assignment, subscripts, storage order, modules, logical values) |
| C.2 | Starting R: interactive `>` prompt, IDEs (ESS/RStudio/StatET), `Rscript` for batch work |
| C.3 | First session: defining and loading functions with `source()`, `ls()`, `class()`, vector construction with `c()`, subsetting `x[2:4]`, `x[c(1,3:5)]` |
| C.4 | Vectorization: compiled built-ins vs interpreter loops; `system.time()` benchmark |
| C.5 | Second session: matrix construction (`rbind()`, `matrix()`), element-wise `*` vs `%*%` (linear algebra), `ifelse()`, `t()`, `solve()` for linear systems and matrix inverse |
| C.6 | Recycling: scalar replication to match vector/matrix dimensions |
| C.7 | More on vectorization: `ifelse()` form and semantics |
| C.8 | Third session: `t()` transpose, submatrix extraction, `rep()`, `solve()` system and inverse |
| C.9 | Default argument values: `sort(x, decreasing=FALSE)` pattern |
| C.10 | List type: basics (`list()`, `$`, `[[]]`), `Reduce()`, S3 classes and generic dispatch |
| C.11 | Workhorse functions: `apply()` (rows/cols of matrix), `lapply()` (list output), `sapply()` (simplified output), `split()` (group by factor) |
| C.12 | Handy utilities: `names()`, `str()`, `summary()` for exploring complex nested objects |
| C.13 | Data frames: mixed-type tabular data; `airquality` worked example; filter, add column, I/O |
| C.14 | Graphics: base R graphics; `lattice` and `ggplot2` packages; `pr2file()` utility for saving PDF/PNG/JPEG |
| C.15 | Packages: CRAN, `install.packages()`, `library()`, Task Views; `parallel` package listing |
| C.16 | Other learning sources: `http://heather.cs.ucdavis.edu/~matloff/r.html` |
| C.17 | Online help: `?fn`, `help(fn)`, `example(wireframe)` |
| C.18 | Debugging: `debug()` primitive; RStudio, ess-tracebug, StatET, debugR alternatives |
| C.19 | Complex numbers: `complex()`, arithmetic, `Re()`, `Im()`, `abs()`, `exp()` |
| C.20 | Further reading: *The Art of R Programming* (Matloff, NSP 2011), *Advanced R* (Wickham), *The R Book*, *R in a Nutshell*, *R for Dummies* |

## Code Examples (Representative)

**Vectorized oddcount** — counts odd elements without a loop:
```r
oddcount <- function(x) sum(x %% 2 == 1)
```

**Vectorized sum vs loop benchmark** (§C.4):
```r
x <- runif(1000000)
system.time(sum(x))        # user 0.008, elapsed 0.006
system.time({s <- 0; for (i in 1:1000000) s <- s + x[i]})
                           # user 2.776, elapsed 2.859
```

**Matrix operations** (§C.5):
```r
m1 <- rbind(1:2, c(5,8))
m2 <- matrix(1:6, nrow=2)  # column-major: 1,3,5 across row 1
m1 * m3                    # element-wise
m1 %*% m3                  # linear algebra multiply
solve(ma, c(3,17))         # solve linear system
solve(ma)                  # matrix inverse
```

**S3 generic dispatch** (§C.10.3):
```r
j <- list(name="Joe", salary=55000, union=T)
class(j) <- "employee"
print.employee <- function(wrkr) {
    cat(wrkr$name, "\n")
    cat("salary", wrkr$salary, "\n")
}
print(j)   # dispatches to print.employee()
```

**Data frame filtering** (§C.13):
```r
aqjune <- airquality[airquality$Month == 6,]
mean(aqjune$Temp)
write.table(aqjune, "AQJune")
```

## Connections

- [[Rlanguage]] — the entity page for R as a language; this appendix extends it with a parallel-computing primer angle.
- [[RVectorization]] — Matloff's primary performance recommendation for R code; bridges to the parallel R chapters.
- [[S3Classes]] — R's lightweight OO system introduced here; used implicitly throughout the parproc book's R examples.
- [[Snow]] — the R parallel package built upon in Ch1, Ch9, Ch11, Ch14; the `parallel` package listing in §C.15 is its successor API.
- [[DataFrame]] — R's native tabular structure; §C.13 gives the authoritative R-side definition (vs. [[DataFrame]]'s pandas-centric existing page).
- [[NormMatloff]] — author; this is the final appendix of his textbook.
- [[parproc-ch01-intro-parallel-processing]] — Ch1 uses Snow/R throughout; this appendix supplies the R primer that Ch1 assumes.
- [[parproc-ch14-statistics-data-mining]] — Ch14's K-means Snow implementation and FFT/R examples presuppose vectorization fluency.
- [[parproc-appB-matrix-algebra]] — preceding appendix; covers the math behind R's `%*%` / `solve()` / `eigen()` operators.

## Contradictions

- None. The [[DataFrame]] concept page already notes R's `data.frame` as the pandas inspiration; §C.13's R-side detail is additive. The existing [[Vectorization]] concept page covers CPU/GPU SIMD — a distinct sense from R's functional vectorization here; both senses now have dedicated pages.
