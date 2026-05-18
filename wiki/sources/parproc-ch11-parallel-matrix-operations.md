---
title: "ParProcBook Ch11: Introduction to Parallel Matrix Operations"
type: source
tags: [textbook, parallel-computing, matrix, linear-algebra, openmp, cuda]
date: 2026-05-17
source_file: raw/parproc-matloff.pdf
---

# ParProcBook Ch11: Introduction to Parallel Matrix Operations

Chapter 11 (book pp. 235–256, PDF pp. 255–276) of *Programming on Parallel Machines: GPU, Multicore, Clusters and More* by [[NormMatloff]] of [[UCDavis]]. The chapter surveys the full stack of parallel matrix algorithms: partitioned matrices as the unifying abstraction, [[FoxAlgorithm|Fox's algorithm]] for MPI-based [[MatrixMultiplication|matrix multiplication]], shared-memory multiplication in [[OpenMP]] and [[CUDA]] (including CUBLAS and Prof. Edgar's shared-memory tiling), R [[Snow]] and GPU interfaces for R; then matrix powers (graph connectedness, Fibonacci, matrix inversion via power series), solving linear systems ([[GaussianElimination|Gaussian elimination]] in CUDA and [[JacobiAlgorithm|Jacobi iteration]] in OpenMP and R/gputools), eigenvalue extraction via the [[PowerMethod|power method]] and CULA SVD, [[SparseMatrix|sparse matrices]] with the Compressed Sparse Row format, and a closing tour of libraries (CUBLAS, CUSP, CULA, ScalaPACK, PLAPACK, OpenBLAS).

## Summary

§11.1 frames the domain shift: modern parallel matrix problems involve thousands or millions of rows/columns, not the 3×3 textbook toys, and dense vs sparse matrices call for fundamentally different algorithms. §11.2 introduces [[PartitionedMatrix|partitioned matrices]] (block decomposition): A and B split into compatible blocks so that C = AB proceeds "as if the submatrices were numbers," a key algebraic fact that drives every subsequent algorithm. §11.3 develops parallel [[MatrixMultiplication|matrix multiplication]] in three settings: [[FoxAlgorithm|Fox's algorithm]] for the message-passing case (MPI nodes exchange blocks in a cyclic broadcast-and-shift pattern over $m = n/\sqrt{p}$ steps), the `#pragma omp parallel for` outer-loop approach for [[OpenMP]], the CUDA kernel assigning one thread per output element with a follow-on CUBLAS/shared-memory version attributed to Prof. Richard Edgar that achieves 500× speedup via tiling into GPU shared memory, and brief notes on R [[Snow]] (row-chunk tiling, §1.6.3.1 pattern) and R/gputools `gpuMatMult()`. §11.4 applies matrix powers to [[GraphConnectedness|graph connectedness]] (the adjacency matrix theorem: the (i,j) element of $A^r$ counts r-step paths, so connectivity reduces to computing R up to $A^{n-1}$), [[FibonacciNumbers|Fibonacci numbers]] (the 2×2 matrix recurrence), and [[MatrixInversion|matrix inversion]] via the power series $(I-C)^{-1} = I + C + C^2 + \ldots$, noting the repeated-squaring trick to compute $A^{32}$ in 5 multiplications. §11.5 covers solving $Ax = b$: sequential and parallel [[GaussianElimination|Gaussian elimination]] (reduced row echelon form, CUDA implementation using one thread per row in a single block with the pivot row in shared memory, limited to 512×512 or ~30×30 in 4K shared memory), and the [[JacobiAlgorithm|Jacobi iterative algorithm]] expressed as $x^{(k+1)} = D^{-1}(b - Ox^{(k)})$ with convergence guaranteed when diagonal dominance holds — parallelized in [[OpenMP]] (each thread owns a section of x, barrier after each iteration) and in R via gputools `gpumatmult`. §11.6 treats eigenvalue/eigenvector extraction: the [[PowerMethod|power method]] iterates $x^{(k)} = A^k x / \|A^k x\|$ to converge to the dominant eigenvector $v_1$; deflation ($B = A - \lambda_1 v_1 v_1'$) peels off subsequent eigenvalues; CULA provides SVD routines with a gputools interface. §11.7 covers [[SparseMatrix|sparse matrices]] in two categories — structured (tridiagonal, block patterns) and amorphous — with the Compressed Sparse Row (CSR) format: three arrays `avals`, `cols`, `rowplaces` encoding nonzero values, their column indices, and per-row start offsets. §11.8 catalogs libraries: CUBLAS (closed-source CUDA), CUSP (sparse), CULA (not NVIDIA), ScalaPACK, PLAPACK, OpenBLAS (OpenMP-backed, can replace R's BLAS for large-matrix speedups).

## Key Claims

- **Partitioned matrix multiplication is algebraically exact.** Submatrices of compatible size multiply "just like numbers": $C_{ij} = \sum_k A_{ik} B_{kj}$ where each term is a submatrix product. This is the algebraic foundation of every block-parallel matrix algorithm. (§11.2, p. 237, eq. 11.12).
- **Fox's algorithm performs cyclic broadcasts within block rows.** Each node computing $C_{ij}$ needs $\sum_{k=0}^{m-1} A_{i,(i+k) \bmod m} B_{(i+k) \bmod m, j}$ (eq. 11.15). Over $m$ steps: broadcast $A_{i,km}$ across row $i$, accumulate into $C_{ij}$, shift $B$ down by one row. Cannon's algorithm differs by rotating both rows and columns cyclically rather than broadcasting within rows. (§11.3.1, pp. 238–239).
- **The CUDA shared-memory tiling gives 500× speedup over a naive serial baseline.** Prof. Edgar's `MultiplyOptimise` kernel loads BLOCK_SIZE×BLOCK_SIZE submatrices of A and B into `__shared__` memory, each thread loads one element, `__syncthreads()` before and after the local multiply, looping across all submatrix pairs along the shared dimension. The baseline CUDA kernel (one thread per element, no shared memory) gives "a good speedup" but the shared-memory version extends it from 20× to 500×. (§11.3.2, pp. 240–243).
- **Graph connectivity reduces to computing matrix powers up to $A^{n-1}$.** Element (i,j) of $A^r$ counts r-step paths from i to j. A directed graph is connected iff every off-diagonal element of some $R^{(k)}$ among $R^{(1)}, \ldots, R^{(n-1)}$ is 1 (for undirected); $R^{(k)} = b(A^k)$ where $b(\cdot)$ booleanizes nonzero entries. (§11.4.1, pp. 243–245, Theorem 1).
- **Fibonacci numbers are computable via $A^{n-1}$ for $A = \bigl(\begin{smallmatrix}1&1\\1&0\end{smallmatrix}\bigr)$.** The recurrence $f_n = f_{n-1} + f_{n-2}$ expressed in matrix form gives $(f_{n+1}, f_n)^T = A^{n-1}(1,1)^T$. Parallel matrix multiplication thus accelerates Fibonacci computation. (§11.4.2, pp. 245–246).
- **Matrix inversion via power series requires the condition $\sum_{i,j} c_{ij}^2 < 1$.** $(I-C)^{-1} = I + C + C^2 + \ldots$; to invert A, set $C = I - dA$ for small enough $d$. Serial inversion is $O(n^3)$, same as multiplication, but multiplication parallelizes more effectively — hence the power-series approach may pay off in parallel contexts. (§11.4.3, p. 246).
- **Repeated squaring reduces $k$ multiplications to $\log_2 k$.** Computing $A^{32}$ sequentially takes 31 multiplications; squaring 5 times suffices. This trick applies to matrix powers for graph reachability, Fibonacci, and matrix inversion. (§11.4.4, p. 247).
- **Gaussian elimination in CUDA is limited to ~30×30 matrices under 4K shared memory.** Using one thread per row and one block (to avoid inter-block synchronization), the pivot row is stored in `__shared__` memory. With 512-thread block limit, $n \leq 512$; with 4K shared memory in single precision, $n \leq 30$. (§11.5.2, pp. 248–249).
- **The Jacobi algorithm converges when the matrix is diagonally dominant.** The iteration $x^{(k+1)} = D^{-1}(b - Ox^{(k)})$ (where D is the diagonal and O is A with diagonal zeroed) is parallelized by assigning each thread a section of the x vector; threads must broadcast their updated section after every iteration. (§11.5.3–11.5.4, pp. 249–251).
- **The power method converges to the dominant eigenvector of a symmetric matrix.** Iteration $x^{(k)} = A^k x / \|A^k x\|$ converges to the eigenvector $v_1$ for eigenvalue $\lambda_1$; deflation $B = A - \lambda_1 v_1 v_1'$ has eigenvalues $\lambda_2, \ldots, \lambda_n, 0$, enabling iterative extraction of further eigenpairs. (§11.6.1, pp. 252–253).
- **Compressed Sparse Row (CSR) stores three arrays: values, column indices, and row-start offsets.** For an m×n matrix with k nonzeros: `avals[k]` (row-major nonzero values), `cols[k]` (their column indices), `rowplaces[m+1]` (index into `avals` of the first nonzero in each row; last entry is k). Load balancing for sparse operations remains a challenge. (§11.7, p. 254).
- **OpenBLAS can replace R's built-in BLAS transparently.** Because OpenBLAS uses OpenMP internally, R users who swap in OpenBLAS automatically get parallelized large-matrix operations with no code changes. (§11.8, p. 255).

## Key Quotes

> *"These matrices are not those little 3×3 toys you worked with in your linear algebra class. In parallel processing applications of matrix algebra, our matrices can have thousands of rows and columns, or even larger."* — p. 235. Frames why parallel algorithms are needed.

> *"The key point is that multiplication still works if we pretend that those submatrices are numbers!"* — p. 237. The algebraic basis of partitioned matrix multiplication.

> *"Professor Edgar found that use of shared device memory resulted a huge improvement, extending the original speedup of 20X to 500X!"* — p. 243. The performance impact of shared-memory tiling in CUDA.

> *"This is Fox's algorithm. Cannon's algorithm is similar, except that it does cyclical rotation in both rows and columns."* — p. 239. Distinguishes Fox from Cannon.

> *"This algorithm is guaranteed to converge if each diagonal element of A is larger in absolute value than the sum of the absolute values of the other elements in its row."* — p. 250. Diagonal dominance as the convergence condition for Jacobi.

> *"R users can replace the built-in BLAS by OpenBLAS, thus automatically getting big speedups for large matrices."* — p. 255. Practical performance tip.

## Connections

- [[NormMatloff]] — author.
- [[UCDavis]] — author's institution.
- [[PartitionedMatrix]] — §11.2 core abstraction for all block-parallel algorithms.
- [[MatrixMultiplication]] — §11.3 primary operation; parallelized via Fox (MPI), OpenMP pragma, CUDA tiling.
- [[FoxAlgorithm]] — §11.3.1 MPI-based block matrix multiplication; new concept page.
- [[MatrixVectorMultiply]] — §11.3.3 notes the Snow row-chunk pattern from §1.6.3.1 extends directly to matrix-matrix products.
- [[GaussianElimination]] — §11.5.1–11.5.2; the existing stub page is now substantiated.
- [[JacobiAlgorithm]] — §11.5.3–11.5.5 iterative solver; new concept page.
- [[GraphConnectedness]] — §11.4.1 application of matrix powers; new concept page.
- [[FibonacciNumbers]] — §11.4.2 application of matrix powers; new concept page.
- [[MatrixInversion]] — §11.4.3 via power series; new concept page.
- [[PowerMethod]] — §11.6.1 dominant eigenvector extraction; new concept page.
- [[Eigenvalue]] — §11.6 subject; new concept page.
- [[Eigenvector]] — §11.6 subject; new concept page.
- [[SparseMatrix]] — §11.7 Compressed Sparse Row representation; new concept page.
- [[OpenMP]] — §11.3.2 matrix multiply, §11.5.4 Jacobi implementation.
- [[CUDA]] — §11.3.2 matrix multiply (Edgar tiling), §11.5.2 Gaussian elimination.
- [[MPI]] — §11.3.1 Fox's algorithm setting.
- [[Snow]] — §11.3.3 R matrix-matrix multiplication via row-chunk tiling.
- [[CUBLAS]] — §11.3.2 and §11.8; highly optimized CUDA matrix routines (closed-source).
- [[parproc-ch05-cuda-gpu-programming]] — CUDA memory hierarchy and CUBLAS library introduced in Ch5.
- [[parproc-ch08-introduction-to-mpi]] — MPI collectives and communicators used by Fox's algorithm.
- [[parproc-ch10-parallel-prefix-problem]] — preceding chapter; prefix scan is used in some matrix-related preprocessing but not directly invoked in Ch11.

## Contradictions

- **Jacobi convergence condition is sufficient, not necessary.** The chapter states convergence is guaranteed under diagonal dominance; the standard literature notes this is a sufficient condition and that Jacobi can converge for some non-diagonally-dominant systems. No contradiction with prior wiki content, but worth noting as a simplification.
- **"Singular value" equated to "eigenvalue" in footnote 1 (p. 253).** Matloff writes "The term *singular value* is a synonym for *eigenvalue*." This is an oversimplification: singular values of a matrix A are the square roots of the eigenvalues of $A^T A$, which coincide with eigenvalues only for symmetric positive semidefinite matrices. No prior wiki page makes this claim, so no contradiction, but the equation is imprecise.
- **No contradiction with [[MatrixVectorMultiply]].** The Snow row-chunk tiling pattern described in §11.3.3 is a direct extension of the matrix-vector pattern from Ch1/Ch2 and is consistent with the existing page.
