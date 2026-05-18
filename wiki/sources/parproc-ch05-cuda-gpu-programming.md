---
title: "ParProcBook Ch5: Introduction to GPU Programming with CUDA"
type: source
tags: [textbook, parallel-computing, cuda, gpu, simt]
date: 2026-05-17
source_file: raw/parproc-matloff.pdf
---

# ParProcBook Ch5: Introduction to GPU Programming with CUDA

Chapter 5 (book pp. 119–156, PDF pp. 139–176) of *Programming on Parallel Machines: GPU, Multicore, Clusters and More* by [[NormMatloff]] of [[UCDavis]]. A thirty-eight-page applied introduction to [[CUDA]] on [[NVIDIA]] GPUs, structured around five worked examples — row sums, mutual outlinks, prime-finder via Sieve of Eratosthenes, cumulative sums, and an adjacency-matrix transformation — used to motivate the [[SIMT]] hardware model, the [[Grid|grid]]/[[Block|block]]/[[Warp|warp]]/[[Thread|thread]] hierarchy, the multi-tier GPU [[GPUMemoryHierarchy|memory hierarchy]] (shared / global / registers / local / [[ConstantMemory|constant]] / [[TextureMemory|texture]]), [[KernelLaunch|kernel-launch]] syntax, host-device transfer mechanics, and intra-block ([[ThreadBarrier|`__syncthreads()`]]) vs inter-block ([[AtomicAdd|atomic operations]] / [[CudaThreadSynchronize|`cudaThreadSynchronize`]]) synchronization. Closes with a tour of "higher level" entries — [[CUBLAS]], [[Thrust]] (deferred to Ch6), [[CUFFT]] — plus four short topics: [[LoopUnrolling|loop unrolling]] via `#pragma unroll`, [[ShortVectors|short vectors]] (`int4`/`char2`), [[TrueCaching|true caching]] (programmer-managed [[SharedMemory|shared memory]] vs an automatic L1), and [[UnifiedMemory|unified memory]] (`managed`, hardware-assisted from [[NVIDIAPascal|Pascal]]).

## Summary

Ch5 is the first non-CPU chapter of the book — Ch1–Ch4 covered [[SharedMemoryArchitecture|shared-memory]] / [[MessagePassingArchitecture|message-passing]] / [[SIMD]] paradigms running on multicore PCs under [[OpenMP]] / [[Pthreads]] / [[MPI]]. Ch5 pivots to GPUs, which Matloff frames as *"easily programmable"* because they "now consist of multiprocessor elements that run under the familiar shared-memory threads model" — but with a critical twist: GPUs *"can run hundreds or thousands of threads at once"*, vs. the four-thread quad-core machines of Ch4. This concurrency level forces a radically different cost model.

The chapter opens (§5.1 Overview, §5.2 Terminology) by establishing the **host/device split** — `main()` runs on the CPU (host); kernels run on the GPU (device); threads are grouped into **blocks**; the totality of blocks is the **grid** — and naming [[NVIDIA]]'s hardware lineage: Tesla → Fermi → Kepler → Pascal (the discussion stays at the Tesla baseline).

**§5.3 Calculate Row Sums** is the canonical first program: a `__global__ void find1elt(int *m, int *rs, int n)` kernel that finds one row's sum given `int rownum = blockIdx.x`, plus a `main()` that does `cudaMalloc` / `cudaMemcpy(...HostToDevice)` / kernel launch via `find1elt<<<dimGrid,dimBlock>>>(dm,drs,n)` / `cudaThreadSynchronize()` / `cudaMemcpy(...DeviceToHost)` / `cudaFree`. The launch syntax — angle-brackets-with-three-elements `<<<grid,block>>>` — is the chapter's central new piece of C syntax. Key annotations: kernels are identified by `__global__ void`, helper device functions by `__device__`; kernels return `void`, communicating only through pointer arguments; kernel calls **do not block** (`cudaThreadSynchronize()` waits explicitly; `cudaMemcpy` blocks implicitly; two consecutive kernel calls have an implicit barrier between them); intra-block barrier is `__syncthreads()` but *"cannot be invoked... across blocks"*.

**§5.4 Understanding the Hardware Structure** is the chapter's spine.

- **§5.4.1 Processing Units** — a GPU is a set of [[StreamingMultiprocessor|streaming multiprocessors]] (SMs); each SM contains a set of [[StreamingProcessor|streaming processors]] (SPs, individual cores). *"You might say the GPU is a multi-multiprocessor machine."* Different SMs **cannot synchronize via barrier** — a deliberate independence that lets the hardware run faster. Word size 32 bits; double-precision via `float2`-style 64-bit types.

