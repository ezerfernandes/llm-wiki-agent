---
title: "`exec` (POSIX Process Image Replacement)"
type: concept
tags: [posix, unix, process, system-call, operating-system, c]
sources: [dis-13-2-processes]
last_updated: 2026-05-17
---

# `exec` (POSIX Process Image Replacement)

[[OperatingSystem|POSIX]] family of [[SystemCall|system calls]] (`execvp`, `execve`, `execl`, `execlp`, `execv`, `execvpe`, ...) that **replaces the calling [[Process|process]]'s image** with a new program. The PID does **not** change; everything else does — text segment, data segment, [[CallStack|stack]], [[Heap|heap]], and the [[CpuRegister|register]] snapshot are reinitialized to the new executable's entry point.

Canonical signature ([[dis-13-2-processes|DIS Ch 13.2]]):

```c
int execvp(char *filename, char *argv[]);
```

## Semantics

- **Overwrites** the process's [[ProcessMemory|address space]] with the specified executable.
- **Reinitializes** execution state to start at the program's first instruction.
- **On success — does not return.** There is no caller to return to; the caller's code no longer exists in memory.
- **On failure — returns `-1`** with `errno` set (file not found, not executable, etc.). This is the *only* way `exec` returns.
- **PID preserved**; open file descriptors preserved by default (subject to close-on-exec flag); parent / child relationship preserved.

## Canonical idiom — fork + exec

```c
pid_t pid = fork();
if (pid == 0) {
    /* child */
    execvp("/bin/ls", (char *[]){"ls", "-l", NULL});
    perror("execvp");     /* only reached if exec fails */
    exit(127);
} else {
    /* parent */
    int status;
    waitpid(pid, &status, 0);
}
```

The **[[Fork|`fork`]] + `exec` pattern** is how every Unix shell launches a command: `fork` creates a new process that is a duplicate of the shell; the child immediately `exec`s the target program, becoming that program with the same PID. The shell parent then [[Wait|`wait`s]] for the child.

## The `exec` family naming convention

`exec` + suffix letters:

- **`l`** — args passed as **l**ist of separate arguments (`execl(path, arg0, arg1, ..., NULL)`).
- **`v`** — args passed as **v**ector (`char *argv[]`).
- **`p`** — uses `PATH` environment variable to find the executable.
- **`e`** — explicit **e**nvironment array (`char *envp[]`).

`execve` is the lowest-level — the actual kernel syscall the library variants wrap.

## Connections

- [[dis-13-2-processes]] — primary source.
- [[Fork]] — paired primitive; together implement the Unix process-spawn pattern.
- [[Wait]] — the parent-side reaper after `fork+exec`.
- [[Process]] / [[ProcessMemory]] — what `exec` rewrites.
- [[ProcessID]] — preserved across `exec`.
- [[SystemCall]] — the kernel surface `execve` lives on.
- [[OperatingSystem]] — owner of the call.
- [[Exit]] / [[ExitStatus]] — paired with the fallback path when `exec` fails.
- [[CLanguage]] — host language of the API (`<unistd.h>`).
