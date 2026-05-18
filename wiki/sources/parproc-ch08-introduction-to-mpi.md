---
title: "ParProcBook Ch8: Introduction to MPI"
type: source
tags: [textbook, parallel-computing, mpi, message-passing, collective-communication]
date: 2026-05-17
source_file: raw/parproc-matloff.pdf
---

# ParProcBook Ch8: Introduction to MPI

Chapter 8 (book pp. 187–212, PDF pp. 207–232) of *Programming on Parallel Machines: GPU, Multicore, Clusters and More* by [[NormMatloff]] of [[UCDavis]]. The dedicated [[MPI]] chapter: the de-facto-standard message-passing API delivered via two worked examples (a parallel [[DijkstraAlgorithm|Dijkstra shortest-path]] solver and a 0-removal stream-compaction kernel), an API tour (`MPI_Init` / `MPI_Finalize` / `MPI_Comm_size` / `MPI_Comm_rank` / `MPI_Send` / `MPI_Recv`), a collective-communication section that rewrites the Dijkstra example with `MPI_Reduce` + `MPI_Bcast` + `MPI_Gather` (and the alternative `MPI_Allreduce`, plus `MPI_Scatter` + `MPI_Allgather` + `MPI_Barrier`), the [[MPICommunicator|communicator]] sub-group story (`MPI_Comm_group` / `MPI_Group_incl` / `MPI_Comm_create`), the [[BufferingMPI|buffering / synchrony / safety]] discussion (`MPI_Send` semantics, TCP/IP socket layering, the synchronous-deadlock pattern, [[NonblockingComm|`MPI_Isend` / `MPI_Irecv`]] for "living dangerously", `MPI_Sendrecv` for safe exchange), and the *use-from-other-languages* coda. Establishes the **[[SPMD|SPMD]] (Single Program Multiple Data)** model as MPI's canonical execution mode and reframes [[MPI]] from Ch1's pipeline-curio into the chapter-length API surface the rest of the book reuses.

## Summary

§8.1 opens with the one-line thesis: *"MPI is the de facto standard for message-passing software."* §8.1.1 *History* situates MPI on a 20-year arc: small shared-memory machines historically expensive → *"This led to interest in message-passing machines."* The first affordable message-machine was the [[Hypercube]] (*"a physics professor at Cal Tech"* — David Cohen / nCUBE-era origin; Intel and nCube commercialized). [[NetworkOfWorkstations|NOWs]] followed, refined into [[Cluster|clusters]] with better network hardware. *"All of this necessitated the development of standardized software tools based on a message-passing paradigm. The first popular such tool was **Parallel Virtual Machine (PVM)**. It still has its adherents today, but has largely been supplanted by the Message Passing Interface (MPI). MPI itself later became MPI 2."* Ch8's scope is *"intended mainly for the original."*

§8.1.2 *Structure and Execution.* *"MPI is merely a set of Application Programmer Interfaces (APIs), called from user programs written in C, C++ and other languages. It has many implementations, with some being open source and generic, while others are proprietary and fine-tuned for specific commercial hardware."* The chapter's working model: an MPI program **x** is run on N machines in a cluster; each machine runs its own copy of x. *"Official MPI terminology refers to this as four **processes**. Now that multicore machines are commonplace, one might indeed run two or more cooperating MPI processes — where now we use the term *processes* in the real OS sense — on the same multicore machine. In this document, we will tend to refer to the various MPI processes as **nodes**, with an eye to the cluster setting."* The execution-model name: **[[SPMD|Single Program Multiple Data (SPMD)]]** — *"though the nodes are all running the same program, they will likely be working on different parts of the program's data. This is the typical approach, but there could be different programs running on different nodes. Most of the APIs involve a node sending information to, or receiving information from, other nodes."*

§8.1.3 *Implementations.* Two popular MPI implementations: **MPICH** and **LAM**. *"MPICH offers more tailoring to various networks and other platforms, while LAM runs on networks."* Then the unannotated retirement note: *"LAM is no longer being developed, and has been replaced by Open MPI (not to be confused with [[OpenMP]]). Personally, I still prefer the simplicity of LAM. It is still being maintained."* Hard warning: *"If your machine has more than one MPI implementation, make absolutely sure one is not interfering with the other. Make sure all execution and library paths all include one and only one implementation at a time."* (Multi-MPI-install pollution is a real-world support issue.)

§8.1.4 *Performance Issues.* *"Mere usage of a parallel language on a parallel platform does not guarantee a performance improvement over a serial version of your program. The central issue here is the overhead involved in internode communication."* The chapter gives the contemporary [[Infiniband]] numbers: *"Infiniband, one of the fastest cluster networks commercially available, has a [[Latency|latency]] of about 1.0-3.0 microseconds, meaning that it takes the first bit of a packet that long to get from one node on an Infiniband switch to another. Comparing that to the nanosecond time scale of CPU speeds, one can see that the communications overhead can destroy a program's performance. And Ethernet is quite a bit slower than Infiniband."* Then the [[Latency|latency]] vs [[Bandwidth|bandwidth]] distinction worked numerically: 1.0 μs latency + 1 gigabit/s = 1000 bits/μs; a 2000-bit message arrives in 1+2 = 3 μs. At 10 gigabits/s the same message takes 1.2 μs to arrive *fully*: *"So latency is a major problem even if the bandwidth is high. For this reason, MPI applications that run well on networks tend to be of the **embarrassingly parallel** type, with very little communication between the processes."* (On a shared-memory multicore where all MPI processes co-reside, *"the problem is less severe. In fact, some implementations of MPI communicate directly through shared memory in that case, rather than using the TCP/IP or other network protocol."*)

§8.2 *Review of Earlier Example* is a one-line forward-link back to Ch1.6.2.2's pipelined prime finder.

§8.3 *Example: Dijkstra Algorithm.* The chapter's primary worked example. The pseudocode is the same single-source shortest-path procedure already developed under [[OpenMP]] in Ch4: maintain `Done` / `NonDone` sets, `Dist[J]` array; each iteration *"finds the closest vertex J to 0 among all those not yet processed, and then updates the list of minimum distances to each vertex from 0 by considering paths that go through J."*