- **§5.4.2 Thread Operation** — the [[SIMT]] heart of the chapter. The hardware assigns one block to one SM (multiple blocks may share an SM) and then **divides each block into [[Warp|warps]] of 32 threads**. *"All the threads in a warp run the code in lockstep"* — same instruction fetch, same execute cycle, branches mask off divergent threads. This is the classical [[SIMD]] pattern; on GPUs it is called **single instruction, multiple thread (SIMT)**. [[ThreadDivergence|Thread divergence]] — when threads in the **same warp** take different branches of an if/else — is *"a performance killer"* because the divergent paths serialize; threads in the same block but **different warps** can diverge freely. The **"OS in hardware"** subsection (§5.4.2.3) frames the SM as a hardware time-sharer: warps take fixed-length timeslices like processes, and when a warp blocks on a long global-memory access the SM schedules a different warp — exactly analogous to an OS suspending an I/O-blocked process — except *"each warp has its own set of registers, so a context switch does very little saving and restoring."* This **latency hiding via overcommitted warps** is the central performance lever: *"CUDA programmers typically employ a large number of threads, each of which does only a small amount of work — quite a contrast to something like OpenMP, where coarser granularity is generally needed."*

- **§5.4.3 Memory Structure** — the GPU memory hierarchy, presented as two comparison tables:

  | type | shared | global |
  |---|---|---|
  | scope | global to block | global to app |
  | size | small | large |
  | location | on-chip | off-chip |
  | speed | blinding | molasses |
  | lifetime | kernel | application |
  | host access? | no | yes |
  | cached? | no (Tesla) | no (Tesla) |

  Shared memory is *"partitioned among all blocks in an SM... 16K bytes per SM on the lower models"*; declared via `__shared__ int abcsharedmem[100]` inside the kernel, or **dynamically allocated** in the launch with `extern __shared__ int sv[]` plus `kernel<<<grid,block,vsize>>>(...)`. The third launch argument is the shared-memory byte count. **Consistency**: shared memory is sequential within a thread but *"relaxed among threads in a block"* — a thread's write is not visible to other threads until `__syncthreads()`. Global memory is shared by the entire application, persistent across kernel calls, accessible from the host, but takes *"hundreds of clock cycles per access"*. **Key takeaway**: *"shared memory is used essentially as a programmer-managed cache"* — copy from global to shared, compute, copy back.

  Hardware mitigates global-memory cost via two mechanisms:

  - **[[LatencyHiding|Latency hiding]]** (§5.4.3.2): when a warp issues a slow global-memory access, the SM schedules another warp. This is the OS-in-hardware story applied to memory I/O.
  - **[[MemoryCoalescing|Coalescing]]** (§5.4.3.2): if a half-warp's threads access consecutive words, the hardware merges up to 32-word reads/writes into one transaction *"because the memory is low-order interleaved"*. The programmer takes advantage by careful array layout and padding.

  **Shared-memory bank conflicts** (§5.4.3.3): shared memory is split into 8 (Tesla) or 32 (newer) low-order-interleaved banks. Best half-warp access is to **different banks**; **broadcast** (all threads read the same word in the same bank) is exception-free.

  Other memory types (§5.4.3.5):

  | type | registers | local | constant | texture |
  |---|---|---|---|---|
  | scope | single thread | single thread | global to app | global to app |
  | location | device | device | host+device cache | host+device cache |
  | speed | fast | molasses | fast if cache hit | fast if cache hit |
  | lifetime | kernel | kernel | application | application |
  | host access? | no | no | yes | yes |
  | device access? | read/write | read/write | read | read |

  **Registers** are abundant per SM (more than CPU). **Local memory** is misleadingly named — it lives in *global* memory, allocated by the compiler when a thread's variables don't fit in registers ([[RegisterSpill|register spill]]). **[[ConstantMemory|Constant memory]]**: read-only from the device, read/write from the host, 64K, **cached on-chip** — declared `__constant__ int x;` and populated via `cudaMemcpyToSymbol("x",&y,sizeof(int))`. *"Note again that the name Constant refers to the fact that device code cannot change it. But host code certainly can change it between kernel calls."* — useful for iterative algorithms with per-iteration parameter updates. **[[TextureMemory|Texture memory]]** is similar but with **two-dimensional caching**: `a[i][j]` and `a[i+1][j]` are far apart in linear global memory but may share a cache line in texture caching.

  **Host-device transfer performance** (§5.4.3.4): `cudaMallocHost()` instead of `malloc()` allocates page-locked memory the OS won't swap out, enabling DMA — *"makes cudaMemcpy() twice as fast."*

- **§5.4.4 Threads Hierarchy** — the four-level CUDA hierarchy: grid → blocks → threads → warps. Each block has 2D coordinates `blockIdx.x`/`blockIdx.y`; each thread has 3D coordinates `threadIdx.x/y/z`; `gridDim` and `blockDim` (also `dim3`) expose grid/block sizes. **Crucially**: *"the 'coordinates' of a block within the grid, and of a thread within a block, are merely abstractions"* — no physical 2D/3D arrangement in the hardware; the multi-D indexing is a programmer convenience (e.g. **tiling** a matrix into sub-block tiles).

- **§5.4.5 What's NOT There** — no C library (special versions like `__sin()`), no function call stack (functions are inlined), no function pointers.

