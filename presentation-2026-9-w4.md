---

marp: true
theme: default
paginate: true
size: 16:9
title: AI News Weekly
description: GPT-6 Sol/Luna, Claude Opus 5.5 and Jev
style: |
section {
font-family: "Noto Sans JP", "Yu Gothic", sans-serif;
padding: 56px 70px;
font-size: 29px;
line-height: 1.45;
}

h1 {
font-size: 48px;
margin-bottom: 28px;
}

h2 {
font-size: 34px;
}

table {
font-size: 23px;
}

blockquote {
border-left: 6px solid #555;
padding-left: 24px;
font-size: 34px;
font-weight: 600;
}

.small {
font-size: 19px;
}

.tiny {
font-size: 15px;
}

.big {
font-size: 48px;
font-weight: 700;
}

.center {
text-align: center;
}

.columns {
display: grid;
grid-template-columns: 1fr 1fr;
gap: 48px;
}

.three-columns {
display: grid;
grid-template-columns: 1fr 1fr 1fr;
gap: 32px;
}

.card {
border: 1px solid #bbb;
border-radius: 12px;
padding: 22px;
}

.muted {
color: #666;
}

.source {
position: absolute;
bottom: 28px;
left: 70px;
font-size: 14px;
color: #777;
}

---

<!-- _class: lead -->

# 今週のAIニュース

## 「もっと賢く」だけではない

### 知能が、速く・安く・software-nativeになっていく

**GPT-6 Sol / Luna · Claude Opus 5.5 · Jev**

2026-09

<!--
話すポイント:
今週は単純な「新モデル紹介」ではなく、
知能の価格と使われ方が変わっている、という一つのテーマで見る。
-->

---

# 今週の3つのニュース

<div class="three-columns">

<div class="card">

## GPT-6

### Sol / Luna

**ほぼ同等以上の能力を
約半額で提供**

</div>

<div class="card">

## Claude

### Opus 5.5

**Agentic Codingを中心に
高性能 + 低コスト化**

</div>

<div class="card">

## Jev

**文章ではなく
「判断」を返すAI**

</div>

</div>

<br>

> 共通テーマは **Intelligence per Dollar**

<!--
話すポイント:
能力上限そのものよりも「同じ能力をいくらで提供できるか」が
急速に重要になっている。
-->

---

# GPT-6 Sol / Luna

## また半額になりました

| Model          | Input / 1M | Output / 1M |
| -------------- | ---------: | ----------: |
| GPT-5.6 Sol    |      $4.00 |      $20.00 |
| **GPT-6 Sol**  |  **$2.00** |  **$10.00** |
| GPT-5.6 Luna   |      $0.20 |       $1.20 |
| **GPT-6 Luna** |  **$0.10** |   **$0.50** |

<div class="big center">
約 50% OFF
</div>

<div class="source">
Source: OpenAI, "Introducing GPT-6 Sol and Luna", Sep. 22 2026
</div>

<!--
話すポイント:
5.6自体がかなり安くなったばかりなのに、さらに短期間で半額。
最近はモデル名より価格表の寿命の方が短い気がする。
-->

---

# OpenAIは何の魔法を使ったのか？

公式説明では：

* **Inference efficiency の改善**
* **Prompt caching の改善**
* GPT-6では cached input が通常価格の **90% OFF**
* reasoning effort や tool構成を変えても
  cacheを維持しやすくなった

<br>

> 魔法というより、
> **モデルだけでなく serving stack 全体の効率化**

<div class="source">
Source: OpenAI — GPT-6 Sol/Luna announcement & Prompt Caching update
</div>

<!--
話すポイント:
モデルの学習だけではなく、推論基盤・キャッシュまで含めて改善している。
AIのコスト競争はモデル単体の競争ではなくなっている。
-->

---

# 性能はどう変わった？

## Artificial Analysis — max vs max

|                    | GPT-5.6 Sol |       GPT-6 Sol | GPT-5.6 Luna |      GPT-6 Luna |
| ------------------ | ----------: | --------------: | -----------: | --------------: |
| Intelligence Index |          47 |          **48** |       **37** |          **37** |
| Output speed       |  80.3 tok/s | **124.9 tok/s** |  142.9 tok/s | **150.5 tok/s** |
| Cost / task        |       $1.99 |       **$1.06** |        $0.18 |       **$0.07** |