**§8.3.2 *The MPI Code.*** The full `Dijkstra.c` listing. Architectural choices:
- Node 0 *"will both participate in the computation and serve as a 'manager.'"*
- Three message types are programmer-defined: `MYMIN_MSG` (worker-to-manager partial minima), `OVRLMIN_MSG` (manager-to-workers overall-min broadcast), `COLLECT_MSG` (worker-to-manager final-segment collection).
- Vertices are partitioned by `chunk = nv / nnodes`; node `me` owns `[startv, endv] = [me*chunk, me*chunk + chunk - 1]`.
- Every node generates the *same* random graph by seeding `srand(9999)` deterministically — *"this will be generated at all nodes; could generate just at node 0 and then send to others, but faster this way."* A nice latency-vs-recomputation tradeoff.
- The main loop runs `nv` iterations of `findmymin()` → `findoverallmin()` → `disseminateoverallmin()` → `notdone[overallmin[1]] = 0` → `updatemymind(startv, endv)`; then a final `updateallmind()` collects.
- Workers `MPI_Send(mymin, ...)` to node 0 in `findoverallmin`; node 0 `MPI_Recv`s from each i=1..nnodes-1 and tracks the global min.
- `disseminateoverallmin` is a manual broadcast: node 0 loops `MPI_Send(overallmin, ...)` to each worker; workers `MPI_Recv` once.
- `updateallmind` is a manual gather: workers `MPI_Send(mind+startv, chunk, ...)` to 0; node 0 `MPI_Recv`s each chunk into `mind+i*chunk`.
- *"`while (dbg) ;`"* — the canonical debugger-attach stall: *"deliberately sets up an infinite loop of dbg is nonzero, for reasons to be discussed below."*

This Dijkstra example **uses only `MPI_Send` and `MPI_Recv`** — the chapter deliberately implements broadcast/reduce/gather by hand before introducing the collective APIs that subsume them in §8.6. The refactored §8.6.1 *Refined Dijkstra Code* replaces the manual loops with `MPI_Reduce(mymin, overallmin, 1, MPI_2INT, MPI_MINLOC, 0, MPI_COMM_WORLD)` + `MPI_Bcast(overallmin, 1, MPI_2INT, 0, MPI_COMM_WORLD)` + a final `MPI_Gather(mind+startv, chunk, MPI_INT, mind, chunk, MPI_INT, 0, MPI_COMM_WORLD)` — the entire `findoverallmin` / `disseminateoverallmin` / `updateallmind` functions disappear.

**§8.3.3 *Introduction to MPI APIs.*** API tour built off the Dijkstra code:

- **`MPI_Init(&argc, &argv)` and `MPI_Finalize()`** — *"required for starting and ending execution of an MPI program. Their actions may be implementation-dependent. For instance, if our platform is an Ethernet-based cluster, `MPI_Init` will probably set up the TCP/IP sockets via which the various nodes communicate with each other. On an Infiniband-based cluster, connections in the special Infiniband network protocol will be established. On a shared-memory multiprocessor, an implementation of MPI that is tailored to that platform would take very different actions."*
- **`MPI_Comm_size(MPI_COMM_WORLD, &nnodes)` and `MPI_Comm_rank(MPI_COMM_WORLD, &me)`** — *"the first call determines how many nodes are participating in our computation, placing the result in our variable `nnodes`. Here **MPI_COMM_WORLD** is our node group, termed a **communicator** in MPI parlance. MPI allows the programmer to subdivide the nodes into groups, to facilitate performance and clarity of code. Note that for some operations, such as barriers, the only way to apply the operation to a proper subset of all nodes is to form a group. The totality of all groups is denoted by **MPI_COMM_WORLD**."* The second call writes the node's [[MPICommunicator|rank]] (0-based ID within its group).
- **`MPI_Send(mymin, 2, MPI_INT, 0, MYMIN_MSG, MPI_COMM_WORLD)`** — six arguments: (1) `mymin` — address of bytes to send. (2,3) `count=2`, `MPI_INT` — *"why did the designers of MPI bother to define data types? The answer is that we want to be able to run MPI on a heterogeneous set of machines, with MPI serving as the 'broker' between them in case different architectures among those machines handle data differently."* The endianness story: Intel = little-endian, Sun SPARC = big-endian; *"if our set of nodes included machines of both types, straight transmission of sequences of 8 bytes might mean that some of the machines literally receive the data backwards!"* Also handles 32-vs-64-bit word size. (4) Destination rank `0`. (5) Message tag `MYMIN_MSG` — receiver-side filter. (6) [[MPICommunicator|Communicator]] `MPI_COMM_WORLD`.
- **`MPI_Recv(othermin, 2, MPI_INT, i, MYMIN_MSG, MPI_COMM_WORLD, &status)`** — same six arguments plus a status output. The wildcard values: **`MPI_ANY_SOURCE`** (don't care about sender) and **`MPI_ANY_TAG`** (don't care about message type). `MPI_Status` is *"an MPI struct containing information about the received message. Its primary fields of interest are **MPI_SOURCE**, which contains the identity of the sending node, and **MPI_TAG**, which contains the message type."*

§8.4 *Example: Removing 0s from an Array.* A 0-removal **stream-compaction** kernel. Architecture: manager (rank 0) generates `has0s[N]` of random values mod 4, [[MPIScatter|scatters]] `lenchunk = n/(nnodes-1)` elements to each worker (via explicit `MPI_Send`s in this version), each worker calls a local `remov0s()` (sequential `if (oldx[i] != 0) newx[count++] = oldx[i]`), then `MPI_Send`s `no0s[]` of length `nno0s` back. Manager `MPI_Recv`s the variable-length results, using **`MPI_Get_count(&status, MPI_INT, &lenchunk)`** to discover the actual size of each received chunk (since lengths are data-dependent). The kernel demonstrates the **variable-output-length** pattern unique to message-passing (vs the static-output stream compaction of [[Thrust]] / [[CUDA]]).

