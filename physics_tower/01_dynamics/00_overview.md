# 01_dynamics（力学の全体像）

力学は、

- 何が運動を変えるか
- 何が保存されるか
- どの近似が妥当か

を、定量的に判断するための基礎です。
このページでは、EMANの物理学の力学章で重視される「直観と式の往復」を意識し、

- 直観
- 導出
- 検算

を1セットとして扱います。

## 1. 学習目標

1. 運動方程式

$$
\mathbf{F}=m\mathbf{a}
$$

と、保存則の関係を説明できる。
2. 衝突・落下・回転の問題で、どの保存則を使うか選べる。
3. 解いた後に、次元・符号・極限で妥当性を検証できる。
4. `01_dynamics` 配下の子mdへ目的意識を持って進める。

## 2. 前提知識

- ベクトルの成分表示
- 微分積分の初歩
- 高校レベルの仕事・エネルギー概念

## 3. 基本記号

位置

$$
\mathbf{r}
$$

速度

$$
\mathbf{v}=\frac{d\mathbf{r}}{dt}
$$

加速度

$$
\mathbf{a}=\frac{d\mathbf{v}}{dt}
$$

運動量

$$
\mathbf{p}=m\mathbf{v}
$$

運動エネルギー

$$
K=\frac{1}{2}mv^2
$$

角運動量

$$
\mathbf{L}=\mathbf{r}\times\mathbf{p}
$$

トルク

$$
\boldsymbol{\tau}=\mathbf{r}\times\mathbf{F}
$$

## 4. 本文（直観→導出→確認）

### 4.1 直観

力学計算で最初に決めるべきは、

- 系の境界
- 無視する効果（摩擦・空気抵抗など）
- 有効な時間スケール

です。ここが曖昧だと、式は正しくても解釈が崩れます。

### 4.2 導出A：運動量保存

多体系でニュートン方程式を総和すると

$$
\frac{d}{dt}\sum_i \mathbf{p}_i=\sum_i \mathbf{F}_i^{\text{ext}}+\sum_i \mathbf{F}_i^{\text{int}}
$$

作用反作用により

$$
\sum_i \mathbf{F}_i^{\text{int}}=\mathbf{0}
$$

なので

$$
\frac{d\mathbf{P}}{dt}=\mathbf{F}_{\text{ext}}
$$

外力和がゼロなら

$$
\mathbf{P}=\text{const.}
$$

### 4.3 導出B：力学的エネルギー保存

1質点で

$$
m\frac{d\mathbf{v}}{dt}=\mathbf{F}
$$

両辺を

$$
\mathbf{v}
$$

と内積すると

$$
\frac{d}{dt}\left(\frac{1}{2}mv^2\right)=\mathbf{F}\cdot\mathbf{v}
$$

保存力

$$
\mathbf{F}=-\nabla U
$$

を仮定すると

$$
\mathbf{F}\cdot\mathbf{v}=-\frac{dU}{dt}
$$

よって

$$
\frac{d}{dt}\left(K+U\right)=0
$$

### 4.4 導出C：角運動量保存

角運動量

$$
\mathbf{L}=\mathbf{r}\times\mathbf{p}
$$

を時間微分すると

$$
\frac{d\mathbf{L}}{dt}=\mathbf{r}\times\frac{d\mathbf{p}}{dt}+\mathbf{v}\times\mathbf{p}
$$

第2項は

$$
\mathbf{v}\times m\mathbf{v}=\mathbf{0}
$$

なので

$$
\frac{d\mathbf{L}}{dt}=\mathbf{r}\times\mathbf{F}=\boldsymbol{\tau}
$$

外トルクがゼロなら

$$
\mathbf{L}=\text{const.}
$$

### 4.5 確認テンプレ

1. 次元整合
2. 符号整合
3. 極限整合
4. 既知解への還元

## 5. 例題（3題）

### 例題1（運動量）

質量

$$
2m
$$

と

$$
m
$$

の2物体が、1次元でそれぞれ速度

$$
3u,
\quad
-u
$$

を持つ。全運動量を求めよ。

**解答**

$$
P=(2m)(3u)+(m)(-u)=5mu
$$

### 例題2（エネルギー）

高さ

$$
h
$$

から静止落下（空気抵抗無視）した物体の着地直前速度を求めよ。

**解答**

$$
mgh=\frac{1}{2}mv^2
$$

$$
v=\sqrt{2gh}
$$

### 例題3（角運動量）

外トルクゼロで慣性モーメントが

$$
I_1
$$

から

$$
I_2
$$

へ変化したときの角速度比を求めよ。

**解答**

$$
I_1\omega_1=I_2\omega_2
$$

$$
\frac{\omega_2}{\omega_1}=\frac{I_1}{I_2}
$$

## 6. 演習（10問）

1. 外力ゼロの2体系で運動量保存を導出せよ。
2. 保存力の定義から

$$
K+U=\text{const.}
$$

を示せ。
3. 外トルクゼロなら角運動量保存となることを示せ。
4. 1次元弾性衝突で必要な保存式を2本書け。
5. 反発係数の定義式を書け。
6. 重心速度の定義を書け。
7. 次元解析で

$$
K
$$

の単位を示せ。
8. 回転運動で角運動量ベクトルの向きの決め方を説明せよ。
9. 保存則の誤用例を1つ挙げ、誤りの理由を述べよ。
10. 検算チェック項目を3つ挙げよ。

## 7. 章末まとめ

- 運動方程式と保存則は独立ではなく、相互に導出可能である。
- 問題を解く前に「系の切り方」を固定すると、誤りが減り見通しが良くなる。
- 力学では、公式暗記より適用条件の判断が重要である。
- 導出後の検算は解答の信頼性を大きく高める。

## 8. 参考（学習補助）

- EMANの物理学（力学）: https://eman-physics.net/mechanics/

## 9. ナビゲーション

- 親: [../README.md](../README.md)
- 関連: [columns_and_qa/README.md](columns_and_qa/README.md)
- 関連: [part01_momentum_conservation/README.md](part01_momentum_conservation/README.md)
- 関連: [part02_energy_conservation/README.md](part02_energy_conservation/README.md)
- 関連: [part03_angular_momentum/README.md](part03_angular_momentum/README.md)
- 関連: [part04_applications/README.md](part04_applications/README.md)
