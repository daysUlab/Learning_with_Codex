# 01_dynamics（力学の全体像）

力学は、自然科学の中で最初に「現象を数式で予測する力」を与えてくれる章です。
このページでは、EMANの物理学の力学章で重視される流れ（現象理解 → 原理 → 計算）を意識して、

- 直観
- 導出
- 検算

を往復できるように整理します。

## 1. 学習目標

1. 運動方程式

$$
\mathbf{F}=m\mathbf{a}
$$

と保存則の関係を説明できる。
2. 衝突・落下・回転で、どの保存則を使うか判断できる。
3. 導出した式を次元・極限・符号で検算できる。
4. 後続の `part01`〜`part04` にスムーズに接続できる。

## 2. 前提知識

- ベクトルの成分表示
- 微分積分の初歩
- 仕事とエネルギーの高校レベルの概念

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

## 4. 本文（直観→導出→確認）

### 4.1 直観

EMANの力学解説でも繰り返されるポイントは、

- 「何を系として切り出すか」
- 「何を無視してよいか」

を先に決めることです。

たとえば衝突問題では、物体1つを追うより「衝突する2物体をまとめた系」と見ると、内部力が消えて保存則が前面に出ます。

### 4.2 導出A：運動量保存

多体系でニュートン方程式を足し上げると

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

特に

$$
\mathbf{F}_{\text{ext}}=\mathbf{0}
$$

なら

$$
\mathbf{P}=\text{const.}
$$

### 4.3 導出B：力学的エネルギー保存

1質点で

$$
m\frac{d\mathbf{v}}{dt}=\mathbf{F}
$$

両辺を速度と内積すると

$$
\frac{d}{dt}\left(\frac{1}{2}mv^2\right)=\mathbf{F}\cdot\mathbf{v}
$$

保存力

$$
\mathbf{F}=-\nabla U
$$

なら

$$
\mathbf{F}\cdot\mathbf{v}=-\frac{dU}{dt}
$$

よって

$$
\frac{d}{dt}\left(K+U\right)=0
$$

### 4.4 導出C：角運動量保存

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

したがって

$$
\boldsymbol{\tau}=\mathbf{0}
$$

なら

$$
\mathbf{L}=\text{const.}
$$

### 4.5 確認テンプレ

1. **次元**：式の左右で単位が一致しているか。
2. **極限**：

$$
 t\to 0
$$

や

$$
 g\to 0
$$

で不自然にならないか。
3. **符号**：座標軸の向きと力の向きが整合しているか。
4. **物理像**：計算結果が現象の直観と矛盾しないか。

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

の物体が1次元で速度

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

から静かに落とした物体の着地直前速度を求めよ（空気抵抗なし）。

**解答**

$$
mgh=\frac{1}{2}mv^2
$$

$$
v=\sqrt{2gh}
$$

### 例題3（角運動量）

外トルクゼロの回転体で、慣性モーメントが

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
4. 1次元弾性衝突で立てるべき保存式を2本書け。
5. 反発係数の定義式を書け。
6. 重心速度の定義を書け。
7. 次元解析で

$$
K
$$

の単位を確認せよ。
8. 回転運動で

$$
\mathbf{L}
$$

の向きの決め方を説明せよ。
9. 保存則を誤用しやすい例を1つ挙げて理由を述べよ。
10. 検算チェック項目を3つ挙げよ。

## 7. 章末まとめ

- 運動方程式と保存則は対立せず、互いに導出可能である。
- 系の切り方を先に決めると、計算量が大きく減る。
- 力学の学習は「式を覚える」より「適用条件を判断する」ことが本質。
- 導出後は必ず次元・極限・符号で検算する。

## 8. 参考（学習補助）

- EMANの物理学（力学）: https://eman-physics.net/mechanics/

## 9. ナビゲーション

- 親: [../README.md](../README.md)
- 次: [columns_and_qa/README.md](columns_and_qa/README.md)
- 次: [part01_momentum_conservation/README.md](part01_momentum_conservation/README.md)
