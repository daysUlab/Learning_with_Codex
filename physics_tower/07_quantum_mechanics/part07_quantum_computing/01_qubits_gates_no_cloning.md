# qubit・Bloch sphere・gate・no-cloning

## qubitは三値bitではない

$$
|\psi\rangle=
\cos\frac\theta2|0\rangle+
e^{i\varphi}\sin\frac\theta2|1\rangle
$$

はpure qubitのBloch sphere表示です。sphereはstate空間の座標で、物理空間内の小さな矢印とは限りません。

代表gateは

$$
X=\begin{pmatrix}0&1\\1&0\end{pmatrix},\quad
Z=\begin{pmatrix}1&0\\0&-1\end{pmatrix},\quad
H=\frac1{\sqrt2}\begin{pmatrix}1&1\\1&-1\end{pmatrix}
$$

です。unitary gateは未知stateを壊さずコピーする操作ではありません。

## no-cloning

任意の

$$
|\psi\rangle
$$

を複製するunitaryがあると仮定し、

$$
U|0\rangle|b\rangle=|0\rangle|0\rangle
$$

$$
U|1\rangle|b\rangle=|1\rangle|1\rangle
$$

とします。線形性から

$$
U(\alpha|0\rangle+\beta|1\rangle)|b\rangle
=\alpha|00\rangle+\beta|11\rangle
$$

ですが、複製state

$$
(\alpha|0\rangle+\beta|1\rangle)^{\otimes2}
$$

とは一般に異なります。

## 演習と全解答

1.
   $$
   H|0\rangle
   $$
   を求めよ。
   **解答**：
   $$
   |+\rangle
   $$
2.
   $$
   Z|+\rangle
   $$
   を求めよ。
   **解答**：
   $$
   |-\rangle
   $$
3. qubit測定で中間値0.3が直接出るか。
   **解答**：計算basis測定なら0か1が出て、0.3は確率や期待値として現れます。
4. 既知の直交state集合はcopyできるか。
   **解答**：basis stateを識別してcopyするunitaryは作れます。禁止されるのは任意の未知stateの完全copyです。
5. no-cloningの根本にある性質を述べよ。
   **解答**：量子操作の線形性とinner product保存です。
6. Bloch sphere内部の点は何を表すか。
   **解答**：一般にはmixed qubit stateです。

## ナビゲーション

- 前：[density matrix](../part05_many_body/03_density_matrices_entanglement.md)
- 次：[Bellとalgorithm](02_entanglement_bell_algorithms.md)
- Logic正本：[量子gate](../../../logic_tower/90_essays/quantum_computing_and_logic/04_quantum_gates_as_linear_transformations.md)
