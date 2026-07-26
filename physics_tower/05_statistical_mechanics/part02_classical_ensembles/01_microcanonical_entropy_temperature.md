# microcanonical ensemble・Boltzmann entropy・温度

## 孤立系の分布

energy、volume、particle numberを固定した孤立系

$$
(E,V,N)
$$

で、許されたenergy shell内のmicrostateを等確率とします。これがmicrocanonical ensembleです。

Boltzmann entropyは

$$
S(E,V,N)=k_B\ln\Omega(E,V,N)
$$

です。logを使うと独立系のmultiplicityの積がentropyの和になります。

$$
\Omega_{AB}=\Omega_A\Omega_B
$$

$$
S_{AB}=S_A+S_B
$$

## temperatureの微視的意味

$$
\frac1T=\left(\frac{\partial S}{\partial E}\right)_{V,N}
$$

です。二系がenergy

$$
\delta E
$$

を交換するとtotal entropy最大条件から

$$
\frac1{T_A}=\frac1{T_B}
$$

を得ます。

## pressureとchemical potential

fundamental relationとの比較から

$$
\frac pT=\left(\frac{\partial S}{\partial V}\right)_{E,N}
$$

$$
-\frac\mu T=\left(\frac{\partial S}{\partial N}\right)_{E,V}
$$

です。

## 演習と全解答

1. multiplicityを十倍にするとentropyはいくら増えるか。
   **解答**：
   $$
   \Delta S=k_B\ln10
   $$
2. 独立な同一系二つのentropyはどうなるか。
   **解答**：加法的に二倍です。
3. entropy最大はmultiplicity最大と同じか。
   **解答**：logは単調なので同じです。
4. 高温側は
   $$
   \partial S/\partial E
   $$
   が大きいか。
   **解答**：
   $$
   1/T
   $$
   なので小さいです。
5. 等確率原理はdynamicsから自明か。
   **解答**：基本仮定で、ergodicity・typicalityとの関係を吟味します。
6. phase spaceで状態数に単位問題がある理由は何か。
   **解答**：continuous volumeには単位があるため、量子scale
   $$
   h^{3N}
   $$
   などでcellを規格化します。

## ナビゲーション

- 前：[multiplicity](../part01_kinetic_theory/03_multiplicity_fluctuations_einstein_solid.md)
- 次：[canonical](02_canonical_boltzmann_partition.md)
- 親：[part02](README.md)
