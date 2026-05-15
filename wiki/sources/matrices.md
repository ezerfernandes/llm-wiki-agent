---
title: "Matrices"
type: source
tags: [math, vectors-and-matrices]
date: 2026-05-10
source_file: raw/vectors-and-matrices/matrices.md
---

## Summary
A matrix is a rectangular array of [[types-of-numbers|real numbers]] arranged in rows and columns. A matrix with \\( m \\) rows and \\( n \\) columns is said to have dimensions \\( m \\times n \\), and is called an \\( m \\times n \\) matrix. For example, a \\( 3 \\times 2 \\) matrix has 3 rows and 2 columns. Each number appearing in a matrix is called an element. Elements are identified by two subscript indices: the first indicates the row and the second the column. Thus \\( a_{2,3} \\) denotes the element in the second row and third column. A matrix \\( A \\) of dimensions \\( m \\times n…

## Key Claims
- **Vectors and the zero matrix** — A matrix consisting of a single row is called a row [[vectors|vector]], and a matrix consisting of a single column is called a column vector.
- **Square matrices and special types** — A matrix is called square when its number of rows equals its number of columns, that is, when it has dimensions \\( n \\times n \\).
- **Transpose** — The transpose of a matrix \\( A \\) of dimensions \\( m \\times n \\), denoted \\( A^{\\mathrm{T}} \\), is the matrix of dimensions \\( n \\times m \\) obtained by interchanging the rows and columns of \\( A \\).
- **Additive inverse matrix** — The additive inverse of a matrix \\( A \\), denoted \\( -A \\), is the matrix obtained by negating every element of \\( A \\): each entry \\( a_{ij} \\) becomes \\( -a_{ij} \\).
- **Matrix addition and subtraction** — Two matrices can be added or subtracted only if they have the same dimensions.
- **Scalar multiplication** — Given a matrix \\( A = (a_{ij}) \\) of dimensions \\( m \\times n \\) and a real number \\( k \\), the scalar multiple \\( kA \\) is the \\( m \\times n \\) matrix whose element in position \\( (i,j) \\) is \\( k \\cdot a_{ij} \\).
- **Matrix multiplication** — Matrix multiplication is defined under a compatibility condition: the product \\( AB \\) is defined only when the number of columns of \\( A \\) equals the number of rows of \\( B \\).

## Key Quotes
> Source page: algebrica.org — see `source_file`.

## Connections
- [[types-of-numbers|TypesOfNumbers]] — real numbers
- [[groups|Groups]] — group
- [[vectors|Vectors]] — vector
- [[linear-combinations|LinearCombinations]] — linear combinations
- [[eigenvalues-and-eigenvectors|EigenvaluesAndEigenvectors]] — eigenvalues
- [[determinant-of-a-square-matrix|Determinant]] — determinant
- [[inverse-matrix|InverseMatrix]] — inverse matrix

## Contradictions
None.
