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
| `logic_tower/00_orientation/00_what_is_logic.md` | DONE | 2026-02-16 | 論理学の目的・必要性・誤謬例・証明/意味の2視点・最小用語・確認問題を追加し初学者向けに本文化。 |
| `logic_tower/00_orientation/01_language_and_meaning.md` | DONE | 2026-02-16 | 構文と意味の違いを初学者向けに本文化。規則・直観例・誤解・ミニ演習・自己確認を追加。 |
| `logic_tower/00_orientation/02_proof_and_model.md` | DONE | 2026-02-16 | 証明視点とモデル視点の違いを本文化。記号（⊢/⊨）、健全性/完全性の入口、演習と自己確認を追加。 |
| `logic_tower/01_propositional_logic/00_overview.md` | DONE | 2026-02-16 | 命題論理章の入口を本文化。到達目標・学習マップ・典型例・つまずき対策・自己確認を追加。 |
| `logic_tower/01_propositional_logic/01_syntax_semantics.md` | DONE | 2026-02-16 | 構文と意味の基礎を本文化。Mermaid図のGitHub互換性を修正し、処理フロー可視化・規則・例・演習・自己確認を整備。 |
| `logic_tower/01_propositional_logic/02_truth_tables.md` | DONE | 2026-02-16 | 真理値表の作り方を本文化。Mermaid手順図とTeX論理記号を用いて判定手順・反例探索・演習を追加。 |
| `logic_tower/01_propositional_logic/03_normal_forms.md` | DONE | 2026-02-16 | 標準形（CNF/DNF）を本文化。Mermaid変換フロー図とTeX記法で同値変形・例題・演習を追加。 |
| `logic_tower/01_propositional_logic/04_natural_deduction.md` | DONE | 2026-02-16 | 自然演繹を本文化。Mermaid証明フロー図、導入/除去規則、TeX記号での例題・演習を追加。 |
| `logic_tower/02_predicate_logic/00_overview.md` | TODO | - |  |
| `logic_tower/02_predicate_logic/01_quantifiers.md` | TODO | - |  |
| `logic_tower/02_predicate_logic/02_structures_and_models.md` | TODO | - |  |
| `logic_tower/02_predicate_logic/03_proofs.md` | TODO | - |  |
| `logic_tower/03_soundness_completeness/00_overview.md` | TODO | - |  |
| `logic_tower/03_soundness_completeness/01_soundness.md` | TODO | - |  |
| `logic_tower/03_soundness_completeness/02_completeness.md` | TODO | - |  |
| `logic_tower/03_soundness_completeness/03_compactness_low_level.md` | TODO | - |  |
| `logic_tower/04_computability_and_automata/00_overview.md` | TODO | - |  |
| `logic_tower/04_computability_and_automata/01_finite_automata.md` | TODO | - |  |
| `logic_tower/04_computability_and_automata/02_pushdown_automata.md` | TODO | - |  |
| `logic_tower/04_computability_and_automata/03_turing_machines.md` | TODO | - |  |
| `logic_tower/04_computability_and_automata/04_decidability.md` | TODO | - |  |
| `logic_tower/05_modal_and_nonclassical/00_overview.md` | TODO | - |  |
| `logic_tower/05_modal_and_nonclassical/01_modal_logic_kripke.md` | TODO | - |  |
| `logic_tower/05_modal_and_nonclassical/02_intuitionistic_logic.md` | TODO | - |  |
| `logic_tower/05_modal_and_nonclassical/03_other_logics_map.md` | TODO | - |  |
| `logic_tower/90_essays/README.md` | TODO | - |  |
| `logic_tower/90_essays/logic_and_database_queries.md` | TODO | - | 新規スケルトン（子md拡張）。 |
| `logic_tower/90_essays/modal_logic_and_computation.md` | TODO | - |  |
| `logic_tower/90_essays/proof_assistants_and_logic.md` | TODO | - | 新規スケルトン（子md拡張）。 |
| `logic_tower/PROGRESS.md` | DONE | 2026-02-16 | physics_tower の運用を踏襲して進捗管理基盤を新規作成。 |
