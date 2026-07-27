# 基底・行列・unitary時間発展・三つの表示

## 演算子を行列で見る

orthonormal basis

$$
\{|n\rangle\}
$$

を選ぶと

$$
A_{mn}=\langle m|\hat A|n\rangle
$$

です。basis変更

$$
|n'\rangle=\hat U|n\rangle
$$

では、受動的表示として

$$
A'=U^\dagger AU
$$

となります。固有値や期待値は変わりません。

## 時間発展演算子

時間非依存Hamiltonianなら

$$
\hat U(t)=e^{-i\hat Ht/\hbar}
$$

です。

$$
\hat U^\dagger\hat U=\hat I
$$

なのでinner productと確率を保存します。

## Schrödinger・Heisenberg・相互作用表示

| 表示 | state | operator |
|---|---|---|
| Schrödinger | 時間発展 | 原則固定 |
| Heisenberg | 固定 | 時間発展 |
| interaction | 一部をfree発展へ分離 | 摂動interactionが発展 |

Heisenberg表示では

$$
\frac{d\hat A_H}{dt}
=\frac{i}{\hbar}[\hat H,\hat A_H]
+\left(\frac{\partial\hat A}{\partial t}\right)_H
$$

です。解析力学の

$$
\frac{dA}{dt}=\{A,H\}+\frac{\partial A}{\partial t}
$$

と構造を比較できます。

## 演習と全解答

1. 対角Hamiltonian
   $$
   H=\operatorname{diag}(E_1,E_2)
   $$
   の
   $$
   U(t)
   $$
   を書け。
   **解答**：
   $$
   U=\operatorname{diag}(e^{-iE_1t/\hbar},e^{-iE_2t/\hbar})
   $$
2.
   $$
   U^\dagger U=I
   $$
   がnorm保存を意味することを示せ。
   **解答**：
   $$
   \langle\psi(t)|\psi(t)\rangle
   =\langle\psi(0)|U^\dagger U|\psi(0)\rangle=1
   $$
3. energy固有stateは物理的に全く変化しないか。
   **解答**：単独ならglobal phaseだけですが、他energyとの重ね合わせでは相対phaseが観測可能です。
4. basis変更と実際のgate操作を区別せよ。
   **解答**：前者は同じstateの座標表示変更、後者は固定したbasisに対してstateを能動的に変えます。
5. Heisenberg式で
   $$
   [H,A]=0
   $$
   かつ陽な時間依存なしなら何が言えるか。
   **解答**：
   $$
   dA_H/dt=0
   $$
   で保存observableです。
6. interaction表示を使う主目的を述べよ。
   **解答**：解けるfree発展を分離し、残るinteractionを摂動展開しやすくすることです。

## ナビゲーション

- 前：[Schrödinger基本問題](../part09_schrodinger_dynamics/README.md)
- 次：[正準量子化](02_poisson_commutator_quantization.md)
- 古典正本：[phase space](../../03_analytical_mechanics/part04_gateway_to_qm/02_phase_space_and_poisson_brackets.md)
