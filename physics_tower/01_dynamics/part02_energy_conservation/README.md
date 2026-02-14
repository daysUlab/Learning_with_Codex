# part02_energy_conservation（エネルギー保存）

このパートでは、位置エネルギーと運動エネルギーの交換を中心に、力学問題を短く解く方法を整理します。

## 1. 学習目標

1. 仕事とエネルギーの関係を式で説明できる。
2. 保存力系でエネルギー保存を適用できる。
3. 非保存力がある場合の修正式を書ける。

## 2. 基本式

仕事と運動エネルギーの関係

$$
W=\Delta K
$$

保存力

$$
\mathbf{F}=-\nabla U
$$

のもとで

$$
K+U=\text{const.}
$$

非保存力があるとき

$$
\Delta(K+U)=W_{\text{nc}}
$$

## 3. 典型問題の型

### 型A：高さと速度

$$
mgh=\frac{1}{2}mv^2
$$

### 型B：ばね

$$
\frac{1}{2}kx^2+\frac{1}{2}mv^2=E
$$

### 型C：摩擦あり

$$
K_i+U_i+W_{\text{fr}}=K_f+U_f
$$

## 4. 例題（2題）

### 例題1

高さ

$$
h
$$

から滑り落ちる質点の最下点速度を求めよ（摩擦なし）。

**解答**

$$
mgh=\frac{1}{2}mv^2
$$

$$
v=\sqrt{2gh}
$$

### 例題2

ばね定数

$$
k
$$

のばねを

$$
A
$$

だけ縮めて離した。平衡点での速さを求めよ。

**解答**

$$
\frac{1}{2}kA^2=\frac{1}{2}mv^2
$$

$$
v=A\sqrt{\frac{k}{m}}
$$

## 5. 演習（5問）

1. 摩擦がない斜面で速度を高さの関数として求めよ。
2. ばね振動で最大速度を求めよ。
3. 摩擦仕事

$$
W_{\text{fr}}=-\mu mg\ell
$$

を使って終速度を求める式を書け。
4. 位置エネルギーの基準点を変えても物理が変わらない理由を述べよ。
5. エネルギー保存が使えない条件を1つ挙げよ。

## 6. ナビゲーション

- 親: [../00_overview.md](../00_overview.md)
- 前: [../part01_momentum_conservation/README.md](../part01_momentum_conservation/README.md)
- 次: [../part03_angular_momentum/README.md](../part03_angular_momentum/README.md)
