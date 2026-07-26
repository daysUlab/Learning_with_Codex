# 自由度・一般化座標・拘束

## 問い

物体の位置を三成分で書けても、三成分が独立とは限りません。拘束を満たすconfigurationを最小個数の変数でどう表すかを学びます。

三次元の粒子が曲面

$$
f(x,y,z,t)=0
$$

上に拘束されれば、独立な自由度は通常二つです。一般化座標

$$
q_1,\ldots,q_s
$$

で

$$
\mathbf r_a=\mathbf r_a(q_1,\ldots,q_s,t)
$$

と表します。距離一定の二重振り子ならCartesian座標四つに拘束二本があり、角度二つで十分です。

## holonomicとnonholonomic

- holonomic拘束：座標と時刻の等式に積分できる。
- scleronomous：拘束式に時刻が陽に現れない。
- nonholonomic：速度を含み、座標だけの等式へ一般に積分できない。

転がり条件は接触の仕方によりnonholonomicとなります。座標を減らせない場合はLagrange未定乗数を使います。

## 速度と運動エネルギー

$$
\dot{\mathbf r}_a=\sum_i\frac{\partial\mathbf r_a}{\partial q_i}\dot q_i+\frac{\partial\mathbf r_a}{\partial t}
$$

したがって曲線座標では運動エネルギーに座標依存係数や交差項が現れます。これは架空の力を追加したのではなく、Euclid空間の距離を別座標で書いた結果です。

## 数値例：円周上の粒子

半径を

$$
R=0.50\ \mathrm{m}
$$

とし、座標を角度とすれば

$$
x=R\cos\theta,\quad y=R\sin\theta,\quad T=\frac12mR^2\dot\theta^2
$$

です。半径方向の拘束力を求めないなら角度一本で完結します。

## 演習と全解答

1. 自由な三粒子の自由度を答えよ。
   **解答**：三次元なら
   $$
   3\times3=9
   $$
2. 剛体の自由度を答えよ。
   **解答**：並進三、回転三で通常六です。
3. 球面上の一粒子の自由度は何か。
   **解答**：拘束一本なので二です。
4. 振り子に角度を使う利点は何か。
   **解答**：糸長一定を恒等的に満たし、張力を運動方程式から除けます。
5. 時間依存する支持点はscleronomousか。
   **解答**：いいえ。拘束式に時刻が陽に現れます。
6. 円周上で
   $$
   m=2.0\ \mathrm{kg},\ R=0.50\ \mathrm{m},\ \dot\theta=4.0\ \mathrm{s^{-1}}
   $$
   の運動エネルギーを求めよ。
   **解答**：
   $$
   T=\frac12(2.0)(0.50)^2(4.0)^2=4.0\ \mathrm{J}
   $$

## 適用範囲・接続

座標選択は拘束を簡単にしますが、非理想拘束や摩擦まで自動的に消しません。次ページで仮想仕事を使い、理想拘束力が一般化方程式に仕事をしない条件を示します。

- 前：[三形式比較](01_newton_lagrange_hamilton_comparison.md)
- 次：[仮想仕事](../part02_basics/01_virtual_work_and_euler_lagrange.md)
- 親：[part01](README.md)

## 参考資料

Landau & Lifshitz, *Mechanics*, §1–2.
