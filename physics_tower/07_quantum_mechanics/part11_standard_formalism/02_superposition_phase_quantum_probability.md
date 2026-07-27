# 重ね合わせ・相対位相・量子確率

## 現代量子論から見ると

ここではpure stateのcoherent superpositionと、density operatorのconvex mixtureを区別します。off-diagonal成分はbasis依存ですが、そのbasisにおけるinterference可能性を担います。

## 二準位系で三つを区別する

| 記述 | state | Z測定 | X測定 |
|---|---|---|---|
| 古典的0/1確率混合 | $$\rho_{\rm mix}=I/2$$ | 各1/2 | 各1/2 |
| 量子重ね合わせ | $$|+\rangle=(|0\rangle+|1\rangle)/\sqrt2$$ | 各1/2 | +が1 |
| 位相を変えた重ね合わせ | $$|-\rangle=(|0\rangle-|1\rangle)/\sqrt2$$ | 各1/2 | -が1 |

Z測定だけでは三者を区別できません。量子stateは確率に加えて相対phaseを残します。

z基底では

$$
\rho_+=\frac12\begin{pmatrix}1&1\\1&1\end{pmatrix},
\qquad
\rho_{\rm mix}=\frac12\begin{pmatrix}1&0\\0&1\end{pmatrix}.
$$

対角成分は同じでも、coherent superpositionだけがoff-diagonal成分を持ち、x測定の干渉差を生みます。

一般のpure qubitは

$$
|\psi\rangle=\alpha|0\rangle+\beta|1\rangle,\qquad
|\alpha|^2+|\beta|^2=1
$$

です。全体phaseは消せますが

$$
\arg\beta-\arg\alpha
$$

は干渉結果を変えます。

## なぜ複素数が要るか

時間発展

$$
U(t)=e^{-i\hat Ht/\hbar}
$$

はnormを保つ連続回転です。実数だけでも一部のstateは書けますが、一般の位相回転・運動量・干渉を閉じた形で扱うには複素vector空間が自然です。

Hadamard変換

$$
H=\frac1{\sqrt2}
\begin{pmatrix}
1&1\\
1&-1
\end{pmatrix}
$$

を使うと

$$
H|+\rangle=|0\rangle,\qquad H|-\rangle=|1\rangle
$$

となり、相対phaseをpopulation差へ変換できます。

## 演習と全解答

1.
   $$
   |\psi\rangle=(|0\rangle+i|1\rangle)/\sqrt2
   $$
   のZ測定確率を求めよ。
   **解答**：両方
   $$
   1/2
   $$
   です。
2.
   $$
   (|0\rangle+2|1\rangle)
   $$
   を規格化せよ。
   **解答**：
   $$
   |\psi\rangle=\frac{|0\rangle+2|1\rangle}{\sqrt5}
   $$
3.
   $$
   |+\rangle
   $$
   と
   $$
   |-\rangle
   $$
   の内積を求めよ。
   **解答**：
   $$
   \langle+|-\rangle=0
   $$
4. global phase
   $$
   -1
   $$
   とrelative phase
   $$
   |0\rangle-|1\rangle
   $$
   の違いを述べよ。
   **解答**：全成分の共通符号は確率を変えませんが、一成分だけの符号は干渉を変えます。
5. 古典mixとsuperpositionをZ測定だけで区別できるか。
   **解答**：できません。Xなど別basisの測定が必要です。
6. 「qubitは0と1の中間値」という説明の問題を述べよ。
   **解答**：振幅とphaseを持つstateであり、測定basisごとに離散結果の確率を与えるので、数値0.5とは異なります。

## ナビゲーション

- 前：[状態とBorn則](01_state_wavefunction_born.md)
- 次：[Hilbert空間と演算子](03_hilbert_operators_eigenvalues.md)
- Logic正本：[qubitは三値bitではない](../../../logic_tower/90_essays/quantum_computing_and_logic/03_qubits_are_not_three_valued_bits.md)
