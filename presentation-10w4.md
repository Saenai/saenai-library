---
marp: true
theme: default
size: "16:9"
paginate: true
lang: ja
title: AI Update 2026.09–10 — 高性能AIが「個人の道具」になった
description: 2026年9月28日〜10月30日のAI動向。モデルの能力とコスト、科学研究、個人・コミュニティの技術的突破、セキュリティと開発運用への示唆。
header: AI UPDATE / 2026.09–10
footer: 2026-10-30 時点 ｜ チーム共有
style: |
  section {
    background-color: #f7f9fc;
    background-image: linear-gradient(90deg, #173451 0%, #173451 76%, #129d94 76%, #129d94 100%);
    background-repeat: no-repeat;
    background-size: 100% 7px;
    color: #172b41;
    font-family: "Noto Sans CJK JP", "Yu Gothic", "Meiryo", sans-serif;
    font-size: 27px;
    line-height: 1.55;
    padding: 70px 72px 68px;
    justify-content: center;
    letter-spacing: 0.01em;
  }
  h1 {
    color: #173451;
    font-size: 41px;
    line-height: 1.3;
    letter-spacing: -0.025em;
    margin: 0 0 28px;
    border: 0;
  }
  h2 { color: #087e78; font-size: 31px; line-height: 1.35; margin: 20px 0 16px; }
  h3 { color: #173451; font-size: 25px; margin: 20px 0 10px; }
  p { margin: 12px 0; }
  strong { color: #087e78; font-weight: 700; }
  a { color: #126d9a; text-decoration: none; }
  ul, ol { padding-left: 1.3em; margin: 12px 0; }
  li { margin: 8px 0; }
  li > p { margin: 0; }
  blockquote {
    border-left: 5px solid #129d94;
    background: #eaf2f5;
    color: #173451;
    padding: 14px 22px;
    margin: 24px 0 0;
    font-size: 28px;
    font-weight: 600;
  }
  blockquote p { margin: 0; }
  table {
    width: 100%;
    display: table;
    font-size: 23px;
    line-height: 1.45;
    border-collapse: collapse;
    margin: 18px 0;
  }
  th { background: #173451; color: #ffffff; font-weight: 600; }
  td, th { border: 0; border-bottom: 1px solid #d5dfe9; padding: 12px 16px; }
  tr:nth-child(2n) { background: #edf2f7; }
  tr:nth-child(2n+1) { background: #ffffff; }
  td strong { color: #087e78; }
  code { background: #e6edf3; color: #173451; font-size: 0.83em; padding: 0.12em 0.3em; }
  header { top: 27px; left: 72px; color: #64758a; font-size: 14px; letter-spacing: 0.12em; }
  footer { bottom: 22px; left: 72px; right: 92px; color: #66778a; font-size: 13px; letter-spacing: 0; }
  section::after { right: 35px; bottom: 20px; color: #66778a; font-size: 15px; }
  section.cover, section.takeaway {
    background-color: #10283f;
    color: #ecf3fa;
    background-image: linear-gradient(90deg, #129d94 0%, #129d94 25%, #27465f 25%, #27465f 100%);
  }
  section.cover h1 { color: #ffffff; font-size: 56px; line-height: 1.45; margin-bottom: 30px; }
  section.cover h2 { color: #63d3c8; font-size: 26px; font-weight: 500; }
  section.cover p { color: #b8cbdb; font-size: 23px; }
  section.cover header, section.cover footer, section.cover::after,
  section.takeaway header, section.takeaway footer, section.takeaway::after { color: #9eb5c9; }
  section.takeaway h1 { color: #ffffff; font-size: 46px; }
  section.takeaway strong { color: #63d3c8; }
  section.takeaway blockquote { background: #1c3a53; color: #ffffff; }
  section.compact { font-size: 25px; }
  section.compact table { font-size: 21px; }
  section.compact td, section.compact th { padding: 10px 13px; }
  section.metric h2 { font-size: 57px; line-height: 1.25; letter-spacing: -0.03em; }
  section.references { font-size: 20px; line-height: 1.45; }
  section.references h1 { font-size: 35px; margin-bottom: 20px; }
  section.references table { font-size: 18px; line-height: 1.4; }
  section.references td, section.references th { padding: 9px 12px; }
  section.references p { font-size: 18px; color: #64758a; }
---

<!-- _class: cover -->
<!-- _paginate: false -->
<!-- _header: AI UPDATE / SEPTEMBER–OCTOBER 2026 -->

# 高性能AIが、
# 「個人の道具」になった

## 能力の向上 × コストの低下が変える、研究・開発・セキュリティ

2026.09.28–10.30 ｜ チーム向け情報共有

<!--
今日は約1か月分のAIニュースを、モデル名の紹介ではなく「何ができるようになり、誰がそれを実行できるようになったか」という観点で共有します。
特に、個人や小規模コミュニティが市販のAIを利用して、大手企業の製品の内部に踏み込めるようになった事例を見ます。その後、私たちの開発・保守への意味を考えます。
公開情報の確認日：2026-10-30。社内環境に関する記述は発表者提供情報です。
-->

---

<!-- _header: OVERVIEW / 今月の見方 -->
<!-- _footer: '根拠となる事例：[S03 Terra](https://openai.com/index/introducing-gpt-6-1-terra/) ／ [S08 Switch 2](https://pepsipu.com/blog/2026-10-switch2-jailbreak-ns2jb/)' -->

# 変化は「より賢い」だけではない

| 変化 | 注目する点 |
|---|---|
| **能力が上がる** | 調査・実装・操作・検証を、連続した作業として扱う |
| **実行コストが下がる** | 同じ予算で、より多くの仮説と修正を試せる |
| **使い手が広がる** | 個人・小規模チームも、高度な研究を進められる |

> 大手の製品でも、「個人には解析しきれない」を前提にできなくなる。

<!--
下段は今回の事例から導く見方です。「個人が大手製品を解析すること自体が今年初めて」という意味ではありません。
変化の中心は、専門家がAIと分担し、解析・実装・試行を反復できる範囲が広がっていることです。攻撃だけでなく、保守・監査・互換性研究にも同じ能力が使えます。
価格低下の根拠と突破事例の根拠は別です。以下の個別研究について、利用料金や総費用が公表されているとは限りません。
-->

---

<!-- _header: 01 / MODEL & COST -->
<!-- _class: compact -->
<!-- _footer: '出典：[S01 Sonnet](https://www.anthropic.com/claude-sonnet-5-5) ／ [S02 Haiku](https://www.anthropic.com/claude-haiku-5-5) ／ [S03 Terra](https://openai.com/index/introducing-gpt-6-1-terra/)' -->

# モデル更新：上位能力が、速く・安くなる

| 公開日 | モデル | 今回のポイント |
|---|---|---|
| 9/28 | **Claude Sonnet 5.5** | 日常の開発・資料作成。前世代より高速・省トークン |
| 10/7 | **Claude Haiku 5.5** | 要約・分類・サブエージェントなど、大量処理向け |
| 10/26 | **GPT-6.1 Terra** | 視覚理解・Computer Use・文章作成。Solより低単価 |

**社内環境でも GPT-6.1 Sol が利用可能に。**

外部のニュースを眺めるだけでなく、業務で試せる段階へ。

<!--
Computer Useは、画面を読み、マウスやキーボード等を操作して複数段階の作業を進める能力です。
Terraを「Solより全面的に高性能」とは紹介しません。得意な作業、速度、コストの組み合わせが異なります。
社内のSol利用可否は発表者からの情報で、公開資料による確認事項ではありません。公開APIの料金を社内環境の課金にそのまま当てはめないでください。
公式発表：S01、S02、S03。Terra公開日の補助確認：公式開発者コミュニティの2026-10-26の公開案内。
-->

---

<!-- _header: 01 / MODEL & COST -->
<!-- _footer: '提供元公表値・評価条件は別：[S01 Sonnet 5.5](https://www.anthropic.com/claude-sonnet-5-5) ／ [S03 GPT-6.1 Terra](https://openai.com/index/introducing-gpt-6-1-terra/)' -->

# 「単価」と「仕事1件の費用」は違う

| 比較 | 公表されている変化 | 読み方 |
|---|---|---|
| Sonnet 5 → **5.5** | 生成速度 **30%以上向上**／タスク費用 **最大約30%減** | 少ないトークンで同じ仕事をこなす |
| Sol 6.1 → **Terra 6.1** | 標準APIのトークン単価 **50%減** | 得意分野に合えば低コスト化できる |

**業務で見る指標：合格した成果物1件あたりの総費用**

モデル料金 ＋ 再試行 ＋ ツール実行 ＋ 人の確認・修正

<!--
数字は各社が公表した条件での比較であり、私たちの業務で測定した値ではありません。
Sonnetの改善は、入力・出力の基本単価を下げた効果だけではなく、タスクに必要なトークン量や速度の改善です。Terraの50%は標準APIの単価比較です。
低単価モデルでも何度もやり直せば高くなり、高性能モデルで一度で終われば安くなることがあります。社内で比較するなら、同じ課題と合格条件を使います。
-->

---

<!-- _header: 01 / MODEL & COST -->
<!-- _footer: '出典：[S04 Anthropic Pricing](https://platform.claude.com/docs/en/about-claude/pricing) ｜ USD / 100万tokens、標準API、2026-10-30確認' -->

# Haiku 5.5：100Kを超えると料金帯が変わる

| 1リクエストの入力長 | 入力単価 | 出力単価 | キャッシュ読込 |
|---|---:|---:|---:|
| **100,000 tokens 以下** | $0.10 | $0.50 | $0.01 |
| **100,000 tokens 超** | $0.50 | $2.50 | $0.05 |

**超過した分だけではなく、そのリクエストが高い料金帯になる。**

入力長の判定には、キャッシュの読み書きも含まれる。

> 短い定型処理では強い。長時間エージェントでは履歴の設計も重要。

<!--
Haikuが一律に「安くない」ということではありません。短い入力では非常に低価格ですが、入力長の境界により各単価が5倍になります。
境界を超える前の過去リクエストまで遡って再課金されるわけではありません。リクエストごとの判定です。
ここでは標準料金だけを示しています。Batch割引、キャッシュ書込料金、地域別条件、社内環境の料金は別です。
-->

---

<!-- _header: 02 / SCIENCE -->
<!-- _class: metric -->
<!-- _footer: '出典：[S05 OpenAI公開資料](https://openai.com/index/sharing-ai-progress-in-mathematics/) ／ [S06 初回公開数の研究レビュー](https://arxiv.org/abs/2610.17090) ／ [S07 改訂履歴](https://github.com/openai/math/blob/main/history.md)' -->

# 数学：成果の「生成規模」が変わった

## 722本 ／ 372ファミリー

10/6、OpenAIが内部研究モデルによる数学原稿を初回公開。

**部分的にLeanによる形式化も公開。**
一方、翌10/7には3本を撤回し、14本を改訂。

> 新しいボトルネックは、生成された成果を検証・理解・再利用すること。

<!--
722は初回公開時の原稿数であり、722件の独立した大問題がすべて確定した、という意味ではありません。数論、幾何、解析など幅広い領域に及びます。
使用されたのは未公開の内部研究モデルで、社内で使えるSolと同一だとは確認されていません。
原稿や形式化は追加・改訂されるため、現在のリポジトリの件数と初回件数は異なります。S06は初回公開を対象とする独立研究レビューであり、それ自体が全証明の検証を意味するものではありません。
S05：https://openai.com/index/sharing-ai-progress-in-mathematics/
S06：https://arxiv.org/abs/2610.17090
S07：https://github.com/openai/math/blob/main/history.md
-->

---

<!-- _header: 02 / SCIENCE -->
<!-- _class: compact -->
<!-- _footer: '出典：[S09 OpenAI・10/26発表](https://openai.com/index/building-scientific-understanding-with-academic-communities/) ／ [S07 公開原稿の履歴](https://github.com/openai/math/blob/main/history.md)' -->

# 10/26：研究の前提に踏み込む成果を発表

| 分野 | OpenAIが発表した成果 | 意味 |
|---|---|---|
| 計算量理論 | **ETH：指数時間仮説の反証** | 多くの条件付き計算困難性の、前提を再考 |
| 調和解析 | **全次元の局所平滑化予想の証明** | Kakeya・制限予想にも及ぶ大きな進展 |
| 数理物理 | **QCD等の存在証明に関する成果** | 専門家グループが理解・検証を進める |

争点は「AIにできるか」から、**どう確かめ、理解し、次へつなぐか**へ。

研究者の仕事が無意味になるのではなく、研究の進め方が変わる。

<!--
ここでの分類は、2026-10-26のOpenAI発表を紹介したものです。自然言語原稿、形式化、専門家の独立検証を区別します。
ETHの反証はP=NPの証明ではありません。「ETHが成立すればX」という既存の条件命題も、それだけで論理的に誤りになるわけではありません。
調和解析の重要な予想群への成果であり、調和解析全体が終わったとはいえません。制限予想の正確な範囲は原稿を参照してください。
QCD等の存在証明と、Yang–Millsの存在・質量ギャップという千年紀問題全体の解決・公認は同じではありません。
この発表では外部専門家との協働・検証体制が強調されています。数学界を単純な賛成派・反対派に分けず、新手法への期待と検証負担の双方を伝えます。
-->

---

<!-- _header: 03 / INDIVIDUAL × AI -->
<!-- _footer: '出典：[S08 開発者本人の技術報告・10/18](https://pepsipu.com/blog/2026-10-switch2-jailbreak-ns2jb/) ｜ 作者による実機検証の報告' -->

# Switch 2：個人研究者 × Codex × 実機

**個人研究者が、非公式コードを実行する jailbreak を公開。**

- Codexが脆弱性を発見し、利用に向けた調査・実装にも参加。
- 人間が研究方針を選び、実機を使って試行を重ねた。
- 作者は「一言で全自動」説を否定。実作業は**約2週間**。

> 個人がAIを研究の戦力にして、大手製品の防御境界を越えた。

<!--
今回の主題を最も直接的に示す事例です。人間が対象を選び、複数のCodex作業を進め、実機に入力・観測・再起動できる環境も用意しています。
報告の対象は当時の特定ファームウェアで、全バージョンや全防御の突破ではありません。AIと人間のどちらか一方だけの成果として紹介しないようにします。
著者は約2週間の実質的作業が必要だったと追記しています。使用モデルの正確な版や総利用費が確認できないため、「Solが数ドルで破った」といった換算はしません。
出典：https://pepsipu.com/blog/2026-10-switch2-jailbreak-ns2jb/
-->

---

<!-- _header: 03 / INDIVIDUAL × AI -->
<!-- _footer: '出典：[S10 Scott Helmeによる再現報告・10/20](https://scotthelme.co.uk/eight-bits-of-trust-emudhras-ca-keys-cracked-in-milliseconds/)' -->

# eMudhra：信頼の根元を、手元のAIで検証

**8つの中間CA鍵に、極端に弱い秘密値。**

P-384用の秘密値が、`4` や `56` など**1 byteに収まる値**だった。

研究者は公開証明書から復元し、
**Claudeへの単一の指示でも再現できた**と報告。

> 強い暗号でも、鍵生成・運用のミスは守ってくれない。

<!--
1 bitではなく1 byteです。また、楕円曲線暗号そのものを一般的に破った事例ではありません。秘密値の生成・選択の不備が問題です。
単一プロンプトで再現したのは、すでに問題が判明した弱鍵の復元であり、最初の発見までAIが単独で行ったと確認されたわけではありません。
個人の手元で専門的な調査結果を検証しやすくなった例として位置づけます。証明書の利用者側にも、信頼ストア更新という運用課題が残ります。
出典：https://scotthelme.co.uk/eight-bits-of-trust-emudhras-ca-keys-cracked-in-milliseconds/
-->

---

<!-- _header: 03 / COMMUNITY RESEARCH -->
<!-- _footer: '出典：[S11 gpu-unlock](https://github.com/Zagitta/gpu-unlock) ／ [S12 Ada版の計測記録](https://github.com/JustAResearcher/gpu-unlock-ada) ｜ コミュニティ報告' -->

# GPU：メーカー側の性能制限にも到達

**RTX 20／30／40系の特定Tensor演算の制限を、コミュニティが回避。**

| RTX 4090の公開測定例 | 結果 |
|---|---|
| 特定のFP16／BF16命令スループット | **約2倍** |
| 同じ450 W上限での実GEMM・FP16 | **約12〜34%向上**（測定した形状） |

電力・メモリ帯域の制約は残る。すべての処理が2倍になるわけではない。

> 製品内部の制限も、個人・コミュニティの研究対象になっている。

<!--
これはメーカーの性能制限を回避する研究で、インターネット経由のサーバー侵入とは別の種類の話です。ハードウェア自体が変わるわけでもありません。
S12には同一450 W上限での比較が記載されています。命令レベルの約2倍と、実アプリケーションの向上率は分けます。
この資料で確認した記録だけでは、突破に対するAIの寄与を定量化できません。「AIが単独でNVIDIAを破った」証拠とはせず、個人・コミュニティが到達している技術領域の広さとして紹介します。
-->

---

<!-- _header: 03 / COMMUNITY RESEARCH -->
<!-- _class: compact -->
<!-- _footer: '出典：[S13 Sony A7 IV研究](https://github.com/leogenot/sony-a7iv-feature-research) ／ [S14 AnyPS5](https://github.com/boykopovar/AnyPS5)' -->

# カメラ・ゲーム機：閉じた製品の内部へ

| 対象 | 確認できる進展 | 「何ができたか」 |
|---|---|---|
| **Sony A7 IV** | 実行中のカメラから復号済みファイルを取得。機能設定を調査 | ファームウェア解析・一部表示の変更 |
| **AnyPS5** | 実行ファイルの変換、システムAPIの再実装、シェーダー変換 | PS5ソフトのPC向け互換性研究 |

**防御の突破・機能制限の回避・互換性の実装は、それぞれ別。**

AIの寄与が確認できた事例と、技術的進展だけを確認した事例も分ける。

<!--
Sonyの事例はA7 IVの特定バージョンにおける研究です。暗号方式全般の破綻や、全カメラ機種の自由な書き換えではありません。シャッター角表示は確認されても、すべての調整機能が使える状態とは限りません。
AnyPS5は互換性を実装するプロジェクトです。PS5本体のセキュリティ突破と同じニュースにまとめないでください。APIの実装率も、そのままゲームの動作率にはなりません。
この2件は、AIの効果を直接実証する主例ではなく、閉じた製品に対するコミュニティの活動範囲を示す補助例です。
-->

---

<!-- _header: 04 / SECURITY RESEARCH -->
<!-- _footer: '出典：[S15 Anthropic Frontier Red Team・10/27](https://www.anthropic.com/research/discovering-vulnerabilities-with-claude) ｜ 未公開の内部研究モデル' -->

# さらに先では、複数の防御をつなげて突破

Anthropicは、**5種類の実ソフトウェアへの攻撃チェーン**を報告。

| 対象 | 報告された影響 |
|---|---|
| Chrome／Safari | サンドボックス外でのコード実行／同一オリジン制約の回避 |
| Android | 特定のUSB接続条件で、ロック中のデータにアクセス |
| Windows／Linux | 遠隔サービス妨害／特定構成での遠隔コード実行 |

単発のバグ発見だけでなく、**複数の弱点を組み合わせる能力**へ。

<!--
ここは、個人が利用した市販AIの話から、研究段階の能力の上限へ視点を移すスライドです。Anthropic自身の報告で、未公開内部モデルによる成果です。
公開モデルを使えば誰でも同じ結果を再現できる、とまではいえません。Windowsはサービス妨害、Linuxは特定構成でのコード実行で、影響の種類も異なります。
報告はベンダーへの協調的な開示プロセスに基づきます。発見数の紹介よりも、探索・検証・利用チェーン構築までがつながる点を強調します。
-->

---

<!-- _header: 04 / SECURITY INCIDENTS -->
<!-- _footer: '出典：[S16 PHP Foundation・10/21](https://thephp.foundation/blog/2026/10/21/todays-php-security-release-and-how-were-strengthening-php-security/)' -->

# PHP2Shell：基盤の欠陥が、業務を止める

**認証なしの遠隔コード実行につながる、PHP本体の2件の重大脆弱性。**

`CVE-2026-109618` ／ `CVE-2026-109619`

- メモリ不足やエラー処理に関わる、基盤部分の不備。
- 条件が合えば、PHPプロセスの権限でコードが実行される。
- OpenAIも独立に発見。人の監査・他社の研究も修正に貢献。

> 自分たちの業務コードを変更していなくても、緊急対応は起きる。

<!--
PHPはサーバー側の実行環境です。「すべてのPHPサイトが直ちにroot権限を渡す」という説明はしません。実行方式やアプリケーション、権限境界で影響が変わります。
PHP Foundationによると、問題の兆候は2024年の監査後の作業でも見つかっており、2026年にはCalifが実際の悪用につながる経路を報告し、OpenAIも独立に根本原因を発見しました。
10/21に修正版8.2.35、8.3.36、8.4.27、8.5.12が公開されました。これはこの事案の修正版の記録であり、今後も常に最新という意味ではありません。
-->

---

<!-- _header: 04 / BUSINESS IMPACT -->
<!-- _class: compact -->
<!-- _footer: '出典：[S17 コドモン技術ブログ・10/23](https://tech.codmon.com/entry/2026/10/23/173909) ／ [S18 コニカミノルタ・10/26](https://www.konicaminolta.jp/instruments/topics_important/20261026/)' -->

# 被害がなくても、停止コストは発生する

| 実例 | 起きたこと |
|---|---|
| **コドモン** | 10/21に予防的な日中停止。修正版を待ち、検証後に再開 |
| **コニカミノルタの対象Webサイト** | 予防的に公開停止。対応を終え10/23に再開 |

両社とも、公表時点で本件による**不正アクセス・情報漏えいは未確認**。

コドモンでは、**攻撃の手がかりが先に広まり、修正版がまだない時間帯**が問題に。

> 「侵入されてから対応する」では、事業継続を守れない。

<!--
停止の事実と、攻撃を受けた事実は別です。この2件は、情報保護を優先した予防的停止として公表されています。
コドモンの振り返りは、修正版が出る前から情報が広まり、その間の運用判断が難しかったことを具体的に記録しています。
私たちへの示唆は、パッチ適用の技術だけでなく、誰が停止・再開を判断するか、顧客への連絡、検証方法、代替手段を平時に決めておくことです。
-->

---

<!-- _header: 04 / OUR TECHNOLOGY STACK -->
<!-- _class: compact -->
<!-- _footer: '出典：[S19 Node.js・10/21](https://nodejs.org/en/blog/vulnerability/october-2026-security-releases) ／ [S20 Apache Tomcat](https://tomcat.apache.org/security-11.html)' -->

# Node.js・Tomcatも、依存先のリスク

| 対象 | 今回の主な問題 | 対応版の例 |
|---|---|---|
| **Node.js** | Brotli解凍時のメモリ破壊。条件次第でRCE。Codex Securityが報告 | 22.23.4／24.22.1／26.12.1 |
| **Tomcat** | 特定JNDI認証の回避、HTTP/2・AJPの応答混同等 | 11系は11.0.27 |

Node.jsの公式区分は **High**、上記Tomcat項目は **Important**。

**重大度だけでなく、対象バージョン・機能・入力経路を確認する。**

<!--
Node.jsの10/21公開情報では、BrotliのCVE-2026-111497についてOpenAI Codex Securityが報告者として記載され、修正者は別に記載されています。「AIがその日のうちに単独で修正・テスト・リリースした」とは断定できません。
Tomcatの対象項目は10/20に公開されています。11.0.27自体のリリース日は10/12です。公表日と修正版の公開日は区別します。
他系列は各系列の公式情報を確認します。表は当該問題の修正版の例であり、2026-10-30時点の全製品の最新パッチ一覧ではありません。
Java案件でもビルドツールや管理UIがNode.jsに依存している場合があります。実際の構成確認が必要です。
-->

---

<!-- _header: 05 / BEYOND SECURITY -->
<!-- _footer: '出典：[S21 Alliance Artsの告知](https://store.steampowered.com/news/app/4150720/view/746066581090468248) ／ [S22 PC Gamer・10/19報道](https://www.pcgamer.com/gaming-industry/steam-week-in-review-steam-next-fest-has-over-8-000-demos-as-worthless-vibe-coded-slop-levels-up/)' -->

# 作る速さは、模倣する速さにもなる

**ゲーム開発でも、公開方法への影響が表面化。**

- 『Escape the Walls』：映像公開後、複数の類似作品が登場したと報道。
- 『Drunken Goddess Reflux』：AI等による迅速な模倣を懸念し、公開デモの方針を変更。

## 見方：実装の難しさだけに依存した優位性は、薄くなる

品質、継続改善、独自データ、ユーザーとの関係がより重要に。

<!--
このページは技術的な脆弱性ではなく、制作と競争の話です。作品が似ていること、AIで作られたこと、法的な侵害に該当すること、経済損失が生じたことは同じではありません。
PC Gamerの報道で、類似作品の出現と、Alliance Artsの公開方針変更を確認しています。損失額や、すべての類似作品でのAI使用は確定していません。
下段は発表者の解釈です。「実装できること」だけでなく、運用・改善・顧客理解まで含めた価値を考える必要があります。
-->

---

<!-- _header: 06 / WHAT CHANGED — 考察 -->
<!-- _class: takeaway -->
<!-- _footer: '考察の根拠：前掲のモデル価格、Switch 2、eMudhra、PHP2Shellの事例' -->

# 変わるのは、技術だけでなく
# 「攻める側の採算」

以前から存在した弱点にも、
**調査・解析・実装・試行のコストが下がることで手が届く。**

> 「大手製」「閉じている」「長年動いている」は、
> それだけでは安全の根拠にならない。

<!--
これは事例を踏まえた見立てです。2026年以前の技術がすべて脆弱になった、という意味ではありません。
個人や小規模チームにも、以前は割に合わなかった分析に取り組める余地が広がっています。一方で、攻撃対象の知識、実機や環境、検証能力、人の判断も必要です。
今後はモデル性能と予算だけでなく、分析を実行できる環境と、その結果を確かめる仕組みが競争力になります。
-->

---

<!-- _header: 06 / LEGACY SYSTEMS — 見通し -->
<!-- _footer: '背景事例：[S16 PHP Foundation](https://thephp.foundation/blog/2026/10/21/todays-php-security-release-and-how-were-strengthening-php-security/) ／ [S17 コドモン](https://tech.codmon.com/entry/2026/10/23/173909)' -->

# 「動いているので放置」のコストが上がる

更新されない動的サイトには、**情報を残す価値**と**実行基盤のリスク**がある。

| 選択肢 | 残すもの・減らすもの |
|---|---|
| **更新して継続** | 機能を残し、保守可能な構成へ |
| **隔離・機能制限** | 必要な機能を残し、攻撃経路を減らす |
| **静的化・アーカイブ** | 内容を残し、不要なサーバー側実行をなくす |

「古いサイトがすべて消える」は未確定。
**維持できない動的サービスが、継続判断を迫られる**可能性はある。

<!--
このページは今後の見通しであり、歴史的サイトが一斉に消滅したという統計的事実を示しているわけではありません。
実行環境の保守と、公開コンテンツの保存は分けて考えられます。静的化によって残せる内容もあります。
私たちのシステムでも、使われていない管理画面や古い機能を動かし続ける必要があるか、保守の責任者と予算があるかを考える契機になります。
-->

---

<!-- _header: 07 / OUR TEAM — 提案 -->
<!-- _class: compact -->
<!-- _footer: 'チーム向け確認観点。具体的な採用製品・依存関係・接続経路は実構成で確認する。' -->

# 外部公開していなくても、境界はある

**外部接続が少ないことと、外部由来の入力がないことは違う。**

| 確認する層 | 私たちの開発・保守で見るもの |
|---|---|
| 実行環境 | JDK、APサーバー、フレームワーク、直接・間接依存 |
| 基盤 | OS、コンテナイメージ、証明書ストア |
| 開発経路 | リポジトリ、依存配布元、CI Runner、開発端末 |
| 連携経路 | 受信ファイル、バッチ入力、他システムAPI、管理アクセス |

> 自システムだけでなく、接続先を含む全体の弱点にならない。

<!--
これは実際に脆弱性があると断定するページではなく、影響確認の範囲を提案するものです。
インターネットに直接公開していないことはリスクを下げます。ただし、ファイル連携、依存パッケージ、管理アクセスなどの信頼境界は残ります。
Javaの業務コードだけを見るのではなく、ビルドから本番までの経路を確認します。社内・顧客の既存資産管理やセキュリティ窓口を利用し、重複した管理台帳を増やすことは目的にしません。
-->

---

<!-- _header: 07 / OUR TEAM — 提案 -->
<!-- _footer: '提案：既存の脆弱性管理・変更管理に組み込む。根拠事例：[S17 コドモン](https://tech.codmon.com/entry/2026/10/23/173909)' -->

# 目標は「すぐ更新できる」状態を平時につくる

| 能力 | 平時に準備すること |
|---|---|
| **把握する** | 使用バージョン・間接依存・担当者が分かる |
| **判断する** | 影響条件、露出、悪用状況、暫定対策を確認できる |
| **直す・戻す** | 更新を試せる環境、回帰テスト、切戻し手順がある |
| **決めて伝える** | 緊急変更の承認者、顧客連絡、停止・再開条件が明確 |

**測るもの：影響判定までの時間／対策完了までの時間。**

<!--
すべての脆弱性に一律で即時停止・即時更新を求めるのではなく、現実の影響に応じて優先順位をつけます。
パッチの差分が攻撃側の手がかりにもなることを踏まえ、公表後に準備を始めるのでは遅れる場合があります。更新だけでなく、隔離や機能停止を暫定策にできるようにします。
承認を省くのではなく、必要な判断が速くできるよう、緊急時の連絡先と手順を平時に整理します。既存のJiraや変更管理で担当・期限・証跡を扱う想定です。
-->

---

<!-- _header: 07 / OUR TEAM — 提案 -->
<!-- _footer: '社内のGPT-6.1 Sol利用可否：発表者提供情報。以下は活用案であり、実測済みの効果ではない。' -->

# 私たちも、GPT-6.1 Solを防御側に使う

| 作業 | AIに任せる下準備 | 人が判断すること |
|---|---|---|
| **影響調査** | 公告・変更点の整理、対象依存の候補抽出 | 実構成との一致、利用条件 |
| **更新と検証** | 修正案、回帰テスト案、失敗ログの分析 | 挙動の妥当性、合格・切戻し判断 |
| **変更管理** | 変更要約、確認項目、報告文の下書き | 承認、顧客説明、リリース判断 |

**まず1件、既存の保守タスクで、時間と品質を比較する。**

対象データ・外部接続・実行権限は、承認済み環境の範囲で扱う。

<!--
AI利用の目標を「使った回数」にしないことが大切です。既存の依存更新や小さな保守タスクを選び、調査時間、レビュー修正量、テスト結果で効果を見ます。
社内環境にSolがあることは、顧客コードを任意の外部サービスへ送ってよいことや、本番へ自動変更してよいことを意味しません。既存の利用範囲と権限で実施します。
AIには根拠の提示やテストの作成を任せ、人は採否を判断する。防御側も同じ技術で対応能力を上げることが、この共有の実務的な着地点です。
-->

---

<!-- _header: TAKEAWAYS -->
<!-- _class: takeaway -->
<!-- _footer: '2026-10-30 ｜ 以下は参照資料' -->

# 攻撃者だけが速くなる世界にしない

**能力向上 × コスト低下**が、個人・小規模チームの到達範囲を広げる。

大手製品も、長年動いた基盤も、改めて検証される。

私たちに必要なのは、**把握し、判断し、更新し、戻せる能力**。

> AIを「便利な相談相手」から、
> 検証可能な開発・保守の戦力へ。

<!--
最後に伝えたいのは、危機感だけではありません。個人や小規模チームの能力が拡張されるなら、私たちのチームもその側に立てます。
モデルの進歩を追うことと、日々の開発・保守のやり方を改善することをつなげたい、という結論です。
次の一歩として、依存関係の影響確認か既存の更新タスクを1件選び、社内のAIを使う場合と従来の進め方を比較する提案で締めます。
-->

---

<!-- _header: APPENDIX / SOURCES 1 -->
<!-- _class: references -->
<!-- _footer: '確認日：2026-10-30。価格・モデル・公開原稿は更新されるため、利用時は原典を再確認。' -->

# 参照資料：モデル・科学研究

| ID | 資料 |
|---|---|
| S01 | Anthropic — [Introducing Claude Sonnet 5.5](https://www.anthropic.com/claude-sonnet-5-5)（9/28） |
| S02 | Anthropic — [Introducing Claude Haiku 5.5](https://www.anthropic.com/claude-haiku-5-5)（10/7） |
| S03 | OpenAI — [Introducing GPT-6.1 Terra](https://openai.com/index/introducing-gpt-6-1-terra/)（10/26） |
| S04 | Anthropic — [Pricing / Long context pricing](https://platform.claude.com/docs/en/about-claude/pricing) |
| S05 | OpenAI — [Sharing AI progress in mathematics](https://openai.com/index/sharing-ai-progress-in-mathematics/)（10/6） |
| S06 | Ying Xie — [What the Machine Invented](https://arxiv.org/abs/2610.17090)（初回公開を扱う研究レビュー） |
| S07 | OpenAI — [math / history.md](https://github.com/openai/math/blob/main/history.md)（撤回・改訂・追加履歴） |
| S09 | OpenAI — [Working with academic communities](https://openai.com/index/building-scientific-understanding-with-academic-communities/)（10/26） |

<!--
通常の発表ではここから先は読み上げず、質疑や配布後の参照に使います。
S06は独立著者の研究原稿です。他は提供元の公式発表・公式公開資料です。ベンチマークの数値は提供元の条件に依存します。
Terraの10/26公開の公式補助資料：https://community.openai.com/t/gpt-6-1-terra-delivering-fast-and-capable-computer-use-at-a-lower-price/1409900
-->

---

<!-- _header: APPENDIX / SOURCES 2 -->
<!-- _class: references -->
<!-- _footer: '研究者・作者自身の記録を優先。個別環境の実証と、一般化された性能・安全性は区別する。' -->

# 参照資料：個人・コミュニティの事例

| ID | 資料 |
|---|---|
| S08 | 開発者本人 — [jailbreaking the switch 2](https://pepsipu.com/blog/2026-10-switch2-jailbreak-ns2jb/)（10/18、追記あり） |
| S10 | Scott Helme — [Eight Bits of Trust](https://scotthelme.co.uk/eight-bits-of-trust-emudhras-ca-keys-cracked-in-milliseconds/)（10/20） |
| S11 | GitHub — [Zagitta/gpu-unlock](https://github.com/Zagitta/gpu-unlock) |
| S12 | GitHub — [JustAResearcher/gpu-unlock-ada](https://github.com/JustAResearcher/gpu-unlock-ada) |
| S13 | GitHub — [Sony A7 IV firmware and feature research](https://github.com/leogenot/sony-a7iv-feature-research) |
| S14 | GitHub — [boykopovar/AnyPS5](https://github.com/boykopovar/AnyPS5) |
| S21 | Alliance Arts — [Change to the Demo Release Plan](https://store.steampowered.com/news/app/4150720/view/746066581090468248) |
| S22 | PC Gamer — [Steam Week in Review](https://www.pcgamer.com/gaming-industry/steam-week-in-review-steam-next-fest-has-over-8-000-demos-as-worthless-vibe-coded-slop-levels-up/)（10/19、ゲーム事例の報道） |

<!--
S08とS10ではAIの関与を作者が明示しています。S11〜S14は、この資料で確認した情報だけではAIの寄与を断定しません。
S21の告知内容はS22の掲載引用・報道でも確認しています。類似作品の存在や方針変更と、法的な侵害判断・損失の確定を区別します。
-->

---

<!-- _header: APPENDIX / SOURCES 3 -->
<!-- _class: references -->
<!-- _footer: 'CVE・深刻度・影響条件・対応版は各プロジェクトの最新公告を参照。' -->

# 参照資料：セキュリティ・事業影響

| ID | 資料 |
|---|---|
| S15 | Anthropic — [Discovering and exploiting vulnerabilities with Claude](https://www.anthropic.com/research/discovering-vulnerabilities-with-claude)（10/27） |
| S16 | PHP Foundation — [Today's PHP Security Release](https://thephp.foundation/blog/2026/10/21/todays-php-security-release-and-how-were-strengthening-php-security/)（10/21） |
| S17 | コドモン Product Team Blog — [PHP2Shellへの対応を振り返って](https://tech.codmon.com/entry/2026/10/23/173909)（10/23） |
| S18 | コニカミノルタ — [Webサイトの公開再開について](https://www.konicaminolta.jp/instruments/topics_important/20261026/)（10/26） |
| S19 | Node.js — [October 21, 2026 Security Releases](https://nodejs.org/en/blog/vulnerability/october-2026-security-releases) |
| S20 | Apache — [Tomcat 11 vulnerabilities](https://tomcat.apache.org/security-11.html)（10/20公表の項目） |

本編の「考察」「見通し」「提案」は、これらの事実からの整理であり、
各発表元の見解や、チームで決定済みの方針を意味するものではない。

<!--
この資料の目的は、最近の技術変化と実務への影響を共有することです。実装の利用手順や攻撃手順は含めていません。
発表後に実案件の対応へ進む際は、現時点の構成・公告・責任範囲を確認して、既存のセキュリティ管理・変更管理の中で扱います。
-->
