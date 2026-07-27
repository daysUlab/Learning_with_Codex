# tensor product・同種粒子・Pauli原理

## 一粒子から多粒子へ

区別可能な二系のstate空間は

$$
\mathcal H_{AB}=\mathcal H_A\otimes\mathcal H_B
$$

です。各二準位ならdimensionは

$$
2\times2=4
$$

です。

同種粒子では粒子labelは観測可能な個体識別ではありません。交換演算子

$$
\hat P_{12}
$$

に対し

$$
\hat P_{12}|\Psi_B\rangle=+|\Psi_B\rangle
$$

がboson、

$$
\hat P_{12}|\Psi_F\rangle=-|\Psi_F\rangle
$$

がfermionです。

二つの一粒子state

$$
|a\rangle,\ |b\rangle
$$

から

$$
|\Psi_\pm\rangle=
\frac{|a\rangle|b\rangle\pm|b\rangle|a\rangle}
{\sqrt{2}}
$$

を作ります。fermionで

$$
a=b
$$

ならstateがzeroとなり、Pauli exclusionを得ます。

量子統計との役割分担は明確です。本ページは許される多粒子stateを定め、Fermi–Dirac・Bose–Einstein分布は熱平衡で各stateがどう占有されるかを定めます。

## 演習と全解答

1. 三つのqubitのstate空間次元を求めよ。
   **解答**：
   $$
   2^3=8
   $$
2. fermion二粒子を同じ一粒子stateへ入れたantisymmetric stateを計算せよ。
   **解答**：
   $$
   (|a,a\rangle-|a,a\rangle)/\sqrt2=0
   $$
3. bosonは一stateへ複数入れるか。
   **解答**：交換対称性は禁止しません。
4. electronを位置だけで同一stateか判定できるか。
   **解答**：できません。spinを含む全一粒子stateを比較します。
5. distinguishable particleでもtensor productは使うか。
   **解答**：使います。違いは交換対称化を課すかです。
6. Pauli原理からFermi分布を単独で導けるか。
   **解答**：energy、温度、chemical potential、熱平衡の最大entropy条件も必要です。

## ナビゲーション

- 前：[半導体](../part10_solid_state_semiconductors/README.md)
- 次：[exchangeとmean field](02_exchange_slater_mean_field.md)
- 統計正本：[Fermi・Bose](../../05_statistical_mechanics/part03_quantum_and_applications/01_classical_limit_fermi_bose.md)
