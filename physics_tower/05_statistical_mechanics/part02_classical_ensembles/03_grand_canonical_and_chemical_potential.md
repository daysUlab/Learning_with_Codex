# grand canonical ensembleとchemical potential

## 熱と粒子を交換する系

温度

$$
T
$$

chemical potential

$$
\mu
$$

volume

$$
V
$$

を固定し、energyとparticle numberが揺らぐ系を扱います。microstate

$$
(i,N)
$$

の重みは

$$
P_{i,N}=\frac{e^{-\beta(E_{i,N}-\mu N)}}{\Xi}
$$

grand partition functionは

$$
\Xi=\sum_N\sum_i e^{-\beta(E_{i,N}-\mu N)}
$$

です。

grand potential

$$
\Phi_G=-k_BT\ln\Xi
$$

から

$$
\langle N\rangle=\frac1\beta\frac{\partial\ln\Xi}{\partial\mu}
$$

を得ます。

## chemical potentialの意味

粒子数を増やす自由energy costで、particle flowとreaction equilibriumを制御します。semiconductorでは平衡electronのchemical potentialがFermi levelです。

## 一状態のfermion予告

占有数

$$
n=0,1
$$

だけなら

$$
\Xi_\varepsilon=1+e^{-\beta(\varepsilon-\mu)}
$$

平均占有は

$$
\langle n\rangle=\frac1{e^{\beta(\varepsilon-\mu)}+1}
$$

です。

## 演習と全解答

1. grand canonicalで固定する三量は何か。
   **解答**：
   $$
   T,V,\mu
   $$
2.
   $$
   \mu
   $$
   が大きいとparticleは増えやすいか。
   **解答**：重み
   $$
   e^{\beta\mu N}
   $$
   が大きくなり増えやすいです。
3. Nは一定か。
   **解答**：揺らぎます。
4. semiconductorのFermi levelは何に対応するか。
   **解答**：electronのchemical potentialです。
5. photon numberに通常chemical potentialを置くか。
   **解答**：平衡blackbody radiationではphotonが生成消滅できるため
   $$
   \mu=0
   $$
6. subsystemが大きくてもensembleは使えるか。
   **解答**：reservoirが十分大きくintensive変数を固定できる近似が必要です。

## ナビゲーション

- 前：[canonical](02_canonical_boltzmann_partition.md)
- 次：[古典例](04_classical_examples_and_equipartition.md)
- 親：[part02](README.md)
