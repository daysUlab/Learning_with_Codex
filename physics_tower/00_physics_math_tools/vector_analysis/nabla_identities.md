# nabla_identities（ナブラ恒等式の実践）

このページでは、ベクトル解析で最頻出のナブラ恒等式を、

- 直観
- 成分導出
- 検算

の順で整理します。電磁気学・流体力学でそのまま使える計算手順に落とし込むことが目標です。

## 1. 学習目標

1. 勾配・発散・回転の合成演算を式として正確に書ける。
2. 次の代表恒等式を成分で導出できる。
3. 物理での意味（保存則、ポテンシャル表示、波動方程式）を説明できる。
4. 記号ミスを避けるための検算テンプレを実行できる。
5. 後続の電磁気・流体で必要な最小セットを暗記ではなく再導出できる。

## 2. 前提知識

- [README.md](README.md) の勾配・発散・回転
- 偏微分と混合偏微分
- 直交座標での成分表示

## 3. 記法

スカラー場を

$$
f(x,y,z)
$$

ベクトル場を

$$
\mathbf{F}(x,y,z)=
\begin{pmatrix}
F_x \\
F_y \\
F_z
\end{pmatrix}
$$

とする。

ナブラは

$$
\nabla=
\begin{pmatrix}
\partial_x \\
\partial_y \\
\partial_z
\end{pmatrix}
$$

とし、

$$
\partial_x=\frac{\partial}{\partial x},\quad
\partial_y=\frac{\partial}{\partial y},\quad
\partial_z=\frac{\partial}{\partial z}
$$

を用いる。

## 4. 本文（直観→導出→確認）

### 4.1 直観：恒等式は「構造」を見抜く道具

- 回転の発散がゼロになる恒等式は、「渦には湧き出しがない」という幾何学的制約を表す。
- 勾配の回転がゼロになる恒等式は、「ポテンシャル由来の場は渦なし」を表す。
- 二重回転の恒等式は、波動方程式やヘルムホルツ分解へ接続する計算の核心になる。

### 4.2 恒等式A：

$$
\nabla\cdot(\nabla\times\mathbf{F})=0
$$

#### 成分導出

$$
\nabla\times\mathbf{F}=
\begin{pmatrix}
\partial_y F_z-\partial_z F_y \\
\partial_z F_x-\partial_x F_z \\
\partial_x F_y-\partial_y F_x
\end{pmatrix}
$$

よって発散を取ると

$$
\nabla\cdot(\nabla\times\mathbf{F})=
\partial_x(\partial_y F_z-\partial_z F_y)
+\partial_y(\partial_z F_x-\partial_x F_z)
+\partial_z(\partial_x F_y-\partial_y F_x)
$$

$$
=(\partial_x\partial_y F_z-\partial_y\partial_x F_z)
+(\partial_y\partial_z F_x-\partial_z\partial_y F_x)
+(\partial_z\partial_x F_y-\partial_x\partial_z F_y)=0
$$

混合偏微分の交換可能性で各項が相殺される。

### 4.3 恒等式B：

$$
\nabla\times(\nabla f)=\mathbf{0}
$$

#### 成分導出

$$
\nabla f=
\begin{pmatrix}
\partial_x f \\
\partial_y f \\
\partial_z f
\end{pmatrix}
$$

これの回転を計算すると

$$
\nabla\times(\nabla f)=
\begin{pmatrix}
\partial_y\partial_z f-\partial_z\partial_y f \\
\partial_z\partial_x f-\partial_x\partial_z f \\
\partial_x\partial_y f-\partial_y\partial_x f
\end{pmatrix}=
\begin{pmatrix}
0 \\
0 \\
0
\end{pmatrix}
$$

となる。

### 4.4 恒等式C：

$$
\nabla\times(\nabla\times\mathbf{F})=
\nabla(\nabla\cdot\mathbf{F})-\nabla^2\mathbf{F}
$$

ここで

$$
\nabla^2\mathbf{F}=
\begin{pmatrix}
\nabla^2 F_x \\
\nabla^2 F_y \\
\nabla^2 F_z
\end{pmatrix},\quad
\nabla^2=\partial_x^2+\partial_y^2+\partial_z^2
$$

