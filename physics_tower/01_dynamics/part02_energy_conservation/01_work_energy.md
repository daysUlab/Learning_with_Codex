# 仕事と運動エネルギー定理

## 学習目標
- 仕事と運動エネルギーの関係を運動方程式から導ける。
- 速度や軌道が求めにくい問題でエネルギー法を使える。

## 1. 導出
運動方程式

$$
\mathbf{F}=m\frac{d\mathbf{v}}{dt}
$$

の両辺と微小変位

$$
d\mathbf{r}
$$

の内積をとると

$$
\mathbf{F}\cdot d\mathbf{r}
= m\frac{d\mathbf{v}}{dt}\cdot d\mathbf{r}
$$

右辺に

$$
d\mathbf{r}=\mathbf{v}dt
$$

を用いれば

$$
\mathbf{F}\cdot d\mathbf{r}=m\mathbf{v}\cdot d\mathbf{v}
$$

したがって

$$
\int_{A}^{B}\mathbf{F}\cdot d\mathbf{r}
=\int_{v_A}^{v_B}m\mathbf{v}\cdot d\mathbf{v}
=\frac{1}{2}mv_B^2-\frac{1}{2}mv_A^2
$$

となり

$$
W_{A\to B}=\Delta K
$$

を得る。

## 2. 複数の力がある場合
合力の仕事は各力の仕事の和である。

$$
\Delta K=\sum_j W_j
$$

ここから「どの力がエネルギーを供給し、どの力が散逸させるか」を切り分ける。

## 3. 有効な使いどころ
- 時間依存より位置依存が自然な問題。
- 速度の大きさだけ知りたい問題。
- 直線運動でなくても、仕事が計算しやすい問題。

## 4. 典型例
高さ

$$
h
$$

だけ落下した質点では重力の仕事

$$
W= mgh
$$

により

$$
\frac{1}{2}mv^2-\frac{1}{2}mv_0^2 = mgh
$$

を得る。初速ゼロなら

$$
v=\sqrt{2gh}
$$

となる。

## まとめ
- 仕事と運動エネルギー定理は、運動方程式と同値の重要な表現である。
- 力の内積積分として仕事を正しく評価することが鍵になる。
