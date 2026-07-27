# Schrödinger方程式・Hamiltonian・確率保存

## 現代量子論から見ると

このページはpure state、孤立した閉鎖系、連続的で可逆なunitary発展へ限定します。一般のopen-system stateはCPTP channelで変化し、system単独ではSchrödinger方程式に従うとは限りません。

## 時間発展の中心式

非相対論的一粒子で

$$
\hat H=-\frac{\hbar^2}{2m}\nabla^2+V(\mathbf r,t)
$$

とすると

$$
i\hbar\frac{\partial\psi}{\partial t}=\hat H\psi
$$

です。Hamiltonianはenergy observableであると同時に、時間並進の生成子です。初期波動関数とHamiltonianを与えれば、閉じた系のstateを予測します。

時間非依存potentialでは

$$
\psi(\mathbf r,t)=\phi(\mathbf r)e^{-iEt/\hbar}
$$

を代入して

$$
\hat H\phi=E\phi
$$

を得ます。定常stateの確率密度は時間に依存しませんが、state vectorのphaseは回転します。

## 連続の式

Schrödinger式と複素共役式から

$$
\frac{\partial}{\partial t}|\psi|^2+\nabla\cdot\mathbf j=0
$$

$$
\mathbf j=\frac{\hbar}{2mi}
\left(\psi^*\nabla\psi-\psi\nabla\psi^*\right)
$$

を得ます。境界でfluxが消えるか、無限遠で波動関数が十分減衰すれば全確率は保存されます。符号は時間発展

$$
e^{-iEt/\hbar}
$$

と整合します。

## 適用範囲

potentialは外場または有効相互作用として与えます。測定はinstrument、散逸したopen systemはchannel、光の生成消滅は量子場という別modelが必要です。

## 演習と全解答

1.
   $$
   [\hbar\partial_t]
   $$
   の次元を確認せよ。
   **解答**：
   $$
   \mathrm{J\,s}\times\mathrm{s^{-1}}=\mathrm J
   $$
   でHamiltonianと一致します。
2. energy固有stateの確率密度が一定であることを示せ。
   **解答**：
   $$
   |\phi e^{-iEt/\hbar}|^2=|\phi|^2
   $$
3. 異なるenergyの重ね合わせの確率密度は必ず一定か。
   **解答**：相対phase
   $$
   e^{-i(E_m-E_n)t/\hbar}
   $$
   の干渉項があるため一般に変化します。
4. 実数の定常波動関数でcurrentを求めよ。
   **解答**：
   $$
   \mathbf j=0
   $$
5. 非Hermitian Hamiltonianでnorm保存が破れる可能性を説明せよ。
   **解答**：時間発展がunitaryでなくなり、source・sinkを含む有効modelになるためです。
6. 連続の式で
   $$
   \nabla\cdot\mathbf j<0
   $$
   の点は何を意味するか。
   **解答**：その近傍へ確率が流入し、確率密度が増加することを意味します。

## ナビゲーション

- 前：[測定](../part11_standard_formalism/05_measurement_decoherence_interpretations.md)
- 次：[自由粒子](02_free_particle_wave_packets.md)
- 解析力学：[Hamiltonian](../../03_analytical_mechanics/part04_gateway_to_qm/01_legendre_transform_and_hamiltonian.md)