§8.5 *Debugging MPI Code.* *"If you are using GDB — either directly, or via an IDE such as Eclipse or Netbeans — the trick with MPI is to **attach** GDB to your running MPI processes."* The recipe:
1. Code includes `while (dbg) ;` — *"deliberately sets up an infinite loop if dbg is nonzero."*
2. Start the MPI program (`a.out`) on machines A, B, C; open three terminal windows.
3. On each machine, find the process ID with `ps ax`, then `gdb a.out 88888` (or the actual PID).
4. GDB attaches mid-loop; Ctrl-C interrupts; `(gdb) set var dbg = 0` lets the program proceed.
5. Set breakpoints before issuing `c` (continue).

This is the canonical **attach-style multi-process debugging** workflow — distinguishing message-passing debugging from shared-memory debugging where one debugger can see all threads in a single process.

§8.6 *Collective Communications.* The refined Dijkstra version (`Dijkstra.coll1.c`) drops three hand-written functions and replaces them with three collective calls:

- **§8.6.2 [[MPIBcast|`MPI_Bcast(overallmin, 1, MPI_2INT, 0, MPI_COMM_WORLD)`]]** replaces a `for (i=1; i<nnodes; i++) MPI_Send(...)` loop. *"At this point all nodes participate in a broadcast operation, in which node 0 sends 2 objects of type MPI_INT to each node (including itself). The source of the data will be located at address overallmin at node 0, and the other nodes will receive the data at a location of that name."* The pedagogical clarification: *"the name of the function is 'broadcast,' which makes it sound like only node 0 executes this line of code, which is not the case; all the nodes in the group execute this line. The only difference is the action; most nodes participate by receiving, while node 0 participates by sending."* Two reasons to prefer broadcast over a loop: (1) clarity / readability, (2) **the MPI implementation may exploit hardware multicast** — *"on a shared-memory multiprocessor system, special machine instructions specific to that platform's architecture can be exploited, as for instance IBM has done for its shared-memory machines. Even on an ordinary Ethernet, one could exploit Ethernet's own broadcast mechanism, as had been done for PVM."*
- **§8.6.3 [[MPIReduce|`MPI_Reduce(mymin, overallmin, 1, MPI_2INT, MPI_MINLOC, 0, MPI_COMM_WORLD)`]]** replaces the `findoverallmin` function. *"At this point all nodes in this group participate in a 'reduce' operation. The type of reduce operation is **MPI_MINLOC**, which means that the minimum value among the nodes will be computed, and the index attaining that minimum will be recorded as well."* The full **reduce-operation table** (§8.6.3 p. 203):

| Op | Meaning |
|---|---|
| `MPI_MAX` | max |
| `MPI_MIN` | min |
| `MPI_SUM` | sum |
| `MPI_PROD` | product |
| `MPI_LAND` | wordwise boolean and |
| `MPI_LOR` | wordwise boolean or |
| `MPI_LXOR` | wordwise exclusive or |
| `MPI_BAND` | bitwise boolean and |
| `MPI_BOR` | bitwise boolean or |
| `MPI_BXOR` | bitwise exclusive or |
| `MPI_MAXLOC` | max value and location |
| `MPI_MINLOC` | min value and location |
- **[[MPIAllreduce|`MPI_Allreduce(mymin, overallmin, 1, MPI_2INT, MPI_MINLOC, MPI_COMM_WORLD)`]]** *"does the same operation, except that instead of just depositing the result at one node, it does so at all nodes."* — collapses the common `MPI_Reduce`+`MPI_Bcast` idiom into one call.
- **§8.6.4 [[MPIGather|`MPI_Gather(mind+startv, chunk, MPI_INT, mind, chunk, MPI_INT, 0, MPI_COMM_WORLD)`]]** replaces `updateallmind`. *"At this point all nodes participate in a gather operation, in which each node (including Node 0) contributes chunk number of MPI integers, from a location mind+startv in that node's program. Node 0 then receives chunk items sent from each node, stringing everything together in node order and depositing it all at mind in the program running at Node 0."* Side-note: *"the fifth argument is redundant with the second; same for the third and sixth."*
- **[[MPIAllgather|`MPI_Allgather(srcbuf, srccount, srctype, destbuf, destcount, desttype, communicator)`]]** — *"places the result at all nodes, not just one. Its call form is the same as MPI_Gather, but with one fewer argument (since the identity of 'the' gathering node is no longer meaningful)."*
- **§8.6.5 [[MPIScatter|`MPI_Scatter(oh, lenchunk, MPI_INT, ohchunk, lenchunk, MPI_INT, 0, MPI_COMM_WORLD)`]]** — *"the opposite of MPI_Gather, i.e. it breaks long data into chunks which it parcels out to individual nodes."* Inversion: scatter breaks a single buffer into chunks distributed across all nodes; gather collects per-node chunks into a single buffer.
- **§8.6.9 [[MPIBarrier|`MPI_Barrier(comm)`]]** — *"implements a barrier for a given communicator. The name of the communicator is the sole argument for the function. Explicit barriers are less common in message-passing programs than in the shared-memory world."*

Two more §8.6 worked examples:
- **§8.6.6 *Count Number of Edges in a Directed Graph.*** Manager scatters `oh` (one-hop matrix) into per-node chunks; each node counts nonzero entries; `MPI_Reduce(mycount, numedge, 1, MPI_INT, MPI_SUM, 0, MPI_COMM_WORLD)` totals globally.
- **§8.6.7 *Cumulative Sums.*** Two-phase prefix-sum: scatter chunks, each node does a sequential prefix-sum locally, gather the per-chunk last elements (= local sums) to node 0, broadcast the array of local sums, each node node>0 adds the prefix-sum of all preceding nodes' totals to its local prefix sums. Pattern: **scan = local-scan + share-locals + add-prefix-of-locals** — the Hillis-Steele / Brent-Kung idea adapted to coarse-grained MPI chunks.
- **§8.6.8 *Mutual Outlinks.*** Same problem as the Ch4 OpenMP / Ch5 CUDA / Ch6 Thrust treatments — count mutual outbound links between Web pages in an adjacency matrix `m[n][n]`. `MPI_Bcast(m, n*n, MPI_INT, 0, MPI_COMM_WORLD)` distributes the full adjacency matrix; each node handles `i = me, me+nnodes, me+2*nnodes, ...` rows (round-robin static assignment); local `tot` summed via `MPI_Reduce(&tot, &grandtot, 1, MPI_INT, MPI_SUM, 0, MPI_COMM_WORLD)`. *"For each node i, check all possible pairing nodes j > i; the various nodes work on values of i in a Round Robin fashion, with node k handling all i for which i mod nnodes = k."*

