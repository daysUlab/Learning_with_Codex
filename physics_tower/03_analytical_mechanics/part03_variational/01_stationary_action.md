# 停留作用：軌道全体から運動方程式を得る

## 問い

各時刻の力を追わず、経路全体へ一つの条件を課して運動方程式を得られるでしょうか。

作用を

$$
S[q]=\int_{t_1}^{t_2}L(q,\dot q,t)\,dt
$$

と定義します。端点を固定した変分

$$
q(t)\to q(t)+\varepsilon\eta(t),\qquad \eta(t_1)=\eta(t_2)=0
$$

を考えると

$$
\delta S=\int_{t_1}^{t_2}\left(
\frac{\partial L}{\partial q}\eta+
\frac{\partial L}{\partial\dot q}\dot\eta
\right)dt
$$

です。第二項を部分積分し、境界項が消えるので

$$
\delta S=\int_{t_1}^{t_2}
\left[
\frac{\partial L}{\partial q}-
\frac{d}{dt}\frac{\partial L}{\partial\dot q}
\right]\eta\,dt
$$

任意の

$$
\eta
$$

に対して停留する条件からEuler–Lagrange方程式が出ます。

## 「最小」ではなく「停留」

実軌道の作用は局所最小、最大、鞍点のいずれでもあり得ます。したがって最小作用より停留作用が正確です。作用へ全時間微分

$$
\frac{dF(q,t)}{dt}
$$

を加えても、固定端では境界値しか変わらず運動方程式は同じです。

## 演習と全解答

1. なぜ端点を固定するか。
   **解答**：部分積分の境界項を消し、同じ始点・終点を結ぶ経路を比較するためです。
2. 自由粒子で式を出せ。
   **解答**：
   $$
   L=\frac12m\dot x^2\Rightarrow \frac d{dt}(m\dot x)=0
   $$
3. potentialを含めよ。
   **解答**：
   $$
   L=\frac12m\dot x^2-V(x)\Rightarrow m\ddot x=-V'(x)
   $$
4. actionのSI単位は何か。
   **解答**：
   $$
   \mathrm{J\,s}
   $$
5. 全微分を加えると作用はどう変わるか。
   **解答**：
   $$
   S\to S+F(q_2,t_2)-F(q_1,t_1)
   $$
6. 経路積分と同じものか。
   **解答**：古典では停留経路を選ぶ原理です。量子の経路積分は全経路へphaseを割り当てるため、本章では予告に留めます。

## 適用範囲・接続

nonconservativeな散逸を通常の

$$
T-V
$$

だけで表せない場合があります。場では座標の代わりにfieldを変分します。

- 前：[比較例](../part02_basics/04_central_force_and_rotating_systems.md)
- 次：[Noether](02_symmetry_cyclic_noether.md)
- 親：[part03](README.md)

## 参考資料

Lanczos, *The Variational Principles of Mechanics*.
