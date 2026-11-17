# Activity Report Workflow — Design (As-Is)

Source: [activity-report.yml](../../.github/workflows/activity-report.yml), [build-report.sh](../../scripts/build-report.sh)
Basis: source at commit 4f2c9ab. `build-report.sh` was run locally against test CSV files; the workflow was not run on GitHub.

## Summary

A manually triggered GitHub Actions workflow builds a list of active record IDs from `data/records.csv`, publishes it as the artifact `activity-report`, and checks in a second job that the report is not empty.

**An empty report is not caught where it is made.** If no row is `active`, the `build` job succeeds and uploads a zero-byte file; only the `validate` job fails.

## Interfaces

| Name | Kind | Required / default | Meaning | Consumer |
| --- | --- | --- | --- | --- |
| `workflow_dispatch` | trigger | — | the only trigger; no inputs | GitHub Actions |
| `$1` | script argument | required | input CSV path; the workflow passes `data/records.csv` | `build-report.sh` |
| `REPORT_DIR` | env var | required | output directory; the workflow sets `${{ runner.temp }}/report` | `build-report.sh` |
| input CSV | file | — | header row, then `id,status`; split on `,`, quotes not handled | `awk` |
| `report.txt` | file | — | one ID per line; overwritten each run | `Publish report` step |
| exit `1` | exit code | — | `$1` or `REPORT_DIR` missing; nothing is created | `Build report` step fails |
| exit `2` | exit code | — | input file not readable; nothing is created | `Build report` step fails |
| `activity-report` | artifact | — | contains `report.txt` | `validate` |
| `contents: read` | token permission | — | set on `build`; `validate` sets none and gets the repository default | — |

## Behavior

| Condition | Behavior | Source |
| --- | --- | --- |
| no row has a second field of exactly `active` | `awk` writes an empty `report.txt`, the script exits 0, and `Publish report` uploads the empty file | [build-report.sh](../../scripts/build-report.sh) `awk`; [workflow](../../.github/workflows/activity-report.yml) `Publish report` |
| `build` succeeds | `validate` downloads the artifact and fails the run if `report.txt` is empty | workflow `Require nonempty report` |
| any step of `build` fails | the remaining steps of `build` and the whole `validate` job are skipped | workflow `needs: build`, no `if` |

Nothing outside the run changes. `report.txt` is written under `runner.temp`, which is discarded with the hosted runner, so a re-run is safe.

## Open Questions

- Is an empty report a valid result? `build` treats it as valid and `validate` as an error.
- The CSV is split on every `,` and quotes are not handled. Is that the agreed input format?
