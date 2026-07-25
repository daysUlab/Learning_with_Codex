# logic_tower 執筆進捗（PROGRESS）

## 運用ルール（このリポジトリ専用）
- ユーザーが **「次をお願いします」** とだけ指示した場合も、このファイルを最初に確認する。
- 優先順位は次の通り。既存執筆キューとv1.0アップグレードキューに未完了がなければ、v1.1拡張キューへ進む。
  1. `status=DOING` の行があれば、そのファイルを最優先で仕上げて `DONE` にする。
  2. `DOING` が無ければ、キュー先頭から最初の `TODO` を1件だけ選んで執筆する。
  3. 1回の実行で本文執筆は **必ず1ファイルのみ**。
- 執筆完了後は、この表の対象行を `DONE` に更新し、`last_updated` と `notes` を記録する。
- 次の `TODO` は同一実行内で `DOING` にしない（次回実行時に選ばれるよう `TODO` のまま残す）。
- 対象範囲は `logic_tower/` 配下のみ。
- 新しい章（新フォルダ）に入るタイミングでは、導線設計を先に行い、**子mdを3ファイル以上スケルトン作成**してから本文執筆に入る。
- 入口ページは `00_overview.md` 優先、なければ `README.md` を使う。
- 本文化時は初心者向けを最優先とし、定義だけで終わらず「直観・例・つまずきポイント・確認問題」の4要素を可能な限り含める。
- 図解はASCIIではなく `mermaid` を使用し、本文化ページには原則として **1記事1図以上** を含める。
- `DONE` 更新前に「Mermaid図があるか」「図の読み取りポイント説明があるか」を確認する。
- 論理記号（否定・連言・選言・含意・量化記号）は、本文で扱う際に可能な限りTeX記法（`$\lnot$`, `$\land$`, `$\lor$`, `$\to$`, `$\forall$`, `$\exists$`）を併記する。

## キュー定義
- 順序規則: `logic_tower/README.md` → `00_orientation` → `01` 以降を番号順 → `90_essays`。
- 各フォルダ内はファイル名辞書順。

## 執筆キュー

