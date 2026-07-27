# 量子計算と論理

古典Boolean回路から可逆計算・量子ゲートへ進み、量子論理との違いを明確にします。

物理的な量子state、Born則、unitary時間発展、entanglement、decoherenceの正本は[Physics Towerの量子力学](../../../physics_tower/07_quantum_mechanics/00_overview.md)です。本カテゴリはBoolean回路、可逆計算、qubitを三値論理と誤認しないこと、量子論理とprogrammingの違いを担当します。

> 種別：発展・応用  
> 状態：全10記事 本文化済み  
> 前提：命題論理・線形代数の初歩

## このカテゴリの役割

全10記事を本文化済みです。古典Boolean回路、可逆計算、量子ゲート、測定を順に学び、最後に量子計算と量子論理、対象レベルとメタレベルを分離します。

## 記事一覧

| # | 記事 | 概要 |
|---:|---|---|
| 1 | [ビット・Boolean関数・古典回路](00_bits_boolean_functions_and_classical_circuits.md) | 古典計算の状態と演算を整理し、量子回路との比較基準を作る。 |
| 2 | [古典ゲートはなぜ不可逆でもよいのか](01_why_classical_gates_can_be_irreversible.md) | ANDなどが入力情報を失うことと、古典計算機での熱・消去の議論への入口を作る。 |
| 3 | [可逆計算](02_reversible_computation.md) | 入力から出力を一意に逆算できる計算と、古典関数の可逆埋め込みを学ぶ。 |
| 4 | [量子ビットは三値ビットではない](03_qubits_are_not_three_valued_bits.md) | 重ね合わせを0・1・その中間という第三の真理値と誤解しないための基礎を作る。 |
| 5 | [量子ゲートは線形変換](04_quantum_gates_as_linear_transformations.md) | 量子ゲートを複素ベクトル空間上のユニタリ変換として扱う。 |
| 6 | [ToffoliゲートとBoolean計算の埋め込み](05_toffoli_and_embedded_boolean_computation.md) | 不可逆なBoolean関数を補助量子ビット付きの可逆写像へ埋め込む。 |
| 7 | [測定と確率](06_measurement_and_probability.md) | 量子状態から古典的結果が得られる測定と、振幅・確率・状態更新を区別する。 |
| 8 | [量子論理は量子プログラミングではない](07_quantum_logic_is_not_quantum_programming.md) | 量子回路の計算モデルと、量子力学の命題構造を扱う量子論理を分離する。 |
| 9 | [量子力学における命題](08_propositions_in_quantum_mechanics.md) | 観測可能量の命題を射影作用素や閉部分空間へ対応させ、非Boolean性の意味を探る。 |
| 10 | [量子力学は古典論理を否定するのか](09_does_quantum_mechanics_refute_classical_logic.md) | 物理理論の対象レベルと、それを記述するメタレベルの古典数学を分けて論争を整理する。 |

## 各記事の共通構成

- 直観 → 定義 → 例 → 誤解・復帰方法 → 演習 → 全解答 → 学習チェックの順を基本とする。
- ページ冒頭に種別・前提・難易度・読了目安を表示する。
- 確立事項、実証結果、解釈、仮説を区別する。
- 既存の完成記事と重複する場合は、正本へリンクして発展部分に集中する。

## ナビゲーション

- 親：[../README.md](../README.md)
- タワー入口：[../../README.md](../../README.md)
- 進捗：[../../PROGRESS.md](../../PROGRESS.md)
