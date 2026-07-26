# 仮想変位・一般化力・Euler–Lagrange方程式

## 問い

拘束力を成分ごとに求めず、許された変位だけにNewton式を投影するにはどうすればよいでしょうか。

固定時刻で拘束と両立する仮想変位は

$$
\delta\mathbf r_a=\sum_i\frac{\partial\mathbf r_a}{\partial q_i}\delta q_i
$$

です。d'Alembert原理は

$$
\sum_a\left(\mathbf F_a-\dot{\mathbf p}_a\right)\cdot\delta\mathbf r_a=0
$$

と書けます。理想拘束の反力は仮想仕事をしないため消えます。一般化力

$$
Q_i=\sum_a\mathbf F_a\cdot\frac{\partial\mathbf r_a}{\partial q_i}
$$

を使うと

$$
\frac{d}{dt}\frac{\partial T}{\partial\dot q_i}-\frac{\partial T}{\partial q_i}=Q_i
$$

を得ます。保存力なら

$$
Q_i=-\frac{\partial V}{\partial q_i}
$$

なので

$$
\frac{d}{dt}\frac{\partial L}{\partial\dot q_i}-\frac{\partial L}{\partial q_i}=0,\qquad L=T-V
$$

です。

## 重力振り子

$$
T=\frac12ml^2\dot\theta^2,\qquad V=mgl(1-\cos\theta)
$$

より

$$
ml^2\ddot\theta+mgl\sin\theta=0
$$

張力は現れません。小角では

$$
\ddot\theta+\frac{g}{l}\theta=0
$$

となります。

## 検算

角度が無次元なので各項の次元はenergyです。微分後の式を

$$
ml
$$

で割れば加速度次元が揃います。

## 演習と全解答

1. 一般化力の次元は常にforceか。
   **解答**：いいえ。角座標ならtorque、一般には
   $$
   [Q_i\delta q_i]=\mathrm{J}
   $$
2. 自由粒子から何を得るか。
   **解答**：
   $$
   L=\frac12m\dot x^2\Rightarrow m\ddot x=0
   $$
3. ばねで式を導け。
   **解答**：
   $$
   L=\frac12m\dot x^2-\frac12kx^2\Rightarrow m\ddot x+kx=0
   $$
4. 振り子の張力が消える理由は何か。
   **解答**：許された仮想変位が接線方向で、張力が半径方向だからです。
5. 小角近似の条件は何か。
   **解答**：
   $$
   |\theta|\ll1,\qquad \sin\theta\simeq\theta
   $$
6. 摩擦力
   $$
   F=-b\dot x
   $$
   を加えよ。
   **解答**：一般化力を
   $$
   Q=-b\dot x
   $$
   として
   $$
   m\ddot x+b\dot x+kx=0
   $$

## 限界・ナビゲーション

理想拘束でない摩擦や衝撃には一般化力、非holonomic拘束、接触modelが必要です。

- 前：[自由度](../part01_supplements/02_degrees_of_freedom_and_coordinates.md)
- 次：[斜面と振り子](02_incline_and_pendulum_comparison.md)
- 親：[part02](README.md)

## 参考資料

Taylor, *Classical Mechanics*, Ch.7.
