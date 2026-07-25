# logic_tower 執筆進捗（PROGRESS）

## 運用ルール（このリポジトリ専用）
- ユーザーが **「次をお願いします」** とだけ指示した場合も、このファイルを最初に確認する。
- 優先順位は次の通り。
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
| `logic_tower/02_predicate_logic/01_quantifiers.md` | DONE | 2026-02-16 | 量化記号を本文化。Mermaid学習フロー図、TeX記法、否定同値変形、スコープ注意点、演習を追加。 |
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
| `logic_tower/02_predicate_logic/01_quantifiers.md` | UPGRADE_TODO |  | 量化記号のスコープを括弧明記方針へ統一し、誤読例を補う。 |
| `logic_tower/02_predicate_logic/02_structures_and_models.md` | UPGRADE_TODO |  | 構造・割当・満足・モデルの区別を具体例で補強する。 |
| `logic_tower/02_predicate_logic/03_proofs.md` | UPGRADE_TODO |  | 量化規則の変数条件と典型的な誤証明を補強する。 |
| `logic_tower/03_soundness_completeness/00_overview.md` | UPGRADE_TODO |  | 性質を言語・意味論・証明体系の組に相対化し、完全性と不完全性の混同を防ぐ。 |
| `logic_tower/03_soundness_completeness/01_soundness.md` | UPGRADE_TODO |  | 局所健全性から体系全体の健全性への流れを補強する。 |
| `logic_tower/03_soundness_completeness/02_completeness.md` | UPGRADE_TODO |  | 古典一階述語論理の完全性とGödelの不完全性を明確に区別する。 |
| `logic_tower/03_soundness_completeness/03_compactness_low_level.md` | UPGRADE_TODO |  | 有限部分の充足可能性と判定アルゴリズムを区別し、無限モデル例の前提を厳密化する。 |
