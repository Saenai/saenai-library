# ADR (Architecture Decision Record)

Records one significant decision: the situation, the choice, and what it costs. Written once. When a later decision replaces it, add one line under the title, `Superseded by [NNNN](NNNN-....md).`, and leave the body as it was.

File: `docs/adr/NNNN-<decision-in-kebab-case>.md`, numbered in order.

Example: [0001-fail-empty-report-in-build.md](../../examples/sample-repo/docs/adr/0001-fail-empty-report-in-build.md)

## When to write one

When a choice is hard to reverse, affects more than one component, or will be questioned later. Not for a choice fully dictated by a requirement.

## Skeleton

All sections are required, in this order.

```markdown
# NNNN. {{Decision as a short statement}}

## Context
## Decision
## Consequences
## Alternatives Considered
```

## Sections

**Context.** The problem, constraints and requirements that forced a choice. Facts, with links.

**Decision.** The choice in one or two sentences, active voice: "The script exits with code 3 when…".

**Consequences.** What becomes easier, what becomes harder, what new obligation it creates. Include the downsides.

**Alternatives Considered.** Each real alternative and why it lost, one or two sentences each. No straw men; if none were considered, write `None recorded.`

## Leave out

Status fields and dates (Git has them) and implementation detail (link the design).
