# 01_dynamics（力学の全体像）

この章では、力学を

- 運動量保存
- エネルギー保存
- 角運動量保存

の3本柱で整理し、問題ごとにどの保存則を主役にするか判断できる状態を目指します。

## 1. 学習目標

1. 力学の基本量を定義し、単位と次元を説明できる。
2. ニュートン方程式から保存則への接続を説明できる。
3. 衝突・振動・回転の典型問題で、解法の入口を選択できる。
4. 導出後に行う検算テンプレを実行できる。
5. 後続の各パートへ目的意識を持って進める。

## 2. 前提知識

- 速度と加速度の定義
- 微分積分の基本
- ベクトルの成分表示

復習リンク:

- [../00_physics_math_tools/00_overview.md](../00_physics_math_tools/00_overview.md)
- [../00_physics_math_tools/vector_analysis/README.md](../00_physics_math_tools/vector_analysis/README.md)

## 3. 記法・単位・符号規約

- 質量

$$
m
$$

- 位置

$$
\mathbf{r}
$$

- 速度

$$
\mathbf{v}=\frac{d\mathbf{r}}{dt}
$$

- 加速度

$$
\mathbf{a}=\frac{d\mathbf{v}}{dt}
$$

- 力

$$
\mathbf{F}
$$

- 運動量

$$
\mathbf{p}=m\mathbf{v}
$$

- 運動エネルギー

$$
K=\frac{1}{2}mv^2
$$

- 角運動量

$$
\mathbf{L}=\mathbf{r}\times\mathbf{p}
$$

- トルク

$$
\boldsymbol{\tau}=\mathbf{r}\times\mathbf{F}
$$

## 4. 本文（直観→導出→確認）

### 4.1 直観：保存則は「計算の近道」

力学の基本方程式は

$$
\mathbf{F}=m\mathbf{a}
$$

ですが、毎回これを成分で解くのは重いことがあります。

- 外力の合計がゼロなら運動量保存
- 非保存力が無視できるなら力学的エネルギー保存
- 外トルクがゼロなら角運動量保存

という形で、保存則に切り替えると短い計算で答えへ到達できます。

### 4.2 導出A：運動量保存

ニュートン方程式を系全体で足し上げると

$$
\frac{d}{dt}\sum_i \mathbf{p}_i=\sum_i \mathbf{F}_i^{\text{ext}}+\sum_i \mathbf{F}_i^{\text{int}}
$$

内部力は作用反作用で打ち消し合うため

$$
\sum_i \mathbf{F}_i^{\text{int}}=\mathbf{0}
$$

よって

$$
\frac{d\mathbf{P}}{dt}=\mathbf{F}_{\text{ext}},\quad \mathbf{P}=\sum_i \mathbf{p}_i
$$

特に

$$
\mathbf{F}_{\text{ext}}=\mathbf{0}
$$

なら

$$
\mathbf{P}=\text{const.}
$$

### 4.3 導出B：エネルギー保存

1質点で

$$
m\frac{d\mathbf{v}}{dt}=\mathbf{F}
$$

両辺と

$$
\mathbf{v}
$$

の内積をとると

$$
m\frac{d\mathbf{v}}{dt}\cdot\mathbf{v}=\mathbf{F}\cdot\mathbf{v}
$$

左辺は

$$
\frac{d}{dt}\left(\frac{1}{2}mv^2\right)
$$

右辺は位置依存ポテンシャル

$$
U
$$

を用いて

$$
\mathbf{F}=-\nabla U
$$

と書けるとき

$$
\mathbf{F}\cdot\mathbf{v}=-\frac{dU}{dt}
$$

したがって

$$
\frac{d}{dt}\left(K+U\right)=0
$$

### 4.4 導出C：角運動量保存

角運動量の時間微分は

$$
\frac{d\mathbf{L}}{dt}=\frac{d}{dt}(\mathbf{r}\times\mathbf{p})
$$

$$
=\mathbf{r}\times\frac{d\mathbf{p}}{dt}+\frac{d\mathbf{r}}{dt}\times\mathbf{p}
$$

2項目は

$$
\mathbf{v}\times m\mathbf{v}=\mathbf{0}
$$

なので

$$
\frac{d\mathbf{L}}{dt}=\mathbf{r}\times\mathbf{F}=\boldsymbol{\tau}
$$

ゆえに

$$
\boldsymbol{\tau}=\mathbf{0}
$$

なら

$$
\mathbf{L}=\text{const.}
$$

### 4.5 確認テンプレ

1. 保存則の適用条件を書いたか。
2. 系の取り方を明示したか。
3. 次元整合を確認したか。
4. 極限で既知結果へ戻るか確認したか。

## 5. 例題（3題）

### 例題1（易）

質量

$$
2m
$$

の物体が速度

$$
3u
$$

で進み、質量

$$
m
$$

の物体が速度

$$
-u
$$

