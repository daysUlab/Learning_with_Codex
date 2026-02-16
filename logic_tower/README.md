# logic_tower

logic_tower の入口ページです。
このタワーは、**「論理式を読むのが初めて」**という段階から、
命題論理・述語論理・完全性・計算可能性・様相論理までを、
段階的に学べるように設計しています。

physics_tower と同様に、単語の定義だけで終わらず、
**直観 → 定義 → 例 → 手を動かす確認**の流れで理解を積み上げます。

## このタワーで到達したい状態
- 命題・述語・証明・モデルの違いを、自分の言葉で説明できる。
- 真理値表や自然演繹で、短い主張の妥当性を確認できる。
- 「証明できること」と「意味的に正しいこと」の関係（健全性・完全性）を理解できる。
- 計算機科学（オートマトン・決定可能性）とのつながりを説明できる。
- 非古典論理（様相論理・直観主義論理）の位置づけを把握できる。

## 初学者向けの読み方（おすすめ）
1. `00_orientation` で、論理学の役割と「証明 vs モデル」の見取り図をつかむ。
2. `01_propositional_logic` で、記号の読み方と真理値表に慣れる。
3. `02_predicate_logic` で、量化（「すべて」「ある」）の扱いを学ぶ。
4. `03_soundness_completeness` で、証明体系の意味を整理する。
5. `04_computability_and_automata` で、形式言語と計算可能性へ接続する。
6. `05_modal_and_nonclassical` で、古典論理の外側を俯瞰する。
7. `90_essays` で、実務・他分野への応用イメージを補強する。

## 学習時のコツ
- 記号を丸暗記せず、**日本語文との対応**を必ず確認する。
- 「どの前提から何を示したか」を毎回1行でメモする。
- 行き詰まったら、無理に進まず `00_orientation` の定義へ戻る。

## 運用メモ
- 執筆順は [PROGRESS.md](PROGRESS.md) のキューに従います。
- 章の本文化は 1 回の実行で 1 ファイルずつ進めます。
- 新しい章に入る際は、先に子mdを3本以上スケルトン作成してから本文化します。

## ナビゲーション
- 親: [README.md](README.md)
- 子:
  - [00_orientation/](00_orientation/)
  - [01_propositional_logic/](01_propositional_logic/)
  - [02_predicate_logic/](02_predicate_logic/)
  - [03_soundness_completeness/](03_soundness_completeness/)
  - [04_computability_and_automata/](04_computability_and_automata/)
  - [05_modal_and_nonclassical/](05_modal_and_nonclassical/)
  - [90_essays/](90_essays/)