| file_path | status | last_updated | notes |
|---|---|---|---|
| `logic_tower/README.md` | DONE | 2026-02-16 | 入口ページを初学者向けに大幅増補。到達目標・ロードマップ・用語最小セット・典型例・つまずきポイント・自己確認を追加。 |
| `logic_tower/00_orientation/README.md` | DONE | 2026-02-16 | 導入章READMEを本文化。学習目標・3つの問い・直観例・つまずき対策・自己確認を追加。 |
| `logic_tower/00_orientation/00_what_is_logic.md` | UPGRADE_DONE | 2026-07-25 | 形式化と決定可能性を区別し、前提の真偽と推論の妥当性を分離。人間向けタイトル、到達目標、Mermaid図と読み取り、具体例2件、誤解・復帰手順、演習6問と全解答、学習チェック、前・次・親リンクを追加。 |
| `logic_tower/00_orientation/01_language_and_meaning.md` | UPGRADE_DONE | 2026-07-25 | 構文・意味・解釈の区別を構文木と複数割当で補強。自然言語の形式化で失う情報も明示し、Mermaid図、段階例2件、誤解・復帰手順、演習6問と全解答、学習チェック、前・次・親リンクを追加。 |
| `logic_tower/00_orientation/02_proof_and_model.md` | UPGRADE_DONE | 2026-07-25 | 証明可能性と意味論的帰結を分離し、反例モデルを使う段階例を追加。完全性を言語・意味論・証明体系の組に相対化し、Mermaid図、演習6問と全解答、復帰手順、学習チェック、前・次・親リンクを整備。 GitHub上のブロック数式表示を安定させるため、追加式の区切りを `$` に修正。 |
| `logic_tower/01_propositional_logic/00_overview.md` | UPGRADE_DONE | 2026-07-25 | 章入口を、構文・真理値表・標準形・自然演繹の役割が見える構成へ統一。Mermaid学習図、段階例2件、典型的誤解と復帰手順、演習6問と全解答、学習チェック、前・次・親リンクを追加。 GitHub上のブロック数式表示を安定させるため、追加式の区切りを `$` に修正。 |
| `logic_tower/01_propositional_logic/01_syntax_semantics.md` | UPGRADE_DONE | 2026-07-25 | 構文規則と意味評価の往復を補強し、主結合子・構文木・妥当性の区別を演習化。既存Mermaid図と例を保持し、演習6問と全解答、誤解・復帰手順、学習チェック、前・次・親リンクを整備。 |
| `logic_tower/01_propositional_logic/02_truth_tables.md` | UPGRADE_DONE | 2026-07-25 | 真理値表の作表・式分類・反例探索を6問の段階演習へ拡張。既存の2例とMermaid手順図を保持し、全解答、典型誤答と復帰手順、学習チェック、前・次・親リンクを整備。 |
| `logic_tower/01_propositional_logic/03_normal_forms.md` | UPGRADE_DONE | 2026-07-25 | CNF・DNFの変換例と同値法則を保持し、否定押し下げ・分配・簡単化・検算を段階演習化。Mermaid図、誤変形からの復帰手順、演習6問と全解答、学習チェック、前・次・親リンクを整備。 |
| `logic_tower/01_propositional_logic/04_natural_deduction.md` | UPGRADE_DONE | 2026-07-25 | 導入・除去規則と既存3例を保持し、仮定スコープ・選言除去・後件肯定を段階演習で補強。Mermaid図、演習6問と全解答、誤解・復帰手順、学習チェック、前・次・親リンクを整備。 |
| `logic_tower/02_predicate_logic/00_overview.md` | UPGRADE_DONE | 2026-07-25 | 命題論理から述語論理への拡張を、対象・述語・量化・構造の順で再構成。既存Mermaid図と対象付き推論を保持し、量化順序の段階例、誤解・復帰手順、演習6問と全解答、学習チェック、前・次・親リンクを整備。 |
| `logic_tower/02_predicate_logic/01_quantifiers.md` | UPGRADE_DONE | 2026-07-25 | 量化記号のスコープを括弧明記方針へ統一し、省略規則が教材・体系で異なることを明示。既存例とMermaid図を保持し、量化順序・自由変数・否定変形を含む演習6問と全解答、復帰手順、学習チェック、前・次・親リンクを整備。 |
| `logic_tower/02_predicate_logic/02_structures_and_models.md` | DONE | 2026-02-16 | 構造とモデルを本文化。Mermaid意味評価フロー図、TeX記法、充足/妥当性の区別、演習を追加。 |
| `logic_tower/02_predicate_logic/03_proofs.md` | DONE | 2026-02-16 | 述語論理の証明規則を本文化。Mermaid証明フロー図、TeX記法、量化導入/除去規則と変数条件を追加。 |
| `logic_tower/03_soundness_completeness/00_overview.md` | DONE | 2026-02-16 | 健全性・完全性章の入口を本文化。Mermaid概念図とTeX記法で⊢/⊨/コンパクト性の関係を整理。 |
| `logic_tower/03_soundness_completeness/01_soundness.md` | DONE | 2026-02-16 | 健全性を本文化。Mermaid概念図、TeX定義、局所健全性の例、完全性との差分と演習を追加。 |
| `logic_tower/03_soundness_completeness/02_completeness.md` | DONE | 2026-02-16 | 完全性を本文化。Mermaid方向図、TeX定義、健全性との対比、反例モデル構成の発想、演習を追加。 |
| `logic_tower/03_soundness_completeness/03_compactness_low_level.md` | DONE | 2026-03-25 | コンパクト性を初学者向けに本文化。Mermaid概念図、完全性との接続、イメージ重視の演習4問＋解答を追加。 |
| `logic_tower/04_computability_and_automata/00_overview.md` | DONE | 2026-03-26 | 計算可能性章の入口を本文化。Mermaid全体マップ、モデル比較、決定可能性の基礎、演習4問＋解答を追加。 |
| `logic_tower/04_computability_and_automata/01_finite_automata.md` | DONE | 2026-07-25 | 有限オートマトン入門を本文化。Mermaid状態遷移図、DFAの5つ組・受理判定・設計手順、NFA/正規表現との関係、演習6問＋解答を追加。 |
| `logic_tower/04_computability_and_automata/02_pushdown_automata.md` | DONE | 2026-07-25 | PDA入門を本文化。Mermaid処理フロー図、スタック操作・7つ組・括弧列とa^n b^nの追跡、CFGとの関係・限界、演習6問＋解答を追加。 |
| `logic_tower/04_computability_and_automata/03_turing_machines.md` | DONE | 2026-07-25 | チューリング機械を本文化。Mermaid処理図、7つ組・瞬間記述・a^n b^n c^nの判定、認識と決定、チャーチ＝チューリングのテーゼ、演習6問＋解答を追加。 |
| `logic_tower/04_computability_and_automata/04_decidability.md` | DONE | 2026-07-25 | 決定可能性を本文化。Mermaid包含図、決定可能/認識可能の区別、停止問題・対角線論法・写像還元・ライスの定理、演習6問＋解答を追加。 |
| `logic_tower/05_modal_and_nonclassical/00_overview.md` | DONE | 2026-07-25 | 様相・非古典論理章の入口を本文化。Mermaid学習マップ、必然/可能・クリプキ意味論・直観主義論理の導入、体系比較、演習5問＋解答を追加。 |
| `logic_tower/05_modal_and_nonclassical/01_modal_logic_kripke.md` | DONE | 2026-07-25 | 様相論理とクリプキ意味論を本文化。Mermaidモデル図、フレーム/モデル・満足関係・空虚真・公理K・フレーム条件、演習6問＋解答を追加。 |
| `logic_tower/05_modal_and_nonclassical/02_intuitionistic_logic.md` | DONE | 2026-07-25 | 直観主義論理を本文化。Mermaid証拠図、BHK解釈・否定・排中律・二重否定・カリー＝ハワード対応・情報増加モデル、演習6問＋解答を追加。 |
| `logic_tower/05_modal_and_nonclassical/03_other_logics_map.md` | DONE | 2026-07-25 | 非古典論理の地図を本文化。Mermaid分類図、時相・認識・義務・多値・ファジィ・矛盾許容・関連性論理の比較、演習6問＋解答を追加。 |
| `logic_tower/90_essays/README.md` | DONE | 2026-07-25 | 応用エッセイ章の入口を本文化。Mermaid接続図、本編からDB・モデル検査・証明支援系への往復導線、共通の形式化手順、演習4問＋解答を追加。 |
| `logic_tower/90_essays/logic_and_database_queries.md` | DONE | 2026-07-25 | 論理とDB問い合わせを本文化。Mermaid翻訳フロー、述語・EXISTS・全称の二重NOT EXISTS・空虚真・NULLの3値論理・JOINと重複、演習6問＋解答を追加。 |
| `logic_tower/90_essays/modal_logic_and_computation.md` | DONE | 2026-07-25 | 様相論理と計算を本文化。Mermaid状態遷移図、安全性/活性、LTL演算子、CTLの経路量化、モデル検査・状態爆発・公平性、演習6問＋解答を追加。 |
| `logic_tower/90_essays/proof_assistants_and_logic.md` | DONE | 2026-07-25 | 証明支援系と論理を本文化。Mermaid検査フロー、Curry–Howard対応、ゴール/コンテキスト、自然演繹との対応、帰納法・古典公理・信頼境界、演習6問＋解答を追加。 |
| `logic_tower/PROGRESS.md` | DONE | 2026-02-16 | physics_tower の運用を踏襲して進捗管理基盤を新規作成。 |

