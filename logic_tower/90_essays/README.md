# 発展・応用エッセイ

この領域は、Logic Tower本線で学んだ論理を、数学、回路、データベース、検証、量子計算、AIへ接続する支線です。

個別分野を並べるだけでなく、全記事を次の中心軸でつなぎます。

> 表現力 ― 推論可能性 ― 計算可能性 ― 実用性

## 完成本文化済みの橋渡し記事

以下の3記事は既存の正本として残します。

- [論理とデータベース問い合わせ](logic_and_database_queries.md)
- [様相論理と計算・モデル検査](modal_logic_and_computation.md)
- [証明支援系と論理](proof_assistants_and_logic.md)

新しいカテゴリ内の記事は、これらを複製せず、前提記事として参照して発展部分へ進みます。

## 新しいカテゴリ

- [論理の粒度・表現力・限界](foundations_and_expressiveness/) — 自然言語を命題として切り出す段階から、一階論理と高階論理のトレードオフまでを扱います。
- [Boolean代数・回路・SAT](hardware_and_sat/) — 命題論理から論理ゲート、回路検証、SATソルバーへ接続します。
- [論理とデータベース設計](databases/) — 問い合わせだけでなく、関数従属性・キー・正規化・無損失分解を形式的推論として扱います。
- [様相論理・時間・知識・検証](modal_logic_and_verification/) — 様相論理を一階論理へ翻訳できても専用記法が有用な理由と、計算機科学・数学での用途を扱います。
- [量子計算と論理](quantum_computing_and_logic/) — 古典Boolean回路から可逆計算・量子ゲートへ進み、量子論理との違いを明確にします。
- [AI・形式数学・証明探索](ai_mathematics_and_logic/) — LLMの候補生成、探索、形式検証を分離し、AIが数学を解くとは何かを検討します。

## 問いから選ぶ

| 疑問 | 最初に読む場所 |
|---|---|
| 自然言語の命題は本当に明確か | [論理の粒度・表現力・限界](foundations_and_expressiveness/) |
| 命題論理は現代でも使われるか | [Boolean代数・回路・SAT](hardware_and_sat/) |
| 一階論理は高階論理より強いのか | [論理の粒度・表現力・限界](foundations_and_expressiveness/) |
| 様相論理は一階論理で代替できるか | [様相論理・時間・知識・検証](modal_logic_and_verification/) |
| 正規化は論理とどう関係するか | [論理とデータベース設計](databases/) |
| 量子計算では古典論理を捨てるのか | [量子計算と論理](quantum_computing_and_logic/) |
| LLMは数学をどう解くのか | [AI・形式数学・証明探索](ai_mathematics_and_logic/) |

## 本線との往復

- 命題・原子性・抽象化に迷ったら：[00_orientation](../00_orientation/)
- 真理値関数・標準形に戻るなら：[01_propositional_logic](../01_propositional_logic/)
- 量化・構造・モデルに戻るなら：[02_predicate_logic](../02_predicate_logic/)
- 健全性・完全性・コンパクト性に戻るなら：[03_soundness_completeness](../03_soundness_completeness/)
- 決定可能性・探索限界に戻るなら：[04_computability_and_automata](../04_computability_and_automata/)
- 可能世界・非古典論理に戻るなら：[05_modal_and_nonclassical](../05_modal_and_nonclassical/)

## 記事状態

カテゴリREADMEは導線設計済みです。各子ページは概要・論点・注意点だけを持つスケルトンであり、[PROGRESS.md](../PROGRESS.md) の拡張キュー順に本文化します。

本文化時は、記事冒頭のラベル、確立事項・実証結果・解釈・仮説の区別、一次資料の日付、Mermaid図、段階例、演習と全解答をそろえます。

## ナビゲーション

- 親：[../README.md](../README.md)
- 進捗：[../PROGRESS.md](../PROGRESS.md)
