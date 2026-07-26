# 比較例題：斜面上の物体と単振り子

## 斜面

傾斜角

$$
\alpha
$$

の摩擦なし斜面で、斜面下向きを

$$
s
$$

とします。

| 観点 | Newton | Lagrange |
|---|---|---|
| 変数 | 水平・鉛直または接線・法線 | 斜面方向座標s |
| 式 | 接線方向と法線方向 | Euler–Lagrange一本 |
| 拘束力 | 垂直抗力を求める | 不要なら消える |
| 対称性 | 成分分解後に見る | sがpotentialに線形 |

Newtonでは

$$
m\ddot s=mg\sin\alpha,\qquad N=mg\cos\alpha
$$

です。Lagrangian

$$
L=\frac12m\dot s^2+mgs\sin\alpha
$$

から同じ接線運動を得ます。抗力まで必要ならNewtonが直接的です。

## 単振り子

Newtonでは接線方向

$$
ml\ddot\theta=-mg\sin\theta
$$

と半径方向

$$
T-mg\cos\theta=ml\dot\theta^2
$$

を分けます。Lagrangeでは角度だけで運動式が出ます。張力が目的ならNewton式へ戻ります。

energyは

$$
E=\frac12ml^2\dot\theta^2+mgl(1-\cos\theta)
$$

です。時間に陽に依存しないため保存されます。

## 数値例

$$
l=1.0\ \mathrm{m}
$$

なら小振幅周期は

$$
\tau=2\pi\sqrt{\frac{l}{g}}\simeq2.01\ \mathrm{s}
$$

です。

## 演習と全解答

1. 30度斜面の加速度を求めよ。
   **解答**：
   $$
   a=g\sin30^\circ=\frac g2
   $$
2. 質量を二倍にすると斜面加速度はどうなるか。
   **解答**：変わりません。
3. 斜面の抗力を求めるのに有利な形式は何か。
   **解答**：Newton形式です。
4. 振り子で保存される量を答えよ。
   **解答**：支点固定・摩擦なしなら上記のmechanical energyです。
5. 小角周期が質量に依存しないことを示せ。
   **解答**：
   $$
   ml^2\ddot\theta+mgl\theta=0
   $$
   で質量が消えます。
6. 最下点速度
   $$
   v
   $$
   の張力を求めよ。
   **解答**：
   $$
   T=mg+\frac{mv^2}{l}
   $$

## 結論

答えは同じです。欲しい量が軌道ならLagrange、拘束力そのものならNewtonが有利です。

- 前：[EL方程式](01_virtual_work_and_euler_lagrange.md)
- 次：[Atwood](03_atwood_and_connected_bodies.md)
- 親：[part02](README.md)