<br>

### 大きな能力ジャンプではない

### しかし **同じ知能の価格が急落**

<div class="source">
Source: Artificial Analysis — GPT-6 vs GPT-5.6 comparisons
</div>

<!--
話すポイント:
総合スコアだけを見ると大きく変わっていない。
今回の最大の進歩は「同じ能力を圧倒的に安く提供すること」。
-->

---

# 「性能据え置き」は進歩していない？

<div class="columns">

<div>

## 従来の見方

新モデルなら

* benchmark ↑
* reasoning ↑
* coding ↑

でなければ
「進化していない」

</div>

<div>

## 今回の見方

同じ仕事を

* **半額**
* より高速に
* より高いusage limitで

処理できる

### → これも十分大きな進化

</div>

</div>

<br>

> AIにおいて **価格性能比の改善 = 能力の民主化**

<!--
話すポイント:
業務利用ではベンチマーク1点より、同じ予算で何件処理できるかの方が重要。
-->

---

# Lunaは特に象徴的

## GPT-6 Luna

* Intelligence Index: **37 → 37**
* Output: **$1.20 → $0.50**
* Cost / task: **$0.18 → $0.07**
* Output speed: **約143 → 151 tok/s**

つまり：

<div class="big center">
同じ知能が、より安く大量に使える
</div>

<div class="small">
※ max reasoningではTTFTやtask全体時間が必ずしも改善しているわけではない。
「すべてが高速化」とは言えない点には注意。
</div>

<!--
話すポイント:
Lunaは「品質を捨てて安くしたモデル」ではない。
むしろ一定水準の知能そのものがcommodity化している例。
-->

---

# そして Claude Opus 5.5

## Anthropicも efficiency を強化

|                   | Opus 5 | **Opus 5.5** |
| ----------------- | -----: | -----------: |
| Input / 1M        |     $5 |       **$4** |
| Output / 1M       |    $25 |      **$20** |
| Cache read / 1M   |  $0.50 |    **$0.20** |
| Typical task cost |      — |   **約40%低下** |
| Output speed      |      — | **30%以上高速化** |

<br>

> Frontier競争が
> **「一番賢いモデル」→「一仕事いくらか」**
> に移りつつある

<div class="source">
Source: Anthropic, "Claude Opus 5.5", Sep. 22 2026
</div>

---

# Opus 5.5：Software Engineeringが特に強い

| Benchmark              |  Opus 5.5 | Fable 5.1 | GPT-6 Astra |
| ---------------------- | --------: | --------: | ----------: |
| Terminal-Bench 4.0     | **66.4%** |     55.8% |       57.9% |
| FrontierCode 1.1       | **54.4%** |     50.3% |       53.3% |
| Terminal-Bench-Science |     58.7% |     52.6% |   **64.6%** |

<br>

### SWEでは非常に強い

しかし：

> **一つのbenchmark群で勝つ = 通用能力で常に一番**
> ではない

<div class="source">
Source: Anthropic published evaluation results
</div>

<!--
話すポイント:
Opus 5.5はcodingだけではなくknowledge workも強い。
ただし「Astraを超えたモデル」と単純化するのは危険。
ScienceではAstraが上。
モデル選択は用途別に考える。
-->

---

# 今後のモデル選択

## 「どれが一番賢い？」から

### ↓

## 「この仕事を、いくらで、どの品質で終わらせる？」

<div class="three-columns">

<div class="card">

### Luna

大量・低コスト

日常処理
分類
軽い調査

</div>

<div class="card">

### Sol / Opus

複雑な業務

Coding
Agent
調査・実装

</div>

<div class="card">

### Astra / Frontier

最高難度

研究
難問
失敗コストが高い仕事

</div>

</div>

<!--
話すポイント:
今後はモデルランキングより workload × cost のマッピングが重要。
-->

---

<!-- _class: lead -->

# でも、そもそも……

