# 熱力学と統計力学の境界

## 二つの理論の役割

| 熱力学 | 統計力学 |
|---|---|
| 微視構造を仮定しない | microstateとHamiltonianを仮定する |
| 状態量の関係 | 状態数と確率 |
| 可能・不可能な過程 | なぜその過程が圧倒的か |
| 平衡条件・最大効率 | 平均・揺らぎ・相転移 |
| energy・entropy収支 | 比熱や物質差の計算 |

熱力学は統計力学の未完成版ではありません。engineの最大効率や平衡条件は分子modelなしに厳密な制約を与えます。統計力学は、entropyがなぜ増えるか、温度や圧力が何を平均した量か、物質ごとの値がなぜ違うかを説明します。

## 同じ量を別方向から見る

熱力学では

$$
\frac1T=\left(\frac{\partial S}{\partial U}\right)_{V,N}
$$

を状態関係として使います。統計力学では

$$
S=k_B\ln\Omega
$$

を通じて状態数のenergy依存から温度を説明します。

## 判断例

- heat engineの最大効率：熱力学。
- ideal gas圧力の分子衝突起源：統計力学。
- phase coexistence条件：熱力学。
- critical fluctuationとuniversality：統計力学。
- semiconductor carrier density：量子統計力学。

## 演習と全解答

1. Carnot効率に分子modelは必要か。
   **解答**：不要です。
2. 比熱の数値を第一原理から出すのはどちらか。
   **解答**：統計力学に量子・物質modelを組み合わせます。
3. entropy収支を立てるのはどちらか。
   **解答**：熱力学です。
4. fluctuationの大きさを扱うのはどちらか。
   **解答**：統計力学です。
5. Fermi levelを巨視的平衡で何に対応させるか。
   **解答**：electronのchemical potentialです。
6. 熱力学が正しく統計modelが外れた場合、何を疑うか。
   **解答**：microstate、Hamiltonian、相互作用、classical/quantum近似を疑います。

## 次の理論

[統計力学](../../05_statistical_mechanics/00_overview.md)では粒子運動→状態数→ensemble→partition function→量子統計の順に微視的理由を組み立てます。

- 前：[工学応用](03_engineering_energy_and_cooling.md)
- 親：[part02](README.md)