**§8.6.10 *Creating Communicators.*** [[MPICommunicator|Communicators]] are sub-groups of MPI processes. The four-call recipe (illustrated by splitting `MPI_COMM_WORLD` into two halves of size `nnodes/2`):

```c
MPI_Group worldgroup, subgroup;
MPI_Comm subcomm;
int *subranks = malloc(nn2 * sizeof(int));
// populate subranks with the ranks {start, start+1, ..., start+nn2-1}
MPI_Comm_group(MPI_COMM_WORLD, &worldgroup);     // 1. extract group from communicator
MPI_Group_incl(worldgroup, nn2, subranks, &subgroup);  // 2. build sub-group from ranks
MPI_Comm_create(MPI_COMM_WORLD, subgroup, &subcomm);   // 3. wrap sub-group in a communicator
MPI_Group_rank(subgroup, &subme);                // 4. learn my rank in the new group
```

*"You would then use **subcomm** instead of MPI_COMM_WORLD whenever you wish to, say, broadcast only to that group."*

§8.7 *Buffering, Synchrony and Related Issues.* The chapter's lowest-level section: what *actually happens* inside `MPI_Send` / `MPI_Recv` on a TCP/IP cluster.

**§8.7.1 *Buffering, Etc.*** The three-layer abstraction: OS's TCP/IP stack at Session/Transport/Network layers; MPI internals at the Application layer; the user's MPI program at a "Super-application" layer. `MPI_Init` sets up TCP/IP sockets between every node pair (the **connection**). `MPI_Send` writes to the socket; *"the TCP/IP stack will transmit that data to the TCP/IP socket at B."* Two technical traps:

1. **TCP/IP coalesces messages.** *"In TCP/IP the totality of bytes sent by A to B during lifetime of the connection is considered one long message. So for instance if the MPI program at A calls `MPI_Send()` five times, the MPI internals will write to the socket five times, but the bytes from those five messages will not be perceived by the TCP/IP stack at B as five messages, but rather as just one long message."* MPI at B continually reads and re-decomposes into message-sized chunks, *"keeping them ready for calls to `MPI_Recv` from the MPI application program at B."*
2. **Flow control bounds OS buffer size.** *"The buffer space the OS at B has set up for receiving data is limited. As A is sending to B, the TCP layer at B is telling its counterpart at A when A is allowed to send more data."*

The blocking semantics: *"If no such message has arrived yet, MPI won't return to the caller yet, and thus the caller blocks. `MPI_Send` can block too. If the platform and MPI implementation is that of the TCP/IP network context described above, then the send call will return when its call to the OS' `write()` (or equivalent, depending on OS) returns, but that could be delayed if the OS' buffer space is full. On the other hand, another implementation could require a positive response from B before allowing the send call to return."* The performance cost of buffering: *"`MPI_Recv()` at B must copy messages from the OS' buffer space to the MPI application program's program variables, e.g. `x` above. This is definitely a blow to performance. That in fact is why networks developed specially for parallel processing typically include mechanisms to avoid the copying. Infiniband, for example, has a Remote Direct Memory Access capability, meaning that A can write directly to `x` at B."* (Cross-link to [[Infiniband]] / RDMA from Ch7.)

The MPI-standard guarantee, surgically stated: *"`MPI_Send(x,...)` will return only when it is safe for the application program to write over the array which it is using to store its message, i.e. `x`."* So the **safety guarantee** is *"send-side x is writable again"*, not *"receive-side has the data"* — buffering can make these very different events.

**§8.7.2 *Safety.*** Two deadlock patterns:

1. *"With synchronous communication, deadlock is a real risk. Say A wants to send two messages to B, of types U and V, but that B wants to receive V first. Then A won't even get to send V, because in preparing to send U it must wait for a notice from B that B wants to read U — a notice which will never come, because B sends such a notice for V first."* — the **classic tag-mismatch deadlock**.
2. *"Even with buffering, as buffer space is always by nature finite. A program can fail if it runs out of buffer space, either at the sender or the receiver."* (The chapter points at the LLNL `unsafe.c` example.)

The terminology: *"In MPI terminology, asynchronous communication is considered **unsafe**. The program may run fine on most systems, as most systems are buffered, but fail on some systems. Of course, as long as you know your program won't be run in nonbuffered settings, it's fine, and since there is potentially such a performance penalty for doing things synchronously, most people are willing to go ahead with their 'unsafe' code."*

**§8.7.3 *Living Dangerously.*** [[NonblockingComm|Nonblocking variants]]: *"If one is sure that there will be no problems of buffer overflow and so on, one can use variant send and receive calls provided by MPI, such as **`MPI_Isend()`** and **`MPI_Irecv()`**. The key difference between them and `MPI_Send()` and `MPI_Recv()` is that they return immediately, and thus are termed **nonblocking**. Your code can go on and do other things, not having to wait."* The safety contract: *"at A you cannot touch the data you are sending until you determine that it has either been buffered somewhere or has reached x at B. Similarly, at B you can't use the data at x until you determine that it has arrived."* Two helpers: **`MPI_Wait()`** blocks until completion; **`MPI_Probe()`** non-blockingly asks whether the operation has completed.

**§8.7.4 *Safe Exchange Operations.*** The lower-rank-sends-first idiom is fine but ugly. MPI provides **`MPI_Sendrecv_replace(buf, count, datatype, dest, sendtag, source, recvtag, comm, status)`**: *"a more convenient, safer and possibly faster alternative."* *"Note that the sent and received messages can be of different lengths and can use different tags."*

§8.8 *Use of MPI from Other Languages.* *"MPI is a vehicle for parallelizing C/C++, but some clever people have extended the concept to other languages, such as the cases of Python and R that we treat in Chapters ?? and ??."* (Unresolved cross-references — same forward-reference glitch as in Ch7.)