**§5.5 Synchronization, Within and Between Blocks** — `__syncthreads()` is the intra-block barrier. *"Threads across blocks cannot sync with each other in this manner."* For inter-block coordination CUDA provides **[[AtomicOperation|atomic operations]]** without pre-emption: `atomicAdd`, `atomicExch`, `atomicCAS`, `atomicMin`, `atomicMax`, `atomicAnd`, `atomicOr`. Locks can be hand-rolled via `atomicCAS`/`atomicExch` (`-arch=sm_11` required at compile time). A barrier built from atomics has microsecond-scale overhead, so for real inter-block synchronization the usual idiom is to **return to the host** between kernel calls — `cudaThreadSynchronize()` then re-launch. *"If you have a small problem, maybe you can get satisfactory performance by using just one block, thus enabling the use of `__syncthreads()`. You'll have to use a larger granularity, i.e. more work assigned to each thread. But using just one block means you're using only one SM, thus only a fraction of the potential power of the GPU."*

**§5.6 Blocks/Threads Tradeoff** — the chapter's design-decision summary:

- Each block is bound to one SM for its lifetime; the programmer has no control over which.
- Limits (Tesla): 512 threads/block, 786 threads/SM (so e.g. 2 blocks × 384 threads or 3 blocks × 256 threads).
- Block size should be **≥ 32 and a multiple of 32** (warp size); fewer than 32 wastes SP cycles.
- Larger blocks → more shared memory per block; smaller blocks → less per-block barrier cost.
- Want **≥ #SMs** blocks (use the full GPU); want **many warps per SM** (for latency hiding); want **few threads per block in same warp doing divergent work** (reduce [[ThreadDivergence]]).
- *"A commonly-cited rule of thumb is to have between 128 and 256 threads per block."*

**§5.7 Hardware, Installation, Compilation, Debugging** — install the CUDA toolkit from [[NVIDIA]], compile `.cu` files with `nvcc -g -G x.cu` (the `-g -G` flags enable host- and device-side debugging), set `LD_LIBRARY_PATH`. Query device limits via `cudaDeviceProp Props; cudaGetDeviceProperties(&Props, 0);` printing `Props.sharedMemPerBlock`, `maxThreadsPerBlock`, `maxGridSize[0]`, `totalConstMem`. Old debugging: `-deviceemu` (removed at 3.2); current: `cuda-gdb` (X11 must be off on Unix).

**§5.8 Improving Row Sums** — modify to compute **column** sums, on the same row-major-stored matrix. With column sums, threads in a half-warp march down adjoining columns in lockstep, hitting adjacent words → coalescing wins. Timings show `cs 20000` slightly faster than `rs 20000`. The headline number: the CPU-only column-sum version takes **62 seconds** on n=20000 vs the GPU's **~4.5 seconds** — *"No wonder people talk of CUDA in terms like 'a supercomputer on our desktop'"* — and that's **without** optimizing memory coalescing or bank conflicts. Caveat: *"this is an 'embarrassingly parallel' application... in many applications we may have to settle for a much more modest increase, and work harder to get it."*

**§5.9 Finding the Mean Number of Mutual Outlinks** — same problem as Ch2 §2.4.3 / Ch4 §4.12, now in CUDA. Each thread `me = blockIdx.x * blockDim.x + threadIdx.x` handles every `totth`-th `i` (`for (i = me; i < n; i += totth)`), inner loop computes the dot product, **`atomicAdd(tot, sum)`** aggregates across blocks. Demonstrates the global-atomic-as-inter-block-reduction idiom.

**§5.10 Finding Prime Numbers** — Sieve of Eratosthenes in **shared memory** (one block, `n ≤ 4000`). Two `__device__` helpers, `initsp` and `cpytoglb`, surround the main kernel. Three design refinements vs the Ch1 sieve: (1) **partition the multiples of each prime `m` across the threads**, not the primes themselves across the threads — *"the thinking here is that the second version will be more amenable to lockstep execution, thus causing less thread divergence"*. (2) Stage everything in shared memory; only copy the final array to global memory at the end. (3) Variable-length `extern __shared__ int sprimes[]` allocated at launch. Caveats: single block → only one SM in use → fraction of the GPU; 16K shared-memory limit caps `n` near 4000.

**§5.11 Finding Cumulative Sums** — prefix scan (general case deferred to Ch10). Algorithm: each thread computes the cumulative sum of its own contiguous chunk; `__syncthreads()`; thread `i>0` adds the sum of all preceding chunks' high values to every element of its chunk. One block; explicit disclaimers ("multiple blocks", "shared memory", "staggered access for bank balance" listed as improvements not made).

**§5.12 When Is Shared Memory Advantageous** — *"Shared memory only helps if we are doing multiple accesses to the data."* Single-read-single-write transfers are net-negative because of the copy overhead.

**§5.13 Transforming an Adjacency Matrix** — same problem as Ch4 §4.13. **Two-kernel design**: `tgkernel1` counts the 1s in each row and stores compacted indices back into the adjacency matrix; the host runs a serial `cumulcounts` (prefix sum of counts → starts); `tgkernel2` writes each thread's `(row, col)` pairs into the output edge list at its `starts[me]` offset. The pattern — partial computation in kernel 1, serial scan on host, finalization in kernel 2 — is the CUDA generalization of Ch4's two-phase `omp single`-bracketed approach. **`-lrt`** link flag needed for `clock_gettime` C++ linkage.

