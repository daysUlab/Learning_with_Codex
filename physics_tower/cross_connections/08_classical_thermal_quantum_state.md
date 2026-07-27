# 古典状態・熱力学状態・量子状態

| 軸 | 古典力学 | 熱力学 | 統計力学 | 量子力学 |
|---|---|---|---|---|
| 状態 | phase-space point | 少数の巨視量 | microstate分布 | state vector／density operator |
| 捨てる情報 | 原則trajectoryを保持 | 個々の粒子 | 個体labelやtrajectoryの詳細 | 同時に確定しない古典値 |
| 発展 | Hamilton flow | process・balance | Liouville/master/ensemble | unitary＋測定規則 |
| 確率 | 初期条件の無知 | 通常は直接不要 | ensemble・粗視化 | amplitudeからBorn則 |

同じ「状態」は分野ごとに十分統計量が違います。熱力学stateは量子stateの粗い別名ではなく、平衡・巨視scaleで目的に十分な圧縮です。

## 演習と全解答

1. 温度だけで一個の分子位置を予測できるか。
   **解答**：できません。温度は巨視的state variableです。
2. 古典phase-space分布と量子pure stateは同じ確率分布か。
   **解答**：違います。量子stateは相対phaseと非可換observableを持ちます。
3. density matrixは常に熱平衡か。
   **解答**：いいえ。任意のmixed stateや部分系stateを表します。
4. 同じmacrostateに複数microstateが対応するか。
   **解答**：対応します。
5. 量子測定結果をthermal fluctuationと同一視できるか。
   **解答**：できません。量子測定確率はzero temperatureのpure stateにもあります。
6. model選択で最初に問うことを述べよ。
   **解答**：目的のobservableとscaleに、どの情報を残せば十分かです。

- 親：[横断README](README.md)
- 関連：[量子overview](../07_quantum_mechanics/00_overview.md)
