# 横断1：Newton・Lagrange・Hamilton

## 一つの運動、三つの表現

| 問い | Newton | Lagrange | Hamilton |
|---|---|---|---|
| 基本変数 | 位置・速度 | 一般化座標・速度 | 一般化座標・共役運動量 |
| 方程式 | 二階 | 二階 | 一階二本 |
| 拘束 | reactionを含める | 座標へ組み込む | constrained phase space |
| 保存量 | force/torqueから | symmetryから | Poisson bracketから |

調和振動子では

$$
m\ddot x=-kx
$$

$$
L=\frac12m\dot x^2-\frac12kx^2
$$

$$
H=\frac{p^2}{2m}+\frac12kx^2
$$

が同じ軌道を表します。

## モデル選択

軌道とreaction forceが欲しい単純系はNewton、複雑な拘束はLagrange、ensemble・canonical transformation・量子への接続はHamiltonが有利です。

## 演習と解答

1. 三形式で物理予測は変わるか。
   **解答**：同じmodel・初期条件・適用条件なら変わりません。
2. 振り子の張力に有利なのは何か。
   **解答**：Newtonです。
3. cyclic coordinateから何が分かるか。
   **解答**：共役運動量保存です。
4. phase spaceは何次元か。
   **解答**：N自由度なら
   $$
   2N
   $$
5. Hamiltonianは常にenergyか。
   **解答**：いいえ。条件を確認します。
6. 統計力学への直接の入口は何か。
   **解答**：Hamiltonianとphase spaceです。

- 詳細：[解析力学](../03_analytical_mechanics/00_overview.md)
- 次：[energy](02_mechanical_and_internal_energy.md)
- 親：[横断記事](README.md)