である。

#### 成分確認（x成分）

左辺x成分は

$$
[\nabla\times(\nabla\times\mathbf{F})]_x=
\partial_y(\partial_x F_y-\partial_y F_x)-\partial_z(\partial_z F_x-\partial_x F_z)
$$

$$
=\partial_x\partial_y F_y+\partial_x\partial_z F_z-(\partial_y^2+\partial_z^2)F_x
$$

右辺x成分は

$$
[\nabla(\nabla\cdot\mathbf{F})-\nabla^2\mathbf{F}]_x=
\partial_x(\partial_x F_x+\partial_y F_y+\partial_z F_z)-
(\partial_x^2+\partial_y^2+\partial_z^2)F_x
$$

$$
=\partial_x\partial_y F_y+\partial_x\partial_z F_z-(\partial_y^2+\partial_z^2)F_x
$$

で一致する。y成分、z成分も同様。

### 4.5 物理への接続

#### 接続1：静電場

$$
\nabla\times\mathbf{E}=\mathbf{0}
$$

なら

$$
\mathbf{E}=-\nabla\phi
$$

とポテンシャル表示できる。

#### 接続2：非圧縮流

$$
\nabla\cdot\mathbf{v}=0
$$

では、二重回転恒等式から

$$
\nabla\times(\nabla\times\mathbf{v})=-\nabla^2\mathbf{v}
$$

が得られ、渦度方程式の整理に有効。

### 4.6 確認テンプレ

1. 演算順を固定したか。
2. 混合偏微分の交換可能性が必要な滑らかさ条件を暗黙に仮定しているか。
3. 成分式で1成分だけでも両辺一致を確認したか。
4. 次元が一致するか。

## 5. 例題（3題）

### 例題1（易）

$$
\mathbf{F}=
\begin{pmatrix}
-y \\
x \\
0
\end{pmatrix}
$$

に対して

$$
\nabla\cdot(\nabla\times\mathbf{F})
$$

を求めよ。

**解答**

まず

$$
\nabla\times\mathbf{F}=
\begin{pmatrix}
0 \\
0 \\
2
\end{pmatrix}
$$

なので

$$
\nabla\cdot(\nabla\times\mathbf{F})=
\partial_x 0+\partial_y 0+\partial_z 2=0
$$

### 例題2（中）

$$
f=x^2y+yz^2
$$

について

$$
\nabla\times(\nabla f)
$$

を確認せよ。

**解答**

$$
\nabla f=
\begin{pmatrix}
2xy \\
x^2+z^2 \\
2yz
\end{pmatrix}
$$

回転を成分計算すると3成分とも0になり

$$
\nabla\times(\nabla f)=\mathbf{0}
$$

### 例題3（やや難）

$$
\mathbf{F}=
\begin{pmatrix}
x^2 \\
xy \\
z
\end{pmatrix}
$$

に対して二重回転恒等式の両辺を計算し一致を示せ。

**解答**

$$
\nabla\cdot\mathbf{F}=2x+x+1=3x+1
$$

$$
\nabla(\nabla\cdot\mathbf{F})=
\begin{pmatrix}
3 \\
0 \\
0
\end{pmatrix}
$$

$$
\nabla^2\mathbf{F}=
\begin{pmatrix}
2 \\
0 \\
0
\end{pmatrix}
$$

よって右辺は

$$
\begin{pmatrix}
1 \\
0 \\
0
\end{pmatrix}
$$

一方、左辺

$$
\nabla\times\mathbf{F}=
\begin{pmatrix}
0 \\
0 \\
y
\end{pmatrix}
$$

$$
\nabla\times(\nabla\times\mathbf{F})=
\begin{pmatrix}
1 \\
0 \\
0
\end{pmatrix}
$$

で一致。

## 6. 演習問題（10問）

### 問1

任意の十分滑らかなベクトル場

$$
\mathbf{F}
$$

について、次を成分表示で示せ。

$$
\nabla\cdot(\nabla\times\mathbf{F})=0
$$

### 問2

任意の十分滑らかなスカラー場

$$
f
$$

について、次を成分表示で示せ。

$$
\nabla\times(\nabla f)=\mathbf{0}
$$

