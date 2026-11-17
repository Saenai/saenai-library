# Activity Report ワークフロー — 設計書 (As-Is)

ソース: [activity-report.yml](../../../sample-repo/.github/workflows/activity-report.yml), [build-report.sh](../../../sample-repo/scripts/build-report.sh)
根拠: コミット 4f2c9ab 時点のソース。`build-report.sh` はテスト用 CSV でローカル実行した。ワークフローは GitHub 上で実行していない。

## 概要

手動で起動する GitHub Actions ワークフロー。`data/records.csv` から有効なレコードの ID 一覧を作成し、アーティファクト `activity-report` として公開したうえで、2 つ目のジョブでレポートが空でないことを確認する。

**空のレポートは、作成した時点では検出されない。** `active` の行が 1 つもない場合、`build` ジョブは成功して 0 バイトのファイルをアップロードし、`validate` ジョブだけが失敗する。

## インターフェース

| 名前 | 種別 | 必須 / 既定値 | 意味 | 利用側 |
| --- | --- | --- | --- | --- |
| `workflow_dispatch` | トリガー | — | 唯一のトリガー。入力なし | GitHub Actions |
| `$1` | スクリプト引数 | 必須 | 入力 CSV のパス。ワークフローは `data/records.csv` を渡す | `build-report.sh` |
| `REPORT_DIR` | 環境変数 | 必須 | 出力ディレクトリ。ワークフローは `${{ runner.temp }}/report` を設定する | `build-report.sh` |
| 入力 CSV | ファイル | — | ヘッダー行の後に `id,status`。`,` で分割し、引用符は処理しない | `awk` |
| `report.txt` | ファイル | — | 1 行に 1 つの ID。実行のたびに上書き | `Publish report` ステップ |
| exit `1` | 終了コード | — | `$1` または `REPORT_DIR` が未指定。何も作成しない | `Build report` ステップが失敗 |
| exit `2` | 終了コード | — | 入力ファイルを読めない。何も作成しない | `Build report` ステップが失敗 |
| `activity-report` | アーティファクト | — | `report.txt` を含む | `validate` |
| `contents: read` | トークン権限 | — | `build` に設定。`validate` は未設定のためリポジトリの既定値になる | — |

## 動作

| 条件 | 動作 | ソース |
| --- | --- | --- |
| 2 列目が `active` と完全一致する行がない | `awk` が空の `report.txt` を書き、スクリプトは 0 で終了し、`Publish report` が空のファイルをアップロードする | [build-report.sh](../../../sample-repo/scripts/build-report.sh) の `awk`、[ワークフロー](../../../sample-repo/.github/workflows/activity-report.yml)の `Publish report` |
| `build` が成功 | `validate` がアーティファクトをダウンロードし、`report.txt` が空なら実行を失敗させる | ワークフローの `Require nonempty report` |
| `build` のいずれかのステップが失敗 | `build` の残りのステップと `validate` ジョブ全体がスキップされる | ワークフローの `needs: build`（`if` なし） |

実行の外には何も変更を残さない。`report.txt` の書き込み先は `runner.temp` で、ホストランナーとともに破棄されるため、再実行しても安全である。

## 未解決事項

- 空のレポートは正しい結果か。現状、`build` は正常として扱い、`validate` はエラーとして扱う。
- CSV はすべての `,` で分割され、引用符は処理されない。これは合意済みの入力形式か。
