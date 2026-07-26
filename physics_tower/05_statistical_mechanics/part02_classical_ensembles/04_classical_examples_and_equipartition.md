# 古典具体例・等分配・classical molecular dynamics

## 等分配則

classical canonical ensembleでHamiltonianに二次形式で現れる独立な項一つは平均

$$
\frac12k_BT
$$

を持ちます。三次元単原子理想気体では

$$
U=\frac32Nk_BT,\qquad C_V=\frac32Nk_B
$$

です。一次元調和振動子はkineticとpotentialの二項があるので

$$
\langle E\rangle=k_BT
$$

です。

## Maxwell speed distribution

$$
f(v)=4\pi\left(\frac{m}{2\pi k_BT}\right)^{3/2}
v^2e^{-mv^2/(2k_BT)}
$$

です。state countの

$$
v^2
$$

とBoltzmann weightの競合で最頻speedが有限になります。

## classical molecular dynamics

Newton/Hamilton方程式を数値積分し、time averageから巨視量を推定します。potential model、finite size、time step、equilibration、ergodicityを検査します。

## 古典統計の破綻

低温では振動・回転自由度が量子化され、等分配が過大評価します。紫外破綻、solid低温比熱、electron gasが代表例です。

## 演習と全解答

1. 単原子気体一粒子の平均並進energyは何か。
   **解答**：
   $$
   \frac32k_BT
   $$
2. 一次元oscillatorの平均potential energyは何か。
   **解答**：
   $$
   \frac12k_BT
   $$
3. N粒子単原子気体の
   $$
   C_V
   $$
   は何か。
   **解答**：
   $$
   \frac32Nk_B
   $$
4. 等分配は全温度で正しいか。
   **解答**：いいえ。energy level間隔よりtemperature energyが小さいと量子効果が重要です。
5. MDでtrajectory一本とensemble平均を同一視する条件は何か。
   **解答**：十分なsamplingとergodicityの仮定を検証します。
6. time stepが大きすぎる兆候は何か。
   **解答**：energy drift、unstable軌道、fast vibrationを解像できないことです。

## ナビゲーション

- 前：[grand canonical](03_grand_canonical_and_chemical_potential.md)
- 次：[量子統計](../part03_quantum_and_applications/01_classical_limit_fermi_bose.md)
- 親：[part02](README.md)