### 問3

次の場に対して、

$$
\nabla\times(\nabla\times\mathbf{F})
$$

を求めよ。

$$
\mathbf{F}=
\begin{pmatrix}
0 \\
0 \\
xy
\end{pmatrix}
$$

### 問4

次の場で

$$
\nabla\cdot\mathbf{F}=0
$$

を確認せよ。

$$
\mathbf{F}=
\begin{pmatrix}
-y \\
x \\
0
\end{pmatrix}
$$

### 問5

次の場のラプラシアン

$$
\nabla^2\mathbf{F}
$$

を求めよ。

$$
\mathbf{F}=
\begin{pmatrix}
xz \\
yz \\
xy
\end{pmatrix}
$$

### 問6

次の

$$
\phi
$$

に対して、

$$
\nabla\times(-\nabla\phi)
$$

を計算せよ。

$$
\phi=x^2+y^2+z^2
$$

### 問7

二重回転恒等式の y 成分のみを明示的に導出せよ。

### 問8

$$
\nabla\cdot\mathbf{v}=0
$$

のとき、

$$
\nabla\times(\nabla\times\mathbf{v})=-\nabla^2\mathbf{v}
$$

を示せ。

### 問9

次の記法が曖昧である理由を、成分表示で説明せよ。

$$
\nabla\cdot(\nabla\mathbf{F})
$$

### 問10

任意のベクトル場を

$$
\mathbf{F}=\nabla\phi+\mathbf{G}
$$

と分解するとき、

$$
\nabla\cdot\mathbf{G}=0
$$

を満たす成分の意味を文章で述べよ。

## 7. 演習解答

### 問1 解答

回転を成分表示し発散を取ると、混合偏微分の差が3組現れ、各組が 0 となる。

### 問2 解答

勾配を成分表示し回転を取ると、混合偏微分の差のみになり 0 となる。

### 問3 解答

$$
\nabla\times\mathbf{F}=
\begin{pmatrix}
x \\
-y \\
0
\end{pmatrix}
$$

$$
\nabla\times(\nabla\times\mathbf{F})=
\begin{pmatrix}
0 \\
0 \\
-2
\end{pmatrix}
$$

### 問4 解答

$$
\nabla\cdot\mathbf{F}=\partial_x(-y)+\partial_y x+\partial_z 0=0
$$

### 問5 解答

各成分が2次微分で 0 になるので、

$$
\nabla^2\mathbf{F}=\mathbf{0}
$$

### 問6 解答

恒等式より必ず

$$
\mathbf{0}
$$

となる。

### 問7 解答

y 成分は

$$
\partial_z(\partial_y F_z-\partial_z F_y)-\partial_x(\partial_x F_y-\partial_y F_x)
$$

を整理して

$$
\partial_y(\nabla\cdot\mathbf{F})-\nabla^2 F_y
$$

に一致する。

### 問8 解答

恒等式 C の右辺で

$$
\nabla(\nabla\cdot\mathbf{v})
$$

が 0 になるので直ちに成立する。

### 問9 解答

$$
\nabla\mathbf{F}
$$

はヤコビ行列を指す場合と他の記法が混在し、

$$
\nabla\cdot(\nabla\mathbf{F})
$$

は成分ごとの発散なのかテンソル縮約なのか不明確である。明示的な添字が必要。

### 問10 解答

$$
\nabla\phi
$$

は無渦成分、

$$
\mathbf{G}
$$

は発散ゼロのソレノイダル成分で、流体では体積保存流れの成分を表す。

## 8. 章末まとめ

- ナブラ恒等式は暗記対象ではなく、成分計算で再構築できる。
- 次の2式は電磁気のポテンシャル表示の基盤。
$$
\nabla\cdot(\nabla\times\mathbf{F})=0
$$
$$
\nabla\times(\nabla f)=\mathbf{0}
$$
- 二重回転恒等式は波動方程式や渦度方程式の変形で必須。
- 演算順、添字、滑らかさ条件を固定して計算するのが実務的に重要。

## 9. ナビゲーション

- 親: [README.md](README.md)
- 次の章: [../../../01_dynamics/00_overview.md](../../../01_dynamics/00_overview.md)
