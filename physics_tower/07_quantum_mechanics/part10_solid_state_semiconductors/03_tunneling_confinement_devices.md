# tunnel・量子閉じ込め・半導体device

## 保留していた現象を回収する

| device・現象 | 量子概念 | 他章の正本 |
|---|---|---|
| gate oxide leakage | 障壁透過 | Poisson・電場は電磁気 |
| NAND program・erase | fieldで変形した障壁のtunnel | threshold・容量は電磁気 |
| quantum well | 境界条件とsubband | 占有は統計 |
| LED・solar cell | band間遷移・photon | pn電場・回路は電磁気 |
| nanoscale MOSFET | confinement・source-drain tunnel | electrostatics・transport |

厚さ

$$
a
$$

の障壁で

$$
T\sim e^{-2\kappa a}
$$

なので、1 nm級の寸法差でもleakageが桁違いになります。

閉じ込め長

$$
L
$$

では

$$
\Delta E\sim\frac{\hbar^2}{m^*L^2}
$$

です。薄膜・nanowire・quantum dotと閉じ込め次元を増やすと、連続bandからsubband・離散準位へ状態密度が変わります。

LEDではelectronとholeの再結合energyがphotonへ移りますが、直接・間接gap、selection rule、非放射再結合が効率を左右します。solar cellは逆向きにphoton吸収でcarrierを作り、内部電場で分離します。

## 演習と全解答

1. 障壁幅が2倍ならWKB透過率はどう変わるか。
   **解答**：
   $$
   T'/T=e^{-2\kappa a}
   $$
   だけさらに減少します。
2. well幅を半分にするとenergy scaleはどうなるか。
   **解答**：
   $$
   L^{-2}
   $$
   なので4倍です。
3. NAND tunnelを電磁気学だけで扱えない理由を述べよ。
   **解答**：電場は障壁形状を与えますが、
   $$
   E<V
   $$
   の透過確率には波動関数が必要です。
4. quantum confinementがband gapを実効的に変え得る理由を述べよ。
   **解答**：electron・holeの最低subband energyがbulk band端から押し上げ・押し下げられるためです。
5. LED photon energyをgapだけで厳密に決められるか。
   **解答**：概算は可能ですが、band dispersion、exciton、温度、phonon、欠陥も影響します。
6. 微細化が常に性能向上になるか。
   **解答**：短channel electrostatics、tunnel leakage、ばらつき、熱、接触抵抗が限界になります。

## ナビゲーション

- 前：[有効質量](02_effective_mass_electrons_holes.md)
- 次：[同種粒子](../part05_many_body/01_tensor_products_identical_particles.md)
- 電磁気正本：[MOSFET](../../02_electromagnetism/part06_semiconductor_bridge/README.md)
