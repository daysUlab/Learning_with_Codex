# 角運動量の合成・磁気モーメント・原子

## tensor product上の合成

二つの角運動量

$$
\mathbf J=\mathbf J_1+\mathbf J_2
$$

を合成すると

$$
j=|j_1-j_2|,\ |j_1-j_2|+1,\ldots,j_1+j_2
$$

です。二つのspin

$$
\frac12
$$

ではtriplet

$$
j=1
$$

とsinglet

$$
j=0
$$

に分かれます。

singletは

$$
|0,0\rangle=\frac{|+z,-z\rangle-|-z,+z\rangle}{\sqrt2}
$$

で、積stateへ分解できないentangled stateです。

## 磁気moment

軌道運動では

$$
\boldsymbol\mu_L=-\frac{e}{2m_e}\mathbf L
$$

spinでは

$$
\boldsymbol\mu_S=-g_s\frac{e}{2m_e}\mathbf S
$$

で

$$
g_s\simeq2
$$

です。外部磁場中のinteractionは

$$
\hat H_Z=-\boldsymbol\mu\cdot\mathbf B
$$

で、Zeeman splitting、NMR・MRI、原子時計、磁性へつながります。

原子では

$$
\mathbf J=\mathbf L+\mathbf S
$$

を用いますが、spin–orbit coupling、核spin、外場の強さによって適切なcoupling schemeが変わります。

## 演習と全解答

1.
   $$
   j_1=1,\quad j_2=1/2
   $$
   の合成
   $$
   j
   $$
   を求めよ。
   **解答**：
   $$
   j=3/2,\ 1/2
   $$
2. 二spinの全Hilbert空間次元を求めよ。
   **解答**：
   $$
   2\times2=4
   $$
3. triplet 3状態とsinglet 1状態で次元が一致することを確認せよ。
   **解答**：
   $$
   3+1=4
   $$
4. electron magnetic momentの符号が角運動量と逆になる理由を述べよ。
   **解答**：electron電荷が
   $$
   -e
   $$
   だからです。
5. 一様磁場でspin up/downのenergyが分かれる理由を式で示せ。
   **解答**：
   $$
   H_Z=-\mu_zB
   $$
   で
   $$
   S_z=\pm\hbar/2
   $$
   が異なるためです。
6. MRIを理解するのに必要な量子概念を三つ挙げよ。
   **解答**：核spin、磁気moment、Zeeman準位と共鳴遷移です。画像再構成にはさらに電磁気・signal処理が必要です。

## ナビゲーション

- 前：[spin](02_spin_half_and_pauli.md)
- 次：[水素原子](../part08_quantum_chemistry/01_hydrogen_atom_and_spectra.md)
- 後続：[entanglement](../part05_many_body/03_density_matrices_entanglement.md)
