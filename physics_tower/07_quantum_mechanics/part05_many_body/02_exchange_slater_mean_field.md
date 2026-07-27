# exchange・Slater行列式・mean field

## 多fermion state

orthonormalな一粒子軌道

$$
\phi_1,\ldots,\phi_N
$$

から

$$
\Psi(x_1,\ldots,x_N)=\frac1{\sqrt{N!}}
\begin{vmatrix}
\phi_1(x_1)&\cdots&\phi_N(x_1)\\
\vdots&\ddots&\vdots\\
\phi_1(x_N)&\cdots&\phi_N(x_N)
\end{vmatrix}
$$

を作ります。二行交換で符号反転し、同じorbitalが二列ならdeterminantはzeroです。

antisymmetryにより、Coulomb相互作用の期待値にdirect termに加えてexchange termが現れます。これは未知の古典力を追加したものではなく、stateの交換対称性の効果です。

## many-body problem

粒子数

$$
N
$$

に対してconfiguration space dimensionとbasis sizeが急増します。Hartree–Fockは各electronが他electronの平均場を感じるself-consistent modelで、一つのSlater determinantまで圧縮します。

mean fieldは独立粒子像を回復しますが、強相関、entanglement、量子揺らぎを落とします。phonon、magnon、quasiparticleは多数の自由度を低energyの有効励起へ再記述する次のmodelです。

## 演習と全解答

1. Slater determinantの二粒子交換で何が起こるか。
   **解答**：行を交換するので全体符号が反転します。
2. 同じorbitalを二列に入れるとどうなるか。
   **解答**：determinantはzeroです。
3. exchange energyは古典Coulomb energyと同一か。
   **解答**：異なります。波動関数のantisymmetryから生じます。
4. Hartree–Fockが含む相関と落とす相関を述べよ。
   **解答**：exchangeは含み、単一determinantを越える動的correlationは落とします。
5. self-consistentとは何か。
   **解答**：仮の軌道から平均場を作り、その場の固有軌道で更新し、収束まで反復します。
6. many-body problemが単にCPU不足だけの問題でない理由を述べよ。
   **解答**：Hilbert空間が指数的に増え、どの相関を残す有効modelが妥当かという物理的選択が必要だからです。

## ナビゲーション

- 前：[同種粒子](01_tensor_products_identical_particles.md)
- 次：[density matrix](03_density_matrices_entanglement.md)
- 化学：[量子化学の近似](../part08_quantum_chemistry/03_many_electron_quantum_chemistry.md)
