# 気体分子運動論：粒子運動から圧力と温度へ

## 問いとmodel

希薄な同一粒子を点粒子、衝突を弾性、壁を固定と近似し、粒子のmomentum移送から圧力を導きます。分子間相互作用と内部自由度は最初は省略します。

一辺

$$
L
$$

の箱で、粒子一個がx壁へ衝突するたびmomentum変化は

$$
\Delta p_x=2mv_x
$$

同じ壁への衝突間隔は

$$
\Delta t=\frac{2L}{|v_x|}
$$

なので平均forceは

$$
F_x=\frac{mv_x^2}{L}
$$

です。N粒子を足し、isotropy

$$
\langle v_x^2\rangle=\frac13\langle v^2\rangle
$$

を使うと

$$
pV=\frac13Nm\langle v^2\rangle
$$

理想気体式と比較して

$$
\frac12m\langle v^2\rangle=\frac32k_BT
$$

を得ます。温度は平均並進kinetic energyの尺度です。

## 数値例

窒素分子の質量を

$$
m=4.65\times10^{-26}\ \mathrm{kg}
$$

とすると300 Kのroot-mean-square speedは

$$
v_{\mathrm{rms}}=\sqrt{\frac{3k_BT}{m}}\simeq517\ \mathrm{m/s}
$$

です。

## 演習と全解答

1. 粒子数を二倍、VとT一定にするとpはどうなるか。
   **解答**：二倍です。
2. temperatureを四倍にするとrms speedはどうなるか。
   **解答**：平方根依存なので二倍です。
3. 同温度で重い分子は遅いか。
   **解答**：
   $$
   v_{\mathrm{rms}}\propto m^{-1/2}
   $$
   なので遅いです。
4. 平均velocityがゼロでもpressureがある理由は何か。
   **解答**：
   $$
   \langle v_x\rangle=0
   $$
   でも
   $$
   \langle v_x^2\rangle>0
   $$
   だからです。
5. dense gasで何が破れるか。
   **解答**：粒子体積と相互作用を無視できません。
6. pressureの単位を検算せよ。
   **解答**：
   $$
   \frac{Nm\langle v^2\rangle}{V}
   \sim\frac{\mathrm{J}}{\mathrm{m^3}}=\mathrm{Pa}
   $$

## 限界・ナビゲーション

平衡分布の形、揺らぎ、量子同種粒子は未説明です。

- 前：[章overview](../00_overview.md)
- 次：[microstateと数え上げ](02_microstate_macrostate_small_counting.md)
- 親：[part01](README.md)
