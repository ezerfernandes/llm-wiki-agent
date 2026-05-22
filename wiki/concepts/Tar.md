---
title: "tar"
type: concept
tags: [unix, archive, compression, command-line]
sources: [dis-app2-8-tar]
last_updated: 2026-05-18
---

# tar

**`tar`** (originally *tape archiver*) bundles a tree of files into a single archive file (`.tar`). Optionally pipelined through gzip or bzip2 compression.

Per [[dis-app2-8-tar|DIS Appendix 2.8]], `tar` is the canonical Unix packaging step before bulk transfer ([[SCP|`scp`]]) or distribution.

## Core operations

| Operation | Command |
|---|---|
| Create | `tar -cvf archive.tar file1 file2 dir/` |
| Extract | `tar -xvf archive.tar` |
| List contents | `tar -tvf archive.tar` |

## Flag reference

| Flag | Meaning |
|---|---|
| `-c` | create archive |
| `-x` | extract archive |
| `-t` | list contents |
| `-v` | verbose (print filenames as they're processed) |
| `-f` | next argument is the archive filename |
| `-z` | gzip compress / decompress |
| `-j` | bzip2 compress / decompress |
| `-J` | xz compress / decompress |

Flags are routinely concatenated: `-czvf` is `-c -z -v -f` collapsed.

## Compressed variants

```bash
tar -czvf project.tar.gz mydir/     # gzip create
tar -xzvf project.tar.gz            # gzip extract
tar -cjvf project.tar.bz2 mydir/    # bzip2 create
tar -xjvf project.tar.bz2           # bzip2 extract
```

## Composition with scp

Canonical pre-transfer recipe per DIS Appendix 2.3:

```bash
tar -czvf bundle.tar.gz mydir/
scp bundle.tar.gz user@host:~/
ssh user@host 'tar -xzvf bundle.tar.gz'
```

## Related
- [[SCP]] — typical downstream tool.
- [[UnixCommandLine]] — invocation context.
- [[DiveIntoSystems]] — Appendix 2.8.

## Sources
- [[dis-app2-8-tar]] — DIS Appendix 2.8 *tar*.