§8.9 *Other MPI Examples in This Book.* Two pointers: the pipelined prime number finder in Ch1, and bucket sort with sampling in §12.5.

## Key Claims

- **MPI is the de facto standard for message-passing software.** *"MPI is the de facto standard for message-passing software."* (§8.1 opening, p. 187). The chapter's one-line thesis.
- **MPI is a set of APIs, not a language.** *"MPI is merely a set of Application Programmer Interfaces (APIs), called from user programs written in C, C++ and other languages."* (§8.1.2, p. 188). This is load-bearing: MPI is portable across implementations (open-source generic + proprietary fine-tuned for specific hardware) and across host languages.
- **[[SPMD|SPMD]] is MPI's canonical execution model.** *"Though the nodes are all running the same program, they will likely be working on different parts of the program's data. This is called the Single Program Multiple Data (SPMD) model."* (§8.1.2, p. 188). Distinguished from MPMD which is also possible but uncommon.
- **MPICH targets diverse networks/platforms; LAM targets networks; Open MPI replaces LAM.** *"MPICH offers more tailoring to various networks and other platforms, while LAM runs on networks. LAM is no longer being developed, and has been replaced by Open MPI (not to be confused with OpenMP)."* (§8.1.3, p. 188). The MPICH/LAM/Open-MPI implementation taxonomy. **Open MPI ≠ OpenMP** — explicit warning to avoid confusion with [[OpenMP]].
- **Multiple MPI installations on one machine must not collide.** *"If your machine has more than one MPI implementation, make absolutely sure one is not interfering with the other. Make sure all execution and library paths all include one and only one implementation at a time."* (§8.1.3, p. 188).
- **MPI performance is bound by internode communication overhead.** *"The central issue here is the overhead involved in internode communication."* (§8.1.4, p. 188). [[Latency]] vs [[Bandwidth]] worked numerically: a 2000-bit message at 1 GB/s + 1 μs latency takes 3 μs to arrive; raising bandwidth 10× still leaves a 1.2 μs minimum. *"So latency is a major problem even if the bandwidth is high."* (§8.1.4, p. 189).
- **MPI applications that run well on networks tend to be [[EmbarrassinglyParallel|embarrassingly parallel]].** *"MPI applications that run well on networks tend to be of the 'embarrassingly parallel' type, with very little communication between the processes."* (§8.1.4, p. 189).
- **`MPI_Init` / `MPI_Finalize` bracket every MPI program; their actions are implementation-dependent.** *"On an Ethernet-based cluster, `MPI_Init` will probably set up the TCP/IP sockets via which the various nodes communicate with each other. On an Infiniband-based cluster, connections in the special Infiniband network protocol will be established. On a shared-memory multiprocessor, an implementation of MPI that is tailored to that platform would take very different actions."* (§8.3.3.1, p. 193).
- **`MPI_Comm_size` returns group size; `MPI_Comm_rank` returns this node's ID within its group.** (§8.3.3.2, p. 194). `MPI_COMM_WORLD` is the default [[MPICommunicator|communicator]] holding all nodes.
- **[[MPICommunicator|Communicators]] subdivide nodes into groups *"to facilitate performance and clarity of code"*.** *"For some operations, such as barriers, the only way to apply the operation to a proper subset of all nodes is to form a group. The totality of all groups is denoted by MPI_COMM_WORLD."* (§8.3.3.2, p. 194).
- **MPI uses typed messages to broker heterogeneous architectures.** *"We want to be able to run MPI on a heterogeneous set of machines, with MPI serving as the 'broker' between them in case different architectures among those machines handle data differently."* The two named heterogeneity sources: (a) **endianness** (Intel little-endian vs Sun SPARC big-endian — *"some of the machines literally receive the data backwards!"*), (b) **word width** (32-bit vs 64-bit). (§8.3.3.3, p. 194).
- **`MPI_Send(buf, count, datatype, dest, tag, comm)` — six arguments.** Tags filter messages on the receive side; `MPI_ANY_TAG` is the wildcard. (§8.3.3.3, p. 194).
- **`MPI_Recv(buf, count, datatype, source, tag, comm, status)` — same six + status output.** `MPI_ANY_SOURCE` / `MPI_ANY_TAG` are wildcards; the `MPI_Status` struct fills `MPI_SOURCE` / `MPI_TAG` so the caller can recover who-sent-what after a wildcard receive. (§8.3.3.4, p. 195).
- **Variable-length receives use `MPI_Get_count`.** The 0-removal example demonstrates: *"`MPI_Get_count(&status, MPI_INT, &lenchunk)`"* — recover the actual element count of a received buffer when senders ship variable-length results (§8.4, p. 197).
- **Debug MPI by attaching GDB to running processes.** *"The trick with MPI is to **attach** GDB to your running MPI processes."* The recipe: code includes `while (dbg) ;`, start the program, `ps ax` to find the PID, `gdb a.out <PID>` attaches mid-loop, Ctrl-C interrupts, `set var dbg = 0` lets it proceed. (§8.5, p. 197–198).
- **[[CollectiveCommunication|Collective communications]] subsume hand-coded send/recv loops.** §8.6's refined Dijkstra deletes three functions (`findoverallmin`, `disseminateoverallmin`, `updateallmind`) and replaces them with `MPI_Reduce` + `MPI_Bcast` + `MPI_Gather`. *"All the nodes in the group execute this line. The only difference is the action; most nodes participate by receiving, while node 0 participates by sending."* (§8.6.2, p. 201).
- **Collectives may exploit hardware (and reading them is easier).** Two pro-collective arguments: (1) clarity / readability of code; (2) *"using the broadcast may improve performance. We may, for instance, be using an implementation of MPI which is tailored to the platform on which we are running MPI. If for instance we are running on a network designed for parallel computing, such as Myrinet or Infiniband, an optimized broadcast may achieve a much higher performance level than would simply a loop with individual send calls."* (§8.6.2, pp. 201–202). Cross-link to Ch7's `MPI_Bcast`-is-not-magic warning: the optimization is conditional on hardware + matching MPI build.
- **The reduce-operation table (12 ops).** `MPI_MAX` / `MPI_MIN` / `MPI_SUM` / `MPI_PROD` / `MPI_LAND` / `MPI_LOR` / `MPI_LXOR` / `MPI_BAND` / `MPI_BOR` / `MPI_BXOR` / `MPI_MAXLOC` / `MPI_MINLOC`. (§8.6.3 table, p. 203). `MAXLOC`/`MINLOC` carry both the extremal value *and* its location — pair type is `MPI_2INT`.
- **`MPI_Allreduce` = `MPI_Reduce` + `MPI_Bcast`.** *"`MPI_Allreduce()` does the same operation, except that instead of just depositing the result at one node, it does so at all nodes."* (§8.6.3, p. 202).
- **`MPI_Gather` strings per-node contributions in rank order at the root.** *"Node 0 then receives chunk items sent from each node, stringing everything together in node order and depositing it all at mind in the program running at Node 0."* (§8.6.4, p. 203). The fifth-and-sixth arguments are *"redundant with the second; same for the third and sixth"* — an MPI design ugliness.
- **`MPI_Scatter` is `MPI_Gather`'s inverse.** *"The opposite of `MPI_Gather`, i.e. it breaks long data into chunks which it parcels out to individual nodes."* (§8.6.5, p. 203).
- **`MPI_Allgather` = gather with all-nodes destination.** Same call signature as `MPI_Gather` minus the root-rank argument. (§8.6.4, p. 203).
- **`MPI_Barrier(comm)` is rarely used in message-passing.** *"Explicit barriers are less common in message-passing programs than in the shared-memory world."* (§8.6.9, p. 208). The implicit reason: most MPI synchronization is *already* explicit at the send/recv boundary; an extra barrier is redundant.
- **Communicators are built in 4 calls: `MPI_Comm_group` → `MPI_Group_incl` → `MPI_Comm_create` → `MPI_Group_rank`.** (§8.6.10, p. 208). Used to scope collectives to a subset of processes (e.g. row-groups in a 2D physics simulation grid).
- **Under the hood, `MPI_Send` writes to a TCP/IP socket established at `MPI_Init`.** *"MPI at node A will have set up a TCP/IP socket to B during the user program's call to `MPI_Init`. [...] When node A calls `MPI_Send()`, MPI will write to the socket, and the TCP/IP stack will transmit that data to the TCP/IP socket at B."* (§8.7.1, p. 209).
- **TCP/IP coalesces 5 MPI_Sends into one long stream.** *"In TCP/IP the totality of bytes sent by A to B during lifetime of the connection is considered one long message. So for instance if the MPI program at A calls `MPI_Send()` five times, the MPI internals will write to the socket five times, but the bytes from those five messages will not be perceived by the TCP/IP stack at B as five messages, but rather as just one long message."* (§8.7.1, p. 209). MPI re-parses message boundaries from the byte stream.
- **`MPI_Send` returns when **the send buffer is safe to reuse**, not when the receiver has the data.** *"`MPI_Send(x,...)` will return only when it is safe for the application program to write over the array which it is using to store its message, i.e. `x`."* (§8.7.1, p. 210). This is a load-bearing semantic — the buffering layer can decouple "send completed" from "receive completed."
- **Buffering helps performance but adds a copy.** `MPI_Recv` *"must copy messages from the OS' buffer space to the MPI application program's program variables, e.g. `x` above. This is definitely a blow to performance. That in fact is why networks developed specially for parallel processing typically include mechanisms to avoid the copying. Infiniband, for example, has a Remote Direct Memory Access capability, meaning that A can write directly to `x` at B."* (§8.7.1, p. 210).
- **Synchronous communication can deadlock on tag mismatch.** *"With synchronous communication, deadlock is a real risk. Say A wants to send two messages to B, of types U and V, but that B wants to receive V first. Then A won't even get to send V, because in preparing to send U it must wait for a notice from B that B wants to read U — a notice which will never come, because B sends such a notice for V first."* (§8.7.2, p. 210). Async-with-buffering removes formal deadlock but can still fail on buffer exhaustion.
- **Async / buffered comm is "unsafe" in MPI terminology.** *"In MPI terminology, asynchronous communication is considered **unsafe**. The program may run fine on most systems, as most systems are buffered, but fail on some systems."* (§8.7.2, p. 210). The pragmatic compromise: *"since there is potentially such a performance penalty for doing things synchronously, most people are willing to go ahead with their 'unsafe' code."*
- **`MPI_Isend` / `MPI_Irecv` are the [[NonblockingComm|nonblocking]] variants.** *"They return immediately, and thus are termed nonblocking. Your code can go on and do other things, not having to wait."* (§8.7.3, p. 211). Completion is checked via `MPI_Wait()` (blocks until done) or `MPI_Probe()` (asks).
- **`MPI_Sendrecv_replace(buf, count, datatype, dest, sendtag, source, recvtag, comm, status)` does a safe in-place exchange.** *"A more convenient, safer and possibly faster alternative."* (§8.7.4, p. 211). *"The sent and received messages can be of different lengths and can use different tags."*

