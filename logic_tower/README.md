# Logic Tower――論理を選ぶ理由まで学ぶ

Logic Towerは、論理体系を順番に覚えるだけでなく、**なぜその論理を使うのか、どこまで表現できるのか、現代科学・計算機・AIにどう残っているのか**を追う教材です。

中心となる問いは次です。

> なぜ、より表現力の高い論理があるのに、命題論理や一階述語論理を使い続けるのか。

論理は強ければ強いほどよいのではありません。用途に合わせて、次の軸の釣り合いを選びます。

- 表現力：何を直接書けるか
- 推論可能性：どの結論を規則から導けるか
- 計算可能性：機械的に何を判定・探索できるか
- 実用性：どの抽象化が問題を見通しよくするか

## 読み方：本線と支線

### 本線

初学者が順番に読む必修コースです。本線は短く保ちます。

1. [00_orientation](00_orientation/) — 文、命題、意味、証明、モデル
2. [01_propositional_logic](01_propositional_logic/) — 命題論理、真理値表、標準形、自然演繹
3. [02_predicate_logic](02_predicate_logic/) — 述語、量化、構造、モデル
4. [03_soundness_completeness](03_soundness_completeness/) — 健全性、完全性、コンパクト性
5. [04_computability_and_automata](04_computability_and_automata/) — 形式言語、計算モデル、決定可能性
6. [05_modal_and_nonclassical](05_modal_and_nonclassical/) — 様相論理、直観主義論理、非古典論理

### 支線

[90_essays](90_essays/) 以下は、疑問や応用から本線へ戻る発展コースです。既存の完成記事を残しながら、カテゴリ別スケルトンを段階的に本文化します。

- [論理の粒度・表現力・限界](90_essays/foundations_and_expressiveness/)
- [Boolean代数・回路・SAT](90_essays/hardware_and_sat/)
- [論理とデータベース設計](90_essays/databases/)
- [様相論理・時間・知識・検証](90_essays/modal_logic_and_verification/)
- [量子計算と論理](90_essays/quantum_computing_and_logic/)
- [AI・形式数学・証明探索](90_essays/ai_mathematics_and_logic/)

## 読者別ルート

### 数学ルート

命題論理 → 述語論理 → 証明とモデル → 健全性・完全性 → [表現力と限界](90_essays/foundations_and_expressiveness/) → 高階論理・数学基礎論

### ソフトウェアルート

命題論理 → [Boolean代数・SAT](90_essays/hardware_and_sat/) → 計算可能性 → [様相論理・検証](90_essays/modal_logic_and_verification/) → 証明支援系

### データエンジニアルート

述語論理 → 集合と関係 → [DB問い合わせ](90_essays/logic_and_database_queries.md) → [関数従属性・正規化](90_essays/databases/)

### AIルート

命題論理 → 述語論理 → 証明探索 → 計算可能性 → [証明支援系](90_essays/proof_assistants_and_logic.md) → [AIと形式数学](90_essays/ai_mathematics_and_logic/)

### 量子ルート

命題論理 → [Boolean代数・古典回路](90_essays/hardware_and_sat/) → [可逆計算・量子回路・量子論理](90_essays/quantum_computing_and_logic/)

## ページラベル

本文化したページでは、冒頭に次を表示します。

- 種別：本線 / 発展 / 応用 / エッセイ
- 前提：なし / 命題論理 / 述語論理 / 線形代数など
- 難易度：入門 / 基礎 / 発展
- 読了目安
- 状態：スケルトン / 本文化済み

## 記述の確かさ

現代研究やAIを扱う記事では、次を区別します。

- **定理**：明示した形式体系の下で数学的に証明された内容
- **実証結果**：論文・実験・ベンチマークで確認された内容
- **解釈**：事実や結果を理解するための説明
- **仮説**：今後の検証が必要な考え

エッセイは誤りを許容する領域ではありません。確立事項と筆者の解釈・仮説を表示したうえで、思考実験を行います。

## 共通する学習方針

- 自然言語例は、直観と形式化の選択・曖昧さを学ぶために使う。
- 数学例は、量化、反例、証人、証明、モデルを明確に学ぶために使う。
- 原子命題は世界の最小単位ではなく、今回の分析で分解しない単位として扱う。
- 真理、妥当性、証明可能性、決定可能性を区別する。
- ツールが式を正しく処理することと、その式が意図を正しく表すことを区別する。

## 執筆側の運用

- 執筆順は [PROGRESS.md](PROGRESS.md) のキューに従う。
- 本文化は1回の作業で1ファイルだけ進める。
- スケルトンは完成本文ではなく、論点と注意点を固定した設計メモである。
- 本文化時は、直観 → 定義 → 例 → 誤解・復帰方法 → 演習 → 全解答 → 学習チェックを基本とする。
- Mermaid図を原則1記事1図以上入れ、読み取りポイントを説明する。

## ナビゲーション

- 親：[../README.md](../README.md)
- 本線：[00_orientation](00_orientation/)
- 発展・応用：[90_essays](90_essays/)
- 進捗：[PROGRESS.md](PROGRESS.md)