**§5.14 Error Checking** — every CUDA call returns `cudaError_t`; print errors via `cudaGetErrorString(err)`. Kernel invocations don't return an error code directly; use `cudaError_t err = cudaGetLastError()` immediately after. `cutilSafeCall()` wraps the boilerplate. CUBLAS calls return `cublasStatus`.

**§5.15 [[LoopUnrolling|Loop Unrolling]]** — same uniprocessor optimization that eliminates branches. The CUDA compiler exposes `#pragma unroll k` to suggest a `k`-fold unroll (`k=1` disables). Particularly powerful on GPUs because *"if x is local to this function, then unrolling will allow the compiler to store it in a register."*

**§5.16 [[ShortVectors|Short Vectors]]** — types `int2`, `int4`, `char2`, `uint4`, etc. — *"a set of four unsigned ints"* treated as a single word for access and instruction purposes. Potential 4× reduction in memory-access time by packing four contiguous words.

**§5.17 Newer Generations** — two convenience features beyond raw "bigger and faster":

- **§5.17.1 [[TrueCaching|True Caching]]** — on-chip memory can now be apportioned between programmer-managed [[SharedMemory|shared memory]] and an **automatic L1 cache**. *"This makes less work for the programmer, at a possible cost of reduced performance."* Frames shared memory historically as *"in essence a programmer-managed cache"*; the true cache is the automation of that pattern.
- **§5.17.2 [[UnifiedMemory|Unified Memory]]** — *"under the Unified Memory, one can declare some data in one's code to be `managed`, and CUDA will automatically move the data to the proper processor, be it CPU or GPU."* Starting with **[[NVIDIAPascal|Pascal]]**, *"there is hardware assist for this, using something similar to virtual memory page tables."* Programmer convenience only — hand-coded `cudaMemcpy()` may still be much more efficient.

**§5.18 CUDA from a Higher Level** — wrapper libraries with the caveat *"each call to a function in these packages involves a CUDA kernel call — with the associated overhead"*.

- **§5.18.1 [[CUBLAS]]** — GPU-accelerated BLAS callable from straight C. Worked example: re-do row sums as **post-multiplying A by an all-ones column vector**, using `cublasSgemv('n', n, n, 1.0, dm, n, drs, 1, 0.0, drs, 1)`. **CUBLAS assumes FORTRAN-style column-major** matrix layout (vs C row-major); transposition or column-major fill on the host is required. Boilerplate: `cublasInit()` / `cublasAlloc` / `cublasSetMatrix` / `cublasSetVector` / `cublasSgemv` / `cublasGetVector` / `cublasFree` / `cublasShutdown`. Compile with `-lcublas`.
- **§5.18.2 [[Thrust]]** — *"usable not only with CUDA but also general OpenMP code"*. Deferred in full to Ch6.
- **§5.18.3 [[CUFFT]]** — *"does for the Fast Fourier Transform what CUBLAS does for linear algebra."*

**§5.19 Other CUDA Examples** — forward pointers: Prof. Richard Edgar's shared-memory matrix-multiply (§11.3.2.2), odd/even transposition sort (§12.3.3), Gaussian elimination for linear systems (§11.5.1).

## Key Claims

