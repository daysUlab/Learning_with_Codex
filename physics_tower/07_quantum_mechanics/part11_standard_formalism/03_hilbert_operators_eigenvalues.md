# Hilbert空間・bra-ket・観測量

## stateとbasis

Hilbert空間は内積を持つ完備な複素vector空間です。有限次元では

$$
|\psi\rangle=\sum_n c_n|n\rangle,\qquad
c_n=\langle n|\psi\rangle
$$

です。basisを替えてもstateは同じで、成分だけが変わります。

## 現代量子論から見ると

一般測定はPOVM、sharpな測定はPVM、実数labelを付けたPVMがself-adjoint operatorです。ここではideal PVMへ限定します。装置のnoiseやpost-measurement stateまで一個の演算子が表すわけではありません。

## PVMとself-adjoint演算子

$$
\hat A^\dagger=\hat A
$$

なら固有値は実数で、異なる固有値の固有stateは直交します。

$$
\hat A|a_n\rangle=a_n|a_n\rangle
$$

理想PVMでは

$$
P(a_n)=|\langle a_n|\psi\rangle|^2
$$

です。期待値は「一回で得る値」ではなく、同じ準備を多数回測った平均です。

$$
\langle\hat A\rangle=\langle\psi|\hat A|\psi\rangle
$$

例として

$$
\hat A=
\begin{pmatrix}
1&i\\
-i&2
\end{pmatrix}
$$

はoff-diagonal成分が複素共役なのでHermitianです。

## 固有展開と完全性

離散・非縮退の場合

$$
\hat A=\sum_na_n|a_n\rangle\langle a_n|,\qquad
\sum_n|a_n\rangle\langle a_n|=\hat I
$$

です。縮退があれば同じ固有値の部分空間へ射影します。

## 演習と全解答

1.
   $$
   \begin{pmatrix}0&1\\1&0\end{pmatrix}
   $$
   がHermitianであることを確認せよ。
   **解答**：転置複素共役を取っても同じ行列です。
2. 上の行列の固有値を求めよ。
   **解答**：
   $$
   \det(\hat A-\lambda I)=\lambda^2-1=0
   $$
   より
   $$
   \lambda=\pm1
   $$
3.
   $$
   |0\rangle
   $$
   でPauli Xを測る確率を求めよ。
   **解答**：
   $$
   |0\rangle=(|+\rangle+|-\rangle)/\sqrt2
   $$
   なので各
   $$
   1/2
   $$
4. 一般のPOVMを一つのHermitian演算子で完全に表せるか。
   **解答**：一般にはできません。自己共役演算子は実数label付きPVMに対応し、unsharpなPOVMやstate updateは追加構造を要します。
5. basis変換で物理stateは変わるか。
   **解答**：受動的basis変更なら変わらず、成分と演算子表示が整合して変わります。
6. 縮退固有値を測ると一意のvectorへ必ず更新されるか。
   **解答**：理想的な粗い測定では対応する縮退部分空間への射影までしか定まりません。

## ナビゲーション

- 前：[重ね合わせ](02_superposition_phase_quantum_probability.md)
- 次：[不確定性とFourier](04_commutators_uncertainty_fourier.md)
- 補習：[線形代数](../../00_physics_math_tools/linear_algebra/README.md)