## Key Quotes

> *"MPI is the de facto standard for message-passing software."* — §8.1 opening, p. 187. The one-line chapter thesis.

> *"MPI is merely a set of Application Programmer Interfaces (APIs), called from user programs written in C, C++ and other languages. It has many implementations, with some being open source and generic, while others are proprietary and fine-tuned for specific commercial hardware."* — §8.1.2, p. 188. The API-not-language framing.

> *"Though the nodes are all running the same program, they will likely be working on different parts of the program's data. This is called the Single Program Multiple Data (SPMD) model. This is the typical approach, but there could be different programs running on different nodes."* — §8.1.2, p. 188. The [[SPMD|SPMD]] execution-model definition.

> *"LAM is no longer being developed, and has been replaced by Open MPI (not to be confused with OpenMP)."* — §8.1.3, p. 188. The implementation-history one-liner.

> *"MPI applications that run well on networks tend to be of the 'embarrassingly parallel' type, with very little communication between the processes."* — §8.1.4, p. 189. The performance-shape guidance.

> *"MPI_COMM_WORLD is our node group, termed a communicator in MPI parlance. MPI allows the programmer to subdivide the nodes into groups, to facilitate performance and clarity of code."* — §8.3.3.2, p. 194. The [[MPICommunicator|communicator]] concept introduced.