- **GPUs run hundreds-to-thousands of threads simultaneously.** *"Unlike a multicore machine, with the ability to run just a few threads at one time, e.g. four threads on a quad core machine, GPUs can run hundreds or thousands of threads at once."* (§5.1, p. 119). This concurrency level — not raw clock speed — is the GPU's structural advantage.
- **CUDA = C extension; OpenCL is the cross-vendor competitor; OpenACC is also alive but less used.** *"NVIDIA has developed the CUDA language as a vehicle for programming on their GPUs... OpenCL... It too is a slight extension of C, and it aims to provide a uniform interface that works with multicore machines in addition to GPUs."* (§5.1, p. 120).
- **Host/device terminology.** Host = CPU; device = GPU. A **kernel** is a host-called function that runs on the device. The total set of threads is the **grid**, divided into **blocks**.
- **Kernel launch syntax.** `kernel<<<dimGrid, dimBlock>>>(args)`. Optional third argument is dynamic shared-memory bytes.
- **Function-qualifier triangle.** `__global__ void` = kernel (host-called, device-run, void return). `__device__` = device-only helper (device-called, device-run, can return values). Plain function = host-only.
- **Kernel calls do not block.** The host returns immediately. `cudaThreadSynchronize()` is the explicit host-side barrier; `cudaMemcpy()` blocks implicitly; two sequential kernel calls have an **implicit barrier** between them.
- **`__syncthreads()` is intra-block only.** *"This can only be invoked by threads within a block, not across blocks. In other words, this is barrier synchronization within blocks."* (§5.3, p. 123).
- **Each block is assigned to one SM for the lifetime of the kernel.** The programmer has no control over which SM.
- **The block-to-SM independence is a feature, not a bug.** *"This means that the hardware can run faster. So, if the CUDA application programmer can write his/her algorithm so as to have certain independent chunks, and those chunks can be assigned to different SMs... then that's a 'win.'"* (§5.4.1, p. 124).
- **[[SIMT]] vs [[SIMD]].** *"All the threads in a warp run the code in lockstep. During the machine instruction fetch cycle, the same instruction will be fetched for all of the threads in the warp. Then in the execution cycle, each thread will either execute that particular instruction or execute nothing... This is the classical single instruction, multiple data (SIMD) pattern... here it is called single instruction, multiple thread (SIMT)."* (§5.4.2.1, p. 125).
- **Warp size is 32 threads on NVIDIA hardware.** Block sizes should be multiples of 32.
- **[[ThreadDivergence|Thread divergence]] is a performance killer — but only within a warp.** *"If some threads in a warp take the 'then' branch and others go in the 'else' direction, they cannot operate in lockstep. That means that some threads must wait while others execute... a situation called thread divergence... 'performance killer.' (On the other hand, threads in the same block but in different warps can diverge with no problem.)"* (§5.4.2.2, p. 125).
- **The SM is "an OS in hardware".** Warps run on fixed-length timeslices; when one warp blocks on memory, the SM schedules another. Context switches are nearly free because *"each warp has its own set of registers."* (§5.4.2.3, pp. 125–126).
- **CUDA's granularity advice is the opposite of OpenMP's.** *"CUDA programmers typically employ a large number of threads, each of which does only a small amount of work — again, quite a contrast to something like OpenMP, where coarser granularity is generally needed."* (§5.4.2.3, p. 126).
- **Shared memory is small (16K/SM on Tesla) and on-chip; global is large and off-chip.** Shared is **divvied among the blocks on an SM** — 4 blocks per SM means 4K shared each.
- **Shared memory is a programmer-managed cache.** *"The key implication is that shared memory is used essentially as a programmer-managed cache. Data will start out in global memory, but if a variable is to be accessed multiple times by the GPU code, it's probably better for the programmer to write code that copies it to shared memory, and then access the copy instead of the original."* (§5.4.3.1, p. 127).
- **Shared-memory consistency is relaxed across threads, sequential within a thread.** *"A write by one thread is not guaranteed to be visible to the others in a block until `__syncthreads()` is called."* (§5.4.3.1, p. 128). Writes are visible to the **writing** thread without `__syncthreads()`.
- **Shared memory can be allocated dynamically at launch.** `extern __shared__ int sv[]` plus `kernel<<<grid,block,vsize>>>(...)`. Only one such region per kernel; multiple `extern __shared__` declarations all alias the same buffer.
- **Global memory access is hundreds of clock cycles.** Mitigated by **latency hiding** (warp swap) and **coalescing** (merging consecutive-word accesses in a half-warp into one transaction).
- **[[MemoryCoalescing|Coalescing]] requires consecutive-word access patterns within a half-warp.** Newer GPUs relax to more general patterns. The programmer can promote coalescing via array layout and padding.
- **Shared memory is banked (8 on Tesla, 32 on newer).** Best access pattern: half-warp threads hit different banks. **Broadcast** (all reading the same word) is exception-free.
- **Page-locked host memory doubles transfer speed.** *"This sets up page-locked memory, meaning that it cannot be swapped out by the OS' virtual memory system. This allows the use of DMA hardware to do the memory copy, said to make `cudaMemcpy()` twice as fast."* (§5.4.3.4, p. 131).
- **Constant memory is host-write, device-read, 64K, cached.** Declared `__constant__`; written from host via `cudaMemcpyToSymbol`. Useful for per-iteration parameters in iterative kernels.
- **Texture memory is similar but with 2D caching.** `a[i][j]` and `a[i+1][j]` may share a cache line — useful for image/stencil access patterns.
- **Local memory is global memory in disguise.** Compiler-allocated overflow store for per-thread variables that don't fit in registers ([[RegisterSpill|register spill]]).
- **Grid is at most 2D, block is at most 3D, but neither corresponds to physical hardware.** *"The 'coordinates' of a block within the grid, and of a thread within a block, are merely abstractions... But this does not correspond to any physical arrangement in the hardware."* (§5.4.4, p. 134). They're indexing conveniences for 2D/3D problems.
- **What's NOT in CUDA C.** No host C library (use `__sin()` etc.); no call stack (functions inlined); no function pointers (§5.4.5).
- **Inter-block synchronization is hard.** The two real options are (1) **atomic ops** (`atomicAdd`, `atomicCAS`, etc., available on global and shared) — usable to roll a lock, but barriers built this way have microsecond-scale overhead — or (2) **return to host between kernels** — `cudaThreadSynchronize()` and re-launch. *"Though a barrier could in principle be constructed from the atomic operations, its overhead would be quite high."* (§5.5, p. 136).
- **Block-size rule of thumb: 128–256, multiple of 32, ≥ #SMs total blocks.** Other constraints: shared memory pressure → larger blocks; barrier cost → smaller blocks; thread divergence concentration → smaller blocks. *"A commonly-cited rule of thumb is to have between 128 and 256 threads per block."* (§5.6, p. 137). Tesla limit 512/block, 786/SM.
- **Compile with `nvcc -g -G x.cu`.** `.cu` is the file extension; `-g` debug host code, `-G` debug device code. `LD_LIBRARY_PATH` must include CUDA lib dir on Linux.
- **`cuda-gdb` is the modern device debugger.** Old `-deviceemu` removed at CUDA 3.2; on Unix `cuda-gdb` requires X11 off.
- **Embarrassingly parallel GPU speedup over CPU is dramatic.** Column-sum on n=20000: CPU 62 s, GPU ~4.5 s — even without optimizing coalescing or bank conflicts. *"No wonder people talk of CUDA in terms like 'a supercomputer on our desktop.'"* (§5.8, p. 140). The chapter explicitly warns that most applications are **not** embarrassingly parallel and yield more modest gains.
- **Loop unrolling is a register-allocation win on GPUs.** *"If x is local to this function, then unrolling will allow the compiler to store it in a register."* `#pragma unroll k` — `k=1` disables. (§5.15, p. 151).
- **Short vectors (int4, char2, ...) can give 4× memory bandwidth.** *"A short vector can be treated as a single word in terms of memory access and GPU instructions. It may be possible to reduce time by a factor of 4."* (§5.16, p. 152).
- **True caching trades programmer effort for performance.** Newer GPUs split on-chip memory between [[SharedMemory|shared memory]] and an automatic L1 cache. *"This makes less work for the programmer, at a possible cost of reduced performance."* (§5.17.1, p. 152).
- **Unified memory automates host-device transfer.** *"Under the Unified Memory, one can declare some data in one's code to be `managed`, and CUDA will automatically move the data to the proper processor, be it CPU or GPU."* (§5.17.2, p. 152). Hardware assistance starts at [[NVIDIAPascal|Pascal]] via VM-page-table mechanisms. *"Again, this is for the convenience of the programmer. Hand coding of the memory-to-memory transfers may be much more efficient."*
- **CUBLAS = GPU BLAS, FORTRAN-style column-major.** Callable from C. Mixed CUDA+CUBLAS must use `nvcc`; pure CUBLAS can use `gcc -lcublas`. Note the column-major convention — major source of programmer error.
- **CUFFT = GPU FFT.** Same wrapper-library pattern as CUBLAS.
- **Thrust spans CUDA and OpenMP.** *"The Thrust library is usable not only with CUDA but also to general OpenMP code."* (§5.18.2, p. 155). Treated in Ch6 of the book.
- **Wrapper libraries add kernel-call overhead.** *"Each call to a function in these packages involves a CUDA kernel call — with the associated overhead."* Highly optimized for their target operations, but *"will not generally give you the fastest possible code for any given CUDA application."* (§5.18, p. 153).

