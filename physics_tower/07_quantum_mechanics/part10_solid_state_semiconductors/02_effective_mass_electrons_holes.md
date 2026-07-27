# 有効質量・electron・hole・doping

## 現代量子論から見ると

band eigenstateをwave packetへ組み、semiclassical dynamicsへ縮約します。carrier populationはmixed ensemble、phonon・impurity散乱はunitaryな一電子Schrödinger発展だけでは閉じません。

## band内の運動

semiclassical wave packetでは

$$
\mathbf v_n(\mathbf k)=\frac1\hbar\nabla_{\mathbf k}E_n(\mathbf k)
$$

です。band端近傍を

$$
E(k)\simeq E_0+\frac{\hbar^2(k-k_0)^2}{2m^*}
$$

と近似し、

$$
\frac1{m^*}=\frac1{\hbar^2}\frac{d^2E}{dk^2}
$$

と定義します。有効質量は真空electronの質量変更ではなく、結晶中のdispersion曲率を運動方程式へ圧縮したparameterです。一般にはtensorです。

ほぼ満杯のvalence bandでは、全electronを追う代わりに欠けたstateを正電荷

$$
+e
$$

のholeとして記述します。

dopingはdonor・acceptor由来のstateとcarrier数を変えます。bandそのもの、dopant準位、ionization energyは量子構造、占有率・Fermi level・濃度は[統計力学](../../05_statistical_mechanics/part03_quantum_and_applications/02_semiconductor_carriers_and_einstein_relation.md)です。

## 演習と全解答

1. 放物線bandで曲率が大きいと
   $$
   m^*
   $$
   はどうなるか。
   **解答**：
   $$
   m^*
   $$
   は小さくなります。
2. flat bandのgroup velocityを述べよ。
   **解答**：
   $$
   \nabla_kE\simeq0
   $$
   なので小さいです。
3. holeの正電荷は陽電子を意味するか。
   **解答**：いいえ。valence bandの欠損を有効準粒子として表します。
4. 有効質量が負になるband曲率をどう扱うか。
   **解答**：満杯band近傍の欠損を正のhole質量として再記述できます。
5. dopingをPoisson方程式だけで説明できるか。
   **解答**：空間電位は扱えますが、dopant stateとionization・占有には量子・統計が必要です。
6. carrier mobilityが有効質量だけで決まるか。
   **解答**：散乱時間、phonon、impurity、温度、band anisotropyも必要です。

## ナビゲーション

- 前：[Blochとband](01_periodic_potentials_bloch_bands.md)
- 次：[tunnelと閉じ込め](03_tunneling_confinement_devices.md)
- 統計正本：[半導体carrier](../../05_statistical_mechanics/part03_quantum_and_applications/02_semiconductor_carriers_and_einstein_relation.md)
