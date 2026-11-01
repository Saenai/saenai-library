# Shell scripts and CI workflows

What to look for when documenting Shell scripts and workflow YAML. Use it together with the design or runbook type.

## Find the real boundary

- **Who runs it.** A script may be run by a person, cron/systemd, a CI step or another script. Find the actual invocation (`bash file`, `sh file`, `source file`, or the shebang). The interpreter that actually runs it is what counts.
- **Which platform.** A `.yml` file alone does not tell you whether it is GitHub Actions, GitLab CI, Azure Pipelines or something else. Name the platform in Context, and do not carry one platform's semantics into another.
- **Where values are expanded.** YAML anchors, CI expressions (`${{ }}`), templating and shell expansion happen at different phases. Say which phase a value goes through when it matters.
- **What it calls.** Read called scripts and reusable workflows that are in the repository. For third-party actions or remote services you cannot read, describe the configured inputs and say the behavior comes from their documentation.

## Shell: what to capture

| Look at | Capture |
| --- | --- |
| Positionals, flags, env, stdin, input files, working directory | required or optional, default, format |
| `if`, `case`, `&&`, `\|\|`, loops, early `exit`/`return` | each condition and its outcome, including skips |
| `exit`, `set -e`/`-u`/`-o pipefail`, `trap` | which failures stop the script, and with what code |
| Writes, deletes, moves, network, database, deploys | target, order, what is left behind on failure |
| Locks, temp files, overwrite or append | what happens when run twice, or after a partial run |
| stdout, stderr, output files, exit code | who consumes each |

Pitfalls to check (mention one only when it applies):

- `set -e` does not stop the script for a failure inside an `if` condition or an `&&`/`||` list, and without `pipefail` only the last command of a pipeline counts.
- `> file` truncates before the command runs; a failure leaves an empty or partial file.
- `source` runs in the current shell and can change its variables; a child process cannot.
- `trap ... EXIT` does not run on `kill -9`.
- Relative paths depend on the caller's working directory.
- Exit 0 means the commands succeeded, not that the output is right.

## Workflow YAML: what to capture

| Look at | Capture |
| --- | --- |
| Events, schedules, branch/path filters, manual inputs | when it runs, and when it does not |
| Jobs, stages, `needs`, includes, reusable workflows | dependency edges; what can run in parallel |
| Job/step `if`, `rules`, `continue-on-error`, `allow_failure` | when something runs, is skipped, or may fail |
| Runner, container, default shell, checkout path | where commands run and where files are |
| Inputs, env, outputs, artifacts, caches | producer, consumer, and expansion phase |
| Token permissions, environments, secrets (by name) | which identity can do what |
| Uploads, releases, deploys, tags, external calls | what changes outside the run; partial outcomes |

Platform notes:

- **GitHub Actions.** A job with `needs` is skipped when a needed job fails, unless its `if` uses `always()` or `failure()`. A step after a failed step is skipped unless its `if` says otherwise. A job without `permissions` gets the workflow-level setting, or else the repository default.
- **GitLab CI.** Stages order jobs unless `needs` creates a DAG. `rules` and `allow_failure` change what a failure means downstream.
- Includes, templates and YAML anchors can change the effective configuration from outside the file you were given.

## When a workflow calls a script

Document the interface between them (arguments, env, files, exit code) once, in the document of whichever side owns it. Do not describe both bodies in full.
