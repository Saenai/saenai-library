# Reference

Lookup material: CLI options, config keys, environment variables, file formats, API fields. Read in pieces, by search or scan, rarely end to end.

File: `docs/reference/<name>.reference.md`. If the authoritative definition already lives somewhere readable (a schema file, `--help` output), link to it instead of duplicating it.

## Skeleton

The `##` sections are the groups that exist in the source; there is no fixed list.

```markdown
# {{Thing}} — Reference

{{One sentence: what this covers and where it is defined in the source.}}

## {{Group, e.g. Arguments}}
## {{Group, e.g. Environment variables}}
## {{Group, e.g. Exit codes}}
## Examples
```

## Rules

- One table per group. Columns: name, type or format, required/default, meaning. Add a column only if most rows use it.
- Keep the order of the source definition, or alphabetical if the source has none.
- Every entry comes from the source. An unknown default is written `unknown` and listed under a final `## Open Questions`.
- Examples are real, minimal and copyable.

## Leave out

Explanations of why (link the design) and internal items that are not part of the interface.
