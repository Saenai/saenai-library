# Design

Explains how a component works (**As-Is**) or specifies a change (**To-Be**). Fits anything from one script to a multi-job workflow: the depth varies, the skeleton does not.

File: `docs/design/<name>.design.md`

Examples: [As-Is](../../examples/sample-repo/docs/design/activity-report.design.md), [To-Be](../../examples/sample-repo/docs/design/reject-empty-report.design.md)

## Skeleton

All `##` sections are required, in this order. Write `None.` when one is genuinely empty. Use `###` subsections freely.

```markdown
# {{Component}} — Design (As-Is | To-Be)

Source: {{links to the target files}}
Requirements: {{link; To-Be only}}
Basis: {{what was read; what was run, or "not executed"}}

## Summary
## Context
## Interfaces
## Behavior
## Decisions
## Verification
## Open Questions
```

## Sections

**Summary.** Two to five sentences: what it is, what it does (or what changes), and the most important consequence. To-Be: add a Before / After table of the changed behavior.

**Context.** Where it runs and who calls it: platform, interpreter, trigger, callers, dependencies, constraints from requirements, and what is out of scope. Only what the reader needs for the rest.

**Interfaces.** Everything that crosses the boundary, in one table: arguments, flags, env vars, stdin, input files, outputs, stdout/stderr, exit codes, artifacts, job outputs, permissions. Columns: name, kind, required/default, meaning, consumer. To-Be: only changed interfaces, with Before and After columns, then "Other interfaces are unchanged."

**Behavior.** What happens under which condition. Usually a table with an ID column (`B1`, `B2`, …): condition, behavior, source link. Include failure paths and side effects: partial writes, skipped steps, what downstream sees. If failure effects need more than the table, add `### Failure effects`. A diagram goes here if one helps.

**Decisions.** To-Be: each design choice, its reason, and rejected alternatives, briefly. A decision that will outlive this change belongs in an [ADR](adr.md); link it. As-Is: reasons only if they are recorded somewhere; often `None.`

**Verification.** Table: check, covers (behavior IDs), expected result, status. Status is `Planned`, `Passed (<where>)` or `Failed (<where>)`. A check is `Passed` only if it was run.

**Open Questions.** Facts the reader needs that could not be established, and what each one blocks. As-Is: also behavior that looks risky and deserves a decision, stated as an observation. `None.` is a good outcome.

## Depth

Go deeper only where the risk is.

| Risk | Example | Must cover |
| --- | --- | --- |
| Local | single script, small change | entry, interfaces, main branches, exit codes |
| Integrated | multi-job workflow, script calling services | producer/consumer contracts, skip and failure propagation |
| Consequential | deletes, deploys, data integrity, permissions, concurrency | partial state, re-run behavior, authorization, rollback |

## As-Is and To-Be

- As-Is describes the source as it is. No fixes in the body.
- To-Be describes only the delta and links the As-Is design (or the source) for the rest. Requirements are the authority; a missing business rule is an open question, not a choice to make silently.

## Leave out

Copies of the source, function-by-function walkthroughs, diagrams that repeat a table, and behaviors nobody would ask about.