## Key Quotes

> *"Even if you don't play video games, you can be grateful to the game players, as their numbers have given rise to a class of highly powerful parallel processing devices — graphics processing units (GPUs). Yes, you program right on the video card in your computer, even though your program may have nothing to do with graphics or games."* — §5, p. 119. The chapter's hook.

> *"Unlike a multicore machine, with the ability to run just a few threads at one time, e.g. four threads on a quad core machine, GPUs can run hundreds or thousands of threads at once."* — §5.1, p. 119. The defining contrast with Ch4 OpenMP.

> *"You might say the GPU is a multi-multiprocessor machine."* — §5.4.1, p. 124. The SM/SP hierarchy in one line.

> *"Two threads located in different SMs cannot synchronize with each other in the barrier sense. Though this sounds like a negative at first, it is actually a great advantage, as the independence of threads in separate SMs means that the hardware can run faster."* — §5.4.1, p. 124. The structural reason inter-block sync is hard.

> *"All the threads in a warp run the code in lockstep. During the machine instruction fetch cycle, the same instruction will be fetched for all of the threads in the warp. Then in the execution cycle, each thread will either execute that particular instruction or execute nothing... This is the classical single instruction, multiple data (SIMD) pattern used in some early special-purpose computers such as the ILLIAC; here it is called single instruction, multiple thread (SIMT)."* — §5.4.2.1, p. 125. The SIMT definition.

> *"If some threads in a warp take the 'then' branch and others go in the 'else' direction, they cannot operate in lockstep. That means that some threads must wait while others execute. This renders the code at that point somewhat serial rather than parallel, a situation called thread divergence. As one CUDA Web tutorial points out, this can be a 'performance killer.' (On the other hand, threads in the same block but in different warps can diverge with no problem.)"* — §5.4.2.2, p. 125. The thread-divergence canonical statement.

> *"Each warp has its own set of registers, so a context switch does very little saving and restoring of context, quite a contrast to the OS case. Moreover, as noted above, the long latency of global memory may be solvable by having a lot of threads that the hardware can timeshare to hide that latency."* — §5.4.2.3, p. 126. Latency hiding rationale.

