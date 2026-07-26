# phase space・Hamilton流・Poisson括弧

## phase space

自由度

$$
N
$$

の系は

$$
(q_1,\ldots,q_N,p_1,\ldots,p_N)
$$

という

$$
2N
$$

次元のphase spaceの一点で表します。軌道はHamiltonianが作るflowです。

任意の量

$$
A(q,p,t)
$$

の時間発展は

$$
\frac{dA}{dt}=\{A,H\}+\frac{\partial A}{\partial t}
$$

Poisson括弧は

$$
\{A,B\}=\sum_i\left(
\frac{\partial A}{\partial q_i}\frac{\partial B}{\partial p_i}
-\frac{\partial A}{\partial p_i}\frac{\partial B}{\partial q_i}
\right)
$$

です。

基本関係は

$$
\{q_i,p_j\}=\delta_{ij},\quad
\{q_i,q_j\}=0,\quad
\{p_i,p_j\}=0
$$

です。

## Liouvilleへの橋

Hamilton flowはphase-space volumeを保存します。

$$
\sum_i\left(
\frac{\partial\dot q_i}{\partial q_i}+
\frac{\partial\dot p_i}{\partial p_i}
\right)=0
$$

したがって確率密度はflowに沿って保存され、統計力学のLiouville方程式へ進みます。

## 演習と全解答

1. 一粒子三次元のphase space次元は何か。
   **解答**：六です。
2.
   $$
   \{q,p^2/2m\}
   $$
   を求めよ。
   **解答**：
   $$
   \frac pm
   $$
3.
   $$
   \{p,V(q)\}
   $$
   を求めよ。
   **解答**：
   $$
   -\frac{dV}{dq}
   $$
4. 保存量の判定を書け。
   **解答**：陽な時間依存がなければ
   $$
   \{A,H\}=0
   $$
5. phase-space volume保存は軌道が混ざらない意味か。
   **解答**：細粒度volumeは保存しますが、stretchingとfoldingにより粗視化すると混合して見えます。
6. 量子との対応を述べよ。
   **解答**：Poisson括弧はcommutatorの古典対応になりますが、演算子化の詳細は量子力学で扱います。

## 限界・ナビゲーション

散逸系では通常のphase-space volumeは収縮し得ます。環境まで含めたHamilton系との区別が必要です。

- 前：[Legendre変換](01_legendre_transform_and_hamiltonian.md)
- 次：[場](../part05_infinite_dof/01_from_particles_to_fields.md)
- 関連：[統計力学](../../05_statistical_mechanics/00_overview.md)

## 参考資料

Arnold, *Mathematical Methods of Classical Mechanics*.
