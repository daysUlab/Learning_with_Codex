# 対称性・cyclic coordinate・Noetherの定理

## 問い

保存則を運動方程式を解いた後に発見するのではなく、作用の不変性から先に読めるでしょうか。

Lagrangianが座標

$$
q_k
$$

に陽に依存しないとき

$$
\frac{\partial L}{\partial q_k}=0
$$

なのでEuler–Lagrange式から

$$
\frac{d}{dt}\frac{\partial L}{\partial\dot q_k}=0
$$

すなわち共役運動量が保存されます。この

$$
q_k
$$

をcyclic coordinateと呼びます。

## 連続対称性

微小変換

$$
q_i\to q_i+\varepsilon\Delta q_i,\qquad
t\to t+\varepsilon\Delta t
$$

で作用が不変ならNoether charge

$$
Q=\sum_i p_i\Delta q_i-H\Delta t
$$

が保存されます。

| 対称性 | 保存量 |
|---|---|
| 空間並進 | linear momentum |
| 回転 | angular momentum |
| 時間並進 | energy |
| gauge対称性 | charge conservationへ接続 |

## 例：中心力

極角

$$
\phi
$$

はcyclicなので

$$
p_\phi=mr^2\dot\phi
$$

が保存されます。これは回転対称性の結果です。

## 演習と全解答

1. 自由粒子でcyclicな座標を答えよ。
   **解答**：Cartesian座標すべてで、各運動量が保存します。
2. 時間依存potentialではenergyは保存するか。
   **解答**：一般には保存しません。
3. 振り子の角度はcyclicか。
   **解答**：
   $$
   V=mgl(1-\cos\theta)
   $$
   に現れるのでcyclicではありません。
4. 球対称potentialで保存される量は何か。
   **解答**：angular momentum vectorです。
5. 離散対称性にも同じ形の保存量が必ずあるか。
   **解答**：Noether第一定理の直接対応は連続対称性です。
6. Lが全微分だけ変わる場合は対称性か。
   **解答**：作用の運動方程式は不変で、境界項を含めたNoether量が得られます。

## 誤解と限界

対称性は「見た目が丸い」だけでなく作用の不変性です。開放系や外部駆動では、含めなかった外界へ保存量が流出できます。

- 前：[停留作用](01_stationary_action.md)
- 次：[Hamiltonian](../part04_gateway_to_qm/01_legendre_transform_and_hamiltonian.md)
- 親：[part03](README.md)

## 参考資料

Noether (1918), *Invariante Variationsprobleme*.
