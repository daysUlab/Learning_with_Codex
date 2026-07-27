# 量子力学で使う数学――止まった操作だけ直す

## 複素数と位相

$$
z=re^{i\theta},\qquad z^*=re^{-i\theta},\qquad |z|^2=z^*z
$$

です。全体phaseと相対phaseを区別します。

## vector・内積・Dirac記法

$$
\langle\phi|\psi\rangle
$$

はbraとketの内積、

$$
|\phi\rangle\langle\phi|
$$

は射影operatorです。braを単なる横vectorでなく、ketのcomplex conjugate transposeとして読みます。

## 固有値とHermitian

$$
A^\dagger=A,\qquad A|a\rangle=a|a\rangle
$$

です。unitaryは

$$
U^\dagger U=I
$$

で、Hermitianと役割が異なります。

## 確率と規格化

$$
\int|\psi|^2dx=1,\qquad
\langle x\rangle=\int x|\psi|^2dx
$$

$$
(\Delta x)^2=\langle x^2\rangle-\langle x\rangle^2
$$

です。amplitudeとprobabilityを取り違えません。

## 微分方程式と境界条件

二階空間微分の固有値問題では、方程式だけでなく連続性、壁、周期性、無限遠での減衰が固有値を選びます。

## Fourier変換

$$
\phi(p)=\frac1{\sqrt{2\pi\hbar}}\int e^{-ipx/\hbar}\psi(x)dx
$$

です。指数の符号と

$$
\hbar
$$

を章規約に合わせます。

## commutator

$$
[A,BC]=[A,B]C+B[A,C]
$$

を使うと高次式を展開できます。

## tensor product

$$
\begin{pmatrix}a\\b\end{pmatrix}
\otimes
\begin{pmatrix}c\\d\end{pmatrix}
=
\begin{pmatrix}ac\\ad\\bc\\bd\end{pmatrix}
$$

です。直和ではなくdimensionを掛けます。

## 演習と全解答

1.
   $$
   |1+i|^2
   $$
   を求めよ。
   **解答**：
   $$
   (1-i)(1+i)=2
   $$
2.
   $$
   A=\begin{pmatrix}1&i\\-i&2\end{pmatrix}
   $$
   はHermitianか。
   **解答**：はい。
3. 確率
   $$
   (1/4,1/4)
   $$
   の二成分stateは規格化済みか。
   **解答**：和が
   $$
   1/2
   $$
   なので未規格化です。
4.
   $$
   [x,p^3]
   $$
   を求めよ。
   **解答**：
   $$
   3i\hbar p^2
   $$
5. 二次元vectorと三次元vectorのtensor product次元を求めよ。
   **解答**：
   $$
   2\times3=6
   $$
6. 箱の固有値を微分方程式だけで決められない理由を述べよ。
   **解答**：境界条件が許される波長、従ってenergyを選ぶためです。

## ナビゲーション

- 親：[診断README](README.md)
- 章：[量子力学overview](../00_overview.md)