## その仕事に

# 「文章生成」は必要でしょうか？

<!--
話すポイント:
ここでJevへ転換。
多くのenterprise automationは作文ではなく判断が必要。
-->

---

# Jevとは？

## TypeSafe AI が公開した

## 最初の **System One Model**

LLM：

> 状況を読んで、文章を生成する

Jev：

> 状況を読んで、
> **型付きの判断 + probability** を返す

<br>

### `"Decision, not strings"`

<div class="source">
Source: TypeSafe AI, "Introducing System One Models & Jev", Sep. 15 2026
</div>

---

# System One Model

名前の由来：

### Daniel Kahneman

**Thinking, Fast and Slow**

* System 1
  → 速い・直感的な判断
* System 2
  → 遅い・熟考型の推論

<br>

TypeSafeの発想：

> すべての処理に
> 「長いreasoning + text generation」は必要ない

<!--
話すポイント:
System Oneは「低知能」という意味ではなく、
対象タスクを判断に限定して設計そのものを変える発想。
-->

---

# Jevの出力

## 例：Incident Routing

### LLM

```text
Based on the logs and previous incidents,
I believe this issue is most likely...
```

### Jev

```json
{
  "Application": 0.08,
  "Database": 0.74,
  "Network": 0.12,
  "HumanReview": 0.06
}
```

<br>

> **Unstructured state in → Typed decision out**

---

# Jevの3つのPrimitive

<div class="three-columns">

<div class="card">

## Noul

### Yes / No

`Escalate?`

YES 0.91
NO 0.09

</div>

<div class="card">

## Choice

### 選択

`Which team?`

APP 0.10
DB 0.75
NW 0.15

</div>

<div class="card">

## Score

### 評価

`Risk?`

8.2 / 10
Confidence 0.88

</div>

</div>

<br>

普通のprogram logicから見ると：

### **AI-powered if statement**

---

# なぜそんなに速くて安い？

## LLM

```text
token1 → token2 → token3 → token4 → ...
```

Autoregressive
逐次生成

## Jev

```text
Decision A
Decision B
Decision C
Decision D
```

**並列出力**

<br>

|                 |                    Jev |
| --------------- | ---------------------: |
| Input           | **$0.042 / 1M tokens** |
| Output          |               **Free** |
| Typical latency |          **70–500 ms** |

<div class="source">
Source: TypeSafe AI — launch announcement
</div>

---

# Jevという名前にも意味がある

## William Stanley Jevons

### Jevons Paradox

効率が改善
↓
単位コストが下がる
↓
使う量が減る……

### とは限らない

<div class="big center">
むしろ用途が増え、総需要が増える
</div>

<!--
話すポイント:
蒸気機関が石炭を効率化した結果、石炭消費が増えたという有名な考え方。
TypeSafeはmachine intelligenceでも同じことが起こると考えている。
-->

---

# AIでも Jevons Paradox？

## Lunaが半額になったから

### AI予算が半額になる？

<br>

### おそらく逆

今まで高すぎてAIを使わなかった

* 小さな分類
* routing
* scoring
* validation
* monitoring
* guardrail

にもAIを入れられる

<br>

> **AIの単価 ↓ → AIを使う場所 ↑↑**

---

# Jevは「Hallucinationしない」？

## TypeSafeの主張

### "Zero hallucinations"

ただし意味を分ける必要がある。

<div class="columns">

<div class="card">

## ✅ 保証できること

* schema外の出力をしない
* type errorを起こさない
* 定義外の文字列を生成しない

</div>

<div class="card">

## ❌ 保証できないこと

* 判断が常に正しい
* probabilityが完全
* semantic errorがゼロ

</div>

</div>

<br>

> **Type-safe ≠ Correct**

<!--
話すポイント:
例えばCRITICALをNORMALと判断することはあり得る。
「hallucinationゼロ」は通常のLLM文脈の意味で受け取らない方がいい。
-->

---

# Jevの数字は面白い。しかしまだ新しい

TypeSafeの自社workflow評価：

<div class="big center">
193.6× faster  
444.6× cheaper
</div>

しかし公式自身も：

