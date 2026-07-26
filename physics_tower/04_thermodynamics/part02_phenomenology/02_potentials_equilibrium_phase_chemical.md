# 熱力学potential・平衡・相・chemical potential

## 自然変数を選ぶ

単純系のfundamental relationは

$$
dU=T\,dS-p\,dV+\mu\,dN
$$

です。外界が固定する変数に応じてLegendre変換します。

| potential | 定義 | 自然変数 | 平衡での性質 |
|---|---|---|---|
| internal energy | U | S, V, N | 最小 |
| enthalpy | H＝U＋pV | S, p, N | 最小 |
| Helmholtz free energy | F＝U−TS | T, V, N | 最小 |
| Gibbs free energy | G＝U−TS＋pV | T, p, N | 最小 |

例えば

$$
dF=-S\,dT-p\,dV+\mu\,dN
$$

です。

## chemical potentialと相平衡

$$
\mu=\left(\frac{\partial U}{\partial N}\right)_{S,V}
$$

は粒子を一つ加えるenergy costです。物質移動可能な二系の平衡条件は

$$
\mu_A=\mu_B
$$

です。二相共存では温度、圧力、各成分のchemical potentialが一致します。

## Maxwell関係

$$
dF=-S\,dT-p\,dV
$$

の混合偏微分から

$$
\left(\frac{\partial S}{\partial V}\right)_T
=
\left(\frac{\partial p}{\partial T}\right)_V
$$

を得ます。

## 演習と全解答

1. 室温・定容で選ぶpotentialは何か。
   **解答**：Helmholtz free energyです。
2. 室温・大気圧で化学反応に使うpotentialは何か。
   **解答**：Gibbs free energyです。
3.
   $$
   dG
   $$
   を書け。
   **解答**：
   $$
   dG=-S\,dT+V\,dp+\mu\,dN
   $$
4. particle flowはどちら向きか。
   **解答**：他条件固定なら高いchemical potentialから低い側へ進みます。
5. phase transitionでGはどうなるか。
   **解答**：共存相のmolar Gibbs free energyが一致します。
6. Legendre変換は情報を捨てるか。
   **解答**：適切な凸性の下では同じ状態関係を自然変数を変えて表します。

## 限界・接続

熱力学はpotentialの形や実測値を使えますが、微視的Hamiltonianからその値を出すのは統計力学です。

- 前：[不可逆性](01_reversible_irreversible_and_entropy_generation.md)
- 次：[工学応用](03_engineering_energy_and_cooling.md)
- 関連：[Legendre横断](../../cross_connections/05_legendre_in_mechanics_and_thermodynamics.md)
