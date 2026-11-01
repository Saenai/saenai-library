# Activity report

Builds a list of active record IDs from `data/records.csv` and publishes it as a GitHub Actions artifact.

## Quick start

```bash
gh workflow run activity-report.yml
gh run watch
gh run download --name activity-report
```

You get `report.txt` with one ID per line.

## Usage

Run the script locally:

```bash
REPORT_DIR=out bash scripts/build-report.sh data/records.csv
```

| Exit code | Meaning |
| --- | --- |
| 0 | report written to `out/report.txt` (may be empty) |
| 1 | `REPORT_DIR` or the input path not given |
| 2 | input file not readable |

## Related documents

- [Design](docs/design/activity-report.design.md): how the workflow and script behave.
- [Runbook](docs/runbooks/activity-report.runbook.md): running it and fixing failures.
- [Proposed change: reject empty reports](docs/design/reject-empty-report.design.md), and the [decision behind it](docs/adr/0001-fail-empty-report-in-build.md).
