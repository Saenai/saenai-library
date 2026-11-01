#!/usr/bin/env bash
set -euo pipefail

input="${1:?Input CSV path is required}"
output_dir="${REPORT_DIR:?REPORT_DIR is required}"

if [[ ! -r "$input" ]]; then
  printf 'Cannot read input: %s\n' "$input" >&2
  exit 2
fi

mkdir -p "$output_dir"
awk -F, 'NR > 1 && $2 == "active" { print $1 }' "$input" > "$output_dir/report.txt"
