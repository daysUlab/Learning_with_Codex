# pure state・mixed state・状態vector――一般状態の中の特殊な境界

## pure state

density operatorがrank oneなら

$$
\rho=|\psi\rangle\langle\psi|
$$

と書けます。これをpure stateと呼びます。

$$
\rho^2=\rho,\qquad
\operatorname{Tr}\rho^2=1
$$

が成り立ちます。状態vector

$$
|\psi\rangle
$$

と

$$
e^{i\chi}|\psi\rangle
$$

は同じprojectorを作るため、物理状態はvectorそのものよりrayに対応します。

## mixed state

一般の状態はspectral decomposition

$$
\rho=\sum_k\lambda_k|k\rangle\langle k|,
\qquad \lambda_k\geq0,\quad\sum_k\lambda_k=1
$$

を持ちます。rankが2以上ならmixed stateで、

$$
\operatorname{Tr}\rho^2<1
$$

です。ただしpurityだけで混合の原因は分かりません。

同じ

$$
\rho=\frac12I
$$

は、z基底の0/1を半々で準備しても、x基底の+/−を半々で準備しても得られます。ensemble分解は一意ではなく、density operatorが同じなら系単独の測定では区別できません。

## superpositionとmixture

$$
|+\rangle=\frac{|0\rangle+|1\rangle}{\sqrt2}
$$

では

$$
\rho_+=\frac12
\begin{pmatrix}
1&1\\
1&1
\end{pmatrix}
$$

です。一方、0/1のincoherent mixtureは

$$
\rho_{\mathrm{mix}}=\frac12
\begin{pmatrix}
1&0\\
0&1
\end{pmatrix}.
$$

z測定は同じ統計ですが、x測定では前者が `+` を確率1、後者が `+`/`-` を各1/2で返します。off-diagonal成分は選んだbasisにおける干渉可能性を表します。

## reduced stateへの入口

全体系がpureでも、環境や相手系を捨てたreduced stateはmixedになり得ます。これは単に「どのpure stateか知らない」という古典的無知だけではなく、entanglementから生じる場合があります。

## 演習と全解答

1.
   $$
   \rho=\begin{pmatrix}1&0\\0&0\end{pmatrix}
   $$
   のrankとpurityを求めよ。  
   **解答**：rank 1、
   $$
   \operatorname{Tr}\rho^2=1
   $$
   なのでpureです。
2.
   $$
   \rho=I/2
   $$
   のpurityを求めよ。  
   **解答**：
   $$
   \operatorname{Tr}(I/4)=1/2
   $$
3.
   $$
   |-\rangle=(|0\rangle-|1\rangle)/\sqrt2
   $$
   のdensity matrixを書け。  
   **解答**：
   $$
   \rho_-=\frac12
   \begin{pmatrix}1&-1\\-1&1\end{pmatrix}
   $$
4. 0/1の半々mixと+/−の半々mixが同じことを示せ。  
   **解答**：
   $$
   \frac12(|+\rangle\langle+|+|-\rangle\langle-|)
   =\frac12I
   $$
   で、off-diagonal成分が相殺します。
5. pure superpositionとmixed stateを同義にできない理由を述べよ。  
   **解答**：superpositionはrank-one projectorでcoherenceを持ち、mixed stateは一般にrankが大きく、別basisの干渉統計が異なります。
6. global phaseがdensity operatorから消えることを示せ。  
   **解答**：
   $$
   e^{i\chi}|\psi\rangle\langle\psi|e^{-i\chi}
   =|\psi\rangle\langle\psi|
   $$

## 参考・ナビゲーション

- 参考：[波動関数とは何か？純粋状態と混合状態（qm大学物理）](https://qmcharge.com/article-wavefunction-pure-mixed)（確認日：2026-07-27）
- 前：[密度演算子](02_classical_probability_density_operator.md)
- 次：[POVM](04_generalized_born_povm.md)