> *"For these reasons, CUDA programmers typically employ a large number of threads, each of which does only a small amount of work — again, quite a contrast to something like OpenMP, where coarser granularity is generally needed."* — §5.4.2.3, p. 126. The granularity flip.

> *"The key implication is that shared memory is used essentially as a programmer-managed cache."* — §5.4.3.1, p. 127. The shared-memory thesis in one line.

> *"Shared memory consistency... is sequential within a thread, but relaxed among threads in a block: A write by one thread is not guaranteed to be visible to the others in a block until `__syncthreads()` is called."* — §5.4.3.1, p. 128. The consistency model.

> *"As noted, the latency for global memory is quite high, on the order of hundreds of clock cycles. However, the hardware attempts to ameliorate this problem in a couple of ways."* — §5.4.3.2, p. 130. Setting up the latency-hiding + coalescing story.

> *"This sets up page-locked memory... This allows the use of DMA hardware to do the memory copy, said to make `cudaMemcpy()` twice as fast."* — §5.4.3.4, p. 131. The `cudaMallocHost` optimization.

> *"The 'coordinates' of a block within the grid, and of a thread within a block, are merely abstractions. If for instance one is programming computation of heat flow across a two-dimensional slab, the programmer may find it clearer to use two-dimensional IDs for the threads. But this does not correspond to any physical arrangement in the hardware."* — §5.4.4, p. 134. Demystifying the 2D/3D indexing.

> *"Threads across blocks cannot sync with each other in this manner."* — §5.5, p. 135. The fundamental block-isolation rule.

> *"Though a barrier could in principle be constructed from the atomic operations, its overhead would be quite high... implementing a barrier in this manner would not be much faster than attaining interblock synchronization by returning to the host and calling `cudaThreadSynchronize()` there."* — §5.5, p. 136. Why inter-block sync drives kernel granularity.

> *"A commonly-cited rule of thumb is to have between 128 and 256 threads per block."* — §5.6, p. 137. The block-size headline.

> *"Very impressive! No wonder people talk of CUDA in terms like 'a supercomputer on our desktop.' And remember, this includes the time to copy the matrix from the host to the device (and to copy the output array back). And we didn't even try to optimize thread configuration, memory coalescing and bank usage..."* — §5.8, p. 140. The headline speedup quote.

> *"On the other hand, remember that this is an 'embarrassingly parallel' application, and in many applications we may have to settle for a much more modest increase, and work harder to get it."* — §5.8, p. 140. The immediate disclaimer.

> *"Shared memory only helps if we are doing multiple accesses to the data. If for instance our code does a single read and a single write to an element of an array, then transferring it back and forth between global and shared memory isn't worthwhile."* — §5.12, p. 147. The reuse-or-don't-bother rule.

> *"Each call to a function in these packages involves a CUDA kernel call — with the associated overhead."* — §5.18, p. 153. The wrapper-library caveat.

## Connections