で進む1次元衝突を考える。衝突前の全運動量を求めよ。

**解答**

$$
P=(2m)(3u)+(m)(-u)=5mu
$$

### 例題2（中）

質量

$$
m
$$

の物体を高さ

$$
h
$$

から静かに落とす。空気抵抗を無視した地面直前の速さを求めよ。

**解答**

$$
mgh=\frac{1}{2}mv^2
$$

$$
v=\sqrt{2gh}
$$

### 例題3（やや難）

中心力場で運動する質点について、面積速度が一定であることを示せ。

**解答**

中心力では

$$
\boldsymbol{\tau}=\mathbf{r}\times\mathbf{F}=\mathbf{0}
$$

なので

$$
\mathbf{L}=\text{const.}
$$

また面積速度は

$$
\frac{dA}{dt}=\frac{1}{2}r^2\dot{\theta}
$$

角運動量の大きさ

$$
L=mr^2\dot{\theta}
$$

より

$$
\frac{dA}{dt}=\frac{L}{2m}=\text{const.}
$$

## 6. 演習問題（10問）

### 問1

外力がゼロの2体系で、全運動量が保存されることを示せ。

### 問2

次式の次元が一致することを示せ。

$$
K=\frac{1}{2}mv^2
$$

### 問3

重力場で

$$
U=mgy
$$

としたとき、力

$$
\mathbf{F}
$$

を

$$
\mathbf{F}=-\nabla U
$$

から求めよ。

### 問4

1次元弾性衝突の保存則を2本書け。

### 問5

半径

$$
r
$$

角速度

$$
\omega
$$

の等速円運動で、速さ

$$
v
$$

を求めよ。

### 問6

トルクがゼロのとき角運動量が保存されることを式で示せ。

### 問7

高さ

$$
4h
$$

から落下した物体の地面直前速度を求めよ。

### 問8

次の量のうち保存則適用が最短になるものを選べ。

$$
\text{斜方投射の最高点の高さ}
$$

### 問9

非保存力が働くとき

$$
K+U
$$

が一般には保存しない理由を述べよ。

### 問10

系の取り方を変えると保存則の見え方が変わる例を1つ挙げよ。

## 7. 演習解答

### 問1 解答

$$
\frac{d\mathbf{P}}{dt}=\mathbf{F}_{\text{ext}}=\mathbf{0}
$$

より

$$
\mathbf{P}=\text{const.}
$$

### 問2 解答

$$
[K]=\text{J}=
\text{kg}\cdot\text{m}^2\cdot\text{s}^{-2}
$$

$$
\left[\frac{1}{2}mv^2\right]=\text{kg}\cdot(\text{m}\cdot\text{s}^{-1})^2=
\text{kg}\cdot\text{m}^2\cdot\text{s}^{-2}
$$

### 問3 解答

$$
\nabla U=
\begin{pmatrix}
0 \\
mg \\
0
\end{pmatrix}
$$

$$
\mathbf{F}=-\nabla U=
\begin{pmatrix}
0 \\
-mg \\
0
\end{pmatrix}
$$

### 問4 解答

$$
m_1u_1+m_2u_2=m_1v_1+m_2v_2
$$

$$
\frac{1}{2}m_1u_1^2+\frac{1}{2}m_2u_2^2=
\frac{1}{2}m_1v_1^2+\frac{1}{2}m_2v_2^2
$$

### 問5 解答

$$
v=r\omega
$$

### 問6 解答

$$
\frac{d\mathbf{L}}{dt}=\boldsymbol{\tau}=\mathbf{0}
$$

よって

$$
\mathbf{L}=\text{const.}
$$

### 問7 解答

$$
mg(4h)=\frac{1}{2}mv^2
$$

$$
v=\sqrt{8gh}=2\sqrt{2gh}
$$

### 問8 解答

最高点では速度0の条件を使えるため、エネルギー保存が最短。

### 問9 解答

摩擦のような非保存力は力学的エネルギーを熱などへ散逸させるため、

$$
K+U
$$

は一定でなくなる。

### 問10 解答

2物体衝突で、2物体系全体を取ると運動量保存が使えるが、片方のみを系にすると相互作用力が外力になる。

## 8. 章末まとめ

- 力学は運動量・エネルギー・角運動量の3保存則で整理できる。
- 保存則は適用条件を書いてから使う。
- ニュートン方程式と保存則は対立せず、相互に導出可能。
- 検算は次元、符号、極限、既知結果の4点を固定すると安定する。

## 9. ナビゲーション

- 親: [../README.md](../README.md)
- 次: [part01_momentum_conservation/README.md](part01_momentum_conservation/README.md)
- 関連: [part02_energy_conservation/README.md](part02_energy_conservation/README.md)
- 関連: [part03_angular_momentum/README.md](part03_angular_momentum/README.md)
- 補助: [columns_and_qa/README.md](columns_and_qa/README.md)
