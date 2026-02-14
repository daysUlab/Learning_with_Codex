# part02_use_maxwell（マクスウェル方程式を使う）

このパートでは、対称性と境界条件を使って場を求める実践手順を扱います。

## 1. 学習目標

1. 対称性から適切な方程式形を選べる。
2. 境界条件を使って定数を決定できる。
3. 電場・磁場を計算して物理的に解釈できる。

## 2. 基本手順

1. 対称性を判定する。
2. 積分形または微分形を選ぶ。
3. 境界条件を適用する。
4. 次元と極限で検算する。

## 3. 典型公式

点電荷

$$
\mathbf{E}=\frac{1}{4\pi\varepsilon_0}\frac{q}{r^2}\hat{\mathbf{r}}
$$

無限直線電流

$$
B=\frac{\mu_0 I}{2\pi r}
$$

平面波の関係

$$
B=\frac{E}{c}
$$

## 4. 例題（1題）

無限長直線電流

$$
I
$$

の周囲の磁場を求めよ。

**解答**

$$
\oint \mathbf{B}\cdot d\mathbf{l}=\mu_0 I
$$

$$
B(2\pi r)=\mu_0 I
$$

$$
B=\frac{\mu_0 I}{2\pi r}
$$

## 5. 演習（3問）

1. 球対称電荷分布の外部電場を求めよ。
2. 平行平板コンデンサ内部の電場を書け。
3. ソレノイド内部磁場の近似式を書け。

## 6. ナビゲーション

- 親: [../00_overview.md](../00_overview.md)
- 前: [../part01_build_maxwell/README.md](../part01_build_maxwell/README.md)
- 次: [../part03_phenomenology/README.md](../part03_phenomenology/README.md)