## v1.0アップグレードキュー

### 運用ルール

- 既存の執筆キューの `DONE` は「一度本文を作成済み」を表し、この表はv1.0品質への更新状況を表す。
- 優先順位は `UPGRADING`、次に表の先頭の `UPGRADE_TODO` とする。
- 1回の作業で更新する本文は1ファイルだけとし、同じ作業内で次の本文へ着手しない。
- 本文の正しい説明と既存の文体を残し、直観・定義・例・誤解・復帰方法・演習・全解答・学習チェック・ナビゲーションを補う。
- 完了時は `UPGRADE_DONE` に変更し、`last_updated` と判断理由を含む `notes` を残す。

| file_path | status | last_updated | notes |
|---|---|---|---|
| `logic_tower/00_orientation/README.md` | UPGRADE_DONE | 2026-07-25 | 既存の3つの問いと章導線を保持し、形式化と決定可能性を区別する表現へ修正。人間向けタイトル、用語と記号、Mermaid図と読み取り、段階例2件、典型的誤解、復帰手順、演習6問と全解答、学習チェック、前・次・親リンクを追加し、後半ページ相当の学習順へ統一。 |
| `logic_tower/00_orientation/00_what_is_logic.md` | UPGRADE_DONE | 2026-07-25 | 形式化と決定可能性を区別し、前提の真偽と推論の妥当性を分離。人間向けタイトル、到達目標、Mermaid図と読み取り、具体例2件、誤解・復帰手順、演習6問と全解答、学習チェック、前・次・親リンクを追加。 |
| `logic_tower/00_orientation/01_language_and_meaning.md` | UPGRADE_DONE | 2026-07-25 | 構文・意味・解釈の区別を構文木と複数割当で補強。自然言語の形式化で失う情報も明示し、Mermaid図、段階例2件、誤解・復帰手順、演習6問と全解答、学習チェック、前・次・親リンクを追加。 |
| `logic_tower/00_orientation/02_proof_and_model.md` | UPGRADE_DONE | 2026-07-25 | 証明可能性と意味論的帰結を分離し、反例モデルを使う段階例を追加。完全性を言語・意味論・証明体系の組に相対化し、Mermaid図、演習6問と全解答、復帰手順、学習チェック、前・次・親リンクを整備。 GitHub上のブロック数式表示を安定させるため、追加式の区切りを `$` に修正。 |
| `logic_tower/01_propositional_logic/00_overview.md` | UPGRADE_DONE | 2026-07-25 | 章入口を、構文・真理値表・標準形・自然演繹の役割が見える構成へ統一。Mermaid学習図、段階例2件、典型的誤解と復帰手順、演習6問と全解答、学習チェック、前・次・親リンクを追加。 GitHub上のブロック数式表示を安定させるため、追加式の区切りを `$` に修正。 |
| `logic_tower/01_propositional_logic/01_syntax_semantics.md` | UPGRADE_DONE | 2026-07-25 | 構文規則と意味評価の往復を補強し、主結合子・構文木・妥当性の区別を演習化。既存Mermaid図と例を保持し、演習6問と全解答、誤解・復帰手順、学習チェック、前・次・親リンクを整備。 |
| `logic_tower/01_propositional_logic/02_truth_tables.md` | UPGRADE_DONE | 2026-07-25 | 真理値表の作表・式分類・反例探索を6問の段階演習へ拡張。既存の2例とMermaid手順図を保持し、全解答、典型誤答と復帰手順、学習チェック、前・次・親リンクを整備。 |
| `logic_tower/01_propositional_logic/03_normal_forms.md` | UPGRADE_DONE | 2026-07-25 | CNF・DNFの変換例と同値法則を保持し、否定押し下げ・分配・簡単化・検算を段階演習化。Mermaid図、誤変形からの復帰手順、演習6問と全解答、学習チェック、前・次・親リンクを整備。 |
| `logic_tower/01_propositional_logic/04_natural_deduction.md` | UPGRADE_DONE | 2026-07-25 | 導入・除去規則と既存3例を保持し、仮定スコープ・選言除去・後件肯定を段階演習で補強。Mermaid図、演習6問と全解答、誤解・復帰手順、学習チェック、前・次・親リンクを整備。 |
| `logic_tower/02_predicate_logic/00_overview.md` | UPGRADE_DONE | 2026-07-25 | 命題論理から述語論理への拡張を、対象・述語・量化・構造の順で再構成。既存Mermaid図と対象付き推論を保持し、量化順序の段階例、誤解・復帰手順、演習6問と全解答、学習チェック、前・次・親リンクを整備。 |
| `logic_tower/02_predicate_logic/01_quantifiers.md` | UPGRADE_DONE | 2026-07-25 | 量化記号のスコープを括弧明記方針へ統一し、省略規則が教材・体系で異なることを明示。既存例とMermaid図を保持し、量化順序・自由変数・否定変形を含む演習6問と全解答、復帰手順、学習チェック、前・次・親リンクを整備。 |
| `logic_tower/02_predicate_logic/02_structures_and_models.md` | UPGRADE_DONE | 2026-07-25 | 構造・割当・項評価・充足・モデルの役割を分離し、有限構造と複数構造の段階例、反例モデル、典型的誤解と復帰手順、Mermaid図、演習6問と全解答、学習チェック、前・次・親リンクを整備。 |
| `logic_tower/02_predicate_logic/03_proofs.md` | UPGRADE_DONE | 2026-07-25 | 量化4規則を任意性・新鮮性・依存範囲と結び付け、全称導入と存在除去の段階証明、変数捕獲を含む誤証明、復帰手順、Mermaid図、演習6問と全解答、学習チェック、前・次・親リンクを整備。 |
| `logic_tower/03_soundness_completeness/00_overview.md` | UPGRADE_DONE | 2026-07-25 | 健全性・完全性を言語・意味論・証明体系の組に相対化し、完全性と算術理論の不完全性、コンパクト性と判定可能性を区別。Mermaid図、段階例2件、誤解・復帰手順、演習6問と全解答、学習チェック、章内外リンクを整備。 |
| `logic_tower/03_soundness_completeness/01_soundness.md` | UPGRADE_DONE | 2026-07-25 | 局所健全性・公理の妥当性から導出木の高さに関する帰納法で体系全体へ進む流れを明示。量化規則と含意導入の例、非健全規則の反例、保証範囲、Mermaid図、演習6問と全解答、復帰手順、学習チェック、前・次・親リンクを整備。 |
| `logic_tower/03_soundness_completeness/02_completeness.md` | UPGRADE_DONE | 2026-07-25 | 古典一階述語論理の全モデルに関する完全性と、実効的算術理論・標準自然数構造に関するGödelの不完全性を非標準モデルも含めて区別。対偶的モデル構成、保証しない事項、Mermaid図、演習6問と全解答、復帰手順、学習チェック、前・次・親リンクを整備。 |
| `logic_tower/03_soundness_completeness/03_compactness_low_level.md` | UPGRADE_DONE | 2026-07-25 | コンパクト性を存在定理として明記し、任意の有限部分と有限回の判定を分離。順序公理を暗黙にした例を相異なる定数 c_i≠c_j へ置換し、完全性・健全性からの導出、Mermaid図、演習6問と全解答、誤解・復帰手順、学習チェック、前・次・親リンクを整備。 |


