---
title: "S3 Classes (R)"
type: concept
tags: [r-language, object-oriented, polymorphism]
sources: [parproc-appC-r-quick-start]
last_updated: 2026-05-17
---

# S3 Classes

S3 is [[Rlanguage|R]]'s original and most widely used object-oriented system. An S3 object is simply an R [[RList|list]] with a `class` attribute set to a character string. S3 is informal — there is no formal class declaration — but it is sufficient for the majority of R programming and is the system underlying most base-R and CRAN functions.

## Mechanics

```r
j <- list(name="Joe", salary=55000, union=TRUE)
class(j) <- "employee"
```

`j` is now an S3 object of class `"employee"`. Its components are accessed normally via `$` or `[[]]`.

## Generic Dispatch

S3 uses *generic functions* — functions that look up the class attribute of their first argument and dispatch to a class-specific method named `generic.class`. For example:

```r
print.employee <- function(wrkr) {
    cat(wrkr$name, "\n")
    cat("salary", wrkr$salary, "\n")
    cat("union member", wrkr$union, "\n")
}
print(j)   # R finds print.employee and calls it
```

If no class-specific method exists, R falls back to the default method (e.g., `print.default`, which prints the list structure).

## Key Properties

- **No formal class definition required**: any list can be promoted to an S3 object by setting `class()`.
- **Single dispatch only**: dispatch is on the class of the *first* argument.
- **Method naming convention**: `generic.class` (e.g., `summary.lm`, `predict.glm`, `print.employee`).
- **S4 is the stricter alternative**: S4 requires formal class declarations and supports multiple dispatch, but S3 covers the vast majority of practical R OO code.

## Connections

- [[Rlanguage]] — the language.
- [[RList]] — S3 objects are lists with a class attribute.
- [[parproc-appC-r-quick-start]] — §C.10.3 introduces S3 with the `employee` example.
- [[RVectorization]] — R's functional style complements S3's lightweight OO.
