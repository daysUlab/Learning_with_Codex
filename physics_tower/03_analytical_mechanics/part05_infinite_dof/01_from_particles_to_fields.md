# 粒子から連続体・場へ

## 問い

有限個の座標を、各空間点に値を持つfieldへどう一般化するでしょうか。

弦の横変位

$$
\phi(x,t)
$$

を考えます。線密度

$$
\mu
$$

張力

$$
\mathcal T
$$

ならLagrangian densityは

$$
\mathcal L=\frac12\mu(\partial_t\phi)^2-\frac12\mathcal T(\partial_x\phi)^2
$$

作用は

$$
S[\phi]=\int dt\int dx\,\mathcal L
$$

です。fieldを変分して時間・空間で部分積分すると

$$
\frac{\partial\mathcal L}{\partial\phi}
-\partial_t\frac{\partial\mathcal L}{\partial(\partial_t\phi)}
-\partial_x\frac{\partial\mathcal L}{\partial(\partial_x\phi)}=0
$$

したがって

$$
\mu\partial_t^2\phi-\mathcal T\partial_x^2\phi=0
$$

を得ます。波速は

$$
c=\sqrt{\frac{\mathcal T}{\mu}}
$$

です。

## 何が変わり、何が残るか

座標indexが連続な空間点へ変わりますが、作用、境界項、対称性、Noetherの構造は残ります。電磁場、相対論、場の量子論へ一般化できます。

## 演習と全解答

1.
   $$
   [\mathcal T/\mu]
   $$
   を調べよ。
   **解答**：
   $$
   \mathrm{m^2/s^2}
   $$
   なので平方根は速度です。
2. 空間一様な変位では弾性energyはどうなるか。
   **解答**：
   $$
   \partial_x\phi=0
   $$
   なのでゼロです。
3. 固定端条件を書け。
   **解答**：
   $$
   \phi(0,t)=\phi(L,t)=0
   $$
4. plane waveを代入せよ。
   **解答**：
   $$
   \phi=Ae^{i(kx-\omega t)},\qquad\omega^2=c^2k^2
   $$
5. fieldの自由度は有限か。
   **解答**：連続modelでは無限です。格子化すると有限になります。
6. 離散ばね鎖との関係は何か。
   **解答**：格子間隔より十分長い波長で連続弦modelへ近づきます。

## 限界・ナビゲーション

原子scaleではcontinuum近似が破綻します。量子化は本ページの範囲外です。

- 前：[phase space](../part04_gateway_to_qm/02_phase_space_and_poisson_brackets.md)
- 次：[荷電粒子](../part06_canonical_em/01_charged_particle_and_gauge.md)
- 親：[part05](README.md)