## v1.1 発展・応用拡張キュー

> 完了状態：カテゴリREADME 6件と子記事65件をすべて `EXPANSION_DONE` に更新済み（2026-07-25）。未完了キューはありません。

### 運用ルール

- カテゴリREADMEは導線設計済み、子ページは本文未完成のスケルトンである。
- 優先順位は `EXPANDING`、次に表の先頭の `EXPANSION_TODO` とする。
- 1回の作業で本文化する子ページは1ファイルだけとし、同じ作業内で次の子ページへ着手しない。
- 完了時は `EXPANSION_DONE` に変更し、`last_updated` と判断理由を `notes` に残す。
- 本文化時は、冒頭ラベル、Mermaid図、読み取り説明、段階例、典型的誤解、復帰方法、演習5〜6問、全解答、学習チェック、相対リンクを整備する。
- 現代研究・製品・AIを扱う場合は、一次資料を確認し、事実の日付と推測・解釈を分ける。
- 既存の完成記事と重複する場合は、正本へリンクし、新規ページでは発展論点に集中する。

| file_path | status | last_updated | notes |
|---|---|---|---|
| `logic_tower/90_essays/foundations_and_expressiveness/README.md` | EXPANSION_DONE | 2026-07-25 | 全子記事の本文化完了に合わせ、状態・読み方・カテゴリ導線を完成版へ更新。 |
| `logic_tower/90_essays/foundations_and_expressiveness/00_when_is_a_sentence_a_proposition.md` | EXPANSION_DONE | 2026-07-25 | 文と命題を分離し、文脈・時点・指示対象・測定規約を固定する段階例を追加。Mermaid図、誤解と復帰手順、演習6問・全解答、学習チェック、前後リンクを整備。 |
| `logic_tower/90_essays/foundations_and_expressiveness/01_atomic_does_not_mean_indivisible.md` | EXPANSION_DONE | 2026-07-25 | 原子性を形式言語と分析目的に相対化し、Pから述語への粒度変更と仕様設計上の情報損失を具体化。図・演習6問・全解答・復帰手順を整備。 |
| `logic_tower/90_essays/foundations_and_expressiveness/02_why_propositional_logic_still_matters.md` | EXPANSION_DONE | 2026-07-25 | 有限問題の命題化、SAT・回路・設定探索への接続、符号化に相対的な保証範囲を説明。図・演習6問・全解答・復帰手順を整備。 |
| `logic_tower/90_essays/foundations_and_expressiveness/03_names_constants_and_identity.md` | EXPANSION_DONE | 2026-07-25 | 固有名・個体定項・変数・等号・存在・一意存在を分離し、標準一階論理と自由論理の境界を明示。図・演習6問・全解答を整備。 |
| `logic_tower/90_essays/foundations_and_expressiveness/04_quantifiers_in_mathematics.md` | EXPANSION_DONE | 2026-07-25 | 数学例で定義域、全称・存在、反例・証人、量化否定を段階化。図・演習6問・全解答・復帰手順を整備。 |
| `logic_tower/90_essays/foundations_and_expressiveness/05_quantifier_order.md` | EXPANSION_DONE | 2026-07-25 | ∀x∃yと∃y∀xを、依存する証人・共通証人・ゲーム意味論・実数例で比較。図・演習6問・全解答を整備。 |
| `logic_tower/90_essays/foundations_and_expressiveness/06_counterexamples_and_witnesses.md` | EXPANSION_DONE | 2026-07-25 | 反例と証人の非対称性、有限全探索と探索失敗の限界を整理。図・演習6問・全解答・復帰手順を整備。 |
| `logic_tower/90_essays/foundations_and_expressiveness/07_what_does_stronger_logic_mean.md` | EXPANSION_DONE | 2026-07-25 | 表現力・証明力・決定可能性・計算量を別軸に分解し、単一の最強順位を避ける比較枠組みを提示。図・演習6問・全解答を整備。 |
| `logic_tower/90_essays/foundations_and_expressiveness/08_first_order_vs_higher_order.md` | EXPANSION_DONE | 2026-07-25 | 個体量化と集合・関係量化、標準意味論とHenkin意味論、表現力と完全性の交換関係を整理。図・演習6問・全解答を整備。 |
| `logic_tower/90_essays/foundations_and_expressiveness/09_lindstrom_and_the_tradeoff.md` | EXPANSION_DONE | 2026-07-25 | Lindströmの定理を条件付き最大性として説明し、コンパクト性・下方Löwenheim–Skolem性・有限性表現の関係を明示。図・演習6問・全解答を整備。 |
| `logic_tower/90_essays/foundations_and_expressiveness/10_why_mathematics_uses_classical_first_order_foundations.md` | EXPANSION_DONE | 2026-07-25 | 一階論理と集合論の役割分担、完全性と不完全性、代替基礎を整理し、標準採用を唯一性と誤解しない構成へ本文化。 |
| `logic_tower/90_essays/hardware_and_sat/README.md` | EXPANSION_DONE | 2026-07-25 | 全子記事の本文化完了に合わせ、状態・読み方・カテゴリ導線を完成版へ更新。 |
| `logic_tower/90_essays/hardware_and_sat/00_boolean_algebra.md` | EXPANSION_DONE | 2026-07-25 | Boolean代数の基本法則、双対性、吸収律、論理式・代数・物理回路の三層を整理。図・演習6問・全解答を整備。 |
| `logic_tower/90_essays/hardware_and_sat/01_logic_gates.md` | EXPANSION_DONE | 2026-07-25 | AND・OR・NOTの真理関数から組合せ回路へ接続し、論理抽象と電圧・遅延など物理実装を分離。図・演習6問・全解答を整備。 |
| `logic_tower/90_essays/hardware_and_sat/02_functional_completeness.md` | EXPANSION_DONE | 2026-07-25 | 任意のBoolean関数の表現可能性をDNF構成で説明し、機能的完全性と効率性を区別。図・演習6問・全解答を整備。 |
| `logic_tower/90_essays/hardware_and_sat/03_nand_and_nor.md` | EXPANSION_DONE | 2026-07-25 | NAND・NORから基本ゲートを構成して万能性を示し、ゲート種類と個数・段数・性能を区別。図・演習6問・全解答を整備。 |
| `logic_tower/90_essays/hardware_and_sat/04_from_formulas_to_circuits.md` | EXPANSION_DONE | 2026-07-25 | 構文木から回路への変換、共通部分式共有によるDAG化、サイズ・深さ・ファンアウトの違いを説明。図・演習6問・全解答を整備。 |
| `logic_tower/90_essays/hardware_and_sat/05_circuit_equivalence.md` | EXPANSION_DONE | 2026-07-25 | miter回路とSATにより全入力等価性を反例探索へ変換し、組合せ回路と順序回路の前提差を明示。図・演習6問・全解答を整備。 |
| `logic_tower/90_essays/hardware_and_sat/06_sat_and_circuit_verification.md` | EXPANSION_DONE | 2026-07-25 | 回路違反条件、CNF、Tseitin等充足変換、有界検証の保証範囲を段階化。図・演習6問・全解答・反例確認手順を整備。 |
| `logic_tower/90_essays/hardware_and_sat/07_bdd_and_symbolic_representation.md` | EXPANSION_DONE | 2026-07-25 | BDD・ROBDDの共有と簡約、固定変数順序での標準性、順序依存の指数的膨張を整理。図・演習6問・全解答を整備。 |
| `logic_tower/90_essays/databases/README.md` | EXPANSION_DONE | 2026-07-25 | 全子記事の本文化完了に合わせ、状態・読み方・カテゴリ導線を完成版へ更新。 |
| `logic_tower/90_essays/databases/00_relations_as_mathematical_relations.md` | EXPANSION_DONE | 2026-07-25 | 関係・タプル・属性・定義域・スキーマを定義し、SQLのbag semantics・NULL・表示順との差を明示。図・演習6問・全解答を整備。 |
| `logic_tower/90_essays/databases/01_relational_algebra_and_first_order_logic.md` | EXPANSION_DONE | 2026-07-25 | 選択と連言・射影と存在量化・結合・差・安全性を整理。Mermaid図、段階例、誤解と復帰手順、演習6問・全解答、学習チェック、前後リンクを整備。 |
| `logic_tower/90_essays/databases/02_functional_dependencies.md` | EXPANSION_DONE | 2026-07-25 | 定義・制約と観測・自明・非自明を整理。Mermaid図、段階例、誤解と復帰手順、演習6問・全解答、学習チェック、前後リンクを整備。 |
| `logic_tower/90_essays/databases/03_armstrongs_axioms.md` | EXPANSION_DONE | 2026-07-25 | 反射律・増加律・推移律と完全性を整理。Mermaid図、段階例、誤解と復帰手順、演習6問・全解答、学習チェック、前後リンクを整備。 |
| `logic_tower/90_essays/databases/04_attribute_closure_and_keys.md` | EXPANSION_DONE | 2026-07-25 | 閉包アルゴリズム・スーパーキー・候補キーを整理。Mermaid図、段階例、誤解と復帰手順、演習6問・全解答、学習チェック、前後リンクを整備。 |
| `logic_tower/90_essays/databases/05_why_normalization_is_logical_reasoning.md` | EXPANSION_DONE | 2026-07-25 | 冗長性の原因・更新異常・分解の義務を整理。Mermaid図、段階例、誤解と復帰手順、演習6問・全解答、学習チェック、前後リンクを整備。 |
| `logic_tower/90_essays/databases/06_first_second_and_third_normal_forms.md` | EXPANSION_DONE | 2026-07-25 | 第一正規形・第二正規形・第三正規形を整理。Mermaid図、段階例、誤解と復帰手順、演習6問・全解答、学習チェック、前後リンクを整備。 |
| `logic_tower/90_essays/databases/07_bcnf_and_tradeoffs.md` | EXPANSION_DONE | 2026-07-25 | BCNF・3NFとの差・トレードオフを整理。Mermaid図、段階例、誤解と復帰手順、演習6問・全解答、学習チェック、前後リンクを整備。 |
| `logic_tower/90_essays/databases/08_lossless_join_decomposition.md` | EXPANSION_DONE | 2026-07-25 | 射影と再結合・二分解の条件・全インスタンスへの保証を整理。Mermaid図、段階例、誤解と復帰手順、演習6問・全解答、学習チェック、前後リンクを整備。 |
| `logic_tower/90_essays/databases/09_dependency_preservation.md` | EXPANSION_DONE | 2026-07-25 | 制約の射影・保存条件・実務的意味を整理。Mermaid図、段階例、誤解と復帰手順、演習6問・全解答、学習チェック、前後リンクを整備。 |
| `logic_tower/90_essays/databases/10_multivalued_dependencies_and_4nf.md` | EXPANSION_DONE | 2026-07-25 | 多値従属性・直積状の冗長性・第四正規形を整理。Mermaid図、段階例、誤解と復帰手順、演習6問・全解答、学習チェック、前後リンクを整備。 |
| `logic_tower/90_essays/databases/11_sql_null_and_three_valued_logic.md` | EXPANSION_DONE | 2026-07-25 | 比較とUNKNOWN・文脈ごとの採否・NOT INとNOT EXISTSを整理。Mermaid図、段階例、誤解と復帰手順、演習6問・全解答、学習チェック、前後リンクを整備。 |
| `logic_tower/90_essays/databases/12_why_real_databases_are_not_pure_set_theory.md` | EXPANSION_DONE | 2026-07-25 | 集合とバッグ・値と実行文脈・状態変化とトランザクションを整理。Mermaid図、段階例、誤解と復帰手順、演習6問・全解答、学習チェック、前後リンクを整備。 |
| `logic_tower/90_essays/modal_logic_and_verification/README.md` | EXPANSION_DONE | 2026-07-25 | 全子記事の本文化完了に合わせ、状態・読み方・カテゴリ導線を完成版へ更新。 |
| `logic_tower/90_essays/modal_logic_and_verification/00_standard_translation_to_first_order_logic.md` | EXPANSION_DONE | 2026-07-25 | 命題変数の持ち上げ・必然と可能・再帰的翻訳を整理。Mermaid図、段階例、誤解と復帰手順、演習6問・全解答、学習チェック、前後リンクを整備。 |
| `logic_tower/90_essays/modal_logic_and_verification/01_why_modal_logic_is_useful_even_if_translatable.md` | EXPANSION_DONE | 2026-07-25 | 意図を直接書く・モデルに相対的な読み・制限の利点を整理。Mermaid図、段階例、誤解と復帰手順、演習6問・全解答、学習チェック、前後リンクを整備。 |
| `logic_tower/90_essays/modal_logic_and_verification/02_temporal_logic_and_model_checking.md` | EXPANSION_DONE | 2026-07-25 | LTL・安全性と活性・モデル検査を整理。Mermaid図、段階例、誤解と復帰手順、演習6問・全解答、学習チェック、前後リンクを整備。 |
| `logic_tower/90_essays/modal_logic_and_verification/03_epistemic_logic_and_distributed_systems.md` | EXPANSION_DONE | 2026-07-25 | 個人の知識・相互知識と共通知識・通信と不可能性を整理。Mermaid図、段階例、誤解と復帰手順、演習6問・全解答、学習チェック、前後リンクを整備。 |
| `logic_tower/90_essays/modal_logic_and_verification/04_provability_logic.md` | EXPANSION_DONE | 2026-07-25 | 証明可能性述語・導出可能性条件・Gödel–Löb論理を整理。Mermaid図、段階例、誤解と復帰手順、演習6問・全解答、学習チェック、前後リンクを整備。 |
| `logic_tower/90_essays/modal_logic_and_verification/05_modal_logic_in_mathematics.md` | EXPANSION_DONE | 2026-07-25 | 位相意味論・forcingと集合論的宇宙・内部論理を整理。Mermaid図、段階例、誤解と復帰手順、演習6問・全解答、学習チェック、前後リンクを整備。 |
| `logic_tower/90_essays/modal_logic_and_verification/06_modal_logic_and_physics.md` | EXPANSION_DONE | 2026-07-25 | 可能性の種類・時空と因果・モデル依存性を整理。Mermaid図、段階例、誤解と復帰手順、演習6問・全解答、学習チェック、前後リンクを整備。 |
| `logic_tower/90_essays/quantum_computing_and_logic/README.md` | EXPANSION_DONE | 2026-07-25 | 全子記事の本文化完了に合わせ、状態・読み方・カテゴリ導線を完成版へ更新。 |
| `logic_tower/90_essays/quantum_computing_and_logic/00_bits_boolean_functions_and_classical_circuits.md` | EXPANSION_DONE | 2026-07-25 | ビット・Boolean関数・状態を持つ回路を整理。Mermaid図、段階例、誤解と復帰手順、演習6問・全解答、学習チェック、前後リンクを整備。 |
| `logic_tower/90_essays/quantum_computing_and_logic/01_why_classical_gates_can_be_irreversible.md` | EXPANSION_DONE | 2026-07-25 | 単射性・古典実装・情報と熱を整理。Mermaid図、段階例、誤解と復帰手順、演習6問・全解答、学習チェック、前後リンクを整備。 |
| `logic_tower/90_essays/quantum_computing_and_logic/02_reversible_computation.md` | EXPANSION_DONE | 2026-07-25 | 可逆ゲート・埋め込み・補助情報の後始末を整理。Mermaid図、段階例、誤解と復帰手順、演習6問・全解答、学習チェック、前後リンクを整備。 |
| `logic_tower/90_essays/quantum_computing_and_logic/03_qubits_are_not_three_valued_bits.md` | EXPANSION_DONE | 2026-07-25 | 重ね合わせ・測定基底・混合状態を整理。Mermaid図、段階例、誤解と復帰手順、演習6問・全解答、学習チェック、前後リンクを整備。 |
| `logic_tower/90_essays/quantum_computing_and_logic/04_quantum_gates_as_linear_transformations.md` | EXPANSION_DONE | 2026-07-25 | 線形性・ユニタリ性・多量子ビットを整理。Mermaid図、段階例、誤解と復帰手順、演習6問・全解答、学習チェック、前後リンクを整備。 |
| `logic_tower/90_essays/quantum_computing_and_logic/05_toffoli_and_embedded_boolean_computation.md` | EXPANSION_DONE | 2026-07-25 | CCNOT・ANDの保存・万能性の範囲を整理。Mermaid図、段階例、誤解と復帰手順、演習6問・全解答、学習チェック、前後リンクを整備。 |
| `logic_tower/90_essays/quantum_computing_and_logic/06_measurement_and_probability.md` | EXPANSION_DONE | 2026-07-25 | Born則・状態更新・統計的推定を整理。Mermaid図、段階例、誤解と復帰手順、演習6問・全解答、学習チェック、前後リンクを整備。 |
| `logic_tower/90_essays/quantum_computing_and_logic/07_quantum_logic_is_not_quantum_programming.md` | EXPANSION_DONE | 2026-07-25 | 計算モデル・命題構造・非Boolean性を整理。Mermaid図、段階例、誤解と復帰手順、演習6問・全解答、学習チェック、前後リンクを整備。 |
| `logic_tower/90_essays/quantum_computing_and_logic/08_propositions_in_quantum_mechanics.md` | EXPANSION_DONE | 2026-07-25 | 射影命題・格子演算・文脈と可換性を整理。Mermaid図、段階例、誤解と復帰手順、演習6問・全解答、学習チェック、前後リンクを整備。 |
| `logic_tower/90_essays/quantum_computing_and_logic/09_does_quantum_mechanics_refute_classical_logic.md` | EXPANSION_DONE | 2026-07-25 | 対象レベル・メタレベル・複数の立場を整理。Mermaid図、段階例、誤解と復帰手順、演習6問・全解答、学習チェック、前後リンクを整備。 |
| `logic_tower/90_essays/ai_mathematics_and_logic/README.md` | EXPANSION_DONE | 2026-07-25 | 全子記事の本文化完了に合わせ、状態・読み方・カテゴリ導線を完成版へ更新。 |
| `logic_tower/90_essays/ai_mathematics_and_logic/00_what_does_it_mean_for_ai_to_solve_math.md` | EXPANSION_DONE | 2026-07-25 | 出力の型・検証の型・成果の文脈を整理。Mermaid図、段階例、誤解と復帰手順、演習6問・全解答、学習チェック、前後リンクを整備。 |
| `logic_tower/90_essays/ai_mathematics_and_logic/01_llms_are_not_proof_checkers.md` | EXPANSION_DONE | 2026-07-25 | 確率的生成・小さな検査器・役割分担を整理。Mermaid図、段階例、誤解と復帰手順、演習6問・全解答、学習チェック、前後リンクを整備。 |
| `logic_tower/90_essays/ai_mathematics_and_logic/02_proof_generation_and_verification.md` | EXPANSION_DONE | 2026-07-25 | 生成・検証・信頼基盤を整理。Mermaid図、段階例、誤解と復帰手順、演習6問・全解答、学習チェック、前後リンクを整備。 |
| `logic_tower/90_essays/ai_mathematics_and_logic/03_search_space_of_mathematical_proofs.md` | EXPANSION_DONE | 2026-07-25 | 状態・行動・誘導を整理。Mermaid図、段階例、誤解と復帰手順、演習6問・全解答、学習チェック、前後リンクを整備。 |
| `logic_tower/90_essays/ai_mathematics_and_logic/04_tactic_prediction.md` | EXPANSION_DONE | 2026-07-25 | 入力表現・候補生成・評価を整理。Mermaid図、段階例、誤解と復帰手順、演習6問・全解答、学習チェック、前後リンクを整備。 |
| `logic_tower/90_essays/ai_mathematics_and_logic/05_lean_coq_and_formal_mathematics.md` | EXPANSION_DONE | 2026-07-25 | Curry–Howard対応・ツール層・形式数学の資産を整理。Mermaid図、段階例、誤解と復帰手順、演習6問・全解答、学習チェック、前後リンクを整備。 |
| `logic_tower/90_essays/ai_mathematics_and_logic/06_neural_theorem_proving.md` | EXPANSION_DONE | 2026-07-25 | 前提選択・方策と価値・環境フィードバックを整理。Mermaid図、段階例、誤解と復帰手順、演習6問・全解答、学習チェック、前後リンクを整備。 |
| `logic_tower/90_essays/ai_mathematics_and_logic/07_reinforcement_learning_for_proofs.md` | EXPANSION_DONE | 2026-07-25 | 状態と遷移・学習信号・自己生成を整理。Mermaid図、段階例、誤解と復帰手順、演習6問・全解答、学習チェック、前後リンクを整備。 |
| `logic_tower/90_essays/ai_mathematics_and_logic/08_alphaproof_and_olympiad_mathematics.md` | EXPANSION_DONE | 2026-07-25 | 確認された結果・形式化と探索・計算条件を整理。Mermaid図、段階例、誤解と復帰手順、演習6問・全解答、学習チェック、前後リンクを整備。 |
| `logic_tower/90_essays/ai_mathematics_and_logic/09_conjecture_generation.md` | EXPANSION_DONE | 2026-07-25 | パターン抽出・候補のフィルタ・研究サイクルを整理。Mermaid図、段階例、誤解と復帰手順、演習6問・全解答、学習チェック、前後リンクを整備。 |
| `logic_tower/90_essays/ai_mathematics_and_logic/10_counterexample_search.md` | EXPANSION_DONE | 2026-07-25 | 否定の形式化・探索手段・検証と縮小を整理。Mermaid図、段階例、誤解と復帰手順、演習6問・全解答、学習チェック、前後リンクを整備。 |
| `logic_tower/90_essays/ai_mathematics_and_logic/11_formalization_bottleneck.md` | EXPANSION_DONE | 2026-07-25 | 定理文の曖昧さ・依存知識・保守性を整理。Mermaid図、段階例、誤解と復帰手順、演習6問・全解答、学習チェック、前後リンクを整備。 |
| `logic_tower/90_essays/ai_mathematics_and_logic/12_can_llms_discover_new_mathematics.md` | EXPANSION_DONE | 2026-07-25 | 新規性の層・検証パイプライン・共同発見を整理。Mermaid図、段階例、誤解と復帰手順、演習6問・全解答、学習チェック、前後リンクを整備。 |
| `logic_tower/90_essays/ai_mathematics_and_logic/13_when_an_ai_proof_should_be_trusted.md` | EXPANSION_DONE | 2026-07-25 | 定理文・証明と公理・再現性を整理。Mermaid図、段階例、誤解と復帰手順、演習6問・全解答、学習チェック、前後リンクを整備。 |
| `logic_tower/90_essays/ai_mathematics_and_logic/14_human_ai_mathematical_collaboration.md` | EXPANSION_DONE | 2026-07-25 | 探索の分業・検証の分業・来歴管理を整理。Mermaid図、段階例、誤解と復帰手順、演習6問・全解答、学習チェック、前後リンクを整備。 |
| `logic_tower/90_essays/ai_mathematics_and_logic/15_why_math_is_good_for_verifiable_ai.md` | EXPANSION_DONE | 2026-07-25 | 安価な反証と検査・探索のスケール・境界を整理。Mermaid図、段階例、誤解と復帰手順、演習6問・全解答、学習チェック、前後リンクを整備。 |
