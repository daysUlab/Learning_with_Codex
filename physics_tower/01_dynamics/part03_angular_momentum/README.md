# part03_angular_momentum（角運動量保存）

このパートでは、回転運動を「トルクと角運動量」の対応で整理し、中心力問題や回転体系の基本を扱います。

## 1. 学習目標

1. 角運動量とトルクをベクトルで定義できる。
2. 外トルクゼロから角運動量保存を導出できる。
3. 面積速度一定との関係を説明できる。

## 2. 基本式

角運動量

$$
\mathbf{L}=\mathbf{r}\times\mathbf{p}
$$

トルク

$$
\boldsymbol{\tau}=\mathbf{r}\times\mathbf{F}
$$

運動方程式

$$
\frac{d\mathbf{L}}{dt}=\boldsymbol{\tau}
$$

特に

$$
\boldsymbol{\tau}=\mathbf{0}
$$

なら

$$
\mathbf{L}=\text{const.}
$$

## 3. 典型問題の型

### 型A：中心力運動

$$
\mathbf{F}\parallel\mathbf{r}
$$

なので

$$
\mathbf{r}\times\mathbf{F}=\mathbf{0}
$$

### 型B：回転体の慣性モーメント

$$
L=I\omega
$$

外トルクゼロなら

$$
I\omega=\text{const.}
$$

### 型C：面積速度

$$
\frac{dA}{dt}=\frac{L}{2m}
$$

## 4. 例題（2題）

### 例題1

半径

$$
r
$$

の円運動で速さ

$$
v
$$

、質量

$$
m
$$

の粒子の角運動量の大きさを求めよ。

**解答**

$$
L=mrv
$$

### 例題2

フィギュアスケータが慣性モーメントを

$$
I_1
$$

から

$$
I_2
$$

へ変えたとき、角速度の比を求めよ（外トルクなし）。

**解答**

$$
I_1\omega_1=I_2\omega_2
$$

$$
\frac{\omega_2}{\omega_1}=\frac{I_1}{I_2}
$$

## 5. 演習（5問）

1. 中心力で角運動量保存を示せ。
2. トルクと仕事率の関係を述べよ。
3. 面積速度一定からケプラー第2法則を説明せよ。
4. 回転半径を小さくすると角速度が増す理由を式で示せ。
5. 角運動量保存とエネルギー保存の違いを述べよ。

## 6. ナビゲーション

- 親: [../00_overview.md](../00_overview.md)
- 前: [../part02_energy_conservation/README.md](../part02_energy_conservation/README.md)
- 次: [../part04_applications/README.md](../part04_applications/README.md)