> *"Why did the designers of MPI bother to define data types? The answer is that we want to be able to run MPI on a heterogeneous set of machines, with MPI serving as the 'broker' between them in case different architectures among those machines handle data differently."* — §8.3.3.3, p. 194. The endianness/word-width motivation for typed messages.

> *"The trick with MPI is to attach GDB to your running MPI processes."* — §8.5, p. 197. The debugging recipe headline.

> *"At this point all nodes participate in a broadcast operation [...] The name of the function is 'broadcast,' which makes it sound like only node 0 executes this line of code, which is not the case; all the nodes in the group execute this line. The only difference is the action; most nodes participate by receiving, while node 0 participates by sending."* — §8.6.2, pp. 201. The crucial *all-nodes-execute-the-collective* clarification.

> *"Using the broadcast may improve performance. We may, for instance, be using an implementation of MPI which is tailored to the platform on which we are running MPI. If for instance we are running on a network designed for parallel computing, such as Myrinet or Infiniband, an optimized broadcast may achieve a much higher performance level than would simply a loop with individual send calls."* — §8.6.2, p. 201. The hardware-multicast-when-available rationale.

> *"`MPI_Allreduce()` [...] does the same operation, except that instead of just depositing the result at one node, it does so at all nodes."* — §8.6.3, p. 202. The reduce-vs-allreduce distinction.

> *"Explicit barriers are less common in message-passing programs than in the shared-memory world."* — §8.6.9, p. 208. The why-MPI_Barrier-is-rare remark.

> *"In TCP/IP the totality of bytes sent by A to B during lifetime of the connection is considered one long message. So for instance if the MPI program at A calls `MPI_Send()` five times, the MPI internals will write to the socket five times, but the bytes from those five messages will not be perceived by the TCP/IP stack at B as five messages, but rather as just one long message."* — §8.7.1, p. 209. The TCP-stream-coalescing trap.

> *"Technically, the MPI standard states that `MPI_Send(x,...)` will return only when it is safe for the application program to write over the array which it is using to store its message, i.e. x."* — §8.7.1, p. 210. The exact MPI-standard send-semantics statement.

> *"With synchronous communication, deadlock is a real risk. Say A wants to send two messages to B, of types U and V, but that B wants to receive V first. Then A won't even get to send V, because in preparing to send U it must wait for a notice from B that B wants to read U — a notice which will never come."* — §8.7.2, p. 210. The classic tag-mismatch [[Deadlock|deadlock]] pattern.

> *"In MPI terminology, asynchronous communication is considered **unsafe**. The program may run fine on most systems, as most systems are buffered, but fail on some systems."* — §8.7.2, p. 210. The unsafe-by-definition terminology.

> *"If one is sure that there will be no problems of buffer overflow and so on, one can use variant send and receive calls provided by MPI, such as `MPI_Isend()` and `MPI_Irecv()`. The key difference between them and `MPI_Send()` and `MPI_Recv()` is that they return immediately, and thus are termed **nonblocking**."* — §8.7.3, p. 211. The nonblocking-variants intro.

## Connections

