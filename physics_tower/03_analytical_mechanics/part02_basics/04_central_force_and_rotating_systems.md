# 比較例題：中心力・惑星運動・回転する輪上のbead

## 中心力

平面極座標で

$$
L=\frac12m\left(\dot r^2+r^2\dot\phi^2\right)-V(r)
$$

です。角度

$$
\phi
$$

がLに現れないので

$$
p_\phi=mr^2\dot\phi=\ell
$$

が保存されます。radial motionは

$$
m\ddot r=-\frac{dV_{\mathrm{eff}}}{dr},\qquad
V_{\mathrm{eff}}=V(r)+\frac{\ell^2}{2mr^2}
$$

へ還元されます。Newtonのvector式と同じですが、回転対称性と角運動量保存が座標から直ちに見えます。

重力

$$
V(r)=-\frac{GMm}{r}
$$

では円軌道条件

$$
\frac{GMm}{r^2}=\frac{\ell^2}{mr^3}
$$

を得ます。

## 回転する輪上のbead

鉛直軸まわりに角速度

$$
\Omega
$$

で回る半径

$$
R
$$

の輪上で、最低点から角度

$$
\theta
$$

を取ります。

$$
L=\frac12mR^2\left(\dot\theta^2+\Omega^2\sin^2\theta\right)-mgR(1-\cos\theta)
$$

よって

$$
\ddot\theta=\sin\theta\left(\Omega^2\cos\theta-\frac gR\right)
$$

です。回転座標で遠心力を個別に入れるより、inertial frameのkinetic energyから一式で出せます。

## 演習と全解答

1. 中心力で保存されるvector量は何か。
   **解答**：角運動量です。
2. 面積速度を示せ。
   **解答**：
   $$
   \frac{dA}{dt}=\frac12r^2\dot\phi=\frac{\ell}{2m}
   $$
3. 有効potentialの遠心項はどこで大きいか。
   **解答**：
   $$
   r\to0
   $$
   で発散します。
4. 円軌道の速さを求めよ。
   **解答**：
   $$
   v=\sqrt{\frac{GM}{r}}
   $$
5. beadで最低点が不安定化する条件を求めよ。
   **解答**：小角展開から
   $$
   \Omega^2>\frac gR
   $$
6. 回転系でenergyは保存するか。
   **解答**：外部駆動が一定角速度を保つため、全装置を含めないbead単独のmechanical energyは一般に保存しません。ただし時間非依存の有効Lagrangianに対応するJacobi積分は一定です。

## 限界・ナビゲーション

中心力は相互作用が位置だけに依存する場合です。相対論的重力や量子軌道は別理論が必要です。

- 前：[Atwood](03_atwood_and_connected_bodies.md)
- 次：[停留作用](../part03_variational/01_stationary_action.md)
- 親：[part02](README.md)
