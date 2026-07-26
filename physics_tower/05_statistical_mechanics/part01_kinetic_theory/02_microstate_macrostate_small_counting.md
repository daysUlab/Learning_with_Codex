# microstate・macrostate：小さな数え上げから始める

## 区別

- microstate：各自由度の状態を全て指定。
- macrostate：energy、磁化、左右の粒子数など少数の巨視量だけ指定。
- multiplicity
  $$
  \Omega
  $$
  ：一つのmacrostateに対応するmicrostate数。

## coin

三枚の区別できるcoinで表が

$$
n
$$

枚のmacrostateのmultiplicityは

$$
\Omega(n)=\binom{3}{n}
$$

です。

| n | 0 | 1 | 2 | 3 |
|---|---:|---:|---:|---:|
| multiplicity | 1 | 3 | 3 | 1 |

等確率なmicrostateなら中間macrostateほど起こりやすい。

## 箱への粒子分配

N個の区別できる粒子を左右へ独立に入れると

$$
\Omega(N_L)=\binom{N}{N_L}
$$

で、総microstate数は

$$
2^N
$$

です。Nが大きいほどhalf付近へ相対的に集中します。

## 二準位paramagnet

spinが磁場に平行・反平行の二状態を取り、上向き数でmacrostateを指定できます。energyとmagnetizationが同じ数え上げで結びつきます。

## 演習と全解答

1. coin二枚のmicrostate数は何か。
   **解答**：
   $$
   2^2=4
   $$
2. 二枚で表一枚のmultiplicityは何か。
   **解答**：
   $$
   \binom21=2
   $$
3. 四粒子で左右2対2のmultiplicityは何か。
   **解答**：
   $$
   \binom42=6
   $$
4. 最頻macrostateと一つのmicrostateを混同してよいか。
   **解答**：いいえ。macrostateは多くのmicrostateの集合です。
5. 粒子が区別不能なら同じ式か。
   **解答**：一般には違います。量子統計では占有の数え方が変わります。
6. N=10で全粒子が左にいる確率は何か。
   **解答**：
   $$
   2^{-10}=\frac1{1024}
   $$

## ナビゲーション

- 前：[気体分子運動論](01_kinetic_theory_pressure_temperature.md)
- 次：[最頻状態と揺らぎ](03_multiplicity_fluctuations_einstein_solid.md)
- 親：[part01](README.md)
