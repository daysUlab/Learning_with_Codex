# 井戸・階段・障壁――境界条件が作る離散準位とtunnel

## 箱の中の粒子

無限深井戸

$$
V(x)=0\quad(0<x<L)
$$

外側で

$$
V=\infty
$$

とすると

$$
\psi(0)=\psi(L)=0
$$

です。解は

$$
\psi_n(x)=\sqrt{\frac2L}\sin\frac{n\pi x}{L}
$$

$$
E_n=\frac{n^2\pi^2\hbar^2}{2mL^2},\qquad n=1,2,\ldots
$$

です。古典粒子は任意の正energyを持てますが、量子では境界条件が波長を選びます。

## 有限井戸・階段・障壁

有限の不連続potentialでは、有限な

$$
V
$$

に対して

$$
\psi,\quad\frac{d\psi}{dx}
$$

を連続に接続します。有限井戸のbound stateは外側へ指数的tailを持ちます。

高さ

$$
V_0
$$

幅

$$
a
$$

の障壁で

$$
E<V_0
$$

でも透過はzeroではありません。厚い障壁なら

$$
T\sim e^{-2\kappa a},\qquad
\kappa=\frac{\sqrt{2m(V_0-E)}}{\hbar}
$$

です。これは粒子が障壁内で負の運動energyを持つ古典軌道を通る、という意味ではありません。

| 応用 | 障壁・tunnelの役割 |
|---|---|
| NAND | oxide障壁を越えるprogram・erase |
| STM | gap幅への指数感度で表面を読む |
| 核融合 | Coulomb障壁の透過 |

## 演習と全解答

1. 箱の幅を2倍にすると
   $$
   E_n
   $$
   はどうなるか。
   **解答**：
   $$
   E_n\propto L^{-2}
   $$
   なので1/4です。
2. 基底stateにnodeはいくつあるか。
   **解答**：井戸内部には0個です。
3.
   $$
   n=2
   $$
   のenergyは基底の何倍か。
   **解答**：4倍です。
4. 障壁幅を
   $$
   \Delta a
   $$
   増やした透過率比を近似せよ。
   **解答**：
   $$
   T'/T\simeq e^{-2\kappa\Delta a}
   $$
5. 有限potential stepで波動関数自体が不連続でよいか。
   **解答**：通常は不可です。Schrödinger式を微小区間で積分すると
   $$
   \psi
   $$
   と一次微分の連続性を得ます。
6. 古典的に許されない領域で検出確率がzeroでない例を二つ挙げよ。
   **解答**：有限井戸外のtailと有限障壁内・向こう側のtunnelです。

## ナビゲーション

- 前：[自由粒子](02_free_particle_wave_packets.md)
- 次：[調和振動子](04_harmonic_oscillator_four_views.md)
- 応用：[NAND](../../02_electromagnetism/part07_semiconductor_products/05_nand_flash_and_floating_gate_or_charge_trap.md)
