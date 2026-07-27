# 古典確率から密度演算子へ――可換な確率をどう拡張するか

## 古典確率を行列で書く

結果

$$
i=1,\ldots,n
$$

の確率を

$$
p_i\geq0,\qquad\sum_i p_i=1
$$

とします。対角行列

$$
\rho_{\mathrm{cl}}=\operatorname{diag}(p_1,\ldots,p_n)
$$

と値

$$
A_{\mathrm{cl}}=\operatorname{diag}(a_1,\ldots,a_n)
$$

を使えば

$$
\mathbb E[A]=\sum_i a_ip_i
=\operatorname{Tr}(\rho_{\mathrm{cl}}A_{\mathrm{cl}})
$$

です。同じ古典標本空間上の量は一つの基底で同時に対角化でき、互いに可換です。

## 量子状態の一般形式

有限次元量子論では、状態をdensity operator

$$
\rho\geq0,\qquad\operatorname{Tr}\rho=1
$$

で表します。正値性は任意のvector

$$
|v\rangle
$$

に対して

$$
\langle v|\rho|v\rangle\geq0
$$

を意味します。確率

$$
q,\ 1-q
$$

で二つの準備を選ぶと

$$
\rho=q\rho_1+(1-q)\rho_2
$$

です。したがって状態集合は凸集合です。

## 非可換性で増える情報

qubitをz基底で

$$
\rho=
\begin{pmatrix}
\rho_{00}&\rho_{01}\\
\rho_{10}&\rho_{11}
\end{pmatrix}
$$

と表すと、対角成分はz結果の確率、off-diagonal成分は別基底で観測できるcoherenceを担います。基底を替えれば対角・非対角の役割も変わります。density **operator**は基底に依らない対象、density **matrix**は選んだ基底での行列表現です。

## 再構成としての限界

「古典確率の可換性を外せば量子論になる」という見方は、標準形式の差を掴む有力な入口です。ただし、なぜ複素Hilbert空間、Born則、tensor productが自然界を記述するかを、この一操作だけから唯一導出したことにはなりません。

## 演習と全解答

1.
   $$
   \rho=\begin{pmatrix}0.7&0\\0&0.3\end{pmatrix}
   $$
   がdensity operatorか判定せよ。  
   **解答**：固有値は0.7, 0.3で非負、traceは1なので該当します。
2.
   $$
   \rho=\begin{pmatrix}1&0\\0&-0.1\end{pmatrix}
   $$
   はどうか。  
   **解答**：負固有値を持ち正値でないため該当しません。traceも0.9です。
3. 古典三値分布
   $$
   (1/2,1/3,1/6)
   $$
   のdensity matrixを書け。  
   **解答**：
   $$
   \operatorname{diag}(1/2,1/3,1/6)
   $$
4.
   $$
   A=\operatorname{diag}(1,4),\quad
   \rho=\operatorname{diag}(3/4,1/4)
   $$
   の期待値を求めよ。  
   **解答**：
   $$
   \operatorname{Tr}(\rho A)=3/4+1=7/4
   $$
5. density operatorとdensity matrixを区別せよ。  
   **解答**：前者はbasis非依存の線形演算子、後者は特定basisで並べた成分です。
6. 二つのdensity operatorの凸結合がtrace oneであることを示せ。  
   **解答**：
   $$
   \operatorname{Tr}[q\rho_1+(1-q)\rho_2]
   =q+(1-q)=1
   $$
   で、正値性も非負係数の和から保たれます。

## 参考・ナビゲーション

- 参考：[なぜ密度演算子が出てくるのか？（qm大学物理）](https://qmcharge.com/article-without-wavefunction)（確認日：2026-07-27。古典期待値のtrace表示という視点を検討。唯一の導出とは扱わない）
- 前：[状態準備](01_preparation_state_measurement.md)
- 次：[pureとmixed](03_pure_mixed_state_vector.md)