* workflowによる
* 実世界改善の **high end**
* 自社チーム作成evalによるbias可能性
* Jevはまだ **Early Access**

と明記

<br>

> 面白い新しいprimitive
> ≠ すでにLLMを置き換えた技術

<div class="source">
Source: TypeSafe AI — published workflow evaluation
</div>

---

# 私たちの仕事では？

## 「生成」より「小さな判断」が多い

| Process                 | Decision AI の候補                    |
| ----------------------- | ---------------------------------- |
| Jira受付                  | Category / Priority / 担当候補         |
| 調査                      | 既知障害 / 新規問題 / 追加調査                 |
| Agent実行                 | Continue / Retry / Stop / Escalate |
| Unit / Integration Test | Code / Data / Env / Flaky          |
| Review                  | Risk score / 追加review要否            |
| Release                 | Check結果の分類・escalation              |
| Monitoring              | Ignore / Investigate / Escalate    |

<!--
話すポイント:
いきなりJev導入という意味ではない。
「判断を文章生成モデルから分離する」という設計思想が重要。
-->

---

# 今後あり得るAI Architecture

```text
┌──────────────────────────────┐
│      Deterministic Code      │
│     明確なルール・計算       │
└──────────────┬───────────────┘
               ↓
┌──────────────────────────────┐
│    Cheap Decision Model      │
│ classify / score / route     │
└──────────────┬───────────────┘
               ↓
┌──────────────────────────────┐
│     General-purpose LLM      │
│   Luna / Sol / Opus etc.     │
└──────────────┬───────────────┘
               ↓
┌──────────────────────────────┐
│      Frontier Model          │
│ Astra / high-cost reasoning  │
└──────────────┬───────────────┘
               ↓
┌──────────────────────────────┐
│            Human             │
│ judgment / approval / owner  │
└──────────────────────────────┘
```

### 難しい処理だけ上へEscalateする

---

# ただし、仕事で使うなら

## 技術だけでは決まらない

特に新しい外部AIサービスでは：

* Customer / Security approval
* 送信可能なデータ範囲
* Data retention
* Data residency
* SLA / Availability
* Auditability
* 誤判定時の責任
* Human review threshold

が必要

<br>

> **「使える」ことと「使ってよい」ことは別**

<!--
話すポイント:
顧客環境ではここが非常に重要。
最初のPOCならsynthetic / anonymized data、
ticket routingやtest failure classification等が安全。
-->

---

# 今週のニュースを一枚で

<div class="three-columns">

<div class="card">

## Cost ↓

Sol / Luna
Opus 5.5

**同じ知能が
急速に安くなる**

</div>

<div class="card">

## Specialization ↑

Opus 5.5

**用途別の強さが
より重要になる**

</div>

<div class="card">

## Granularity ↓

Jev

**小さな判断にも
AIを入れられる**

</div>

</div>

<br>

# Intelligence is becoming infrastructure.

---

# Takeaway

昔：

> **どのAIが一番賢いか？**

これから：

> **どの仕事を、どのAIに、
> いくらで任せるべきか？**

そしてさらに：

> **そもそも、この判断に
> LLMを使う必要があるのか？**

---

<!-- _class: lead -->

# 知能そのものが

# Software Component になり始めている

モデルが安くなるほど
AIを使う場所は減るのではなく

## むしろ増えるかもしれない

**Jevons Paradox for Intelligence**

---

# Sources / Notes

### Primary sources

* OpenAI
  *Introducing GPT-6 Sol and Luna* — Sep. 22, 2026
* Anthropic
  *Claude Opus 5.5* — Sep. 22, 2026
* TypeSafe AI
  *Introducing System One Models & Jev* — Sep. 15, 2026

### Independent benchmark reference

* Artificial Analysis
  GPT-6 Sol / Luna vs GPT-5.6 comparisons

### Caution

* Benchmark results depend on **harness / reasoning effort / tools / evaluation setup**
* Cross-vendor scores should not be interpreted as absolute model rankings
* Jev performance claims are still mainly based on **vendor-published evaluations**

---

<!-- _class: lead -->

# Thank you

### Questions / Discussion