- [[NormMatloff]] — author.
- [[UCDavis]] — author's institution.
- [[parproc-ch01-intro-parallel-processing]] — Ch1 introduced MPI via the pipelined prime-finder. Ch8 is the chapter-length API expansion that backfills the API surface Ch1 forward-referenced.
- [[parproc-ch02-recurring-performance-issues]] — Ch2's [[Latency]] / [[Bandwidth]] / [[EmbarrassinglyParallel|embarrassingly parallel]] vocabulary is the analytical frame for §8.1.4's MPI-performance discussion. The 2000-bit-message arithmetic is a direct Ch2 application.
- [[parproc-ch04-introduction-to-openmp]] — Ch4's [[DijkstraAlgorithm|Dijkstra]] worked example is reused in §8.3 as the **MPI side-by-side**: same algorithm, message-passing version vs shared-memory version. The chapter explicitly invokes the parallel structure (find min, relax) from Ch4 §4.2.1.
- [[parproc-ch07-message-passing-systems]] — Ch7 is the hardware-substrate chapter; Ch8 is its programming-API counterpart. The Ch7 *"`MPI_Bcast` is O(P) sequential sends unless hardware multicast"* warning is operationalized in Ch8 §8.6.2's optimization rationale. The Ch7 [[Infiniband]] / RDMA discussion is referenced again in §8.7.1's *"why networks developed specially for parallel processing typically include mechanisms to avoid the copying."*
- [[MPI]] — the chapter subject; this Ch8 source page substantially expands the [[MPI]] entity page's API surface, implementation taxonomy, SPMD framing, communicator subdivision, collective operations, and buffering/synchrony semantics.
- [[SPMD]] — new concept page. The Single Program Multiple Data execution model: every MPI node runs the same program text but on different data partitions.
- [[CollectiveCommunication]] — new concept page. The all-nodes-participate communication primitive class subsuming broadcast / reduce / gather / scatter / barrier.
- [[MPISend]] — new concept page. The fundamental point-to-point send, six-argument signature, type-broker rationale, the *"safe to overwrite the send buffer"* return semantic.
- [[MPIRecv]] — new concept page. The matching point-to-point receive with `MPI_ANY_SOURCE` / `MPI_ANY_TAG` wildcards + `MPI_Status` struct.
- [[MPIBcast]] — new concept page. The one-to-all broadcast collective.
- [[MPIReduce]] — new concept page. The all-to-one reduce collective with the 12-op table including `MPI_MINLOC` / `MPI_MAXLOC`.
- [[MPIAllreduce]] — new concept page. `MPI_Reduce` + `MPI_Bcast` collapsed into one call.
- [[MPIGather]] — new concept page. The all-to-one gather collective: each node contributes a chunk; root concatenates in rank order.
- [[MPIAllgather]] — new concept page. Gather with all-nodes destination.
- [[MPIScatter]] — new concept page. The one-to-all scatter collective; inverse of gather.
- [[MPIBarrier]] — new concept page. The barrier-for-a-communicator; rarely used because most MPI synchronization is implicit at send/recv boundaries.
- [[MPICommunicator]] — new concept page. Subgroups of MPI processes, created via `MPI_Comm_group` → `MPI_Group_incl` → `MPI_Comm_create` → `MPI_Group_rank`. `MPI_COMM_WORLD` is the universal communicator.
- [[BufferingMPI]] — new concept page. The TCP/IP-socket / OS-buffer / MPI-internals layering; the send-buffer-reusable semantic; the receiver-side message-boundary re-parsing.
- [[NonblockingComm]] — new concept page. The `MPI_Isend` / `MPI_Irecv` *"living dangerously"* variants + `MPI_Wait` / `MPI_Probe` completion checks.
- [[DijkstraAlgorithm]] — reused. Ch8's primary worked example (§8.3, §8.6.1).
- [[Hypercube]] — reused. Ch8 §8.1.1 names hypercubes as the historical first affordable message-passing hardware. Algorithmically, MPI collectives often use logical-hypercube schedules even on flat networks.
- [[NetworkOfWorkstations]] — reused. Ch8 §8.1.1 names NOWs as the post-hypercube substrate.
- [[Cluster]] — reused. Ch8 §8.1.4's *"shared-memory multiprocessor (especially a multicore one, where communication between cores is particularly fast)"* MPI-on-shared-memory scenario.
- [[MessagePassingArchitecture]] — Ch8 is its programming-API chapter.
- [[Infiniband]] — reused. Ch8 §8.1.4 quotes the 1–3 μs latency, and §8.7.1 invokes RDMA as the buffering-avoidance mechanism.
- [[Latency]] — reused. Ch8 §8.1.4's numerical worked example.
- [[Bandwidth]] — reused. Ch8 §8.1.4's *"latency is a major problem even if the bandwidth is high"* punchline.
- [[EmbarrassinglyParallel]] — reused. Ch8 §8.1.4's preferred MPI workload shape.
- [[OpenMP]] — reused. Ch8 §8.1.3 warns *"Open MPI (not to be confused with OpenMP)"* — distinct technologies that are easily confused.
- [[ScatterGather]] — reused. Ch8 §8.6.4 / §8.6.5 are the canonical MPI realization of the scatter/gather paradigm.
- [[Deadlock]] — reused. Ch8 §8.7.2's synchronous-comm tag-mismatch deadlock.
- [[GDB]] — reused. Ch8 §8.5's attach-style multi-process debugging.
- Endianness — referenced; Ch8 §8.3.3.3's heterogeneous-architecture motivation for typed messages (no dedicated wiki page; covered inline on the [[MPI]] / [[MPISend]] pages).
- [[MapReduce]] — referenced. Ch8 §8.6.4–§8.6.5 scatter/gather is the MPI analog of MapReduce's split/combine.

## Contradictions

- **No outright contradictions with prior Ch1–Ch7 content.** Ch8 is the API-detail chapter for the [[MPI]] forward-reference Ch1 made, the [[ScatterGather]] / Hadoop / Snow trio Ch1 §1.6.2.4 sketched, the [[Hypercube]] / [[NetworkOfWorkstations]] / [[Infiniband]] / [[Cluster]] hardware substrate Ch7 backfilled, and the [[DijkstraAlgorithm]] worked example Ch4 developed under [[OpenMP]]. Every Ch8 claim is consistent with prior chapters and adds either implementation detail (sockets, buffering, blocking semantics) or new API surface (collectives, communicators, nonblocking variants).
- **Minor clarification vs Ch1's MPI introduction.** Ch1 introduced `MPI_Send` / `MPI_Recv` and named the canonical-boilerplate four (`MPI_Init` / `MPI_Comm_size` / `MPI_Comm_rank` / `MPI_Finalize`) as a *single* programming pattern. Ch8 reveals that even the four boilerplate calls are implementation-dependent in their effect: *"On an Ethernet-based cluster, `MPI_Init` will probably set up the TCP/IP sockets [...] On an Infiniband-based cluster, connections in the special Infiniband network protocol will be established. On a shared-memory multiprocessor, an implementation of MPI that is tailored to that platform would take very different actions."* (§8.3.3.1, p. 193). This is a *deepening*, not a contradiction.
- **Minor terminology evolution: *processes* vs *nodes*.** §8.1.2 acknowledges *"Official MPI terminology refers to this as four processes. Now that multicore machines are commonplace, one might indeed run two or more cooperating MPI processes — where now we use the term processes in the real OS sense — on the same multicore machine."* The author chooses *nodes* for the rest of the book *"with an eye to the cluster setting."* Useful disambiguation when reconciling cross-chapter usage.

## Notes on chapter cohesion

- **Same Dijkstra worked-example pattern Ch4 used.** Ch4 walked OpenMP pragmas by progressively annotating a single Dijkstra implementation. Ch8 reuses the same algorithm structure but with MPI explicit message-passing, then refactors the entire code in §8.6.1 to use collectives. Pedagogically excellent — the reader sees the *same problem* in three forms (sequential, OpenMP, MPI raw send/recv, MPI collectives).
- **The §8.3.2 `findoverallmin` / `disseminateoverallmin` / `updateallmind` functions are deliberately hand-written.** They reappear in §8.6 as the *deletable* code that collectives replace. This is the chapter's *use the API as motivation* pedagogy.
- **Section 8.8 *Use of MPI from Other Languages* is a four-line tease.** Forward-references to Chapter ?? for Python and R bindings — unresolved cross-references, same pattern as Ch7's snow reference.
- **Section 8.9 *Other MPI Examples in This Book* is a 2-bullet pointer list.** Pipelined prime finder (Ch1), bucket sort with sampling (§12.5). Functions as an MPI-readers' index.
- **Chapter length: 26 pages.** A medium-length chapter — longer than Ch7 (6 pages) but shorter than Ch3/4/5 (~38 pages each). Dense with code listings.