- [[NormMatloff]] — author.
- [[UCDavis]] — author's institution.
- [[parproc-ch01-intro-parallel-processing]] — Ch1 surveyed [[SharedMemoryArchitecture|shared memory]] / [[MessagePassingArchitecture|message passing]] / [[SIMD]] paradigms on CPUs; Ch5 introduces a fourth substrate (the GPU) that is **all three at once** — shared memory within a block, message-passing-by-host-roundtrip across blocks, SIMD within a warp.
- [[parproc-ch02-recurring-performance-issues]] — Ch2's [[LoadBalancing]] / [[StaticTaskAssignment]] / [[EmbarrassinglyParallel]] / [[Latency]] vs [[Bandwidth]] vocabulary all reappear in Ch5: §5.9 mutual outlinks reuses Ch2 §2.4.3's randomized static assignment; §5.8 names its 14× speedup as embarrassingly parallel; latency hiding via overcommitted warps is Ch2's [[Latency]] discussion operationalized.
- [[parproc-ch03-shared-memory-parallelism]] — Ch3's [[MemoryInterleaving|low-order interleaving]] is the hardware basis for [[MemoryCoalescing|coalescing]] (§5.4.3.2 explicitly cites §3.2.1); [[BankConflict|bank conflicts]] from §3.2.2 reappear as shared-memory banking (§5.4.3.3); [[MemoryConsistency|relaxed consistency]] from §3.6 underlies the `__syncthreads()` rule (§5.4.3.1); [[CacheCoherency|coherency]] arguments are bypassed in CUDA because shared memory isn't cached on Tesla.
- [[parproc-ch04-introduction-to-openmp]] — Ch5 explicitly contrasts CUDA's many-small-thread granularity with Ch4's OpenMP's coarse-thread model; §5.9 (mutual outlinks) and §5.13 (adjacency-matrix transform) are direct CUDA ports of Ch4 §4.12 / §4.13; `__syncthreads()` is the CUDA analog of [[Barrier|`#pragma omp barrier`]]; `atomicAdd` is the CUDA analog of [[AtomicClause|`#pragma omp atomic`]]; no CUDA equivalent for `#pragma omp critical` (no general mutex, only atomics).
- [[CUDA]] — substantially fleshed out by this ingest with hardware model, memory hierarchy, kernel-launch syntax, synchronization rules, compilation toolchain, and wrapper-library pointers.
- [[NVIDIA]] — primary vendor; updated with Tesla baseline + Pascal Unified Memory note.
- [[GPU]] — the hardware category; the chapter is the long-form hardware tour the [[GPU]] page should reference.
- [[GPUMemoryHierarchy]] — the existing concept page already covers SRAM/HBM bandwidth; Ch5 adds the CUDA-specific tier names (shared / global / constant / texture / registers / local) and the programmer-managed-cache discipline.
- [[SIMT]] — new concept page; the GPU-specific refinement of [[SIMD]].
- [[ThreadDivergence]] — new concept page; performance killer within a warp.
- [[Warp]] — new concept page; 32-thread SIMT execution unit.
- [[Grid]] — new concept page; totality of CUDA threads for an application.
- [[Block]] — new concept page; the SM-assignment unit, 1–512 threads.
- [[KernelLaunch]] — new concept page; the `<<<grid,block,shmem>>>` syntax + the async semantics.
- [[GlobalMemory]] — new concept page; off-chip, large, slow, app-lifetime.
- [[SharedMemory]] — new concept page; on-chip, small, fast, block-scope, kernel-lifetime.
- [[ConstantMemory]] — new concept page; 64K, host-write/device-read, cached.
- [[TextureMemory]] — new concept page; 2D-cached read-only memory.
- [[UnifiedMemory]] — new concept page; `managed` data with auto-migration since Pascal.
- [[MemoryCoalescing]] — new concept page; the half-warp consecutive-word access optimization.
- [[LoopUnrolling]] — new concept page; `#pragma unroll k` for register allocation + branch elimination.
- [[CUBLAS]] — new concept page; GPU BLAS, column-major.
- [[CUFFT]] — new concept page; GPU FFT.
- [[Thrust]] — new concept page; CUDA+OpenMP wrapper library (Ch6).
- [[StreamingMultiprocessor]] / [[StreamingProcessor]] — the hardware unit hierarchy (referenced; pages not created in this ingest).
- [[Multicore]] — Ch4's substrate; the GPU is reframed in §5.1 as "multi-multiprocessor."
- [[FalseSharing]] — not central in Ch5 (no cross-thread cache lines on Tesla shared memory) but the analogous concern is shared-memory bank conflicts.
- [[ParallelComputing]] — overarching domain.
- [[SharedMemoryArchitecture]] — the CUDA shared-memory model is its on-chip realization at block scope.
- [[Barrier]] — `__syncthreads()` is CUDA's intra-block barrier; the inter-block case has no direct equivalent and falls back to host-roundtrip.

## Contradictions

- **No contradictions with prior wiki content.** Ch5 extends rather than overrides Ch1–Ch4: it introduces a new substrate (GPU) and a new programming model (CUDA / SIMT), but its [[LoadBalancing]] / [[Latency]] / [[MemoryInterleaving]] / [[BankConflict]] / [[MemoryConsistency]] references are consistent with their established Ch2/Ch3 treatment.
- **Internal tension with [[GPU]] page's "memory transfers are slow" thesis.** [[GPU]] (sourced from D2L) warns at length about host↔device transfer cost. Ch5 §5.17.2 [[UnifiedMemory|Unified Memory]] introduces `managed` data that hides those transfers — but the chapter explicitly notes *"hand coding of the memory-to-memory transfers may be much more efficient"*. So Unified Memory is a convenience-for-correctness tool, not a performance escape hatch. Consistent with the [[GPU]] page rather than contradictory.
- **Tesla-baseline caveats.** Several numbers are Tesla-specific (16K shared/SM; 8 banks; 512 threads/block; 786 threads/SM; warp size 32). Newer architectures relax most of these. The 32-thread warp size persists across Fermi/Kepler/Pascal/Volta/Ampere/Hopper. The chapter is explicit that *"unless otherwise stated, all statements here refer to Tesla, keeping things at the basic level"* (§5.1, p. 120) — readers extrapolating to modern hardware should consult NVIDIA's current programming guide.
- **Refines [[GPUMemoryHierarchy]] without contradicting it.** That page (sourced from [[2205.14135-flashattention]]) gives A100 SRAM/HBM bandwidth numbers. Ch5 adds the **CUDA-tier-name** layer (shared = on-chip programmer-managed; global = HBM; constant = 64K cached; texture = 2D-cached; local = global-in-disguise; registers = per-thread). Same hierarchy, different framing — programmer-API view vs hardware-tier view.
- **Latency-hiding mechanism aligns with Ch2 §2.5.** Ch2 introduced [[Latency]] vs [[Bandwidth]] and prefetching/overlap-with-computation as latency-hiding levers. Ch5's warp-swap-on-memory-stall is the same idea implemented in hardware at extremely fine grain — no contradiction, an instance.
